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

    # Package Management
    package_manager = brew.Homebrew
    package_name = "mactex"
