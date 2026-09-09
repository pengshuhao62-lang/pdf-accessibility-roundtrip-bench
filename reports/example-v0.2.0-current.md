# PDF Accessibility Roundtrip Bench report

- Run ID: `20260909T030924Z-fbcdcf7e`
- Started: `2026-09-09T03:09:24+00:00`
- Ended: `2026-09-09T03:29:29+00:00`
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
| `java` | `openjdk version &quot;17.0.18&quot; 2026-01-20 LTS \| OpenJDK Runtime Environment Zulu17.64+17-CA (build 17.0.18+8-LTS) \| OpenJDK 64-Bit Server VM Zulu17.64+17-CA (build 17.0.18+8-LTS, mixed mode, sharing)` |
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


## Diagnostics and reproduction

### ua1-ref-2-01-magazine-danish-qpdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 82 → 0
- role_map_count: 1 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 73 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-ref-2-01-magazine-danish --output lab/reproduction.json
```

### ua1-ref-2-01-magazine-danish-qpdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.1-8
- Output 2: PDF/UA rule 7.18.5-1
- Output 2: PDF/UA rule 7.2-24
- Output 2: PDF/UA rule 7.2-30
- Output 2: PDF/UA rule 7.2-33
- Output 2: PDF/UA rule 7.2-34
- Output 3: PDF/UA rule 6.2-1
- Output 3: PDF/UA rule 7.1-10
- Output 3: PDF/UA rule 7.1-11
- Output 3: PDF/UA rule 7.1-3
- Output 3: PDF/UA rule 7.1-8
- Output 3: PDF/UA rule 7.18.5-1
- Output 3: PDF/UA rule 7.2-24
- Output 3: PDF/UA rule 7.2-33
- Output 3: PDF/UA rule 7.2-34
- Output 4: PDF/UA rule 6.2-1
- Output 4: PDF/UA rule 7.1-10
- Output 4: PDF/UA rule 7.1-11
- Output 4: PDF/UA rule 7.1-3
- Output 4: PDF/UA rule 7.1-8
- Output 4: PDF/UA rule 7.2-33
- Output 4: PDF/UA rule 7.2-34
- Output 5: PDF/UA rule 6.2-1
- Output 5: PDF/UA rule 7.1-10
- Output 5: PDF/UA rule 7.1-11
- Output 5: PDF/UA rule 7.1-3
- Output 5: PDF/UA rule 7.1-8
- Output 5: PDF/UA rule 7.2-33
- Output 5: PDF/UA rule 7.2-34
- Output 6: PDF/UA rule 6.2-1
- Output 6: PDF/UA rule 7.1-10
- Output 6: PDF/UA rule 7.1-11
- Output 6: PDF/UA rule 7.1-3
- Output 6: PDF/UA rule 7.1-8
- Output 6: PDF/UA rule 7.2-34
- Output 7: PDF/UA rule 6.2-1
- Output 7: PDF/UA rule 7.1-10
- Output 7: PDF/UA rule 7.1-11
- Output 7: PDF/UA rule 7.1-3
- Output 7: PDF/UA rule 7.1-8
- Output 7: PDF/UA rule 7.18.5-1
- Output 7: PDF/UA rule 7.2-24
- Output 7: PDF/UA rule 7.2-33
- Output 7: PDF/UA rule 7.2-34
- Output 8: PDF/UA rule 6.2-1
- Output 8: PDF/UA rule 7.1-10
- Output 8: PDF/UA rule 7.1-11
- Output 8: PDF/UA rule 7.1-3
- Output 8: PDF/UA rule 7.1-8
- Output 8: PDF/UA rule 7.2-33
- Output 8: PDF/UA rule 7.2-34
- Output 9: PDF/UA rule 6.2-1
- Output 9: PDF/UA rule 7.1-10
- Output 9: PDF/UA rule 7.1-11
- Output 9: PDF/UA rule 7.1-3
- Output 9: PDF/UA rule 7.1-8
- Output 9: PDF/UA rule 7.2-33
- Output 9: PDF/UA rule 7.2-34
- Output 10: PDF/UA rule 6.2-1
- Output 10: PDF/UA rule 7.1-10
- Output 10: PDF/UA rule 7.1-11
- Output 10: PDF/UA rule 7.1-3
- Output 10: PDF/UA rule 7.1-8
- Output 10: PDF/UA rule 7.18.5-1
- Output 10: PDF/UA rule 7.2-24
- Output 10: PDF/UA rule 7.2-33
- Output 10: PDF/UA rule 7.2-34
- Output 11: PDF/UA rule 6.2-1
- Output 11: PDF/UA rule 7.1-10
- Output 11: PDF/UA rule 7.1-11
- Output 11: PDF/UA rule 7.1-3
- Output 11: PDF/UA rule 7.1-8
- Output 11: PDF/UA rule 7.2-34
- Output 12: PDF/UA rule 6.2-1
- Output 12: PDF/UA rule 7.1-10
- Output 12: PDF/UA rule 7.1-11
- Output 12: PDF/UA rule 7.1-3
- Output 12: PDF/UA rule 7.1-8
- Output 12: PDF/UA rule 7.2-33
- Output 12: PDF/UA rule 7.2-34
- Output 13: PDF/UA rule 6.2-1
- Output 13: PDF/UA rule 7.1-10
- Output 13: PDF/UA rule 7.1-11
- Output 13: PDF/UA rule 7.1-3
- Output 13: PDF/UA rule 7.1-8
- Output 13: PDF/UA rule 7.2-33
- Output 13: PDF/UA rule 7.2-34
- Output 14: PDF/UA rule 6.2-1
- Output 14: PDF/UA rule 7.1-10
- Output 14: PDF/UA rule 7.1-11
- Output 14: PDF/UA rule 7.1-3
- Output 14: PDF/UA rule 7.1-8
- Output 14: PDF/UA rule 7.2-33
- Output 14: PDF/UA rule 7.2-34
- Output 15: PDF/UA rule 6.2-1
- Output 15: PDF/UA rule 7.1-10
- Output 15: PDF/UA rule 7.1-11
- Output 15: PDF/UA rule 7.1-3
- Output 15: PDF/UA rule 7.1-8
- Output 15: PDF/UA rule 7.2-34
- Output 16: PDF/UA rule 6.2-1
- Output 16: PDF/UA rule 7.1-10
- Output 16: PDF/UA rule 7.1-11
- Output 16: PDF/UA rule 7.1-3
- Output 16: PDF/UA rule 7.1-8
- Output 16: PDF/UA rule 7.2-33
- Output 16: PDF/UA rule 7.2-34
- Output 17: PDF/UA rule 6.2-1
- Output 17: PDF/UA rule 7.1-10
- Output 17: PDF/UA rule 7.1-11
- Output 17: PDF/UA rule 7.1-3
- Output 17: PDF/UA rule 7.1-8
- Output 17: PDF/UA rule 7.2-33
- Output 17: PDF/UA rule 7.2-34
- Output 18: PDF/UA rule 6.2-1
- Output 18: PDF/UA rule 7.1-10
- Output 18: PDF/UA rule 7.1-11
- Output 18: PDF/UA rule 7.1-3
- Output 18: PDF/UA rule 7.1-8
- Output 18: PDF/UA rule 7.2-33
- Output 18: PDF/UA rule 7.2-34
- Output 19: PDF/UA rule 6.2-1
- Output 19: PDF/UA rule 7.1-10
- Output 19: PDF/UA rule 7.1-11
- Output 19: PDF/UA rule 7.1-3
- Output 19: PDF/UA rule 7.1-8
- Output 19: PDF/UA rule 7.2-34
- Output 20: PDF/UA rule 6.2-1
- Output 20: PDF/UA rule 7.1-10
- Output 20: PDF/UA rule 7.1-11
- Output 20: PDF/UA rule 7.1-3
- Output 20: PDF/UA rule 7.1-8
- Output 20: PDF/UA rule 7.2-34
- Output 21: PDF/UA rule 6.2-1
- Output 21: PDF/UA rule 7.1-10
- Output 21: PDF/UA rule 7.1-11
- Output 21: PDF/UA rule 7.1-3
- Output 21: PDF/UA rule 7.1-8
- Output 21: PDF/UA rule 7.2-34
- Output 22: PDF/UA rule 6.2-1
- Output 22: PDF/UA rule 7.1-10
- Output 22: PDF/UA rule 7.1-11
- Output 22: PDF/UA rule 7.1-3
- Output 22: PDF/UA rule 7.1-8
- Output 22: PDF/UA rule 7.2-34
- Output 23: PDF/UA rule 6.2-1
- Output 23: PDF/UA rule 7.1-10
- Output 23: PDF/UA rule 7.1-11
- Output 23: PDF/UA rule 7.1-3
- Output 23: PDF/UA rule 7.1-8
- Output 23: PDF/UA rule 7.2-34
- Output 24: PDF/UA rule 6.2-1
- Output 24: PDF/UA rule 7.1-10
- Output 24: PDF/UA rule 7.1-11
- Output 24: PDF/UA rule 7.1-3
- Output 24: PDF/UA rule 7.1-8
- Output 24: PDF/UA rule 7.2-33
- Output 24: PDF/UA rule 7.2-34
- Output 25: PDF/UA rule 6.2-1
- Output 25: PDF/UA rule 7.1-10
- Output 25: PDF/UA rule 7.1-11
- Output 25: PDF/UA rule 7.1-3
- Output 25: PDF/UA rule 7.1-8
- Output 25: PDF/UA rule 7.2-33
- Output 25: PDF/UA rule 7.2-34
- Output 26: PDF/UA rule 6.2-1
- Output 26: PDF/UA rule 7.1-10
- Output 26: PDF/UA rule 7.1-11
- Output 26: PDF/UA rule 7.1-3
- Output 26: PDF/UA rule 7.1-8
- Output 26: PDF/UA rule 7.2-33
- Output 26: PDF/UA rule 7.2-34
- Output 27: PDF/UA rule 6.2-1
- Output 27: PDF/UA rule 7.1-10
- Output 27: PDF/UA rule 7.1-11
- Output 27: PDF/UA rule 7.1-3
- Output 27: PDF/UA rule 7.1-8
- Output 27: PDF/UA rule 7.2-33
- Output 27: PDF/UA rule 7.2-34
- Output 28: PDF/UA rule 6.2-1
- Output 28: PDF/UA rule 7.1-10
- Output 28: PDF/UA rule 7.1-11
- Output 28: PDF/UA rule 7.1-3
- Output 28: PDF/UA rule 7.1-8
- Output 28: PDF/UA rule 7.2-33
- Output 28: PDF/UA rule 7.2-34
- Output 29: PDF/UA rule 6.2-1
- Output 29: PDF/UA rule 7.1-10
- Output 29: PDF/UA rule 7.1-11
- Output 29: PDF/UA rule 7.1-3
- Output 29: PDF/UA rule 7.1-8
- Output 29: PDF/UA rule 7.2-34
- Output 30: PDF/UA rule 6.2-1
- Output 30: PDF/UA rule 7.1-10
- Output 30: PDF/UA rule 7.1-11
- Output 30: PDF/UA rule 7.1-3
- Output 30: PDF/UA rule 7.1-8
- Output 30: PDF/UA rule 7.18.5-1
- Output 30: PDF/UA rule 7.2-24
- Output 30: PDF/UA rule 7.2-34
- Output 31: PDF/UA rule 6.2-1
- Output 31: PDF/UA rule 7.1-10
- Output 31: PDF/UA rule 7.1-11
- Output 31: PDF/UA rule 7.1-3
- Output 31: PDF/UA rule 7.1-8
- Output 31: PDF/UA rule 7.18.5-1
- Output 31: PDF/UA rule 7.2-24
- Output 31: PDF/UA rule 7.2-34
- Output 32: PDF/UA rule 6.2-1
- Output 32: PDF/UA rule 7.1-10
- Output 32: PDF/UA rule 7.1-11
- Output 32: PDF/UA rule 7.1-3
- Output 32: PDF/UA rule 7.1-8
- Output 32: PDF/UA rule 7.18.5-1
- Output 32: PDF/UA rule 7.2-24
- Output 32: PDF/UA rule 7.2-33
- Output 32: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 80 → 0
- role_map_count: 1 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 72 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-ref-2-01-magazine-danish --output lab/reproduction.json
```

### ua1-ref-2-01-magazine-danish-pymupdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.1-2
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.18.5-2
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 82 → 0
- role_map_count: 1 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 73 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-ref-2-01-magazine-danish --output lab/reproduction.json
```

### ua1-ref-2-01-magazine-danish-pymupdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.1-8
- Output 2: PDF/UA rule 7.18.1-2
- Output 2: PDF/UA rule 7.18.3-1
- Output 2: PDF/UA rule 7.18.5-1
- Output 2: PDF/UA rule 7.18.5-2
- Output 2: PDF/UA rule 7.2-30
- Output 2: PDF/UA rule 7.2-33
- Output 2: PDF/UA rule 7.2-34
- Output 3: PDF/UA rule 6.2-1
- Output 3: PDF/UA rule 7.1-10
- Output 3: PDF/UA rule 7.1-11
- Output 3: PDF/UA rule 7.1-3
- Output 3: PDF/UA rule 7.1-8
- Output 3: PDF/UA rule 7.18.1-2
- Output 3: PDF/UA rule 7.18.3-1
- Output 3: PDF/UA rule 7.18.5-1
- Output 3: PDF/UA rule 7.18.5-2
- Output 3: PDF/UA rule 7.2-33
- Output 3: PDF/UA rule 7.2-34
- Output 4: PDF/UA rule 6.2-1
- Output 4: PDF/UA rule 7.1-10
- Output 4: PDF/UA rule 7.1-11
- Output 4: PDF/UA rule 7.1-3
- Output 4: PDF/UA rule 7.1-8
- Output 4: PDF/UA rule 7.2-33
- Output 4: PDF/UA rule 7.2-34
- Output 5: PDF/UA rule 6.2-1
- Output 5: PDF/UA rule 7.1-10
- Output 5: PDF/UA rule 7.1-11
- Output 5: PDF/UA rule 7.1-3
- Output 5: PDF/UA rule 7.1-8
- Output 5: PDF/UA rule 7.2-33
- Output 5: PDF/UA rule 7.2-34
- Output 6: PDF/UA rule 6.2-1
- Output 6: PDF/UA rule 7.1-10
- Output 6: PDF/UA rule 7.1-11
- Output 6: PDF/UA rule 7.1-3
- Output 6: PDF/UA rule 7.1-8
- Output 6: PDF/UA rule 7.2-34
- Output 7: PDF/UA rule 6.2-1
- Output 7: PDF/UA rule 7.1-10
- Output 7: PDF/UA rule 7.1-11
- Output 7: PDF/UA rule 7.1-3
- Output 7: PDF/UA rule 7.1-8
- Output 7: PDF/UA rule 7.18.1-2
- Output 7: PDF/UA rule 7.18.3-1
- Output 7: PDF/UA rule 7.18.5-1
- Output 7: PDF/UA rule 7.18.5-2
- Output 7: PDF/UA rule 7.2-33
- Output 7: PDF/UA rule 7.2-34
- Output 8: PDF/UA rule 6.2-1
- Output 8: PDF/UA rule 7.1-10
- Output 8: PDF/UA rule 7.1-11
- Output 8: PDF/UA rule 7.1-3
- Output 8: PDF/UA rule 7.1-8
- Output 8: PDF/UA rule 7.2-33
- Output 8: PDF/UA rule 7.2-34
- Output 9: PDF/UA rule 6.2-1
- Output 9: PDF/UA rule 7.1-10
- Output 9: PDF/UA rule 7.1-11
- Output 9: PDF/UA rule 7.1-3
- Output 9: PDF/UA rule 7.1-8
- Output 9: PDF/UA rule 7.2-33
- Output 9: PDF/UA rule 7.2-34
- Output 10: PDF/UA rule 6.2-1
- Output 10: PDF/UA rule 7.1-10
- Output 10: PDF/UA rule 7.1-11
- Output 10: PDF/UA rule 7.1-3
- Output 10: PDF/UA rule 7.1-8
- Output 10: PDF/UA rule 7.18.1-2
- Output 10: PDF/UA rule 7.18.3-1
- Output 10: PDF/UA rule 7.18.5-1
- Output 10: PDF/UA rule 7.18.5-2
- Output 10: PDF/UA rule 7.2-33
- Output 10: PDF/UA rule 7.2-34
- Output 11: PDF/UA rule 6.2-1
- Output 11: PDF/UA rule 7.1-10
- Output 11: PDF/UA rule 7.1-11
- Output 11: PDF/UA rule 7.1-3
- Output 11: PDF/UA rule 7.1-8
- Output 11: PDF/UA rule 7.2-34
- Output 12: PDF/UA rule 6.2-1
- Output 12: PDF/UA rule 7.1-10
- Output 12: PDF/UA rule 7.1-11
- Output 12: PDF/UA rule 7.1-3
- Output 12: PDF/UA rule 7.1-8
- Output 12: PDF/UA rule 7.2-33
- Output 12: PDF/UA rule 7.2-34
- Output 13: PDF/UA rule 6.2-1
- Output 13: PDF/UA rule 7.1-10
- Output 13: PDF/UA rule 7.1-11
- Output 13: PDF/UA rule 7.1-3
- Output 13: PDF/UA rule 7.1-8
- Output 13: PDF/UA rule 7.2-33
- Output 13: PDF/UA rule 7.2-34
- Output 14: PDF/UA rule 6.2-1
- Output 14: PDF/UA rule 7.1-10
- Output 14: PDF/UA rule 7.1-11
- Output 14: PDF/UA rule 7.1-3
- Output 14: PDF/UA rule 7.1-8
- Output 14: PDF/UA rule 7.2-33
- Output 14: PDF/UA rule 7.2-34
- Output 15: PDF/UA rule 6.2-1
- Output 15: PDF/UA rule 7.1-10
- Output 15: PDF/UA rule 7.1-11
- Output 15: PDF/UA rule 7.1-3
- Output 15: PDF/UA rule 7.1-8
- Output 15: PDF/UA rule 7.2-34
- Output 16: PDF/UA rule 6.2-1
- Output 16: PDF/UA rule 7.1-10
- Output 16: PDF/UA rule 7.1-11
- Output 16: PDF/UA rule 7.1-3
- Output 16: PDF/UA rule 7.1-8
- Output 16: PDF/UA rule 7.2-33
- Output 16: PDF/UA rule 7.2-34
- Output 17: PDF/UA rule 6.2-1
- Output 17: PDF/UA rule 7.1-10
- Output 17: PDF/UA rule 7.1-11
- Output 17: PDF/UA rule 7.1-3
- Output 17: PDF/UA rule 7.1-8
- Output 17: PDF/UA rule 7.2-33
- Output 17: PDF/UA rule 7.2-34
- Output 18: PDF/UA rule 6.2-1
- Output 18: PDF/UA rule 7.1-10
- Output 18: PDF/UA rule 7.1-11
- Output 18: PDF/UA rule 7.1-3
- Output 18: PDF/UA rule 7.1-8
- Output 18: PDF/UA rule 7.2-33
- Output 18: PDF/UA rule 7.2-34
- Output 19: PDF/UA rule 6.2-1
- Output 19: PDF/UA rule 7.1-10
- Output 19: PDF/UA rule 7.1-11
- Output 19: PDF/UA rule 7.1-3
- Output 19: PDF/UA rule 7.1-8
- Output 19: PDF/UA rule 7.2-34
- Output 20: PDF/UA rule 6.2-1
- Output 20: PDF/UA rule 7.1-10
- Output 20: PDF/UA rule 7.1-11
- Output 20: PDF/UA rule 7.1-3
- Output 20: PDF/UA rule 7.1-8
- Output 20: PDF/UA rule 7.2-34
- Output 21: PDF/UA rule 6.2-1
- Output 21: PDF/UA rule 7.1-10
- Output 21: PDF/UA rule 7.1-11
- Output 21: PDF/UA rule 7.1-3
- Output 21: PDF/UA rule 7.1-8
- Output 21: PDF/UA rule 7.2-34
- Output 22: PDF/UA rule 6.2-1
- Output 22: PDF/UA rule 7.1-10
- Output 22: PDF/UA rule 7.1-11
- Output 22: PDF/UA rule 7.1-3
- Output 22: PDF/UA rule 7.1-8
- Output 22: PDF/UA rule 7.2-34
- Output 23: PDF/UA rule 6.2-1
- Output 23: PDF/UA rule 7.1-10
- Output 23: PDF/UA rule 7.1-11
- Output 23: PDF/UA rule 7.1-3
- Output 23: PDF/UA rule 7.1-8
- Output 23: PDF/UA rule 7.2-34
- Output 24: PDF/UA rule 6.2-1
- Output 24: PDF/UA rule 7.1-10
- Output 24: PDF/UA rule 7.1-11
- Output 24: PDF/UA rule 7.1-3
- Output 24: PDF/UA rule 7.1-8
- Output 24: PDF/UA rule 7.2-33
- Output 24: PDF/UA rule 7.2-34
- Output 25: PDF/UA rule 6.2-1
- Output 25: PDF/UA rule 7.1-10
- Output 25: PDF/UA rule 7.1-11
- Output 25: PDF/UA rule 7.1-3
- Output 25: PDF/UA rule 7.1-8
- Output 25: PDF/UA rule 7.2-33
- Output 25: PDF/UA rule 7.2-34
- Output 26: PDF/UA rule 6.2-1
- Output 26: PDF/UA rule 7.1-10
- Output 26: PDF/UA rule 7.1-11
- Output 26: PDF/UA rule 7.1-3
- Output 26: PDF/UA rule 7.1-8
- Output 26: PDF/UA rule 7.2-33
- Output 26: PDF/UA rule 7.2-34
- Output 27: PDF/UA rule 6.2-1
- Output 27: PDF/UA rule 7.1-10
- Output 27: PDF/UA rule 7.1-11
- Output 27: PDF/UA rule 7.1-3
- Output 27: PDF/UA rule 7.1-8
- Output 27: PDF/UA rule 7.2-33
- Output 27: PDF/UA rule 7.2-34
- Output 28: PDF/UA rule 6.2-1
- Output 28: PDF/UA rule 7.1-10
- Output 28: PDF/UA rule 7.1-11
- Output 28: PDF/UA rule 7.1-3
- Output 28: PDF/UA rule 7.1-8
- Output 28: PDF/UA rule 7.2-33
- Output 28: PDF/UA rule 7.2-34
- Output 29: PDF/UA rule 6.2-1
- Output 29: PDF/UA rule 7.1-10
- Output 29: PDF/UA rule 7.1-11
- Output 29: PDF/UA rule 7.1-3
- Output 29: PDF/UA rule 7.1-8
- Output 29: PDF/UA rule 7.2-34
- Output 30: PDF/UA rule 6.2-1
- Output 30: PDF/UA rule 7.1-10
- Output 30: PDF/UA rule 7.1-11
- Output 30: PDF/UA rule 7.1-3
- Output 30: PDF/UA rule 7.1-8
- Output 30: PDF/UA rule 7.18.1-2
- Output 30: PDF/UA rule 7.18.3-1
- Output 30: PDF/UA rule 7.18.5-1
- Output 30: PDF/UA rule 7.18.5-2
- Output 30: PDF/UA rule 7.2-34
- Output 31: PDF/UA rule 6.2-1
- Output 31: PDF/UA rule 7.1-10
- Output 31: PDF/UA rule 7.1-11
- Output 31: PDF/UA rule 7.1-3
- Output 31: PDF/UA rule 7.1-8
- Output 31: PDF/UA rule 7.18.1-2
- Output 31: PDF/UA rule 7.18.3-1
- Output 31: PDF/UA rule 7.18.5-1
- Output 31: PDF/UA rule 7.18.5-2
- Output 31: PDF/UA rule 7.2-34
- Output 32: PDF/UA rule 6.2-1
- Output 32: PDF/UA rule 7.1-10
- Output 32: PDF/UA rule 7.1-11
- Output 32: PDF/UA rule 7.1-3
- Output 32: PDF/UA rule 7.1-8
- Output 32: PDF/UA rule 7.18.1-2
- Output 32: PDF/UA rule 7.18.3-1
- Output 32: PDF/UA rule 7.18.5-1
- Output 32: PDF/UA rule 7.18.5-2
- Output 32: PDF/UA rule 7.2-33
- Output 32: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 80 → 0
- role_map_count: 1 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 72 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-ref-2-01-magazine-danish --output lab/reproduction.json
```

