from pathlib import Path
from typing import List

from qaz.managers import git, shell
from qaz.modules.base import Module


class Vim(Module):
    name = "vim"

    # Configuration files
    zshrc_file = None
    symlinks = {".vimrc": "~"}

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        repo_path = Path.home() / ".vim/bundle/Vundle.vim"
        git.clone(
            repo_url="https://github.com/VundleVim/Vundle.vim.git", repo_path=repo_path
        )
        shell.run("vim +PluginInstall +qall")

    @classmethod
    def upgrade_action(cls):
        repo_path = Path.home() / ".vim/bundle/Vundle.vim"
        git.pull(repo_path)
        shell.run("vim +PluginInstall +qall")
