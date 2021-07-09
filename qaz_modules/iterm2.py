from typing import Dict, List

from qaz.managers import brew, shell
from qaz.modules.base import Module


class ITerm2(Module):
    name = "iTerm2"

    # Configuration files
    zshrc_file = None
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        brew.install_or_upgrade_cask("iterm2")
        shell.run(
            "curl -L https://iterm2.com/shell_integration/zsh -o ~/.zshrc.d/.iterm2_shell_integration.zsh"  # noqa: E501
        )

    @classmethod
    def upgrade_action(cls):
        brew.install_or_upgrade_cask("iterm2")
