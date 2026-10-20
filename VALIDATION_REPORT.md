# Validation report

Verified on October 19, 2026 using installed Google Chrome through Python Playwright, loading `index.html` with `file://` and browser networking disabled.

## Passed

- All 100 multiple-choice questions and 10 written prompts are included; each domain has 20 multiple-choice questions and two written prompts.
- Original multiple-choice stems and options match the supplied review except the four documented HTML-tag restorations.
- All 31 nonempty domain combinations generate deterministic, balanced mock tests without duplicate question IDs inside a test. Single-domain mocks contain 20 questions; larger mocks contain up to 40.
- A–D keyboard selection, explicit checking, correct/incorrect feedback, scoring, skips, flags, question navigation, save/exit, reload/resume, final results, and missed-question retry work.
- Written drafts and confidence survive reload; domain filters and expandable outlines work.
- JSON export includes written responses. Valid imports restore progress; invalid imports preserve existing progress. Reset works after confirmation.
- Deferred tests withhold feedback and dashboard scoring until final submission.
- An expired timer finalizes after reload.
- Light and dark themes render at 1360px and 390px widths. Home, written practice, history, source notes, and question states have no document-level horizontal overflow.
- No uncaught browser errors or external network requests occurred during the final integration run.

The checks are reproducible with `tools/validate_app.py`. Representative screenshots are in `design/screenshots/`.

## Limits

Safari, Firefox, other devices, screen readers, and a complete WCAG audit were not tested. The study key and outlines are authored aids, not an instructor-provided key or rubric. Browser storage availability varies, especially for local files and private browsing; retain exported backups.
