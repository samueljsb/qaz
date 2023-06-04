from __future__ import annotations

import sys
from pathlib import Path

from qaz import managers
from qaz.modules.base import Bundle
from qaz.modules.registry import registry
from qaz.utils import files
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
        "RectangleConfig.json": "~/Library/Application Support/Rectangle/RectangleConfig.json",  # noqa: E501
    }

    def _configure_1password_ssh_agent(self) -> None:
        Path("~", ".1password").expanduser().mkdir(exist_ok=True)
        files.create_symlink(
            Path(
                "~/Library/Group Containers/2BUA8C4S2C.com.1password/t/agent.sock"
            ).expanduser(),
            Path("~", ".1password", "agent.sock").expanduser(),
        )

    def pre_install(self) -> None:
        self._configure_1password_ssh_agent()

    def pre_upgrade(self) -> None:
        self._configure_1password_ssh_agent()

    def post_install(self) -> None:
        shell.run_script("set-defaults.sh")

    def post_upgrade(self) -> None:
        shell.run_script("set-defaults.sh")


if sys.platform == "darwin":
    registry.register(MacOS)
