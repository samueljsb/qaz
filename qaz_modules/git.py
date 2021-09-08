from typing import Dict, List

from qaz.managers import brew, shell
from qaz.modules.base import Module


class Git(Module):
    name = "git"

    # Configuration files
    zshrc_file = "git.zsh"
    symlinks = {".gitconfig": "~", ".gitignore": "~", ".git-commit-msg": "~"}

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        brew.install_or_upgrade_formula("git")

    @classmethod
    def upgrade_action(cls):
        brew.install_or_upgrade_formula("git")


class GitHubCLI(Module):
    name = "GitHub"

    # Configuration files
    zshrc_file = "github.zsh"
    symlinks = {"github_config.yml": "~/.config/gh/config.yml"}

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        brew.install_or_upgrade_formula("gh")
        shell.run("gh auth login --web")

    @classmethod
    def upgrade_action(cls):
        brew.install_or_upgrade_formula("gh")


class LazyGit(Module):
    name = "lazygit"

    # Configuration files
    zshrc_file = None
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        brew.install_or_upgrade_formula("jesseduffield/lazygit/lazygit")

    @classmethod
    def upgrade_action(cls):
        brew.install_or_upgrade_formula("jesseduffield/lazygit/lazygit")


class DiffSoFancy(Module):
    name = "diff-so-fancy"

    # Configuration files
    zshrc_file = None
    symlinks = {".gitconfig.diff-so-fancy": "~"}

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        brew.install_or_upgrade_formula("diff-so-fancy")

    @classmethod
    def upgrade_action(cls):
        brew.install_or_upgrade_formula("diff-so-fancy")
