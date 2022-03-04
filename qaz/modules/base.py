from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from types import MappingProxyType

from qaz import settings
from qaz.managers import files


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

    # Configuration files
    zshrc_file: str | None = None
    symlinks: Mapping[str, str] = MappingProxyType({})

    @property
    def zshrc_path(self) -> Path | None:
        if self.zshrc_file:
            return settings.root_dir() / "zshrc" / self.zshrc_file
        else:
            return None

    def install(self) -> None:
        self.install_action()
        self.configure()

    def upgrade(self) -> None:
        self.upgrade_action()
        self.configure()

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
        """
        Configure this module by linking settings files and running config scripts.
        """
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
