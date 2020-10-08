import os

from qaz.managers import npm
from qaz.module import Module
from qaz.modules.asdf import ASDFModule


class NodeJS(ASDFModule):
    """JavaScript runtime environment that executes JavaScript code outside a web browser."""

    name = "Node.js"
    plugin_name = "nodejs"
    vscode_extensions = [
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "numso.prettier-standard-vscode",
    ]

    def install_action(self) -> None:
        """Do not check downloads against OpenPGP signatures."""
        os.environ["NODEJS_CHECK_SIGNATURES"] = "no"
        super().install_action()


class Yarn(ASDFModule):
    """JavaScript package manager."""

    name = "Yarn"
    plugin_name = "yarn"
    requires = [NodeJS()]


class NodeModule(Module):
    """A Module which is managed by NPM.

    Attributes:
      package_name: The name of the package to manage.

    """

    package_name: str
    _base_requires = [NodeJS()]

    def install_action(self) -> None:
        """Install this package from Homebrew."""
        npm.install_or_upgrade(self.package_name)
        return super().install_action()

    def upgrade_action(self) -> None:
        """Upgrade this package from Homebrew."""
        npm.install_or_upgrade(self.package_name)
        return super().upgrade_action()
