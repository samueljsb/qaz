import os

from qaz.modules.asdf import ASDFModule


class NodeJS(ASDFModule):
    """JavaScript runtime environment that executes JavaScript code outside a web browser."""

    name = "Node.js"
    plugin_name = "nodejs"

    def install_action(self) -> None:
        """Do not check downloads against OpenPGP signatures."""
        os.environ["NODEJS_CHECK_SIGNATURES"] = "no"
        super().install_action()


class Yarn(ASDFModule):
    """JavaScript package manager."""

    name = "Yarn"
    plugin_name = "yarn"
    dependencies = [NodeJS()]
