from __future__ import annotations

from qaz import managers
from qaz.modules.base import Bundle
from qaz.modules.base import Module
from qaz.modules.registry import registry
from qaz.utils import shell


@registry.register
class Python(Bundle):
    name = "Python"

    managers = (
        managers.BrewFormula("pre-commit"),
        managers.BrewFormula("virtualenv"),
    )

    # Configuration files
    zshrc_files = (
        "python.zsh",
        "virtualenv.zsh",
    )
    symlinks = {
        ".pypirc": "~",
        "pythonstartup.py": "~/.config/",
        ".pdbrc.py": "~",
    }

    def install_action(self) -> None:
        shell.run("pre-commit", "init-templatedir", "~/.git-template")

    def update_action(self) -> None:
        shell.run("pre-commit", "init-templatedir", "~/.git-template")


@registry.register
class PythonLauncher(Module):
    name = "py"
    manager = managers.BrewFormula("python-launcher")
