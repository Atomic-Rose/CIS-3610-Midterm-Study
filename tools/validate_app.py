"""Offline Chromium integration checks. Install playwright in a development venv to run."""
from pathlib import Path
import json, os, re
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
bank=json.loads((ROOT/'question-bank.json').read_text())
essays=json.loads((ROOT/'essay-bank.json').read_text())
assert len(bank)==100 and len({q['id'] for q in bank})==100
assert all(sum(q['chapter']==d for q in bank)==20 for d in range(1,6))
assert len(essays)==10 and all(sum(q['chapter']==d for q in essays)==2 for d in range(1,6))
assert all(len(q['options'])==4 and q['answer'] in 'ABCD' and q['explanation'] for q in bank)
assert all(q['points'] and q['example'] for q in essays)
# Verify source preservation, allowing only the four explicitly restored HTML-tag questions.
source=(ROOT/'Resources/midterm-review.txt').read_text()
rows=re.findall(r'([^\n]+)\n\nA\) (.*?)\n\nB\) (.*?)\n\nC\) (.*?)\n\nD\) ([^\n]+)',source,re.S)
assert len(rows)==100
for i,(stem,*options) in enumerate(rows):
    if i not in [20,27,32,38]:
        assert bank[i]['statement']==stem.strip()
        assert bank[i]['options']==options
