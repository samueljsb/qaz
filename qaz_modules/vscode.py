from __future__ import annotations

from sys import platform

from qaz.modules.base import Module
from qaz.modules.registry import registry
from qaz.utils import vs_code


if platform == "darwin":
    SETTINGS_DIR = "~/Library/Application Support/Code/User"
elif platform == "linux":
    SETTINGS_DIR = "~/.config/Code/User"
else:
    SETTINGS_DIR = "~/.config/Code/User"


@registry.register
class VSCode(Module):
    name = "VSCode"

    # Configuration files
    symlinks = {
        "keybindings.json": SETTINGS_DIR,
        "settings.json": SETTINGS_DIR,
        ".editorconfig": "~",
    }

    # Other
    extensions = [
        # VS Code
        "aaron-bond.better-comments",
        "alefragnani.Bookmarks",
        "artdiniz.quitcontrol-vscode",
        "byi8220.indented-block-highlighting",
        "EditorConfig.EditorConfig",
        "formulahendry.auto-close-tag",
        "mikestead.dotenv",
        "naumovs.color-highlight",
        "PKief.material-icon-theme",
        "stkb.rewrap",
        "swyphcosmo.spellchecker",
        # Git
        "codezombiech.gitignore",
        "fabiospampinato.vscode-open-in-github",
        "github.vscode-github-actions",
        "sidneys1.gitconfig",
        "waderyan.gitblame",
        # Python
        "lextudio.restructuredtext",
        "ms-python.python",
        "ms-python.vscode-pylance",
        # Other
        "DavidAnson.vscode-markdownlint",
        "ms-azuretools.vscode-docker",
    ]

    def post_install(self) -> None:
        vs_code.install_extensions(self.extensions)

    def post_upgrade(self) -> None:
        vs_code.install_extensions(self.extensions)
