from __future__ import annotations

from sys import platform

from qaz.managers import asdf, brew, pip, pipx, shell
from qaz.modules.base import Module


class Python(Module):
    name = "Python"

    # Configuration files
    zshrc_file = "python.zsh"
    symlinks = {".pypirc": "~", "pythonstartup.py": "~/.config/", ".pdbrc.py": "~"}

    # Other
    vscode_extensions = [
        "freakypie.code-python-isort",
        "lextudio.restructuredtext",
        "ms-python.python",
        "ms-python.vscode-pylance",
        "wholroyd.jinja",
    ]

    package_manager = asdf.ASDF("python")

    @classmethod
    def install_action(cls) -> None:
        super().install_action()
        pip.install_or_upgrade_package("pip")
        if platform == "darwin":
            pip.install_or_upgrade_package("gnureadline")

    @classmethod
    def upgrade_action(cls) -> None:
        super().upgrade_action()
        pip.install_or_upgrade_package("pip")
        if platform == "darwin":
            pip.install_or_upgrade_package("gnureadline")


class Poetry(Module):
    name = "Poetry"

    # Configuration files
    zshrc_file = "poetry.zsh"

    # Other
    vscode_extensions: list[str] = []

    @classmethod
    def install_action(cls) -> None:
        shell.run(
            "curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python"  # noqa: E501
        )

    @classmethod
    def upgrade_action(cls) -> None:
        shell.run("poetry self update")


class Rich(Module):
    name = "rich"

    # Other
    vscode_extensions: list[str] = []

    @classmethod
    def install_action(cls) -> None:
        pip.install_or_upgrade_package("rich")

    @classmethod
    def upgrade_action(cls) -> None:
        pip.install_or_upgrade_package("rich")


class Pipx(Module):
    name = "pipx"

    # Configuration files
    zshrc_file = "pipx.zsh"

    # Other
    vscode_extensions: list[str] = []

    # Package Management
    package_manager = brew.Homebrew("pipx")


class Bpython(Module):
    name = "bpython"

    # Configuration files
    symlinks = {"bpython": "~/.config/bpython"}

    # Other
    vscode_extensions: list[str] = []

    @classmethod
    def install_action(cls) -> None:
        pipx.install_or_upgrade_package("bpython")

    @classmethod
    def upgrade_action(cls) -> None:
        pipx.install_or_upgrade_package("bpython")


class Tox(Module):
    name = "tox"

    # Other
    vscode_extensions: list[str] = []

    @classmethod
    def install_action(cls) -> None:
        pipx.install_or_upgrade_package("tox")

    @classmethod
    def upgrade_action(cls) -> None:
        pipx.install_or_upgrade_package("tox")
