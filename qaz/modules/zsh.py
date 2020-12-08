from pathlib import Path
from sys import platform

from qaz.module import Module
from qaz.modules.brew import BrewModule
from qaz.modules.git import GitModule
from qaz.utils import shell


class ZSHBase(Module):
    name = "zsh"
    zshrc_file = "_zsh.zsh"  # load early to allow modules to overwrite settings
    symlinks = {
        ".zshrc": "~",
        ".editorconfig": "~",
        "e": "/usr/local/bin",
    }

    def _set_default_shell(self):
        zsh_path = shell.capture("which zsh")

        # Make sure zsh is an allowed shell.
        shells = Path("/etc/shells")
        if zsh_path not in shells.read_text():
            with shells.open("a") as fd:
                fd.write(zsh_path + "\n")

        # Make zsh the default shell.
        shell.run(f"chsh -s {zsh_path}")


if platform == "darwin":

    class ZSH(ZSHBase, BrewModule):  # type: ignore
        package_name = "zsh"

        def install_action(self):
            super().install_action()
            self._set_default_shell()

        def upgrade_action(self):
            super().install_action()
            self._set_default_shell()


elif platform == "linux":

    class ZSH(ZSHBase):  # type: ignore
        def install_action(self):
            shell.run("sudo apt update")
            shell.run("sudo apt install zsh")
            self._set_default_shell()

        def upgrade_action(self):
            shell.run("sudo apt update")
            shell.run("sudo apt upgrade zsh")
            self._set_default_shell()


class OhMyZSH(Module):
    name = "Oh-My-Zsh"
    zshrc_file = "_oh-my-zsh.zsh"  # load early to allow modules to overwrite settings

    def install_action(self) -> None:
        shell.run(
            'sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"',  # noqa: E501
            env={"CHSH": "no", "RUNZSH": "no", "KEEP_ZSHRC": "yes"},
        )

        # Install themes and plugins.
        self.ZshSyntaxHighlighting().install()
        self.ZshAutosuggestions().install()

    def upgrade_action(self) -> None:
        zsh_dir = Path.home().resolve() / ".oh-my-zsh"
        shell.run(f"sh {zsh_dir / 'tools/upgrade.sh'}", env={"ZSH": str(zsh_dir)})

        # Upgrade themes and plugins.
        self.ZshSyntaxHighlighting().upgrade()
        self.ZshAutosuggestions().upgrade()

    #  Plugins

    class ZshSyntaxHighlighting(GitModule):
        name = "zsh-syntax-highlighting"
        repo_url = "https://github.com/zsh-users/zsh-syntax-highlighting.git"
        repo_path = (
            Path.home().resolve() / ".oh-my-zsh/custom/plugins/zsh-syntax-highlighting"
        )

    class ZshAutosuggestions(GitModule):
        name = "zsh-autosuggestions"
        repo_url = "https://github.com/zsh-users/zsh-autosuggestions.git"
        repo_path = (
            Path.home().resolve() / ".oh-my-zsh/custom/plugins/zsh-autosuggestions"
        )
