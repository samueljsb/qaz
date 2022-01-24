from __future__ import annotations

from distutils.version import StrictVersion

from . import shell


def install_or_upgrade_plugin(plugin: str) -> None:
    shell.run("asdf update")

    if plugin not in _installed_plugins():
        shell.run(f"asdf plugin add {plugin}")
    else:
        shell.run(f"asdf plugin update {plugin}")

    shell.run(f"asdf install {plugin} latest")
    _set_latest(plugin)


def _installed_plugins() -> list[str]:
    return shell.capture("asdf plugin list").split()


def _set_latest(plugin: str) -> None:
    """
    Set the version for a plugin to the latest installed version.
    """
    versions = _installed_versions(plugin)
    shell.run(f"asdf global {plugin} {versions[-1]}")
    shell.run(f"asdf reshim {plugin}")


def _installed_versions(plugin: str) -> list[str]:
    versions = shell.capture(f"asdf list {plugin}").split()

    # Sort the versions.
    # This is necessary to ensure '3.10.0' is later than '3.1.0'.
    versions.sort(key=StrictVersion)

    return versions
