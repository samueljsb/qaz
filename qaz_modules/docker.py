from __future__ import annotations

from qaz.managers import brew
from qaz.modules.base import Module
from qaz.modules.registry import register


@register
class MacOSDocker(Module):
    name = "Docker"
    auto_update = True

    # Configuration files
    zshrc_file = "docker.zsh"


@register
class LazyDocker(Module):
    name = "lazydocker"

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("jesseduffield/lazydocker/lazydocker")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("jesseduffield/lazydocker/lazydocker")
