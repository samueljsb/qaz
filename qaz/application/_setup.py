from __future__ import annotations

from pathlib import Path

from qaz import settings


def setup(root_dir: str) -> None:
    """
    Set up QAZ for the first time.

    This creates a settings file and the directory for zshrc files.
    """
    # Create settings file.
    settings.set_root_dir(root_dir)

    # Create installed dir
    zshrc_dir = Path.home().joinpath(".zshrc.d")
    zshrc_dir.mkdir(exist_ok=True)
