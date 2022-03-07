from __future__ import annotations

from qaz.managers import brew
from qaz.modules.base import Module
from qaz.modules.registry import registry


@registry.register
class Starship(Module):
    name = "starship"

    # Configuration files
    zshrc_file = "starship.zsh"
    symlinks = {"starship.toml": "~/.config"}

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("starship")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("starship")

    @property
    def version(self) -> str:
        return brew.version("starship")
