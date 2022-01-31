from sys import platform

from qaz.managers import brew, vs_code
from qaz.modules.base import Module
from qaz.modules.registry import register


if platform == "darwin":
    SETTINGS_DIR = "~/Library/Application Support/Code/User"
elif platform == "linux":
    SETTINGS_DIR = "~/.config/Code/User"
else:
    SETTINGS_DIR = "~/.config/Code/User"


@register
class VSCode(Module):
    name = "VSCode"
    auto_update = True

    # Configuration files
    symlinks = {"settings.json": SETTINGS_DIR}

    # Other
    extensions = [
        # VS Code
        "aaron-bond.better-comments",
        "alefragnani.Bookmarks",
        "byi8220.indented-block-highlighting",
        "EditorConfig.EditorConfig",
        "formulahendry.auto-close-tag",
        "mikestead.dotenv",
        "naumovs.color-highlight",
        "PKief.material-icon-theme",
        "pnp.polacode",
        "stkb.rewrap",
        "swyphcosmo.spellchecker",
        "VisualStudioExptTeam.vscodeintellicode",
        # Git
        "codezombiech.gitignore",
        "knisterpeter.vscode-github",
        "npxms.hide-gitignored",
        "sidneys1.gitconfig",
        "waderyan.gitblame",
        # NodeJS
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "numso.prettier-standard-vscode",
        # Python
        "freakypie.code-python-isort",
        "lextudio.restructuredtext",
        "ms-python.python",
        "ms-python.vscode-pylance",
        "wholroyd.jinja",
        # Ruby
        "rebornix.ruby",
        "sissel.shopify-liquid",
        "wingrunr21.vscode-ruby",
        # Rust
        "rust-lang.rust",
        # TOML
        "bungcip.better-toml",
        # Misc.
        "DavidAnson.vscode-markdownlint",
        "mrmlnc.vscode-apache",
        "ms-azuretools.vscode-docker",
        "syler.sass-indented",
        "torn4dom4n.latex-support",
        "wholroyd.jinja",
        "william-voyek.vscode-nginx",
    ]

    def install_action(self) -> None:
        brew.install_or_upgrade_cask("visual-studio-code")
        vs_code.install_extensions(self.extensions)

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_cask("visual-studio-code")
        vs_code.install_extensions(self.extensions)
