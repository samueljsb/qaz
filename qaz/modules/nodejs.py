from qaz.modules.asdf import ASDFModule


class NodeJS(ASDFModule):
    """JavaScript runtime environment that executes JavaScript code outside a web browser."""

    name = "Node.js"
    plugin_name = "nodejs"


class Yarn(ASDFModule):
    """JavaScript package manager."""

    name = "Yarn"
    plugin_name = "yarn"
    dependencies = [NodeJS()]
