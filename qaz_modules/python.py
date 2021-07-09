from sys import platform
from typing import Dict, List

from qaz.managers import asdf, brew, pip, pipx, shell
from qaz.modules.base import Module


class Python(Module):
    name = "Python"

    # Configuration files
    zshrc_file = "python.zsh"
    symlinks = {".pypirc": "~", "pythonstartup.py": "~/.config/", ".pdbrc.py": "~"}

    # Other
    vscode_extensions = [
        "lextudio.restructuredtext",
        "ms-python.python",
        "ms-python.vscode-pylance",
        "wholroyd.jinja",
    ]

    @classmethod
    def install_action(cls):
        asdf.install_or_upgrade_plugin("python")
        pip.install_or_upgrade_package("pip")
        if platform == "darwin":
            pip.install_or_upgrade_package("gnureadline")

    @classmethod
    def upgrade_action(cls):
        asdf.install_or_upgrade_plugin("python")
        pip.install_or_upgrade_package("pip")
        if platform == "darwin":
            pip.install_or_upgrade_package("gnureadline")


class Poetry(Module):
    name = "Poetry"

    # Configuration files
    zshrc_file = "poetry.zsh"
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    # N.B. This is installed by install.sh, so no install script is needed here.
    @classmethod
    def install_action(cls):
        pass

    @classmethod
    def upgrade_action(cls):
        shell.run("poetry self update")


class Rich(Module):
    name = "rich"

    # Configuration files
    zshrc_file = None
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        pip.install_or_upgrade_package("rich")

    @classmethod
    def upgrade_action(cls):
        pip.install_or_upgrade_package("rich")


class Pipx(Module):
    name = "pipx"

    # Configuration files
    zshrc_file = "pipx.zsh"
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        brew.install_or_upgrade_formula("pipx")

    @classmethod
    def upgrade_action(cls):
        brew.install_or_upgrade_formula("pipx")


class Bpython(Module):
    name = "bpython"

    # Configuration files
    zshrc_file = None
    symlinks = {"bpython": "~/.config/bpython"}

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        pipx.install_or_upgrade_package("bpython")

    @classmethod
    def upgrade_action(cls):
        pipx.install_or_upgrade_package("bpython")


class Tox(Module):
    name = "tox"

    # Configuration files
    zshrc_file = None
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        pipx.install_or_upgrade_package("tox")

    @classmethod
    def upgrade_action(cls):
        pipx.install_or_upgrade_package("tox")
