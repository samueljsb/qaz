from pathlib import Path
from typing import Dict, List, Optional, Union

from qaz.config import ModuleConfig, config
from qaz.managers import code
from qaz.utils import files, output, shell


PathLike = Union[Path, str]


class DependenciesMissing(Exception):
    """Error raised when dependencies of a module are not installed."""

    def __init__(self, dependencies: List[str]) -> None:
        self.dependencies = dependencies

    def __str__(self) -> str:
        return f"Dependencies missing: {', '.join(self.dependencies)}."


class Module:
    """A module to be installed.

    Each module contains configuration and install/upgrade methods for one topic.

    Attributes:
        name (req'd): The module name. This should also be the folder containing it.
        config_file: The name of the zsh config file for this module.
        symlinks: A mapping of file (in `dotfiles/`) to the location of the symlink that should be created.
        requires: The modules that need to be installed before this one.

    """

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
        self._zshrc_path = config.root_dir / "zshrc" / zshrc_fname

        # base requirements
        self.requires = self.requires + (self._base_requires or [])

        return super().__init_subclass__()

    def install(self, install_dependencies: bool = False) -> None:
        """Install the module.

        Args:
            install_dependencies: Install this modules dependencies if they are not installed.

        Raises:
            DependenciesMissing if a dependency is not installed and install_dependencies is False.
            ModuleDoesNotExist if a dependency cannot be found.

        """
        module_config = self._get_config()
        output.message(f"Installing {self.name}...")
        if module_config.installed:
            output.message(f"... {self.name} already installed!")
            return

        self._check_dependencies(install_dependencies=install_dependencies)

        self.install_action()
        self._link_zshrc()
        self._create_symlinks()
        self._install_vscode_extensions()

        module_config.installed = True
        output.message(f"... {self.name} installed!")

        self._save_config(module_config)

    def install_action(self) -> None:
        """Run actions to install this module.

        Overwrite this method to provide custom install behaviour.
        """
        pass

    def upgrade(self) -> None:
        """Upgrade this module."""
        if not self._get_config().installed:
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
        """Run actions to upgrade this module.

        Overwrite this method to provide custom upgrade behaviour.
        """
        pass

    def _get_config(self) -> ModuleConfig:
        """Get the configuration for this module."""
        return config.get_module(self.name)

    def _save_config(self, module_config: ModuleConfig) -> None:
        """Save the configuration for this module.

        Args:
            module_config: The configuration to save.

        """
        config.modules[self.name] = module_config
        config.save()

    def _check_dependencies(self, install_dependencies: bool = False) -> None:
        """Check all dependencies are installed.

        Args:
            install_dependencies: Install missing dependencies.

        Raises:
            DependenciesMissing if a dependency is not installed and install_dependencies is False.
            ModuleDoesNotExist if a dependency cannot be found.

        """
        if missing := [
            dep for dep in self.requires if dep.name not in config.installed_modules
        ]:
            if install_dependencies:
                for module in missing:
                    module.install(install_dependencies=True)
            else:
                raise DependenciesMissing([dep.name for dep in missing])

    def _link_zshrc(self) -> None:
        """Create symlink from ~/.zshrc.d to the zshrc file for this module."""
        if self._zshrc_path.exists():
            files.create_symlink(
                self._zshrc_path,
                Path.home() / ".zshrc.d",
            )

    def _create_symlinks(self) -> None:
        """Create symlinks for this module."""
        for _target, _link in self.symlinks.items():
            files.create_symlink(
                config.root_dir / "configfiles" / _target, Path(_link).expanduser()
            )

    def _install_vscode_extensions(self) -> None:
        """Install VS Code extensions for this module."""
        command = shell.capture("command -v code")
        if not command or not self.vscode_extensions:
            return

        output.message("Installing VS Code extensions...")
        code.install_extensions(self.vscode_extensions)
        output.message("... VS Code extensions installed!")
