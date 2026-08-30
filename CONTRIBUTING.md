# Contributing

Contributions should improve reproducible PDF/UA roundtrip testing without expanding the project into a general PDF editor or validator.

## Requirements

- Python 3.9 or newer;
- standard-library tests plus the pinned project dependencies;
- no private PDFs or unclear-license files;
- a clear fixture source and license;
- deterministic output;
- no automatic modification of input files;
- no shell interpolation for external commands.

## Adding a fixture

Add the fixture to the manifest with its profile, source, license, expected page count, SHA-256, and merge partner. Validate the baseline with the matching veraPDF profile before using it in the matrix.

## Adding a tool adapter

Implement merge, split, and resave behavior behind the common adapter interface. Include version detection, bounded execution, output validation, and simulation tests. Do not silently replace a missing tool with another implementation.

## Tests

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m compileall -q src tests tools
git diff --check
```

Keep generated reports and case directories out of commits. Do not submit private documents, credentials, or unredacted logs.
