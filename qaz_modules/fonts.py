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
        clone_options=("--filter=blob:none", "--sparse"),
    )

    def _install_font(self, font_name: str) -> None:
        # fmt: off
        shell.run(
            "git", "-C", self.manager.repo_path, "sparse-checkout", "add", f"patched-fonts/{font_name}",  # noqa: E501
        )
        # fmt: on
        shell.run(self.manager.repo_path / "install.sh", font_name)

    def post_install(self) -> None:
        for font_name in FONTS:
            self._install_font(font_name)

    def post_upgrade(self) -> None:
        for font_name in FONTS:
            self._install_font(font_name)
