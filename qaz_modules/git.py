from __future__ import annotations

from qaz.managers import brew, shell
from qaz.modules.base import Module
from qaz.modules.registry import register


@register
class Git(Module):
    name = "git"

    # Configuration files
    zshrc_file = "git.zsh"
    symlinks = {".gitconfig": "~", ".gitignore": "~", ".git-commit-msg": "~"}

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("git")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("git")


@register
class GitHubCLI(Module):
    name = "GitHub"

    # Configuration files
    zshrc_file = "github.zsh"
    symlinks = {"github_config.yml": "~/.config/gh/config.yml"}

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("gh")
        shell.run("gh auth login --web")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("gh")


@register
class LazyGit(Module):
    name = "lazygit"

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("jesseduffield/lazygit/lazygit")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("jesseduffield/lazygit/lazygit")


@register
class GitUI(Module):
    name = "GitUI"

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("gitui")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("gitui")


@register
class DiffSoFancy(Module):
    name = "diff-so-fancy"

    # Configuration files
    symlinks = {".gitconfig.diff-so-fancy": "~"}

    def install_action(self) -> None:
        brew.install_or_upgrade_formula("diff-so-fancy")

    def upgrade_action(self) -> None:
        brew.install_or_upgrade_formula("diff-so-fancy")
