from __future__ import annotations

from qaz.modules.registry import registry


def configure() -> None:
    """
    Configure all installed modules.

    This symlinks the zshrc and configuration files for all of the installed modules.
    """
    for module in registry.installed_modules:
        module.configure()


def unconfigure() -> None:
    """
    Unconfigure all installed modules.

    This removes symlinks for zshrc and configuration files for all of the installed
    modules and copies the file across in their place.
    """
    for module in registry.installed_modules:
        module.unconfigure()
