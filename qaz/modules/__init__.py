from sys import platform
from typing import Iterable, List

from qaz.module import Module

from .asdf import ASDF
from .brew import Brew
from .docker import Docker, LazyDocker
from .fonts import NerdFonts
from .git import DiffSoFancy, Git, GitHubCLI, LazyGit
from .iterm2 import ITerm2
from .latex import Mactex
from .macos import Bartender, MacOS, QuickLookExtensions, Rectangle
from .nodejs import NodeJS, Yarn
from .python import Bpython, Pipx, Poetry, Python, Rich, Tox
from .ruby import Ruby
from .rust import Rust
from .starship import Starship
from .tools import Bat, Exa, Figlet, GNUSed, Less, TrashCLI
from .vim import Vim
from .vscode import VSCode
from .zsh import ZSH, OhMyZSH


class ModuleNotFound(Exception):
    pass


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
    Rich(),
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

mac_modules: List[Module] = [
    ITerm2(),
    Mactex(),
    MacOS(),
    QuickLookExtensions(),
    Bartender(),
    Rectangle(),
    GNUSed(),
]

all_modules = modules
if platform == "darwin":
    all_modules.extend(mac_modules)


def get_modules(module_names: Iterable[str]) -> List[Module]:
    modules_by_name = {m.name.casefold(): m for m in all_modules}
    found = []
    missing = []
    for name in (name.casefold() for name in module_names):
        if name in modules_by_name:
            found.append(modules_by_name[name])
        else:
            missing.append(name)

    if missing:
        raise ModuleNotFound(f"Modules not found with names: {missing}")
    return found
