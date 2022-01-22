from __future__ import annotations

from qaz.modules.base import Module


class Rust(Module):
    name = "Rust"
    is_language = True

    # Configuration files
    zshrc_file = None
    symlinks: dict[str, str] = {}

    # Other
    vscode_extensions: list[str] = []
