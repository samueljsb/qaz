from pathlib import Path
from typing import Union

from . import shell


def clone(*, repo_url: str, repo_path: Union[Path, str], options: str = "") -> None:
    shell.run(f"git clone {options} {repo_url} {repo_path}")


def pull(repo_path: Union[Path, str]) -> None:
    shell.run(f"git -C {repo_path} pull")
