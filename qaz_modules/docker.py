from typing import Dict, List

from qaz.managers import brew, shell
from qaz.modules.base import Module


class MacOSDocker(Module):
    name = "Docker"

    # Configuration files
    zshrc_file = "docker.zsh"
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        brew.install_or_upgrade_cask("docker")
        shell.run("open /Applications/Docker.app")

    @classmethod
    def upgrade_action(cls):
        brew.install_or_upgrade_cask("docker")


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

    @classmethod
    def install_action(cls):
        brew.install_or_upgrade_formula("jesseduffield/lazydocker/lazydocker")

    @classmethod
    def upgrade_action(cls):
        brew.install_or_upgrade_formula("jesseduffield/lazydocker/lazydocker")
