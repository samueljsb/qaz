from qaz import config
from qaz.managers import brew
from qaz.module import Module
from qaz.modules.brew import Brew, BrewCaskModule
from qaz.utils import shell


class MacOS(Module):
    name = "macOS"

    def install_action(self):
        shell.run(str(config.get_root_dir() / "scripts" / "set-defaults.sh"))

    def upgrade_action(self):
        shell.run(str(config.get_root_dir() / "scripts" / "set-defaults.sh"))


class QuickLookExtensions(Module):
    name = "QuickLook"
    _base_requires = [Brew()]

    extensions = (
        "qlcolorcode",
        "qlstephen",
        "qlmarkdown",
        "suspicious-package",
    )

    def install_action(self):
        for extension in self.extensions:
            brew.install_or_upgrade_cask(extension)
        return super().install_action()

    def upgrade_action(self):
        for extension in self.extensions:
            brew.install_or_upgrade_cask(extension)
        return super().upgrade_action()


class Bartender(BrewCaskModule):
    name = "Bartender"
    cask_name = "bartender"


class Rectangle(BrewCaskModule):
    name = "Rectangle"
    cask_name = "rectangle"


# class IStats(GemModule):

#     name = "iStats"
#     gem_name = "iStats"

#     # sudo gem install iStats
#     # duso gem update iStats
