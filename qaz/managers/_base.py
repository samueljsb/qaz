from __future__ import annotations

from typing import Protocol


class Manager(Protocol):
    def install(self) -> None:
        ...

    def upgrade(self) -> None:
        ...

    def name(self) -> str:
        ...

    def version(self) -> str:
        ...
