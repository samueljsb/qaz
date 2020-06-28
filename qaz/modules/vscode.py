from pathlib import Path
from sys import platform
from typing import List

from qaz.exceptions import DependenciesMissing
from qaz.module import Module
from qaz.utils import capture, run


EXTENSIONS = [
    "alefragnani.Bookmarks",
    "bungcip.better-toml",
    "byi8220.indented-block-highlighting",
    "codezombiech.gitignore",
    "DavidAnson.vscode-markdownlint",
    "dbaeumer.vscode-eslint",
    "EditorConfig.EditorConfig",
    "formulahendry.auto-close-tag",
    "ginfuru.ginfuru-vscode-jekyll-syntax",
    "lextudio.restructuredtext",
    "mikestead.dotenv",
    "ms-python.python",
    "naumovs.color-highlight",
    "npxms.hide-gitignored",
    "numso.prettier-standard-vscode",
    "PKief.material-icon-theme",
    "pnp.polacode",
    "sidneys1.gitconfig",
    "syler.sass-indented",
    "torn4dom4n.latex-support",
    "VisualStudioExptTeam.vscodeintellicode",
    "waderyan.gitblame",
    "wholroyd.jinja",
]

if platform == "darwin":
    SETTINGS_DIR = Path.home() / "Library/Application Support/Code/User"
elif platform == "linux":
    SETTINGS_DIR = Path.home() / ".config/Code/User"
else:
    SETTINGS_DIR = Path.home() / ".config/Code/User"


class VSCode(Module):
    """My configuration and plugins for Visual Studio Code.

    Requires VSCode to be installed before this module can be installed.
    """

    name = "VSCode"
    symlinks = {"settings.json": SETTINGS_DIR}

    @staticmethod
    def list_extensions() -> List[str]:
        """Get a list of the currently installed VSCode extensions."""
        return capture("code --list-extensions").split()

    def _check_dependencies(self, *args, **kwargs) -> None:  # type: ignore
        command = capture("command -v code")
        if not command:
            raise DependenciesMissing(
                [
                    "VSCode is not installed, you must install VSCode before installing this module."
                ]
            )
        return super()._check_dependencies(*args, **kwargs)

    def install_action(self) -> None:
        """Install VSCode extensions."""
        for name in EXTENSIONS:
            run(f"code --install-extension {name}")

    def upgrade_action(self) -> None:
        """Install VSCode extensions."""
        installed = self.list_extensions()
        for name in [ext for ext in EXTENSIONS if ext not in installed]:
            run(f"code --install-extension {name}")
