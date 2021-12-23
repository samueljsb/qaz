from __future__ import annotations

from qaz.managers import brew
from qaz.modules.base import Module


class MacTex(Module):
    name = "LaTeX"

    # Other
    vscode_extensions: list[str] = []

    # Package Management
    package_manager = brew.Homebrew("mactex")
