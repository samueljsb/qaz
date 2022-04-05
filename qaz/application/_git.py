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

    # Create local git config.
    config_file_content = _build_config_file(author_name, author_email)
    with Path.home().joinpath(".gitconfig.local").open("w+") as file:
        file.write(config_file_content)

    # Generate SSH key.
    return _generate_or_retrieve_ssh_key(author_email)


def _build_config_file(author_name: str, author_email: str) -> str:
    if platform == "darwin":
        git_credential = "osxkeychain"
    elif platform == "linux":
        git_credential = "cache"
    else:
        git_credential = ""

    return f"""\
[user]
    name = {author_name}
    email = {author_email}

[credential]
    helper = {git_credential}
"""


def _generate_or_retrieve_ssh_key(email: str) -> str:
    ssh_dir = Path.home() / ".ssh"
    id_rsa = ssh_dir / "id_rsa"
    id_rsa_pub = ssh_dir / "id_rsa.pub"
    if not id_rsa.exists():
        shell.run("ssh-keygen", "-t", "rsa", "-b", "4096", "-C", email, "-f", id_rsa)
        shell.run("ssh-add", "-K", id_rsa)
    with id_rsa_pub.open() as fd:
        public_key = fd.read()
    return public_key
