from sys import platform

from qaz.module import Module
from qaz.modules.brew import BrewCaskModule, BrewModule
from qaz.utils import shell


if platform == "darwin":

    class Docker(BrewCaskModule):  # type: ignore
        name = "Docker"
        cask_name = "docker"

        def install_action(self) -> None:
            super().install_action()
            shell.run("open /Applications/Docker.app")


elif platform == "linux":

    class Docker(Module):  # type: ignore
        name = "Docker"

        def install_action(self) -> None:
            # TODO
            raise NotImplementedError

        def upgrade_action(self) -> None:
            # TODO
            raise NotImplementedError


class LazyDocker(BrewModule):
    name = "lazydocker"
    package_name = "jesseduffield/lazydocker/lazydocker"
    requires = [Docker()]
