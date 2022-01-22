from __future__ import annotations

from qaz.managers import brew, npm
from qaz.modules.base import Module


class Bat(Module):
    name = "bat"

    # Configuration files
    zshrc_file = "bat.zsh"

    # Other
    vscode_extensions: list[str] = []

    # Package Management
    package_manager = brew.Homebrew("bat")


class Exa(Module):
    name = "exa"

    # Configuration files
    zshrc_file = "exa.zsh"

    # Other
    vscode_extensions: list[str] = []

    # Package Management
    package_manager = brew.Homebrew("exa")


class Figlet(Module):
    name = "FIGlet"

    # Configuration files
    zshrc_file = "figlet.zsh"

    # Other
    vscode_extensions: list[str] = []

    # Package Management
    package_manager = brew.Homebrew("figlet")


class Fzf(Module):
    name = "fzf"

    # Configuration files
    zshrc_file = "fzf.zsh"

    # Other
    vscode_extensions: list[str] = []

    # Package Management
    package_manager = brew.Homebrew("fzf")


class GNUSed(Module):
    """
    GNU sed.

    This allows MacOS to have a more convenient version of sed.
    """

    name = "sed"

    # Configuration files
    zshrc_file = "sed.zsh"

    # Other
    vscode_extensions: list[str] = []

    # Package Management
    package_manager = brew.Homebrew("gnu-sed")


class Less(Module):
    name = "less"

    # Configuration files
    zshrc_file = "less.zsh"

    # Other
    vscode_extensions: list[str] = []

    # Package Management
    package_manager = brew.Homebrew("less")


class McFly(Module):
    name = "McFly"

    # Configuration files
    zshrc_file = "mcfly.zsh"

    # Other
    vscode_extensions: list[str] = []

    # Package Management
    package_manager = brew.Homebrew("cantino/mcfly/mcfly")


class TrashCLI(Module):
    name = "trash-cli"

    # Configuration files
    zshrc_file = "trash-cli.zsh"

    # Other
    vscode_extensions: list[str] = []

    package_manager = npm.NPM("trash-cli")
