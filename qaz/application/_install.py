from __future__ import annotations

from qaz.modules.registry import registry


class ModuleAlreadyInstalled(Exception):
    """
    A module cannot be installed because it is already installed.
    """

    pass


def install_module(name: str) -> str:
    """
    Install the given module.

    Returns the version that has been installed.

    Raises:
        - KeyError if the module name is not registered.
        - ModuleAlreadyInstalled if the module is already installed.

    """
    module = registry.modules[name.casefold()]

    # Check the module can be installed.
    if module.is_installed:
        raise ModuleAlreadyInstalled

    # Install the module.
    module.install()

    return module.version
