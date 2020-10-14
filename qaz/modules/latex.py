from qaz.modules.brew import BrewCaskModule


class Mactex(BrewCaskModule):
    """Full TeX Live distribution without GUI applications."""

    name = "LaTeX"
    cask_name = "mactex-no-gui"
