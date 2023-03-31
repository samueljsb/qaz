from __future__ import annotations

import logging
import os
import subprocess
from os import PathLike

from qaz import settings


logger = logging.getLogger(__name__)


def run(
    *args: str | PathLike[str],
    env: dict[str, str] | None = None,
) -> None:
    logger.debug("$ " + " ".join(str(part) for part in args))

    subprocess.run(
        args,
        check=True,
        env=os.environ.update(env if env else {}),
    )


def run_script(script_name: str, *args: str) -> None:
    run(settings.root_dir() / "scripts" / script_name, *args)


def capture(
    *args: str | PathLike[str],
    env: dict[str, str] | None = None,
) -> str:
    process = subprocess.run(
        args,
        env=os.environ.update(env if env else {}),
        text=True,
        capture_output=True,
    )
    return process.stdout
