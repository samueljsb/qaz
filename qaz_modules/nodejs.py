from __future__ import annotations

import os

from qaz.managers import asdf
from qaz.modules.base import Module


class NodeJS(Module):
    name = "Node.js"

    # Other
    vscode_extensions = [
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "numso.prettier-standard-vscode",
    ]

    @classmethod
    def install_action(cls) -> None:
        os.environ["NODEJS_CHECK_SIGNATURES"] = "no"
        asdf.install_or_upgrade_plugin("nodejs")

    @classmethod
    def upgrade_action(cls) -> None:
        os.environ["NODEJS_CHECK_SIGNATURES"] = "no"
        asdf.install_or_upgrade_plugin("nodejs")


class Yarn(Module):
    name = "Yarn"

    # Other
    vscode_extensions: list[str] = []

    @classmethod
    def install_action(cls) -> None:
        asdf.install_or_upgrade_plugin("yarn")

    @classmethod
    def upgrade_action(cls) -> None:
        asdf.install_or_upgrade_plugin("yarn")
