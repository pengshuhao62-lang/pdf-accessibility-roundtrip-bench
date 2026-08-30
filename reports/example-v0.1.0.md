# PDF Accessibility Roundtrip Bench report

- Run ID: `20260830T124612Z-9f176d1d`
- Started: `2026-08-30T12:46:12+00:00`
- Ended: `2026-08-30T13:22:16+00:00`
- Profiles: `ua1, ua2`
- Tools: `qpdf, pymupdf, ghostscript`
- Operations: `merge, split, resave`

## Summary

| Classification | Cases |
| --- | ---: |
| `baseline_invalid` | 0 |
| `tool_unavailable` | 0 |
| `transformation_failed` | 0 |
| `output_unreadable` | 0 |
| `new_pdfua_violation` | 140 |
| `structure_signal_changed` | 0 |
| `passed` | 40 |
| `manual_review` | 0 |
| **Total** | **180** |

## Compatibility matrix

| Profile | Tool | Operation | Total | Passed | New PDF/UA violations | Other |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| `ua1` | `ghostscript` | `merge` | 15 | 0 | 15 | 0 |
| `ua1` | `ghostscript` | `resave` | 15 | 0 | 15 | 0 |
| `ua1` | `ghostscript` | `split` | 15 | 0 | 15 | 0 |
| `ua1` | `pymupdf` | `merge` | 15 | 0 | 15 | 0 |
| `ua1` | `pymupdf` | `resave` | 15 | 15 | 0 | 0 |
| `ua1` | `pymupdf` | `split` | 15 | 0 | 15 | 0 |
| `ua1` | `qpdf` | `merge` | 15 | 0 | 15 | 0 |
| `ua1` | `qpdf` | `resave` | 15 | 15 | 0 | 0 |
| `ua1` | `qpdf` | `split` | 15 | 0 | 15 | 0 |
| `ua2` | `ghostscript` | `merge` | 5 | 0 | 5 | 0 |
| `ua2` | `ghostscript` | `resave` | 5 | 0 | 5 | 0 |
| `ua2` | `ghostscript` | `split` | 5 | 0 | 5 | 0 |
| `ua2` | `pymupdf` | `merge` | 5 | 0 | 5 | 0 |
| `ua2` | `pymupdf` | `resave` | 5 | 5 | 0 | 0 |
| `ua2` | `pymupdf` | `split` | 5 | 0 | 5 | 0 |
| `ua2` | `qpdf` | `merge` | 5 | 0 | 5 | 0 |
| `ua2` | `qpdf` | `resave` | 5 | 5 | 0 | 0 |
| `ua2` | `qpdf` | `split` | 5 | 0 | 5 | 0 |

## Environment

| Field | Value |
| --- | --- |
| `architecture` | `arm64` |
| `ghostscript` | `available` |
| `os` | `Darwin` |
| `os_version` | `15.5` |
| `python` | `3.9.6` |
| `qpdf` | `available` |
| `tool_root` | `isolated-external-ssd-toolchain` |
| `verapdf` | `available` |

## Tool versions

| Tool | Version |
| --- | --- |
| `ghostscript` | `10.07.1` |
| `pymupdf` | `1.26.5` |
| `qpdf` | `qpdf version 12.3.2` |
| `verapdf` | `veraPDF 1.30.2` |

## Cases

