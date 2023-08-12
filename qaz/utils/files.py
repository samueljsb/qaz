from __future__ import annotations

import logging
import shutil
from pathlib import Path

from . import shell


logger = logging.getLogger(__name__)


def _determine_dest(src: Path, dest: Path | None) -> Path:
    dest = dest or Path.home()

    if dest.is_dir() and not src.is_dir():
        dest = dest / src.name

    return dest


def create_symlink(target: Path, link: Path | None = None) -> None:
    """
    Create a symlink from link to target.

    If the link is a directory and the target is a file, the link will be created at the
    same filename within the given directory.
    """
    link = link or Path.home()
    link = _determine_dest(target, link)

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
        shell.run("sudo", "ln", "-s", target.expanduser(), link.expanduser())
    except FileExistsError:
        logger.error(f"Could not create symlink because a file exists: {link}")
        return

    logger.info(f"Linked {link} -> {target}")


class NotASymlink(Exception):
    def __init__(self, link: str) -> None:
        self.link = link


def remove_symlink(target: Path, link: Path) -> None:
    link_to_remove = _determine_dest(target, link)
    if not link_to_remove.is_symlink():
        raise NotASymlink(link_to_remove)

    target = link_to_remove.resolve()

    link_to_remove.unlink()
    logger.info(f"Removed link {link} -> {target}")


def copy_file(src: Path, dest: Path) -> None:
    dest = _determine_dest(src, dest)
    shutil.copy(src, dest)

    logger.info(f"Copied file {src} -> {dest}")
