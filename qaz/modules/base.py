from __future__ import annotations

import abc
import datetime
import logging
from collections.abc import Mapping
from pathlib import Path
from types import MappingProxyType
from typing import Sequence

from qaz import settings
from qaz.managers import Manager
from qaz.utils import files


logger = logging.getLogger(__name__)


class ModuleBase(abc.ABC):
    """
    A module that can be installed by QAZ to manage a program or tool.
    """

    name: str

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
    def versions(self) -> dict[str, str]:  # name: version
        """
        Get the currently installed versions of the tools this module installs.
        """
        return {}

    def install(self) -> None:
        self.pre_install()
        self._install()
        self.configure()
        self.post_install()
        self.is_installed = True

    @abc.abstractmethod
    def _install(self) -> None:
        ...

    def pre_install(self) -> None:  # default no-op  # noqa: B027
        """
        Run actions before this module has been installed.

        Overwrite this method to provide custom install behaviour.
        """
        pass

    def post_install(self) -> None:  # default no-op  # noqa: B027
        """
        Run actions after this module has been installed.

        Overwrite this method to provide custom install behaviour.
        """
        pass

    def upgrade(self) -> None:
        self.pre_upgrade()
        self._upgrade()
        self.configure()
        self.post_upgrade()
        self.last_upgraded_at = datetime.datetime.now()

    @abc.abstractmethod
    def _upgrade(self) -> None:
        ...

    def pre_upgrade(self) -> None:  # default no-op  # noqa: B027
        """
        Run actions aftbeforeer this module has been upgraded.

        Overwrite this method to provide custom upgrade behaviour.
        """
        pass

    def post_upgrade(self) -> None:  # default no-op  # noqa: B027
        """
        Run actions after this module has been upgraded.

        Overwrite this method to provide custom upgrade behaviour.
        """
        pass

    def configure(self) -> None:
        """Configure this module by linking config files and running config scripts."""
        for target, link in self.symlinks.items():
            files.create_symlink(
                settings.root_dir() / "configfiles" / target,
                Path(link).expanduser(),
            )

    def unconfigure(self) -> None:
        for target, link in self.symlinks.items():
            try:
                files.remove_symlink(
                    settings.root_dir() / "configfiles" / target,
                    Path(link).expanduser(),
                )
            except files.NotASymlink as exc:
                logger.warn(f"Skipping {exc.link}: no symlink found")
                continue

            files.copy_file(
                settings.root_dir() / "configfiles" / target,
                Path(link).expanduser(),
            )


class Module(ModuleBase):
    """A module that provides a single tool."""

    manager: Manager | None = None
    zshrc_file: str | None = None

    @property
    def versions(self) -> dict[str, str]:
        if self.manager:
            return {self.manager.name(): self.manager.version()}
        else:
            return {}

    def _install(self) -> None:
        if self.manager:
            self.manager.install()

    def _upgrade(self) -> None:
        if self.manager:
            self.manager.upgrade()

    def configure(self) -> None:
        """Configure this module by linking config files and running config scripts."""
        if self.zshrc_file:
            zshrc_path = settings.root_dir() / "zshrc" / self.zshrc_file
            files.create_symlink(
                zshrc_path,
                Path.home() / ".zshrc.d",
            )

        super().configure()

    def unconfigure(self) -> None:
        if self.zshrc_file:
            zshrc_path = settings.root_dir() / "zshrc" / self.zshrc_file
            try:
                files.remove_symlink(
                    zshrc_path,
                    Path.home() / ".zshrc.d",
                )
            except files.NotASymlink as exc:
                logger.warn(f"Skipping {exc.link}: no symlink found")
            else:
                files.copy_file(
                    zshrc_path,
                    Path.home() / ".zshrc.d",
                )

        super().unconfigure()


class Bundle(ModuleBase):
    """A module that bundles together several tools."""

    managers: Sequence[Manager] = ()

    zshrc_files: Sequence[str] = ()

    @property
    def versions(self) -> dict[str, str]:
        return {manager.name(): manager.version() for manager in self.managers}

    def _install(self) -> None:
        for manager in self.managers:
            manager.install()

    def _upgrade(self) -> None:
        for manager in self.managers:
            manager.upgrade()

    def configure(self) -> None:
        """Configure this module by linking config files and running config scripts."""
        for rc_file in self.zshrc_files:
            rc_path = settings.root_dir() / "zshrc" / rc_file
            files.create_symlink(
                rc_path,
                Path.home() / ".zshrc.d",
            )

        super().configure()

    def unconfigure(self) -> None:
        for rc_file in self.zshrc_files:
            rc_path = settings.root_dir() / "zshrc" / rc_file
            try:
                files.remove_symlink(
                    rc_path,
                    Path.home() / ".zshrc.d",
                )
            except files.NotASymlink as exc:
                logger.warn(f"Skipping {exc.link}: no symlink found")
                continue

            files.copy_file(
                rc_path,
                Path.home() / ".zshrc.d",
            )

        super().unconfigure()
