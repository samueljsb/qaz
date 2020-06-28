from sys import platform

from qaz.module import Module
from qaz.modules.brew import BrewModule
from qaz.modules.python import PipxModule
from qaz.utils import run


if platform == "darwin":

    class Docker(BrewModule):  # type: ignore
        """Docker for macOS."""

        name = "Docker"
        package_name = "docker"

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


class DockerCompose(PipxModule):
    """A tool for defining and running multi-container Docker applications."""

    name = "docker-compose"
    package_name = "docker-compose"
    requires = [Docker()]


class LazyDocker(BrewModule):
    """A simple terminal UI for both Docker and docker-compose."""

    name = "lazydocker"
    package_name = "jesseduffield/lazydocker/lazydocker"
    requires = [Docker()]
