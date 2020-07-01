from pathlib import Path
from sys import platform

from qaz.module import Module
from qaz.modules.brew import BrewModule
from qaz.modules.git import GitModule
from qaz.utils import run


class ZSHBase(Module):
    """Z shell."""

    name = "zsh"
    zshrc_file = "_zsh.zsh"  # load early to allow modules to overwrite settings
    symlinks = {
        ".zshrc": "~",
        ".editorconfig": "~",
        "e": "/usr/local/bin",
    }


if platform == "darwin":

    class ZSH(ZSHBase, BrewModule):  # type: ignore
        """Z shell."""

        package_name = "zsh"


elif platform == "linux":

    class ZSH(ZSHBase):  # type: ignore
        """zsh for Linux."""

        def install_action(self) -> None:
            """Install zsh from apt."""
            run("sudo apt update")
            run("sudo apt install zsh")

        def upgrade_action(self) -> None:
            """Upgrade zsh from apt."""
            run("sudo apt update")
            run("sudo apt upgrade zsh")


class OhMyZSH(Module):
    """Framework for managing your Zsh configuration."""

    name = "Oh-My-Zsh"
    zshrc_file = "_oh-my-zsh.zsh"  # load early to allow modules to overwrite settings

    def install_action(self) -> None:
        """Install Oh-My-Zsh and plugins."""
        run(
            'sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"',
            env={"CHSH": "no", "RUNZSH": "no", "KEEP_ZSHRC": "yes"},
        )

        # Install themes and plugins.
        self.ZshSyntaxHighlighting().install()
        self.ZshAutosuggestions().install()

    def upgrade_action(self) -> None:
        """Upgrade oh-my-zsh and plugins."""
        zsh_dir = Path.home().resolve() / ".oh-my-zsh"
        run(f"sh {zsh_dir / 'tools/upgrade.sh'}", env={"ZSH": str(zsh_dir)})

        # Upgrade themes and plugins.
        self.ZshSyntaxHighlighting().upgrade()
        self.ZshAutosuggestions().upgrade()

    #  Plugins

    class ZshSyntaxHighlighting(GitModule):
        """Oh-My-Zsh plugin for syntax highlighting."""

        name = "zsh-syntax-highlighting"
        repo_url = "https://github.com/zsh-users/zsh-syntax-highlighting.git"
        repo_path = (
            Path.home().resolve() / ".oh-my-zsh/custom/plugins/zsh-syntax-highlighting"
        )

    class ZshAutosuggestions(GitModule):
        """Oh-My-Zsh plugin for autosuggestions."""

        name = "zsh-autosuggestions"
        repo_url = "https://github.com/zsh-users/zsh-autosuggestions.git"
        repo_path = (
            Path.home().resolve() / ".oh-my-zsh/custom/plugins/zsh-autosuggestions"
        )