| Fixture | Profile | Tool | Operation | Classification |
| --- | --- | --- | --- | --- |
| `ua1-ref-2-01-magazine-danish` | `ua1` | `qpdf` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-01-magazine-danish` | `ua1` | `qpdf` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-01-magazine-danish` | `ua1` | `qpdf` | `resave` | `passed` |
| `ua1-ref-2-01-magazine-danish` | `ua1` | `pymupdf` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-01-magazine-danish` | `ua1` | `pymupdf` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-01-magazine-danish` | `ua1` | `pymupdf` | `resave` | `passed` |
| `ua1-ref-2-01-magazine-danish` | `ua1` | `ghostscript` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-01-magazine-danish` | `ua1` | `ghostscript` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-01-magazine-danish` | `ua1` | `ghostscript` | `resave` | `new_pdfua_violation` |
| `ua1-ref-2-02-invoice` | `ua1` | `qpdf` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-02-invoice` | `ua1` | `qpdf` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-02-invoice` | `ua1` | `qpdf` | `resave` | `passed` |
| `ua1-ref-2-02-invoice` | `ua1` | `pymupdf` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-02-invoice` | `ua1` | `pymupdf` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-02-invoice` | `ua1` | `pymupdf` | `resave` | `passed` |
| `ua1-ref-2-02-invoice` | `ua1` | `ghostscript` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-02-invoice` | `ua1` | `ghostscript` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-02-invoice` | `ua1` | `ghostscript` | `resave` | `new_pdfua_violation` |
| `ua1-ref-2-03-academicabstract` | `ua1` | `qpdf` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-03-academicabstract` | `ua1` | `qpdf` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-03-academicabstract` | `ua1` | `qpdf` | `resave` | `passed` |
| `ua1-ref-2-03-academicabstract` | `ua1` | `pymupdf` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-03-academicabstract` | `ua1` | `pymupdf` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-03-academicabstract` | `ua1` | `pymupdf` | `resave` | `passed` |
| `ua1-ref-2-03-academicabstract` | `ua1` | `ghostscript` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-03-academicabstract` | `ua1` | `ghostscript` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-03-academicabstract` | `ua1` | `ghostscript` | `resave` | `new_pdfua_violation` |
| `ua1-ref-2-04-presentation` | `ua1` | `qpdf` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-04-presentation` | `ua1` | `qpdf` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-04-presentation` | `ua1` | `qpdf` | `resave` | `passed` |
| `ua1-ref-2-04-presentation` | `ua1` | `pymupdf` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-04-presentation` | `ua1` | `pymupdf` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-04-presentation` | `ua1` | `pymupdf` | `resave` | `passed` |
| `ua1-ref-2-04-presentation` | `ua1` | `ghostscript` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-04-presentation` | `ua1` | `ghostscript` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-04-presentation` | `ua1` | `ghostscript` | `resave` | `new_pdfua_violation` |
| `ua1-ref-2-05-bookchapter-german` | `ua1` | `qpdf` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-05-bookchapter-german` | `ua1` | `qpdf` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-05-bookchapter-german` | `ua1` | `qpdf` | `resave` | `passed` |
| `ua1-ref-2-05-bookchapter-german` | `ua1` | `pymupdf` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-05-bookchapter-german` | `ua1` | `pymupdf` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-05-bookchapter-german` | `ua1` | `pymupdf` | `resave` | `passed` |
| `ua1-ref-2-05-bookchapter-german` | `ua1` | `ghostscript` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-05-bookchapter-german` | `ua1` | `ghostscript` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-05-bookchapter-german` | `ua1` | `ghostscript` | `resave` | `new_pdfua_violation` |
| `ua1-ref-2-06-brochure` | `ua1` | `qpdf` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-06-brochure` | `ua1` | `qpdf` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-06-brochure` | `ua1` | `qpdf` | `resave` | `passed` |
| `ua1-ref-2-06-brochure` | `ua1` | `pymupdf` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-06-brochure` | `ua1` | `pymupdf` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-06-brochure` | `ua1` | `pymupdf` | `resave` | `passed` |
| `ua1-ref-2-06-brochure` | `ua1` | `ghostscript` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-06-brochure` | `ua1` | `ghostscript` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-06-brochure` | `ua1` | `ghostscript` | `resave` | `new_pdfua_violation` |
| `ua1-ref-2-08-bookchapter` | `ua1` | `qpdf` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-08-bookchapter` | `ua1` | `qpdf` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-08-bookchapter` | `ua1` | `qpdf` | `resave` | `passed` |
| `ua1-ref-2-08-bookchapter` | `ua1` | `pymupdf` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-08-bookchapter` | `ua1` | `pymupdf` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-08-bookchapter` | `ua1` | `pymupdf` | `resave` | `passed` |
| `ua1-ref-2-08-bookchapter` | `ua1` | `ghostscript` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-08-bookchapter` | `ua1` | `ghostscript` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-08-bookchapter` | `ua1` | `ghostscript` | `resave` | `new_pdfua_violation` |
| `ua1-ref-2-09-scanned` | `ua1` | `qpdf` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-09-scanned` | `ua1` | `qpdf` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-09-scanned` | `ua1` | `qpdf` | `resave` | `passed` |
| `ua1-ref-2-09-scanned` | `ua1` | `pymupdf` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-09-scanned` | `ua1` | `pymupdf` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-09-scanned` | `ua1` | `pymupdf` | `resave` | `passed` |
| `ua1-ref-2-09-scanned` | `ua1` | `ghostscript` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-09-scanned` | `ua1` | `ghostscript` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-09-scanned` | `ua1` | `ghostscript` | `resave` | `new_pdfua_violation` |
| `ua1-ref-2-10-form` | `ua1` | `qpdf` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-10-form` | `ua1` | `qpdf` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-10-form` | `ua1` | `qpdf` | `resave` | `passed` |
| `ua1-ref-2-10-form` | `ua1` | `pymupdf` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-10-form` | `ua1` | `pymupdf` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-10-form` | `ua1` | `pymupdf` | `resave` | `passed` |
| `ua1-ref-2-10-form` | `ua1` | `ghostscript` | `merge` | `new_pdfua_violation` |
| `ua1-ref-2-10-form` | `ua1` | `ghostscript` | `split` | `new_pdfua_violation` |
| `ua1-ref-2-10-form` | `ua1` | `ghostscript` | `resave` | `new_pdfua_violation` |
| `ua1-heading-001` | `ua1` | `qpdf` | `merge` | `new_pdfua_violation` |
| `ua1-heading-001` | `ua1` | `qpdf` | `split` | `new_pdfua_violation` |
| `ua1-heading-001` | `ua1` | `qpdf` | `resave` | `passed` |
| `ua1-heading-001` | `ua1` | `pymupdf` | `merge` | `new_pdfua_violation` |
| `ua1-heading-001` | `ua1` | `pymupdf` | `split` | `new_pdfua_violation` |
| `ua1-heading-001` | `ua1` | `pymupdf` | `resave` | `passed` |
| `ua1-heading-001` | `ua1` | `ghostscript` | `merge` | `new_pdfua_violation` |
| `ua1-heading-001` | `ua1` | `ghostscript` | `split` | `new_pdfua_violation` |
| `ua1-heading-001` | `ua1` | `ghostscript` | `resave` | `new_pdfua_violation` |
| `ua1-link-001` | `ua1` | `qpdf` | `merge` | `new_pdfua_violation` |
| `ua1-link-001` | `ua1` | `qpdf` | `split` | `new_pdfua_violation` |
| `ua1-link-001` | `ua1` | `qpdf` | `resave` | `passed` |
| `ua1-link-001` | `ua1` | `pymupdf` | `merge` | `new_pdfua_violation` |
| `ua1-link-001` | `ua1` | `pymupdf` | `split` | `new_pdfua_violation` |
| `ua1-link-001` | `ua1` | `pymupdf` | `resave` | `passed` |
| `ua1-link-001` | `ua1` | `ghostscript` | `merge` | `new_pdfua_violation` |
| `ua1-link-001` | `ua1` | `ghostscript` | `split` | `new_pdfua_violation` |
| `ua1-link-001` | `ua1` | `ghostscript` | `resave` | `new_pdfua_violation` |
| `ua1-list-001` | `ua1` | `qpdf` | `merge` | `new_pdfua_violation` |
| `ua1-list-001` | `ua1` | `qpdf` | `split` | `new_pdfua_violation` |
| `ua1-list-001` | `ua1` | `qpdf` | `resave` | `passed` |
| `ua1-list-001` | `ua1` | `pymupdf` | `merge` | `new_pdfua_violation` |
| `ua1-list-001` | `ua1` | `pymupdf` | `split` | `new_pdfua_violation` |
| `ua1-list-001` | `ua1` | `pymupdf` | `resave` | `passed` |
| `ua1-list-001` | `ua1` | `ghostscript` | `merge` | `new_pdfua_violation` |
| `ua1-list-001` | `ua1` | `ghostscript` | `split` | `new_pdfua_violation` |
| `ua1-list-001` | `ua1` | `ghostscript` | `resave` | `new_pdfua_violation` |
| `ua1-paragraph-001` | `ua1` | `qpdf` | `merge` | `new_pdfua_violation` |
| `ua1-paragraph-001` | `ua1` | `qpdf` | `split` | `new_pdfua_violation` |
| `ua1-paragraph-001` | `ua1` | `qpdf` | `resave` | `passed` |
| `ua1-paragraph-001` | `ua1` | `pymupdf` | `merge` | `new_pdfua_violation` |
| `ua1-paragraph-001` | `ua1` | `pymupdf` | `split` | `new_pdfua_violation` |
| `ua1-paragraph-001` | `ua1` | `pymupdf` | `resave` | `passed` |
| `ua1-paragraph-001` | `ua1` | `ghostscript` | `merge` | `new_pdfua_violation` |
| `ua1-paragraph-001` | `ua1` | `ghostscript` | `split` | `new_pdfua_violation` |
| `ua1-paragraph-001` | `ua1` | `ghostscript` | `resave` | `new_pdfua_violation` |
| `ua1-table-001` | `ua1` | `qpdf` | `merge` | `new_pdfua_violation` |
| `ua1-table-001` | `ua1` | `qpdf` | `split` | `new_pdfua_violation` |
| `ua1-table-001` | `ua1` | `qpdf` | `resave` | `passed` |
| `ua1-table-001` | `ua1` | `pymupdf` | `merge` | `new_pdfua_violation` |
| `ua1-table-001` | `ua1` | `pymupdf` | `split` | `new_pdfua_violation` |
| `ua1-table-001` | `ua1` | `pymupdf` | `resave` | `passed` |
| `ua1-table-001` | `ua1` | `ghostscript` | `merge` | `new_pdfua_violation` |
| `ua1-table-001` | `ua1` | `ghostscript` | `split` | `new_pdfua_violation` |
| `ua1-table-001` | `ua1` | `ghostscript` | `resave` | `new_pdfua_violation` |
| `ua1-unicode-001` | `ua1` | `qpdf` | `merge` | `new_pdfua_violation` |
| `ua1-unicode-001` | `ua1` | `qpdf` | `split` | `new_pdfua_violation` |
| `ua1-unicode-001` | `ua1` | `qpdf` | `resave` | `passed` |
| `ua1-unicode-001` | `ua1` | `pymupdf` | `merge` | `new_pdfua_violation` |
| `ua1-unicode-001` | `ua1` | `pymupdf` | `split` | `new_pdfua_violation` |
| `ua1-unicode-001` | `ua1` | `pymupdf` | `resave` | `passed` |
| `ua1-unicode-001` | `ua1` | `ghostscript` | `merge` | `new_pdfua_violation` |
| `ua1-unicode-001` | `ua1` | `ghostscript` | `split` | `new_pdfua_violation` |
| `ua1-unicode-001` | `ua1` | `ghostscript` | `resave` | `new_pdfua_violation` |
| `ua2-heading-001` | `ua2` | `qpdf` | `merge` | `new_pdfua_violation` |
| `ua2-heading-001` | `ua2` | `qpdf` | `split` | `new_pdfua_violation` |
| `ua2-heading-001` | `ua2` | `qpdf` | `resave` | `passed` |
| `ua2-heading-001` | `ua2` | `pymupdf` | `merge` | `new_pdfua_violation` |
| `ua2-heading-001` | `ua2` | `pymupdf` | `split` | `new_pdfua_violation` |
| `ua2-heading-001` | `ua2` | `pymupdf` | `resave` | `passed` |
| `ua2-heading-001` | `ua2` | `ghostscript` | `merge` | `new_pdfua_violation` |
| `ua2-heading-001` | `ua2` | `ghostscript` | `split` | `new_pdfua_violation` |
| `ua2-heading-001` | `ua2` | `ghostscript` | `resave` | `new_pdfua_violation` |
| `ua2-link-001` | `ua2` | `qpdf` | `merge` | `new_pdfua_violation` |
| `ua2-link-001` | `ua2` | `qpdf` | `split` | `new_pdfua_violation` |
| `ua2-link-001` | `ua2` | `qpdf` | `resave` | `passed` |
| `ua2-link-001` | `ua2` | `pymupdf` | `merge` | `new_pdfua_violation` |
| `ua2-link-001` | `ua2` | `pymupdf` | `split` | `new_pdfua_violation` |
| `ua2-link-001` | `ua2` | `pymupdf` | `resave` | `passed` |
| `ua2-link-001` | `ua2` | `ghostscript` | `merge` | `new_pdfua_violation` |
| `ua2-link-001` | `ua2` | `ghostscript` | `split` | `new_pdfua_violation` |
| `ua2-link-001` | `ua2` | `ghostscript` | `resave` | `new_pdfua_violation` |
| `ua2-paragraph-001` | `ua2` | `qpdf` | `merge` | `new_pdfua_violation` |
| `ua2-paragraph-001` | `ua2` | `qpdf` | `split` | `new_pdfua_violation` |
| `ua2-paragraph-001` | `ua2` | `qpdf` | `resave` | `passed` |
| `ua2-paragraph-001` | `ua2` | `pymupdf` | `merge` | `new_pdfua_violation` |
| `ua2-paragraph-001` | `ua2` | `pymupdf` | `split` | `new_pdfua_violation` |
| `ua2-paragraph-001` | `ua2` | `pymupdf` | `resave` | `passed` |
| `ua2-paragraph-001` | `ua2` | `ghostscript` | `merge` | `new_pdfua_violation` |
| `ua2-paragraph-001` | `ua2` | `ghostscript` | `split` | `new_pdfua_violation` |
| `ua2-paragraph-001` | `ua2` | `ghostscript` | `resave` | `new_pdfua_violation` |
| `ua2-table-001` | `ua2` | `qpdf` | `merge` | `new_pdfua_violation` |
| `ua2-table-001` | `ua2` | `qpdf` | `split` | `new_pdfua_violation` |
| `ua2-table-001` | `ua2` | `qpdf` | `resave` | `passed` |
| `ua2-table-001` | `ua2` | `pymupdf` | `merge` | `new_pdfua_violation` |
| `ua2-table-001` | `ua2` | `pymupdf` | `split` | `new_pdfua_violation` |
| `ua2-table-001` | `ua2` | `pymupdf` | `resave` | `passed` |
| `ua2-table-001` | `ua2` | `ghostscript` | `merge` | `new_pdfua_violation` |
| `ua2-table-001` | `ua2` | `ghostscript` | `split` | `new_pdfua_violation` |
| `ua2-table-001` | `ua2` | `ghostscript` | `resave` | `new_pdfua_violation` |
| `ua2-unicode-001` | `ua2` | `qpdf` | `merge` | `new_pdfua_violation` |
| `ua2-unicode-001` | `ua2` | `qpdf` | `split` | `new_pdfua_violation` |
| `ua2-unicode-001` | `ua2` | `qpdf` | `resave` | `passed` |
| `ua2-unicode-001` | `ua2` | `pymupdf` | `merge` | `new_pdfua_violation` |
| `ua2-unicode-001` | `ua2` | `pymupdf` | `split` | `new_pdfua_violation` |
| `ua2-unicode-001` | `ua2` | `pymupdf` | `resave` | `passed` |
| `ua2-unicode-001` | `ua2` | `ghostscript` | `merge` | `new_pdfua_violation` |
| `ua2-unicode-001` | `ua2` | `ghostscript` | `split` | `new_pdfua_violation` |
| `ua2-unicode-001` | `ua2` | `ghostscript` | `resave` | `new_pdfua_violation` |

## Interpretation

This report covers machine-verifiable PDF/UA checks and limited structural signals. It is not a complete manual screen-reader accessibility assessment.
