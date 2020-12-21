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
    suppress_output: bool = False
):
    output.command(command)

    process = subprocess.run(
        command,
        cwd=cwd,
        shell=True,
        env=os.environ.update(env if env else {}),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    if not suppress_output:
        # Collect each line before trying to output.
        # NOTE: this is necessary because rich.out doesn't handle printing each
        # character one at a time without a newline at the end.
        line = ""
        for char in process.stdout:
            if char == "\n":
                output.out(line)
                line = ""
                continue
            line += char

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
