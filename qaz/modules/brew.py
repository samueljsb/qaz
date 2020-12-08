from qaz.managers import brew
from qaz.module import Module
from qaz.utils import shell


class Brew(Module):
    name = "Homebrew"

    def install_action(self):
        shell.run(
            '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"',  # noqa: E501
            env={"CI": "1"},
        )
        shell.run("brew analytics off")

    def upgrade_action(self):
        shell.run("brew update")
        shell.run("brew analytics off")


class BrewModule(Module):
    package_name: str
    _base_requires = [Brew()]

    def install_action(self):
        brew.install_or_upgrade_formula(self.package_name)
        return super().install_action()

    def upgrade_action(self):
        brew.install_or_upgrade_formula(self.package_name)
        return super().upgrade_action()


class BrewCaskModule(Module):
    cask_name: str
    _base_requires = [Brew()]

    def install_action(self):
        brew.install_or_upgrade_cask(self.cask_name)
        return super().install_action()

    def upgrade_action(self):
        brew.install_or_upgrade_cask(self.cask_name)
        return super().upgrade_action()
