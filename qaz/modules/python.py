from qaz.managers import pipx
from qaz.module import Module
from qaz.modules.asdf import ASDFModule
from qaz.modules.brew import BrewModule
from qaz.utils import shell


class Python(ASDFModule):
    """An interpreted, high-level, general-purpose programming language.

    Extras are assorted packages for managing Python, incl. formatters, linters, and a
    fancy interpreter.
    """

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
    """Python dependency management and packaging made easy."""

    name = "Poetry"
    requires = [Python()]

    # N.B. This is installed by install.sh, so no install script is needed here.

    def upgrade_action(self) -> None:
        """Update poetry through its own command."""
        shell.run("poetry self update")


class Pipx(BrewModule):
    """Install and run Python applications in isolated environments."""

    name = "pipx"
    package_name = "pipx"
    requires = [Python()]


class PipxModule(Module):
    """A Module which is managed by pipx.

    Attributes:
      package_name: The name of the package to install.

    """

    package_name: str
    _base_requires = [Pipx()]

    def install_action(self) -> None:
        """Install this package from Pipx."""
        pipx.install_or_upgrade_package(self.package_name)

    def upgrade_action(self) -> None:
        """Upgrade this package from Homebrew."""
        pipx.install_or_upgrade_package(self.package_name)


class Bpython(PipxModule):
    """A fancy interface to the Python interpreter."""

    name = "bpython"
    package_name = "bpython"
    symlinks = {"bpython": "~/.config/bpython"}


class Tox(PipxModule):
    """A generic virtualenv management and test command line tool."""

    name = "tox"
    package_name = "tox"
