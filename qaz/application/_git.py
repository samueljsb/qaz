from __future__ import annotations

from pathlib import Path

from . import _install


def configure_git(*, author_name: str, author_email: str) -> None:
    """
    Install and configure git.
    """
    _install.install_module("git")

    # Create local git config.
    with Path.home().joinpath(".gitconfig.local").open("w+") as file:
        file.write(
            f"""\
[user]
  name = {author_name}
  email = {author_email}
"""
        )
