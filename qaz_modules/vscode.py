from sys import platform

from qaz.managers import brew
from qaz.modules.base import Module


if platform == "darwin":
    SETTINGS_DIR = "~/Library/Application Support/Code/User"
elif platform == "linux":
    SETTINGS_DIR = "~/.config/Code/User"
else:
    SETTINGS_DIR = "~/.config/Code/User"


class VSCode(Module):
    name = "VSCode"

    # Configuration files
    zshrc_file = None
    symlinks = {"settings.json": SETTINGS_DIR}

    # Other
    vscode_extensions = [
        "aaron-bond.better-comments",
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

    def install_action(self):
        brew.install_or_upgrade_cask("visual-studio-code")

    def upgrade_action(self):
        brew.install_or_upgrade_cask("visual-studio-code")
