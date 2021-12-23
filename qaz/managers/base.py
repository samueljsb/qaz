from __future__ import annotations

import subprocess
from abc import ABC, abstractmethod


class Manager(ABC):
    @abstractmethod
    def install(self) -> tuple[str, subprocess.CompletedProcess[str] | None]:
        """
        Install the package.

        Returns the version that has been installed and the process that installed it.
        """
        ...

    @abstractmethod
    def upgrade(self) -> tuple[str, str, subprocess.CompletedProcess[str] | None]:
        """
        Upgrade the package.

        Returns the previous and new versions of the package and the process that
        upgraded it.
        """
        ...
