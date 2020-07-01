from pathlib import Path
from sys import platform
from typing import List

from qaz.module import Module
from qaz.modules.brew import BrewModule
from qaz.utils import message, run


LOCAL_CONFIG_TEMPL = """
[user]
        name = {git_authorname}
        email = {git_authoremail}
[credential]
        helper = {git_credential}
"""


class Git(BrewModule):
    """Distributed version-control system.

    Extras:
        lazygit: A simple terminal UI for git commands.

    """

    name = "git"
    package_name = "git"
    symlinks = {".gitconfig": "~", ".gitignore": "~"}

    def install_action(self) -> None:
        """Install git and set up local config."""
        super().install_action()

        # Set up local config
        if platform == "darwin":
            git_credential = "osxkeychain"
        elif platform == "linux":
            git_credential = "cache"
        else:
            git_credential = ""

        git_authorname = input("- What is your git author name? ")
        git_authoremail = input("- What is your git author email? ")

        with Path.home().joinpath(".gitconfig.local").open("w+") as fd:
            fd.write(
                LOCAL_CONFIG_TEMPL.format(
                    git_authorname=git_authorname,
                    git_authoremail=git_authoremail,
                    git_credential=git_credential,
                )
            )

        # Create SSH key if not already present.
        id_rsa = Path.home() / ".ssh/id_rsa"
        if not id_rsa.exists():
            run(f"ssh-keygen -t rsa -b 4096 -C '{git_authoremail}' -f ~/.ssh/{id_rsa}")
        id_rsa_pub = Path.home() / ".ssh/id_rsa.pub"
        with id_rsa_pub.open() as fd:
            public_key = fd.read()
        message(f"Add your public key to GitHub:\n    {public_key}")
        run("ssh-add -K ~/.ssh/id_rsa")


class GitModule(Module):
    """A Module which is installed by cloning a git repo.

    Attributes:
      repo_url: The url of the repo to clone.
      repo_path: The path to which to clone the repo.
      additional_clone_options: Additional options to pass to git when cloning.

    """

    repo_url: str
    repo_path: Path
    additional_clone_options: List[str] = list()
    _base_requires = [Git()]

    def install_action(self) -> None:
        """Clone the repo."""
        run(
            f"git clone {' '.join(self.additional_clone_options)} {self.repo_url} {self.repo_path}"
        )

    def upgrade_action(self) -> None:
        """Pull the latest commits for this repo."""
        run(f"git -C {self.repo_path} pull")


class LazyGit(BrewModule):
    """A simple terminal UI for git commands."""

    name = "lazygit"
    package_name = "jesseduffield/lazygit/lazygit"


class DiffSoFancy(BrewModule):
    """A simple terminal UI for git commands."""

    name = "diff-so-fancy"
    package_name = "diff-so-fancy"
    symlinks = {".gitconfig.diff-so-fancy": "~"}
