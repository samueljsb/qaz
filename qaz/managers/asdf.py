from typing import List

from . import shell


def install_or_upgrade_plugin(plugin: str):
    shell.run("asdf update")

    if plugin not in _get_installed_plugins():
        shell.run(f"asdf plugin add {plugin}")
    else:
        shell.run(f"asdf plugin update {plugin}")

    shell.run(f"asdf install {plugin} latest")
    _set_latest(plugin)


def _get_installed_plugins() -> List[str]:
    return shell.capture("asdf plugin list").split()


def _set_latest(plugin: str):
    """
    Set the version for a plugin to the latest installed version.
    """
    versions = _get_installed_versions(plugin)
    shell.run(f"asdf global {plugin} {versions[-1]}")
    shell.run(f"asdf reshim {plugin}")


def _get_installed_versions(plugin: str) -> List[str]:
    return shell.capture(f"asdf list {plugin}").split()
