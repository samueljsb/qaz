from __future__ import annotations

from qaz import managers
from qaz.modules.base import Module
from qaz.modules.registry import registry


@registry.register
class MacOSDocker(Module):
    name = "Docker"
    auto_update = True

    # Configuration files
    zshrc_file = "docker.zsh"


@registry.register
class LazyDocker(Module):
    name = "lazydocker"
    manager = managers.BrewFormula("jesseduffield/lazydocker/lazydocker")
