from __future__ import annotations

import logging
from collections.abc import Iterable

from qaz import settings
from qaz.modules import queries as module_queries
from qaz.modules.base import Module


logger = logging.getLogger(__name__)


class CannotUpgradeModule(Exception):
    """
    A module cannot be upgraded.
    """

    pass


def upgrade_modules(module_names: Iterable[str]) -> None:
    """
    Upgrade modules with names matching the given names.

    Raises:
        - ValueError if a module name is not recognised.
        - CannotUpgradeModule if a module cannot be upgraded for any reason.

    """
    # Retrieve the modules to be upgraded.
    try:
        modules_to_upgrade = module_queries.modules_by_name(module_names)
    except module_queries.ModuleNotFound as exc:
        raise ValueError(exc)

    # Install each module.
    for module in modules_to_upgrade:
        logger.info("Upgrading %s...", module.name)
        upgrade_module(module)
        logger.info("...%s upgraded.", module.name)


def upgrade_module(module: Module) -> None:
    """
    Upgrade the given module.

    Raises CannotUpgradeModule if the module cannot be upgraded for any reason.
    """
    # Check the module can be installed.
    if not module_queries.is_module_installed(module):
        raise CannotUpgradeModule(f"Module '{module.name}' not installed.")

    # Upgrade the module.
    try:
        module.upgrade()
    except Exception as exc:
        logger.exception(exc)
        raise CannotUpgradeModule(exc)

    settings.record_module_upgraded(module.name)
