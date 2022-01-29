from __future__ import annotations

import sys

from qaz.managers import brew
from qaz.modules.base import Module
from qaz.modules.registry import register


class MacTex(Module):
    name = "LaTeX"

    def install_action(self) -> None:
        brew.install_or_upgrade_cask("mactex")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_cask("mactex")


if sys.platform == "darwin":
    register(MacTex)
