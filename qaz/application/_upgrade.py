from __future__ import annotations

from qaz.modules.registry import registry


class NotInstalled(Exception):
    pass


def upgrade_module(name: str) -> dict[str, tuple[str, str]]:
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

    from_versions = module.versions

    module.upgrade()
    to_versions = module.versions

    upgrade_versions = {
        name_: (from_versions.get(name_, ""), to_version)
        for name_, to_version in to_versions.items()
    }

    return upgrade_versions
