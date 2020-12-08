import os

from qaz.managers import npm
from qaz.module import Module
from qaz.modules.asdf import ASDFModule


class NodeJS(ASDFModule):
    name = "Node.js"
    plugin_name = "nodejs"
    vscode_extensions = [
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "numso.prettier-standard-vscode",
    ]

    def install_action(self) -> None:
        os.environ["NODEJS_CHECK_SIGNATURES"] = "no"
        super().install_action()


class Yarn(ASDFModule):
    name = "Yarn"
    plugin_name = "yarn"
    requires = [NodeJS()]


class NodeModule(Module):
    package_name: str
    _base_requires = [NodeJS()]

    def install_action(self) -> None:
        npm.install_or_upgrade_package(self.package_name)
        return super().install_action()

    def upgrade_action(self) -> None:
        npm.install_or_upgrade_package(self.package_name)
        return super().upgrade_action()
