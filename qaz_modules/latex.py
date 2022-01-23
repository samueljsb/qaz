from __future__ import annotations

from qaz.managers import brew
from qaz.modules.base import Module


class MacTex(Module):
    name = "LaTeX"

    @classmethod
    def install_action(cls) -> None:
        brew.install_or_upgrade_cask("mactex")

    @classmethod
    def upgrade_action(cls) -> None:
        brew.install_or_upgrade_cask("mactex")
