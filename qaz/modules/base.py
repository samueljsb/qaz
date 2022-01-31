from __future__ import annotations

from collections.abc import Mapping
from types import MappingProxyType


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
