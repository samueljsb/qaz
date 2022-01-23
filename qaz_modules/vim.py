from __future__ import annotations

from pathlib import Path

from qaz.managers import git, shell
from qaz.modules.base import Module


class Vim(Module):
    name = "vim"

    # Configuration files
    symlinks = {".vimrc": "~"}

    def install_action(self) -> None:
        repo_path = Path.home() / ".vim/bundle/Vundle.vim"
        git.clone(
            repo_url="https://github.com/VundleVim/Vundle.vim.git", repo_path=repo_path
        )
        shell.run("vim +PluginInstall +qall")

    def upgrade_action(self) -> None:
        repo_path = Path.home() / ".vim/bundle/Vundle.vim"
        git.pull(repo_path)
        shell.run("vim +PluginInstall +qall")
