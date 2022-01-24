from __future__ import annotations

from qaz.managers import brew, shell
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

    def install_action(self) -> None:
        shell.run(
            "curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python"  # noqa: E501
        )

    def upgrade_action(self) -> None:
        shell.run("poetry self update")


class PythonLauncher(Module):
    name = "py"

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("python-launcher")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("python-launcher")
