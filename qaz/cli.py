from pathlib import Path
from subprocess import CalledProcessError
from typing import Iterable, Tuple

import click

from .config import Config, config
from .module import DependenciesMissing
from .modules import ModuleDoesNotExist, all_modules, get_module
from .utils import output, shell


SETUP_MESSAGE = """
Access this tool again with
    qaz [OPTIONS] COMMAND [ARGS]...

You may want to install some basics to begin:
    qaz install -d git starship
"""


@click.group()
def cli() -> None:
    """Manage your system configuration and install/update tools."""


@cli.command()
@click.argument("root_dir")
def setup(root_dir: str) -> None:
    """Install this tool and the basics."""
    output.message("Installing qaz...")

    # Create config
    new_config = Config(root_dir)
    new_config.save()
    config.load_from_file()

    # Create installed dir
    zshrc_dir = Path.home().joinpath(".zshrc.d")
    zshrc_dir.mkdir(exist_ok=True)

    try:
        # 'Install' modules installed by install.sh (it's already installed, but this adds it properly)
        get_module("asdf").install(install_dependencies=True)
        get_module("python").install(install_dependencies=True)
        get_module("poetry").install(install_dependencies=True)

        # Install zsh
        get_module("zsh").install(install_dependencies=True)
    except (ModuleDoesNotExist, DependenciesMissing, CalledProcessError) as err:
        output.error(str(err))
        raise click.Abort

    # Set zsh as the system shell
    zsh_path = shell.capture("which zsh")
    shell.run(f"sudo bash -c 'echo \"{zsh_path}\" >> /etc/shells'")
    shell.run(f"chsh -s {zsh_path}")

    output.message("... qaz is installed.")
    output.message(SETUP_MESSAGE)


@cli.command()
def update() -> None:
    """Update this tool."""
    shell.run(f"git -C {config.root_dir} pull")


@cli.command()
@click.argument("modules", nargs=-1)
@click.option(
    "-d",
    "--install-dependencies",
    is_flag=True,
    help="Install this module's dependencies if they are missing.",
)
def install(modules: Tuple[str], install_dependencies: bool) -> None:
    """Install modules.

    The module names are case-insensitive.
    """
    for module in modules:
        try:
            get_module(module).install(install_dependencies=install_dependencies)
        except (ModuleDoesNotExist, DependenciesMissing, CalledProcessError) as err:
            output.error(str(err))


@cli.command()
@click.argument("modules", nargs=-1)
@click.option(
    "-a", "--all", "upgrade_all", is_flag=True, help="Upgrade all installed modules."
)
def upgrade(modules: Iterable[str], upgrade_all: bool) -> None:
    """Upgrade modules.

    The module names are case-insensitive.
    """
    if upgrade_all:
        modules = config.installed_modules
    for module in modules:
        try:
            get_module(module).upgrade()
        except (ModuleDoesNotExist, DependenciesMissing, CalledProcessError) as err:
            output.error(str(err))


@cli.command("list")
def _list() -> None:
    """List installed and available modules."""
    for module in all_modules:
        if module.name in config.installed_modules:
            click.echo(f"{module.name} - installed")
        else:
            click.echo(module.name)


@cli.command()
def edit() -> None:
    """Open the repo for editing."""
    shell.run(f"$EDITOR {config.root_dir}")
