import logging
from pathlib import Path
from sys import platform
from typing import Dict, List

import click

from qaz.managers import brew, shell
from qaz.modules.base import Module


logger = logging.getLogger(__name__)


LOCAL_CONFIG_TEMPL = """
[user]
        name = {git_authorname}
        email = {git_authoremail}
[credential]
        helper = {git_credential}
"""


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

        # Set up local config
        if platform == "darwin":
            git_credential = "osxkeychain"
        elif platform == "linux":
            git_credential = "cache"
        else:
            git_credential = ""

        git_authorname = click.prompt("git author name", err=True)
        git_authoremail = click.prompt("git author email", err=True)

        with Path.home().joinpath(".gitconfig.local").open("w+") as fd:
            fd.write(
                LOCAL_CONFIG_TEMPL.format(
                    git_authorname=git_authorname,
                    git_authoremail=git_authoremail,
                    git_credential=git_credential,
                )
            )

        # Create SSH key if not already present.
        ssh_dir = Path.home() / ".ssh"
        id_rsa = ssh_dir / "id_rsa"
        id_rsa_pub = ssh_dir / "id_rsa.pub"
        if not id_rsa.exists():
            shell.run(f"ssh-keygen -t rsa -b 4096 -C '{git_authoremail}' -f {id_rsa}")
        with id_rsa_pub.open() as fd:
            public_key = fd.read()
        logger.info(f"Add your public key to GitHub:\n    {public_key}")
        shell.run(f"ssh-add -K {id_rsa}")

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
