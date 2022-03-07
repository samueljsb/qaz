from __future__ import annotations

import datetime
import logging

from qaz.modules.registry import registry


logger = logging.getLogger(__name__)


class CannotUpgradeModule(Exception):
    """
    A module cannot be upgraded.
    """

    pass


def upgrade_module(name: str) -> None:
    """
    Upgrade the given module.

    Raises:
        - KeyError if the module name is not registered.
        - CannotUpgradeModule if the module cannot be upgraded for any reason.

    """
    module = registry.modules[name.casefold()]
    logger.info("Upgrading %s...", module.name)

    # Check the module can be upgraded.
    if not module.is_installed:
        logger.warning("...%s is not installed.", module.name)
        raise CannotUpgradeModule

    # Upgrade the module.
    try:
        module.upgrade()
    except Exception as exc:
        logger.exception("... error upgrading %s.", module.name)
        raise CannotUpgradeModule(exc) from exc

    module.last_upgraded_at = datetime.datetime.now()

    logger.info("...%s upgraded.", module.name)
