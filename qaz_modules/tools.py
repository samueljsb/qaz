from typing import Dict, List

from qaz.managers import brew, npm
from qaz.modules.base import Module


class Bat(Module):
    name = "bat"

    # Configuration files
    zshrc_file = "bat.zsh"
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []
    # Package Management
    package_manager = brew.Homebrew
    package_name = "bat"


class Exa(Module):
    name = "exa"

    # Configuration files
    zshrc_file = "exa.zsh"
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    # Package Management
    package_manager = brew.Homebrew
    package_name = "exa"


class Figlet(Module):
    name = "FIGlet"

    # Configuration files
    zshrc_file = "figlet.zsh"
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    # Package Management
    package_manager = brew.Homebrew
    package_name = "figlet"


class Fzf(Module):
    name = "fzf"

    # Configuration files
    zshrc_file = "fzf.zsh"
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    # Package Management
    package_manager = brew.Homebrew
    package_name = "fzf"


class GNUSed(Module):
    """
    GNU sed.

    This allows MacOS to have a more convenient version of sed.
    """

    name = "sed"

    # Configuration files
    zshrc_file = "sed.zsh"
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    # Package Management
    package_manager = brew.Homebrew
    package_name = "gnu-sed"


class Less(Module):
    name = "less"

    # Configuration files
    zshrc_file = "less.zsh"
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    # Package Management
    package_manager = brew.Homebrew
    package_name = "less"


class McFly(Module):
    name = "McFly"

    # Configuration files
    zshrc_file = "mcfly.zsh"
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    # Package Management
    package_manager = brew.Homebrew
    package_name = "cantino/mcfly/mcfly"


class TrashCLI(Module):
    name = "trash-cli"

    # Configuration files
    zshrc_file = "trash-cli.zsh"
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        npm.install_or_upgrade_package("trash-cli")

    @classmethod
    def upgrade_action(cls):
        npm.install_or_upgrade_package("trash-cli")
