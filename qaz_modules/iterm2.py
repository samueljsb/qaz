from __future__ import annotations

import sys

from qaz.modules.base import Module
from qaz.modules.registry import registry
from qaz.utils import shell


class ITerm2(Module):
    name = "iTerm2"
    auto_update = True

    def install_action(self) -> None:
        shell.run(
            *("curl", "-L", "https://iterm2.com/shell_integration/zsh"),
            *("-o", "~/.zshrc.d/.iterm2_shell_integration.zsh"),
        )


if sys.platform == "darwin":
    registry.register(ITerm2)
