from sys import platform
from typing import List

from qaz.exceptions import ModuleDoesNotExist
from qaz.module import Module
from .asdf import ASDF
from .brew import Brew
from .docker import Docker, LazyDocker
from .fonts import NerdFonts
from .git import DiffSoFancy, Git, GitHubCLI, LazyGit
from .iterm2 import ITerm2
from .latex import Mactex
from .macos import Bartender, MacOS, Rectangle
from .nodejs import NodeJS, Yarn
from .python import Bpython, Pipx, Poetry, Python, Tox
from .ruby import Ruby
from .rust import Rust
from .starship import Starship
from .tools import Bat, Exa, Figlet, Less, TrashCLI
from .vim import Vim
from .vscode import VSCode
from .zsh import ZSH, OhMyZSH


modules: List[Module] = [
    ASDF(),
    Brew(),
    Docker(),
    LazyDocker(),
    Git(),
    GitHubCLI(),
    LazyGit(),
    DiffSoFancy(),
    Less(),
    NerdFonts(),
    NodeJS(),
    OhMyZSH(),
    Pipx(),
    Poetry(),
    Python(),
    Bpython(),
    Tox(),
    Ruby(),
    Rust(),
    Starship(),
    TrashCLI(),
    Vim(),
    VSCode(),
    Yarn(),
    ZSH(),
    Bat(),
    Exa(),
    Figlet(),
]

mac_modules: List[Module] = [ITerm2(), Mactex(), MacOS(), Bartender(), Rectangle()]

all_modules = modules
if platform == "darwin":
    all_modules.extend(mac_modules)


def get_module(name: str) -> Module:
    """Get a module by name.

    The lookup is case-insensitive.

    Args:
        name: The name of the module to retreive.

    Returns:
        A `Module` instance with the given name.

    Raises:
        ModuleDoesNotExist if the module with the given name cannot be found.

    """
    try:
        return next(
            module for module in all_modules if module.name.lower() == name.lower()
        )
    except StopIteration:
        raise ModuleDoesNotExist(name)
