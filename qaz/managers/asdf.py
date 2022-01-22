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
        proc = subprocess.run(
            f"asdf plugin add {self.plugin}",
            shell=True,
            text=True,
            capture_output=True,
        )
        proc.check_returncode()

        # Install the plugin.
        proc = subprocess.run(
            f"asdf install {self.plugin} latest",
            shell=True,
            text=True,
            capture_output=True,
        )
        proc.check_returncode()

        version = self._set_latest()
        return version, proc

    def upgrade(self) -> tuple[str, str, subprocess.CompletedProcess[str]]:
        # Get the current version of this formula.
        from_version = self._latest_version()

        # Install the latest version of the plugin.
        proc = subprocess.run(
            f"asdf install {self.plugin} latest",
            shell=True,
            text=True,
            capture_output=True,
        )
        proc.check_returncode()

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


def install_or_upgrade_plugin(plugin: str) -> None:
    shell.run("asdf update")

    if plugin not in _get_installed_plugins():
        shell.run(f"asdf plugin add {plugin}")
    else:
        shell.run(f"asdf plugin update {plugin}")

    shell.run(f"asdf install {plugin} latest")
    _set_latest(plugin)


def _get_installed_plugins() -> list[str]:
    return shell.capture("asdf plugin list").split()


def _set_latest(plugin: str) -> None:
    """
    Set the version for a plugin to the latest installed version.
    """
    versions = _get_installed_versions(plugin)
    shell.run(f"asdf global {plugin} {versions[-1]}")
    shell.run(f"asdf reshim {plugin}")


def _get_installed_versions(plugin: str) -> list[str]:
    versions = shell.capture(f"asdf list {plugin}").split()

    # Sort the versions.
    # This is necessary to ensure '3.10.0' is later than '3.1.0'.
    versions.sort(key=StrictVersion)

    return versions
