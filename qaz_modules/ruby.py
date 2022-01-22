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

    package_manager = asdf.ASDF("ruby")
