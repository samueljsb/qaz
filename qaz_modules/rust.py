from __future__ import annotations

from qaz.managers import asdf
from qaz.modules.base import Module


class Rust(Module):
    name = "Rust"

    # Other
    vscode_extensions = [
        "rust-lang.rust",
    ]

    package_manager = asdf.ASDF("rust")
