from __future__ import annotations

import datetime
from collections.abc import Mapping
from pathlib import Path
from types import MappingProxyType

from qaz import managers
from qaz import settings
from qaz.utils import files


class Module:
    """
    A module that can be installed by QAZ to manage a program or tool.

    Attrs:
        name:               This is used to identify the module.
        zshrc_file:         This is the name of the zshrc file that should be installed
                            when this module is installed (optional). If none is
                            provided, no file will be installed.
        symlinks:           Additional files that should be installed for this module.
                            This is a dictionary of config filepaths to destination
                            paths.

    """

    name: str

    manager: managers.Manager | None = None

    # Configuration files
    zshrc_file: str | None = None
    symlinks: Mapping[str, str] = MappingProxyType({})

    @property
    def is_installed(self) -> bool:
        return settings.is_module_installed(self.name)

    @is_installed.setter
    def is_installed(self, is_installed_: bool) -> None:
        if is_installed_:
            settings.set_module_installed(self.name)
        else:
            raise ValueError("It is not possible to uninstall a module")

    @property
    def last_upgraded_at(self) -> datetime.datetime | None:
        return settings.last_upgraded_at(self.name)

    @last_upgraded_at.setter
    def last_upgraded_at(self, upgraded_at: datetime.datetime) -> None:
        settings.record_module_upgraded(self.name, upgraded_at)

    @property
    def zshrc_path(self) -> Path | None:
        if self.zshrc_file:
            return settings.root_dir() / "zshrc" / self.zshrc_file
        else:
            return None

    @property
    def version(self) -> str:
        """
        Get the currently installed version.

        Returns an empty string if the module is not installed or the version cannot be
        determined.
        """
        if self.manager:
            return self.manager.version()
        else:
            return ""

    def install(self) -> None:
        if self.manager:
            self.manager.install()
        self.configure()
        self.install_action()
        self.is_installed = True

    def upgrade(self) -> None:
        if self.manager:
            self.manager.upgrade()
        self.configure()
        self.upgrade_action()
        self.last_upgraded_at = datetime.datetime.now()

    def install_action(self) -> None:
        """
        Run actions to install this module.

        Overwrite this method to provide custom install behaviour.
        """
        pass

    def upgrade_action(self) -> None:
        """
        Run actions to upgrade this module.

        Overwrite this method to provide custom upgrade behaviour.
        """
        pass

    def configure(self) -> None:
        """Configure this module by linking config files and running config scripts."""
        if self.zshrc_path:
            files.create_symlink(
                self.zshrc_path,
                Path.home() / ".zshrc.d",
            )

        for target, link in self.symlinks.items():
            files.create_symlink(
                settings.root_dir() / "configfiles" / target,
                Path(link).expanduser(),
            )
