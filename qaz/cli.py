from pathlib import Path
from subprocess import CalledProcessError
from typing import Iterable, Tuple

import click

from .config import Config, config
from .module import DependenciesMissing
from .modules import all_modules, get_modules
from .utils import output, shell


@click.group()
def cli():
    """
    Manage your system configuration and install/update tools.
    """


@cli.command()
@click.argument("root_dir")
def setup(root_dir: str):
    """
    Install this tool and the basics.
    """
    output.message("Installing qaz...")

    # Create config
    new_config = Config(root_dir)
    new_config.save()
    config.load_from_file()

    # Create installed dir
    zshrc_dir = Path.home().joinpath(".zshrc.d")
    zshrc_dir.mkdir(exist_ok=True)

    ALREADY_INSTALLED = ("asdf", "python", "poetry")
    INSTALL_NOW = ("zsh",)
    install(ALREADY_INSTALLED + INSTALL_NOW)

    output.message("... qaz is installed.")


@cli.command()
def update():
    """
    Update this tool.
    """
    shell.run(f"git -C {config.root_dir} pull")


@cli.command()
@click.argument("modules", nargs=-1)
def install(modules: Tuple[str]):
    """
    Install modules.
    """
    try:
        _modules = get_modules(modules)
    except ValueError as exc:
        raise click.ClickException(str(exc))

    for module in _modules:
        try:
            module.install()
        except (DependenciesMissing, CalledProcessError) as exc:
            raise click.ClickException(str(exc))


@cli.command()
@click.argument("modules", nargs=-1)
@click.option(
    "-a", "--all", "upgrade_all", is_flag=True, help="Upgrade all installed modules."
)
def upgrade(modules: Iterable[str], upgrade_all: bool):
    """
    Upgrade modules.
    """
    if upgrade_all:
        modules = config.installed_modules

    try:
        _modules = get_modules(modules)
    except ValueError as exc:
        raise click.ClickException(str(exc))

    for module in _modules:
        try:
            module.upgrade()
        except (DependenciesMissing, CalledProcessError) as exc:
            raise click.ClickException(str(exc))


@cli.command("list")
def _list():
    """
    List installed and available modules.
    """
    for module in all_modules:
        if module.name in config.installed_modules:
            click.echo(f"{module.name} - installed")
        else:
            click.echo(module.name)


@cli.command()
def edit():
    """
    Open the repo for editing.
    """
    shell.run(f"$EDITOR {config.root_dir}")
