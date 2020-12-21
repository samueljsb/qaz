from pathlib import Path
from subprocess import CalledProcessError
from typing import Iterable, Tuple

import click

from qaz import config
from qaz.utils import output, shell

from .module import DependenciesMissing, NotInstalled
from .modules import ModuleNotFound, all_modules, get_modules


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
    with output.status("Installing qaz...", "Installed qaz 🎉"):

        # Create config
        config.create_new_config_file(root_dir)

        # Create installed dir
        zshrc_dir = Path.home().joinpath(".zshrc.d")
        zshrc_dir.mkdir(exist_ok=True)

        ALREADY_INSTALLED = ("asdf", "python", "poetry")
        install(ALREADY_INSTALLED)


@cli.command()
def update():
    """
    Update this tool.
    """
    root_dir = config.get_root_dir()

    with output.status("Updating qaz...", "Updated qaz 🥳"):
        shell.run(f"git -C {root_dir} pull")
        shell.run("poetry install --remove-untracked", cwd=root_dir)


@cli.command()
@click.argument("modules", nargs=-1)
def install(modules: Tuple[str]):
    """
    Install modules.
    """
    try:
        modules_to_install = get_modules(modules)
    except ModuleNotFound as exc:
        output.error(str(exc))
        raise click.Abort()

    for module in modules_to_install:
        with output.status(
            f"Installing {module.name}...", f"Installed {module.name} 🎉"
        ):
            try:
                module.install()
            except DependenciesMissing as exc:
                output.error(str(exc))
                raise click.Abort()
            except CalledProcessError as exc:
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
        modules = [m.name for m in all_modules if config.is_module_installed(m.name)]

    try:
        modules_to_upgrade = get_modules(modules)
    except ModuleNotFound as exc:
        output.error(str(exc))
        raise click.Abort()

    for module in modules_to_upgrade:
        with output.status(f"Upgrading {module.name}...", f"Upgraded {module.name} 🥳"):
            try:
                module.upgrade()
            except (DependenciesMissing, NotInstalled) as exc:
                output.error(str(exc))
                raise click.Abort()
            except CalledProcessError as exc:
                raise click.ClickException(str(exc))


@cli.command("list")
def _list():
    """
    List installed and available modules.
    """
    for module in sorted(all_modules, key=lambda m: m.name.casefold()):
        if config.is_module_installed(module.name):
            status = click.style("✓", fg="green", bold=True)
        else:
            status = ""
        click.echo(f"{status:1} {module.name}")


@cli.command()
def edit():
    """
    Open the repo for editing.
    """
    shell.run(f"$EDITOR {config.root_dir}")
