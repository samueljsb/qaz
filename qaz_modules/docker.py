from typing import Dict, List

from qaz.managers import brew
from qaz.modules.base import Module


class MacOSDocker(Module):
    name = "Docker"
    auto_update = True

    # Configuration files
    zshrc_file = "docker.zsh"
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    # Package Management
    package_manager = brew.Homebrew
    package_name = "docker"


class LinuxDocker(Module):
    name = "Docker"

    # Configuration files
    zshrc_file = "docker.zsh"
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        # TODO
        raise NotImplementedError

    @classmethod
    def upgrade_action(cls):
        # TODO
        raise NotImplementedError


class LazyDocker(Module):
    name = "lazydocker"

    # Configuration files
    zshrc_file = None
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    # Package Management
    package_manager = brew.Homebrew
    package_name = "jesseduffield/lazydocker/lazydocker"
