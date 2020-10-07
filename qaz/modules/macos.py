from qaz.config import config
from qaz.module import Module
from qaz.modules.brew import BrewCaskModule
from qaz.utils import run


class MacOS(Module):
    """My configuration for macOS."""

    name = "macOS"

    def install_action(self) -> None:
        """Run the script to set defaults."""
        run(str(config.root_dir / "scripts" / "set-defaults.sh"))

    def upgrade_action(self) -> None:
        """Run the script to set defaults."""
        run(str(config.root_dir / "scripts" / "set-defaults.sh"))


class Bartender(BrewCaskModule):
    """Menu bar icon organizer."""

    name = "Bartender"
    cask_name = "bartender"


# class IStats(GemModule):

#     name = "iStats"
#     gem_name = "iStats"

#     # sudo gem install iStats
#     # duso gem update iStats
