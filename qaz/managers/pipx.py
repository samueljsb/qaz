from __future__ import annotations

import json
import subprocess

from . import shell
from .base import Manager


class PipX(Manager):
    package: str

    def __init__(self, package: str) -> None:
        self.package = package

    def install(self) -> tuple[str, subprocess.CompletedProcess[str] | None]:
        # Install the package.
        proc = subprocess.run(
            f"pipx install {self.package}",
            shell=True,
            text=True,
            capture_output=True,
        )
        if proc.returncode not in (0, 1):  # pipx returns 1 on success
            raise subprocess.CalledProcessError(
                returncode=proc.returncode,
                cmd=f"pipx install {self.package}",
                output=proc.stdout,
                stderr=proc.stderr,
            )

        return self._version(), proc

    def upgrade(self) -> tuple[str, str, subprocess.CompletedProcess[str]]:
        from_version = self._version()

        # Update the package.
        proc = subprocess.run(
            f"pipx upgrade {self.package}",
            shell=True,
            text=True,
            capture_output=True,
        )
        if proc.returncode not in (0, 1):  # pipx returns 1 on success
            raise subprocess.CalledProcessError(
                returncode=proc.returncode,
                cmd=f"pipx upgrade {self.package}",
                output=proc.stdout,
                stderr=proc.stderr,
            )

        return from_version, self._version(), proc

    def _version(self) -> str:
        data = json.loads(shell.capture("pipx list --json"))
        return data["venvs"][self.package]["metadata"]["main_package"][
            "package_version"
        ]
