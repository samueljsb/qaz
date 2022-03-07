from __future__ import annotations

from pathlib import Path

from . import shell


def clone(*, repo_url: str, repo_path: Path | str, options: str = "") -> None:
    shell.run(f"git clone {options} {repo_url} {repo_path}")


def pull(repo_path: Path | str) -> None:
    shell.run(f"git -C {repo_path} pull")


def version(repo_path: Path | str) -> str:
    return shell.capture(
        f"git -C {repo_path} show --format='%(describe:tags)' --no-patch"
    ).strip()
