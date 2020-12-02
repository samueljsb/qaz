from qaz.managers import brew
from qaz.module import Module
from qaz.utils import run


class Brew(Module):
    """The Missing Package Manager for macOS (or Linux)."""

    name = "Homebrew"

    def install_action(self) -> None:
        """Install Homebrew."""
        run(
            '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"',
            env={"CI": "1"},
        )
        run("brew analytics off")

    def upgrade_action(self) -> None:
        """Update Homebrew."""
        run("brew update")
        run("brew analytics off")


class BrewModule(Module):
    """A Module which is managed by Homebrew.

    Attributes:
      package_name: The name of the package to manage.

    """

    package_name: str
    _base_requires = [Brew()]

    def install_action(self) -> None:
        """Install this package from Homebrew."""
        brew.install_or_upgrade_formula(self.package_name)
        return super().install_action()

    def upgrade_action(self) -> None:
        """Upgrade this package from Homebrew."""
        brew.install_or_upgrade_formula(self.package_name)
        return super().upgrade_action()


class BrewCaskModule(Module):
    """A Module which is managed by Homebrew.

    Attributes:
      cask_name: The name of the cask to manage.

    """

    cask_name: str
    _base_requires = [Brew()]

    def install_action(self) -> None:
        """Install this cask from Homebrew."""
        brew.install_or_upgrade_cask(self.cask_name)
        return super().install_action()

    def upgrade_action(self) -> None:
        """Upgrade this cask from Homebrew."""
        brew.install_or_upgrade_cask(self.cask_name)
        return super().upgrade_action()
