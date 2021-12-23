from __future__ import annotations

import subprocess

from . import shell
from .base import InstallResult, Manager, UpgradeResult


class Homebrew(Manager):

    name: str  # formula or cask name

    def __init__(self, name: str) -> None:
        self.name = name

    def install(self) -> tuple[str, subprocess.CompletedProcess[str] | None]:
        # Get the current version of this formula.
        if version := self._version():
            return version, None

        # Install.
        proc = subprocess.run(
            f"brew install {self.name}",
            shell=True,
            text=True,
            capture_output=True,
        )
        proc.check_returncode()

        # Get the new version.
        version = self._version()
        return version, proc

    def upgrade(self) -> tuple[str, str, subprocess.CompletedProcess[str]]:
        # Get the current version of this formula.
        from_version = self._version()

        # Upgrade.
        proc = subprocess.run(
            f"brew upgrade {self.name}",
            shell=True,
            text=True,
            capture_output=True,
        )
        proc.check_returncode()

        # Get the new version.
        version = self._version()
        return from_version, version, proc

    def _version(self) -> str:
        proc = subprocess.run(
            f"brew list --versions {self.name}",
            shell=True,
            text=True,
            capture_output=True,
        )

        if not proc.stdout:  # not installed
            return ""
        return proc.stdout.split()[-1]


def install_or_upgrade_formula(formula: str) -> None:
    if formula.split("/")[-1] in _get_installed_formulae():
        shell.run(f"brew upgrade {formula}")
    else:
        shell.run(f"brew install {formula}")


def _get_installed_formulae() -> list[str]:
    return shell.capture("brew list --formula -1").split()


def install_or_upgrade_cask(cask: str) -> None:
    if cask in _get_installed_casks():
        shell.run(f"brew upgrade --cask {cask}")
    else:
        shell.run(f"brew cask install {cask}")


def _get_installed_casks() -> list[str]:
    return shell.capture("brew list --cask -1").split()
