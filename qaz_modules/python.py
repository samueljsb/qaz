from __future__ import annotations

from qaz import managers
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
class PreCommit(Module):
    name = "pre-commit"
    manager = managers.BrewFormula("pre-commit")

    def install_action(self) -> None:
        shell.run("pre-commit", "init-templatedir", "~/.git-template")

    def update_action(self) -> None:
        shell.run("pre-commit", "init-templatedir", "~/.git-template")


@registry.register
class PythonLauncher(Module):
    name = "py"
    manager = managers.BrewFormula("python-launcher")


@registry.register
class Virtualenv(Module):
    name = "virtualenv"
    manager = managers.BrewFormula("virtualenv")

    # Configuration files
    zshrc_file = "virtualenv.zsh"
