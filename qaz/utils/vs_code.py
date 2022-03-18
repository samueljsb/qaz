from __future__ import annotations

from collections.abc import Iterable
from collections.abc import Set

from . import shell


def install_extensions(extensions: Iterable[str]) -> None:
    """
    Install all currently uninstalled extensions.

    VS Code extensions cannot be upgraded from the command line so we skip already
    installed extensions for the sake of speed.
    """
    # If VS Code is not installed, don't try to install extensions.
    if not _is_vs_code_installed():
        return

    for extension in {ext.casefold() for ext in extensions} - _installed_extensions():
        shell.run(f"code --install-extension {extension}")


def _is_vs_code_installed() -> bool:
    command = shell.capture("command -v code")
    return bool(command)


def _installed_extensions() -> Set[str]:
    return {ext.casefold() for ext in shell.capture("code --list-extensions").split()}
