from __future__ import annotations

import subprocess
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class InstallResult:
    class Status(Enum):
        INSTALLED = "INSTALLED"
        ALREADY_INSTALLED = "ALREADY_INSTALLED"
        ERROR = "ERROR"

    status: Status
    version: str

    # Shell output
    process: subprocess.CompletedProcess

    @property
    def is_error(self) -> bool:
        return self.status == self.Status.ERROR

    @classmethod
    def installed(
        cls,
        *,
        version: str,
        process: subprocess.CompletedProcess,
    ) -> InstallResult:
        return cls(
            status=cls.Status.INSTALLED,
            version=version,
            process=process,
        )

    @classmethod
    def already_installed(
        cls,
        *,
        version: str,
    ) -> InstallResult:
        return cls(
            status=cls.Status.ALREADY_INSTALLED,
            version=version,
            process=subprocess.CompletedProcess("", 0),
        )

    @classmethod
    def error(
        cls,
        *,
        process: subprocess.CompletedProcess,
    ) -> InstallResult:
        return cls(
            status=cls.Status.ERROR,
            version="",
            process=process,
        )


@dataclass(frozen=True)
class UpgradeResult:
    class Status(Enum):
        UPGRADED = "INSTALLED"
        UP_TO_DATE = "UP_TO_DATE"
        ERROR = "ERROR"

    status: Status
    from_version: str
    to_version: str

    # Shell output
    process: subprocess.CompletedProcess

    @property
    def is_error(self) -> bool:
        return self.status == self.Status.ERROR

    @classmethod
    def upgraded(
        cls,
        *,
        from_version: str,
        to_version: str,
        process: subprocess.CompletedProcess,
    ) -> UpgradeResult:
        if from_version == to_version:
            status = cls.Status.UP_TO_DATE
        else:
            status = cls.Status.UPGRADED

        return cls(
            status=status,
            from_version=from_version,
            to_version=to_version,
            process=process,
        )

    @classmethod
    def error(
        cls,
        *,
        process: subprocess.CompletedProcess,
    ) -> UpgradeResult:
        return cls(
            status=cls.Status.ERROR,
            from_version="",
            to_version="",
            process=process,
        )


class Manager(ABC):
    @classmethod
    @abstractmethod
    def install(cls, __name: str, /) -> InstallResult:
        ...

    @classmethod
    @abstractmethod
    def upgrade(cls, __name: str, /) -> UpgradeResult:
        ...
