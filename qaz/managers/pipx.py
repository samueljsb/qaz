from __future__ import annotations

import re

from . import shell


def install_or_upgrade_package(package: str) -> None:
    if package not in _get_installed_packages():
        shell.run(f"pipx install {package}")
    else:
        shell.run(
            f"pipx upgrade {package}", allow_fail=True
        )  # pipx returns 1 on success


def _get_installed_packages() -> list[str]:
    output = shell.capture("pipx list")
    return re.findall(r"package ([A-Za-z0-9_-]+)", output)
