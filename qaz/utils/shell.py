import os
import subprocess
from typing import Dict

from . import output


def run(
    command: str,
    *,
    allow_fail: bool = False,
    env: Dict[str, str] = None,
    log: bool = True
):
    if log:
        output.command(command)

    process = subprocess.run(
        command,
        shell=True,
        env=os.environ.update(env if env else {}),
    )
    if not allow_fail:
        process.check_returncode()


def capture(command: str, *, env: Dict[str, str] = None) -> str:
    process = subprocess.run(
        command,
        shell=True,
        env=os.environ.update(env if env else {}),
        text=True,
        capture_output=True,
    )
    return process.stdout
