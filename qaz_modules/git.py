from __future__ import annotations

from qaz import managers
from qaz.modules.base import Bundle
from qaz.modules.base import Module
from qaz.modules.registry import registry
from qaz.utils import shell


@registry.register
class Git(Bundle):
    name = "git"

    managers = (
        managers.BrewFormula("git"),
        managers.BrewFormula("git-absorb"),
        managers.BrewFormula("diff-so-fancy"),
    )

    # Configuration files
    zshrc_file = "git.zsh"
    symlinks = {
        "git": "~/.config/git",
    }


@registry.register
class GitHubCLI(Module):
    name = "GitHub"
    manager = managers.BrewFormula("gh")

    # Configuration files
    zshrc_file = "github.zsh"
    symlinks = {"github_config.yml": "~/.config/gh/config.yml"}

    def post_install(self) -> None:
        shell.run("gh", "auth", "login", "--web")


@registry.register
class GitUI(Module):
    name = "GitUI"
    manager = managers.BrewFormula("gitui")
