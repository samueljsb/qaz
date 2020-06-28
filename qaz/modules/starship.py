from qaz.modules.asdf import ASDFModule


class Starship(ASDFModule):
    """A shell prompt."""

    name = "starship"
    plugin_name = "starship"
    symlinks = {"starship.toml": "~/.config"}
