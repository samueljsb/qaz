from sys import platform

from qaz.managers import brew, vs_code
from qaz.modules.base import Module


if platform == "darwin":
    SETTINGS_DIR = "~/Library/Application Support/Code/User"
elif platform == "linux":
    SETTINGS_DIR = "~/.config/Code/User"
else:
    SETTINGS_DIR = "~/.config/Code/User"


class VSCode(Module):
    name = "VSCode"
    auto_update = True

    # Configuration files
    zshrc_file = None
    symlinks = {"settings.json": SETTINGS_DIR}

    # Other
    extensions = [
        "aaron-bond.better-comments",
        "alefragnani.Bookmarks",
        "bungcip.better-toml",
        "byi8220.indented-block-highlighting",
        "codezombiech.gitignore",
        "DavidAnson.vscode-markdownlint",
        "EditorConfig.EditorConfig",
        "esbenp.prettier-vscode",
        "formulahendry.auto-close-tag",
        "knisterpeter.vscode-github",
        "mikestead.dotenv",
        "mrmlnc.vscode-apache",
        "ms-azuretools.vscode-docker",
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
        "zamerick.vscode-caddyfile-syntax",
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
    ]

    @classmethod
    def install_action(cls) -> None:
        brew.install_or_upgrade_cask("visual-studio-code")
        vs_code.install_extensions(cls.extensions)

    @classmethod
    def upgrade_action(cls) -> None:
        brew.install_or_upgrade_cask("visual-studio-code")
        vs_code.install_extensions(cls.extensions)
