from __future__ import annotations

from pathlib import Path
from typing import NamedTuple

from qaz.utils import git


class Git(NamedTuple):
    repo_url: str
    repo_path: Path

    clone_options: str = ""
    preserve_local_changes: bool = False

    def install(self) -> None:
        git.clone(
            repo_url=self.repo_url,
            repo_path=self.repo_path,
            options=self.clone_options,
        )

    def upgrade(self) -> None:
        git.pull(self.repo_path, with_stash=self.preserve_local_changes)

    def version(self) -> str:
        return git.version(self.repo_path)
