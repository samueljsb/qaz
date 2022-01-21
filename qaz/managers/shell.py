from __future__ import annotations

import logging
import os
import subprocess
from pathlib import Path

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
    cwd: str | Path | None = None,
    allow_fail: bool = False,
    env: dict[str, str] = None,
):
    logger.debug(f"$ {command}")

    process = subprocess.run(
        command,
        cwd=cwd,
        shell=True,
        env=os.environ.update(env if env else {}),
    )
    if not allow_fail:
        if process.returncode == 127:
            raise CommandNotFound(f"Command '{command.split()[0]}' not found.")
        process.check_returncode()


def run_script(script_name: str) -> None:
    run(str(settings.get_root_dir() / "scripts" / script_name))


def capture(command: str, *, env: dict[str, str] = None) -> str:
    process = subprocess.run(
        command,
        shell=True,
        env=os.environ.update(env if env else {}),
        text=True,
        capture_output=True,
    )
    return process.stdout
