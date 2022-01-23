from __future__ import annotations

from qaz.managers import brew
from qaz.modules.base import Module


class MacOSDocker(Module):
    name = "Docker"
    auto_update = True

    # Configuration files
    zshrc_file = "docker.zsh"

    def install_action(self) -> None:
        brew.install_or_upgrade_cask("docker")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_cask("docker")


class LinuxDocker(Module):
    name = "Docker"

    # Configuration files
    zshrc_file = "docker.zsh"

    def install_action(self) -> None:
        # TODO
        raise NotImplementedError

    def upgrade_action(self) -> None:
        # TODO
        raise NotImplementedError


class LazyDocker(Module):
    name = "lazydocker"

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("jesseduffield/lazydocker/lazydocker")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("jesseduffield/lazydocker/lazydocker")
