from __future__ import annotations

import json

from . import shell


def install_or_upgrade_package(package: str) -> None:
    if package not in _installed_packages():
        shell.run(f"npm install --global {package}")
    else:
        shell.run(f"npm update --global {package}")


def _installed_packages() -> list[str]:
    output = shell.capture("npm list --global --json")
    data = json.loads(output)
    return [k for k in data.get("dependencies", {})]
