"""Check browser-local progress isolation against a running HTTP(S) deployment."""
import os, sys
from playwright.sync_api import sync_playwright
url=sys.argv[1] if len(sys.argv)>1 else 'http://127.0.0.1:8766/'
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path=os.environ.get('CHROME_PATH','/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'),headless=True)
    a=browser.new_context();b=browser.new_context()
    first=a.new_page();second=b.new_page();errors=[];writes=[]
    for page in [first,second]:
        page.on('pageerror',lambda error:errors.append(str(error)))
        page.on('request',lambda request:writes.append(request.url) if request.method not in ['GET','HEAD'] else None)
        response=page.goto(url)
        assert response.status==200
    first.click('#hero-start')
    answer=first.evaluate('BY_ID.get(state.active.ids[0]).answer')
    first.click('#answer-'+answer);first.click('#primary');first.click('#pause')
    first.click('[data-view="essays"]');first.fill('#essay-E01','This draft belongs only to browser A.')
    first.click('[data-view="cards"]');first.click('#fc-flip');first.click('#fc-known')
    first.reload()
    assert first.evaluate('overallStats().correct')==1
    assert first.evaluate('state.essays.E01.text')=='This draft belongs only to browser A.'
    assert first.evaluate('state.cards.Q001')=='known'
    second.reload()
    assert second.evaluate('overallStats().f.length')==0
    assert second.evaluate('state.active===null && Object.keys(state.essays).length===0 && Object.keys(state.cards).length===0')
    second.click('[data-view="essays"]');second.fill('#essay-E01','Independent browser B draft.')
    second.reload();assert second.evaluate('state.essays.E01.text')=='Independent browser B draft.'
    first.reload();assert first.evaluate('state.essays.E01.text')=='This draft belongs only to browser A.'
    assert not errors,errors
    assert not writes,writes
    browser.close()
print('PASS: quiz progress, written drafts, and flashcard marks persist per browser and stay independent; no uploads or browser errors.')
