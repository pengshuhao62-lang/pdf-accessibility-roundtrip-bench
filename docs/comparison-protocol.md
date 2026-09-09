# Run comparison protocol v2

`compare-runs` compares recorded evidence for the same fixture, profile, tool and
operation. Reports are parsed as data; reproduction commands are generated from
validated identifiers and never executed by the comparison command.

## Required context

Both reports must use schema `0.2` and `pdfua-roundtrip-v2`. Comparison requires:

- identical input IDs, SHA-256 checksums and declared page counts, including the
  second input of a merge;
- identical operation parameters and adapter defaults;
- identical analyzer source fingerprint, veraPDF version, Java version, OS
  version, CPU architecture and Python version;
- identical pypdf and ReportLab versions;
- a recorded version of the selected processing tool;
- complete, unique case identities and the declared expected case count.

The selected processing tool's version may differ: that is the variable under
test. Other context changes produce `not_comparable`, even when they appear
harmless. Legacy v0.1 reports remain readable with `summarize`, but need fresh
measurements for version comparisons. The analyzer fingerprint guards code
identity, not authenticity of a downloaded report.

## Evidence and signals

Each comparable case requires a compliant readable baseline, completed
transformation, complete readable output validations and structural snapshots,
and a recorded classification consistent with that evidence. A noncompliant
output without failed-rule identifiers is insufficient for a rule comparison.

Signals are either `output-N:pdfua:RULE` or
`structure:FIELD:BEFORE->AFTER`. Output numbers identify deterministic adapter
output order; they do not infer an original page, paragraph or PDF object.
Structural totals aggregate output files, with all-output agreement for boolean
fields. The fields are page count, structure tree presence, marked-PDF flag,
alternative-text count, role-map count, document-language presence, document-title
presence and outline count.

- `new`: observed only in the later valid run.
- `persistent`: observed in both valid runs.
- `no_longer_observed`: observed only in the earlier valid run.
- `not_comparable`: missing, failed, inconsistent or mismatched evidence.

These are set differences over measured signals. They are not proof of universal
accessibility or a causal explanation of a tool change. The benchmark does not
perform manual screen-reader review.

## Exit codes

| Command | 0 | 1 | 2 |
| --- | --- | --- | --- |
| `compare-runs` | No new signals in comparable cases | New signals | Incomparable evidence or invalid input |
| `run` | Completed measurement, including observed PDF/UA violations | — | Incomplete measurement or invalid input |
| `verify-corpus` | All baselines and integrity checks pass | Corpus validation failure | Invalid input/tool setup error |

For comparison, code 2 takes priority over code 1. CI should preserve the report
even on a nonzero comparison exit. A benchmark that successfully measures a
known PDF-tool regression is different from a failed benchmark execution.

All report-writing commands require a new output filename and refuse existing
files and symlinks. Rerun with a new path rather than replacing prior evidence.

## Reproducing one case

Install the recorded tool versions, retain the matching corpus, then use the
command emitted for that case. `--fixtures` selects exact fixture IDs while
retaining validation of a merge partner. The runner verifies corpus integrity
before invoking tools and verifies copied input hashes before transformation.

Generated JSON omits raw absolute paths and process logs by default. Keep raw
case files local; publish the sanitized JSON and Markdown summaries.
