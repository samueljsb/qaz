from __future__ import annotations

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
            shell.run(f"code --install-extension {extension}")

        return "", None

    def upgrade(self) -> tuple[str, str, None]:
        # Install any new extensions.
        version, proc = self.install()
        return "", version, proc


def _is_vs_code_installed() -> bool:
    command = shell.capture("command -v code")
    return bool(command)


def _get_installed_extensions() -> Set[str]:
    return set(shell.capture("code --list-extensions").split())
