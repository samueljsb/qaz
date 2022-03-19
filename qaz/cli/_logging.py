from __future__ import annotations

import logging
from typing import Any

import click


class ClickHandler(logging.Handler):
    style_kwargs: dict[int, dict[str, Any]] = {
        logging.DEBUG: dict(fg="bright_white", err=True),
        logging.INFO: dict(bold=True, err=True),
        logging.WARNING: dict(fg="bright_black", bg="yellow", bold=True, err=True),
        logging.ERROR: dict(fg="bright_red", bold=True, err=True),
        logging.CRITICAL: dict(fg="bright_white", bg="red", err=True),
    }

    def emit(self, record: logging.LogRecord) -> None:
        try:
            msg = self.format(record)
            style_kwargs = self.style_kwargs.get(record.levelno, {})
            click.secho(msg, **style_kwargs)
        except Exception:
            self.handleError(record)


def configure_logging() -> None:
    """Configure both the core qaz logger and the logger for the module plugins."""
    loggers = [logging.getLogger("qaz"), logging.getLogger("qaz_modules")]
    for logger in loggers:
        logger.handlers = [ClickHandler()]
        logger.propagate = False
        logger.setLevel(logging.DEBUG)
