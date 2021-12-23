from typing import Dict, List

from qaz.managers import brew, shell
from qaz.modules.base import Module


class ITerm2(Module):
    name = "iTerm2"
    auto_update = True

    # Configuration files
    zshrc_file = None
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    # Package Management
    package_manager = brew.Homebrew
    package_name = "iterm2"

    @classmethod
    def install_action(cls):
        super().install_action()
        shell.run(
            "curl -L https://iterm2.com/shell_integration/zsh -o ~/.zshrc.d/.iterm2_shell_integration.zsh"  # noqa: E501
        )
