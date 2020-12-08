from pathlib import Path

from qaz.modules.git import GitModule
from qaz.utils import shell


class Vim(GitModule):
    name = "vim"
    repo_url = "https://github.com/VundleVim/Vundle.vim.git"
    repo_path = Path.home() / ".vim/bundle/Vundle.vim"
    symlinks = {".vimrc": "~"}

    def install_action(self) -> None:
        super().install_action()
        shell.run("vim +PluginInstall +qall")

    def upgrade_action(self) -> None:
        super().upgrade_action()
        shell.run("vim +PluginInstall +qall")
