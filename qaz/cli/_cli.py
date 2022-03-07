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
    public_key = git.configure_git(author_name=author_name, author_email=author_email)
    logger.info(f"Add your public key to GitHub:\n    {public_key}")


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
    for name in modules:
        logger.info("Installing %s...", name)
        try:
            install.install_module(name)
        except install.ModuleAlreadyInstalled:
            logger.warning("...%s is already installed.", name)
            continue
        except KeyError:
            logger.exception("... unknown module name '%s'.", name)
            ctx.exit(1)
        except install.CannotInstallModule:
            logger.exception("... error installing %s.", name)
            ctx.exit(1)
        else:
            logger.info("...%s installed.", name)


@cli.command("upgrade")
@click.argument("modules", nargs=-1)
@click.pass_context
def _upgrade(ctx: click.Context, modules: Iterable[str]) -> None:
    """
    Upgrade modules.
    """
    for name in modules:
        logger.info("Upgrading %s...", name)
        try:
            upgrade.upgrade_module(name)
        except KeyError:
            logger.exception("... unknown module name '%s'.", name)
            ctx.exit(1)
        except upgrade.NotInstalled:
            logger.exception("...%s is not installed.", name)
            ctx.exit(1)
        except install.CannotInstallModule:
            logger.exception("... error upgrading %s.", name)
            ctx.exit(1)
        else:
            logger.info("...%s upgraded.", name)


@cli.command("list")
def _list() -> None:
    """
    List installed and available modules.
    """
    list_modules.output_modules_lists()
