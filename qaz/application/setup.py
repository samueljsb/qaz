from pathlib import Path

from qaz import settings

from . import install


def setup_qaz(root_dir: str) -> None:
    """
    Set up QAZ for the first time.

    This creates a settings file and the directory for zshrc files then 'installs' the
    modules that have already been installed by the install script.
    """
    # Create settings file.
    settings.set_root_dir(root_dir)

    # Create installed dir
    zshrc_dir = Path.home().joinpath(".zshrc.d")
    zshrc_dir.mkdir(exist_ok=True)

    # Install the modules which have already been installed by the setup script.
    already_installed = ("asdf", "python", "poetry")
    install.install_modules(already_installed)
