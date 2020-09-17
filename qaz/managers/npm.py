import json
from typing import List

from qaz.utils import capture, run


def install(name: str) -> None:
    """Install a package.

    Args:
        name: The name of the package to install.

    """
    run(f"npm install --global {name}")


def upgrade(name: str) -> None:
    """Update a package.

    Args:
        name: The name of the package to upgrade.

    """
    run(f"npm update --global {name}")


def upgrade_all() -> None:
    """Update all packages."""
    for name in [package for package in installed()]:
        upgrade(name)


def installed() -> List[str]:
    """Get a list of installed packages."""
    output = capture("npm list --global --json")
    data = json.loads(output)
    if "dependencies" in data:
        return [k for k in data["dependencies"].keys()]
    return []


def install_or_upgrade(name: str) -> None:
    """Install or update a package.

    If the given package is not installed, install it. If the package is
    installed, update it.

    Args:
        name: The name of the package to install or upgrade.

    """
    if name in installed():
        return upgrade(name)
    else:
        return install(name)
