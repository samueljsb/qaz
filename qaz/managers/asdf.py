from __future__ import annotations

import subprocess
from distutils.version import StrictVersion

from . import shell
from .base import Manager


class ASDF(Manager):

    plugin: str  # formula or cask name

    def __init__(self, plugin: str) -> None:
        self.plugin = plugin

    def install(self) -> tuple[str, subprocess.CompletedProcess[str] | None]:
        shell.run("asdf update")

        # Add the plugin.
        shell.run(f"asdf plugin add {self.plugin}")

        # Install the plugin.
        proc = shell.run(f"asdf install {self.plugin} latest")

        version = self._set_latest()
        return version, proc

    def upgrade(self) -> tuple[str, str, subprocess.CompletedProcess[str]]:
        # Get the current version of this formula.
        from_version = self._latest_version()

        # Install the latest version of the plugin.
        proc = shell.run(f"asdf install {self.plugin} latest")

        version = self._set_latest()
        return from_version, version, proc

    def _set_latest(self) -> str:
        version = self._latest_version()
        shell.run(f"asdf global {self.plugin} {version}")
        shell.run(f"asdf reshim {self.plugin}")
        return version

    def _latest_version(self) -> str:
        versions = shell.capture(f"asdf list {self.plugin}").split()
        versions.sort(key=StrictVersion)
        return versions[-1]
