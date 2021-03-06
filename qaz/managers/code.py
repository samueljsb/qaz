from typing import Iterable, Set

from qaz.utils import shell


def install_extensions(extensions: Iterable[str]):
    """
    Install all currently uninstalled extensions.

    VSCode extensions cannot be upgraded from the command line so we skip already
    installed extensions for the sake of speed.
    """
    for extension in set(extensions) - _get_installed_extensions():
        shell.run(f"code --install-extension {extension}")


def _get_installed_extensions() -> Set[str]:
    return set(shell.capture("code --list-extensions").split())