### ua1-ref-2-01-magazine-danish-ghostscript-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 1: PDF/UA rule 7.21.4.2-2
- Output 1: PDF/UA rule 7.21.7-1
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 82 → 0
- role_map_count: 1 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-ref-2-01-magazine-danish --output lab/reproduction.json
```

### ua1-ref-2-01-magazine-danish-ghostscript-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 2: PDF/UA rule 5-1
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.18.3-1
- Output 2: PDF/UA rule 7.18.5-1
- Output 2: PDF/UA rule 7.2-24
- Output 2: PDF/UA rule 7.2-30
- Output 2: PDF/UA rule 7.2-33
- Output 2: PDF/UA rule 7.2-34
- Output 3: PDF/UA rule 5-1
- Output 3: PDF/UA rule 6.2-1
- Output 3: PDF/UA rule 7.1-10
- Output 3: PDF/UA rule 7.1-11
- Output 3: PDF/UA rule 7.1-3
- Output 3: PDF/UA rule 7.18.3-1
- Output 3: PDF/UA rule 7.18.5-1
- Output 3: PDF/UA rule 7.2-24
- Output 3: PDF/UA rule 7.2-33
- Output 3: PDF/UA rule 7.2-34
- Output 3: PDF/UA rule 7.21.4.2-2
- Output 3: PDF/UA rule 7.21.7-1
- Output 4: PDF/UA rule 5-1
- Output 4: PDF/UA rule 6.2-1
- Output 4: PDF/UA rule 7.1-10
- Output 4: PDF/UA rule 7.1-11
- Output 4: PDF/UA rule 7.1-3
- Output 4: PDF/UA rule 7.2-33
- Output 4: PDF/UA rule 7.2-34
- Output 5: PDF/UA rule 5-1
- Output 5: PDF/UA rule 6.2-1
- Output 5: PDF/UA rule 7.1-10
- Output 5: PDF/UA rule 7.1-11
- Output 5: PDF/UA rule 7.1-3
- Output 5: PDF/UA rule 7.2-33
- Output 5: PDF/UA rule 7.2-34
- Output 5: PDF/UA rule 7.21.4.2-2
- Output 6: PDF/UA rule 5-1
- Output 6: PDF/UA rule 6.2-1
- Output 6: PDF/UA rule 7.1-10
- Output 6: PDF/UA rule 7.1-11
- Output 6: PDF/UA rule 7.1-3
- Output 6: PDF/UA rule 7.2-33
- Output 6: PDF/UA rule 7.2-34
- Output 6: PDF/UA rule 7.21.4.2-2
- Output 6: PDF/UA rule 7.21.7-1
- Output 7: PDF/UA rule 5-1
- Output 7: PDF/UA rule 6.2-1
- Output 7: PDF/UA rule 7.1-10
- Output 7: PDF/UA rule 7.1-11
- Output 7: PDF/UA rule 7.1-3
- Output 7: PDF/UA rule 7.18.3-1
- Output 7: PDF/UA rule 7.18.5-1
- Output 7: PDF/UA rule 7.2-24
- Output 7: PDF/UA rule 7.2-33
- Output 7: PDF/UA rule 7.2-34
- Output 7: PDF/UA rule 7.21.4.2-2
- Output 8: PDF/UA rule 5-1
- Output 8: PDF/UA rule 6.2-1
- Output 8: PDF/UA rule 7.1-10
- Output 8: PDF/UA rule 7.1-11
- Output 8: PDF/UA rule 7.1-3
- Output 8: PDF/UA rule 7.2-33
- Output 8: PDF/UA rule 7.2-34
- Output 8: PDF/UA rule 7.21.4.2-2
- Output 9: PDF/UA rule 5-1
- Output 9: PDF/UA rule 6.2-1
- Output 9: PDF/UA rule 7.1-10
- Output 9: PDF/UA rule 7.1-11
- Output 9: PDF/UA rule 7.1-3
- Output 9: PDF/UA rule 7.2-33
- Output 9: PDF/UA rule 7.2-34
- Output 9: PDF/UA rule 7.21.4.2-2
- Output 9: PDF/UA rule 7.21.7-1
- Output 10: PDF/UA rule 5-1
- Output 10: PDF/UA rule 6.2-1
- Output 10: PDF/UA rule 7.1-10
- Output 10: PDF/UA rule 7.1-11
- Output 10: PDF/UA rule 7.1-3
- Output 10: PDF/UA rule 7.18.3-1
- Output 10: PDF/UA rule 7.18.5-1
- Output 10: PDF/UA rule 7.2-24
- Output 10: PDF/UA rule 7.2-33
- Output 10: PDF/UA rule 7.2-34
- Output 10: PDF/UA rule 7.21.4.2-2
- Output 10: PDF/UA rule 7.21.7-1
- Output 11: PDF/UA rule 5-1
- Output 11: PDF/UA rule 6.2-1
- Output 11: PDF/UA rule 7.1-10
- Output 11: PDF/UA rule 7.1-11
- Output 11: PDF/UA rule 7.1-3
- Output 11: PDF/UA rule 7.2-33
- Output 11: PDF/UA rule 7.2-34
- Output 11: PDF/UA rule 7.21.4.2-2
- Output 11: PDF/UA rule 7.21.7-1
- Output 12: PDF/UA rule 5-1
- Output 12: PDF/UA rule 6.2-1
- Output 12: PDF/UA rule 7.1-10
- Output 12: PDF/UA rule 7.1-11
- Output 12: PDF/UA rule 7.1-3
- Output 12: PDF/UA rule 7.2-33
- Output 12: PDF/UA rule 7.2-34
- Output 12: PDF/UA rule 7.21.4.2-2
- Output 13: PDF/UA rule 5-1
- Output 13: PDF/UA rule 6.2-1
- Output 13: PDF/UA rule 7.1-10
- Output 13: PDF/UA rule 7.1-11
- Output 13: PDF/UA rule 7.1-3
- Output 13: PDF/UA rule 7.2-33
- Output 13: PDF/UA rule 7.2-34
- Output 13: PDF/UA rule 7.21.4.2-2
- Output 13: PDF/UA rule 7.21.7-1
- Output 14: PDF/UA rule 5-1
- Output 14: PDF/UA rule 6.2-1
- Output 14: PDF/UA rule 7.1-10
- Output 14: PDF/UA rule 7.1-11
- Output 14: PDF/UA rule 7.1-3
- Output 14: PDF/UA rule 7.2-33
- Output 14: PDF/UA rule 7.2-34
- Output 14: PDF/UA rule 7.21.4.2-2
- Output 15: PDF/UA rule 5-1
- Output 15: PDF/UA rule 6.2-1
- Output 15: PDF/UA rule 7.1-10
- Output 15: PDF/UA rule 7.1-11
- Output 15: PDF/UA rule 7.1-3
- Output 15: PDF/UA rule 7.2-33
- Output 15: PDF/UA rule 7.2-34
- Output 15: PDF/UA rule 7.21.4.2-2
- Output 15: PDF/UA rule 7.21.7-1
- Output 16: PDF/UA rule 5-1
- Output 16: PDF/UA rule 6.2-1
- Output 16: PDF/UA rule 7.1-10
- Output 16: PDF/UA rule 7.1-11
- Output 16: PDF/UA rule 7.1-3
- Output 16: PDF/UA rule 7.2-33
- Output 16: PDF/UA rule 7.2-34
- Output 16: PDF/UA rule 7.21.7-1
- Output 17: PDF/UA rule 5-1
- Output 17: PDF/UA rule 6.2-1
- Output 17: PDF/UA rule 7.1-10
- Output 17: PDF/UA rule 7.1-11
- Output 17: PDF/UA rule 7.1-3
- Output 17: PDF/UA rule 7.2-33
- Output 17: PDF/UA rule 7.2-34
- Output 17: PDF/UA rule 7.21.7-1
- Output 18: PDF/UA rule 5-1
- Output 18: PDF/UA rule 6.2-1
- Output 18: PDF/UA rule 7.1-10
- Output 18: PDF/UA rule 7.1-11
- Output 18: PDF/UA rule 7.1-3
- Output 18: PDF/UA rule 7.2-33
- Output 18: PDF/UA rule 7.2-34
- Output 18: PDF/UA rule 7.21.7-1
- Output 19: PDF/UA rule 5-1
- Output 19: PDF/UA rule 6.2-1
- Output 19: PDF/UA rule 7.1-10
- Output 19: PDF/UA rule 7.1-11
- Output 19: PDF/UA rule 7.1-3
- Output 19: PDF/UA rule 7.2-33
- Output 19: PDF/UA rule 7.2-34
- Output 19: PDF/UA rule 7.21.4.2-2
- Output 19: PDF/UA rule 7.21.7-1
- Output 20: PDF/UA rule 5-1
- Output 20: PDF/UA rule 6.2-1
- Output 20: PDF/UA rule 7.1-10
- Output 20: PDF/UA rule 7.1-11
- Output 20: PDF/UA rule 7.1-3
- Output 20: PDF/UA rule 7.2-33
- Output 20: PDF/UA rule 7.2-34
- Output 20: PDF/UA rule 7.21.4.2-2
- Output 21: PDF/UA rule 5-1
- Output 21: PDF/UA rule 6.2-1
- Output 21: PDF/UA rule 7.1-10
- Output 21: PDF/UA rule 7.1-11
- Output 21: PDF/UA rule 7.1-3
- Output 21: PDF/UA rule 7.2-33
- Output 21: PDF/UA rule 7.2-34
- Output 21: PDF/UA rule 7.21.4.2-2
- Output 22: PDF/UA rule 5-1
- Output 22: PDF/UA rule 6.2-1
- Output 22: PDF/UA rule 7.1-10
- Output 22: PDF/UA rule 7.1-11
- Output 22: PDF/UA rule 7.1-3
- Output 22: PDF/UA rule 7.2-33
- Output 22: PDF/UA rule 7.2-34
- Output 22: PDF/UA rule 7.21.4.2-2
- Output 23: PDF/UA rule 5-1
- Output 23: PDF/UA rule 6.2-1
- Output 23: PDF/UA rule 7.1-10
- Output 23: PDF/UA rule 7.1-11
- Output 23: PDF/UA rule 7.1-3
- Output 23: PDF/UA rule 7.2-33
- Output 23: PDF/UA rule 7.2-34
- Output 23: PDF/UA rule 7.21.4.2-2
- Output 23: PDF/UA rule 7.21.7-1
- Output 24: PDF/UA rule 5-1
- Output 24: PDF/UA rule 6.2-1
- Output 24: PDF/UA rule 7.1-10
- Output 24: PDF/UA rule 7.1-11
- Output 24: PDF/UA rule 7.1-3
- Output 24: PDF/UA rule 7.2-33
- Output 24: PDF/UA rule 7.2-34
- Output 24: PDF/UA rule 7.21.4.2-2
- Output 25: PDF/UA rule 5-1
- Output 25: PDF/UA rule 6.2-1
- Output 25: PDF/UA rule 7.1-10
- Output 25: PDF/UA rule 7.1-11
- Output 25: PDF/UA rule 7.1-3
- Output 25: PDF/UA rule 7.2-33
- Output 25: PDF/UA rule 7.2-34
- Output 25: PDF/UA rule 7.21.4.2-2
- Output 26: PDF/UA rule 5-1
- Output 26: PDF/UA rule 6.2-1
- Output 26: PDF/UA rule 7.1-10
- Output 26: PDF/UA rule 7.1-11
- Output 26: PDF/UA rule 7.1-3
- Output 26: PDF/UA rule 7.2-33
- Output 26: PDF/UA rule 7.2-34
- Output 26: PDF/UA rule 7.21.4.2-2
- Output 27: PDF/UA rule 5-1
- Output 27: PDF/UA rule 6.2-1
- Output 27: PDF/UA rule 7.1-10
- Output 27: PDF/UA rule 7.1-11
- Output 27: PDF/UA rule 7.1-3
- Output 27: PDF/UA rule 7.2-33
- Output 27: PDF/UA rule 7.2-34
- Output 27: PDF/UA rule 7.21.4.2-2
- Output 27: PDF/UA rule 7.21.7-1
- Output 28: PDF/UA rule 5-1
- Output 28: PDF/UA rule 6.2-1
- Output 28: PDF/UA rule 7.1-10
- Output 28: PDF/UA rule 7.1-11
- Output 28: PDF/UA rule 7.1-3
- Output 28: PDF/UA rule 7.2-33
- Output 28: PDF/UA rule 7.2-34
- Output 28: PDF/UA rule 7.21.4.2-2
- Output 29: PDF/UA rule 5-1
- Output 29: PDF/UA rule 6.2-1
- Output 29: PDF/UA rule 7.1-10
- Output 29: PDF/UA rule 7.1-11
- Output 29: PDF/UA rule 7.1-3
- Output 29: PDF/UA rule 7.2-33
- Output 29: PDF/UA rule 7.2-34
- Output 29: PDF/UA rule 7.21.4.2-2
- Output 30: PDF/UA rule 5-1
- Output 30: PDF/UA rule 6.2-1
- Output 30: PDF/UA rule 7.1-10
- Output 30: PDF/UA rule 7.1-11
- Output 30: PDF/UA rule 7.1-3
- Output 30: PDF/UA rule 7.18.3-1
- Output 30: PDF/UA rule 7.18.5-1
- Output 30: PDF/UA rule 7.2-24
- Output 30: PDF/UA rule 7.2-33
- Output 30: PDF/UA rule 7.2-34
- Output 30: PDF/UA rule 7.21.4.2-2
- Output 30: PDF/UA rule 7.21.7-1
- Output 31: PDF/UA rule 5-1
- Output 31: PDF/UA rule 6.2-1
- Output 31: PDF/UA rule 7.1-10
- Output 31: PDF/UA rule 7.1-11
- Output 31: PDF/UA rule 7.1-3
- Output 31: PDF/UA rule 7.18.3-1
- Output 31: PDF/UA rule 7.18.5-1
- Output 31: PDF/UA rule 7.2-24
- Output 31: PDF/UA rule 7.2-33
- Output 31: PDF/UA rule 7.2-34
- Output 31: PDF/UA rule 7.21.4.2-2
- Output 31: PDF/UA rule 7.21.7-1
- Output 32: PDF/UA rule 5-1
- Output 32: PDF/UA rule 6.2-1
- Output 32: PDF/UA rule 7.1-10
- Output 32: PDF/UA rule 7.1-11
- Output 32: PDF/UA rule 7.1-3
- Output 32: PDF/UA rule 7.18.3-1
- Output 32: PDF/UA rule 7.18.5-1
- Output 32: PDF/UA rule 7.2-24
- Output 32: PDF/UA rule 7.2-33
- Output 32: PDF/UA rule 7.2-34
- Output 32: PDF/UA rule 7.21.4.2-2
- Output 32: PDF/UA rule 7.21.7-1
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 80 → 0
- role_map_count: 1 → 0
- document_language_present: True → False
- outline_count: 72 → 1

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-ref-2-01-magazine-danish --output lab/reproduction.json
```

### ua1-ref-2-01-magazine-danish-ghostscript-resave

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 1: PDF/UA rule 7.21.4.2-2
- Output 1: PDF/UA rule 7.21.7-1
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 80 → 0
- role_map_count: 1 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-ref-2-01-magazine-danish --output lab/reproduction.json
```

### ua1-ref-2-02-invoice-qpdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 2 → 0
- role_map_count: 4 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 5 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-ref-2-02-invoice --output lab/reproduction.json
```

### ua1-ref-2-02-invoice-qpdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 2 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 1 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-ref-2-02-invoice --output lab/reproduction.json
```

### ua1-ref-2-02-invoice-pymupdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.1-2
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.18.5-2
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 2 → 0
- role_map_count: 4 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 5 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-ref-2-02-invoice --output lab/reproduction.json
```

### ua1-ref-2-02-invoice-pymupdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 2 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 1 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-ref-2-02-invoice --output lab/reproduction.json
```

### ua1-ref-2-02-invoice-ghostscript-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 1: PDF/UA rule 7.21.4.2-2
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 2 → 0
- role_map_count: 4 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-ref-2-02-invoice --output lab/reproduction.json
```

### ua1-ref-2-02-invoice-ghostscript-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 2 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-ref-2-02-invoice --output lab/reproduction.json
```

### ua1-ref-2-02-invoice-ghostscript-resave

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 2 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-ref-2-02-invoice --output lab/reproduction.json
```

### ua1-ref-2-03-academicabstract-qpdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 15 → 0
- role_map_count: 16 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 8 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-ref-2-03-academicabstract --output lab/reproduction.json
```

### ua1-ref-2-03-academicabstract-qpdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-34
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.1-8
- Output 2: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- role_map_count: 4 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 4 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-ref-2-03-academicabstract --output lab/reproduction.json
```

### ua1-ref-2-03-academicabstract-pymupdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.1-2
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.18.5-2
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 15 → 0
- role_map_count: 16 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 8 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-ref-2-03-academicabstract --output lab/reproduction.json
```

### ua1-ref-2-03-academicabstract-pymupdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.1-2
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.18.5-2
- Output 1: PDF/UA rule 7.2-34
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.1-8
- Output 2: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- role_map_count: 4 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 4 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-ref-2-03-academicabstract --output lab/reproduction.json
```

### ua1-ref-2-03-academicabstract-ghostscript-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 1: PDF/UA rule 7.21.4.2-2
- Output 1: PDF/UA rule 7.21.7-1
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 15 → 0
- role_map_count: 16 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-ref-2-03-academicabstract --output lab/reproduction.json
```

### ua1-ref-2-03-academicabstract-ghostscript-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 1: PDF/UA rule 7.21.4.2-2
- Output 2: PDF/UA rule 5-1
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.2-33
- Output 2: PDF/UA rule 7.2-34
- Output 2: PDF/UA rule 7.21.4.2-2
- struct_tree_present: True → False
- marked_pdf: True → False
- role_map_count: 4 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-ref-2-03-academicabstract --output lab/reproduction.json
```

### ua1-ref-2-03-academicabstract-ghostscript-resave

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 1: PDF/UA rule 7.21.4.2-2
- struct_tree_present: True → False
- marked_pdf: True → False
- role_map_count: 4 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-ref-2-03-academicabstract --output lab/reproduction.json
```

### ua1-ref-2-04-presentation-qpdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 20 → 0
- role_map_count: 17 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 26 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-ref-2-04-presentation --output lab/reproduction.json
```

### ua1-ref-2-04-presentation-qpdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.1-8
- Output 2: PDF/UA rule 7.18.5-1
- Output 2: PDF/UA rule 7.2-24
- Output 2: PDF/UA rule 7.2-30
- Output 2: PDF/UA rule 7.2-33
- Output 2: PDF/UA rule 7.2-34
- Output 3: PDF/UA rule 6.2-1
- Output 3: PDF/UA rule 7.1-10
- Output 3: PDF/UA rule 7.1-11
- Output 3: PDF/UA rule 7.1-3
- Output 3: PDF/UA rule 7.1-8
- Output 3: PDF/UA rule 7.18.5-1
- Output 3: PDF/UA rule 7.2-24
- Output 3: PDF/UA rule 7.2-30
- Output 3: PDF/UA rule 7.2-33
- Output 3: PDF/UA rule 7.2-34
- Output 4: PDF/UA rule 6.2-1
- Output 4: PDF/UA rule 7.1-10
- Output 4: PDF/UA rule 7.1-11
- Output 4: PDF/UA rule 7.1-3
- Output 4: PDF/UA rule 7.1-8
- Output 4: PDF/UA rule 7.2-30
- Output 4: PDF/UA rule 7.2-33
- Output 4: PDF/UA rule 7.2-34
- Output 5: PDF/UA rule 6.2-1
- Output 5: PDF/UA rule 7.1-10
- Output 5: PDF/UA rule 7.1-11
- Output 5: PDF/UA rule 7.1-3
- Output 5: PDF/UA rule 7.1-8
- Output 5: PDF/UA rule 7.2-30
- Output 5: PDF/UA rule 7.2-33
- Output 5: PDF/UA rule 7.2-34
- Output 6: PDF/UA rule 6.2-1
- Output 6: PDF/UA rule 7.1-10
- Output 6: PDF/UA rule 7.1-11
- Output 6: PDF/UA rule 7.1-3
- Output 6: PDF/UA rule 7.1-8
- Output 6: PDF/UA rule 7.18.5-1
- Output 6: PDF/UA rule 7.2-24
- Output 6: PDF/UA rule 7.2-30
- Output 6: PDF/UA rule 7.2-33
- Output 6: PDF/UA rule 7.2-34
- Output 7: PDF/UA rule 6.2-1
- Output 7: PDF/UA rule 7.1-10
- Output 7: PDF/UA rule 7.1-11
- Output 7: PDF/UA rule 7.1-3
- Output 7: PDF/UA rule 7.1-8
- Output 7: PDF/UA rule 7.18.5-1
- Output 7: PDF/UA rule 7.2-24
- Output 7: PDF/UA rule 7.2-30
- Output 7: PDF/UA rule 7.2-33
- Output 7: PDF/UA rule 7.2-34
- Output 8: PDF/UA rule 6.2-1
- Output 8: PDF/UA rule 7.1-10
- Output 8: PDF/UA rule 7.1-11
- Output 8: PDF/UA rule 7.1-3
- Output 8: PDF/UA rule 7.1-8
- Output 8: PDF/UA rule 7.18.5-1
- Output 8: PDF/UA rule 7.2-24
- Output 8: PDF/UA rule 7.2-30
- Output 8: PDF/UA rule 7.2-33
- Output 8: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 15 → 0
- role_map_count: 12 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 4 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-ref-2-04-presentation --output lab/reproduction.json
```

### ua1-ref-2-04-presentation-pymupdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.1-2
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.18.5-2
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 20 → 0
- role_map_count: 17 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 26 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-ref-2-04-presentation --output lab/reproduction.json
```

### ua1-ref-2-04-presentation-pymupdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.1-2
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.18.5-2
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.1-8
- Output 2: PDF/UA rule 7.2-30
- Output 2: PDF/UA rule 7.2-33
- Output 2: PDF/UA rule 7.2-34
- Output 3: PDF/UA rule 6.2-1
- Output 3: PDF/UA rule 7.1-10
- Output 3: PDF/UA rule 7.1-11
- Output 3: PDF/UA rule 7.1-3
- Output 3: PDF/UA rule 7.1-8
- Output 3: PDF/UA rule 7.18.1-2
- Output 3: PDF/UA rule 7.18.3-1
- Output 3: PDF/UA rule 7.18.5-1
- Output 3: PDF/UA rule 7.18.5-2
- Output 3: PDF/UA rule 7.2-30
- Output 3: PDF/UA rule 7.2-33
- Output 3: PDF/UA rule 7.2-34
- Output 4: PDF/UA rule 6.2-1
- Output 4: PDF/UA rule 7.1-10
- Output 4: PDF/UA rule 7.1-11
- Output 4: PDF/UA rule 7.1-3
- Output 4: PDF/UA rule 7.1-8
- Output 4: PDF/UA rule 7.2-30
- Output 4: PDF/UA rule 7.2-33
- Output 4: PDF/UA rule 7.2-34
- Output 5: PDF/UA rule 6.2-1
- Output 5: PDF/UA rule 7.1-10
- Output 5: PDF/UA rule 7.1-11
- Output 5: PDF/UA rule 7.1-3
- Output 5: PDF/UA rule 7.1-8
- Output 5: PDF/UA rule 7.2-30
- Output 5: PDF/UA rule 7.2-33
- Output 5: PDF/UA rule 7.2-34
- Output 6: PDF/UA rule 6.2-1
- Output 6: PDF/UA rule 7.1-10
- Output 6: PDF/UA rule 7.1-11
- Output 6: PDF/UA rule 7.1-3
- Output 6: PDF/UA rule 7.1-8
- Output 6: PDF/UA rule 7.18.1-2
- Output 6: PDF/UA rule 7.18.3-1
- Output 6: PDF/UA rule 7.18.5-1
- Output 6: PDF/UA rule 7.18.5-2
- Output 6: PDF/UA rule 7.2-30
- Output 6: PDF/UA rule 7.2-33
- Output 6: PDF/UA rule 7.2-34
- Output 7: PDF/UA rule 6.2-1
- Output 7: PDF/UA rule 7.1-10
- Output 7: PDF/UA rule 7.1-11
- Output 7: PDF/UA rule 7.1-3
- Output 7: PDF/UA rule 7.1-8
- Output 7: PDF/UA rule 7.18.1-2
- Output 7: PDF/UA rule 7.18.3-1
- Output 7: PDF/UA rule 7.18.5-1
- Output 7: PDF/UA rule 7.18.5-2
- Output 7: PDF/UA rule 7.2-30
- Output 7: PDF/UA rule 7.2-33
- Output 7: PDF/UA rule 7.2-34
- Output 8: PDF/UA rule 6.2-1
- Output 8: PDF/UA rule 7.1-10
- Output 8: PDF/UA rule 7.1-11
- Output 8: PDF/UA rule 7.1-3
- Output 8: PDF/UA rule 7.1-8
- Output 8: PDF/UA rule 7.18.1-2
- Output 8: PDF/UA rule 7.18.3-1
- Output 8: PDF/UA rule 7.18.5-1
- Output 8: PDF/UA rule 7.18.5-2
- Output 8: PDF/UA rule 7.2-30
- Output 8: PDF/UA rule 7.2-33
- Output 8: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 15 → 0
- role_map_count: 12 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 4 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-ref-2-04-presentation --output lab/reproduction.json
```

### ua1-ref-2-04-presentation-ghostscript-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 1: PDF/UA rule 7.21.4.2-2
- Output 1: PDF/UA rule 7.21.7-1
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 20 → 0
- role_map_count: 17 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-ref-2-04-presentation --output lab/reproduction.json
```

