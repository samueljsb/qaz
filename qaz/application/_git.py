from __future__ import annotations

from pathlib import Path
from sys import platform

from qaz.utils import shell

from . import _install


def configure_git(*, author_name: str, author_email: str) -> str:
    """
    Install and configure git.

    Returns the public key configured for git.
    """
    _install.install_module("git")

    # Generate SSH key.
    public_key_path = _generate_or_retrieve_ssh_key(author_email)

    # Create local git config.
    config_file_content = _build_config_file(author_name, author_email, public_key_path)
    with Path.home().joinpath(".gitconfig.local").open("w+") as file:
        file.write(config_file_content)

    return public_key_path.read_text()


def _build_config_file(author_name: str, author_email: str, ssh_key_path: Path) -> str:
    if platform == "darwin":
        git_credential = "osxkeychain"
    elif platform == "linux":
        git_credential = "cache"
    else:
        git_credential = ""

    return f"""\
[commit]
    gpgsign = true

[credential]
    helper = {git_credential}

[gpg]
    format = ssh

[user]
    name = {author_name}
    email = {author_email}
    signingkey = {ssh_key_path}
"""


def _generate_or_retrieve_ssh_key(email: str) -> Path:
    ssh_dir = Path.home() / ".ssh"
    id_rsa = ssh_dir / "id_rsa"
    id_rsa_pub = ssh_dir / "id_rsa.pub"

    if not id_rsa.exists():
        shell.run("ssh-keygen", "-t", "rsa", "-b", "4096", "-C", email, "-f", id_rsa)
        shell.run("ssh-add", "--apple-use-keychain")

    return id_rsa_pub
