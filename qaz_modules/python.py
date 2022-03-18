from __future__ import annotations

from qaz.managers import brew
from qaz.modules.base import Module
from qaz.modules.registry import registry
from qaz.utils import shell


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

    @property
    def version(self) -> str:
        return shell.capture("poetry --version").strip().split()[-1]


@registry.register
class PreCommit(Module):
    name = "pre-commit"

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("pre-commit")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("pre-commit")

    @property
    def version(self) -> str:
        return brew.version("pre-commit")


@registry.register
class PythonLauncher(Module):
    name = "py"

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("python-launcher")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("python-launcher")

    @property
    def version(self) -> str:
        return brew.version("python-launcher")


@registry.register
class Virtualenv(Module):
    name = "virtualenv"

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("virtualenv")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("virtualenv")

    @property
    def version(self) -> str:
        return brew.version("virtualenv")