### ua1-ref-2-04-presentation-ghostscript-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 2: PDF/UA rule 5-1
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.2-30
- Output 2: PDF/UA rule 7.2-33
- Output 2: PDF/UA rule 7.2-34
- Output 3: PDF/UA rule 5-1
- Output 3: PDF/UA rule 6.2-1
- Output 3: PDF/UA rule 7.1-10
- Output 3: PDF/UA rule 7.1-11
- Output 3: PDF/UA rule 7.1-3
- Output 3: PDF/UA rule 7.18.3-1
- Output 3: PDF/UA rule 7.18.5-1
- Output 3: PDF/UA rule 7.2-2
- Output 3: PDF/UA rule 7.2-24
- Output 3: PDF/UA rule 7.2-30
- Output 3: PDF/UA rule 7.2-33
- Output 3: PDF/UA rule 7.2-34
- Output 4: PDF/UA rule 5-1
- Output 4: PDF/UA rule 6.2-1
- Output 4: PDF/UA rule 7.1-10
- Output 4: PDF/UA rule 7.1-11
- Output 4: PDF/UA rule 7.1-3
- Output 4: PDF/UA rule 7.2-30
- Output 4: PDF/UA rule 7.2-33
- Output 4: PDF/UA rule 7.2-34
- Output 5: PDF/UA rule 5-1
- Output 5: PDF/UA rule 6.2-1
- Output 5: PDF/UA rule 7.1-10
- Output 5: PDF/UA rule 7.1-11
- Output 5: PDF/UA rule 7.1-3
- Output 5: PDF/UA rule 7.2-30
- Output 5: PDF/UA rule 7.2-33
- Output 5: PDF/UA rule 7.2-34
- Output 6: PDF/UA rule 5-1
- Output 6: PDF/UA rule 6.2-1
- Output 6: PDF/UA rule 7.1-10
- Output 6: PDF/UA rule 7.1-11
- Output 6: PDF/UA rule 7.1-3
- Output 6: PDF/UA rule 7.18.3-1
- Output 6: PDF/UA rule 7.18.5-1
- Output 6: PDF/UA rule 7.2-24
- Output 6: PDF/UA rule 7.2-30
- Output 6: PDF/UA rule 7.2-33
- Output 6: PDF/UA rule 7.2-34
- Output 7: PDF/UA rule 5-1
- Output 7: PDF/UA rule 6.2-1
- Output 7: PDF/UA rule 7.1-10
- Output 7: PDF/UA rule 7.1-11
- Output 7: PDF/UA rule 7.1-3
- Output 7: PDF/UA rule 7.18.3-1
- Output 7: PDF/UA rule 7.18.5-1
- Output 7: PDF/UA rule 7.2-24
- Output 7: PDF/UA rule 7.2-30
- Output 7: PDF/UA rule 7.2-33
- Output 7: PDF/UA rule 7.2-34
- Output 7: PDF/UA rule 7.21.7-1
- Output 8: PDF/UA rule 5-1
- Output 8: PDF/UA rule 6.2-1
- Output 8: PDF/UA rule 7.1-10
- Output 8: PDF/UA rule 7.1-11
- Output 8: PDF/UA rule 7.1-3
- Output 8: PDF/UA rule 7.18.3-1
- Output 8: PDF/UA rule 7.18.5-1
- Output 8: PDF/UA rule 7.2-24
- Output 8: PDF/UA rule 7.2-30
- Output 8: PDF/UA rule 7.2-33
- Output 8: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 15 → 0
- role_map_count: 12 → 0
- document_language_present: True → False
- outline_count: 4 → 1

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-ref-2-04-presentation --output lab/reproduction.json
```

### ua1-ref-2-04-presentation-ghostscript-resave

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 1: PDF/UA rule 7.21.7-1
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 15 → 0
- role_map_count: 12 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-ref-2-04-presentation --output lab/reproduction.json
```

### ua1-ref-2-05-bookchapter-german-qpdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 9 → 0
- role_map_count: 13 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 34 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-ref-2-05-bookchapter-german --output lab/reproduction.json
```

### ua1-ref-2-05-bookchapter-german-qpdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-34
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.1-8
- Output 2: PDF/UA rule 7.2-30
- Output 2: PDF/UA rule 7.2-34
- Output 3: PDF/UA rule 6.2-1
- Output 3: PDF/UA rule 7.1-10
- Output 3: PDF/UA rule 7.1-11
- Output 3: PDF/UA rule 7.1-3
- Output 3: PDF/UA rule 7.1-8
- Output 3: PDF/UA rule 7.2-30
- Output 3: PDF/UA rule 7.2-34
- Output 4: PDF/UA rule 6.2-1
- Output 4: PDF/UA rule 7.1-10
- Output 4: PDF/UA rule 7.1-11
- Output 4: PDF/UA rule 7.1-3
- Output 4: PDF/UA rule 7.1-8
- Output 4: PDF/UA rule 7.18.5-1
- Output 4: PDF/UA rule 7.2-24
- Output 4: PDF/UA rule 7.2-30
- Output 4: PDF/UA rule 7.2-34
- Output 5: PDF/UA rule 6.2-1
- Output 5: PDF/UA rule 7.1-10
- Output 5: PDF/UA rule 7.1-11
- Output 5: PDF/UA rule 7.1-3
- Output 5: PDF/UA rule 7.1-8
- Output 5: PDF/UA rule 7.2-30
- Output 5: PDF/UA rule 7.2-34
- Output 6: PDF/UA rule 6.2-1
- Output 6: PDF/UA rule 7.1-10
- Output 6: PDF/UA rule 7.1-11
- Output 6: PDF/UA rule 7.1-3
- Output 6: PDF/UA rule 7.1-8
- Output 6: PDF/UA rule 7.18.5-1
- Output 6: PDF/UA rule 7.2-24
- Output 6: PDF/UA rule 7.2-30
- Output 6: PDF/UA rule 7.2-34
- Output 7: PDF/UA rule 6.2-1
- Output 7: PDF/UA rule 7.1-10
- Output 7: PDF/UA rule 7.1-11
- Output 7: PDF/UA rule 7.1-3
- Output 7: PDF/UA rule 7.1-8
- Output 7: PDF/UA rule 7.18.5-1
- Output 7: PDF/UA rule 7.2-24
- Output 7: PDF/UA rule 7.2-30
- Output 7: PDF/UA rule 7.2-34
- Output 8: PDF/UA rule 6.2-1
- Output 8: PDF/UA rule 7.1-10
- Output 8: PDF/UA rule 7.1-11
- Output 8: PDF/UA rule 7.1-3
- Output 8: PDF/UA rule 7.1-8
- Output 8: PDF/UA rule 7.2-30
- Output 8: PDF/UA rule 7.2-33
- Output 8: PDF/UA rule 7.2-34
- Output 9: PDF/UA rule 6.2-1
- Output 9: PDF/UA rule 7.1-10
- Output 9: PDF/UA rule 7.1-11
- Output 9: PDF/UA rule 7.1-3
- Output 9: PDF/UA rule 7.1-8
- Output 9: PDF/UA rule 7.2-30
- Output 9: PDF/UA rule 7.2-34
- Output 10: PDF/UA rule 6.2-1
- Output 10: PDF/UA rule 7.1-10
- Output 10: PDF/UA rule 7.1-11
- Output 10: PDF/UA rule 7.1-3
- Output 10: PDF/UA rule 7.1-8
- Output 10: PDF/UA rule 7.2-30
- Output 10: PDF/UA rule 7.2-34
- Output 11: PDF/UA rule 6.2-1
- Output 11: PDF/UA rule 7.1-10
- Output 11: PDF/UA rule 7.1-11
- Output 11: PDF/UA rule 7.1-3
- Output 11: PDF/UA rule 7.1-8
- Output 11: PDF/UA rule 7.18.5-1
- Output 11: PDF/UA rule 7.2-24
- Output 11: PDF/UA rule 7.2-30
- Output 11: PDF/UA rule 7.2-34
- Output 12: PDF/UA rule 6.2-1
- Output 12: PDF/UA rule 7.1-10
- Output 12: PDF/UA rule 7.1-11
- Output 12: PDF/UA rule 7.1-3
- Output 12: PDF/UA rule 7.1-8
- Output 12: PDF/UA rule 7.18.5-1
- Output 12: PDF/UA rule 7.2-24
- Output 12: PDF/UA rule 7.2-30
- Output 12: PDF/UA rule 7.2-34
- Output 13: PDF/UA rule 6.2-1
- Output 13: PDF/UA rule 7.1-10
- Output 13: PDF/UA rule 7.1-11
- Output 13: PDF/UA rule 7.1-3
- Output 13: PDF/UA rule 7.1-8
- Output 13: PDF/UA rule 7.18.5-1
- Output 13: PDF/UA rule 7.2-24
- Output 13: PDF/UA rule 7.2-30
- Output 13: PDF/UA rule 7.2-34
- Output 14: PDF/UA rule 6.2-1
- Output 14: PDF/UA rule 7.1-10
- Output 14: PDF/UA rule 7.1-11
- Output 14: PDF/UA rule 7.1-3
- Output 14: PDF/UA rule 7.1-8
- Output 14: PDF/UA rule 7.18.5-1
- Output 14: PDF/UA rule 7.2-24
- Output 14: PDF/UA rule 7.2-30
- Output 14: PDF/UA rule 7.2-34
- Output 15: PDF/UA rule 6.2-1
- Output 15: PDF/UA rule 7.1-10
- Output 15: PDF/UA rule 7.1-11
- Output 15: PDF/UA rule 7.1-3
- Output 15: PDF/UA rule 7.1-8
- Output 15: PDF/UA rule 7.18.5-1
- Output 15: PDF/UA rule 7.2-24
- Output 15: PDF/UA rule 7.2-30
- Output 15: PDF/UA rule 7.2-34
- Output 16: PDF/UA rule 6.2-1
- Output 16: PDF/UA rule 7.1-10
- Output 16: PDF/UA rule 7.1-11
- Output 16: PDF/UA rule 7.1-3
- Output 16: PDF/UA rule 7.1-8
- Output 16: PDF/UA rule 7.2-30
- Output 16: PDF/UA rule 7.2-34
- Output 17: PDF/UA rule 6.2-1
- Output 17: PDF/UA rule 7.1-10
- Output 17: PDF/UA rule 7.1-11
- Output 17: PDF/UA rule 7.1-3
- Output 17: PDF/UA rule 7.1-8
- Output 17: PDF/UA rule 7.18.5-1
- Output 17: PDF/UA rule 7.2-24
- Output 17: PDF/UA rule 7.2-30
- Output 17: PDF/UA rule 7.2-34
- Output 18: PDF/UA rule 6.2-1
- Output 18: PDF/UA rule 7.1-10
- Output 18: PDF/UA rule 7.1-11
- Output 18: PDF/UA rule 7.1-3
- Output 18: PDF/UA rule 7.1-8
- Output 18: PDF/UA rule 7.2-30
- Output 18: PDF/UA rule 7.2-34
- Output 19: PDF/UA rule 6.2-1
- Output 19: PDF/UA rule 7.1-10
- Output 19: PDF/UA rule 7.1-11
- Output 19: PDF/UA rule 7.1-3
- Output 19: PDF/UA rule 7.1-8
- Output 19: PDF/UA rule 7.2-30
- Output 19: PDF/UA rule 7.2-34
- Output 20: PDF/UA rule 6.2-1
- Output 20: PDF/UA rule 7.1-10
- Output 20: PDF/UA rule 7.1-11
- Output 20: PDF/UA rule 7.1-3
- Output 20: PDF/UA rule 7.1-8
- Output 20: PDF/UA rule 7.2-30
- Output 20: PDF/UA rule 7.2-34
- Output 21: PDF/UA rule 6.2-1
- Output 21: PDF/UA rule 7.1-10
- Output 21: PDF/UA rule 7.1-11
- Output 21: PDF/UA rule 7.1-3
- Output 21: PDF/UA rule 7.1-8
- Output 21: PDF/UA rule 7.2-30
- Output 21: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 5 → 0
- role_map_count: 5 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 22 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-ref-2-05-bookchapter-german --output lab/reproduction.json
```

### ua1-ref-2-05-bookchapter-german-pymupdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.1-2
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.18.5-2
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 9 → 0
- role_map_count: 13 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 34 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-ref-2-05-bookchapter-german --output lab/reproduction.json
```

### ua1-ref-2-05-bookchapter-german-pymupdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-34
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.1-8
- Output 2: PDF/UA rule 7.2-30
- Output 2: PDF/UA rule 7.2-34
- Output 3: PDF/UA rule 6.2-1
- Output 3: PDF/UA rule 7.1-10
- Output 3: PDF/UA rule 7.1-11
- Output 3: PDF/UA rule 7.1-3
- Output 3: PDF/UA rule 7.1-8
- Output 3: PDF/UA rule 7.2-30
- Output 3: PDF/UA rule 7.2-34
- Output 4: PDF/UA rule 6.2-1
- Output 4: PDF/UA rule 7.1-10
- Output 4: PDF/UA rule 7.1-11
- Output 4: PDF/UA rule 7.1-3
- Output 4: PDF/UA rule 7.1-8
- Output 4: PDF/UA rule 7.18.1-2
- Output 4: PDF/UA rule 7.18.3-1
- Output 4: PDF/UA rule 7.18.5-1
- Output 4: PDF/UA rule 7.18.5-2
- Output 4: PDF/UA rule 7.2-30
- Output 4: PDF/UA rule 7.2-34
- Output 5: PDF/UA rule 6.2-1
- Output 5: PDF/UA rule 7.1-10
- Output 5: PDF/UA rule 7.1-11
- Output 5: PDF/UA rule 7.1-3
- Output 5: PDF/UA rule 7.1-8
- Output 5: PDF/UA rule 7.2-30
- Output 5: PDF/UA rule 7.2-34
- Output 6: PDF/UA rule 6.2-1
- Output 6: PDF/UA rule 7.1-10
- Output 6: PDF/UA rule 7.1-11
- Output 6: PDF/UA rule 7.1-3
- Output 6: PDF/UA rule 7.1-8
- Output 6: PDF/UA rule 7.2-30
- Output 6: PDF/UA rule 7.2-34
- Output 7: PDF/UA rule 6.2-1
- Output 7: PDF/UA rule 7.1-10
- Output 7: PDF/UA rule 7.1-11
- Output 7: PDF/UA rule 7.1-3
- Output 7: PDF/UA rule 7.1-8
- Output 7: PDF/UA rule 7.2-30
- Output 7: PDF/UA rule 7.2-34
- Output 8: PDF/UA rule 6.2-1
- Output 8: PDF/UA rule 7.1-10
- Output 8: PDF/UA rule 7.1-11
- Output 8: PDF/UA rule 7.1-3
- Output 8: PDF/UA rule 7.1-8
- Output 8: PDF/UA rule 7.2-30
- Output 8: PDF/UA rule 7.2-33
- Output 8: PDF/UA rule 7.2-34
- Output 9: PDF/UA rule 6.2-1
- Output 9: PDF/UA rule 7.1-10
- Output 9: PDF/UA rule 7.1-11
- Output 9: PDF/UA rule 7.1-3
- Output 9: PDF/UA rule 7.1-8
- Output 9: PDF/UA rule 7.2-30
- Output 9: PDF/UA rule 7.2-34
- Output 10: PDF/UA rule 6.2-1
- Output 10: PDF/UA rule 7.1-10
- Output 10: PDF/UA rule 7.1-11
- Output 10: PDF/UA rule 7.1-3
- Output 10: PDF/UA rule 7.1-8
- Output 10: PDF/UA rule 7.2-30
- Output 10: PDF/UA rule 7.2-34
- Output 11: PDF/UA rule 6.2-1
- Output 11: PDF/UA rule 7.1-10
- Output 11: PDF/UA rule 7.1-11
- Output 11: PDF/UA rule 7.1-3
- Output 11: PDF/UA rule 7.1-8
- Output 11: PDF/UA rule 7.18.1-2
- Output 11: PDF/UA rule 7.18.3-1
- Output 11: PDF/UA rule 7.18.5-1
- Output 11: PDF/UA rule 7.18.5-2
- Output 11: PDF/UA rule 7.2-30
- Output 11: PDF/UA rule 7.2-34
- Output 12: PDF/UA rule 6.2-1
- Output 12: PDF/UA rule 7.1-10
- Output 12: PDF/UA rule 7.1-11
- Output 12: PDF/UA rule 7.1-3
- Output 12: PDF/UA rule 7.1-8
- Output 12: PDF/UA rule 7.18.1-2
- Output 12: PDF/UA rule 7.18.3-1
- Output 12: PDF/UA rule 7.18.5-1
- Output 12: PDF/UA rule 7.18.5-2
- Output 12: PDF/UA rule 7.2-30
- Output 12: PDF/UA rule 7.2-34
- Output 13: PDF/UA rule 6.2-1
- Output 13: PDF/UA rule 7.1-10
- Output 13: PDF/UA rule 7.1-11
- Output 13: PDF/UA rule 7.1-3
- Output 13: PDF/UA rule 7.1-8
- Output 13: PDF/UA rule 7.18.1-2
- Output 13: PDF/UA rule 7.18.3-1
- Output 13: PDF/UA rule 7.18.5-1
- Output 13: PDF/UA rule 7.18.5-2
- Output 13: PDF/UA rule 7.2-30
- Output 13: PDF/UA rule 7.2-34
- Output 14: PDF/UA rule 6.2-1
- Output 14: PDF/UA rule 7.1-10
- Output 14: PDF/UA rule 7.1-11
- Output 14: PDF/UA rule 7.1-3
- Output 14: PDF/UA rule 7.1-8
- Output 14: PDF/UA rule 7.18.1-2
- Output 14: PDF/UA rule 7.18.3-1
- Output 14: PDF/UA rule 7.18.5-1
- Output 14: PDF/UA rule 7.18.5-2
- Output 14: PDF/UA rule 7.2-30
- Output 14: PDF/UA rule 7.2-34
- Output 15: PDF/UA rule 6.2-1
- Output 15: PDF/UA rule 7.1-10
- Output 15: PDF/UA rule 7.1-11
- Output 15: PDF/UA rule 7.1-3
- Output 15: PDF/UA rule 7.1-8
- Output 15: PDF/UA rule 7.18.1-2
- Output 15: PDF/UA rule 7.18.3-1
- Output 15: PDF/UA rule 7.18.5-1
- Output 15: PDF/UA rule 7.18.5-2
- Output 15: PDF/UA rule 7.2-30
- Output 15: PDF/UA rule 7.2-34
- Output 16: PDF/UA rule 6.2-1
- Output 16: PDF/UA rule 7.1-10
- Output 16: PDF/UA rule 7.1-11
- Output 16: PDF/UA rule 7.1-3
- Output 16: PDF/UA rule 7.1-8
- Output 16: PDF/UA rule 7.2-30
- Output 16: PDF/UA rule 7.2-34
- Output 17: PDF/UA rule 6.2-1
- Output 17: PDF/UA rule 7.1-10
- Output 17: PDF/UA rule 7.1-11
- Output 17: PDF/UA rule 7.1-3
- Output 17: PDF/UA rule 7.1-8
- Output 17: PDF/UA rule 7.18.1-2
- Output 17: PDF/UA rule 7.18.3-1
- Output 17: PDF/UA rule 7.18.5-1
- Output 17: PDF/UA rule 7.18.5-2
- Output 17: PDF/UA rule 7.2-30
- Output 17: PDF/UA rule 7.2-34
- Output 18: PDF/UA rule 6.2-1
- Output 18: PDF/UA rule 7.1-10
- Output 18: PDF/UA rule 7.1-11
- Output 18: PDF/UA rule 7.1-3
- Output 18: PDF/UA rule 7.1-8
- Output 18: PDF/UA rule 7.2-30
- Output 18: PDF/UA rule 7.2-34
- Output 19: PDF/UA rule 6.2-1
- Output 19: PDF/UA rule 7.1-10
- Output 19: PDF/UA rule 7.1-11
- Output 19: PDF/UA rule 7.1-3
- Output 19: PDF/UA rule 7.1-8
- Output 19: PDF/UA rule 7.2-30
- Output 19: PDF/UA rule 7.2-34
- Output 20: PDF/UA rule 6.2-1
- Output 20: PDF/UA rule 7.1-10
- Output 20: PDF/UA rule 7.1-11
- Output 20: PDF/UA rule 7.1-3
- Output 20: PDF/UA rule 7.1-8
- Output 20: PDF/UA rule 7.2-30
- Output 20: PDF/UA rule 7.2-34
- Output 21: PDF/UA rule 6.2-1
- Output 21: PDF/UA rule 7.1-10
- Output 21: PDF/UA rule 7.1-11
- Output 21: PDF/UA rule 7.1-3
- Output 21: PDF/UA rule 7.1-8
- Output 21: PDF/UA rule 7.2-30
- Output 21: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 5 → 0
- role_map_count: 5 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 22 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-ref-2-05-bookchapter-german --output lab/reproduction.json
```

