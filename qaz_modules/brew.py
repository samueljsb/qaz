from typing import Dict, List

from qaz.managers import shell
from qaz.modules.base import Module


class Homebrew(Module):
    name = "Homebrew"

    # Configuration files
    zshrc_file = None
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        shell.run(
            "/bin/bash -c "
            '"$(curl -fsSL '
            'https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"',
            env={"CI": "1"},
        )
        shell.run("brew analytics off")

    @classmethod
    def upgrade_action(cls):
        shell.run("brew update")
        shell.run("brew analytics off")
