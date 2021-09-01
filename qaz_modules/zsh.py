from pathlib import Path
from typing import Dict, List

from qaz.managers import brew, git, shell
from qaz.modules.base import Module


class MacOSZsh(Module):
    name = "zsh"

    # Configuration files
    zshrc_file = "_zsh.zsh"  # load early to allow modules to overwrite settings
    symlinks = {
        ".zshrc": "~",
        ".editorconfig": "~",
        "e": "/usr/local/bin",
    }

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        brew.install_or_upgrade_formula("zsh")
        _set_default_shell()

    @classmethod
    def upgrade_action(cls):
        brew.install_or_upgrade_formula("zsh")
        _set_default_shell()


class LinuxZsh(Module):
    name = "zsh"

    # Configuration files
    zshrc_file = "_zsh.zsh"  # load early to allow modules to overwrite settings
    symlinks = {
        ".zshrc": "~",
        ".editorconfig": "~",
        "e": "/usr/local/bin",
    }

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        shell.run("sudo apt update")
        shell.run("sudo apt install --yes zsh")
        _set_default_shell()

    @classmethod
    def upgrade_action(cls):
        shell.run("sudo apt update")
        shell.run("sudo apt upgrade --yes zsh")
        _set_default_shell()


def _set_default_shell():
    zsh_path = shell.capture("which zsh")

    # Make sure zsh is an allowed shell.
    shells = Path("/etc/shells")
    if zsh_path not in shells.read_text():
        with shells.open("a") as fd:
            fd.write(zsh_path + "\n")

    # Make zsh the default shell.
    shell.run(f"chsh -s {zsh_path}")


class OhMyZSH(Module):
    name = "Oh-My-Zsh"

    # Configuration files
    zshrc_file = "_oh-my-zsh.zsh"  # load early to allow modules to overwrite settings
    symlinks: Dict[str, str] = {}

    # Other
    vscode_extensions: List[str] = []

    @classmethod
    def install_action(cls):
        shell.run(
            'sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"',  # noqa: E501
            env={"CHSH": "no", "RUNZSH": "no", "KEEP_ZSHRC": "yes"},
        )

        # Install themes and plugins.
        git.clone(
            repo_url="https://github.com/zsh-users/zsh-syntax-highlighting.git",
            repo_path=Path.home() / ".oh-my-zsh/custom/plugins/zsh-syntax-highlighting",
        )
        git.clone(
            repo_url="https://github.com/zsh-users/zsh-autosuggestions.git",
            repo_path=Path.home() / ".oh-my-zsh/custom/plugins/zsh-autosuggestions",
        )

    @classmethod
    def upgrade_action(cls):
        zsh_dir = Path.home().resolve() / ".oh-my-zsh"
        shell.run(f"sh {zsh_dir / 'tools/upgrade.sh'} --interactive", env={"ZSH": str(zsh_dir)})

        # Upgrade themes and plugins.
        git.pull(Path.home() / ".oh-my-zsh/custom/plugins/zsh-syntax-highlighting")
        git.pull(Path.home() / ".oh-my-zsh/custom/plugins/zsh-autosuggestions")
