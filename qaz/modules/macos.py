from qaz.config import legacy_config as config
from qaz.managers import brew
from qaz.module import Module
from qaz.modules.brew import Brew, BrewCaskModule
from qaz.utils import shell


class MacOS(Module):
    """My configuration for macOS."""

    name = "macOS"

    def install_action(self) -> None:
        """Run the script to set defaults."""
        shell.run(str(config.root_dir / "scripts" / "set-defaults.sh"))

    def upgrade_action(self) -> None:
        """Run the script to set defaults."""
        shell.run(str(config.root_dir / "scripts" / "set-defaults.sh"))


class QuickLookExtensions(Module):
    """Extensions for MacOS QuickLook."""

    name = "QuickLook"
    _base_requires = [Brew()]

    extensions = (
        "qlcolorcode",
        "qlstephen",
        "qlmarkdown",
        "suspicious-package",
    )

    def install_action(self) -> None:
        """Install this cask from Homebrew."""
        for extension in self.extensions:
            brew.install_or_upgrade_cask(extension)
        return super().install_action()

    def upgrade_action(self) -> None:
        """Upgrade this cask from Homebrew."""
        for extension in self.extensions:
            brew.install_or_upgrade_cask(extension)
        return super().upgrade_action()


class Bartender(BrewCaskModule):
    """Menu bar icon organizer."""

    name = "Bartender"
    cask_name = "bartender"


class Rectangle(BrewCaskModule):
    """Move and resize windows using keyboard shortcuts or snap areas."""

    name = "Rectangle"
    cask_name = "rectangle"


# class IStats(GemModule):

#     name = "iStats"
#     gem_name = "iStats"

#     # sudo gem install iStats
#     # duso gem update iStats
