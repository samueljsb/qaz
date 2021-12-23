from __future__ import annotations

from qaz.managers import asdf
from qaz.modules.base import Module


class Rust(Module):
    name = "Rust"

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
