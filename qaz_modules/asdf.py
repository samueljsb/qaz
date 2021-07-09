from typing import List

from qaz.managers import shell
from qaz.modules.base import Module


class ASDF(Module):
    name = "asdf"

    # Configuration files
    zshrc_file = "asdf.zsh"
    symlinks = {".asdfrc": "~"}

    # Other
    vscode_extensions: List[str] = []

    # N.B. This is installed by install.sh, so no install script is needed here.
    @classmethod
    def install_action(cls) -> None:
        pass

    @classmethod
    def upgrade_action(cls) -> None:
        shell.run("asdf update")
