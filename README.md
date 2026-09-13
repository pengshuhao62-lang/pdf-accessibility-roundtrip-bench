# PDF Accessibility Roundtrip Bench

PDF Accessibility Roundtrip Bench (`pdfua-bench`) measures whether common PDF processing tools introduce machine-verifiable PDF/UA regressions.

It starts with a PDF that passes a declared PDF/UA profile, performs a controlled roundtrip operation, validates the output again, and reports new validation failures or observable structural changes.

This is an independent community benchmark. It is not affiliated with PDF Association, veraPDF, qpdf, Ghostscript, PyMuPDF, or any PDF vendor.

## What v0.3.0 covers

- PDF/UA-1 and PDF/UA-2, declared per fixture;
- qpdf, PyMuPDF, and Ghostscript;
- merge, split, and resave operations;
- 20 public or self-authored fixtures;
- Markdown and JSON reports;
- an English CLI and macOS GitHub Actions workflows;
- a manual review checklist kept separate from automated scores.
- guarded comparisons of two tool-version runs, with new, persistent and no-longer-observed signals;
- per-case failed-rule diagnostics and exact fixture reproduction commands;
- an installable wheel that includes the licensed 20-fixture corpus.
- failed-check evidence with verified output-page anchors and explicit unresolved locations;
- integrity-checked single-case PDF bundles and strictly version-matched replay;
- isolated GitHub Action run/compare modes for reusable regression gates.

See [v3 diagnostics and reproduction](docs/reproduction-bundles.md) and
[GitHub Action examples](docs/github-action.md).

The benchmark measures machine-verifiable conformance and limited structure signals. It does not claim to replace a full human screen-reader review.

## Local setup

The project targets Python 3.9 or newer. Runtime dependencies are pinned in `setup.cfg`; the tested environment uses the versions in `toolchain.lock.json`.

The benchmark tools are intentionally installed outside this repository in a user-selected external-SSD directory. The exact local path is not part of reports or public documentation.

Set `PDFUA_BENCH_TOOL_ROOT` when the isolated toolchain is not in the default location. You may also set `PDFUA_BENCH_VERAPDF`, `PDFUA_BENCH_QPDF`, and `PDFUA_BENCH_GHOSTSCRIPT` to explicit executable paths.

```bash
export PDFUA_BENCH_TOOL_ROOT=/path/to/pdf-bench-toolchain
export JAVA_HOME=/path/to/pdf-bench-toolchain/env/lib/jvm
export PATH="$JAVA_HOME/bin:/path/to/pdf-bench-toolchain/env/bin:$PATH"
```

Create or activate the project environment before use:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e .
```

## Commands

Check the local toolchain:

```bash
pdfua-bench preflight
pdfua-bench preflight --json
```

Verify corpus files and their declared baselines:

```bash
pdfua-bench verify-corpus
```

Run the full matrix:

```bash
pdfua-bench run \
  --profiles ua1,ua2 \
  --tools qpdf,pymupdf,ghostscript \
  --operations merge,split,resave \
  --output lab/runs/run.json
```

Generate a public-safe Markdown summary:

```bash
pdfua-bench summarize \
  --input lab/runs/run.json \
  --format markdown \
  --output reports/generated/run.md
```

Compare two runs made with matching corpus and analysis context:

```bash
pdfua-bench compare-runs \
  --before lab/before.json --after lab/after.json \
  --output reports/generated/comparison.md
```

Reproduce one case:

```bash
pdfua-bench run --profiles ua1 --tools qpdf --operations resave \
  --fixtures ua1-paragraph-001 --output lab/one-case.json
```

Comparison exits with `0` for no new signals, `1` for new signals, and `2` for
incomparable or invalid evidence. `run` exits with `2` for incomplete measurement;
observed PDF/UA violations in a successfully measured case are report data.
See the [comparison protocol](docs/comparison-protocol.md) for exact guards.

Every report output must have a new filename. Existing evidence is preserved.
Outside a source checkout, commands use the corpus bundled in the installed
wheel; `pdfua-bench corpus-path` prints its location. Use `--corpus` to explicitly
select another manifest.

The run creates disposable case directories under `lab/`. Original fixture files are never overwritten.

An example of the initial sanitized run is available under [`reports/`](reports/README.md).

## Result classifications

- `baseline_invalid`: the input did not pass its declared profile;
- `tool_unavailable`: a required external tool or validator is unavailable;
- `transformation_failed`: a tool or validator process failed or timed out;
- `output_unreadable`: the transformation did not produce a readable PDF;
- `new_pdfua_violation`: the output introduced new failed PDF/UA rules;
- `structure_signal_changed`: automated validation passed, but a tracked structure signal changed;
- `passed`: no automated regression was found;
- `manual_review`: a separate human review is recommended.

## Corpus and licensing

See [ATTRIBUTIONS.md](ATTRIBUTIONS.md) for the PDF/UA-1 Reference Suite license and the self-authored fixture license. The public repository contains no private documents.

## Limitations

- Local development and validation target macOS.
- Windows and Linux are not used as local or CI validation environments in this release.
- Tool behavior, PDF versions, validator versions, and fixture selection affect results.
- Automated PDF/UA checks do not establish complete screen-reader usability.
- Encrypted PDFs, digital signatures, arbitrary user documents, and automatic repair are outside the benchmark's current scope.

## Development and tests

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m compileall -q src tests tools
git diff --check
python tools/verify_macos.py --output-dir lab/mac-acceptance
```

GitHub Actions run the unit and simulation tests. A separate macOS workflow can run the full external-tool matrix manually and upload only sanitized reports.

## License

The benchmark code is available under the [MIT License](LICENSE).
