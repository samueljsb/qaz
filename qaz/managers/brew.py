from typing import List

from qaz.utils import capture, run


def install_or_upgrade_formula(formula: str):
    if formula.split("/")[-1] in _get_installed_formulae():
        run(f"brew upgrade {formula}")
    else:
        run(f"brew install {formula}")


def _get_installed_formulae() -> List[str]:
    return capture("brew list -1").split()


def install_or_upgrade_cask(cask: str):
    if cask in _get_installed_casks():
        run(f"brew upgrade --cask {cask}")
    else:
        run(f"brew cask install {cask}")


def _get_installed_casks() -> List[str]:
    return capture("brew list --cask -1").split()
