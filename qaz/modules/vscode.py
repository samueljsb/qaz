from pathlib import Path
from sys import platform

from qaz.exceptions import DependenciesMissing
from qaz.module import Module
from qaz.utils import capture


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
    vscode_extensions = [
        "alefragnani.Bookmarks",
        "bungcip.better-toml",
        "byi8220.indented-block-highlighting",
        "codezombiech.gitignore",
        "DavidAnson.vscode-markdownlint",
        "EditorConfig.EditorConfig",
        "formulahendry.auto-close-tag",
        "mikestead.dotenv",
        "mrmlnc.vscode-apache",
        "ms-azuretools.vscode-docker",
        "ms-python.python",
        "naumovs.color-highlight",
        "npxms.hide-gitignored",
        "PKief.material-icon-theme",
        "pnp.polacode",
        "sidneys1.gitconfig",
        "syler.sass-indented",
        "swyphcosmo.spellchecker",
        "torn4dom4n.latex-support",
        "VisualStudioExptTeam.vscodeintellicode",
        "waderyan.gitblame",
        "wholroyd.jinja",
        "william-voyek.vscode-nginx",
    ]

    def _check_dependencies(self, *args, **kwargs) -> None:  # type: ignore
        command = capture("command -v code")
        if not command:
            raise DependenciesMissing(
                [
                    "VSCode is not installed, you must install VSCode before installing this module."
                ]
            )
        return super()._check_dependencies(*args, **kwargs)
