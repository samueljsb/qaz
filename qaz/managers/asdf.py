from typing import List

from qaz.utils import capture, run


def install_or_upgrade_plugin(plugin: str):
    run("asdf update")

    if plugin not in _get_installed_plugins():
        run(f"asdf plugin add {plugin}")
    else:
        run(f"asdf plugin update {plugin}")

    run(f"asdf install {plugin} latest")
    _set_latest(plugin)


def _get_installed_plugins() -> List[str]:
    asdf_list = capture("asdf list").split("\n")
    return [name for name in asdf_list if not name.startswith(" ")]


def _set_latest(plugin: str):
    """
    Set the version for a plugin to the latest installed version.
    """
    versions = _get_installed_versions(plugin)
    run(f"asdf global {plugin} {versions[-1]}")
    run(f"asdf reshim {plugin}")


def _get_installed_versions(plugin: str) -> List[str]:
    return capture(f"asdf list {plugin}").split()
