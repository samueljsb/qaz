from pathlib import Path

from . import output, shell


def create_symlink(target: Path, link: Path = Path.home()):
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
        output.error(f"Could not create symlink because a file exists: {link}")
        return

    output.message(f"Linked {link} -> {target}")