### ua1-ref-2-05-bookchapter-german-ghostscript-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 1: PDF/UA rule 7.21.4.2-2
- Output 1: PDF/UA rule 7.21.7-1
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 9 → 0
- role_map_count: 13 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-ref-2-05-bookchapter-german --output lab/reproduction.json
```

### ua1-ref-2-05-bookchapter-german-ghostscript-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 1: PDF/UA rule 7.21.7-1
- Output 2: PDF/UA rule 5-1
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.2-30
- Output 2: PDF/UA rule 7.2-33
- Output 2: PDF/UA rule 7.2-34
- Output 2: PDF/UA rule 7.21.7-1
- Output 3: PDF/UA rule 5-1
- Output 3: PDF/UA rule 6.2-1
- Output 3: PDF/UA rule 7.1-10
- Output 3: PDF/UA rule 7.1-11
- Output 3: PDF/UA rule 7.1-3
- Output 3: PDF/UA rule 7.2-30
- Output 3: PDF/UA rule 7.2-33
- Output 3: PDF/UA rule 7.2-34
- Output 3: PDF/UA rule 7.21.7-1
- Output 4: PDF/UA rule 5-1
- Output 4: PDF/UA rule 6.2-1
- Output 4: PDF/UA rule 7.1-10
- Output 4: PDF/UA rule 7.1-11
- Output 4: PDF/UA rule 7.1-3
- Output 4: PDF/UA rule 7.18.3-1
- Output 4: PDF/UA rule 7.18.5-1
- Output 4: PDF/UA rule 7.2-24
- Output 4: PDF/UA rule 7.2-30
- Output 4: PDF/UA rule 7.2-33
- Output 4: PDF/UA rule 7.2-34
- Output 4: PDF/UA rule 7.21.7-1
- Output 5: PDF/UA rule 5-1
- Output 5: PDF/UA rule 6.2-1
- Output 5: PDF/UA rule 7.1-10
- Output 5: PDF/UA rule 7.1-11
- Output 5: PDF/UA rule 7.1-3
- Output 5: PDF/UA rule 7.2-30
- Output 5: PDF/UA rule 7.2-33
- Output 5: PDF/UA rule 7.2-34
- Output 5: PDF/UA rule 7.21.4.2-2
- Output 5: PDF/UA rule 7.21.7-1
- Output 6: PDF/UA rule 5-1
- Output 6: PDF/UA rule 6.2-1
- Output 6: PDF/UA rule 7.1-10
- Output 6: PDF/UA rule 7.1-11
- Output 6: PDF/UA rule 7.1-3
- Output 6: PDF/UA rule 7.2-30
- Output 6: PDF/UA rule 7.2-33
- Output 6: PDF/UA rule 7.2-34
- Output 6: PDF/UA rule 7.21.7-1
- Output 7: PDF/UA rule 5-1
- Output 7: PDF/UA rule 6.2-1
- Output 7: PDF/UA rule 7.1-10
- Output 7: PDF/UA rule 7.1-11
- Output 7: PDF/UA rule 7.1-3
- Output 7: PDF/UA rule 7.2-30
- Output 7: PDF/UA rule 7.2-33
- Output 7: PDF/UA rule 7.2-34
- Output 7: PDF/UA rule 7.21.7-1
- Output 8: PDF/UA rule 5-1
- Output 8: PDF/UA rule 6.2-1
- Output 8: PDF/UA rule 7.1-10
- Output 8: PDF/UA rule 7.1-11
- Output 8: PDF/UA rule 7.1-3
- Output 8: PDF/UA rule 7.2-30
- Output 8: PDF/UA rule 7.2-33
- Output 8: PDF/UA rule 7.2-34
- Output 8: PDF/UA rule 7.21.7-1
- Output 9: PDF/UA rule 5-1
- Output 9: PDF/UA rule 6.2-1
- Output 9: PDF/UA rule 7.1-10
- Output 9: PDF/UA rule 7.1-11
- Output 9: PDF/UA rule 7.1-3
- Output 9: PDF/UA rule 7.2-30
- Output 9: PDF/UA rule 7.2-33
- Output 9: PDF/UA rule 7.2-34
- Output 9: PDF/UA rule 7.21.7-1
- Output 10: PDF/UA rule 5-1
- Output 10: PDF/UA rule 6.2-1
- Output 10: PDF/UA rule 7.1-10
- Output 10: PDF/UA rule 7.1-11
- Output 10: PDF/UA rule 7.1-3
- Output 10: PDF/UA rule 7.2-30
- Output 10: PDF/UA rule 7.2-33
- Output 10: PDF/UA rule 7.2-34
- Output 10: PDF/UA rule 7.21.7-1
- Output 11: PDF/UA rule 5-1
- Output 11: PDF/UA rule 6.2-1
- Output 11: PDF/UA rule 7.1-10
- Output 11: PDF/UA rule 7.1-11
- Output 11: PDF/UA rule 7.1-3
- Output 11: PDF/UA rule 7.18.3-1
- Output 11: PDF/UA rule 7.18.5-1
- Output 11: PDF/UA rule 7.2-24
- Output 11: PDF/UA rule 7.2-30
- Output 11: PDF/UA rule 7.2-33
- Output 11: PDF/UA rule 7.2-34
- Output 11: PDF/UA rule 7.21.4.2-2
- Output 11: PDF/UA rule 7.21.7-1
- Output 12: PDF/UA rule 5-1
- Output 12: PDF/UA rule 6.2-1
- Output 12: PDF/UA rule 7.1-10
- Output 12: PDF/UA rule 7.1-11
- Output 12: PDF/UA rule 7.1-3
- Output 12: PDF/UA rule 7.18.3-1
- Output 12: PDF/UA rule 7.18.5-1
- Output 12: PDF/UA rule 7.2-24
- Output 12: PDF/UA rule 7.2-30
- Output 12: PDF/UA rule 7.2-33
- Output 12: PDF/UA rule 7.2-34
- Output 12: PDF/UA rule 7.21.7-1
- Output 13: PDF/UA rule 5-1
- Output 13: PDF/UA rule 6.2-1
- Output 13: PDF/UA rule 7.1-10
- Output 13: PDF/UA rule 7.1-11
- Output 13: PDF/UA rule 7.1-3
- Output 13: PDF/UA rule 7.18.3-1
- Output 13: PDF/UA rule 7.18.5-1
- Output 13: PDF/UA rule 7.2-24
- Output 13: PDF/UA rule 7.2-30
- Output 13: PDF/UA rule 7.2-33
- Output 13: PDF/UA rule 7.2-34
- Output 13: PDF/UA rule 7.21.4.2-2
- Output 13: PDF/UA rule 7.21.7-1
- Output 14: PDF/UA rule 5-1
- Output 14: PDF/UA rule 6.2-1
- Output 14: PDF/UA rule 7.1-10
- Output 14: PDF/UA rule 7.1-11
- Output 14: PDF/UA rule 7.1-3
- Output 14: PDF/UA rule 7.18.3-1
- Output 14: PDF/UA rule 7.18.5-1
- Output 14: PDF/UA rule 7.2-24
- Output 14: PDF/UA rule 7.2-30
- Output 14: PDF/UA rule 7.2-33
- Output 14: PDF/UA rule 7.2-34
- Output 14: PDF/UA rule 7.21.4.2-2
- Output 14: PDF/UA rule 7.21.7-1
- Output 15: PDF/UA rule 5-1
- Output 15: PDF/UA rule 6.2-1
- Output 15: PDF/UA rule 7.1-10
- Output 15: PDF/UA rule 7.1-11
- Output 15: PDF/UA rule 7.1-3
- Output 15: PDF/UA rule 7.18.3-1
- Output 15: PDF/UA rule 7.18.5-1
- Output 15: PDF/UA rule 7.2-24
- Output 15: PDF/UA rule 7.2-30
- Output 15: PDF/UA rule 7.2-33
- Output 15: PDF/UA rule 7.2-34
- Output 15: PDF/UA rule 7.21.4.2-2
- Output 15: PDF/UA rule 7.21.7-1
- Output 16: PDF/UA rule 5-1
- Output 16: PDF/UA rule 6.2-1
- Output 16: PDF/UA rule 7.1-10
- Output 16: PDF/UA rule 7.1-11
- Output 16: PDF/UA rule 7.1-3
- Output 16: PDF/UA rule 7.2-30
- Output 16: PDF/UA rule 7.2-33
- Output 16: PDF/UA rule 7.2-34
- Output 16: PDF/UA rule 7.21.4.2-2
- Output 16: PDF/UA rule 7.21.7-1
- Output 17: PDF/UA rule 5-1
- Output 17: PDF/UA rule 6.2-1
- Output 17: PDF/UA rule 7.1-10
- Output 17: PDF/UA rule 7.1-11
- Output 17: PDF/UA rule 7.1-3
- Output 17: PDF/UA rule 7.18.3-1
- Output 17: PDF/UA rule 7.18.5-1
- Output 17: PDF/UA rule 7.2-24
- Output 17: PDF/UA rule 7.2-30
- Output 17: PDF/UA rule 7.2-33
- Output 17: PDF/UA rule 7.2-34
- Output 17: PDF/UA rule 7.21.4.2-2
- Output 17: PDF/UA rule 7.21.7-1
- Output 18: PDF/UA rule 5-1
- Output 18: PDF/UA rule 6.2-1
- Output 18: PDF/UA rule 7.1-10
- Output 18: PDF/UA rule 7.1-11
- Output 18: PDF/UA rule 7.1-3
- Output 18: PDF/UA rule 7.2-30
- Output 18: PDF/UA rule 7.2-33
- Output 18: PDF/UA rule 7.2-34
- Output 18: PDF/UA rule 7.21.7-1
- Output 19: PDF/UA rule 5-1
- Output 19: PDF/UA rule 6.2-1
- Output 19: PDF/UA rule 7.1-10
- Output 19: PDF/UA rule 7.1-11
- Output 19: PDF/UA rule 7.1-3
- Output 19: PDF/UA rule 7.2-30
- Output 19: PDF/UA rule 7.2-33
- Output 19: PDF/UA rule 7.2-34
- Output 19: PDF/UA rule 7.21.7-1
- Output 20: PDF/UA rule 5-1
- Output 20: PDF/UA rule 6.2-1
- Output 20: PDF/UA rule 7.1-10
- Output 20: PDF/UA rule 7.1-11
- Output 20: PDF/UA rule 7.1-3
- Output 20: PDF/UA rule 7.2-30
- Output 20: PDF/UA rule 7.2-33
- Output 20: PDF/UA rule 7.2-34
- Output 20: PDF/UA rule 7.21.7-1
- Output 21: PDF/UA rule 5-1
- Output 21: PDF/UA rule 6.2-1
- Output 21: PDF/UA rule 7.1-10
- Output 21: PDF/UA rule 7.1-11
- Output 21: PDF/UA rule 7.1-3
- Output 21: PDF/UA rule 7.2-30
- Output 21: PDF/UA rule 7.2-33
- Output 21: PDF/UA rule 7.2-34
- Output 21: PDF/UA rule 7.21.7-1
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 5 → 0
- role_map_count: 5 → 0
- document_language_present: True → False
- outline_count: 22 → 1

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-ref-2-05-bookchapter-german --output lab/reproduction.json
```

### ua1-ref-2-05-bookchapter-german-ghostscript-resave

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 1: PDF/UA rule 7.21.4.2-2
- Output 1: PDF/UA rule 7.21.7-1
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 5 → 0
- role_map_count: 5 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-ref-2-05-bookchapter-german --output lab/reproduction.json
```

### ua1-ref-2-06-brochure-qpdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 17 → 0
- role_map_count: 8 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 65 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-ref-2-06-brochure --output lab/reproduction.json
```

### ua1-ref-2-06-brochure-qpdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-34
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.1-8
- Output 2: PDF/UA rule 7.18.5-1
- Output 2: PDF/UA rule 7.2-24
- Output 2: PDF/UA rule 7.2-30
- Output 2: PDF/UA rule 7.2-33
- Output 2: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 4 → 0
- role_map_count: 8 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 12 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-ref-2-06-brochure --output lab/reproduction.json
```

### ua1-ref-2-06-brochure-pymupdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.1-2
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.18.5-2
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 17 → 0
- role_map_count: 8 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 65 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-ref-2-06-brochure --output lab/reproduction.json
```

### ua1-ref-2-06-brochure-pymupdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.1-2
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.18.5-2
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-34
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.1-8
- Output 2: PDF/UA rule 7.18.1-2
- Output 2: PDF/UA rule 7.18.3-1
- Output 2: PDF/UA rule 7.18.5-1
- Output 2: PDF/UA rule 7.18.5-2
- Output 2: PDF/UA rule 7.2-30
- Output 2: PDF/UA rule 7.2-33
- Output 2: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 4 → 0
- role_map_count: 8 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 12 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-ref-2-06-brochure --output lab/reproduction.json
```

### ua1-ref-2-06-brochure-ghostscript-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 1: PDF/UA rule 7.21.4.2-2
- Output 1: PDF/UA rule 7.21.7-1
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 17 → 0
- role_map_count: 8 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-ref-2-06-brochure --output lab/reproduction.json
```

### ua1-ref-2-06-brochure-ghostscript-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 1: PDF/UA rule 7.21.4.2-2
- Output 1: PDF/UA rule 7.21.7-1
- Output 2: PDF/UA rule 5-1
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.18.3-1
- Output 2: PDF/UA rule 7.18.5-1
- Output 2: PDF/UA rule 7.2-24
- Output 2: PDF/UA rule 7.2-30
- Output 2: PDF/UA rule 7.2-33
- Output 2: PDF/UA rule 7.2-34
- Output 2: PDF/UA rule 7.21.4.2-2
- Output 2: PDF/UA rule 7.21.7-1
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 4 → 0
- role_map_count: 8 → 0
- document_language_present: True → False
- outline_count: 12 → 1

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-ref-2-06-brochure --output lab/reproduction.json
```

### ua1-ref-2-06-brochure-ghostscript-resave

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 1: PDF/UA rule 7.21.4.2-2
- Output 1: PDF/UA rule 7.21.7-1
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 4 → 0
- role_map_count: 8 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-ref-2-06-brochure --output lab/reproduction.json
```

### ua1-ref-2-08-bookchapter-qpdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 576 → 0
- role_map_count: 3 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 373 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-ref-2-08-bookchapter --output lab/reproduction.json
```

### ua1-ref-2-08-bookchapter-qpdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-34
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.1-8
- Output 2: PDF/UA rule 7.2-34
- Output 3: PDF/UA rule 6.2-1
- Output 3: PDF/UA rule 7.1-10
- Output 3: PDF/UA rule 7.1-11
- Output 3: PDF/UA rule 7.1-3
- Output 3: PDF/UA rule 7.1-8
- Output 3: PDF/UA rule 7.2-34
- Output 4: PDF/UA rule 6.2-1
- Output 4: PDF/UA rule 7.1-10
- Output 4: PDF/UA rule 7.1-11
- Output 4: PDF/UA rule 7.1-3
- Output 4: PDF/UA rule 7.1-8
- Output 4: PDF/UA rule 7.2-34
- Output 5: PDF/UA rule 6.2-1
- Output 5: PDF/UA rule 7.1-10
- Output 5: PDF/UA rule 7.1-11
- Output 5: PDF/UA rule 7.1-3
- Output 5: PDF/UA rule 7.1-8
- Output 5: PDF/UA rule 7.2-34
- Output 6: PDF/UA rule 6.2-1
- Output 6: PDF/UA rule 7.1-10
- Output 6: PDF/UA rule 7.1-11
- Output 6: PDF/UA rule 7.1-3
- Output 6: PDF/UA rule 7.1-8
- Output 6: PDF/UA rule 7.2-34
- Output 7: PDF/UA rule 6.2-1
- Output 7: PDF/UA rule 7.1-10
- Output 7: PDF/UA rule 7.1-11
- Output 7: PDF/UA rule 7.1-3
- Output 7: PDF/UA rule 7.1-8
- Output 7: PDF/UA rule 7.2-34
- Output 8: PDF/UA rule 6.2-1
- Output 8: PDF/UA rule 7.1-10
- Output 8: PDF/UA rule 7.1-11
- Output 8: PDF/UA rule 7.1-3
- Output 8: PDF/UA rule 7.1-8
- Output 8: PDF/UA rule 7.2-34
- Output 9: PDF/UA rule 6.2-1
- Output 9: PDF/UA rule 7.1-10
- Output 9: PDF/UA rule 7.1-11
- Output 9: PDF/UA rule 7.1-3
- Output 9: PDF/UA rule 7.1-8
- Output 9: PDF/UA rule 7.2-34
- Output 10: PDF/UA rule 6.2-1
- Output 10: PDF/UA rule 7.1-10
- Output 10: PDF/UA rule 7.1-11
- Output 10: PDF/UA rule 7.1-3
- Output 10: PDF/UA rule 7.1-8
- Output 10: PDF/UA rule 7.2-34
- Output 11: PDF/UA rule 6.2-1
- Output 11: PDF/UA rule 7.1-10
- Output 11: PDF/UA rule 7.1-11
- Output 11: PDF/UA rule 7.1-3
- Output 11: PDF/UA rule 7.1-8
- Output 11: PDF/UA rule 7.2-34
- Output 12: PDF/UA rule 6.2-1
- Output 12: PDF/UA rule 7.1-10
- Output 12: PDF/UA rule 7.1-11
- Output 12: PDF/UA rule 7.1-3
- Output 12: PDF/UA rule 7.1-8
- Output 12: PDF/UA rule 7.2-34
- Output 13: PDF/UA rule 6.2-1
- Output 13: PDF/UA rule 7.1-10
- Output 13: PDF/UA rule 7.1-11
- Output 13: PDF/UA rule 7.1-3
- Output 13: PDF/UA rule 7.1-8
- Output 13: PDF/UA rule 7.2-34
- Output 14: PDF/UA rule 6.2-1
- Output 14: PDF/UA rule 7.1-10
- Output 14: PDF/UA rule 7.1-11
- Output 14: PDF/UA rule 7.1-3
- Output 14: PDF/UA rule 7.1-8
- Output 14: PDF/UA rule 7.2-34
- Output 15: PDF/UA rule 6.2-1
- Output 15: PDF/UA rule 7.1-10
- Output 15: PDF/UA rule 7.1-11
- Output 15: PDF/UA rule 7.1-3
- Output 15: PDF/UA rule 7.1-8
- Output 15: PDF/UA rule 7.2-34
- Output 16: PDF/UA rule 6.2-1
- Output 16: PDF/UA rule 7.1-10
- Output 16: PDF/UA rule 7.1-11
- Output 16: PDF/UA rule 7.1-3
- Output 16: PDF/UA rule 7.1-8
- Output 16: PDF/UA rule 7.2-34
- Output 17: PDF/UA rule 6.2-1
- Output 17: PDF/UA rule 7.1-10
- Output 17: PDF/UA rule 7.1-11
- Output 17: PDF/UA rule 7.1-3
- Output 17: PDF/UA rule 7.1-8
- Output 17: PDF/UA rule 7.2-34
- Output 18: PDF/UA rule 6.2-1
- Output 18: PDF/UA rule 7.1-10
- Output 18: PDF/UA rule 7.1-11
- Output 18: PDF/UA rule 7.1-3
- Output 18: PDF/UA rule 7.1-8
- Output 18: PDF/UA rule 7.2-34
- Output 19: PDF/UA rule 6.2-1
- Output 19: PDF/UA rule 7.1-10
- Output 19: PDF/UA rule 7.1-11
- Output 19: PDF/UA rule 7.1-3
- Output 19: PDF/UA rule 7.1-8
- Output 19: PDF/UA rule 7.2-34
- Output 20: PDF/UA rule 6.2-1
- Output 20: PDF/UA rule 7.1-10
- Output 20: PDF/UA rule 7.1-11
- Output 20: PDF/UA rule 7.1-3
- Output 20: PDF/UA rule 7.1-8
- Output 20: PDF/UA rule 7.2-34
- Output 21: PDF/UA rule 6.2-1
- Output 21: PDF/UA rule 7.1-10
- Output 21: PDF/UA rule 7.1-11
- Output 21: PDF/UA rule 7.1-3
- Output 21: PDF/UA rule 7.1-8
- Output 21: PDF/UA rule 7.2-34
- Output 22: PDF/UA rule 6.2-1
- Output 22: PDF/UA rule 7.1-10
- Output 22: PDF/UA rule 7.1-11
- Output 22: PDF/UA rule 7.1-3
- Output 22: PDF/UA rule 7.1-8
- Output 22: PDF/UA rule 7.2-34
- Output 23: PDF/UA rule 6.2-1
- Output 23: PDF/UA rule 7.1-10
- Output 23: PDF/UA rule 7.1-11
- Output 23: PDF/UA rule 7.1-3
- Output 23: PDF/UA rule 7.1-8
- Output 23: PDF/UA rule 7.2-34
- Output 24: PDF/UA rule 6.2-1
- Output 24: PDF/UA rule 7.1-10
- Output 24: PDF/UA rule 7.1-11
- Output 24: PDF/UA rule 7.1-3
- Output 24: PDF/UA rule 7.1-8
- Output 24: PDF/UA rule 7.2-34
- Output 25: PDF/UA rule 6.2-1
- Output 25: PDF/UA rule 7.1-10
- Output 25: PDF/UA rule 7.1-11
- Output 25: PDF/UA rule 7.1-3
- Output 25: PDF/UA rule 7.1-8
- Output 25: PDF/UA rule 7.2-34
- Output 26: PDF/UA rule 6.2-1
- Output 26: PDF/UA rule 7.1-10
- Output 26: PDF/UA rule 7.1-11
- Output 26: PDF/UA rule 7.1-3
- Output 26: PDF/UA rule 7.1-8
- Output 26: PDF/UA rule 7.2-34
- Output 27: PDF/UA rule 6.2-1
- Output 27: PDF/UA rule 7.1-10
- Output 27: PDF/UA rule 7.1-11
- Output 27: PDF/UA rule 7.1-3
- Output 27: PDF/UA rule 7.1-8
- Output 27: PDF/UA rule 7.2-34
- Output 28: PDF/UA rule 6.2-1
- Output 28: PDF/UA rule 7.1-10
- Output 28: PDF/UA rule 7.1-11
- Output 28: PDF/UA rule 7.1-3
- Output 28: PDF/UA rule 7.1-8
- Output 28: PDF/UA rule 7.2-34
- Output 29: PDF/UA rule 6.2-1
- Output 29: PDF/UA rule 7.1-10
- Output 29: PDF/UA rule 7.1-11
- Output 29: PDF/UA rule 7.1-3
- Output 29: PDF/UA rule 7.1-8
- Output 29: PDF/UA rule 7.2-34
- Output 30: PDF/UA rule 6.2-1
- Output 30: PDF/UA rule 7.1-10
- Output 30: PDF/UA rule 7.1-11
- Output 30: PDF/UA rule 7.1-3
- Output 30: PDF/UA rule 7.1-8
- Output 30: PDF/UA rule 7.2-34
- Output 31: PDF/UA rule 6.2-1
- Output 31: PDF/UA rule 7.1-10
- Output 31: PDF/UA rule 7.1-11
- Output 31: PDF/UA rule 7.1-3
- Output 31: PDF/UA rule 7.1-8
- Output 31: PDF/UA rule 7.18.5-1
- Output 31: PDF/UA rule 7.2-24
- Output 31: PDF/UA rule 7.2-34
- Output 32: PDF/UA rule 6.2-1
- Output 32: PDF/UA rule 7.1-10
- Output 32: PDF/UA rule 7.1-11
- Output 32: PDF/UA rule 7.1-3
- Output 32: PDF/UA rule 7.1-8
- Output 32: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 13 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 53 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-ref-2-08-bookchapter --output lab/reproduction.json
```

### ua1-ref-2-08-bookchapter-pymupdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.1-2
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.18.5-2
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 576 → 0
- role_map_count: 3 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 373 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-ref-2-08-bookchapter --output lab/reproduction.json
```

### ua1-ref-2-08-bookchapter-pymupdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.1-8
- Output 2: PDF/UA rule 7.2-34
- Output 3: PDF/UA rule 6.2-1
- Output 3: PDF/UA rule 7.1-10
- Output 3: PDF/UA rule 7.1-11
- Output 3: PDF/UA rule 7.1-3
- Output 3: PDF/UA rule 7.1-8
- Output 3: PDF/UA rule 7.2-34
- Output 4: PDF/UA rule 6.2-1
- Output 4: PDF/UA rule 7.1-10
- Output 4: PDF/UA rule 7.1-11
- Output 4: PDF/UA rule 7.1-3
- Output 4: PDF/UA rule 7.1-8
- Output 4: PDF/UA rule 7.2-34
- Output 5: PDF/UA rule 6.2-1
- Output 5: PDF/UA rule 7.1-10
- Output 5: PDF/UA rule 7.1-11
- Output 5: PDF/UA rule 7.1-3
- Output 5: PDF/UA rule 7.1-8
- Output 5: PDF/UA rule 7.2-34
- Output 6: PDF/UA rule 6.2-1
- Output 6: PDF/UA rule 7.1-10
- Output 6: PDF/UA rule 7.1-11
- Output 6: PDF/UA rule 7.1-3
- Output 6: PDF/UA rule 7.1-8
- Output 6: PDF/UA rule 7.2-34
- Output 7: PDF/UA rule 6.2-1
- Output 7: PDF/UA rule 7.1-10
- Output 7: PDF/UA rule 7.1-11
- Output 7: PDF/UA rule 7.1-3
- Output 7: PDF/UA rule 7.1-8
- Output 7: PDF/UA rule 7.2-34
- Output 8: PDF/UA rule 6.2-1
- Output 8: PDF/UA rule 7.1-10
- Output 8: PDF/UA rule 7.1-11
- Output 8: PDF/UA rule 7.1-3
- Output 8: PDF/UA rule 7.1-8
- Output 8: PDF/UA rule 7.2-34
- Output 9: PDF/UA rule 6.2-1
- Output 9: PDF/UA rule 7.1-10
- Output 9: PDF/UA rule 7.1-11
- Output 9: PDF/UA rule 7.1-3
- Output 9: PDF/UA rule 7.1-8
- Output 9: PDF/UA rule 7.2-34
- Output 10: PDF/UA rule 6.2-1
- Output 10: PDF/UA rule 7.1-10
- Output 10: PDF/UA rule 7.1-11
- Output 10: PDF/UA rule 7.1-3
- Output 10: PDF/UA rule 7.1-8
- Output 10: PDF/UA rule 7.2-34
- Output 11: PDF/UA rule 6.2-1
- Output 11: PDF/UA rule 7.1-10
- Output 11: PDF/UA rule 7.1-11
- Output 11: PDF/UA rule 7.1-3
- Output 11: PDF/UA rule 7.1-8
- Output 11: PDF/UA rule 7.2-34
- Output 12: PDF/UA rule 6.2-1
- Output 12: PDF/UA rule 7.1-10
- Output 12: PDF/UA rule 7.1-11
- Output 12: PDF/UA rule 7.1-3
- Output 12: PDF/UA rule 7.1-8
- Output 12: PDF/UA rule 7.2-34
- Output 13: PDF/UA rule 6.2-1
- Output 13: PDF/UA rule 7.1-10
- Output 13: PDF/UA rule 7.1-11
- Output 13: PDF/UA rule 7.1-3
- Output 13: PDF/UA rule 7.1-8
- Output 13: PDF/UA rule 7.2-34
- Output 14: PDF/UA rule 6.2-1
- Output 14: PDF/UA rule 7.1-10
- Output 14: PDF/UA rule 7.1-11
- Output 14: PDF/UA rule 7.1-3
- Output 14: PDF/UA rule 7.1-8
- Output 14: PDF/UA rule 7.2-34
- Output 15: PDF/UA rule 6.2-1
- Output 15: PDF/UA rule 7.1-10
- Output 15: PDF/UA rule 7.1-11
- Output 15: PDF/UA rule 7.1-3
- Output 15: PDF/UA rule 7.1-8
- Output 15: PDF/UA rule 7.2-34
- Output 16: PDF/UA rule 6.2-1
- Output 16: PDF/UA rule 7.1-10
- Output 16: PDF/UA rule 7.1-11
- Output 16: PDF/UA rule 7.1-3
- Output 16: PDF/UA rule 7.1-8
- Output 16: PDF/UA rule 7.2-34
- Output 17: PDF/UA rule 6.2-1
- Output 17: PDF/UA rule 7.1-10
- Output 17: PDF/UA rule 7.1-11
- Output 17: PDF/UA rule 7.1-3
- Output 17: PDF/UA rule 7.1-8
- Output 17: PDF/UA rule 7.2-34
- Output 18: PDF/UA rule 6.2-1
- Output 18: PDF/UA rule 7.1-10
- Output 18: PDF/UA rule 7.1-11
- Output 18: PDF/UA rule 7.1-3
- Output 18: PDF/UA rule 7.1-8
- Output 18: PDF/UA rule 7.2-34
- Output 19: PDF/UA rule 6.2-1
- Output 19: PDF/UA rule 7.1-10
- Output 19: PDF/UA rule 7.1-11
- Output 19: PDF/UA rule 7.1-3
- Output 19: PDF/UA rule 7.1-8
- Output 19: PDF/UA rule 7.2-34
- Output 20: PDF/UA rule 6.2-1
- Output 20: PDF/UA rule 7.1-10
- Output 20: PDF/UA rule 7.1-11
- Output 20: PDF/UA rule 7.1-3
- Output 20: PDF/UA rule 7.1-8
- Output 20: PDF/UA rule 7.2-34
- Output 21: PDF/UA rule 6.2-1
- Output 21: PDF/UA rule 7.1-10
- Output 21: PDF/UA rule 7.1-11
- Output 21: PDF/UA rule 7.1-3
- Output 21: PDF/UA rule 7.1-8
- Output 21: PDF/UA rule 7.2-34
- Output 22: PDF/UA rule 6.2-1
- Output 22: PDF/UA rule 7.1-10
- Output 22: PDF/UA rule 7.1-11
- Output 22: PDF/UA rule 7.1-3
- Output 22: PDF/UA rule 7.1-8
- Output 22: PDF/UA rule 7.2-34
- Output 23: PDF/UA rule 6.2-1
- Output 23: PDF/UA rule 7.1-10
- Output 23: PDF/UA rule 7.1-11
- Output 23: PDF/UA rule 7.1-3
- Output 23: PDF/UA rule 7.1-8
- Output 23: PDF/UA rule 7.2-34
- Output 24: PDF/UA rule 6.2-1
- Output 24: PDF/UA rule 7.1-10
- Output 24: PDF/UA rule 7.1-11
- Output 24: PDF/UA rule 7.1-3
- Output 24: PDF/UA rule 7.1-8
- Output 24: PDF/UA rule 7.2-34
- Output 25: PDF/UA rule 6.2-1
- Output 25: PDF/UA rule 7.1-10
- Output 25: PDF/UA rule 7.1-11
- Output 25: PDF/UA rule 7.1-3
- Output 25: PDF/UA rule 7.1-8
- Output 25: PDF/UA rule 7.2-34
- Output 26: PDF/UA rule 6.2-1
- Output 26: PDF/UA rule 7.1-10
- Output 26: PDF/UA rule 7.1-11
- Output 26: PDF/UA rule 7.1-3
- Output 26: PDF/UA rule 7.1-8
- Output 26: PDF/UA rule 7.2-34
- Output 27: PDF/UA rule 6.2-1
- Output 27: PDF/UA rule 7.1-10
- Output 27: PDF/UA rule 7.1-11
- Output 27: PDF/UA rule 7.1-3
- Output 27: PDF/UA rule 7.1-8
- Output 27: PDF/UA rule 7.2-34
- Output 28: PDF/UA rule 6.2-1
- Output 28: PDF/UA rule 7.1-10
- Output 28: PDF/UA rule 7.1-11
- Output 28: PDF/UA rule 7.1-3
- Output 28: PDF/UA rule 7.1-8
- Output 28: PDF/UA rule 7.2-34
- Output 29: PDF/UA rule 6.2-1
- Output 29: PDF/UA rule 7.1-10
- Output 29: PDF/UA rule 7.1-11
- Output 29: PDF/UA rule 7.1-3
- Output 29: PDF/UA rule 7.1-8
- Output 29: PDF/UA rule 7.2-34
- Output 30: PDF/UA rule 6.2-1
- Output 30: PDF/UA rule 7.1-10
- Output 30: PDF/UA rule 7.1-11
- Output 30: PDF/UA rule 7.1-3
- Output 30: PDF/UA rule 7.1-8
- Output 30: PDF/UA rule 7.2-34
- Output 31: PDF/UA rule 6.2-1
- Output 31: PDF/UA rule 7.1-10
- Output 31: PDF/UA rule 7.1-11
- Output 31: PDF/UA rule 7.1-3
- Output 31: PDF/UA rule 7.1-8
- Output 31: PDF/UA rule 7.18.1-2
- Output 31: PDF/UA rule 7.18.3-1
- Output 31: PDF/UA rule 7.18.5-1
- Output 31: PDF/UA rule 7.18.5-2
- Output 31: PDF/UA rule 7.2-34
- Output 32: PDF/UA rule 6.2-1
- Output 32: PDF/UA rule 7.1-10
- Output 32: PDF/UA rule 7.1-11
- Output 32: PDF/UA rule 7.1-3
- Output 32: PDF/UA rule 7.1-8
- Output 32: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 13 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 53 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-ref-2-08-bookchapter --output lab/reproduction.json
```

