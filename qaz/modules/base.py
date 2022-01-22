from __future__ import annotations

from typing import Protocol


class Module(Protocol):
    """
    A module that can be installed by QAZ to manage a program or tool.

    Attrs:
        name:               This is used to identify the module.
        auto_update:        Whether this module updates itself. Defaults to False (i.e.
                            it should be upgraded by QAZ).
        zshrc_file:         This is the name of the zshrc file that should be installed
                            when this module is installed (optional). If none is
                            provided, no file will be installed.
        symlinks:           Additional files that should be installed for this module.
                            This is a dictionary of config filepaths to destination
                            paths.

    """

    name: str
    auto_update: bool = False
    is_language: bool = False

    # Configuration files
    zshrc_file: str | None
    symlinks: dict[str, str]

    @classmethod
    def install_action(cls) -> None:
        """
        Run actions to install this module.

        Overwrite this method to provide custom install behaviour.
        """
        ...

    @classmethod
    def upgrade_action(cls) -> None:
        """
        Run actions to upgrade this module.

        Overwrite this method to provide custom upgrade behaviour.
        """
        ...
