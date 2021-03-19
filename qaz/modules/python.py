from sys import platform

from qaz.managers import pip, pipx
from qaz.module import Module
from qaz.modules.asdf import ASDFModule
from qaz.modules.brew import BrewModule
from qaz.utils import shell


class Python(ASDFModule):
    name = "Python"
    plugin_name = "python"
    symlinks = {".pypirc": "~", "pythonstartup.py": "~/.config/", ".pdbrc.py": "~"}
    vscode_extensions = [
        "lextudio.restructuredtext",
        "ms-python.python",
        "ms-python.vscode-pylance",
        "wholroyd.jinja",
    ]

    def install_action(self):
        super().install_action()
        pip.install_or_upgrade_package("pip")
        if platform == "darwin":
            pip.install_or_upgrade_package("gnureadline")

    def upgrade_action(self):
        super().upgrade_action()
        pip.install_or_upgrade_package("pip")
        if platform == "darwin":
            pip.install_or_upgrade_package("gnureadline")


class Poetry(Module):
    name = "Poetry"
    requires = [Python()]

    # N.B. This is installed by install.sh, so no install script is needed here.

    def upgrade_action(self):
        shell.run("poetry self update")


class PipModule(Module):
    package_name: str
    _base_requires = [Python()]

    def install_action(self):
        pip.install_or_upgrade_package(self.package_name)

    def upgrade_action(self):
        pip.install_or_upgrade_package(self.package_name)


class Rich(PipModule):
    name = "rich"
    package_name = "rich"


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
