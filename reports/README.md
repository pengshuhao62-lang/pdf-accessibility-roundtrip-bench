# Example reports

The `example-v0.1.0.md` and `example-v0.1.0.json` files are sanitized summaries from the initial local validation run. They contain fixture IDs, tool versions, classifications, and limited structural signals; raw validator logs and temporary case files are intentionally excluded.

## v0.2.0 measured evidence

- [Current local run](example-v0.2.0-current.md) and [JSON](example-v0.2.0-current.json): 180 cases on macOS 15.5 arm64, Python 3.9.6, qpdf 12.3.2, PyMuPDF 1.26.5, Ghostscript 10.07.1 and veraPDF 1.30.2.
- [Reference run JSON](example-v0.2.0-reference.json): the same 180-case matrix and context, with PyMuPDF 1.26.4 in an independent virtual environment.
- [Version comparison](comparison-v0.2.0.md) and [JSON](comparison-v0.2.0.json): 180 comparable cases; 0 new, 5,408 persistent and 0 no-longer-observed signals. Sixty cases exercise the changed PyMuPDF version; the other 120 are unchanged-tool controls.
- [macOS 14 CI run](ci-macos14-v0.2.0.json) and [self-comparison](ci-self-comparison-v0.2.0.json): an independently measured 180-case matrix. CI used qpdf 12.4.1; the remaining processing/validator versions match the current local run.

Both local runs and the CI run measured 40 `passed` and 140
`new_pdfua_violation` cases, with zero baseline or infrastructure failures.
The 5,408 comparison signals include repeated per-output failed rules and
structural changes; they are not 5,408 distinct bugs. No version-change signal
was found between the two local runs on this corpus. This is a measured result,
not a universal claim about either PyMuPDF version.

The CI report has different OS/runtime context and is not used as the reference
for a local tool-version comparison. Its self-comparison was also checked with
the final comparison guards. See [release validation](../docs/release-v0.2.0.md).
