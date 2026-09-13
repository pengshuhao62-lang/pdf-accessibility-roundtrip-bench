# v0.3.0 measured matrix summary

Two independent 180-case runs completed: macOS 15.5 arm64 locally and macOS 14
in GitHub Actions. Each run measured 40 passing cases and 140 cases with PDF/UA
violations, with zero baseline, transformation or infrastructure failures.

| Measure | Local Mac | macOS 14 CI |
| --- | ---: | ---: |
| Completed/self-comparable cases | 180 | 180 |
| Captured failed checks | 335,159 | 335,159 |
| Checks with verified output-page anchors | 330,557 | 330,557 |
| Checks explicitly unresolved to a page | 4,602 | 4,602 |
| Incomparable cases | 0 | 0 |
| Persistent rule/structure signals in self-comparison | 5,408 | 5,408 |
| New signals in self-comparison | 0 | 0 |

Both runs preserved the 20 original fixtures, PDF/UA-1 and PDF/UA-2, and all
qpdf/PyMuPDF/Ghostscript merge/split/resave combinations. Independent replay
of representative merge, split and resave bundles completed with no new signals.
Self-comparison validates recorded evidence consistency, not determinism by itself;
the three separately executed bundle replays provide the reproduction checks.

The largest output had 21,381 failed checks. The official veraPDF 1.30.2 retained
10,005 detailed records, while the full-checks overlay retained all 21,381 with
the same conformance outcome, failed-rule IDs and total failure count.

These counts are repeated checks/signals, not distinct bugs. Verified locations
refer to output PDFs and do not infer original input pages. Unresolved checks
are retained. Human screen-reader review is separate.

## Inspect the evidence

- [Local environment and acceptance](example-v0.3.0-summary.json)
- [CI environment and acceptance](ci-summary-v0.3.0.json)
- [Complete readable Markdown report](https://github.com/pengshuhao62-lang/pdf-accessibility-roundtrip-bench/releases/download/v0.3.0/pdfua-bench-v0.3.0-full-run.md)
- [Complete local JSON, lossless gzip](https://github.com/pengshuhao62-lang/pdf-accessibility-roundtrip-bench/releases/download/v0.3.0/pdfua-bench-v0.3.0-full-run.json.gz)
- [Complete CI JSON, lossless gzip](https://github.com/pengshuhao62-lang/pdf-accessibility-roundtrip-bench/releases/download/v0.3.0/pdfua-bench-v0.3.0-ci-run.json.gz)
- [Self-authored reproduction bundle](https://github.com/pengshuhao62-lang/pdf-accessibility-roundtrip-bench/releases/download/v0.3.0/pdfua-bench-v0.3.0-example-case.zip)

Full Markdown previews 30 checks per output and explicitly labels the preview;
complete JSON retains every check. Local and CI environments differ and are not
used as each other's tool-version reference. See the [release notes](../docs/release-v0.3.0.md).
