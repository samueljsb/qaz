from __future__ import annotations

from qaz.managers import asdf
from qaz.modules.base import Module


class Yarn(Module):
    name = "Yarn"

    @classmethod
    def install_action(cls) -> None:
        asdf.install_or_upgrade_plugin("yarn")

    @classmethod
    def upgrade_action(cls) -> None:
        asdf.install_or_upgrade_plugin("yarn")
