from __future__ import annotations

from pathlib import Path

from qaz.managers import git
from qaz.managers import shell
from qaz.modules.base import Module
from qaz.modules.registry import registry


@registry.register
class Vim(Module):
    name = "vim"

    # Configuration files
    symlinks = {".vimrc": "~"}

    def install_action(self) -> None:
        repo_path = Path.home() / ".vim/bundle/Vundle.vim"
        git.clone(
            repo_url="https://github.com/VundleVim/Vundle.vim", repo_path=repo_path
        )
        shell.run("vim +PluginInstall +qall")

    def upgrade_action(self) -> None:
        repo_path = Path.home() / ".vim/bundle/Vundle.vim"
        git.pull(repo_path)
        shell.run("vim +PluginInstall +qall")

    @property
    def version(self) -> str:
        repo_path = Path.home() / ".vim/bundle/Vundle.vim"
        return git.version(repo_path)
