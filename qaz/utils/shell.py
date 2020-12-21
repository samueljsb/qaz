import os
import subprocess
from typing import Dict, Optional

from . import output


def run(
    command: str,
    *,
    cwd: Optional[str] = None,
    allow_fail: bool = False,
    env: Dict[str, str] = None,
):
    output.command(command)

    process = subprocess.run(
        command,
        cwd=cwd,
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
