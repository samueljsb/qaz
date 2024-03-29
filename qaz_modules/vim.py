from __future__ import annotations

from pathlib import Path

from qaz import managers
from qaz.modules.base import Module
from qaz.modules.registry import registry
from qaz.utils import shell


@registry.register
class Vim(Module):
    name = "vim"
    manager = managers.Git(
        "https://github.com/VundleVim/Vundle.vim",
        Path.home() / ".vim/bundle/Vundle.vim",
    )

    # Configuration files
    symlinks = {
        ".vimrc": "~",
        ".editorconfig": "~",
    }

    def post_install(self) -> None:
        shell.run("vim", "+PluginInstall", "+qall")

    def post_upgrade(self) -> None:
        shell.run("vim", "+PluginInstall", "+qall")
