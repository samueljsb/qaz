from typing import List

from qaz.utils import capture, error, run


def add_plugin(name: str) -> None:
    """Install an asdf plugin.

    Args:
        name: The name of the plugin to install.

    """
    run("asdf update")
    run(f"asdf plugin add {name}")


def install(name: str, version: str = "latest") -> None:
    """Install a specific version of a package.

    Args:
        name: The name of the plugin to install a package from.
        version: The version to install.

    """
    run("asdf update")
    run(f"asdf install {name} {version}")


def update_plugin(name: str) -> None:
    """Upgrade an asdf plugin.

    Args:
        name: The name of the plugin to upgrade.

    """
    run("asdf update")
    run(f"asdf plugin update {name}")


def installed_plugins() -> List[str]:
    """Get a list of plugins installed with asdf.

    Output from asdf list shows plugins and versions installed. The version numbers are
    indented, so can be removed from the list by looking for whitespace.
    """
    asdf_list = capture("asdf list").split("\n")
    return [name for name in asdf_list if not name.startswith(" ")]


def installed_versions(name: str) -> List[str]:
    """Get a list of the package version installed for a plugin.

    Args:
        name: The name of the plugin.

    """
    return capture(f"asdf list {name}").split()


def set_latest(name: str, env: str = "global") -> None:
    """Set the version for a package to the latest installed version.

    Args:
        name: The package to set the version for.
        env: The environment to set the version for (global|local|shell).

    """
    versions = installed_versions(name)
    if not versions:
        error(f"Cannot set the {env} version for {name}: no versions are installed.")
    latest = versions[-1]
    run(f"asdf {env} {name} {latest}")


def install_or_upgrade(name: str) -> None:
    """Install or upgrade a plugin.

    If the given plugin is not installed, install it, install the latest package, and
    set the global version. If the plugin is installed, update it and install the latest
    package.

    Args:
        name: The name of the plugin to install or update.

    """
    if name in installed_plugins():
        update_plugin(name)
    else:
        add_plugin(name)

    install(name)
    set_latest(name)
