from __future__ import annotations

from typing import NamedTuple

from qaz.utils import shell


class BrewFormula(NamedTuple):
    formula: str

    def install(self) -> None:
        return self._install_or_upgrade()

    def upgrade(self) -> None:
        return self._install_or_upgrade()

    def _install_or_upgrade(self) -> None:
        if self.formula.split("/")[-1] in self._installed():
            shell.run(
                *("brew", "upgrade", self.formula),
                env={"HOMEBREW_NO_INSTALLED_DEPENDENTS_CHECK": "1"},
            )
        else:
            shell.run("brew", "install", self.formula)

    def _installed(self) -> list[str]:
        return shell.capture("brew", "list", "--formula", "-1").split()

    def version(self) -> str:
        versions = shell.capture("brew", "list", "--versions", self.formula).strip()
        if not versions:  # not installed
            return ""
        return versions.split()[-1]


class BrewCask(NamedTuple):
    cask: str

    def install(self) -> None:
        return self._install_or_upgrade()

    def upgrade(self) -> None:
        return self._install_or_upgrade()

    def _install_or_upgrade(self) -> None:
        if self.cask in self._installed():
            shell.run("brew", "upgrade", "--cask", self.cask)
        else:
            shell.run("brew", "cask", "install", self.cask)

    def _installed(self) -> list[str]:
        return shell.capture("brew", "list", "--cask", "-1").split()

    def version(self) -> str:
        versions = shell.capture("brew", "list", "--versions", self.cask).strip()
        if not versions:  # not installed
            return ""
        return versions.split()[-1]
