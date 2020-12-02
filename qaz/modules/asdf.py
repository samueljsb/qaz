from qaz.managers import asdf
from qaz.module import Module
from qaz.utils import shell


class ASDF(Module):
    """Manage multiple runtime versions with a single CLI tool."""

    name = "asdf"
    symlinks = {".asdfrc": "~"}

    # N.B. This is installed by install.sh, so no install script is needed here.

    def upgrade_action(self) -> None:
        """Update asdf."""
        shell.run("asdf update")


class ASDFModule(Module):
    """A Module which is managed by asdf.

    Attributes:
      plugin_name: The name of the asdf plugin to manage.

    """

    plugin_name: str
    _base_requires = [ASDF()]

    def install_action(self) -> None:
        """Install this package from asdf."""
        asdf.install_or_upgrade_plugin(self.plugin_name)
        return super().install_action()

    def upgrade_action(self) -> None:
        """Install this package from asdf."""
        asdf.install_or_upgrade_plugin(self.plugin_name)
        return super().upgrade_action()
