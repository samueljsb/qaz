from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from qaz import managers
from qaz.modules.base import Module
from qaz.modules.registry import registry
from qaz.utils import git
from qaz.utils import shell


class MacOSZsh(Module):
    name = "zsh"
    manager = managers.BrewFormula("zsh")

    # Configuration files
    zshrc_file = "_zsh.zsh"  # load early to allow modules to overwrite settings
    symlinks = {
        ".zshrc": "~",
        ".editorconfig": "~",
    }

    def install_action(self) -> None:
        _set_default_shell()

    def upgrade_action(self) -> None:
        _set_default_shell()


class LinuxZsh(Module):
    name = "zsh"

    # Configuration files
    zshrc_file = "_zsh.zsh"  # load early to allow modules to overwrite settings
    symlinks = {
        ".zshrc": "~",
        ".editorconfig": "~",
    }

    def install_action(self) -> None:
        shell.run("sudo", "apt", "update")
        shell.run("sudo", "apt", "install", "--yes", "zsh")
        _set_default_shell()

    def upgrade_action(self) -> None:
        shell.run("sudo", "apt", "update")
        shell.run("sudo", "apt", "upgrade", "--yes", "zsh")
        _set_default_shell()


if sys.platform == "darwin":
    registry.register(MacOSZsh)
elif sys.platform == "Linux":
    registry.register(LinuxZsh)


def _set_default_shell() -> None:
    zsh_path = shell.capture("which", "zsh")

    # Make sure zsh is an allowed shell.
    shells = Path("/etc/shells")
    if zsh_path not in shells.read_text():
        with shells.open("a") as fd:
            fd.write(zsh_path + "\n")

    # Make zsh the default shell.
    shell.run("chsh", "-s", zsh_path)


@registry.register
class OhMyZSH(Module):
    name = "Oh-My-Zsh"

    # Configuration files
    zshrc_file = "_oh-my-zsh.zsh"  # load early to allow modules to overwrite settings

    def install_action(self) -> None:
        install_script = shell.capture(
            "curl",
            "-fsSL",
            "https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh",
        )
        subprocess.run(
            ("sh", "-c", install_script),
            env={"CHSH": "no", "RUNZSH": "no", "KEEP_ZSHRC": "yes"},
        )

        # Install themes and plugins.
        git.clone(
            repo_url="https://github.com/zsh-users/zsh-autosuggestions",
            repo_path=Path.home() / ".oh-my-zsh/custom/plugins/zsh-autosuggestions",
        )

    def upgrade_action(self) -> None:
        zsh_dir = Path.home().resolve() / ".oh-my-zsh"
        shell.run(
            *("sh", zsh_dir / "tools/upgrade.sh", "--interactive"),
            env={"ZSH": str(zsh_dir)},
        )

        # Upgrade themes and plugins.
        git.pull(Path.home() / ".oh-my-zsh/custom/plugins/zsh-autosuggestions")

    @property
    def version(self) -> str:
        zsh_dir = Path.home().resolve() / ".oh-my-zsh"
        return git.version(zsh_dir)


@registry.register
class ZshSyntaxHighlighting(Module):
    name = "zsh-syntax-highlighting"
    manager = managers.BrewFormula("zsh-syntax-highlighting")

    # Configuration files
    zshrc_file = "zsh_syntax_highlighting.zsh"
