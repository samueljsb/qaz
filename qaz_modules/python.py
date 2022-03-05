from __future__ import annotations

from qaz.managers import brew, shell
from qaz.modules.base import Module
from qaz.modules.registry import registry


@registry.register
class Python(Module):
    name = "Python"

    # Configuration files
    zshrc_file = "python.zsh"
    symlinks = {".pypirc": "~", "pythonstartup.py": "~/.config/", ".pdbrc.py": "~"}


@registry.register
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


@registry.register
class PreCommit(Module):
    name = "pre-commit"

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("pre-commit")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("pre-commit")


@registry.register
class PythonLauncher(Module):
    name = "py"

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("python-launcher")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("python-launcher")
