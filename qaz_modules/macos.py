from __future__ import annotations

import sys

from qaz import managers
from qaz.modules.base import Bundle
from qaz.modules.registry import registry
from qaz.utils import shell


class MacOS(Bundle):
    name = "macOS"

    managers = (managers.BrewFormula("gnu-sed"),)

    # Configuration files
    zshrc_files = (
        "macos.zsh",
        "sed.zsh",
    )
    symlinks = {
        "RectangleConfig.json": "~/Library/Application Support/Rectangle/",
    }

    def install_action(self) -> None:
        shell.run_script("set-defaults.sh")

    def upgrade_action(self) -> None:
        shell.run_script("set-defaults.sh")


if sys.platform == "darwin":
    registry.register(MacOS)
