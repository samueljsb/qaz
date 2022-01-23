from __future__ import annotations

from qaz.managers import brew, shell
from qaz.modules.base import Module


class MacOS(Module):
    name = "macOS"

    def install_action(self) -> None:
        shell.run_script("set-defaults.sh")

    def upgrade_action(self) -> None:
        shell.run_script("set-defaults.sh")


class Bartender(Module):
    name = "Bartender"
    auto_update = True

    def install_action(self) -> None:
        brew.install_or_upgrade_cask("bartender")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_cask("bartender")


class Rectangle(Module):
    name = "Rectangle"
    auto_update = True

    def install_action(self) -> None:
        brew.install_or_upgrade_cask("rectangle")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_cask("rectangle")
