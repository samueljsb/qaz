from __future__ import annotations

import sys

from qaz.managers import brew, shell
from qaz.modules.base import Module
from qaz.modules.registry import register


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


if sys.platform == "darwin":
    register(MacOS)
    register(Bartender)
    register(Rectangle)
