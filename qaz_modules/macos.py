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


class QuickLookExtensions(Module):
    name = "QuickLook"

    # Configuration files
    zshrc_file = None
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    extensions = (
        "qlcolorcode",
        "qlstephen",
        "qlmarkdown",
        "suspicious-package",
    )

    @classmethod
    def install_action(cls):
        for extension in cls.extensions:
            brew.install_or_upgrade_cask(extension)
        return super().install_action()

    @classmethod
    def upgrade_action(cls):
        for extension in cls.extensions:
            brew.install_or_upgrade_cask(extension)
        return super().upgrade_action()


class Bartender(Module):
    name = "Bartender"

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
