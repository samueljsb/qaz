from __future__ import annotations

import os.path

from qaz import managers
from qaz.modules.base import Bundle
from qaz.modules.base import Module
from qaz.modules.registry import registry
from qaz.utils import shell


@registry.register
class Python(Bundle):
    name = "Python"

    managers = (
        managers.Pip("aactivator"),
        managers.Pip("pre-commit"),
        managers.Pip("tox"),
        managers.Pip("twine"),
        managers.Pip("virtualenv"),
    )

    # Configuration files
    zshrc_files = (
        "aactivator.zsh",
        "python.zsh",
    )
    symlinks = {
        ".pypirc": "~",
        "pythonstartup.py": "~/.config/",
        ".pdbrc.py": "~",
    }

    def post_install(self) -> None:
        shell.run(
            "pre-commit",
            "init-templatedir",
            os.path.expanduser("~/.local/share/git-core/templates"),
        )

    def pre_upgrade(self) -> None:
        managers.Pip("pip", executables=[]).upgrade()

    def post_upgrade(self) -> None:
        shell.run(
            "pre-commit",
            "init-templatedir",
            os.path.expanduser("~/.local/share/git-core/templates"),
        )


@registry.register
class PythonLauncher(Module):
    name = "py"
    manager = managers.BrewFormula("python-launcher")
