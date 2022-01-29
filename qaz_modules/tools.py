from __future__ import annotations

import sys

from qaz.managers import brew, npm
from qaz.modules.base import Module
from qaz.modules.registry import register


@register
class Bat(Module):
    name = "bat"

    # Configuration files
    zshrc_file = "bat.zsh"

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("bat")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("bat")


@register
class Exa(Module):
    name = "exa"

    # Configuration files
    zshrc_file = "exa.zsh"

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("exa")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("exa")


@register
class Figlet(Module):
    name = "FIGlet"

    # Configuration files
    zshrc_file = "figlet.zsh"

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("figlet")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("figlet")


@register
class Fzf(Module):
    name = "fzf"

    # Configuration files
    zshrc_file = "fzf.zsh"

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("fzf")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("fzf")


class GNUSed(Module):
    """
    GNU sed.

    This allows MacOS to have a more convenient version of sed.
    """

    name = "sed"

    # Configuration files
    zshrc_file = "sed.zsh"

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("gnu-sed")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("gnu-sed")


if sys.platform == "darwin":
    register(GNUSed)


@register
class Less(Module):
    name = "less"

    # Configuration files
    zshrc_file = "less.zsh"

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("less")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("less")


@register
class McFly(Module):
    name = "McFly"

    # Configuration files
    zshrc_file = "mcfly.zsh"

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("cantino/mcfly/mcfly")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("cantino/mcfly/mcfly")


@register
class PGCLI(Module):
    name = "pgcli"

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("pgcli")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("pgcli")


@register
class TrashCLI(Module):
    name = "trash-cli"

    # Configuration files
    zshrc_file = "trash-cli.zsh"

    def install_action(self) -> None:
        npm.install_or_upgrade_package("trash-cli")

    def upgrade_action(self) -> None:
        npm.install_or_upgrade_package("trash-cli")
