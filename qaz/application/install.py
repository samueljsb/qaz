from __future__ import annotations

import logging
from collections.abc import Iterable

from qaz import settings
from qaz.modules import queries as module_queries
from qaz.modules.base import Module


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
    # Retrieve the modules to be installed.
    try:
        modules_to_install = module_queries.modules_by_name(module_names)
    except module_queries.ModuleNotFound as exc:
        raise ValueError(exc)

    # Install each module.
    for module in modules_to_install:
        logger.info("Installing %s...", module.name)
        try:
            install_module(module)
        except ModuleAlreadyInstalled:
            logger.warning("...%s is already installed.", module.name)
        else:
            logger.info("...%s installed.", module.name)


def install_module(module: Module) -> None:
    """
    Install the given module.

    Raises:
        - ModuleAlreadyInstalled if the module is already installed.
        - CannotInstallModule if the module cannot be installed for any other reason.
    """
    # Check the module can be installed.
    if module_queries.is_module_installed(module):
        raise ModuleAlreadyInstalled

    # Install the module
    try:
        module.install()
    except Exception as exc:
        raise CannotInstallModule(exc)

    # Save installed status.
    settings.set_module_installed(module.name)
