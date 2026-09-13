# Changelog

## [0.3.0] - 2026-09-13

- Capture all failed checks with rule pointers, sanitized model paths and PDF object references.
- Verify output-page anchors against actual page objects; leave unverified locations unresolved.
- Reject incomplete diagnostic coverage in v3 comparisons and run exit status.
- Record output hashes and export bounded, integrity-checked single-case PDF bundles.
- Replay bundles only with matching analyzer, environment, dependencies and processing tool.
- Add isolated GitHub Action run/compare modes, bundled-corpus defaults and CI integration examples.
- Preserve all 20 fixtures, the complete 180-case matrix and v2 comparison support.
- Build a source- and JAR-pinned veraPDF capacity overlay to avoid its internal
  10,000-record truncation; verify unchanged official rule results and counts.

## [0.2.0] - 2026-09-09

- Added provenance-guarded comparisons of two recorded runs and explicit CLI exit codes.
- Added failed-rule and structural-change diagnostics with exact fixture selection.
- Added source/analyzer, input, runtime and tool-version comparison context.
- Verify corpus integrity before every matrix and merge-partner baselines before transformation.
- Fail closed when structural inspection exceeds its traversal budget or cannot read objects.
- Fixed relative output paths passed to external tools and honored standard `JAVA_HOME` in CI.
- Preserve existing report files instead of overwriting them.
- Bundle the licensed corpus and attribution in installable wheels.
- Added reproducible macOS acceptance and expanded regression tests.

## [0.1.0] - 2026-08-30

Initial public release of the machine-verifiable PDF/UA roundtrip benchmark.

- Added PDF/UA-1 and PDF/UA-2 fixture profiles.
- Added qpdf, PyMuPDF, and Ghostscript adapters.
- Added merge, split, and resave operations.
- Added veraPDF JSON validation and limited structural snapshots.
- Added Markdown and JSON run reports.
- Added safe process timeouts and isolated output directories.
- Added public corpus attribution, privacy, security, and manual review documentation.
