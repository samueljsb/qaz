from qaz.managers import pipx
from qaz.module import Module
from qaz.modules.asdf import ASDFModule
from qaz.modules.brew import BrewModule
from qaz.utils import shell


class Python(ASDFModule):
    name = "Python"
    plugin_name = "python"
    symlinks = {".pypirc": "~"}
    vscode_extensions = [
        "lextudio.restructuredtext",
        "ms-python.python",
        "ms-python.vscode-pylance",
        "wholroyd.jinja",
    ]


class Poetry(Module):
    name = "Poetry"
    requires = [Python()]

    # N.B. This is installed by install.sh, so no install script is needed here.

    def upgrade_action(self):
        shell.run("poetry self update")


class Pipx(BrewModule):
    name = "pipx"
    package_name = "pipx"
    requires = [Python()]


class PipxModule(Module):
    package_name: str
    _base_requires = [Pipx()]

    def install_action(self):
        pipx.install_or_upgrade_package(self.package_name)

    def upgrade_action(self):
        pipx.install_or_upgrade_package(self.package_name)


class Bpython(PipxModule):
    name = "bpython"
    package_name = "bpython"
    symlinks = {"bpython": "~/.config/bpython"}


class Tox(PipxModule):
    name = "tox"
    package_name = "tox"
