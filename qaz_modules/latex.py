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

    @classmethod
    def install_action(cls) -> None:
        brew.install_or_upgrade_cask("mactex")

    @classmethod
    def upgrade_action(cls) -> None:
        brew.install_or_upgrade_cask("mactex")
