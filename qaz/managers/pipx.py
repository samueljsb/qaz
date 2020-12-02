import re
from typing import List

from qaz.utils import capture, run


def install_or_upgrade_package(package: str):
    if package not in _get_installed_packages():
        run(f"pipx install {package}")
    else:
        run(f"pipx upgrade {package}", allow_fail=True)  # pipx returns 1 on success


def _get_installed_packages() -> List[str]:
    output = capture("pipx list")
    return re.findall(r"package ([A-Za-z0-9_-]+)", output)
