from __future__ import annotations

from qaz.managers import brew, shell
from qaz.modules.base import Module


class MacOS(Module):
    name = "macOS"

    @classmethod
    def install_action(cls) -> None:
        shell.run_script("set-defaults.sh")

    @classmethod
    def upgrade_action(cls) -> None:
        shell.run_script("set-defaults.sh")


class Bartender(Module):
    name = "Bartender"
    auto_update = True

    @classmethod
    def install_action(cls) -> None:
        brew.install_or_upgrade_cask("bartender")

    @classmethod
    def upgrade_action(cls) -> None:
        brew.install_or_upgrade_cask("bartender")


class Rectangle(Module):
    name = "Rectangle"
    auto_update = True

    @classmethod
    def install_action(cls) -> None:
        brew.install_or_upgrade_cask("rectangle")

    @classmethod
    def upgrade_action(cls) -> None:
        brew.install_or_upgrade_cask("rectangle")
