from __future__ import annotations

import subprocess
from pathlib import Path

from . import shell
from .base import Manager


class Git(Manager):
    url: str
    repo_path: Path
    options: str

    def __init__(self, url: str, repo_path: Path, options: str = "") -> None:
        self.url = url
        self.repo_path = repo_path
        self.options = options

    def install(self) -> tuple[str, subprocess.CompletedProcess[str] | None]:
        # Clone the repo.
        proc = subprocess.run(
            f"git clone {self.options} {self.url} {self.repo_path}",
            shell=True,
            text=True,
            capture_output=True,
        )
        proc.check_returncode()

        return self._commit_sha(), proc

    def upgrade(self) -> tuple[str, str, subprocess.CompletedProcess[str]]:
        from_sha = self._commit_sha()

        # Pull the repo.
        proc = subprocess.run(
            f"git -C {self.repo_path} pull",
            shell=True,
            text=True,
            capture_output=True,
        )
        proc.check_returncode()

        return from_sha, self._commit_sha(), proc

    def _commit_sha(self) -> str:
        reference = shell.capture(
            f"git -C {self.repo_path} show --format=reference --no-patch"
        )
        return reference.split()[0]
