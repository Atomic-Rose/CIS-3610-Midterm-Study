# CIS 3610 Midterm Study Studio

An offline adaptation of the neighboring `cis4100-practice` app, retaining its Ink & Signal theme and study workflow.

**Open [index.html](index.html) in your browser.** No installation, server, account, or internet connection is needed. The HTML file contains the fonts, styles, code, and question data, so you can copy it alone to another computer.

## Included material

| Domain | Subject | Multiple choice | Written prompts |
| --- | --- | ---: | ---: |
| 1 | E-business infrastructure & web fundamentals | 20 | 2 |
| 2 | UI scaffolding, semantic HTML & accessibility | 20 | 2 |
| 3 | Client-side logic, JavaScript & debugging | 20 | 2 |
| 4 | Databases, backend routing & security | 20 | 2 |
| 5 | Version control, workflow hygiene & capstone governance | 20 | 2 |

All 100 multiple-choice stems and A–D options and all 10 written prompts come from the supplied review, saved in `Resources/midterm-review.txt`. Missing HTML tags in questions 21, 28, 33, and 39 were restored from context. IDs `Q001`–`Q100` follow the original order; `E01`–`E10` identify written prompts.

The answers, explanations, and essay outlines are authored study aids. No instructor answer key or grading rubric was supplied. Source Notes explains qualifications to simplified wording and links to optional technical references. The original options are preserved, including the repeated A answer pattern in Domains 4 and 5.

## Study workflow

- **Practice:** mixed questions, one domain, one topic, or the complete bank. Choose an answer, then **Check** to reveal feedback.
- **Test:** six repeatable mock tests or a new random test. Customize length, immediate/deferred feedback, and an optional timer. Saved mocks use up to 40 questions, limited to the selected pool. Each test has no repeated questions; different tests may overlap.
- **Review:** missed questions or a cram session prioritized by weak topics.
- **Written practice:** draft a response, reveal the study outline and example, then mark your confidence. Written responses are self-assessed and do not affect quiz scores.
- **Progress & history:** first-attempt scores, retries, topic performance, flagged questions, session results, and JSON backup/import.

Question sessions support **A/B/C/D** to select, **Enter** to check or continue, **N/P** to navigate, **S** to skip, **R** to flag, **G** to open the navigator, and **Esc** to close it. Shortcuts do not intercept typing in form fields. Keyboard Tab navigation and mouse/touch controls also work.

Choose System, Light, or Dark in the header. On mobile, the theme icon cycles through these choices.

## Progress and privacy

Progress and written drafts save to local browser storage. **Save & exit** preserves an unfinished quiz; **Resume** returns to it. The CIS 3610 storage key is separate from CIS 4100 progress. Theme preference is shared with the original app.

Storage can depend on the browser and file location. Export progress before moving files, switching browsers/devices, or clearing browser data. Imports validate the data and ask before replacing progress. Reset requires confirmation. The timer continues while away and finalizes expired work when the app next runs. Skipped and unanswered questions count as incorrect when a session is finalized.

## Development

Editable sources:

- `app-shell.html`: application template.
- `question-bank.json`, `essay-bank.json`, `source-notes.json`: readable content.
- `tools/build_bank.py`, `tools/essay-outlines.json`: review parser, authored key/explanations, and written-response study material.
- `design/`: inherited styles and embedded fonts, with font licenses.

Rebuild using Python 3:

```sh
python3 tools/build_bank.py
python3 tools/package_app.py
```

For developer verification, install Python Playwright in a virtual environment and run `python tools/validate_app.py`. The script uses installed Google Chrome on macOS by default; set `CHROME_PATH` to another installed Chromium executable when needed. Playwright is only a development dependency.

See [VALIDATION_REPORT.md](VALIDATION_REPORT.md) for checks and limitations.
