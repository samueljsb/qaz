from pathlib import Path

from qaz.modules.git import GitModule
from qaz.utils import shell


class Vim(GitModule):
    name = "vim"
    repo_url = "https://github.com/VundleVim/Vundle.vim.git"
    repo_path = Path.home() / ".vim/bundle/Vundle.vim"
    symlinks = {".vimrc": "~"}

    def install_action(self):
        super().install_action()
        shell.run("vim +PluginInstall +qall", suppress_output=True)

    def upgrade_action(self):
        super().upgrade_action()
        shell.run("vim +PluginInstall +qall", suppress_output=True)
