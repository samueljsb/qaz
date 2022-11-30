from __future__ import annotations

from pathlib import Path

from qaz.utils import files
from qaz.utils import shell


VENV_PATH = Path("~/opt/venv").expanduser()


def _ensure_venv() -> None:
    if VENV_PATH.exists():  # assume this means it's a virtual env
        return

    try:
        # fmt: off
        shell.run(
            "virtualenv",
            "--python", "python3.10",
            "--python", "python3.9",
            "--python", "python3.8",
            VENV_PATH,
        )
        # fmt: on
    except FileNotFoundError:
        shell.run("python3", "-m", "venv", VENV_PATH)


class Pip:
    def __init__(self, package: str, /, executables: list[str] | None = None) -> None:
        self.package = package

        if executables is not None:
            self.executables = executables
        else:
            self.executables = [package]

    def install(self) -> None:
        _ensure_venv()

        shell.run(VENV_PATH / "bin" / "python", "-m", "pip", "install", self.package)

        bin_dir = Path().home() / "bin"
        bin_dir.mkdir(exist_ok=True)
        for executable in self.executables:
            files.create_symlink(
                VENV_PATH / "bin" / executable,
                bin_dir,
            )

    def upgrade(self) -> None:
        _ensure_venv()

        shell.run(
            VENV_PATH / "bin" / "python",
            "-m",
            "pip",
            "install",
            "--upgrade",
            self.package,
        )

        bin_dir = Path().home() / "bin"
        bin_dir.mkdir(exist_ok=True)
        for executable in self.executables:
            files.create_symlink(
                VENV_PATH / "bin" / executable,
                bin_dir,
            )

    def name(self) -> str:
        return self.package

    def version(self) -> str:
        _ensure_venv()

        versions = shell.capture(VENV_PATH / "bin" / "python", "-m", "pip", "freeze")
        for line in versions.splitlines():
            package, __, version = line.partition("==")
            if package == self.package:
                return version
        else:  # not installed
            return ""
