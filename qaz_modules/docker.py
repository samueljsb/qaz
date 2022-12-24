from __future__ import annotations

from qaz.modules.base import Module
from qaz.modules.registry import registry


@registry.register
class MacOSDocker(Module):
    name = "Docker"
    auto_update = True

    # Configuration files
    zshrc_file = "docker.zsh"
