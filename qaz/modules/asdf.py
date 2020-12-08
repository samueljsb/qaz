from qaz.managers import asdf
from qaz.module import Module
from qaz.utils import shell


class ASDF(Module):
    name = "asdf"
    symlinks = {".asdfrc": "~"}

    # N.B. This is installed by install.sh, so no install script is needed here.

    def upgrade_action(self):
        shell.run("asdf update")


class ASDFModule(Module):
    plugin_name: str
    _base_requires = [ASDF()]

    def install_action(self):
        asdf.install_or_upgrade_plugin(self.plugin_name)
        return super().install_action()

    def upgrade_action(self):
        asdf.install_or_upgrade_plugin(self.plugin_name)
        return super().upgrade_action()
