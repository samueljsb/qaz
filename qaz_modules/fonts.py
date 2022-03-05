from __future__ import annotations

import logging
import sys
from pathlib import Path

from qaz.managers import git, shell
from qaz.modules.base import Module
from qaz.modules.registry import registry


logger = logging.getLogger(__name__)

FONTS = ["Hack"]


@registry.register
class NerdFonts(Module):
    name = "nerd-fonts"

    def install_action(self) -> None:
        logger.warning("... this might take a while!")
        repo_path = Path().home() / ".nerd-fonts"
        git.clone(
            repo_url="https://github.com/ryanoasis/nerd-fonts.git",
            repo_path=repo_path,
            options="--depth=1",
        )

        for font_name in FONTS:
            shell.run(f"{repo_path / 'install.sh'} {font_name}")

    def upgrade_action(self) -> None:
        repo_path = Path().home() / ".nerd-fonts"

        if sys.platform == "darwin":
            # There are issues with case-insensitive filenames that prevent the repo
            # from being pulled on macOS.
            logger.error("nerd-fonts cannot be upgraded on MacOS at the moment 😞")
        else:
            git.pull(repo_path)

        for font_name in FONTS:
            shell.run(f"{repo_path / 'install.sh'} {font_name}")
