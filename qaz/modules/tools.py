from qaz.modules.brew import BrewModule
from qaz.modules.nodejs import NodeModule


class Bat(BrewModule):
    name = "bat"
    package_name = "bat"


class Exa(BrewModule):
    name = "exa"
    package_name = "exa"


class Figlet(BrewModule):
    name = "FIGlet"
    package_name = "figlet"


class Less(BrewModule):
    name = "less"
    package_name = "less"


class TrashCLI(NodeModule):
    name = "trash-cli"
    package_name = "trash-cli"
