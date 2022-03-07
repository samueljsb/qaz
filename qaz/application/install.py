from __future__ import annotations

import logging
from collections.abc import Iterable

from qaz.modules.registry import registry


logger = logging.getLogger(__name__)


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


def install_modules(module_names: Iterable[str]) -> None:
    """
    Install modules with names matching the given names.

    Raises:
        - ValueError if a module name is not recognised.
        - CannotInstallModule if a module cannot be installed.

    """
    # Install each module.
    for name in module_names:
        install_module(name)


def install_module(name: str) -> None:
    """
    Install the given module.

    Raises:
        - KeyError if the module name is not registered.
        - ModuleAlreadyInstalled if the module is already installed.
        - CannotInstallModule if the module cannot be installed for any other reason.

    """
    module = registry.modules[name.casefold()]
    logger.info("Installing %s...", module.name)

    # Check the module can be installed.
    if module.is_installed:
        logger.warning("...%s is already installed.", module.name)
        raise ModuleAlreadyInstalled

    # Install the module.
    try:
        module.install()
    except Exception as exc:
        logger.exception("... error installing %s.", module.name)
        raise CannotInstallModule(exc) from exc

    # Save installed status.
    module.is_installed = True

    logger.info("...%s installed.", module.name)
