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


def install_or_upgrade_package(package: str) -> None:
    if package not in _get_installed_packages():
        shell.run(f"npm install --global {package}")
    else:
        shell.run(f"npm update --global {package}")


def _get_installed_packages() -> list[str]:
    output = shell.capture("npm list --global --json")
    data = json.loads(output)
    return [k for k in data.get("dependencies", {})]
