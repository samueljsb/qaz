from __future__ import annotations

from qaz.managers import asdf
from qaz.modules.base import Module


class Yarn(Module):
    name = "Yarn"

    def install_action(self) -> None:
        asdf.install_or_upgrade_plugin("yarn")

    def upgrade_action(self) -> None:
        asdf.install_or_upgrade_plugin("yarn")
