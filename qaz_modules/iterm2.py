from __future__ import annotations

from qaz.managers import brew, shell
from qaz.modules.base import Module


class ITerm2(Module):
    name = "iTerm2"
    auto_update = True

    # Other
    vscode_extensions: list[str] = []

    # Package Management
    package_manager = brew.Homebrew("iterm2")

    @classmethod
    def install_action(cls) -> None:
        super().install_action()
        shell.run(
            "curl -L https://iterm2.com/shell_integration/zsh -o ~/.zshrc.d/.iterm2_shell_integration.zsh"  # noqa: E501
        )
