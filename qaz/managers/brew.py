from typing import List

from qaz.utils import capture, run


def install(name: str) -> None:
    """Install a formula.

    Args:
        name: The name of the formula to install.

    """
    run(f"brew install {name}")


def install_cask(name: str) -> None:
    """Install a cask.

    Args:
        name: The name of the cask to install.

    """
    run(f"brew cask install {name}")


def upgrade(name: str) -> None:
    """Upgrade a formula.

    Args:
        name: The name of the formula to upgrade.

    """
    run(f"brew upgrade {name}")


def upgrade_cask(name: str) -> None:
    """Upgrade a cask.

    Args:
        name: The name of the cask to upgrade.

    """
    run(f"brew cask upgrade {name}")


def installed() -> List[str]:
    """Get a list of installed formulae."""
    return capture("brew list -1").split()


def installed_casks() -> List[str]:
    """Get a list of installed casks."""
    return capture("brew cask list -1").split()


def install_or_upgrade(name: str) -> None:
    """Install or upgrade a formula.

    If the given formula is not installed, install it. If the formula is
    installed, update it.

    Args:
        name: The name of the formula to install or update.

    """
    if name.split("/")[-1] in installed():
        return upgrade(name)
    else:
        return install(name)


def install_or_upgrade_cask(name: str) -> None:
    """Install or upgrade a cask.

    If the given cask is not installed, install it. If the cask is
    installed, update it.

    Args:
        name: The name of the cask to install or update.

    """
    if name in installed_casks():
        return upgrade_cask(name)
    else:
        return install_cask(name)
