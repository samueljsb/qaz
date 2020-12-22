from pathlib import Path
from subprocess import CalledProcessError
from typing import Iterable, List, Tuple

import click

from qaz import config
from qaz.utils import output, shell

from .module import DependenciesMissing, Module, NotInstalled
from .modules import all_modules, get_modules


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
    config.create_new_config_file(root_dir)

    # Create installed dir
    zshrc_dir = Path.home().joinpath(".zshrc.d")
    zshrc_dir.mkdir(exist_ok=True)

    ALREADY_INSTALLED = ("asdf", "python", "poetry")
    install(ALREADY_INSTALLED)

    output.message("... qaz is installed.")


@cli.command()
def update():
    """
    Update this tool.
    """
    root_dir = config.get_root_dir()
    shell.run(f"git -C {root_dir} pull")
    shell.run("poetry install --remove-untracked", cwd=root_dir)


@cli.command()
@click.argument("modules", nargs=-1)
@click.pass_context
def install(ctx: click.Context, modules: Tuple[str]):
    """
    Install modules.
    """
    error = False
    for module in _get_modules(modules):
        try:
            output.message(f"Installing {module.name}...")
            module.install()
            output.message(f"... {module.name} installed!")
        except (DependenciesMissing, CalledProcessError) as exc:
            output.error(str(exc))
            error = True

    if error:
        ctx.exit(1)


@cli.command()
@click.argument("modules", nargs=-1)
@click.option(
    "-a", "--all", "upgrade_all", is_flag=True, help="Upgrade all installed modules."
)
@click.pass_context
def upgrade(ctx: click.Context, modules: Iterable[str], upgrade_all: bool):
    """
    Upgrade modules.
    """
    error = False
    if upgrade_all:
        modules = [m.name for m in all_modules if config.is_module_installed(m.name)]

    for module in _get_modules(modules):
        try:
            output.message(f"Upgrading {module.name}...")
            module.upgrade()
            output.message(f"... {module.name} upgraded!")
        except (DependenciesMissing, NotInstalled, CalledProcessError) as exc:
            output.error(str(exc))
            error = True

    if error:
        ctx.exit(1)


def _get_modules(module_names: Iterable[str]) -> List[Module]:
    try:
        return get_modules(module_names)
    except ValueError as exc:
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
