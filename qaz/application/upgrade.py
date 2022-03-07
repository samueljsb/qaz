from __future__ import annotations

from qaz.modules.registry import registry


class CannotUpgradeModule(Exception):
    """
    A module cannot be upgraded.
    """

    pass


class NotInstalled(CannotUpgradeModule):
    pass


def upgrade_module(name: str) -> tuple[str, str]:
    """
    Upgrade the given module.

    Raises:
        - KeyError if the module name is not registered.
        - CannotUpgradeModule if the module cannot be upgraded for any reason.

    """
    module = registry.modules[name.casefold()]

    # Check the module can be upgraded.
    if not module.is_installed:
        raise CannotUpgradeModule

    from_version = module.version

    # Upgrade the module.
    try:
        module.upgrade()
    except Exception as exc:
        raise CannotUpgradeModule(exc) from exc

    return from_version, module.version
