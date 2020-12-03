from qaz.modules.brew import BrewCaskModule
from qaz.utils import shell


class ITerm2(BrewCaskModule):
    """A terminal emulator for macOS that does amazing things."""

    name = "iTerm2"
    cask_name = "iterm2"

    def install_action(self) -> None:
        """Install iTerm2 and run download integration script."""
        super().install_action()
        shell.run(
            "curl -L https://iterm2.com/shell_integration/zsh -o ~/.zshrc.d/.iterm2_shell_integration.zsh"  # noqa: E501
        )
