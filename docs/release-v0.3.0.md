# v0.3.0 — Evidence-linked diagnostics and case reproduction

## What's new

- Failed-check evidence with verified output-page anchors, validator-reported
  objects, exact rule pointers and explicit unresolved locations.
- Complete JSON diagnostics, with a clearly labeled 30-check Markdown preview
  per output. Truncated evidence fails the run/comparison gate.
- `export-case`, `verify-bundle` and `reproduce` commands: package exact input and
  measured output PDFs, retain source/license metadata, verify hashes and replay
  one case with matching tool/runtime versions.
- Isolated GitHub Action `run` and `compare` modes, action-owned corpus defaults
  and practical integration examples for maintainers.
- A source- and JAR-pinned veraPDF diagnostic-capacity overlay. It changes one
  storage constant while preserving official rule evaluation and counters.
  The original installation remains intact and the overlay has a distinct
  recorded version, `veraPDF 1.30.2 + pdfua-full-checks-1`.
- All 20 original corpus fixtures and all 180 combinations remain intact.
  Matching v2 reports remain comparable; v3 diagnostics/bundles need fresh runs.

## Verification

- 69 unit/regression tests pass locally and in macOS CI; clean wheel installation
  is exercised outside the source checkout.
- The development Mac independently completed all 180 cases, capturing the same
  335,159 failed checks with complete diagnostics and zero infrastructure failures.
  Local merge/split/resave bundles and the official-versus-overlay count check passed.
- The full macOS 14 CI completed 180 cases and captured 335,159 failed checks:
  330,557 verified page anchors and 4,602 explicitly unresolved checks.
- All 180 CI cases are self-comparable, with 0 new, 5,408 persistent signals
  and 0 incomparable cases. These repeated rule/structure signals are not
  counts of distinct bugs.
- CI successfully exported, verified and replayed merge, split and resave
  bundles. A >10,000-failure output retained the official validator's conformance,
  failed-rule IDs and 21,381-failure count while recovering all detailed records.
- Local PDF/UA-2 Unicode merge/split/resave bundles replayed without new signals;
  an independently installed wheel also replayed a merge bundle successfully.
- Poppler-rendered Unicode pages before/after qpdf resave were pixel-identical
  and visually inspected.

The 180-case CI has 40 `passed` and 140 `new_pdfua_violation` outcomes, with zero
baseline, transformation or infrastructure failures. Measuring known PDF-tool
violations successfully is different from a failed benchmark execution.

## Evidence and use

- [Full macOS 14 CI](https://github.com/pengshuhao62-lang/pdf-accessibility-roundtrip-bench/actions/runs/34761273013)
- [Unit/build/Action CI](https://github.com/pengshuhao62-lang/pdf-accessibility-roundtrip-bench/actions/runs/34761404638)
- [Evidence index](../reports/README.md)
- [Diagnostic semantics and bundles](reproduction-bundles.md)
- [Full-checks validator build and upstream provenance](verapdf-full-checks.md)
- [GitHub Action integration](github-action.md)

The full CI ran on `00f10c3`; its measurement-engine source fingerprint and
validator overlay are preserved in the release. Later changes document evidence
and package the public artifacts. Local and CI contexts differ and are validated
separately, not presented as a cross-environment tool-version comparison.

Install the release wheel, configure the PDF toolchain and full-checks overlay,
then run `pdfua-bench preflight`. Use fresh output paths for every measurement
and comparison. Complete failed-check JSON is distributed as lossless `.json.gz`
assets alongside readable summaries, a self-authored example bundle and SHA-256
checksums. Review PDF content before sharing a bundle.

Automated checks cover machine-verifiable PDF/UA conformance and limited
structure signals. Human screen-reader review remains a separate activity.