### ua1-ref-2-08-bookchapter-ghostscript-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 1: PDF/UA rule 7.21.4.2-2
- Output 1: PDF/UA rule 7.21.7-1
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 576 → 0
- role_map_count: 3 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-ref-2-08-bookchapter --output lab/reproduction.json
```

### ua1-ref-2-08-bookchapter-ghostscript-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 1: PDF/UA rule 7.21.7-1
- Output 2: PDF/UA rule 5-1
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.2-33
- Output 2: PDF/UA rule 7.2-34
- Output 2: PDF/UA rule 7.21.7-1
- Output 3: PDF/UA rule 5-1
- Output 3: PDF/UA rule 6.2-1
- Output 3: PDF/UA rule 7.1-10
- Output 3: PDF/UA rule 7.1-11
- Output 3: PDF/UA rule 7.1-3
- Output 3: PDF/UA rule 7.2-33
- Output 3: PDF/UA rule 7.2-34
- Output 3: PDF/UA rule 7.21.7-1
- Output 4: PDF/UA rule 5-1
- Output 4: PDF/UA rule 6.2-1
- Output 4: PDF/UA rule 7.1-10
- Output 4: PDF/UA rule 7.1-11
- Output 4: PDF/UA rule 7.1-3
- Output 4: PDF/UA rule 7.2-33
- Output 4: PDF/UA rule 7.2-34
- Output 4: PDF/UA rule 7.21.7-1
- Output 5: PDF/UA rule 5-1
- Output 5: PDF/UA rule 6.2-1
- Output 5: PDF/UA rule 7.1-10
- Output 5: PDF/UA rule 7.1-11
- Output 5: PDF/UA rule 7.1-3
- Output 5: PDF/UA rule 7.2-33
- Output 5: PDF/UA rule 7.2-34
- Output 5: PDF/UA rule 7.21.7-1
- Output 6: PDF/UA rule 5-1
- Output 6: PDF/UA rule 6.2-1
- Output 6: PDF/UA rule 7.1-10
- Output 6: PDF/UA rule 7.1-11
- Output 6: PDF/UA rule 7.1-3
- Output 6: PDF/UA rule 7.2-33
- Output 6: PDF/UA rule 7.2-34
- Output 6: PDF/UA rule 7.21.7-1
- Output 7: PDF/UA rule 5-1
- Output 7: PDF/UA rule 6.2-1
- Output 7: PDF/UA rule 7.1-10
- Output 7: PDF/UA rule 7.1-11
- Output 7: PDF/UA rule 7.1-3
- Output 7: PDF/UA rule 7.2-33
- Output 7: PDF/UA rule 7.2-34
- Output 7: PDF/UA rule 7.21.7-1
- Output 8: PDF/UA rule 5-1
- Output 8: PDF/UA rule 6.2-1
- Output 8: PDF/UA rule 7.1-10
- Output 8: PDF/UA rule 7.1-11
- Output 8: PDF/UA rule 7.1-3
- Output 8: PDF/UA rule 7.2-33
- Output 8: PDF/UA rule 7.2-34
- Output 8: PDF/UA rule 7.21.7-1
- Output 9: PDF/UA rule 5-1
- Output 9: PDF/UA rule 6.2-1
- Output 9: PDF/UA rule 7.1-10
- Output 9: PDF/UA rule 7.1-11
- Output 9: PDF/UA rule 7.1-3
- Output 9: PDF/UA rule 7.2-33
- Output 9: PDF/UA rule 7.2-34
- Output 9: PDF/UA rule 7.21.7-1
- Output 10: PDF/UA rule 5-1
- Output 10: PDF/UA rule 6.2-1
- Output 10: PDF/UA rule 7.1-10
- Output 10: PDF/UA rule 7.1-11
- Output 10: PDF/UA rule 7.1-3
- Output 10: PDF/UA rule 7.2-33
- Output 10: PDF/UA rule 7.2-34
- Output 10: PDF/UA rule 7.21.7-1
- Output 11: PDF/UA rule 5-1
- Output 11: PDF/UA rule 6.2-1
- Output 11: PDF/UA rule 7.1-10
- Output 11: PDF/UA rule 7.1-11
- Output 11: PDF/UA rule 7.1-3
- Output 11: PDF/UA rule 7.2-33
- Output 11: PDF/UA rule 7.2-34
- Output 11: PDF/UA rule 7.21.7-1
- Output 12: PDF/UA rule 5-1
- Output 12: PDF/UA rule 6.2-1
- Output 12: PDF/UA rule 7.1-10
- Output 12: PDF/UA rule 7.1-11
- Output 12: PDF/UA rule 7.1-3
- Output 12: PDF/UA rule 7.2-33
- Output 12: PDF/UA rule 7.2-34
- Output 12: PDF/UA rule 7.21.7-1
- Output 13: PDF/UA rule 5-1
- Output 13: PDF/UA rule 6.2-1
- Output 13: PDF/UA rule 7.1-10
- Output 13: PDF/UA rule 7.1-11
- Output 13: PDF/UA rule 7.1-3
- Output 13: PDF/UA rule 7.2-33
- Output 13: PDF/UA rule 7.2-34
- Output 13: PDF/UA rule 7.21.7-1
- Output 14: PDF/UA rule 5-1
- Output 14: PDF/UA rule 6.2-1
- Output 14: PDF/UA rule 7.1-10
- Output 14: PDF/UA rule 7.1-11
- Output 14: PDF/UA rule 7.1-3
- Output 14: PDF/UA rule 7.2-33
- Output 14: PDF/UA rule 7.2-34
- Output 14: PDF/UA rule 7.21.7-1
- Output 15: PDF/UA rule 5-1
- Output 15: PDF/UA rule 6.2-1
- Output 15: PDF/UA rule 7.1-10
- Output 15: PDF/UA rule 7.1-11
- Output 15: PDF/UA rule 7.1-3
- Output 15: PDF/UA rule 7.2-33
- Output 15: PDF/UA rule 7.2-34
- Output 15: PDF/UA rule 7.21.7-1
- Output 16: PDF/UA rule 5-1
- Output 16: PDF/UA rule 6.2-1
- Output 16: PDF/UA rule 7.1-10
- Output 16: PDF/UA rule 7.1-11
- Output 16: PDF/UA rule 7.1-3
- Output 16: PDF/UA rule 7.2-33
- Output 16: PDF/UA rule 7.2-34
- Output 16: PDF/UA rule 7.21.7-1
- Output 17: PDF/UA rule 5-1
- Output 17: PDF/UA rule 6.2-1
- Output 17: PDF/UA rule 7.1-10
- Output 17: PDF/UA rule 7.1-11
- Output 17: PDF/UA rule 7.1-3
- Output 17: PDF/UA rule 7.2-33
- Output 17: PDF/UA rule 7.2-34
- Output 17: PDF/UA rule 7.21.7-1
- Output 18: PDF/UA rule 5-1
- Output 18: PDF/UA rule 6.2-1
- Output 18: PDF/UA rule 7.1-10
- Output 18: PDF/UA rule 7.1-11
- Output 18: PDF/UA rule 7.1-3
- Output 18: PDF/UA rule 7.2-33
- Output 18: PDF/UA rule 7.2-34
- Output 18: PDF/UA rule 7.21.7-1
- Output 19: PDF/UA rule 5-1
- Output 19: PDF/UA rule 6.2-1
- Output 19: PDF/UA rule 7.1-10
- Output 19: PDF/UA rule 7.1-11
- Output 19: PDF/UA rule 7.1-3
- Output 19: PDF/UA rule 7.2-33
- Output 19: PDF/UA rule 7.2-34
- Output 19: PDF/UA rule 7.21.7-1
- Output 20: PDF/UA rule 5-1
- Output 20: PDF/UA rule 6.2-1
- Output 20: PDF/UA rule 7.1-10
- Output 20: PDF/UA rule 7.1-11
- Output 20: PDF/UA rule 7.1-3
- Output 20: PDF/UA rule 7.2-33
- Output 20: PDF/UA rule 7.2-34
- Output 20: PDF/UA rule 7.21.7-1
- Output 21: PDF/UA rule 5-1
- Output 21: PDF/UA rule 6.2-1
- Output 21: PDF/UA rule 7.1-10
- Output 21: PDF/UA rule 7.1-11
- Output 21: PDF/UA rule 7.1-3
- Output 21: PDF/UA rule 7.2-33
- Output 21: PDF/UA rule 7.2-34
- Output 21: PDF/UA rule 7.21.7-1
- Output 22: PDF/UA rule 5-1
- Output 22: PDF/UA rule 6.2-1
- Output 22: PDF/UA rule 7.1-10
- Output 22: PDF/UA rule 7.1-11
- Output 22: PDF/UA rule 7.1-3
- Output 22: PDF/UA rule 7.2-33
- Output 22: PDF/UA rule 7.2-34
- Output 22: PDF/UA rule 7.21.7-1
- Output 23: PDF/UA rule 5-1
- Output 23: PDF/UA rule 6.2-1
- Output 23: PDF/UA rule 7.1-10
- Output 23: PDF/UA rule 7.1-11
- Output 23: PDF/UA rule 7.1-3
- Output 23: PDF/UA rule 7.2-33
- Output 23: PDF/UA rule 7.2-34
- Output 23: PDF/UA rule 7.21.7-1
- Output 24: PDF/UA rule 5-1
- Output 24: PDF/UA rule 6.2-1
- Output 24: PDF/UA rule 7.1-10
- Output 24: PDF/UA rule 7.1-11
- Output 24: PDF/UA rule 7.1-3
- Output 24: PDF/UA rule 7.2-33
- Output 24: PDF/UA rule 7.2-34
- Output 24: PDF/UA rule 7.21.7-1
- Output 25: PDF/UA rule 5-1
- Output 25: PDF/UA rule 6.2-1
- Output 25: PDF/UA rule 7.1-10
- Output 25: PDF/UA rule 7.1-11
- Output 25: PDF/UA rule 7.1-3
- Output 25: PDF/UA rule 7.2-33
- Output 25: PDF/UA rule 7.2-34
- Output 25: PDF/UA rule 7.21.7-1
- Output 26: PDF/UA rule 5-1
- Output 26: PDF/UA rule 6.2-1
- Output 26: PDF/UA rule 7.1-10
- Output 26: PDF/UA rule 7.1-11
- Output 26: PDF/UA rule 7.1-3
- Output 26: PDF/UA rule 7.2-33
- Output 26: PDF/UA rule 7.2-34
- Output 26: PDF/UA rule 7.21.7-1
- Output 27: PDF/UA rule 5-1
- Output 27: PDF/UA rule 6.2-1
- Output 27: PDF/UA rule 7.1-10
- Output 27: PDF/UA rule 7.1-11
- Output 27: PDF/UA rule 7.1-3
- Output 27: PDF/UA rule 7.2-33
- Output 27: PDF/UA rule 7.2-34
- Output 27: PDF/UA rule 7.21.7-1
- Output 28: PDF/UA rule 5-1
- Output 28: PDF/UA rule 6.2-1
- Output 28: PDF/UA rule 7.1-10
- Output 28: PDF/UA rule 7.1-11
- Output 28: PDF/UA rule 7.1-3
- Output 28: PDF/UA rule 7.2-33
- Output 28: PDF/UA rule 7.2-34
- Output 28: PDF/UA rule 7.21.7-1
- Output 29: PDF/UA rule 5-1
- Output 29: PDF/UA rule 6.2-1
- Output 29: PDF/UA rule 7.1-10
- Output 29: PDF/UA rule 7.1-11
- Output 29: PDF/UA rule 7.1-3
- Output 29: PDF/UA rule 7.2-33
- Output 29: PDF/UA rule 7.2-34
- Output 29: PDF/UA rule 7.21.7-1
- Output 30: PDF/UA rule 5-1
- Output 30: PDF/UA rule 6.2-1
- Output 30: PDF/UA rule 7.1-10
- Output 30: PDF/UA rule 7.1-11
- Output 30: PDF/UA rule 7.1-3
- Output 30: PDF/UA rule 7.2-33
- Output 30: PDF/UA rule 7.2-34
- Output 30: PDF/UA rule 7.21.7-1
- Output 31: PDF/UA rule 5-1
- Output 31: PDF/UA rule 6.2-1
- Output 31: PDF/UA rule 7.1-10
- Output 31: PDF/UA rule 7.1-11
- Output 31: PDF/UA rule 7.1-3
- Output 31: PDF/UA rule 7.18.3-1
- Output 31: PDF/UA rule 7.18.5-1
- Output 31: PDF/UA rule 7.2-24
- Output 31: PDF/UA rule 7.2-33
- Output 31: PDF/UA rule 7.2-34
- Output 31: PDF/UA rule 7.21.7-1
- Output 32: PDF/UA rule 5-1
- Output 32: PDF/UA rule 6.2-1
- Output 32: PDF/UA rule 7.1-10
- Output 32: PDF/UA rule 7.1-11
- Output 32: PDF/UA rule 7.1-3
- Output 32: PDF/UA rule 7.2-33
- Output 32: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 13 → 0
- document_language_present: True → False
- outline_count: 53 → 1

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-ref-2-08-bookchapter --output lab/reproduction.json
```

### ua1-ref-2-08-bookchapter-ghostscript-resave

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 1: PDF/UA rule 7.21.7-1
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 13 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-ref-2-08-bookchapter --output lab/reproduction.json
```

### ua1-ref-2-09-scanned-qpdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.4-1
- Output 1: PDF/UA rule 7.2-25
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 563 → 0
- role_map_count: 9 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 320 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-ref-2-09-scanned --output lab/reproduction.json
```

