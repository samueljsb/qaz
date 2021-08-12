import logging
from typing import Iterable, Tuple

import click

from qaz.application import install, setup, update, upgrade
from qaz.modules import queries as module_queries

from . import _logging


logger = logging.getLogger(__name__)


@click.group()
def cli():
    """
    Manage your system configuration and install/update tools.
    """
    _logging.configure_logging()


@cli.command("setup")
@click.argument("root_dir")
def _setup(root_dir: str):
    """
    Install this tool and the basics.
    """
    logger.info("Installing qaz...")
    setup.setup_qaz(root_dir)
    logger.info("... qaz is installed.")


@cli.command("update")
def _update():
    """
    Update this tool.
    """
    update.update_qaz()


@cli.command("install")
@click.argument("modules", nargs=-1)
@click.pass_context
def _install(ctx: click.Context, modules: Tuple[str]):
    """
    Install modules.
    """
    try:
        install.install_modules(modules)
    except (install.CannotInstallModule, ValueError) as exc:
        logger.error(exc)
        ctx.exit(1)


@cli.command("upgrade")
@click.argument("modules", nargs=-1)
@click.pass_context
def _upgrade(ctx: click.Context, modules: Iterable[str]):
    """
    Upgrade modules.
    """
    try:
        upgrade.upgrade_modules(modules)
    except (upgrade.CannotUpgradeModule, ValueError) as exc:
        logger.error(exc)
        ctx.exit(1)


@cli.command("list")
def _list():
    """
    List installed and available modules.
    """
    all_modules = module_queries.get_all_modules()
    for module in sorted(all_modules.values(), key=lambda module: module.name):
        if module_queries.is_module_installed(module):
            status = click.style("✓", fg="green", bold=True)
        else:
            status = ""
        click.echo(f"{status:1} {module.name}")
