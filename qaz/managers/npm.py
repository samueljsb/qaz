from __future__ import annotations

import json
import subprocess

from . import shell
from .base import Manager


class NPM(Manager):
    package: str

    def __init__(self, package: str) -> None:
        self.package = package

    def install(self) -> tuple[str, subprocess.CompletedProcess[str] | None]:
        # Install the package.
        proc = subprocess.run(
            f"npm install --global {self.package}",
            shell=True,
            text=True,
            capture_output=True,
        )
        proc.check_returncode()

        return self._version(), proc

    def upgrade(self) -> tuple[str, str, subprocess.CompletedProcess[str]]:
        from_version = self._version()

        # Update the package.
        proc = subprocess.run(
            f"npm update --global {self.package}",
            shell=True,
            text=True,
            capture_output=True,
        )
        proc.check_returncode()

        return from_version, self._version(), proc

    def _version(self) -> str:
        data = json.loads(shell.capture("npm list --global --json"))
        return data["dependencies"][self.package]["version"]