html=(ROOT/'index.html').read_text()
assert '__BANK__' not in html and '__ESSAYS__' not in html
assert not re.search(r'<(?:script|link|img)[^>]+(?:src|href)=[\"\'](?:https?:)?//',html)
print('PASS content coverage, source preservation, standalone packaging')
errors=[];requests=[]
with sync_playwright() as p:
    executable=os.environ.get('CHROME_PATH','/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
    browser=p.chromium.launch(executable_path=executable,headless=True)
    ctx=browser.new_context(offline=True,accept_downloads=True,viewport={'width':1360,'height':1000})
    page=ctx.new_page();page.on('pageerror',lambda e:errors.append(e.stack))
    page.on('request',lambda r:requests.append(r.url))
    page.goto((ROOT/'index.html').as_uri())
    assert page.locator('#hero-title').inner_text()=='Start with Domains 1–5'
    # All 31 domain scopes: six unique-in-attempt, balanced, deterministic mocks.
    assert page.evaluate('''()=>{for(let mask=1;mask<32;mask++){
      const cs=[1,2,3,4,5].filter(c=>mask&(1<<(c-1))),tests=savedTests(cs);
      if(JSON.stringify(tests)!==JSON.stringify(savedTests(cs)))return false;
      for(const ids of tests){if(ids.length!==Math.min(40,cs.length*20)||new Set(ids).size!==ids.length)return false;
       const counts=cs.map(c=>ids.filter(id=>BY_ID.get(id).chapter===c).length);
       if(Math.max(...counts)-Math.min(...counts)>1)return false;
       if(ids.some(id=>!cs.includes(BY_ID.get(id).chapter)))return false;
      }}return true}''')
    print('PASS deterministic balanced mocks for all 31 domain scopes')
    page.click('#hero-start');assert page.locator('.answer').count()==4
    assert page.locator('#primary').is_disabled()
    correct=page.evaluate('BY_ID.get(state.active.ids[0]).answer')
    page.keyboard.press(correct.lower())
    assert page.locator(f'#answer-{correct}').get_attribute('aria-pressed')=='true'
    assert page.locator('.feedback').count()==0
    page.click('#primary');assert page.locator('.feedback h3').inner_text()=='Correct'
    assert page.locator('.answer.is-correct').count()==1
    assert page.evaluate('overallStats().correct')==1
    page.click('#primary');page.click('#flag')
    page.click('#pause');page.reload();page.click('#resume')
    assert page.locator('#flag').get_attribute('aria-pressed')=='true'
    page.click('#skip');page.click('#open-nav')
    page.locator('[data-jump="1"]').click()
    wrong=page.evaluate("'ABCD'.split('').find(x=>x!==BY_ID.get(state.active.ids[1]).answer)")
    page.click(f'#answer-{wrong}');page.click('#primary')
    assert 'Incorrect' in page.locator('.feedback h3').inner_text()
    page.click('#open-nav');page.click('#finish');page.click('#confirm-finish')
    assert page.locator('.results-score').count()==1
    assert page.evaluate('state.history.length')==1
    page.click('#retry-missed');assert page.evaluate('state.active.ids.length')==19
    page.click('#pause')
    print('PASS keyboard choice, explicit check, scoring, wrong answers, skips, flags, save/resume, results, retry')
    page.click('[data-view="essays"]');assert page.locator('.essay-card').count()==10
    page.fill('#essay-E01','A headless CMS separates content delivery from presentation. <main> is literal text.')
    page.select_option('#confidence-E01','review')
    page.reload();page.click('[data-view="essays"]')
    assert page.input_value('#essay-E01').startswith('A headless CMS')
    assert page.input_value('#confidence-E01')=='review'
    page.locator('.essay-outline summary').first.click()
    assert page.locator('.essay-outline').first.get_attribute('open') is not None
    page.click('[data-essay-domain="4"]');assert page.locator('.essay-card').count()==2
    page.click('[data-view="history"]')
    with page.expect_download() as download:page.click('#export')
    exported=json.loads(Path(download.value.path()).read_text());assert exported['essays']['E01']['status']=='review'
    assert page.evaluate('validateState(JSON.parse(JSON.stringify(state)))')==page.evaluate('JSON.parse(JSON.stringify(state))')
    page.on('dialog',lambda d:d.accept())
    page.set_input_files('#import',{'name':'progress.json','mimeType':'application/json','buffer':json.dumps(exported).encode()})
    assert page.locator('#toast').inner_text().startswith('Progress imported')
    page.set_input_files('#import',{'name':'bad.json','mimeType':'application/json','buffer':b'{"version": 999}'})
    assert page.locator('#toast').inner_text().startswith('Import rejected')
    assert page.evaluate('state.essays.E01.status')=='review'
    print('PASS written drafts, outlines, filters, confidence, reload, export/import, invalid import protection')
    # Reset then run a deferred test through UI.
    page.click('#reset');page.click('[data-group="test"]');page.click('#customize')
    page.select_option('#feedback-mode','deferred')
    # Single-domain mocks must shrink to 20 unique questions.
    for d in [2,3,4,5]:page.click(f'[data-chapter="{d}"]')
    assert '20 questions' in page.locator('.summary').inner_text()
    assert '${mockSize}' not in page.locator('#content').inner_text()
    page.click('#start');assert page.evaluate('state.active.ids.length')==20
    answer=page.evaluate('BY_ID.get(state.active.ids[0]).answer');page.click(f'#answer-{answer}');page.click('#primary')
    assert page.locator('.feedback').count()==0 and page.evaluate('state.active.index')==1
    assert page.evaluate('overallStats().f.length')==0
    page.click('#open-nav');page.click('#finish');page.click('#confirm-finish')
    assert page.evaluate('overallStats().correct')==1
    print('PASS deferred test, single-domain size, final grading, reset')
    page.click('#result-home');page.click('[data-group="practice"]');page.click('#customize') if page.locator('#timer-minutes').count()==0 else None
    page.fill('#timer-minutes','1');page.locator('#timer-minutes').dispatch_event('change');page.click('#start')
    page.evaluate('state.active.deadline=Date.now()-1;save()');page.reload()
    page.wait_for_function('state.active===null')
    assert page.evaluate('state.active===null')
    assert page.locator('.results-score').count()==1
    print('PASS expired timer finalizes after reload')
    # Representative responsive states in both themes.
    output=ROOT/'design/screenshots';output.mkdir(parents=True,exist_ok=True)
    for width in [1360,390]:
      page.set_viewport_size({'width':width,'height':900})
      for theme in ['light','dark']:
        page.evaluate('(t)=>applyTheme(t,false)',theme)
        for view in ['home','essays','history','notes']:
          page.evaluate('(v)=>show(v)',view)
          assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),(width,theme,view)
          if view=='home':page.screenshot(path=str(output/f'{theme}-{width}-home.png'),full_page=True)
      page.evaluate("state=fresh();startIds(['Q001'],'Layout check','immediate')")
      assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
      page.screenshot(path=str(output/f'question-{width}.png'),full_page=True)
      page.click('#answer-B');page.click('#primary')
      assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
    print('PASS light/dark desktop/mobile layouts without horizontal overflow')
    assert not errors,errors
    assert all(url.startswith('file:') or url.startswith('data:') for url in requests),requests
    browser.close()
print('PASS no uncaught browser errors or network requests')
