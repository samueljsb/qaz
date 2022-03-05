from __future__ import annotations

import datetime
import logging
from collections.abc import Iterable

from qaz.modules.base import Module
from qaz.modules.registry import registry


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
    # Install each module.
    for name in module_names:
        module = registry.modules[name]
        logger.info("Upgrading %s...", module.name)
        upgrade_module(module)
        logger.info("...%s upgraded.", module.name)


def upgrade_module(module: Module) -> None:
    """
    Upgrade the given module.

    Raises CannotUpgradeModule if the module cannot be upgraded for any reason.
    """
    # Check the module can be installed.
    if not module.is_installed:
        raise CannotUpgradeModule(f"Module '{module.name}' not installed.")

    # Upgrade the module.
    try:
        module.upgrade()
    except Exception as exc:
        logger.exception(exc)
        raise CannotUpgradeModule(exc)

    module.last_upgraded_at = datetime.datetime.now()
