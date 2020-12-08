from qaz.modules.asdf import ASDFModule


class Starship(ASDFModule):
    name = "starship"
    plugin_name = "starship"
    symlinks = {"starship.toml": "~/.config"}
