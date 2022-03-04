from __future__ import annotations

import logging
from collections.abc import Iterable

import click

from qaz.application import git, install, setup, update, upgrade

from . import _list as list_modules
from . import _logging


logger = logging.getLogger(__name__)


@click.group()
def cli() -> None:
    """
    Manage your system configuration and install/update tools.
    """
    _logging.configure_logging()


@cli.command("setup")
@click.argument("root_dir")
def _setup(root_dir: str) -> None:
    """
    Install this tool.
    """
    logger.info("Installing qaz...")
    setup.setup_qaz(root_dir)
    logger.info("... qaz is installed.")


@cli.command("git")
@click.option("--author-name", prompt="Your git author name")
@click.option("--author-email", prompt="Your git author email")
def _git(author_name: str, author_email: str) -> None:
    """
    Configure git.
    """
    git.configure_git(author_name=author_name, author_email=author_email)


@cli.command("update")
def _update() -> None:
    """
    Update this tool.
    """
    update.update_qaz()


@cli.command("install")
@click.argument("modules", nargs=-1)
@click.pass_context
def _install(ctx: click.Context, modules: tuple[str]) -> None:
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
def _upgrade(ctx: click.Context, modules: Iterable[str]) -> None:
    """
    Upgrade modules.
    """
    try:
        upgrade.upgrade_modules(modules)
    except (upgrade.CannotUpgradeModule, ValueError) as exc:
        logger.error(exc)
        ctx.exit(1)


@cli.command("list")
def _list() -> None:
    """
    List installed and available modules.
    """
    list_modules.output_modules_lists()
