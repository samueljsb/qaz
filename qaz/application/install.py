from __future__ import annotations

from qaz.modules.registry import registry


class CannotInstallModule(Exception):
    """
    A module cannot be installed.
    """

    pass


class ModuleAlreadyInstalled(CannotInstallModule):
    """
    A module cannot be installed because it is already installed.
    """

    pass


def install_module(name: str) -> None:
    """
    Install the given module.

    Raises:
        - KeyError if the module name is not registered.
        - ModuleAlreadyInstalled if the module is already installed.
        - CannotInstallModule if the module cannot be installed for any other reason.

    """
    module = registry.modules[name.casefold()]

    # Check the module can be installed.
    if module.is_installed:
        raise ModuleAlreadyInstalled

    # Install the module.
    try:
        module.install()
    except Exception as exc:
        raise CannotInstallModule(exc) from exc
