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

    package_manager = asdf.ASDF("starship")
