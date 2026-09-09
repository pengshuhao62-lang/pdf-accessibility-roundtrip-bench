# Changelog

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
