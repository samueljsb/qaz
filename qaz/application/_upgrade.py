from __future__ import annotations

from qaz.modules.registry import registry


class NotInstalled(Exception):
    pass


def upgrade_module(name: str) -> tuple[str, str]:
    """
    Upgrade the given module.

    Raises:
        - KeyError if the module name is not registered.
        - NotInstalled if the module is not installed.

    """
    module = registry.modules[name.casefold()]

    # Check the module can be upgraded.
    if not module.is_installed:
        raise NotInstalled

    from_version = module.version

    module.upgrade()

    return from_version, module.version
