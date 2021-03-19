from pathlib import Path
from sys import platform
from typing import List

import click

from qaz.module import Module
from qaz.modules.brew import BrewModule
from qaz.utils import output, shell


LOCAL_CONFIG_TEMPL = """
[user]
        name = {git_authorname}
        email = {git_authoremail}
[credential]
        helper = {git_credential}
"""


class Git(BrewModule):
    name = "git"
    package_name = "git"
    symlinks = {".gitconfig": "~", ".gitignore": "~", ".git-commit-msg": "~"}

    def install_action(self):
        super().install_action()

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
        output.message(f"Add your public key to GitHub:\n    {public_key}")
        shell.run(f"ssh-add -K {id_rsa}")


class GitModule(Module):
    repo_url: str
    repo_path: Path
    additional_clone_options: List[str] = list()

    def install_action(self):
        shell.run(
            f"git clone {' '.join(self.additional_clone_options)} {self.repo_url} {self.repo_path}"  # noqa: E501
        )

    def upgrade_action(self):
        shell.run(f"git -C {self.repo_path} pull")


class GitHubCLI(BrewModule):
    name = "GitHub"
    package_name = "gh"
    symlinks = {"github_config.yml": "~/.config/gh/config.yml"}

    def install_action(self):
        super().install_action()
        shell.run("gh auth login --web")


class LazyGit(BrewModule):
    name = "lazygit"
    package_name = "jesseduffield/lazygit/lazygit"


class DiffSoFancy(BrewModule):
    name = "diff-so-fancy"
    package_name = "diff-so-fancy"
    symlinks = {".gitconfig.diff-so-fancy": "~"}
