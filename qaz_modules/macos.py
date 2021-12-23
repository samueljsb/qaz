from __future__ import annotations

from qaz.managers import brew, shell
from qaz.modules.base import Module


class MacOS(Module):
    name = "macOS"

    # Other
    vscode_extensions: list[str] = []

    @classmethod
    def install_action(cls) -> None:
        shell.run_script("set-defaults.sh")

    @classmethod
    def upgrade_action(cls) -> None:
        shell.run_script("set-defaults.sh")


class Bartender(Module):
    name = "Bartender"
    auto_update = True

    # Other
    vscode_extensions: list[str] = []

    # Package Management
    package_manager = brew.Homebrew("bartender")


class Rectangle(Module):
    name = "Rectangle"
    auto_update = True

    # Other
    vscode_extensions: list[str] = []

    # Package Management
    package_manager = brew.Homebrew("rectangle")
