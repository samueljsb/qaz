from __future__ import annotations

from pathlib import Path

from qaz import managers
from qaz.modules.base import Module
from qaz.modules.registry import registry
from qaz.utils import shell


FONTS = ["Hack"]


@registry.register
class NerdFonts(Module):
    name = "nerd-fonts"
    manager = managers.Git(
        "https://github.com/ryanoasis/nerd-fonts",
        Path().home() / ".nerd-fonts",
        clone_options="--depth=1",
    )

    def install_action(self) -> None:
        for font_name in FONTS:
            shell.run(self.manager.repo_path / "install.sh", font_name)

    def upgrade_action(self) -> None:
        for font_name in FONTS:
            shell.run(self.manager.repo_path / "install.sh", font_name)
