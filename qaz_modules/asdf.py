from __future__ import annotations

from qaz.managers import shell
from qaz.modules.base import Module


class ASDF(Module):
    name = "asdf"

    # Configuration files
    zshrc_file = "asdf.zsh"
    symlinks = {".asdfrc": "~"}

    # N.B. This is installed by install.sh, so no install script is needed here.
    def install_action(self) -> None:
        pass

    def upgrade_action(self) -> None:
        shell.run("asdf update")
