from __future__ import annotations

from qaz.managers import brew, pipx, shell
from qaz.modules.base import Module


class Python(Module):
    name = "Python"
    is_language = True

    # Configuration files
    zshrc_file = "python.zsh"
    symlinks = {".pypirc": "~", "pythonstartup.py": "~/.config/", ".pdbrc.py": "~"}


class Poetry(Module):
    name = "Poetry"

    # Configuration files
    zshrc_file = "poetry.zsh"
    symlinks: dict[str, str] = {}

    @classmethod
    def install_action(cls) -> None:
        shell.run(
            "curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python"  # noqa: E501
        )

    @classmethod
    def upgrade_action(cls) -> None:
        shell.run("poetry self update")


class Pipx(Module):
    name = "pipx"

    # Configuration files
    zshrc_file = "pipx.zsh"
    symlinks: dict[str, str] = {}

    @classmethod
    def install_action(cls) -> None:
        brew.install_or_upgrade_formula("pipx")

    @classmethod
    def upgrade_action(cls) -> None:
        brew.install_or_upgrade_formula("pipx")


class Bpython(Module):
    name = "bpython"

    # Configuration files
    zshrc_file = None
    symlinks = {"bpython": "~/.config/bpython"}

    @classmethod
    def install_action(cls) -> None:
        pipx.install_or_upgrade_package("bpython")

    @classmethod
    def upgrade_action(cls) -> None:
        pipx.install_or_upgrade_package("bpython")
