from __future__ import annotations

import datetime
import importlib
import sys
from collections.abc import Iterable, Iterator

from qaz import settings

from . import base, config


class ModuleNotFound(Exception):
    """
    A module has not been configured with the given name.
    """


def is_module_installed(module: base.Module) -> bool:
    """
    Check if the given module has been installed.
    """
    return settings.is_module_installed(module.name)


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
    modules = {m.name.casefold(): m for m in all_modules()}
    for name in module_names:
        try:
            yield modules[name.casefold()]
        except KeyError:
            raise ModuleNotFound(f"No module configured with name '{name}'.")


def all_modules() -> Iterator[base.Module]:
    """
    Import all available modules.
    """
    module_paths: tuple[str, ...] = config.COMMON_MODULES
    if sys.platform == "darwin":
        module_paths = module_paths + config.MACOS_MODULES
    elif sys.platform == "Linux":
        module_paths = module_paths + config.LINUX_MODULES

    for module_path in module_paths:
        yield _import_module(module_path)()


def _import_module(dotted_path: str) -> type[base.Module]:
    """
    Import a module class.

    This is copied from Django's `import_string` function.
    """
    try:
        python_module_path, class_name = dotted_path.rsplit(".", 1)
    except ValueError as err:
        raise ImportError("%s doesn't look like a module path" % dotted_path) from err

    python_module = importlib.import_module(python_module_path)

    try:
        return getattr(python_module, class_name)
    except AttributeError as err:
        raise ImportError(
            'Python module "%s" does not define a "%s" attribute/class'
            % (python_module_path, class_name)
        ) from err
