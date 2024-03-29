from __future__ import annotations

from pathlib import Path
from typing import NamedTuple
from typing import Sequence

from qaz.utils import git


class Git(NamedTuple):
    repo_url: str
    repo_path: Path

    clone_options: Sequence[str] = ()
    preserve_local_changes: bool = False

    def install(self) -> None:
        git.clone(
            repo_url=self.repo_url,
            repo_path=self.repo_path,
            options=self.clone_options,
        )

    def upgrade(self) -> None:
        git.pull(self.repo_path, with_stash=self.preserve_local_changes)

    def name(self) -> str:
        __, name = self.repo_url.rsplit("/", maxsplit=1)
        return name

    def version(self) -> str:
        return git.version(self.repo_path)
