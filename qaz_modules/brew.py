from __future__ import annotations

from qaz.modules.base import Module
from qaz.modules.registry import registry
from qaz.utils import shell


@registry.register
class Homebrew(Module):
    name = "Homebrew"

    def install_action(self) -> None:
        shell.run(
            "/bin/bash -c "
            '"$(curl -fsSL '
            'https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"',
            env={"CI": "1"},
        )
        shell.run("brew analytics off")

    def upgrade_action(self) -> None:
        shell.run("brew update")
        shell.run("brew analytics off")

    @property
    def version(self) -> str:
        return shell.capture("brew --version").split("\n")[0].split()[-1]
