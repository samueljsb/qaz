from __future__ import annotations

import subprocess
from collections.abc import Iterable, Set

from . import shell
from .base import Manager


class VSCodeExtensions(Manager):
    extensions: Iterable[str]

    def __init__(self, extensions: Iterable[str]) -> None:
        self.extensions = extensions

    def install(self) -> tuple[str, None]:
        # If VS Code is not installed, don't try to install extensions.
        if not _is_vs_code_installed():
            return "", None

        # Install extensions.
        # VS Code extensions cannot be upgraded from the command line so we skip already
        # installed extensions.
        for extension in set(self.extensions) - _get_installed_extensions():
            proc = subprocess.run(
                f"code --install-extension {extension}",
                shell=True,
                text=True,
                capture_output=True,
            )
            proc.check_returncode()

        return "", None

    def upgrade(self) -> tuple[str, str, None]:
        # Install any new extensions.
        version, proc = self.install()
        return "", version, proc


def install_extensions(extensions: Iterable[str]) -> None:
    """
    Install all currently uninstalled extensions.

    VS Code extensions cannot be upgraded from the command line so we skip already
    installed extensions for the sake of speed.
    """
    # If VS Code is not installed, don't try to install extensions.
    if not _is_vs_code_installed():
        return

    for extension in set(extensions) - _get_installed_extensions():
        shell.run(f"code --install-extension {extension}")


def _is_vs_code_installed() -> bool:
    command = shell.capture("command -v code")
    return bool(command)


def _get_installed_extensions() -> Set[str]:
    return set(shell.capture("code --list-extensions").split())
