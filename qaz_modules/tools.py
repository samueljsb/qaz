from __future__ import annotations

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
    manager = managers.Pip("pgcli")


@registry.register
class TrashCLI(Module):
    name = "trash-cli"
    manager = managers.NPM("trash-cli")

    # Configuration files
    zshrc_file = "trash-cli.zsh"
