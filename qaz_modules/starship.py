from __future__ import annotations

from qaz.managers import asdf
from qaz.modules.base import Module


class Starship(Module):
    name = "starship"

    # Configuration files
    zshrc_file = "starship.zsh"
    symlinks = {"starship.toml": "~/.config"}

    def install_action(self) -> None:
        asdf.install_or_upgrade_plugin("starship")

    def upgrade_action(self) -> None:
        asdf.install_or_upgrade_plugin("starship")
