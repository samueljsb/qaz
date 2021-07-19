from typing import Dict

from qaz.managers import asdf
from qaz.modules.base import Module


class Ruby(Module):
    name = "Ruby"

    # Configuration files
    zshrc_file = None
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions = [
        "rebornix.ruby",
        "sissel.shopify-liquid",
        "wingrunr21.vscode-ruby",
    ]

    @classmethod
    def install_action(cls):
        asdf.install_or_upgrade_plugin("ruby")

    @classmethod
    def upgrade_action(cls):
        asdf.install_or_upgrade_plugin("ruby")