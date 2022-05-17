from __future__ import annotations

from qaz.modules.registry import registry


def install_module(name: str) -> dict[str, str]:  # name: version
    """
    Install the given module.

    Returns the versions of tools installed by this module.

    Raises:
        - KeyError if the module name is not registered.

    """
    module = registry.modules[name.casefold()]

    # Check the module can be installed.
    if not module.is_installed:
        module.install()

    return module.versions
