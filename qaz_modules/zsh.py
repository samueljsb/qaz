from __future__ import annotations

import os
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
    symlinks = {".zshrc": "~"}

    def post_install(self) -> None:
        _set_default_shell()

    def post_upgrade(self) -> None:
        _set_default_shell()


class LinuxZsh(Module):
    name = "zsh"

    # Configuration files
    zshrc_file = "_zsh.zsh"  # load early to allow modules to overwrite settings
    symlinks = {
        ".zshrc": "~",
        ".editorconfig": "~",
    }

    def post_install(self) -> None:
        shell.run("sudo", "apt", "update")
        shell.run("sudo", "apt", "install", "--yes", "zsh")
        _set_default_shell()

    def post_upgrade(self) -> None:
        shell.run("sudo", "apt", "update")
        shell.run("sudo", "apt", "upgrade", "--yes", "zsh")
        _set_default_shell()


if sys.platform == "darwin":
    registry.register(MacOSZsh)
elif sys.platform == "Linux":
    registry.register(LinuxZsh)


def _set_default_shell() -> None:
    zsh_path = shell.capture("which", "zsh").strip()

    # Make sure zsh is an allowed shell.
    shells = Path("/etc/shells")
    if zsh_path not in shells.read_text():
        with shells.open("a") as fd:
            fd.write(zsh_path + "\n")

    # Make zsh the default shell.
    if os.getenv("SHELL") != zsh_path:
        shell.run("chsh", "-s", zsh_path)


@registry.register
class OhMyZSH(Module):
    name = "Oh-My-Zsh"

    # Configuration files
    zshrc_file = "_oh-my-zsh.zsh"  # load early to allow modules to overwrite settings

    def post_install(self) -> None:
        install_script = shell.capture(
            "curl",
            "-fsSL",
            "https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh",
        )
        subprocess.run(
            ("sh", "-c", install_script),
            env={"CHSH": "no", "RUNZSH": "no", "KEEP_ZSHRC": "yes"},
        )

    def post_upgrade(self) -> None:
        zsh_dir = Path.home().resolve() / ".oh-my-zsh"
        shell.run(
            *("sh", zsh_dir / "tools/upgrade.sh", "--interactive"),
            env={"ZSH": str(zsh_dir)},
        )

    @property
    def versions(self) -> dict[str, str]:
        zsh_dir = Path.home().resolve() / ".oh-my-zsh"
        return {"oh-my-zsh": git.version(zsh_dir)}


@registry.register
class ZshAutosuggestions(Module):
    name = "zsh-autosuggestions"
    manager = managers.BrewFormula("zsh-autosuggestions")

    # Configuration files
    zshrc_file = "zsh-autosuggestions.zsh"


@registry.register
class ZshSyntaxHighlighting(Module):
    name = "zsh-syntax-highlighting"
    manager = managers.BrewFormula("zsh-syntax-highlighting")

    # Configuration files
    zshrc_file = "zsh-syntax-highlighting.zsh"
