from __future__ import annotations

from qaz import managers
from qaz.modules.base import Module
from qaz.modules.registry import registry
from qaz.utils import shell


@registry.register
class Git(Module):
    name = "git"
    manager = managers.BrewFormula("git")

    # Configuration files
    zshrc_file = "git.zsh"
    symlinks = {".gitconfig": "~", ".gitignore": "~", ".git-commit-msg": "~"}


@registry.register
class GitHubCLI(Module):
    name = "GitHub"
    manager = managers.BrewFormula("gh")

    # Configuration files
    zshrc_file = "github.zsh"
    symlinks = {"github_config.yml": "~/.config/gh/config.yml"}

    def install_action(self) -> None:
        shell.run("gh auth login --web")


@registry.register
class LazyGit(Module):
    name = "lazygit"
    manager = managers.BrewFormula("jesseduffield/lazygit/lazygit")


@registry.register
class GitUI(Module):
    name = "GitUI"
    manager = managers.BrewFormula("gitui")


@registry.register
class DiffSoFancy(Module):
    name = "diff-so-fancy"
    manager = managers.BrewFormula("diff-so-fancy")

    # Configuration files
    symlinks = {".gitconfig.diff-so-fancy": "~"}
