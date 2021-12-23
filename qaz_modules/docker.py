from __future__ import annotations

from qaz.managers import brew
from qaz.modules.base import Module


class MacOSDocker(Module):
    name = "Docker"
    auto_update = True

    # Configuration files
    zshrc_file = "docker.zsh"
    symlinks: dict[str, str] = {}

    # Other
    vscode_extensions: list[str] = []

    # Package Management
    package_manager = brew.Homebrew("docker")


class LinuxDocker(Module):
    name = "Docker"

    # Configuration files
    zshrc_file = "docker.zsh"
    symlinks: dict[str, str] = {}

    # Other
    vscode_extensions: list[str] = []

    @classmethod
    def install_action(cls) -> None:
        # TODO
        raise NotImplementedError

    @classmethod
    def upgrade_action(cls) -> None:
        # TODO
        raise NotImplementedError


class LazyDocker(Module):
    name = "lazydocker"

    # Configuration files
    zshrc_file = None
    symlinks: dict[str, str] = {}

    # Other
    vscode_extensions: list[str] = []

    # Package Management
    package_manager = brew.Homebrew("jesseduffield/lazydocker/lazydocker")
