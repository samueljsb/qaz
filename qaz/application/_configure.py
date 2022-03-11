from qaz.modules.registry import registry


def configure() -> None:
    """
    Configure all installed modules.

    This symlinks the zshrc and configuration files for all of the installed modules.
    """
    for module in registry.installed_modules:
        module.configure()
