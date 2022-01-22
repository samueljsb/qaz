from __future__ import annotations

import logging
from pathlib import Path

from . import shell
from .base import Manager


logger = logging.getLogger(__name__)


class Symlink(Manager):
    """
    Create a symlink from link to target.
    """

    target: Path
    link: Path

    def __init__(self, target: Path, link: Path = Path.home()) -> None:
        self.target = target
        self.link = link

    def install(self) -> tuple[str, None]:
        self._create_symlink()
        return "", None  # nothing useful to return

    def upgrade(self) -> tuple[str, str, None]:
        self._create_symlink()
        return "", "", None  # nothing useful to return

    def _create_symlink(self) -> None:
        """
        Create a symlink from link to target.

        If the link is a directory and the target is a file, the link will be created at
        the same filename within the given directory.
        """
        if self.link.is_dir() and not self.target.is_dir():
            link = self.link / self.target.name

        if link.is_symlink():
            if link.exists() and link.samefile(self.target):
                return
            link.unlink()

        # Ensure the destination directory exists.
        self.target.parent.mkdir(exist_ok=True)

        try:
            link.symlink_to(self.target)
        except PermissionError:
            # Run ln with sudo in a shell.
            shell.run(f"sudo ln -s {self.target.expanduser()} {link.expanduser()}")


def create_symlink(target: Path, link: Path = Path.home()) -> None:
    """
    Create a symlink from link to target.

    If the link is a directory and the target is a file, the link will be created at the
    same filename within the given directory.
    """
    if link.is_dir() and not target.is_dir():
        link = link / target.name

    if link.is_symlink():
        if link.exists() and link.samefile(target):
            return
        link.unlink()

    # Ensure the destination directory exists.
    target.parent.mkdir(exist_ok=True)

    try:
        link.symlink_to(target)
    except PermissionError:
        # Run ln with sudo in a shell.
        shell.run(f"sudo ln -s {target.expanduser()} {link.expanduser()}")
    except FileExistsError:
        logger.error(f"Could not create symlink because a file exists: {link}")
        return

    logger.info(f"Linked {link} -> {target}")
