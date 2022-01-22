from __future__ import annotations

from qaz.managers import asdf
from qaz.modules.base import Module


class Rust(Module):
    name = "Rust"
    is_language = True

    # Configuration files
    zshrc_file = None
    symlinks: dict[str, str] = {}

    # Other
    vscode_extensions = [
        "rust-lang.rust",
    ]

    @classmethod
    def install_action(cls) -> None:
        asdf.install_or_upgrade_plugin("rust")

    @classmethod
    def upgrade_action(cls) -> None:
        asdf.install_or_upgrade_plugin("rust")
