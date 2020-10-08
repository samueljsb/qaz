from qaz.modules.brew import BrewModule
from qaz.modules.nodejs import NodeModule


class Bat(BrewModule):
    """A cat(1) clone with syntax highlighting and Git integration."""

    name = "bat"
    package_name = "bat"


class Exa(BrewModule):
    """A modern version of 'ls'."""

    name = "exa"
    package_name = "exa"


class Figlet(BrewModule):
    """A program for making large letters out of ordinary text."""

    name = "FIGlet"
    package_name = "figlet"


class Less(BrewModule):
    """Pager program similar to more."""

    name = "less"
    package_name = "less"


class TrashCLI(NodeModule):
    """Move files and folders to the trash."""

    name = "trash-cli"
    package_name = "trash-cli"
