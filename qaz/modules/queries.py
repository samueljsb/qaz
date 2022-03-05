from __future__ import annotations

import datetime
from collections.abc import Iterable, Iterator

from qaz import settings

from . import base
from .registry import populate, registry


class ModuleNotFound(Exception):
    """
    A module has not been configured with the given name.
    """


# Populate the registry if we are going to query it.
populate()


def last_upgraded_at(module: base.Module) -> datetime.datetime | None:
    """
    Get the timestamp of the last time this module was upgraded.
    """
    return settings.last_upgraded_at(module.name)


def modules_by_name(module_names: Iterable[str]) -> Iterator[base.Module]:
    """
    Get the modules with the given names.

    Raises ModuleNotFound if a module with the requested name is not configured.
    """
    for name in module_names:
        try:
            yield registry[name.casefold()]
        except KeyError:
            raise ModuleNotFound(f"No module configured with name '{name}'.")
