"""Build a source-pinned veraPDF 1.30.2 diagnostic-capacity overlay (JDK 17+).

The original installation is never modified. One constant changes; all rule
evaluation, profiles and conformance counters remain upstream code.
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

SOURCE_URL = "https://raw.githubusercontent.com/veraPDF/veraPDF-library/v1.30.2/core/src/main/java/org/verapdf/pdfa/validation/validators/BaseValidator.java"
SOURCE_SHA = "62f6999594ab9741e737fb8d109015d2ae13787dfb4f2540a1875fe79d21e8ac"
JAR_SHA = "889075253fb9df4db5482efb8f8208fb3b4f2e00f5f7e1b1e31edf6fb4b69bb6"
ORIGINAL = b"private static final int MAX_CHECKS_NUMBER = 10_000;"
REPLACEMENT = b"private static final int MAX_CHECKS_NUMBER = Integer.MAX_VALUE;"
VERSION = "veraPDF 1.30.2 + pdfua-full-checks-1"


def digest(path):
    result = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024*1024), b""):
            result.update(chunk)
    return result.hexdigest()


def patch_source(data):
    if hashlib.sha256(data).hexdigest() != SOURCE_SHA or data.count(ORIGINAL) != 1:
        raise ValueError("Upstream source checksum or patch location differs.")
    return data.replace(ORIGINAL, REPLACEMENT)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verapdf", type=Path, required=True, help="original veraPDF 1.30.2 launcher")
    parser.add_argument("--java-home", type=Path, default=Path(os.environ.get("JAVA_HOME", "/missing-jdk")))
    parser.add_argument("--source", type=Path, help="optional previously downloaded, checksum-verified source")
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    original = args.verapdf.resolve(strict=True)
    jar = original.parent / "bin/cli-1.30.2.jar"
    if digest(jar) != JAR_SHA:
        raise ValueError("Expected the pinned official veraPDF 1.30.2 JAR.")
    javac = (args.java_home / "bin/javac").resolve(strict=True)
    data = args.source.read_bytes() if args.source else subprocess.run(
        ["curl", "--fail", "--location", "--silent", "--show-error", "--retry", "3", SOURCE_URL],
        check=True, stdout=subprocess.PIPE, timeout=120).stdout
    patched = patch_source(data)
    root = args.output_dir.resolve()
    root.mkdir(parents=True, exist_ok=False)
    source = root / "source/BaseValidator.java"
    source.parent.mkdir()
    source.write_bytes(patched)
    (root / "source/BaseValidator.upstream.java.txt").write_bytes(data)
    classes = root / "classes"
    classes.mkdir()
    subprocess.run([str(javac), "--release", "8", "-cp", str(jar), "-d", str(classes), str(source)], check=True, timeout=60)
    fingerprints = {str(jar): JAR_SHA}
    fingerprints.update({str(p): digest(p) for p in classes.rglob("*.class")})
    manifest = dict(version=VERSION, upstream_source=SOURCE_URL, source_sha256=SOURCE_SHA,
                    patched_source_sha256=hashlib.sha256(patched).hexdigest(),
                    patch=dict(before=ORIGINAL.decode(), after=REPLACEMENT.decode()), files=fingerprints)
    (root / "build.json").write_text(json.dumps(manifest, indent=2) + "\n")
    launcher = root / "verapdf"
    # JSON-quoted paths are data in this generated Python launcher, not shell code.
    launcher.write_text(f'''#!/usr/bin/env python3
import hashlib, os, sys
files = {fingerprints!r}
if sys.argv[1:] == ["--version"]:
    for path, expected in files.items():
        digest = hashlib.sha256()
        with open(path, "rb") as stream:
            for chunk in iter(lambda: stream.read(1048576), b""):
                digest.update(chunk)
        if digest.hexdigest() != expected:
            raise SystemExit("Full-checks toolchain checksum mismatch")
    print({VERSION!r})
    raise SystemExit(0)
os.environ["CLASSPATH_PREFIX"] = {str(classes)!r}
os.execv({str(original)!r}, [{str(original)!r}] + sys.argv[1:])
''')
    launcher.chmod(0o700)
    print(launcher)


if __name__ == "__main__":
    main()
