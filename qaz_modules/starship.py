from __future__ import annotations

from qaz import managers
from qaz.modules.base import Module
from qaz.modules.registry import registry


@registry.register
class Starship(Module):
    name = "starship"
    manager = managers.BrewFormula("starship")

    # Configuration files
    zshrc_file = "starship.zsh"
    symlinks = {"starship.toml": "~/.config"}