### ua1-ref-2-09-scanned-qpdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.1-8
- Output 3: PDF/UA rule 6.2-1
- Output 3: PDF/UA rule 7.1-10
- Output 3: PDF/UA rule 7.1-11
- Output 3: PDF/UA rule 7.1-3
- Output 3: PDF/UA rule 7.1-8
- Output 4: PDF/UA rule 6.2-1
- Output 4: PDF/UA rule 7.1-10
- Output 4: PDF/UA rule 7.1-11
- Output 4: PDF/UA rule 7.1-3
- Output 4: PDF/UA rule 7.1-8
- Output 5: PDF/UA rule 6.2-1
- Output 5: PDF/UA rule 7.1-10
- Output 5: PDF/UA rule 7.1-11
- Output 5: PDF/UA rule 7.1-3
- Output 5: PDF/UA rule 7.1-8
- Output 6: PDF/UA rule 6.2-1
- Output 6: PDF/UA rule 7.1-10
- Output 6: PDF/UA rule 7.1-11
- Output 6: PDF/UA rule 7.1-3
- Output 6: PDF/UA rule 7.1-8
- Output 7: PDF/UA rule 6.2-1
- Output 7: PDF/UA rule 7.1-10
- Output 7: PDF/UA rule 7.1-11
- Output 7: PDF/UA rule 7.1-3
- Output 7: PDF/UA rule 7.1-8
- Output 8: PDF/UA rule 6.2-1
- Output 8: PDF/UA rule 7.1-10
- Output 8: PDF/UA rule 7.1-11
- Output 8: PDF/UA rule 7.1-3
- Output 8: PDF/UA rule 7.1-8
- Output 9: PDF/UA rule 6.2-1
- Output 9: PDF/UA rule 7.1-10
- Output 9: PDF/UA rule 7.1-11
- Output 9: PDF/UA rule 7.1-3
- Output 9: PDF/UA rule 7.1-8
- Output 9: PDF/UA rule 7.2-34
- Output 10: PDF/UA rule 6.2-1
- Output 10: PDF/UA rule 7.1-10
- Output 10: PDF/UA rule 7.1-11
- Output 10: PDF/UA rule 7.1-3
- Output 10: PDF/UA rule 7.1-8
- Output 11: PDF/UA rule 6.2-1
- Output 11: PDF/UA rule 7.1-10
- Output 11: PDF/UA rule 7.1-11
- Output 11: PDF/UA rule 7.1-3
- Output 11: PDF/UA rule 7.1-8
- Output 12: PDF/UA rule 6.2-1
- Output 12: PDF/UA rule 7.1-10
- Output 12: PDF/UA rule 7.1-11
- Output 12: PDF/UA rule 7.1-3
- Output 12: PDF/UA rule 7.1-8
- Output 13: PDF/UA rule 6.2-1
- Output 13: PDF/UA rule 7.1-10
- Output 13: PDF/UA rule 7.1-11
- Output 13: PDF/UA rule 7.1-3
- Output 13: PDF/UA rule 7.1-8
- Output 14: PDF/UA rule 6.2-1
- Output 14: PDF/UA rule 7.1-10
- Output 14: PDF/UA rule 7.1-11
- Output 14: PDF/UA rule 7.1-3
- Output 14: PDF/UA rule 7.1-8
- Output 15: PDF/UA rule 6.2-1
- Output 15: PDF/UA rule 7.1-10
- Output 15: PDF/UA rule 7.1-11
- Output 15: PDF/UA rule 7.1-3
- Output 15: PDF/UA rule 7.1-8
- Output 16: PDF/UA rule 6.2-1
- Output 16: PDF/UA rule 7.1-10
- Output 16: PDF/UA rule 7.1-11
- Output 16: PDF/UA rule 7.1-3
- Output 16: PDF/UA rule 7.1-8
- Output 17: PDF/UA rule 6.2-1
- Output 17: PDF/UA rule 7.1-10
- Output 17: PDF/UA rule 7.1-11
- Output 17: PDF/UA rule 7.1-3
- Output 17: PDF/UA rule 7.1-8
- Output 18: PDF/UA rule 6.2-1
- Output 18: PDF/UA rule 7.1-10
- Output 18: PDF/UA rule 7.1-11
- Output 18: PDF/UA rule 7.1-3
- Output 18: PDF/UA rule 7.1-8
- Output 19: PDF/UA rule 6.2-1
- Output 19: PDF/UA rule 7.1-10
- Output 19: PDF/UA rule 7.1-11
- Output 19: PDF/UA rule 7.1-3
- Output 19: PDF/UA rule 7.1-8
- Output 19: PDF/UA rule 7.2-34
- Output 20: PDF/UA rule 6.2-1
- Output 20: PDF/UA rule 7.1-10
- Output 20: PDF/UA rule 7.1-11
- Output 20: PDF/UA rule 7.1-3
- Output 20: PDF/UA rule 7.1-8
- Output 21: PDF/UA rule 6.2-1
- Output 21: PDF/UA rule 7.1-10
- Output 21: PDF/UA rule 7.1-11
- Output 21: PDF/UA rule 7.1-3
- Output 21: PDF/UA rule 7.1-8
- Output 21: PDF/UA rule 7.2-34
- Output 22: PDF/UA rule 6.2-1
- Output 22: PDF/UA rule 7.1-10
- Output 22: PDF/UA rule 7.1-11
- Output 22: PDF/UA rule 7.1-3
- Output 22: PDF/UA rule 7.1-8
- Output 22: PDF/UA rule 7.2-34
- Output 23: PDF/UA rule 6.2-1
- Output 23: PDF/UA rule 7.1-10
- Output 23: PDF/UA rule 7.1-11
- Output 23: PDF/UA rule 7.1-3
- Output 23: PDF/UA rule 7.1-8
- Output 24: PDF/UA rule 6.2-1
- Output 24: PDF/UA rule 7.1-10
- Output 24: PDF/UA rule 7.1-11
- Output 24: PDF/UA rule 7.1-3
- Output 24: PDF/UA rule 7.1-8
- Output 25: PDF/UA rule 6.2-1
- Output 25: PDF/UA rule 7.1-10
- Output 25: PDF/UA rule 7.1-11
- Output 25: PDF/UA rule 7.1-3
- Output 25: PDF/UA rule 7.1-8
- Output 26: PDF/UA rule 6.2-1
- Output 26: PDF/UA rule 7.1-10
- Output 26: PDF/UA rule 7.1-11
- Output 26: PDF/UA rule 7.1-3
- Output 26: PDF/UA rule 7.1-8
- Output 27: PDF/UA rule 6.2-1
- Output 27: PDF/UA rule 7.1-10
- Output 27: PDF/UA rule 7.1-11
- Output 27: PDF/UA rule 7.1-3
- Output 27: PDF/UA rule 7.1-8
- Output 28: PDF/UA rule 6.2-1
- Output 28: PDF/UA rule 7.1-10
- Output 28: PDF/UA rule 7.1-11
- Output 28: PDF/UA rule 7.1-3
- Output 28: PDF/UA rule 7.1-8
- Output 29: PDF/UA rule 6.2-1
- Output 29: PDF/UA rule 7.1-10
- Output 29: PDF/UA rule 7.1-11
- Output 29: PDF/UA rule 7.1-3
- Output 29: PDF/UA rule 7.1-8
- Output 30: PDF/UA rule 6.2-1
- Output 30: PDF/UA rule 7.1-10
- Output 30: PDF/UA rule 7.1-11
- Output 30: PDF/UA rule 7.1-3
- Output 30: PDF/UA rule 7.1-8
- Output 31: PDF/UA rule 6.2-1
- Output 31: PDF/UA rule 7.1-10
- Output 31: PDF/UA rule 7.1-11
- Output 31: PDF/UA rule 7.1-3
- Output 31: PDF/UA rule 7.1-8
- Output 32: PDF/UA rule 6.2-1
- Output 32: PDF/UA rule 7.1-10
- Output 32: PDF/UA rule 7.1-11
- Output 32: PDF/UA rule 7.1-3
- Output 32: PDF/UA rule 7.1-8
- Output 33: PDF/UA rule 6.2-1
- Output 33: PDF/UA rule 7.1-10
- Output 33: PDF/UA rule 7.1-11
- Output 33: PDF/UA rule 7.1-3
- Output 33: PDF/UA rule 7.1-8
- Output 34: PDF/UA rule 6.2-1
- Output 34: PDF/UA rule 7.1-10
- Output 34: PDF/UA rule 7.1-11
- Output 34: PDF/UA rule 7.1-3
- Output 34: PDF/UA rule 7.1-8
- Output 35: PDF/UA rule 6.2-1
- Output 35: PDF/UA rule 7.1-10
- Output 35: PDF/UA rule 7.1-11
- Output 35: PDF/UA rule 7.1-3
- Output 35: PDF/UA rule 7.1-8
- Output 36: PDF/UA rule 6.2-1
- Output 36: PDF/UA rule 7.1-10
- Output 36: PDF/UA rule 7.1-11
- Output 36: PDF/UA rule 7.1-3
- Output 36: PDF/UA rule 7.1-8
- Output 37: PDF/UA rule 6.2-1
- Output 37: PDF/UA rule 7.1-10
- Output 37: PDF/UA rule 7.1-11
- Output 37: PDF/UA rule 7.1-3
- Output 37: PDF/UA rule 7.1-8
- Output 38: PDF/UA rule 6.2-1
- Output 38: PDF/UA rule 7.1-10
- Output 38: PDF/UA rule 7.1-11
- Output 38: PDF/UA rule 7.1-3
- Output 38: PDF/UA rule 7.1-8
- Output 39: PDF/UA rule 6.2-1
- Output 39: PDF/UA rule 7.1-10
- Output 39: PDF/UA rule 7.1-11
- Output 39: PDF/UA rule 7.1-3
- Output 39: PDF/UA rule 7.1-8
- Output 40: PDF/UA rule 6.2-1
- Output 40: PDF/UA rule 7.1-10
- Output 40: PDF/UA rule 7.1-11
- Output 40: PDF/UA rule 7.1-3
- Output 40: PDF/UA rule 7.1-8
- Output 41: PDF/UA rule 6.2-1
- Output 41: PDF/UA rule 7.1-10
- Output 41: PDF/UA rule 7.1-11
- Output 41: PDF/UA rule 7.1-3
- Output 41: PDF/UA rule 7.1-8
- Output 42: PDF/UA rule 6.2-1
- Output 42: PDF/UA rule 7.1-10
- Output 42: PDF/UA rule 7.1-11
- Output 42: PDF/UA rule 7.1-3
- Output 42: PDF/UA rule 7.1-8
- Output 43: PDF/UA rule 6.2-1
- Output 43: PDF/UA rule 7.1-10
- Output 43: PDF/UA rule 7.1-11
- Output 43: PDF/UA rule 7.1-3
- Output 43: PDF/UA rule 7.1-8
- Output 44: PDF/UA rule 6.2-1
- Output 44: PDF/UA rule 7.1-10
- Output 44: PDF/UA rule 7.1-11
- Output 44: PDF/UA rule 7.1-3
- Output 44: PDF/UA rule 7.1-8
- Output 45: PDF/UA rule 6.2-1
- Output 45: PDF/UA rule 7.1-10
- Output 45: PDF/UA rule 7.1-11
- Output 45: PDF/UA rule 7.1-3
- Output 45: PDF/UA rule 7.1-8
- Output 46: PDF/UA rule 6.2-1
- Output 46: PDF/UA rule 7.1-10
- Output 46: PDF/UA rule 7.1-11
- Output 46: PDF/UA rule 7.1-3
- Output 46: PDF/UA rule 7.1-8
- Output 47: PDF/UA rule 6.2-1
- Output 47: PDF/UA rule 7.1-10
- Output 47: PDF/UA rule 7.1-11
- Output 47: PDF/UA rule 7.1-3
- Output 47: PDF/UA rule 7.1-8
- Output 48: PDF/UA rule 6.2-1
- Output 48: PDF/UA rule 7.1-10
- Output 48: PDF/UA rule 7.1-11
- Output 48: PDF/UA rule 7.1-3
- Output 48: PDF/UA rule 7.1-8
- Output 49: PDF/UA rule 6.2-1
- Output 49: PDF/UA rule 7.1-10
- Output 49: PDF/UA rule 7.1-11
- Output 49: PDF/UA rule 7.1-3
- Output 49: PDF/UA rule 7.1-8
- Output 50: PDF/UA rule 6.2-1
- Output 50: PDF/UA rule 7.1-10
- Output 50: PDF/UA rule 7.1-11
- Output 50: PDF/UA rule 7.1-3
- Output 50: PDF/UA rule 7.1-8
- Output 51: PDF/UA rule 6.2-1
- Output 51: PDF/UA rule 7.1-10
- Output 51: PDF/UA rule 7.1-11
- Output 51: PDF/UA rule 7.1-3
- Output 51: PDF/UA rule 7.1-8
- Output 52: PDF/UA rule 6.2-1
- Output 52: PDF/UA rule 7.1-10
- Output 52: PDF/UA rule 7.1-11
- Output 52: PDF/UA rule 7.1-3
- Output 52: PDF/UA rule 7.1-8
- Output 53: PDF/UA rule 6.2-1
- Output 53: PDF/UA rule 7.1-10
- Output 53: PDF/UA rule 7.1-11
- Output 53: PDF/UA rule 7.1-3
- Output 53: PDF/UA rule 7.1-8
- Output 54: PDF/UA rule 6.2-1
- Output 54: PDF/UA rule 7.1-10
- Output 54: PDF/UA rule 7.1-11
- Output 54: PDF/UA rule 7.1-3
- Output 54: PDF/UA rule 7.1-8
- Output 55: PDF/UA rule 6.2-1
- Output 55: PDF/UA rule 7.1-10
- Output 55: PDF/UA rule 7.1-11
- Output 55: PDF/UA rule 7.1-3
- Output 55: PDF/UA rule 7.1-8
- Output 56: PDF/UA rule 6.2-1
- Output 56: PDF/UA rule 7.1-10
- Output 56: PDF/UA rule 7.1-11
- Output 56: PDF/UA rule 7.1-3
- Output 56: PDF/UA rule 7.1-8
- Output 57: PDF/UA rule 6.2-1
- Output 57: PDF/UA rule 7.1-10
- Output 57: PDF/UA rule 7.1-11
- Output 57: PDF/UA rule 7.1-3
- Output 57: PDF/UA rule 7.1-8
- Output 58: PDF/UA rule 6.2-1
- Output 58: PDF/UA rule 7.1-10
- Output 58: PDF/UA rule 7.1-11
- Output 58: PDF/UA rule 7.1-3
- Output 58: PDF/UA rule 7.1-8
- Output 59: PDF/UA rule 6.2-1
- Output 59: PDF/UA rule 7.1-10
- Output 59: PDF/UA rule 7.1-11
- Output 59: PDF/UA rule 7.1-3
- Output 59: PDF/UA rule 7.1-8
- Output 60: PDF/UA rule 6.2-1
- Output 60: PDF/UA rule 7.1-10
- Output 60: PDF/UA rule 7.1-11
- Output 60: PDF/UA rule 7.1-3
- Output 60: PDF/UA rule 7.1-8
- Output 61: PDF/UA rule 6.2-1
- Output 61: PDF/UA rule 7.1-10
- Output 61: PDF/UA rule 7.1-11
- Output 61: PDF/UA rule 7.1-3
- Output 61: PDF/UA rule 7.1-8
- Output 62: PDF/UA rule 6.2-1
- Output 62: PDF/UA rule 7.1-10
- Output 62: PDF/UA rule 7.1-11
- Output 62: PDF/UA rule 7.1-3
- Output 62: PDF/UA rule 7.1-8
- Output 63: PDF/UA rule 6.2-1
- Output 63: PDF/UA rule 7.1-10
- Output 63: PDF/UA rule 7.1-11
- Output 63: PDF/UA rule 7.1-3
- Output 63: PDF/UA rule 7.1-8
- Output 63: PDF/UA rule 7.2-34
- Output 64: PDF/UA rule 6.2-1
- Output 64: PDF/UA rule 7.1-10
- Output 64: PDF/UA rule 7.1-11
- Output 64: PDF/UA rule 7.1-3
- Output 64: PDF/UA rule 7.1-8
- Output 65: PDF/UA rule 6.2-1
- Output 65: PDF/UA rule 7.1-10
- Output 65: PDF/UA rule 7.1-11
- Output 65: PDF/UA rule 7.1-3
- Output 65: PDF/UA rule 7.1-8
- Output 66: PDF/UA rule 6.2-1
- Output 66: PDF/UA rule 7.1-10
- Output 66: PDF/UA rule 7.1-11
- Output 66: PDF/UA rule 7.1-3
- Output 66: PDF/UA rule 7.1-8
- Output 67: PDF/UA rule 6.2-1
- Output 67: PDF/UA rule 7.1-10
- Output 67: PDF/UA rule 7.1-11
- Output 67: PDF/UA rule 7.1-3
- Output 67: PDF/UA rule 7.1-8
- Output 68: PDF/UA rule 6.2-1
- Output 68: PDF/UA rule 7.1-10
- Output 68: PDF/UA rule 7.1-11
- Output 68: PDF/UA rule 7.1-3
- Output 68: PDF/UA rule 7.1-8
- Output 69: PDF/UA rule 6.2-1
- Output 69: PDF/UA rule 7.1-10
- Output 69: PDF/UA rule 7.1-11
- Output 69: PDF/UA rule 7.1-3
- Output 69: PDF/UA rule 7.1-8
- Output 70: PDF/UA rule 6.2-1
- Output 70: PDF/UA rule 7.1-10
- Output 70: PDF/UA rule 7.1-11
- Output 70: PDF/UA rule 7.1-3
- Output 70: PDF/UA rule 7.1-8
- Output 71: PDF/UA rule 6.2-1
- Output 71: PDF/UA rule 7.1-10
- Output 71: PDF/UA rule 7.1-11
- Output 71: PDF/UA rule 7.1-3
- Output 71: PDF/UA rule 7.1-8
- Output 72: PDF/UA rule 6.2-1
- Output 72: PDF/UA rule 7.1-10
- Output 72: PDF/UA rule 7.1-11
- Output 72: PDF/UA rule 7.1-3
- Output 72: PDF/UA rule 7.1-8
- Output 73: PDF/UA rule 6.2-1
- Output 73: PDF/UA rule 7.1-10
- Output 73: PDF/UA rule 7.1-11
- Output 73: PDF/UA rule 7.1-3
- Output 73: PDF/UA rule 7.1-8
- Output 74: PDF/UA rule 6.2-1
- Output 74: PDF/UA rule 7.1-10
- Output 74: PDF/UA rule 7.1-11
- Output 74: PDF/UA rule 7.1-3
- Output 74: PDF/UA rule 7.1-8
- Output 75: PDF/UA rule 6.2-1
- Output 75: PDF/UA rule 7.1-10
- Output 75: PDF/UA rule 7.1-11
- Output 75: PDF/UA rule 7.1-3
- Output 75: PDF/UA rule 7.1-8
- Output 76: PDF/UA rule 6.2-1
- Output 76: PDF/UA rule 7.1-10
- Output 76: PDF/UA rule 7.1-11
- Output 76: PDF/UA rule 7.1-3
- Output 76: PDF/UA rule 7.1-8
- Output 77: PDF/UA rule 6.2-1
- Output 77: PDF/UA rule 7.1-10
- Output 77: PDF/UA rule 7.1-11
- Output 77: PDF/UA rule 7.1-3
- Output 77: PDF/UA rule 7.1-8
- Output 78: PDF/UA rule 6.2-1
- Output 78: PDF/UA rule 7.1-10
- Output 78: PDF/UA rule 7.1-11
- Output 78: PDF/UA rule 7.1-3
- Output 78: PDF/UA rule 7.1-8
- Output 78: PDF/UA rule 7.2-34
- Output 79: PDF/UA rule 6.2-1
- Output 79: PDF/UA rule 7.1-10
- Output 79: PDF/UA rule 7.1-11
- Output 79: PDF/UA rule 7.1-3
- Output 79: PDF/UA rule 7.1-8
- Output 80: PDF/UA rule 6.2-1
- Output 80: PDF/UA rule 7.1-10
- Output 80: PDF/UA rule 7.1-11
- Output 80: PDF/UA rule 7.1-3
- Output 80: PDF/UA rule 7.1-8
- Output 81: PDF/UA rule 6.2-1
- Output 81: PDF/UA rule 7.1-10
- Output 81: PDF/UA rule 7.1-11
- Output 81: PDF/UA rule 7.1-3
- Output 81: PDF/UA rule 7.1-8
- Output 82: PDF/UA rule 6.2-1
- Output 82: PDF/UA rule 7.1-10
- Output 82: PDF/UA rule 7.1-11
- Output 82: PDF/UA rule 7.1-3
- Output 82: PDF/UA rule 7.1-8
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 563 → 0
- role_map_count: 3 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 320 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-ref-2-09-scanned --output lab/reproduction.json
```

### ua1-ref-2-09-scanned-pymupdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.4-1
- Output 1: PDF/UA rule 7.2-25
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 563 → 0
- role_map_count: 9 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 320 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-ref-2-09-scanned --output lab/reproduction.json
```

### ua1-ref-2-09-scanned-pymupdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.1-8
- Output 3: PDF/UA rule 6.2-1
- Output 3: PDF/UA rule 7.1-10
- Output 3: PDF/UA rule 7.1-11
- Output 3: PDF/UA rule 7.1-3
- Output 3: PDF/UA rule 7.1-8
- Output 4: PDF/UA rule 6.2-1
- Output 4: PDF/UA rule 7.1-10
- Output 4: PDF/UA rule 7.1-11
- Output 4: PDF/UA rule 7.1-3
- Output 4: PDF/UA rule 7.1-8
- Output 5: PDF/UA rule 6.2-1
- Output 5: PDF/UA rule 7.1-10
- Output 5: PDF/UA rule 7.1-11
- Output 5: PDF/UA rule 7.1-3
- Output 5: PDF/UA rule 7.1-8
- Output 6: PDF/UA rule 6.2-1
- Output 6: PDF/UA rule 7.1-10
- Output 6: PDF/UA rule 7.1-11
- Output 6: PDF/UA rule 7.1-3
- Output 6: PDF/UA rule 7.1-8
- Output 7: PDF/UA rule 6.2-1
- Output 7: PDF/UA rule 7.1-10
- Output 7: PDF/UA rule 7.1-11
- Output 7: PDF/UA rule 7.1-3
- Output 7: PDF/UA rule 7.1-8
- Output 8: PDF/UA rule 6.2-1
- Output 8: PDF/UA rule 7.1-10
- Output 8: PDF/UA rule 7.1-11
- Output 8: PDF/UA rule 7.1-3
- Output 8: PDF/UA rule 7.1-8
- Output 9: PDF/UA rule 6.2-1
- Output 9: PDF/UA rule 7.1-10
- Output 9: PDF/UA rule 7.1-11
- Output 9: PDF/UA rule 7.1-3
- Output 9: PDF/UA rule 7.1-8
- Output 9: PDF/UA rule 7.2-34
- Output 10: PDF/UA rule 6.2-1
- Output 10: PDF/UA rule 7.1-10
- Output 10: PDF/UA rule 7.1-11
- Output 10: PDF/UA rule 7.1-3
- Output 10: PDF/UA rule 7.1-8
- Output 11: PDF/UA rule 6.2-1
- Output 11: PDF/UA rule 7.1-10
- Output 11: PDF/UA rule 7.1-11
- Output 11: PDF/UA rule 7.1-3
- Output 11: PDF/UA rule 7.1-8
- Output 12: PDF/UA rule 6.2-1
- Output 12: PDF/UA rule 7.1-10
- Output 12: PDF/UA rule 7.1-11
- Output 12: PDF/UA rule 7.1-3
- Output 12: PDF/UA rule 7.1-8
- Output 13: PDF/UA rule 6.2-1
- Output 13: PDF/UA rule 7.1-10
- Output 13: PDF/UA rule 7.1-11
- Output 13: PDF/UA rule 7.1-3
- Output 13: PDF/UA rule 7.1-8
- Output 14: PDF/UA rule 6.2-1
- Output 14: PDF/UA rule 7.1-10
- Output 14: PDF/UA rule 7.1-11
- Output 14: PDF/UA rule 7.1-3
- Output 14: PDF/UA rule 7.1-8
- Output 15: PDF/UA rule 6.2-1
- Output 15: PDF/UA rule 7.1-10
- Output 15: PDF/UA rule 7.1-11
- Output 15: PDF/UA rule 7.1-3
- Output 15: PDF/UA rule 7.1-8
- Output 16: PDF/UA rule 6.2-1
- Output 16: PDF/UA rule 7.1-10
- Output 16: PDF/UA rule 7.1-11
- Output 16: PDF/UA rule 7.1-3
- Output 16: PDF/UA rule 7.1-8
- Output 17: PDF/UA rule 6.2-1
- Output 17: PDF/UA rule 7.1-10
- Output 17: PDF/UA rule 7.1-11
- Output 17: PDF/UA rule 7.1-3
- Output 17: PDF/UA rule 7.1-8
- Output 18: PDF/UA rule 6.2-1
- Output 18: PDF/UA rule 7.1-10
- Output 18: PDF/UA rule 7.1-11
- Output 18: PDF/UA rule 7.1-3
- Output 18: PDF/UA rule 7.1-8
- Output 19: PDF/UA rule 6.2-1
- Output 19: PDF/UA rule 7.1-10
- Output 19: PDF/UA rule 7.1-11
- Output 19: PDF/UA rule 7.1-3
- Output 19: PDF/UA rule 7.1-8
- Output 19: PDF/UA rule 7.2-34
- Output 20: PDF/UA rule 6.2-1
- Output 20: PDF/UA rule 7.1-10
- Output 20: PDF/UA rule 7.1-11
- Output 20: PDF/UA rule 7.1-3
- Output 20: PDF/UA rule 7.1-8
- Output 21: PDF/UA rule 6.2-1
- Output 21: PDF/UA rule 7.1-10
- Output 21: PDF/UA rule 7.1-11
- Output 21: PDF/UA rule 7.1-3
- Output 21: PDF/UA rule 7.1-8
- Output 21: PDF/UA rule 7.2-34
- Output 22: PDF/UA rule 6.2-1
- Output 22: PDF/UA rule 7.1-10
- Output 22: PDF/UA rule 7.1-11
- Output 22: PDF/UA rule 7.1-3
- Output 22: PDF/UA rule 7.1-8
- Output 22: PDF/UA rule 7.2-34
- Output 23: PDF/UA rule 6.2-1
- Output 23: PDF/UA rule 7.1-10
- Output 23: PDF/UA rule 7.1-11
- Output 23: PDF/UA rule 7.1-3
- Output 23: PDF/UA rule 7.1-8
- Output 24: PDF/UA rule 6.2-1
- Output 24: PDF/UA rule 7.1-10
- Output 24: PDF/UA rule 7.1-11
- Output 24: PDF/UA rule 7.1-3
- Output 24: PDF/UA rule 7.1-8
- Output 25: PDF/UA rule 6.2-1
- Output 25: PDF/UA rule 7.1-10
- Output 25: PDF/UA rule 7.1-11
- Output 25: PDF/UA rule 7.1-3
- Output 25: PDF/UA rule 7.1-8
- Output 26: PDF/UA rule 6.2-1
- Output 26: PDF/UA rule 7.1-10
- Output 26: PDF/UA rule 7.1-11
- Output 26: PDF/UA rule 7.1-3
- Output 26: PDF/UA rule 7.1-8
- Output 27: PDF/UA rule 6.2-1
- Output 27: PDF/UA rule 7.1-10
- Output 27: PDF/UA rule 7.1-11
- Output 27: PDF/UA rule 7.1-3
- Output 27: PDF/UA rule 7.1-8
- Output 28: PDF/UA rule 6.2-1
- Output 28: PDF/UA rule 7.1-10
- Output 28: PDF/UA rule 7.1-11
- Output 28: PDF/UA rule 7.1-3
- Output 28: PDF/UA rule 7.1-8
- Output 29: PDF/UA rule 6.2-1
- Output 29: PDF/UA rule 7.1-10
- Output 29: PDF/UA rule 7.1-11
- Output 29: PDF/UA rule 7.1-3
- Output 29: PDF/UA rule 7.1-8
- Output 30: PDF/UA rule 6.2-1
- Output 30: PDF/UA rule 7.1-10
- Output 30: PDF/UA rule 7.1-11
- Output 30: PDF/UA rule 7.1-3
- Output 30: PDF/UA rule 7.1-8
- Output 31: PDF/UA rule 6.2-1
- Output 31: PDF/UA rule 7.1-10
- Output 31: PDF/UA rule 7.1-11
- Output 31: PDF/UA rule 7.1-3
- Output 31: PDF/UA rule 7.1-8
- Output 32: PDF/UA rule 6.2-1
- Output 32: PDF/UA rule 7.1-10
- Output 32: PDF/UA rule 7.1-11
- Output 32: PDF/UA rule 7.1-3
- Output 32: PDF/UA rule 7.1-8
- Output 33: PDF/UA rule 6.2-1
- Output 33: PDF/UA rule 7.1-10
- Output 33: PDF/UA rule 7.1-11
- Output 33: PDF/UA rule 7.1-3
- Output 33: PDF/UA rule 7.1-8
- Output 34: PDF/UA rule 6.2-1
- Output 34: PDF/UA rule 7.1-10
- Output 34: PDF/UA rule 7.1-11
- Output 34: PDF/UA rule 7.1-3
- Output 34: PDF/UA rule 7.1-8
- Output 35: PDF/UA rule 6.2-1
- Output 35: PDF/UA rule 7.1-10
- Output 35: PDF/UA rule 7.1-11
- Output 35: PDF/UA rule 7.1-3
- Output 35: PDF/UA rule 7.1-8
- Output 36: PDF/UA rule 6.2-1
- Output 36: PDF/UA rule 7.1-10
- Output 36: PDF/UA rule 7.1-11
- Output 36: PDF/UA rule 7.1-3
- Output 36: PDF/UA rule 7.1-8
- Output 37: PDF/UA rule 6.2-1
- Output 37: PDF/UA rule 7.1-10
- Output 37: PDF/UA rule 7.1-11
- Output 37: PDF/UA rule 7.1-3
- Output 37: PDF/UA rule 7.1-8
- Output 38: PDF/UA rule 6.2-1
- Output 38: PDF/UA rule 7.1-10
- Output 38: PDF/UA rule 7.1-11
- Output 38: PDF/UA rule 7.1-3
- Output 38: PDF/UA rule 7.1-8
- Output 39: PDF/UA rule 6.2-1
- Output 39: PDF/UA rule 7.1-10
- Output 39: PDF/UA rule 7.1-11
- Output 39: PDF/UA rule 7.1-3
- Output 39: PDF/UA rule 7.1-8
- Output 40: PDF/UA rule 6.2-1
- Output 40: PDF/UA rule 7.1-10
- Output 40: PDF/UA rule 7.1-11
- Output 40: PDF/UA rule 7.1-3
- Output 40: PDF/UA rule 7.1-8
- Output 41: PDF/UA rule 6.2-1
- Output 41: PDF/UA rule 7.1-10
- Output 41: PDF/UA rule 7.1-11
- Output 41: PDF/UA rule 7.1-3
- Output 41: PDF/UA rule 7.1-8
- Output 42: PDF/UA rule 6.2-1
- Output 42: PDF/UA rule 7.1-10
- Output 42: PDF/UA rule 7.1-11
- Output 42: PDF/UA rule 7.1-3
- Output 42: PDF/UA rule 7.1-8
- Output 43: PDF/UA rule 6.2-1
- Output 43: PDF/UA rule 7.1-10
- Output 43: PDF/UA rule 7.1-11
- Output 43: PDF/UA rule 7.1-3
- Output 43: PDF/UA rule 7.1-8
- Output 44: PDF/UA rule 6.2-1
- Output 44: PDF/UA rule 7.1-10
- Output 44: PDF/UA rule 7.1-11
- Output 44: PDF/UA rule 7.1-3
- Output 44: PDF/UA rule 7.1-8
- Output 45: PDF/UA rule 6.2-1
- Output 45: PDF/UA rule 7.1-10
- Output 45: PDF/UA rule 7.1-11
- Output 45: PDF/UA rule 7.1-3
- Output 45: PDF/UA rule 7.1-8
- Output 46: PDF/UA rule 6.2-1
- Output 46: PDF/UA rule 7.1-10
- Output 46: PDF/UA rule 7.1-11
- Output 46: PDF/UA rule 7.1-3
- Output 46: PDF/UA rule 7.1-8
- Output 47: PDF/UA rule 6.2-1
- Output 47: PDF/UA rule 7.1-10
- Output 47: PDF/UA rule 7.1-11
- Output 47: PDF/UA rule 7.1-3
- Output 47: PDF/UA rule 7.1-8
- Output 48: PDF/UA rule 6.2-1
- Output 48: PDF/UA rule 7.1-10
- Output 48: PDF/UA rule 7.1-11
- Output 48: PDF/UA rule 7.1-3
- Output 48: PDF/UA rule 7.1-8
- Output 49: PDF/UA rule 6.2-1
- Output 49: PDF/UA rule 7.1-10
- Output 49: PDF/UA rule 7.1-11
- Output 49: PDF/UA rule 7.1-3
- Output 49: PDF/UA rule 7.1-8
- Output 50: PDF/UA rule 6.2-1
- Output 50: PDF/UA rule 7.1-10
- Output 50: PDF/UA rule 7.1-11
- Output 50: PDF/UA rule 7.1-3
- Output 50: PDF/UA rule 7.1-8
- Output 51: PDF/UA rule 6.2-1
- Output 51: PDF/UA rule 7.1-10
- Output 51: PDF/UA rule 7.1-11
- Output 51: PDF/UA rule 7.1-3
- Output 51: PDF/UA rule 7.1-8
- Output 52: PDF/UA rule 6.2-1
- Output 52: PDF/UA rule 7.1-10
- Output 52: PDF/UA rule 7.1-11
- Output 52: PDF/UA rule 7.1-3
- Output 52: PDF/UA rule 7.1-8
- Output 53: PDF/UA rule 6.2-1
- Output 53: PDF/UA rule 7.1-10
- Output 53: PDF/UA rule 7.1-11
- Output 53: PDF/UA rule 7.1-3
- Output 53: PDF/UA rule 7.1-8
- Output 54: PDF/UA rule 6.2-1
- Output 54: PDF/UA rule 7.1-10
- Output 54: PDF/UA rule 7.1-11
- Output 54: PDF/UA rule 7.1-3
- Output 54: PDF/UA rule 7.1-8
- Output 55: PDF/UA rule 6.2-1
- Output 55: PDF/UA rule 7.1-10
- Output 55: PDF/UA rule 7.1-11
- Output 55: PDF/UA rule 7.1-3
- Output 55: PDF/UA rule 7.1-8
- Output 56: PDF/UA rule 6.2-1
- Output 56: PDF/UA rule 7.1-10
- Output 56: PDF/UA rule 7.1-11
- Output 56: PDF/UA rule 7.1-3
- Output 56: PDF/UA rule 7.1-8
- Output 57: PDF/UA rule 6.2-1
- Output 57: PDF/UA rule 7.1-10
- Output 57: PDF/UA rule 7.1-11
- Output 57: PDF/UA rule 7.1-3
- Output 57: PDF/UA rule 7.1-8
- Output 58: PDF/UA rule 6.2-1
- Output 58: PDF/UA rule 7.1-10
- Output 58: PDF/UA rule 7.1-11
- Output 58: PDF/UA rule 7.1-3
- Output 58: PDF/UA rule 7.1-8
- Output 59: PDF/UA rule 6.2-1
- Output 59: PDF/UA rule 7.1-10
- Output 59: PDF/UA rule 7.1-11
- Output 59: PDF/UA rule 7.1-3
- Output 59: PDF/UA rule 7.1-8
- Output 60: PDF/UA rule 6.2-1
- Output 60: PDF/UA rule 7.1-10
- Output 60: PDF/UA rule 7.1-11
- Output 60: PDF/UA rule 7.1-3
- Output 60: PDF/UA rule 7.1-8
- Output 61: PDF/UA rule 6.2-1
- Output 61: PDF/UA rule 7.1-10
- Output 61: PDF/UA rule 7.1-11
- Output 61: PDF/UA rule 7.1-3
- Output 61: PDF/UA rule 7.1-8
- Output 62: PDF/UA rule 6.2-1
- Output 62: PDF/UA rule 7.1-10
- Output 62: PDF/UA rule 7.1-11
- Output 62: PDF/UA rule 7.1-3
- Output 62: PDF/UA rule 7.1-8
- Output 63: PDF/UA rule 6.2-1
- Output 63: PDF/UA rule 7.1-10
- Output 63: PDF/UA rule 7.1-11
- Output 63: PDF/UA rule 7.1-3
- Output 63: PDF/UA rule 7.1-8
- Output 63: PDF/UA rule 7.2-34
- Output 64: PDF/UA rule 6.2-1
- Output 64: PDF/UA rule 7.1-10
- Output 64: PDF/UA rule 7.1-11
- Output 64: PDF/UA rule 7.1-3
- Output 64: PDF/UA rule 7.1-8
- Output 65: PDF/UA rule 6.2-1
- Output 65: PDF/UA rule 7.1-10
- Output 65: PDF/UA rule 7.1-11
- Output 65: PDF/UA rule 7.1-3
- Output 65: PDF/UA rule 7.1-8
- Output 66: PDF/UA rule 6.2-1
- Output 66: PDF/UA rule 7.1-10
- Output 66: PDF/UA rule 7.1-11
- Output 66: PDF/UA rule 7.1-3
- Output 66: PDF/UA rule 7.1-8
- Output 67: PDF/UA rule 6.2-1
- Output 67: PDF/UA rule 7.1-10
- Output 67: PDF/UA rule 7.1-11
- Output 67: PDF/UA rule 7.1-3
- Output 67: PDF/UA rule 7.1-8
- Output 68: PDF/UA rule 6.2-1
- Output 68: PDF/UA rule 7.1-10
- Output 68: PDF/UA rule 7.1-11
- Output 68: PDF/UA rule 7.1-3
- Output 68: PDF/UA rule 7.1-8
- Output 69: PDF/UA rule 6.2-1
- Output 69: PDF/UA rule 7.1-10
- Output 69: PDF/UA rule 7.1-11
- Output 69: PDF/UA rule 7.1-3
- Output 69: PDF/UA rule 7.1-8
- Output 70: PDF/UA rule 6.2-1
- Output 70: PDF/UA rule 7.1-10
- Output 70: PDF/UA rule 7.1-11
- Output 70: PDF/UA rule 7.1-3
- Output 70: PDF/UA rule 7.1-8
- Output 71: PDF/UA rule 6.2-1
- Output 71: PDF/UA rule 7.1-10
- Output 71: PDF/UA rule 7.1-11
- Output 71: PDF/UA rule 7.1-3
- Output 71: PDF/UA rule 7.1-8
- Output 72: PDF/UA rule 6.2-1
- Output 72: PDF/UA rule 7.1-10
- Output 72: PDF/UA rule 7.1-11
- Output 72: PDF/UA rule 7.1-3
- Output 72: PDF/UA rule 7.1-8
- Output 73: PDF/UA rule 6.2-1
- Output 73: PDF/UA rule 7.1-10
- Output 73: PDF/UA rule 7.1-11
- Output 73: PDF/UA rule 7.1-3
- Output 73: PDF/UA rule 7.1-8
- Output 74: PDF/UA rule 6.2-1
- Output 74: PDF/UA rule 7.1-10
- Output 74: PDF/UA rule 7.1-11
- Output 74: PDF/UA rule 7.1-3
- Output 74: PDF/UA rule 7.1-8
- Output 75: PDF/UA rule 6.2-1
- Output 75: PDF/UA rule 7.1-10
- Output 75: PDF/UA rule 7.1-11
- Output 75: PDF/UA rule 7.1-3
- Output 75: PDF/UA rule 7.1-8
- Output 76: PDF/UA rule 6.2-1
- Output 76: PDF/UA rule 7.1-10
- Output 76: PDF/UA rule 7.1-11
- Output 76: PDF/UA rule 7.1-3
- Output 76: PDF/UA rule 7.1-8
- Output 77: PDF/UA rule 6.2-1
- Output 77: PDF/UA rule 7.1-10
- Output 77: PDF/UA rule 7.1-11
- Output 77: PDF/UA rule 7.1-3
- Output 77: PDF/UA rule 7.1-8
- Output 78: PDF/UA rule 6.2-1
- Output 78: PDF/UA rule 7.1-10
- Output 78: PDF/UA rule 7.1-11
- Output 78: PDF/UA rule 7.1-3
- Output 78: PDF/UA rule 7.1-8
- Output 78: PDF/UA rule 7.2-34
- Output 79: PDF/UA rule 6.2-1
- Output 79: PDF/UA rule 7.1-10
- Output 79: PDF/UA rule 7.1-11
- Output 79: PDF/UA rule 7.1-3
- Output 79: PDF/UA rule 7.1-8
- Output 80: PDF/UA rule 6.2-1
- Output 80: PDF/UA rule 7.1-10
- Output 80: PDF/UA rule 7.1-11
- Output 80: PDF/UA rule 7.1-3
- Output 80: PDF/UA rule 7.1-8
- Output 81: PDF/UA rule 6.2-1
- Output 81: PDF/UA rule 7.1-10
- Output 81: PDF/UA rule 7.1-11
- Output 81: PDF/UA rule 7.1-3
- Output 81: PDF/UA rule 7.1-8
- Output 82: PDF/UA rule 6.2-1
- Output 82: PDF/UA rule 7.1-10
- Output 82: PDF/UA rule 7.1-11
- Output 82: PDF/UA rule 7.1-3
- Output 82: PDF/UA rule 7.1-8
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 563 → 0
- role_map_count: 3 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 320 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-ref-2-09-scanned --output lab/reproduction.json
```

### ua1-ref-2-09-scanned-ghostscript-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 1: PDF/UA rule 7.21.4.2-2
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 563 → 0
- role_map_count: 9 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-ref-2-09-scanned --output lab/reproduction.json
```

