from typing import Dict, List

from qaz.managers import brew, shell
from qaz.modules.base import Module


class MacOS(Module):
    name = "macOS"

    # Configuration files
    zshrc_file = None
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        shell.run_script("set-defaults.sh")

    @classmethod
    def upgrade_action(cls):
        shell.run_script("set-defaults.sh")


class Bartender(Module):
    name = "Bartender"
    auto_update = True

    # Configuration files
    zshrc_file = None
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        brew.install_or_upgrade_cask("bartender")

    @classmethod
    def upgrade_action(cls):
        brew.install_or_upgrade_cask("bartender")


class Rectangle(Module):
    name = "Rectangle"
    auto_update = True

    # Configuration files
    zshrc_file = None
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        brew.install_or_upgrade_cask("rectangle")

    @classmethod
    def upgrade_action(cls):
        brew.install_or_upgrade_cask("rectangle")
