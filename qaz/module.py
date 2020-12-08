from pathlib import Path
from typing import Dict, List, Optional, Union

from qaz import config
from qaz.managers import code
from qaz.utils import files, output, shell


PathLike = Union[Path, str]


class DependenciesMissing(Exception):
    def __init__(self, dependencies: List[str]) -> None:
        self.dependencies = dependencies

    def __str__(self) -> str:
        return f"Dependencies missing: {', '.join(self.dependencies)}."


class Module:
    # Attributes to overwrite
    name: str
    zshrc_file: Optional[str] = None
    symlinks: Dict[PathLike, PathLike] = dict()
    requires: List["Module"] = list()
    vscode_extensions: List[str] = list()

    # Internal attributes
    _zshrc_path: Path
    _base_requires: Optional[List["Module"]] = None

    def __init__(self) -> None:
        # .zshrc file
        zshrc_fname = self.zshrc_file or f"{self.name.lower()}.zsh"
        self._zshrc_path = config.get_root_dir() / "zshrc" / zshrc_fname

        # base requirements
        self.requires = self.requires + (self._base_requires or [])

        return super().__init_subclass__()

    def install(self):
        output.message(f"Installing {self.name}...")
        if self.is_installed:
            output.message(f"... {self.name} already installed!")
            return

        self._check_dependencies()

        self.install_action()
        self._link_zshrc()
        self._create_symlinks()
        self._install_vscode_extensions()

        self.set_installed()
        output.message(f"... {self.name} installed!")

    def install_action(self) -> None:
        """
        Run actions to install this module.

        Overwrite this method to provide custom install behaviour.
        """
        pass

    def upgrade(self) -> None:
        if not self.is_installed:
            output.error(f"Cannot upgrade: {self.name} is not installed")
            return

        output.message(f"Upgrading {self.name}...")

        self._check_dependencies()

        self._link_zshrc()
        self._create_symlinks()
        self._install_vscode_extensions()
        self.upgrade_action()

        output.message(f"... {self.name} upgraded!")

    def upgrade_action(self) -> None:
        """
        Run actions to upgrade this module.

        Overwrite this method to provide custom upgrade behaviour.
        """
        pass

    @property
    def is_installed(self) -> bool:
        return config.is_module_installed(self.name)

    def set_installed(self):
        config.set_module_installed(self.name, True)

    def _check_dependencies(self):
        """
        Check all dependencies are installed.
        """
        if missing := [
            dep for dep in self.requires if not config.is_module_installed(dep.name)
        ]:
            raise DependenciesMissing([dep.name for dep in missing])

    def _link_zshrc(self) -> None:
        """
        Create symlink from ~/.zshrc.d to the zshrc file for this module.
        """
        if self._zshrc_path.exists():
            files.create_symlink(
                self._zshrc_path,
                Path.home() / ".zshrc.d",
            )

    def _create_symlinks(self) -> None:
        for _target, _link in self.symlinks.items():
            files.create_symlink(
                config.get_root_dir() / "configfiles" / _target,
                Path(_link).expanduser(),
            )

    def _install_vscode_extensions(self) -> None:
        command = shell.capture("command -v code")
        if not command or not self.vscode_extensions:
            return

        output.message("Installing VS Code extensions...")
        code.install_extensions(self.vscode_extensions)
        output.message("... VS Code extensions installed!")
