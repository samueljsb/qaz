from __future__ import annotations

import logging
from collections.abc import Iterable

import click

from qaz import application

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
    application.setup(root_dir)
    logger.info("... qaz is installed.")


@cli.command("git")
@click.option("--author-name", prompt="Your git author name")
@click.option("--author-email", prompt="Your git author email")
def _git(author_name: str, author_email: str) -> None:
    """
    Configure git.
    """
    public_key = application.configure_git(
        author_name=author_name, author_email=author_email
    )
    logger.info(f"Add your public key to GitHub:\n    {public_key}")


@cli.command("update")
def _update() -> None:
    """
    Update this tool.
    """
    application.update()


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
            installed_version = application.install_module(name)
        except KeyError:
            logger.error("... unknown module name '%s'.", name)
            ctx.exit(1)
        except Exception:
            logger.exception("... error installing %s.", name)
            ctx.exit(1)
        else:
            if installed_version:
                logger.info("... %s installed (%s).", name, installed_version)
            else:
                logger.info("... %s installed.", name)


@cli.command("configure")
def _configure() -> None:
    """
    Configure all installed modules.
    """
    application.configure()


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
            from_version, to_version = application.upgrade_module(name)
        except KeyError:
            logger.error("... unknown module name '%s'.", name)
            ctx.exit(1)
        except application.NotInstalled:
            logger.error("... %s is not installed.", name)
            ctx.exit(1)
        except Exception:
            logger.exception("... error upgrading %s.", name)
            ctx.exit(1)
        else:
            if from_version and to_version and from_version != to_version:
                logger.info(
                    "... %s upgraded (%s -> %s).", name, from_version, to_version
                )
            else:
                logger.info("... %s is already up to date (%s).", name, to_version)


@cli.command("list")
def _list() -> None:
    """
    List installed and available modules.
    """
    list_modules.output_modules_lists()
