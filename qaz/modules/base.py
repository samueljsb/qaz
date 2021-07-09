from typing import Dict, List, Optional, Protocol


class Module(Protocol):
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
        vscode_extensions:  The VSCode extensions to install for working with this
                            module (optional).

    """

    name: str

    # Configuration files
    zshrc_file: Optional[str]
    symlinks: Dict[str, str]

    # Other
    vscode_extensions: List[str]

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
