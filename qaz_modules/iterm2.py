from __future__ import annotations

from qaz.managers import brew, shell
from qaz.modules.base import Module


class ITerm2(Module):
    name = "iTerm2"
    auto_update = True

    def install_action(self) -> None:
        brew.install_or_upgrade_cask("iterm2")
        shell.run(
            "curl -L https://iterm2.com/shell_integration/zsh -o ~/.zshrc.d/.iterm2_shell_integration.zsh"  # noqa: E501
        )

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_cask("iterm2")
