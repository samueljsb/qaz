from __future__ import annotations

import logging
import sys
from pathlib import Path

from qaz.managers import git, shell
from qaz.modules.base import Module


logger = logging.getLogger(__name__)

FONTS = ["Hack"]


class NerdFonts(Module):
    name = "nerd-fonts"

    # Other
    vscode_extensions: list[str] = []

    package_manager = git.Git(
        url="https://github.com/ryanoasis/nerd-fonts.git",
        repo_path=Path().home() / ".nerd-fonts",
        options="--depth=1",
    )

    @classmethod
    def install_action(cls) -> None:
        logger.warning("... this might take a while!")
        super().install_action()

        repo_path = Path().home() / ".nerd-fonts"
        for font_name in FONTS:
            shell.run(f"{repo_path / 'install.sh'} {font_name}")

    @classmethod
    def upgrade_action(cls) -> None:
        if sys.platform == "darwin":
            # There are issues with case-insensitive filenames that prevent the repo
            # from being pulled on macOS.
            logger.error("nerd-fonts cannot be upgraded on MacOS at the moment 😞")
        else:
            super().upgrade_action()

        repo_path = Path().home() / ".nerd-fonts"
        for font_name in FONTS:
            shell.run(f"{repo_path / 'install.sh'} {font_name}")
