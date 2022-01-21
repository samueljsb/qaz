from __future__ import annotations

from qaz.managers import brew
from qaz.modules.base import Module


class MacTex(Module):
    name = "LaTeX"

    # Configuration files
    zshrc_file = None
    symlinks: dict[str, str] = {}

    # Other
    vscode_extensions: list[str] = []

    def install_action(self):
        brew.install_or_upgrade_cask("mactex")

    def upgrade_action(self):
        brew.install_or_upgrade_cask("mactex")
