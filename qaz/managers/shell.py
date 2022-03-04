from __future__ import annotations

import logging
import os
import subprocess

from qaz import settings


logger = logging.getLogger(__name__)


def run(
    command: str,
    *,
    env: dict[str, str] | None = None,
) -> None:
    logger.debug(f"$ {command}")

    process = subprocess.run(
        command,
        shell=True,
        env=os.environ.update(env if env else {}),
    )
    process.check_returncode()


def run_script(script_name: str) -> None:
    run(str(settings.root_dir() / "scripts" / script_name))


def capture(command: str, *, env: dict[str, str] | None = None) -> str:
    process = subprocess.run(
        command,
        shell=True,
        env=os.environ.update(env if env else {}),
        text=True,
        capture_output=True,
    )
    return process.stdout