### ua1-ref-2-09-scanned-ghostscript-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.21.4.2-2
- Output 2: PDF/UA rule 5-1
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.2-33
- Output 2: PDF/UA rule 7.21.4.2-2
- Output 3: PDF/UA rule 5-1
- Output 3: PDF/UA rule 6.2-1
- Output 3: PDF/UA rule 7.1-10
- Output 3: PDF/UA rule 7.1-11
- Output 3: PDF/UA rule 7.1-3
- Output 3: PDF/UA rule 7.2-33
- Output 3: PDF/UA rule 7.21.4.2-2
- Output 4: PDF/UA rule 5-1
- Output 4: PDF/UA rule 6.2-1
- Output 4: PDF/UA rule 7.1-10
- Output 4: PDF/UA rule 7.1-11
- Output 4: PDF/UA rule 7.1-3
- Output 4: PDF/UA rule 7.2-33
- Output 4: PDF/UA rule 7.21.4.2-2
- Output 5: PDF/UA rule 5-1
- Output 5: PDF/UA rule 6.2-1
- Output 5: PDF/UA rule 7.1-10
- Output 5: PDF/UA rule 7.1-11
- Output 5: PDF/UA rule 7.1-3
- Output 5: PDF/UA rule 7.2-33
- Output 5: PDF/UA rule 7.21.4.2-2
- Output 6: PDF/UA rule 5-1
- Output 6: PDF/UA rule 6.2-1
- Output 6: PDF/UA rule 7.1-10
- Output 6: PDF/UA rule 7.1-11
- Output 6: PDF/UA rule 7.1-3
- Output 6: PDF/UA rule 7.2-33
- Output 6: PDF/UA rule 7.21.4.2-2
- Output 7: PDF/UA rule 5-1
- Output 7: PDF/UA rule 6.2-1
- Output 7: PDF/UA rule 7.1-10
- Output 7: PDF/UA rule 7.1-11
- Output 7: PDF/UA rule 7.1-3
- Output 7: PDF/UA rule 7.2-33
- Output 7: PDF/UA rule 7.21.4.2-2
- Output 8: PDF/UA rule 5-1
- Output 8: PDF/UA rule 6.2-1
- Output 8: PDF/UA rule 7.1-10
- Output 8: PDF/UA rule 7.1-11
- Output 8: PDF/UA rule 7.1-3
- Output 8: PDF/UA rule 7.2-33
- Output 8: PDF/UA rule 7.21.4.2-2
- Output 9: PDF/UA rule 5-1
- Output 9: PDF/UA rule 6.2-1
- Output 9: PDF/UA rule 7.1-10
- Output 9: PDF/UA rule 7.1-11
- Output 9: PDF/UA rule 7.1-3
- Output 9: PDF/UA rule 7.2-33
- Output 9: PDF/UA rule 7.2-34
- Output 9: PDF/UA rule 7.21.4.2-2
- Output 10: PDF/UA rule 5-1
- Output 10: PDF/UA rule 6.2-1
- Output 10: PDF/UA rule 7.1-10
- Output 10: PDF/UA rule 7.1-11
- Output 10: PDF/UA rule 7.1-3
- Output 10: PDF/UA rule 7.2-33
- Output 10: PDF/UA rule 7.21.4.2-2
- Output 11: PDF/UA rule 5-1
- Output 11: PDF/UA rule 6.2-1
- Output 11: PDF/UA rule 7.1-10
- Output 11: PDF/UA rule 7.1-11
- Output 11: PDF/UA rule 7.1-3
- Output 11: PDF/UA rule 7.2-33
- Output 11: PDF/UA rule 7.21.4.2-2
- Output 12: PDF/UA rule 5-1
- Output 12: PDF/UA rule 6.2-1
- Output 12: PDF/UA rule 7.1-10
- Output 12: PDF/UA rule 7.1-11
- Output 12: PDF/UA rule 7.1-3
- Output 12: PDF/UA rule 7.2-33
- Output 12: PDF/UA rule 7.21.4.2-2
- Output 13: PDF/UA rule 5-1
- Output 13: PDF/UA rule 6.2-1
- Output 13: PDF/UA rule 7.1-10
- Output 13: PDF/UA rule 7.1-11
- Output 13: PDF/UA rule 7.1-3
- Output 13: PDF/UA rule 7.2-33
- Output 13: PDF/UA rule 7.21.4.2-2
- Output 14: PDF/UA rule 5-1
- Output 14: PDF/UA rule 6.2-1
- Output 14: PDF/UA rule 7.1-10
- Output 14: PDF/UA rule 7.1-11
- Output 14: PDF/UA rule 7.1-3
- Output 14: PDF/UA rule 7.2-33
- Output 14: PDF/UA rule 7.21.4.2-2
- Output 15: PDF/UA rule 5-1
- Output 15: PDF/UA rule 6.2-1
- Output 15: PDF/UA rule 7.1-10
- Output 15: PDF/UA rule 7.1-11
- Output 15: PDF/UA rule 7.1-3
- Output 15: PDF/UA rule 7.2-33
- Output 15: PDF/UA rule 7.21.4.2-2
- Output 16: PDF/UA rule 5-1
- Output 16: PDF/UA rule 6.2-1
- Output 16: PDF/UA rule 7.1-10
- Output 16: PDF/UA rule 7.1-11
- Output 16: PDF/UA rule 7.1-3
- Output 16: PDF/UA rule 7.2-33
- Output 16: PDF/UA rule 7.21.4.2-2
- Output 17: PDF/UA rule 5-1
- Output 17: PDF/UA rule 6.2-1
- Output 17: PDF/UA rule 7.1-10
- Output 17: PDF/UA rule 7.1-11
- Output 17: PDF/UA rule 7.1-3
- Output 17: PDF/UA rule 7.2-33
- Output 17: PDF/UA rule 7.21.4.2-2
- Output 18: PDF/UA rule 5-1
- Output 18: PDF/UA rule 6.2-1
- Output 18: PDF/UA rule 7.1-10
- Output 18: PDF/UA rule 7.1-11
- Output 18: PDF/UA rule 7.1-3
- Output 18: PDF/UA rule 7.2-33
- Output 18: PDF/UA rule 7.21.4.2-2
- Output 19: PDF/UA rule 5-1
- Output 19: PDF/UA rule 6.2-1
- Output 19: PDF/UA rule 7.1-10
- Output 19: PDF/UA rule 7.1-11
- Output 19: PDF/UA rule 7.1-3
- Output 19: PDF/UA rule 7.2-33
- Output 19: PDF/UA rule 7.2-34
- Output 19: PDF/UA rule 7.21.4.2-2
- Output 20: PDF/UA rule 5-1
- Output 20: PDF/UA rule 6.2-1
- Output 20: PDF/UA rule 7.1-10
- Output 20: PDF/UA rule 7.1-11
- Output 20: PDF/UA rule 7.1-3
- Output 20: PDF/UA rule 7.2-33
- Output 20: PDF/UA rule 7.21.4.2-2
- Output 21: PDF/UA rule 5-1
- Output 21: PDF/UA rule 6.2-1
- Output 21: PDF/UA rule 7.1-10
- Output 21: PDF/UA rule 7.1-11
- Output 21: PDF/UA rule 7.1-3
- Output 21: PDF/UA rule 7.2-33
- Output 21: PDF/UA rule 7.2-34
- Output 21: PDF/UA rule 7.21.4.2-2
- Output 22: PDF/UA rule 5-1
- Output 22: PDF/UA rule 6.2-1
- Output 22: PDF/UA rule 7.1-10
- Output 22: PDF/UA rule 7.1-11
- Output 22: PDF/UA rule 7.1-3
- Output 22: PDF/UA rule 7.2-33
- Output 22: PDF/UA rule 7.2-34
- Output 22: PDF/UA rule 7.21.4.2-2
- Output 23: PDF/UA rule 5-1
- Output 23: PDF/UA rule 6.2-1
- Output 23: PDF/UA rule 7.1-10
- Output 23: PDF/UA rule 7.1-11
- Output 23: PDF/UA rule 7.1-3
- Output 23: PDF/UA rule 7.2-33
- Output 23: PDF/UA rule 7.21.4.2-2
- Output 24: PDF/UA rule 5-1
- Output 24: PDF/UA rule 6.2-1
- Output 24: PDF/UA rule 7.1-10
- Output 24: PDF/UA rule 7.1-11
- Output 24: PDF/UA rule 7.1-3
- Output 24: PDF/UA rule 7.2-33
- Output 24: PDF/UA rule 7.21.4.2-2
- Output 25: PDF/UA rule 5-1
- Output 25: PDF/UA rule 6.2-1
- Output 25: PDF/UA rule 7.1-10
- Output 25: PDF/UA rule 7.1-11
- Output 25: PDF/UA rule 7.1-3
- Output 25: PDF/UA rule 7.2-33
- Output 25: PDF/UA rule 7.21.4.2-2
- Output 26: PDF/UA rule 5-1
- Output 26: PDF/UA rule 6.2-1
- Output 26: PDF/UA rule 7.1-10
- Output 26: PDF/UA rule 7.1-11
- Output 26: PDF/UA rule 7.1-3
- Output 26: PDF/UA rule 7.2-33
- Output 26: PDF/UA rule 7.21.4.2-2
- Output 27: PDF/UA rule 5-1
- Output 27: PDF/UA rule 6.2-1
- Output 27: PDF/UA rule 7.1-10
- Output 27: PDF/UA rule 7.1-11
- Output 27: PDF/UA rule 7.1-3
- Output 27: PDF/UA rule 7.2-33
- Output 27: PDF/UA rule 7.21.4.2-2
- Output 28: PDF/UA rule 5-1
- Output 28: PDF/UA rule 6.2-1
- Output 28: PDF/UA rule 7.1-10
- Output 28: PDF/UA rule 7.1-11
- Output 28: PDF/UA rule 7.1-3
- Output 28: PDF/UA rule 7.2-33
- Output 28: PDF/UA rule 7.21.4.2-2
- Output 29: PDF/UA rule 5-1
- Output 29: PDF/UA rule 6.2-1
- Output 29: PDF/UA rule 7.1-10
- Output 29: PDF/UA rule 7.1-11
- Output 29: PDF/UA rule 7.1-3
- Output 29: PDF/UA rule 7.2-33
- Output 29: PDF/UA rule 7.21.4.2-2
- Output 30: PDF/UA rule 5-1
- Output 30: PDF/UA rule 6.2-1
- Output 30: PDF/UA rule 7.1-10
- Output 30: PDF/UA rule 7.1-11
- Output 30: PDF/UA rule 7.1-3
- Output 30: PDF/UA rule 7.2-33
- Output 30: PDF/UA rule 7.21.4.2-2
- Output 31: PDF/UA rule 5-1
- Output 31: PDF/UA rule 6.2-1
- Output 31: PDF/UA rule 7.1-10
- Output 31: PDF/UA rule 7.1-11
- Output 31: PDF/UA rule 7.1-3
- Output 31: PDF/UA rule 7.2-33
- Output 31: PDF/UA rule 7.21.4.2-2
- Output 32: PDF/UA rule 5-1
- Output 32: PDF/UA rule 6.2-1
- Output 32: PDF/UA rule 7.1-10
- Output 32: PDF/UA rule 7.1-11
- Output 32: PDF/UA rule 7.1-3
- Output 32: PDF/UA rule 7.2-33
- Output 32: PDF/UA rule 7.21.4.2-2
- Output 33: PDF/UA rule 5-1
- Output 33: PDF/UA rule 6.2-1
- Output 33: PDF/UA rule 7.1-10
- Output 33: PDF/UA rule 7.1-11
- Output 33: PDF/UA rule 7.1-3
- Output 33: PDF/UA rule 7.2-33
- Output 33: PDF/UA rule 7.21.4.2-2
- Output 34: PDF/UA rule 5-1
- Output 34: PDF/UA rule 6.2-1
- Output 34: PDF/UA rule 7.1-10
- Output 34: PDF/UA rule 7.1-11
- Output 34: PDF/UA rule 7.1-3
- Output 34: PDF/UA rule 7.2-33
- Output 34: PDF/UA rule 7.21.4.2-2
- Output 35: PDF/UA rule 5-1
- Output 35: PDF/UA rule 6.2-1
- Output 35: PDF/UA rule 7.1-10
- Output 35: PDF/UA rule 7.1-11
- Output 35: PDF/UA rule 7.1-3
- Output 35: PDF/UA rule 7.2-33
- Output 35: PDF/UA rule 7.21.4.2-2
- Output 36: PDF/UA rule 5-1
- Output 36: PDF/UA rule 6.2-1
- Output 36: PDF/UA rule 7.1-10
- Output 36: PDF/UA rule 7.1-11
- Output 36: PDF/UA rule 7.1-3
- Output 36: PDF/UA rule 7.2-33
- Output 36: PDF/UA rule 7.21.4.2-2
- Output 37: PDF/UA rule 5-1
- Output 37: PDF/UA rule 6.2-1
- Output 37: PDF/UA rule 7.1-10
- Output 37: PDF/UA rule 7.1-11
- Output 37: PDF/UA rule 7.1-3
- Output 37: PDF/UA rule 7.2-33
- Output 37: PDF/UA rule 7.21.4.2-2
- Output 38: PDF/UA rule 5-1
- Output 38: PDF/UA rule 6.2-1
- Output 38: PDF/UA rule 7.1-10
- Output 38: PDF/UA rule 7.1-11
- Output 38: PDF/UA rule 7.1-3
- Output 38: PDF/UA rule 7.2-33
- Output 38: PDF/UA rule 7.21.4.2-2
- Output 39: PDF/UA rule 5-1
- Output 39: PDF/UA rule 6.2-1
- Output 39: PDF/UA rule 7.1-10
- Output 39: PDF/UA rule 7.1-11
- Output 39: PDF/UA rule 7.1-3
- Output 39: PDF/UA rule 7.2-33
- Output 39: PDF/UA rule 7.21.4.2-2
- Output 40: PDF/UA rule 5-1
- Output 40: PDF/UA rule 6.2-1
- Output 40: PDF/UA rule 7.1-10
- Output 40: PDF/UA rule 7.1-11
- Output 40: PDF/UA rule 7.1-3
- Output 40: PDF/UA rule 7.2-33
- Output 40: PDF/UA rule 7.21.4.2-2
- Output 41: PDF/UA rule 5-1
- Output 41: PDF/UA rule 6.2-1
- Output 41: PDF/UA rule 7.1-10
- Output 41: PDF/UA rule 7.1-11
- Output 41: PDF/UA rule 7.1-3
- Output 41: PDF/UA rule 7.2-33
- Output 41: PDF/UA rule 7.21.4.2-2
- Output 42: PDF/UA rule 5-1
- Output 42: PDF/UA rule 6.2-1
- Output 42: PDF/UA rule 7.1-10
- Output 42: PDF/UA rule 7.1-11
- Output 42: PDF/UA rule 7.1-3
- Output 42: PDF/UA rule 7.2-33
- Output 42: PDF/UA rule 7.21.4.2-2
- Output 43: PDF/UA rule 5-1
- Output 43: PDF/UA rule 6.2-1
- Output 43: PDF/UA rule 7.1-10
- Output 43: PDF/UA rule 7.1-11
- Output 43: PDF/UA rule 7.1-3
- Output 43: PDF/UA rule 7.2-33
- Output 43: PDF/UA rule 7.21.4.2-2
- Output 44: PDF/UA rule 5-1
- Output 44: PDF/UA rule 6.2-1
- Output 44: PDF/UA rule 7.1-10
- Output 44: PDF/UA rule 7.1-11
- Output 44: PDF/UA rule 7.1-3
- Output 44: PDF/UA rule 7.2-33
- Output 44: PDF/UA rule 7.21.4.2-2
- Output 45: PDF/UA rule 5-1
- Output 45: PDF/UA rule 6.2-1
- Output 45: PDF/UA rule 7.1-10
- Output 45: PDF/UA rule 7.1-11
- Output 45: PDF/UA rule 7.1-3
- Output 45: PDF/UA rule 7.2-33
- Output 45: PDF/UA rule 7.21.4.2-2
- Output 46: PDF/UA rule 5-1
- Output 46: PDF/UA rule 6.2-1
- Output 46: PDF/UA rule 7.1-10
- Output 46: PDF/UA rule 7.1-11
- Output 46: PDF/UA rule 7.1-3
- Output 46: PDF/UA rule 7.2-33
- Output 46: PDF/UA rule 7.21.4.2-2
- Output 47: PDF/UA rule 5-1
- Output 47: PDF/UA rule 6.2-1
- Output 47: PDF/UA rule 7.1-10
- Output 47: PDF/UA rule 7.1-11
- Output 47: PDF/UA rule 7.1-3
- Output 47: PDF/UA rule 7.2-33
- Output 47: PDF/UA rule 7.21.4.2-2
- Output 48: PDF/UA rule 5-1
- Output 48: PDF/UA rule 6.2-1
- Output 48: PDF/UA rule 7.1-10
- Output 48: PDF/UA rule 7.1-11
- Output 48: PDF/UA rule 7.1-3
- Output 48: PDF/UA rule 7.2-33
- Output 48: PDF/UA rule 7.21.4.2-2
- Output 49: PDF/UA rule 5-1
- Output 49: PDF/UA rule 6.2-1
- Output 49: PDF/UA rule 7.1-10
- Output 49: PDF/UA rule 7.1-11
- Output 49: PDF/UA rule 7.1-3
- Output 49: PDF/UA rule 7.2-33
- Output 49: PDF/UA rule 7.21.4.2-2
- Output 50: PDF/UA rule 5-1
- Output 50: PDF/UA rule 6.2-1
- Output 50: PDF/UA rule 7.1-10
- Output 50: PDF/UA rule 7.1-11
- Output 50: PDF/UA rule 7.1-3
- Output 50: PDF/UA rule 7.2-33
- Output 50: PDF/UA rule 7.21.4.2-2
- Output 51: PDF/UA rule 5-1
- Output 51: PDF/UA rule 6.2-1
- Output 51: PDF/UA rule 7.1-10
- Output 51: PDF/UA rule 7.1-11
- Output 51: PDF/UA rule 7.1-3
- Output 51: PDF/UA rule 7.2-33
- Output 51: PDF/UA rule 7.21.4.2-2
- Output 52: PDF/UA rule 5-1
- Output 52: PDF/UA rule 6.2-1
- Output 52: PDF/UA rule 7.1-10
- Output 52: PDF/UA rule 7.1-11
- Output 52: PDF/UA rule 7.1-3
- Output 52: PDF/UA rule 7.2-33
- Output 52: PDF/UA rule 7.21.4.2-2
- Output 53: PDF/UA rule 5-1
- Output 53: PDF/UA rule 6.2-1
- Output 53: PDF/UA rule 7.1-10
- Output 53: PDF/UA rule 7.1-11
- Output 53: PDF/UA rule 7.1-3
- Output 53: PDF/UA rule 7.2-33
- Output 53: PDF/UA rule 7.21.4.2-2
- Output 54: PDF/UA rule 5-1
- Output 54: PDF/UA rule 6.2-1
- Output 54: PDF/UA rule 7.1-10
- Output 54: PDF/UA rule 7.1-11
- Output 54: PDF/UA rule 7.1-3
- Output 54: PDF/UA rule 7.2-33
- Output 54: PDF/UA rule 7.21.4.2-2
- Output 55: PDF/UA rule 5-1
- Output 55: PDF/UA rule 6.2-1
- Output 55: PDF/UA rule 7.1-10
- Output 55: PDF/UA rule 7.1-11
- Output 55: PDF/UA rule 7.1-3
- Output 55: PDF/UA rule 7.2-33
- Output 55: PDF/UA rule 7.21.4.2-2
- Output 56: PDF/UA rule 5-1
- Output 56: PDF/UA rule 6.2-1
- Output 56: PDF/UA rule 7.1-10
- Output 56: PDF/UA rule 7.1-11
- Output 56: PDF/UA rule 7.1-3
- Output 56: PDF/UA rule 7.2-33
- Output 56: PDF/UA rule 7.21.4.2-2
- Output 57: PDF/UA rule 5-1
- Output 57: PDF/UA rule 6.2-1
- Output 57: PDF/UA rule 7.1-10
- Output 57: PDF/UA rule 7.1-11
- Output 57: PDF/UA rule 7.1-3
- Output 57: PDF/UA rule 7.2-33
- Output 57: PDF/UA rule 7.21.4.2-2
- Output 58: PDF/UA rule 5-1
- Output 58: PDF/UA rule 6.2-1
- Output 58: PDF/UA rule 7.1-10
- Output 58: PDF/UA rule 7.1-11
- Output 58: PDF/UA rule 7.1-3
- Output 58: PDF/UA rule 7.2-33
- Output 58: PDF/UA rule 7.21.4.2-2
- Output 59: PDF/UA rule 5-1
- Output 59: PDF/UA rule 6.2-1
- Output 59: PDF/UA rule 7.1-10
- Output 59: PDF/UA rule 7.1-11
- Output 59: PDF/UA rule 7.1-3
- Output 59: PDF/UA rule 7.2-33
- Output 59: PDF/UA rule 7.21.4.2-2
- Output 60: PDF/UA rule 5-1
- Output 60: PDF/UA rule 6.2-1
- Output 60: PDF/UA rule 7.1-10
- Output 60: PDF/UA rule 7.1-11
- Output 60: PDF/UA rule 7.1-3
- Output 60: PDF/UA rule 7.2-33
- Output 60: PDF/UA rule 7.21.4.2-2
- Output 61: PDF/UA rule 5-1
- Output 61: PDF/UA rule 6.2-1
- Output 61: PDF/UA rule 7.1-10
- Output 61: PDF/UA rule 7.1-11
- Output 61: PDF/UA rule 7.1-3
- Output 61: PDF/UA rule 7.2-33
- Output 61: PDF/UA rule 7.21.4.2-2
- Output 62: PDF/UA rule 5-1
- Output 62: PDF/UA rule 6.2-1
- Output 62: PDF/UA rule 7.1-10
- Output 62: PDF/UA rule 7.1-11
- Output 62: PDF/UA rule 7.1-3
- Output 62: PDF/UA rule 7.2-33
- Output 62: PDF/UA rule 7.21.4.2-2
- Output 63: PDF/UA rule 5-1
- Output 63: PDF/UA rule 6.2-1
- Output 63: PDF/UA rule 7.1-10
- Output 63: PDF/UA rule 7.1-11
- Output 63: PDF/UA rule 7.1-3
- Output 63: PDF/UA rule 7.2-33
- Output 63: PDF/UA rule 7.2-34
- Output 63: PDF/UA rule 7.21.4.2-2
- Output 64: PDF/UA rule 5-1
- Output 64: PDF/UA rule 6.2-1
- Output 64: PDF/UA rule 7.1-10
- Output 64: PDF/UA rule 7.1-11
- Output 64: PDF/UA rule 7.1-3
- Output 64: PDF/UA rule 7.2-33
- Output 64: PDF/UA rule 7.21.4.2-2
- Output 65: PDF/UA rule 5-1
- Output 65: PDF/UA rule 6.2-1
- Output 65: PDF/UA rule 7.1-10
- Output 65: PDF/UA rule 7.1-11
- Output 65: PDF/UA rule 7.1-3
- Output 65: PDF/UA rule 7.2-33
- Output 65: PDF/UA rule 7.21.4.2-2
- Output 66: PDF/UA rule 5-1
- Output 66: PDF/UA rule 6.2-1
- Output 66: PDF/UA rule 7.1-10
- Output 66: PDF/UA rule 7.1-11
- Output 66: PDF/UA rule 7.1-3
- Output 66: PDF/UA rule 7.2-33
- Output 66: PDF/UA rule 7.21.4.2-2
- Output 67: PDF/UA rule 5-1
- Output 67: PDF/UA rule 6.2-1
- Output 67: PDF/UA rule 7.1-10
- Output 67: PDF/UA rule 7.1-11
- Output 67: PDF/UA rule 7.1-3
- Output 67: PDF/UA rule 7.2-33
- Output 67: PDF/UA rule 7.21.4.2-2
- Output 68: PDF/UA rule 5-1
- Output 68: PDF/UA rule 6.2-1
- Output 68: PDF/UA rule 7.1-10
- Output 68: PDF/UA rule 7.1-11
- Output 68: PDF/UA rule 7.1-3
- Output 68: PDF/UA rule 7.2-33
- Output 68: PDF/UA rule 7.21.4.2-2
- Output 69: PDF/UA rule 5-1
- Output 69: PDF/UA rule 6.2-1
- Output 69: PDF/UA rule 7.1-10
- Output 69: PDF/UA rule 7.1-11
- Output 69: PDF/UA rule 7.1-3
- Output 69: PDF/UA rule 7.2-33
- Output 69: PDF/UA rule 7.21.4.2-2
- Output 70: PDF/UA rule 5-1
- Output 70: PDF/UA rule 6.2-1
- Output 70: PDF/UA rule 7.1-10
- Output 70: PDF/UA rule 7.1-11
- Output 70: PDF/UA rule 7.1-3
- Output 70: PDF/UA rule 7.2-33
- Output 70: PDF/UA rule 7.21.4.2-2
- Output 71: PDF/UA rule 5-1
- Output 71: PDF/UA rule 6.2-1
- Output 71: PDF/UA rule 7.1-10
- Output 71: PDF/UA rule 7.1-11
- Output 71: PDF/UA rule 7.1-3
- Output 71: PDF/UA rule 7.2-33
- Output 71: PDF/UA rule 7.21.4.2-2
- Output 72: PDF/UA rule 5-1
- Output 72: PDF/UA rule 6.2-1
- Output 72: PDF/UA rule 7.1-10
- Output 72: PDF/UA rule 7.1-11
- Output 72: PDF/UA rule 7.1-3
- Output 72: PDF/UA rule 7.2-33
- Output 72: PDF/UA rule 7.21.4.2-2
- Output 73: PDF/UA rule 5-1
- Output 73: PDF/UA rule 6.2-1
- Output 73: PDF/UA rule 7.1-10
- Output 73: PDF/UA rule 7.1-11
- Output 73: PDF/UA rule 7.1-3
- Output 73: PDF/UA rule 7.2-33
- Output 73: PDF/UA rule 7.21.4.2-2
- Output 74: PDF/UA rule 5-1
- Output 74: PDF/UA rule 6.2-1
- Output 74: PDF/UA rule 7.1-10
- Output 74: PDF/UA rule 7.1-11
- Output 74: PDF/UA rule 7.1-3
- Output 74: PDF/UA rule 7.2-33
- Output 74: PDF/UA rule 7.21.4.2-2
- Output 75: PDF/UA rule 5-1
- Output 75: PDF/UA rule 6.2-1
- Output 75: PDF/UA rule 7.1-10
- Output 75: PDF/UA rule 7.1-11
- Output 75: PDF/UA rule 7.1-3
- Output 75: PDF/UA rule 7.2-33
- Output 75: PDF/UA rule 7.21.4.2-2
- Output 76: PDF/UA rule 5-1
- Output 76: PDF/UA rule 6.2-1
- Output 76: PDF/UA rule 7.1-10
- Output 76: PDF/UA rule 7.1-11
- Output 76: PDF/UA rule 7.1-3
- Output 76: PDF/UA rule 7.2-33
- Output 76: PDF/UA rule 7.21.4.2-2
- Output 77: PDF/UA rule 5-1
- Output 77: PDF/UA rule 6.2-1
- Output 77: PDF/UA rule 7.1-10
- Output 77: PDF/UA rule 7.1-11
- Output 77: PDF/UA rule 7.1-3
- Output 77: PDF/UA rule 7.2-33
- Output 77: PDF/UA rule 7.21.4.2-2
- Output 78: PDF/UA rule 5-1
- Output 78: PDF/UA rule 6.2-1
- Output 78: PDF/UA rule 7.1-10
- Output 78: PDF/UA rule 7.1-11
- Output 78: PDF/UA rule 7.1-3
- Output 78: PDF/UA rule 7.2-33
- Output 78: PDF/UA rule 7.2-34
- Output 78: PDF/UA rule 7.21.4.2-2
- Output 79: PDF/UA rule 5-1
- Output 79: PDF/UA rule 6.2-1
- Output 79: PDF/UA rule 7.1-10
- Output 79: PDF/UA rule 7.1-11
- Output 79: PDF/UA rule 7.1-3
- Output 79: PDF/UA rule 7.2-33
- Output 79: PDF/UA rule 7.21.4.2-2
- Output 80: PDF/UA rule 5-1
- Output 80: PDF/UA rule 6.2-1
- Output 80: PDF/UA rule 7.1-10
- Output 80: PDF/UA rule 7.1-11
- Output 80: PDF/UA rule 7.1-3
- Output 80: PDF/UA rule 7.2-33
- Output 80: PDF/UA rule 7.21.4.2-2
- Output 81: PDF/UA rule 5-1
- Output 81: PDF/UA rule 6.2-1
- Output 81: PDF/UA rule 7.1-10
- Output 81: PDF/UA rule 7.1-11
- Output 81: PDF/UA rule 7.1-3
- Output 81: PDF/UA rule 7.2-33
- Output 81: PDF/UA rule 7.21.4.2-2
- Output 82: PDF/UA rule 5-1
- Output 82: PDF/UA rule 6.2-1
- Output 82: PDF/UA rule 7.1-10
- Output 82: PDF/UA rule 7.1-11
- Output 82: PDF/UA rule 7.1-3
- Output 82: PDF/UA rule 7.2-33
- Output 82: PDF/UA rule 7.21.4.2-2
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 563 → 0
- role_map_count: 3 → 0
- document_language_present: True → False
- outline_count: 320 → 3

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-ref-2-09-scanned --output lab/reproduction.json
```

### ua1-ref-2-09-scanned-ghostscript-resave

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 1: PDF/UA rule 7.21.4.2-2
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 563 → 0
- role_map_count: 3 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-ref-2-09-scanned --output lab/reproduction.json
```

