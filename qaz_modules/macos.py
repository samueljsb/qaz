from __future__ import annotations

import sys

from qaz import managers
from qaz.modules.base import Bundle
from qaz.modules.registry import registry
from qaz.utils import shell


class MacOS(Bundle):
    name = "macOS"

    managers = (
        managers.BrewFormula("findutils"),  # find, locate, updatedb, xargs
        managers.BrewFormula("gawk"),  # awk
        managers.BrewFormula("gnu-sed"),  # sed
        managers.BrewFormula("grep"),  # egrep, fgrep, grep
    )

    # Configuration files
    zshrc_files = ("macos.zsh",)
    symlinks = {
        "RectangleConfig.json": "~/Library/Application Support/Rectangle/",
    }

    def post_install(self) -> None:
        shell.run_script("set-defaults.sh")

    def post_upgrade(self) -> None:
        shell.run_script("set-defaults.sh")


if sys.platform == "darwin":
    registry.register(MacOS)
