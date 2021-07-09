from typing import Dict, List

from qaz.managers import brew
from qaz.modules.base import Module


class MacTex(Module):
    name = "LaTeX"

    # Configuration files
    zshrc_file = None
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    def install_action(self):
        brew.install_or_upgrade_cask("mactex")

    def upgrade_action(self):
        brew.install_or_upgrade_cask("mactex")
