from __future__ import annotations

import sys

from qaz import managers
from qaz.modules.base import Module
from qaz.modules.registry import registry


class MacTex(Module):
    name = "LaTeX"
    manager = managers.BrewCask("mactex")


if sys.platform == "darwin":
    registry.register(MacTex)
