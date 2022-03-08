from __future__ import annotations

from qaz.managers import brew
from qaz.modules.base import Module
from qaz.modules.registry import registry


@registry.register
class MacOSDocker(Module):
    name = "Docker"
    auto_update = True

    # Configuration files
    zshrc_file = "docker.zsh"


@registry.register
class LazyDocker(Module):
    name = "lazydocker"

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("jesseduffield/lazydocker/lazydocker")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("jesseduffield/lazydocker/lazydocker")

    @property
    def version(self) -> str:
        return brew.version("jesseduffield/lazydocker/lazydocker")
