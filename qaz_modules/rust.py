from typing import Dict

from qaz.managers import asdf
from qaz.modules.base import Module


class Rust(Module):
    name = "Rust"

    # Configuration files
    zshrc_file = None
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions = [
        "rust-lang.rust",
    ]

    @classmethod
    def install_action(self):
        asdf.install_or_upgrade_plugin("rust")

    @classmethod
    def upgrade_action(cls):
        asdf.install_or_upgrade_plugin("rust")
