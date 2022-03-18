from __future__ import annotations

import sys

from qaz.modules.base import Module
from qaz.modules.registry import registry
from qaz.utils import shell


class MacOS(Module):
    name = "macOS"

    # Configuration files
    zshrc_file = "macos.zsh"

    def install_action(self) -> None:
        shell.run_script("set-defaults.sh")

    def upgrade_action(self) -> None:
        shell.run_script("set-defaults.sh")


if sys.platform == "darwin":
    registry.register(MacOS)
