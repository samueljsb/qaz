from pathlib import Path
from sys import platform

from qaz.modules.brew import BrewCaskModule


if platform == "darwin":
    SETTINGS_DIR = Path.home() / "Library/Application Support/Code/User"
elif platform == "linux":
    SETTINGS_DIR = Path.home() / ".config/Code/User"
else:
    SETTINGS_DIR = Path.home() / ".config/Code/User"


class VSCode(BrewCaskModule):
    name = "VSCode"
    cask_name = "visual-studio-code"
    symlinks = {"settings.json": SETTINGS_DIR}
    vscode_extensions = [
        "alefragnani.Bookmarks",
        "bungcip.better-toml",
        "byi8220.indented-block-highlighting",
        "codezombiech.gitignore",
        "DavidAnson.vscode-markdownlint",
        "EditorConfig.EditorConfig",
        "esbenp.prettier-vscode",
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
