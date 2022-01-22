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

    package_manager = asdf.ASDF("nodejs")

    @classmethod
    def install_action(cls) -> None:
        os.environ["NODEJS_CHECK_SIGNATURES"] = "no"
        super().install_action()

    @classmethod
    def upgrade_action(cls) -> None:
        os.environ["NODEJS_CHECK_SIGNATURES"] = "no"
        super().upgrade_action()


class Yarn(Module):
    name = "Yarn"

    # Other
    vscode_extensions: list[str] = []

    package_manager = asdf.ASDF("yarn")
