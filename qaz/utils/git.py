from __future__ import annotations

from pathlib import Path

from . import shell


def clone(*, repo_url: str, repo_path: Path | str, options: str = "") -> None:
    shell.run(f"git clone {options} {repo_url} {repo_path}")


def pull(repo_path: Path | str, with_stash: bool = False) -> None:
    if with_stash:
        shell.run(f"git -C {repo_path} stash push")

    shell.run(f"git -C {repo_path} pull")

    if with_stash and shell.capture(f"git -C {repo_path} stash list"):
        shell.run(f"git -C {repo_path} stash pop")


def version(repo_path: Path | str) -> str:
    return shell.capture(
        f"git -C {repo_path} show --format='%(describe:tags)' --no-patch"
    ).strip()
