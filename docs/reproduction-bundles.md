# Evidence-linked diagnostics and single-case bundles (v3)

## Read a diagnostic

Each output validation contains `failed_checks` and `diagnostics_complete`.
The JSON keeps every failed check, while Markdown previews 30 per output and
states the full count. A rule ID and `report_pointer` identify the check inside
that output's veraPDF `validationResult` object. The pointer is relative to that
object, not to the whole batch report. Raw reports stay in the local case directory.

`page` is one-based **within the output PDF**. It is populated only when veraPDF's
zero-based `pages[N](object generation obj PDPage)` anchor matches the PDF reader's
actual page object at that index. It does not map a merged page to an original
input page. A missing, ambiguous or mismatched anchor yields `page: null` and
`location_status: unresolved`. Other `object_references` are validator-reported;
they are not all independently verified. A diagnostic identifies evidence, not a
proven root cause or an automatic fix.

Context paths keep allowlisted model names and indices. Parenthesized font names,
free text and error messages are omitted; a SHA-256 of the original context lets
the maintainer correlate it with local raw evidence. These redactions do not
alter rule counts. Completeness checks both per-rule and total failed-check
counts. Truncated coverage makes `run` exit 2 and v3 comparisons incomparable.
Unresolved locations remain legitimate complete diagnostics.

## Export and replay

Use a fresh v0.3 measurement and its unchanged case directory:

```sh
pdfua-bench export-case --input lab/run.json \
  --case FIXTURE-qpdf-resave --run-dir lab/RUN_ID \
  --output lab/case.zip --include-pdfs
pdfua-bench verify-bundle --bundle lab/case.zip
pdfua-bench reproduce --bundle lab/case.zip --output lab/reproduced.json
```

Replace `FIXTURE` and `RUN_ID` with the recorded values. Export packages the exact
input PDFs (including a merge partner), measured output PDFs, input/output hashes,
profile, case parameters, structural/rule/location evidence, tool versions,
runtime context, original source/license metadata and project attribution.
Input bytes are checked against the corpus and output bytes against the run's
fingerprints. **The ZIP contains document content:** `--include-pdfs` acknowledges
this; review permission and privacy before sharing. A sanitized JSON report is
not permission to publish its PDFs. No export or verification command uploads files.

Verification reads only fixed allowlisted data members, checks every hash and
cross-checks provenance. It rejects duplicate entries/JSON keys, extra files,
path traversal, symlinks, encrypted archives and packages over 256 MiB uncompressed
or 512 entries. ZIP checksums establish integrity, not publisher authenticity.
Treat downloaded PDFs as untrusted and run PDF tools in a disposable environment.

Reproduction checks the analyzer fingerprint, OS/version/architecture, Python,
Java, veraPDF, pinned analysis dependencies and selected processing tool version
before transforming documents. It executes a built-in adapter with argument
arrays, never commands supplied by the archive. Different versions stop with
exit 2. Exact-version replay is deliberately strict; for a tool-version experiment,
make two ordinary `run` measurements in a matched environment and use `compare-runs`.

Reproduction exit codes: 0 = comparable with no new signals; 1 = new signals;
2 = invalid, incomplete or context-mismatched evidence. Output PDF timestamps
can change, so replay compares semantic signals, not byte-for-byte output equality.
Every output filename must be new. v2 reports can still be summarized/compared
with other matching v2 reports, but require fresh v3 runs to export a bundle.
