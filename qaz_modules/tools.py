from __future__ import annotations

from qaz.managers import brew, npm
from qaz.modules.base import Module


class Bat(Module):
    name = "bat"

    # Configuration files
    zshrc_file = "bat.zsh"

    @classmethod
    def install_action(cls) -> None:
        brew.install_or_upgrade_formula("bat")

    @classmethod
    def upgrade_action(cls) -> None:
        brew.install_or_upgrade_formula("bat")


class Exa(Module):
    name = "exa"

    # Configuration files
    zshrc_file = "exa.zsh"

    @classmethod
    def install_action(cls) -> None:
        brew.install_or_upgrade_formula("exa")

    @classmethod
    def upgrade_action(cls) -> None:
        brew.install_or_upgrade_formula("exa")


class Figlet(Module):
    name = "FIGlet"

    # Configuration files
    zshrc_file = "figlet.zsh"

    @classmethod
    def install_action(cls) -> None:
        brew.install_or_upgrade_formula("figlet")

    @classmethod
    def upgrade_action(cls) -> None:
        brew.install_or_upgrade_formula("figlet")


class Fzf(Module):
    name = "fzf"

    # Configuration files
    zshrc_file = "fzf.zsh"

    @classmethod
    def install_action(cls) -> None:
        brew.install_or_upgrade_formula("fzf")

    @classmethod
    def upgrade_action(cls) -> None:
        brew.install_or_upgrade_formula("fzf")


class GNUSed(Module):
    """
    GNU sed.

    This allows MacOS to have a more convenient version of sed.
    """

    name = "sed"

    # Configuration files
    zshrc_file = "sed.zsh"

    @classmethod
    def install_action(cls) -> None:
        brew.install_or_upgrade_formula("gnu-sed")

    @classmethod
    def upgrade_action(cls) -> None:
        brew.install_or_upgrade_formula("gnu-sed")


class Less(Module):
    name = "less"

    # Configuration files
    zshrc_file = "less.zsh"

    @classmethod
    def install_action(cls) -> None:
        brew.install_or_upgrade_formula("less")

    @classmethod
    def upgrade_action(cls) -> None:
        brew.install_or_upgrade_formula("less")


class McFly(Module):
    name = "McFly"

    # Configuration files
    zshrc_file = "mcfly.zsh"

    @classmethod
    def install_action(cls) -> None:
        brew.install_or_upgrade_formula("cantino/mcfly/mcfly")

    @classmethod
    def upgrade_action(cls) -> None:
        brew.install_or_upgrade_formula("cantino/mcfly/mcfly")


class TrashCLI(Module):
    name = "trash-cli"

    # Configuration files
    zshrc_file = "trash-cli.zsh"

    @classmethod
    def install_action(cls) -> None:
        npm.install_or_upgrade_package("trash-cli")

    @classmethod
    def upgrade_action(cls) -> None:
        npm.install_or_upgrade_package("trash-cli")
