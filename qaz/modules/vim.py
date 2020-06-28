from pathlib import Path

from qaz.modules.git import GitModule
from qaz.utils import run


class Vim(GitModule):
    """My configuration and plugins for Vim."""

    name = "vim"
    repo_url = "https://github.com/VundleVim/Vundle.vim.git"
    repo_path = Path.home() / ".vim/bundle/Vundle.vim"
    symlinks = {".vimrc": "~"}

    def install_action(self) -> None:
        """Install plugins."""
        super().install_action()
        run("vim +PluginInstall +qall")

    def upgrade_action(self) -> None:
        """Install plugins."""
        super().upgrade_action()
        run("vim +PluginInstall +qall")
