from sys import platform

from qaz.module import Module
from qaz.modules.brew import BrewCaskModule, BrewModule
from qaz.utils import run


if platform == "darwin":

    class Docker(BrewCaskModule):  # type: ignore
        """Docker for macOS."""

        name = "Docker"
        cask_name = "docker"

        def install_action(self) -> None:
            """Install Docker and open the application so it starts."""
            super().install_action()
            run("open /Applications/Docker.app")


elif platform == "linux":

    class Docker(Module):  # type: ignore
        """Docker for Linux."""

        name = "Docker"

        def install_action(self) -> None:
            """TODO."""
            raise NotImplementedError

        def upgrade_action(self) -> None:
            """TODO."""
            raise NotImplementedError


class LazyDocker(BrewModule):
    """A simple terminal UI for both Docker and docker-compose."""

    name = "lazydocker"
    package_name = "jesseduffield/lazydocker/lazydocker"
    requires = [Docker()]
