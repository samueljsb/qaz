from typing import List

from qaz.managers import asdf
from qaz.modules.base import Module


class Starship(Module):
    name = "starship"

    # Configuration files
    zshrc_file = "starship.zsh"
    symlinks = {"starship.toml": "~/.config"}

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        asdf.install_or_upgrade_plugin("starship")

    @classmethod
    def upgrade_action(cls):
        asdf.install_or_upgrade_plugin("starship")
