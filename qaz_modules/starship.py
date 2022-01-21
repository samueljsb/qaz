from __future__ import annotations

from qaz.managers import asdf
from qaz.modules.base import Module


class Starship(Module):
    name = "starship"

    # Configuration files
    zshrc_file = "starship.zsh"
    symlinks = {"starship.toml": "~/.config"}

    # Other
    vscode_extensions: list[str] = []

    @classmethod
    def install_action(cls) -> None:
        asdf.install_or_upgrade_plugin("starship")

    @classmethod
    def upgrade_action(cls) -> None:
        asdf.install_or_upgrade_plugin("starship")
