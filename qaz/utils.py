import os
import subprocess
from pathlib import Path
from typing import Dict

from click import secho


def create_symlink(target: Path, link: Path = Path.home()) -> None:
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
        message(f"Linked {link} -> {target}")
    except FileExistsError:
        error(f"Could not create symlink because a file exists: {link}")


def message(msg: str) -> None:
    """Output a message on stderr.

    The message is formatted in bold.
    """
    secho(msg, bold=True, err=True)


def error(msg: str) -> None:
    """Output  an erro message on stderr.

    The message is formatted bold and red.
    """
    secho(msg, fg="red", bold=True, err=True)


def run(command: str, allow_fail: bool = False, env: Dict[str, str] = None,) -> None:
    """Run a shell command.

    Args:
        command: The command to run.
        allow_fail: If True, do not raise an exception if the command returns non-0.
        env: Key: value pairs to add to the shell's environment variables.

    Raises:
        subprocess.CalledProcessError if the return code is non-0 and allow_fail is False.

    """
    secho(f"$ {command}", bold=True, fg="yellow", err=True)
    process = subprocess.run(
        command, shell=True, env=os.environ.update(env if env else {}),
    )

    if not allow_fail:
        process.check_returncode()


def capture(command: str, env: Dict[str, str] = None) -> str:
    """Run a shell command and capture the output.

    Args:
        command: The command to run.
        env: Key: value pairs to add to the shell's environment variables.

    """
    process = subprocess.run(
        command,
        shell=True,
        env=os.environ.update(env if env else {}),
        text=True,
        capture_output=True,
    )
    return process.stdout