### ua1-ref-2-10-form-qpdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.4-1
- Output 1: PDF/UA rule 7.2-25
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- role_map_count: 6 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 1 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-ref-2-10-form --output lab/reproduction.json
```

### ua1-ref-2-10-form-qpdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.4-1
- Output 1: PDF/UA rule 7.2-25
- struct_tree_present: True → False
- marked_pdf: True → False
- role_map_count: 6 → 0
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-ref-2-10-form --output lab/reproduction.json
```

### ua1-ref-2-10-form-pymupdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.4-1
- Output 1: PDF/UA rule 7.2-25
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- role_map_count: 6 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 1 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-ref-2-10-form --output lab/reproduction.json
```

### ua1-ref-2-10-form-pymupdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.4-1
- Output 1: PDF/UA rule 7.2-25
- struct_tree_present: True → False
- marked_pdf: True → False
- role_map_count: 6 → 0
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-ref-2-10-form --output lab/reproduction.json
```

### ua1-ref-2-10-form-ghostscript-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- role_map_count: 6 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-ref-2-10-form --output lab/reproduction.json
```

### ua1-ref-2-10-form-ghostscript-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-33
- struct_tree_present: True → False
- marked_pdf: True → False
- role_map_count: 6 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-ref-2-10-form --output lab/reproduction.json
```

### ua1-ref-2-10-form-ghostscript-resave

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-33
- struct_tree_present: True → False
- marked_pdf: True → False
- role_map_count: 6 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-ref-2-10-form --output lab/reproduction.json
```

### ua1-heading-001-qpdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 2 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-heading-001 --output lab/reproduction.json
```

### ua1-heading-001-qpdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 1 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-heading-001 --output lab/reproduction.json
```

### ua1-heading-001-pymupdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 2 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-heading-001 --output lab/reproduction.json
```

### ua1-heading-001-pymupdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 1 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-heading-001 --output lab/reproduction.json
```

### ua1-heading-001-ghostscript-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-heading-001 --output lab/reproduction.json
```

### ua1-heading-001-ghostscript-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-heading-001 --output lab/reproduction.json
```

### ua1-heading-001-ghostscript-resave

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-heading-001 --output lab/reproduction.json
```

### ua1-link-001-qpdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 2 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-link-001 --output lab/reproduction.json
```

### ua1-link-001-qpdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 1 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-link-001 --output lab/reproduction.json
```

### ua1-link-001-pymupdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 2 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-link-001 --output lab/reproduction.json
```

### ua1-link-001-pymupdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 1 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-link-001 --output lab/reproduction.json
```

### ua1-link-001-ghostscript-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-link-001 --output lab/reproduction.json
```

### ua1-link-001-ghostscript-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-link-001 --output lab/reproduction.json
```

### ua1-link-001-ghostscript-resave

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-link-001 --output lab/reproduction.json
```

### ua1-list-001-qpdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 2 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-list-001 --output lab/reproduction.json
```

### ua1-list-001-qpdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 1 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-list-001 --output lab/reproduction.json
```

### ua1-list-001-pymupdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 2 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-list-001 --output lab/reproduction.json
```

### ua1-list-001-pymupdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 1 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-list-001 --output lab/reproduction.json
```

### ua1-list-001-ghostscript-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-list-001 --output lab/reproduction.json
```

### ua1-list-001-ghostscript-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-list-001 --output lab/reproduction.json
```

### ua1-list-001-ghostscript-resave

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-list-001 --output lab/reproduction.json
```

### ua1-paragraph-001-qpdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 2 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-paragraph-001 --output lab/reproduction.json
```

### ua1-paragraph-001-qpdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 1 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-paragraph-001 --output lab/reproduction.json
```

### ua1-paragraph-001-pymupdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 2 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-paragraph-001 --output lab/reproduction.json
```

### ua1-paragraph-001-pymupdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 1 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-paragraph-001 --output lab/reproduction.json
```

### ua1-paragraph-001-ghostscript-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-paragraph-001 --output lab/reproduction.json
```

### ua1-paragraph-001-ghostscript-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-paragraph-001 --output lab/reproduction.json
```

### ua1-paragraph-001-ghostscript-resave

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-paragraph-001 --output lab/reproduction.json
```

### ua1-table-001-qpdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 2 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-table-001 --output lab/reproduction.json
```

### ua1-table-001-qpdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.1-8
- Output 2: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 1 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-table-001 --output lab/reproduction.json
```

### ua1-table-001-pymupdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 2 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-table-001 --output lab/reproduction.json
```

### ua1-table-001-pymupdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.1-8
- Output 2: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 1 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-table-001 --output lab/reproduction.json
```

### ua1-table-001-ghostscript-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-table-001 --output lab/reproduction.json
```

### ua1-table-001-ghostscript-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 2: PDF/UA rule 5-1
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 7.1-10
- Output 2: PDF/UA rule 7.1-11
- Output 2: PDF/UA rule 7.1-3
- Output 2: PDF/UA rule 7.2-33
- Output 2: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-table-001 --output lab/reproduction.json
```

### ua1-table-001-ghostscript-resave

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-table-001 --output lab/reproduction.json
```

### ua1-unicode-001-qpdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 80 → 0
- role_map_count: 1 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 73 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-unicode-001 --output lab/reproduction.json
```

### ua1-unicode-001-qpdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 1 → 0

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-unicode-001 --output lab/reproduction.json
```

### ua1-unicode-001-pymupdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.18.1-2
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.18.5-2
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 80 → 0
- role_map_count: 1 → 0
- document_language_present: True → False
- title_present: True → False
- outline_count: 73 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-unicode-001 --output lab/reproduction.json
```

### ua1-unicode-001-pymupdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.1-8
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False
- outline_count: 1 → 0

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-unicode-001 --output lab/reproduction.json
```

### ua1-unicode-001-ghostscript-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.18.3-1
- Output 1: PDF/UA rule 7.18.5-1
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-24
- Output 1: PDF/UA rule 7.2-30
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- Output 1: PDF/UA rule 7.21.4.2-2
- Output 1: PDF/UA rule 7.21.7-1
- struct_tree_present: True → False
- marked_pdf: True → False
- alt_text_count: 80 → 0
- role_map_count: 1 → 0
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-unicode-001 --output lab/reproduction.json
```

### ua1-unicode-001-ghostscript-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-unicode-001 --output lab/reproduction.json
```

### ua1-unicode-001-ghostscript-resave

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 7.1-10
- Output 1: PDF/UA rule 7.1-11
- Output 1: PDF/UA rule 7.1-3
- Output 1: PDF/UA rule 7.2-2
- Output 1: PDF/UA rule 7.2-33
- Output 1: PDF/UA rule 7.2-34
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-unicode-001 --output lab/reproduction.json
```

### ua2-heading-001-qpdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.1-2
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations merge --fixtures ua2-heading-001 --output lab/reproduction.json
```

### ua2-heading-001-qpdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.1-2
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations split --fixtures ua2-heading-001 --output lab/reproduction.json
```

### ua2-heading-001-pymupdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.1-2
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations merge --fixtures ua2-heading-001 --output lab/reproduction.json
```

### ua2-heading-001-pymupdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.1-2
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations split --fixtures ua2-heading-001 --output lab/reproduction.json
```

### ua2-heading-001-ghostscript-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations merge --fixtures ua2-heading-001 --output lab/reproduction.json
```

### ua2-heading-001-ghostscript-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations split --fixtures ua2-heading-001 --output lab/reproduction.json
```

### ua2-heading-001-ghostscript-resave

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations resave --fixtures ua2-heading-001 --output lab/reproduction.json
```

### ua2-link-001-qpdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.1-2
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations merge --fixtures ua2-link-001 --output lab/reproduction.json
```

### ua2-link-001-qpdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.1-2
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations split --fixtures ua2-link-001 --output lab/reproduction.json
```

### ua2-link-001-pymupdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.1-2
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations merge --fixtures ua2-link-001 --output lab/reproduction.json
```

### ua2-link-001-pymupdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.1-2
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations split --fixtures ua2-link-001 --output lab/reproduction.json
```

### ua2-link-001-ghostscript-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations merge --fixtures ua2-link-001 --output lab/reproduction.json
```

### ua2-link-001-ghostscript-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations split --fixtures ua2-link-001 --output lab/reproduction.json
```

### ua2-link-001-ghostscript-resave

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations resave --fixtures ua2-link-001 --output lab/reproduction.json
```

### ua2-paragraph-001-qpdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.1-2
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations merge --fixtures ua2-paragraph-001 --output lab/reproduction.json
```

### ua2-paragraph-001-qpdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.1-2
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations split --fixtures ua2-paragraph-001 --output lab/reproduction.json
```

### ua2-paragraph-001-pymupdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.1-2
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations merge --fixtures ua2-paragraph-001 --output lab/reproduction.json
```

### ua2-paragraph-001-pymupdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.1-2
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations split --fixtures ua2-paragraph-001 --output lab/reproduction.json
```

### ua2-paragraph-001-ghostscript-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations merge --fixtures ua2-paragraph-001 --output lab/reproduction.json
```

### ua2-paragraph-001-ghostscript-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations split --fixtures ua2-paragraph-001 --output lab/reproduction.json
```

### ua2-paragraph-001-ghostscript-resave

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations resave --fixtures ua2-paragraph-001 --output lab/reproduction.json
```

### ua2-table-001-qpdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.1-2
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations merge --fixtures ua2-table-001 --output lab/reproduction.json
```

### ua2-table-001-qpdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.1-2
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 8.11.1-2
- Output 2: PDF/UA rule 8.11.2-1
- Output 2: PDF/UA rule 8.2.1-1
- Output 2: PDF/UA rule 8.2.2-1
- Output 2: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations split --fixtures ua2-table-001 --output lab/reproduction.json
```

### ua2-table-001-pymupdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.1-2
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations merge --fixtures ua2-table-001 --output lab/reproduction.json
```

### ua2-table-001-pymupdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.1-2
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 8.11.1-2
- Output 2: PDF/UA rule 8.11.2-1
- Output 2: PDF/UA rule 8.2.1-1
- Output 2: PDF/UA rule 8.2.2-1
- Output 2: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations split --fixtures ua2-table-001 --output lab/reproduction.json
```

### ua2-table-001-ghostscript-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations merge --fixtures ua2-table-001 --output lab/reproduction.json
```

### ua2-table-001-ghostscript-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- Output 2: PDF/UA rule 5-1
- Output 2: PDF/UA rule 6.2-1
- Output 2: PDF/UA rule 8.11.2-1
- Output 2: PDF/UA rule 8.2.1-1
- Output 2: PDF/UA rule 8.2.2-1
- Output 2: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations split --fixtures ua2-table-001 --output lab/reproduction.json
```

### ua2-table-001-ghostscript-resave

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations resave --fixtures ua2-table-001 --output lab/reproduction.json
```

### ua2-unicode-001-qpdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.1-2
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations merge --fixtures ua2-unicode-001 --output lab/reproduction.json
```

### ua2-unicode-001-qpdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.1-2
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations split --fixtures ua2-unicode-001 --output lab/reproduction.json
```

### ua2-unicode-001-pymupdf-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.1-2
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations merge --fixtures ua2-unicode-001 --output lab/reproduction.json
```

### ua2-unicode-001-pymupdf-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.1-2
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False
- title_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations split --fixtures ua2-unicode-001 --output lab/reproduction.json
```

### ua2-unicode-001-ghostscript-merge

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations merge --fixtures ua2-unicode-001 --output lab/reproduction.json
```

### ua2-unicode-001-ghostscript-split

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations split --fixtures ua2-unicode-001 --output lab/reproduction.json
```

### ua2-unicode-001-ghostscript-resave

Classification: new_pdfua_violation
- Output 1: PDF/UA rule 5-1
- Output 1: PDF/UA rule 6.2-1
- Output 1: PDF/UA rule 8.11.2-1
- Output 1: PDF/UA rule 8.2.1-1
- Output 1: PDF/UA rule 8.2.2-1
- Output 1: PDF/UA rule 8.4.4-1
- struct_tree_present: True → False
- marked_pdf: True → False
- document_language_present: True → False

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations resave --fixtures ua2-unicode-001 --output lab/reproduction.json
```

Use the recorded tool versions and corpus. Output numbers refer to result order, not inferred PDF page/object locations.
