import json
from typing import List

from qaz.utils import shell


def install_or_upgrade_package(package: str):
    if package not in _get_installed_packages():
        shell.run(f"npm install --global {package}")
    else:
        shell.run(f"npm update --global {package}")


def _get_installed_packages() -> List[str]:
    output = shell.capture("npm list --global --json")
    data = json.loads(output)
    return [k for k in data.get("dependencies", {})]
