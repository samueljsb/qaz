from __future__ import annotations

import sys

from qaz import managers
from qaz.modules.base import Module
from qaz.modules.registry import registry


@registry.register
class Bat(Module):
    name = "bat"
    manager = managers.BrewFormula("bat")

    # Configuration files
    zshrc_file = "bat.zsh"


@registry.register
class Exa(Module):
    name = "exa"
    manager = managers.BrewFormula("exa")

    # Configuration files
    zshrc_file = "exa.zsh"


@registry.register
class Fzf(Module):
    name = "fzf"
    manager = managers.BrewFormula("fzf")

    # Configuration files
    zshrc_file = "fzf.zsh"


class GNUSed(Module):
    """
    GNU sed.

    This allows MacOS to have a more convenient version of sed.
    """

    name = "sed"
    manager = managers.BrewFormula("gnu-sed")

    # Configuration files
    zshrc_file = "sed.zsh"


if sys.platform == "darwin":
    registry.register(GNUSed)


@registry.register
class Less(Module):
    name = "less"
    manager = managers.BrewFormula("less")

    # Configuration files
    zshrc_file = "less.zsh"


@registry.register
class McFly(Module):
    name = "McFly"
    manager = managers.BrewFormula("cantino/mcfly/mcfly")

    # Configuration files
    zshrc_file = "mcfly.zsh"


@registry.register
class PGCLI(Module):
    name = "pgcli"
    manager = managers.BrewFormula("pgcli")


@registry.register
class TrashCLI(Module):
    name = "trash-cli"
    manager = managers.NPM("trash-cli")

    # Configuration files
    zshrc_file = "trash-cli.zsh"
