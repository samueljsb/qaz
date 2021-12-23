from __future__ import annotations

from qaz.managers import asdf
from qaz.modules.base import Module


class Ruby(Module):
    name = "Ruby"

    # Other
    vscode_extensions = [
        "rebornix.ruby",
        "sissel.shopify-liquid",
        "wingrunr21.vscode-ruby",
    ]

    @classmethod
    def install_action(cls) -> None:
        asdf.install_or_upgrade_plugin("ruby")

    @classmethod
    def upgrade_action(cls) -> None:
        asdf.install_or_upgrade_plugin("ruby")
