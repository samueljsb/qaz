from __future__ import annotations

from qaz.managers import asdf
from qaz.modules.base import Module


class NodeJS(Module):
    name = "Node.js"
    is_language = True

    # Configuration files
    zshrc_file = None
    symlinks: dict[str, str] = {}

    # Other
    vscode_extensions: list[str] = []


class Yarn(Module):
    name = "Yarn"

    # Configuration files
    zshrc_file = None
    symlinks: dict[str, str] = {}

    # Other
    vscode_extensions: list[str] = []

    @classmethod
    def install_action(cls) -> None:
        asdf.install_or_upgrade_plugin("yarn")

    @classmethod
    def upgrade_action(cls) -> None:
        asdf.install_or_upgrade_plugin("yarn")
