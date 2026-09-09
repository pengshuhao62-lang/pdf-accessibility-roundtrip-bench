"""Bundle the licensed corpus in wheels without duplicating source fixtures."""
from pathlib import Path
from shutil import copy2
from setuptools import setup
from setuptools.command.build_py import build_py


class BuildWithCorpus(build_py):
    def run(self):
        super().run()
        source = Path(__file__).parent
        target = Path(self.build_lib) / "pdfua_bench" / "data"
        for path in (source / "corpus").rglob("*"):
            if path.is_file():
                destination = target / path.relative_to(source)
                destination.parent.mkdir(parents=True, exist_ok=True)
                copy2(path, destination)
        for name in ("ATTRIBUTIONS.md", "LICENSE"):
            copy2(source / name, target / name)


setup(cmdclass={"build_py": BuildWithCorpus})
