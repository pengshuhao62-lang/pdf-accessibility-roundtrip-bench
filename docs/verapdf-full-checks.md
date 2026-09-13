# Full diagnostic capture for veraPDF 1.30.2

## Why an overlay is necessary

The [official CLI](https://docs.verapdf.org/cli/validation/) supports
`--maxfailures -1 --maxfailuresdisplayed -1`. However,
[BaseValidator in v1.30.2](https://github.com/veraPDF/veraPDF-library/blob/v1.30.2/core/src/main/java/org/verapdf/pdfa/validation/validators/BaseValidator.java)
also has a hard-coded `MAX_CHECKS_NUMBER = 10_000` storage ceiling. Validation
continues counting failures beyond it while detailed records are discarded.
The first v3 full CI correctly rejected 10 truncated output validations; all 180
transformations had finished. Reducing the corpus or accepting partial evidence
would hide this problem.

The reproducible overlay changes exactly one source constant to
`Integer.MAX_VALUE`, compiles that class against the original JAR, and uses the
official launcher's `CLASSPATH_PREFIX` support to load it. Rule expressions,
profiles, check evaluation and conformance counters are unchanged. It preserves
the original installation and records a distinct validator version:
`veraPDF 1.30.2 + pdfua-full-checks-1`.

## Build on macOS

From the v0.3.0 source checkout or extracted source distribution, with Python and
JDK 17+ installed:

```sh
python3 tools/build_verapdf_full_checks.py \
  --verapdf /path/to/original-verapdf/verapdf \
  --java-home /path/to/jdk \
  --output-dir /path/to/new-verapdf-full-checks
export PDFUA_BENCH_VERAPDF=/path/to/new-verapdf-full-checks/verapdf
pdfua-bench preflight
```

The output directory must not exist. The build checks SHA-256 for both the
official 1.30.2 JAR and upstream source before compilation. It needs no Maven or
extra Java dependencies. It downloads one pinned upstream Java source with curl;
standard proxy environment variables are honored. For offline builds, supply
`--source /path/to/BaseValidator.java` with the identical source bytes. All
sources, classes, the launcher and `build.json` remain in the chosen directory.
The launcher's `--version` verifies the compiled class and JAR checksums.

Use the resulting launcher with an installed wheel, the source CLI or the GitHub
Action. The repository's full CI builds it automatically. Reproduction bundles
record the distinct validator version, so original and overlaid runs are never
silently compared as the same environment. A stock validator remains usable for
small runs; incomplete capture still makes v3 runs and comparisons fail closed.

More recorded diagnostics cost memory and disk space. Existing process timeouts
and completeness checks remain active. The capacity change is not an unlimited
resource guarantee. Full public evidence is distributed as lossless gzip.

## Verification and licensing

Acceptance reruns a >10,000-failure output through the **unmodified** official
validator and requires identical conformance, failed-rule IDs and failure count.
The overlaid result must include that entire count of detailed records. Separate
tests guard the source hash and the one-constant patch. Both original and patched
source copies remain available beside the locally compiled class.

The upstream source retains its veraPDF copyright and GPLv3+/MPLv2+ notices.
This workflow uses the MPLv2+ option; see
[the upstream MPL license](https://github.com/veraPDF/veraPDF-library/blob/v1.30.2/LICENSE.MPL).
The project does not redistribute a modified veraPDF JAR or claim this overlay
is an official veraPDF release.
