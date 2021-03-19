from pathlib import Path
from typing import Dict, List, Optional, Union

from qaz import config
from qaz.managers import code
from qaz.utils import files, shell


PathLike = Union[Path, str]


class DependenciesMissing(Exception):
    def __init__(self, dependencies: List[str]):
        self.dependencies = dependencies

    def __str__(self) -> str:
        return f"Dependencies missing: {', '.join(self.dependencies)}."


class NotInstalled(Exception):
    pass


class Module:
    # Attributes to overwrite
    name: str
    zshrc_file: Optional[str] = None
    symlinks: Dict[PathLike, PathLike] = dict()
    requires: List["Module"] = list()
    vscode_extensions: List[str] = list()

    # Internal attributes
    _base_requires: Optional[List["Module"]] = None

    def __init__(self):
        # base requirements
        self.requires = self.requires + (self._base_requires or [])

        return super().__init_subclass__()

    def install(self):
        if self.is_installed:
            return

        self._check_dependencies()

        self.install_action()
        self._link_zshrc()
        self._create_symlinks()
        self._install_vscode_extensions()

        self.set_installed()

    def install_action(self):
        """
        Run actions to install this module.

        Overwrite this method to provide custom install behaviour.
        """
        pass

    def upgrade(self):
        if not self.is_installed:
            raise NotInstalled(f"Cannot upgrade: {self.name} is not installed")

        self._check_dependencies()

        self._link_zshrc()
        self._create_symlinks()
        self._install_vscode_extensions()
        self.upgrade_action()

    def upgrade_action(self):
        """
        Run actions to upgrade this module.

        Overwrite this method to provide custom upgrade behaviour.
        """
        pass

    @property
    def is_installed(self) -> bool:
        return config.is_module_installed(self.name)

    def set_installed(self):
        config.set_module_installed(self.name)

    def _check_dependencies(self):
        """
        Check all dependencies are installed.
        """
        if missing := [
            dep for dep in self.requires if not config.is_module_installed(dep.name)
        ]:
            raise DependenciesMissing([dep.name for dep in missing])

    def _link_zshrc(self):
        """
        Create symlink from ~/.zshrc.d to the zshrc file for this module.
        """
        zshrc_fname = self.zshrc_file or f"{self.name.lower()}.zsh"
        zshrc_path = config.get_root_dir() / "zshrc" / zshrc_fname
        if zshrc_path.exists():
            files.create_symlink(
                zshrc_path,
                Path.home() / ".zshrc.d",
            )

    def _create_symlinks(self):
        for _target, _link in self.symlinks.items():
            files.create_symlink(
                config.get_root_dir() / "configfiles" / _target,
                Path(_link).expanduser(),
            )

    def _install_vscode_extensions(self):
        command = shell.capture("command -v code")
        if not command or not self.vscode_extensions:
            return

        code.install_extensions(self.vscode_extensions)
