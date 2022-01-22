from __future__ import annotations

import logging
import os
import subprocess

from qaz import settings


logger = logging.getLogger(__name__)


class CommandNotFound(Exception):
    """
    The given command was not found.
    """

    pass


def run(
    command: str,
    *,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    env = env or {}

    # Run the command.
    logger.debug(f"$ {command}")
    process = subprocess.run(
        command,
        env=os.environ.update(env),
        shell=True,
        text=True,
        capture_output=True,
    )

    # Log stderr if the process failed.
    try:
        process.check_returncode()
    except Exception:
        logger.error(process.stderr)
        raise

    return process


def run_script(script_name: str) -> None:
    run(str(settings.get_root_dir() / "scripts" / script_name))


def capture(command: str, *, env: dict[str, str] | None = None) -> str:
    process = subprocess.run(
        command,
        shell=True,
        env=os.environ.update(env if env else {}),
        text=True,
        capture_output=True,
    )
    return process.stdout
