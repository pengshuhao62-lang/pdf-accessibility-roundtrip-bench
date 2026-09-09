# v0.2.0 — Reproducible PDF accessibility regression comparisons

## What's new

- Compare recorded tool-version runs using fixture hashes, merge-input context,
  analyzer identity, validator/runtime versions and consistent case evidence.
- Separate new, persistent, no-longer-observed and incomparable signals.
- Inspect failed PDF/UA rules and structural changes alongside exact case
  reproduction commands and fixture selection.
- Install a wheel containing all 20 licensed fixtures and their attribution.
- Preserve report files, check corpus integrity before every run, and validate
  both merge inputs before transformation.
- Correct relative output handling, support standard `JAVA_HOME` in CI, and
  fail closed when structural inspection cannot finish reliably.

## Validation

- 42 unit and regression tests pass on the development Mac and in CI.
- CI tests and clean wheel installation pass on macOS 14/Python 3.9 and
  macOS-latest/Python 3.13.
- Two independent local environments completed all 180 cases each on macOS 15.5
  arm64, with PyMuPDF 1.26.4 and 1.26.5 respectively.
- A full macOS 14 CI matrix completed 180 cases, including corpus baseline
  verification and self-comparison.
- Each measured matrix has 40 passed cases, 140 cases with measured PDF/UA
  violations, and zero baseline/infrastructure failures.
- Local version comparison: 180 comparable cases, 0 new signals, 5,408 persistent
  signals, 0 no-longer-observed signals, and 0 incomparable cases.
- A clean installed wheel found and verified all 20 bundled fixtures outside the
  source checkout and completed a real PDF/UA-2 Unicode resave case.
- A sampled invoice's original and qpdf-resaved rendering were pixel-identical.

The unchanged-tool controls are included in the 180-case local comparison; 60
cases exercise the changed PyMuPDF version. Automated checks measure PDF/UA
conformance and limited structural signals, not complete screen-reader usability.

## Evidence

- [42-test CI](https://github.com/pengshuhao62-lang/pdf-accessibility-roundtrip-bench/actions/runs/34306757960)
- [Full macOS 14 matrix](https://github.com/pengshuhao62-lang/pdf-accessibility-roundtrip-bench/actions/runs/34306414928)
- [Public run and comparison reports](https://github.com/pengshuhao62-lang/pdf-accessibility-roundtrip-bench/blob/v0.2.0/reports/README.md)
- [Comparison protocol and exit codes](https://github.com/pengshuhao62-lang/pdf-accessibility-roundtrip-bench/blob/v0.2.0/docs/comparison-protocol.md)

The full CI matrix ran on `06613c0`; its measurement engine fingerprint matches
both final local runs. The downloaded CI evidence was rechecked using the final
baseline-profile and page-evidence comparison guards from `6c48004`.

## Use

Install the wheel or source distribution from the Release, configure qpdf,
Ghostscript, veraPDF and Java as described in the README, then run:

```sh
pdfua-bench preflight
pdfua-bench run --output lab/current.json
pdfua-bench compare-runs --before lab/reference.json --after lab/current.json --output lab/comparison.md
```

Each output needs a new filename. Legacy v0.1 reports can still be summarized;
fresh schema-0.2 measurements are required for guarded comparisons.
