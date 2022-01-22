from __future__ import annotations

from pathlib import Path

from qaz.managers import git, shell
from qaz.modules.base import Module


class Vim(Module):
    name = "vim"

    # Configuration files
    symlinks = {".vimrc": "~"}

    # Other
    vscode_extensions: list[str] = []

    package_manager = git.Git(
        url="https://github.com/VundleVim/Vundle.vim.git",
        repo_path=Path().home() / ".vim/bundle/Vundle.vim",
    )

    @classmethod
    def install_action(cls) -> None:
        super().install_action()
        shell.run("vim +PluginInstall +qall")

    @classmethod
    def upgrade_action(cls) -> None:
        super().upgrade_action()
        shell.run("vim +PluginInstall +qall")
