from __future__ import annotations

import json
import subprocess

from . import shell
from .base import Manager


class PipX(Manager):
    package: str

    def __init__(self, package: str) -> None:
        self.package = package

    def install(self) -> tuple[str, subprocess.CompletedProcess[str] | None]:
        # Install the package.
        try:
            proc = shell.run(f"pipx install {self.package}")
        except subprocess.CalledProcessError as exc:
            if exc.returncode == 1:  # pipx returns 1 on success
                proc = subprocess.CompletedProcess(
                    args=(exc.cmd,),
                    returncode=1,
                    stdout=exc.output,
                    stderr=exc.stderr,
                )
            else:
                raise

        return self._version(), proc

    def upgrade(self) -> tuple[str, str, subprocess.CompletedProcess[str]]:
        from_version = self._version()

        # Update the package.
        try:
            proc = shell.run(f"pipx upgrade {self.package}")
        except subprocess.CalledProcessError as exc:
            if exc.returncode == 1:  # pipx returns 1 on success
                proc = subprocess.CompletedProcess(
                    args=(exc.cmd,),
                    returncode=1,
                    stdout=exc.output,
                    stderr=exc.stderr,
                )
            else:
                raise

        return from_version, self._version(), proc

    def _version(self) -> str:
        data = json.loads(shell.capture("pipx list --json"))
        return data["venvs"][self.package]["metadata"]["main_package"][
            "package_version"
        ]
