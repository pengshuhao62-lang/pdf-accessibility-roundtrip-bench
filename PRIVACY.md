# Privacy

PDF Accessibility Roundtrip Bench is designed to run locally or in the user's own GitHub Actions environment.

## Data handling

- The project has no backend, account system, telemetry, or analytics.
- The benchmark does not upload PDFs to the maintainer.
- The public corpus contains only authorized or self-authored files.
- v0.1.0 runs the declared public corpus and does not accept arbitrary private PDFs through the public workflow.
- Original fixtures are copied to disposable case directories and are never overwritten.
- Reports contain fixture IDs, tool versions, validation outcomes, and limited structural counts.
- Reports do not intentionally contain PDF body text, personal paths, usernames, credentials, or secrets.

## GitHub Actions

The public CI workflow runs tests and simulated adapters. The optional full benchmark workflow runs on macOS, uses public fixtures, and uploads sanitized Markdown/JSON summaries only. It does not upload raw validator logs or temporary case directories.

## Third-party tools

V3 `export-case --include-pdfs` creates a local ZIP containing original and output
PDF content plus source/license metadata. Review each document's sharing rights
before publishing a bundle. Diagnostic reports retain sanitized model paths and
context hashes, not raw error messages or parenthesized font names. Raw validator
reports remain local. See [bundle handling](docs/reproduction-bundles.md).

veraPDF, qpdf, Ghostscript, PyMuPDF, pypdf, and reportlab are run as local dependencies. Their own licenses and behavior remain separate from this project.
