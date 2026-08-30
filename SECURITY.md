# Security policy

## Safe defaults

The benchmark is read-only with respect to its input corpus:

- input PDFs are copied to isolated temporary case directories;
- output paths are checked to remain inside the case directory;
- external commands use argument arrays and `shell=False`;
- repository or PDF-provided scripts are not executed;
- each external process has a timeout and its own process group;
- a timeout terminates only that process group;
- no private documents are included in the public corpus;
- raw logs remain local and are excluded from Git.

The project deliberately does not ship exploit payloads or attempt to repair arbitrary PDFs.

## Reporting a vulnerability

Do not include private PDFs, credentials, API keys, personal paths, or full raw logs in a public issue. Report a minimal synthetic reproduction and the affected version through GitHub's private security reporting channel when available.
