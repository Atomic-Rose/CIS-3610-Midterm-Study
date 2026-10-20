"""Build the self-contained offline app from its editable source files."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
s=(ROOT/'app-shell.html').read_text()
for marker,path in [('/*FONTS*/','design/ink-signal/fonts.css'),('/*TOKENS*/','design/ink-signal/tokens.css'),('/*COMPONENTS*/','design/ink-signal/components.css'),('/*APP*/','design/study-studio.css')]:
    assert s.count(marker)==1
    s=s.replace(marker,(ROOT/path).read_text())
for marker,path in [('__BANK__','question-bank.json'),('__ESSAYS__','essay-bank.json'),('__NOTES__','source-notes.json')]:
    assert s.count(marker)==1
    s=s.replace(marker,json.dumps(json.loads((ROOT/path).read_text()),ensure_ascii=False).replace('</',r'<\/'))
(ROOT/'index.html').write_text(s)
print('Built standalone index.html')
