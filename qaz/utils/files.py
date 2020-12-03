from pathlib import Path

from . import output


def create_symlink(target: Path, link: Path = Path.home()):
    """Create a symlink from link to target.

    If the link is a directory and the target is a file, the link will be created at the
    same filename within the given directory

    Args:
        target: The path of the file to link to.
        link: The link to create.

    """
    if link.is_dir() and not target.is_dir():
        link = link / target.name

    if link.is_symlink():
        if link.exists() and link.samefile(target):
            return
        link.unlink()

    try:
        link.symlink_to(target)
        output.message(f"Linked {link} -> {target}")
    except FileExistsError:
        output.error(f"Could not create symlink because a file exists: {link}")