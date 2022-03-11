from __future__ import annotations

from qaz.modules.registry import registry


def install_module(name: str) -> str:
    """
    Install the given module.

    Returns the version that has been installed.

    Raises:
        - KeyError if the module name is not registered.

    """
    module = registry.modules[name.casefold()]

    # Check the module can be installed.
    if not module.is_installed:
        module.install()

    return module.version
