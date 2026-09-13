# GitHub Action integration

The composite action installs the project in its own temporary Python environment.
Call `actions/setup-python` first (Python 3.9+). Inputs become quoted environment
variables/argument arrays, not shell source. The default corpus comes from the
action checkout, so a consuming repository does not need its own corpus copy.

## Compare saved runs

This mode needs Python but no qpdf, Ghostscript, Java or veraPDF installation.
The reports must satisfy the [comparison protocol](comparison-protocol.md),
including matching environment and analysis versions. The processing tool version
may differ. Use the release tag below, or pin its full commit SHA for immutability.

```yaml
steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-python@v5
    with:
      python-version: '3.9'
  - uses: pengshuhao62-lang/pdf-accessibility-roundtrip-bench@v0.3.0
    with:
      mode: compare
      before: evidence/reference.json
      after: evidence/candidate.json
      output: artifacts/comparison.json
  - uses: actions/upload-artifact@v4
    if: always()
    with:
      name: pdfua-comparison
      path: artifacts/comparison.json
```

The comparison step fails for new signals (exit 1) or incomparable evidence
(exit 2). It writes the comparison report for both outcomes. Malformed input
fails before a report can be produced. `output` must be a fresh path.

## Measure PDFs

Configure the local PDF tools and `JAVA_HOME` as in the README, then use:

```yaml
- uses: pengshuhao62-lang/pdf-accessibility-roundtrip-bench@v0.3.0
  with:
    mode: run
    profiles: ua1,ua2
    tools: qpdf,pymupdf,ghostscript
    operations: merge,split,resave
    output: artifacts/run.json
```

Optional `corpus` overrides the bundled manifest; `fixtures` selects exact IDs.
Run mode measures violations rather than treating every known violation as a CI
execution failure. Use compare mode afterward to gate newly observed regressions.
Incomplete execution/diagnostic coverage fails immediately. The repository's
`Full macOS benchmark` workflow exercises this mode with all 180 cases, baseline
verification and bundle replay. Unit CI also exercises compare mode on macOS.

Only upload reports or approved public-fixture bundles. Keep raw validator logs
and private PDFs out of workflow artifacts.
