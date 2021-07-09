import os
from typing import Dict, List

from qaz.managers import asdf
from qaz.modules.base import Module


class NodeJS(Module):
    name = "Node.js"

    # Configuration files
    zshrc_file = None
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions = [
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "numso.prettier-standard-vscode",
    ]

    @classmethod
    def install_action(cls):
        os.environ["NODEJS_CHECK_SIGNATURES"] = "no"
        asdf.install_or_upgrade_plugin("nodejs")

    @classmethod
    def upgrade_action(cls):
        os.environ["NODEJS_CHECK_SIGNATURES"] = "no"
        asdf.install_or_upgrade_plugin("nodejs")


class Yarn(Module):
    name = "Yarn"

    # Configuration files
    zshrc_file = None
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        asdf.install_or_upgrade_plugin("yarn")

    @classmethod
    def upgrade_action(cls):
        asdf.install_or_upgrade_plugin("yarn")
