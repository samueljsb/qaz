from __future__ import annotations

from qaz.managers import brew, shell
from qaz.modules.base import Module


class Git(Module):
    name = "git"

    # Configuration files
    zshrc_file = "git.zsh"
    symlinks = {".gitconfig": "~", ".gitignore": "~", ".git-commit-msg": "~"}

    # Other
    vscode_extensions: list[str] = []

    # Package Management
    package_manager = brew.Homebrew("git")


class GitHubCLI(Module):
    name = "GitHub"

    # Configuration files
    zshrc_file = "github.zsh"
    symlinks = {"github_config.yml": "~/.config/gh/config.yml"}

    # Other
    vscode_extensions: list[str] = []

    # Package Management
    package_manager = brew.Homebrew("gh")

    @classmethod
    def install_action(cls) -> None:
        super().install_action()
        shell.run("gh auth login --web")


class LazyGit(Module):
    name = "lazygit"

    # Configuration files
    zshrc_file = None
    symlinks: dict[str, str] = {}

    # Other
    vscode_extensions: list[str] = []

    # Package Management
    package_manager = brew.Homebrew("jesseduffield/lazygit/lazygit")


class GitUI(Module):
    name = "GitUI"

    # Configuration files
    zshrc_file = None
    symlinks: dict[str, str] = {}

    # Other
    vscode_extensions: list[str] = []

    # Package Management
    package_manager = brew.Homebrew("gitui")


class DiffSoFancy(Module):
    name = "diff-so-fancy"

    # Configuration files
    zshrc_file = None
    symlinks = {".gitconfig.diff-so-fancy": "~"}

    # Other
    vscode_extensions: list[str] = []

    # Package Management
    package_manager = brew.Homebrew("diff-so-fancy")
