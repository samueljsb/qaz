from __future__ import annotations

import subprocess

from . import shell
from .base import Manager


class Homebrew(Manager):

    name: str  # formula or cask name

    def __init__(self, name: str) -> None:
        self.name = name

    def install(self) -> tuple[str, subprocess.CompletedProcess[str] | None]:
        # Get the current version of this formula.
        if version := self._version():
            return version, None

        # Install.
        proc = shell.run(f"brew install {self.name}")

        # Get the new version.
        version = self._version()
        return version, proc

    def upgrade(self) -> tuple[str, str, subprocess.CompletedProcess[str]]:
        # Get the current version of this formula.
        from_version = self._version()

        # Upgrade.
        proc = shell.run(f"brew upgrade {self.name}")

        # Get the new version.
        version = self._version()
        return from_version, version, proc

    def _version(self) -> str:
        versions = shell.capture(f"brew list --versions {self.name}")
        if not versions:  # not installed
            return ""
        return versions.split()[-1]
