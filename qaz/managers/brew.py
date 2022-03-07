from __future__ import annotations

from . import shell


def install_or_upgrade_formula(formula: str) -> None:
    if formula.split("/")[-1] in _installed_formulae():
        shell.run(
            f"brew upgrade {formula}",
            env={"HOMEBREW_NO_INSTALLED_DEPENDENTS_CHECK": "1"},
        )
    else:
        shell.run(f"brew install {formula}")


def _installed_formulae() -> list[str]:
    return shell.capture("brew list --formula -1").split()


def install_or_upgrade_cask(cask: str) -> None:
    if cask in _installed_casks():
        shell.run(f"brew upgrade --cask {cask}")
    else:
        shell.run(f"brew cask install {cask}")


def _installed_casks() -> list[str]:
    return shell.capture("brew list --cask -1").split()


def version(name: str) -> str:
    versions = shell.capture(f"brew list --versions {name}").strip()
    if not versions:  # not installed
        return ""
    return versions.split()[-1]
