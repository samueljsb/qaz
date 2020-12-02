import json
from typing import List

from qaz.utils import capture, run


def install_or_upgrade_package(package: str):
    if package not in _get_installed_packages():
        run(f"npm install --global {package}")
    else:
        run(f"npm update --global {package}")


def _get_installed_packages() -> List[str]:
    output = capture("npm list --global --json")
    data = json.loads(output)
    return [k for k in data.get("dependencies", {})]
