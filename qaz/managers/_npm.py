from __future__ import annotations

import json
from typing import NamedTuple

from qaz.utils import shell


class NPM(NamedTuple):
    package: str

    def install(self) -> None:
        self._install_or_upgrade()

    def upgrade(self) -> None:
        self._install_or_upgrade()

    def _install_or_upgrade(self) -> None:
        if self.package not in self._installed():
            shell.run("npm", "install", "--global", self.package)
        else:
            shell.run("npm", "update", "--global", self.package)

    def _installed(self) -> list[str]:
        output = shell.capture("npm", "list", "--global", "--json")
        data = json.loads(output)
        return [k for k in data.get("dependencies", {})]

    def version(self) -> str:
        data = json.loads(shell.capture("npm", "list", "--global", "--json"))
        return data["dependencies"][self.package]["version"]
