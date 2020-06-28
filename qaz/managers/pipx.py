import re
from typing import List

from qaz.utils import capture, run


def install(name: str) -> None:
    """Install a package.

    Args:
        name: The name of the package to install.

    """
    run(f"pipx install {name}")


def upgrade(name: str) -> None:
    """Upgrade a package.

    Args:
        name: The name of the package to upgrade.

    """
    run(f"pipx upgrade {name}", allow_fail=True)  # pipx returns 1 on success


def upgrade_all(packages: List[str] = None) -> None:
    """Upgrade all packages.

    Will install new `packages` if they are not yet installed.

    Args:
        packages: The names of packages to install if they are not yet installed.

    """
    run("pipx upgrade-all")
    for name in [package for package in packages or [] if package not in installed()]:
        install(name)


def installed() -> List[str]:
    """Get a list of installed packages."""
    output = capture("pipx list")
    return re.findall(r"package ([A-Za-z0-9_-]+)", output)


def install_or_upgrade(name: str) -> None:
    """Install or upgrade a package.

    If the given package is not installed, install it. If the package is
    installed, update it.

    Args:
        name: The name of the package to install or update.

    """
    if name in installed():
        return upgrade(name)
    else:
        return install(name)
