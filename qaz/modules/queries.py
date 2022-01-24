from __future__ import annotations

import datetime
import importlib
import sys
from collections.abc import Iterable

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


def modules_by_name(module_names: Iterable[str]) -> list[base.Module]:
    """
    Get a sequence of modules with the given names.

    Raises ModuleNotFound if a module with the requested name is not configured.

    N.B: lookup is done with casefolded names, so the input is case-insensitive.
    """
    # Casefold the names to make lookup case-insensitive.
    module_names = [name.casefold() for name in module_names]

    # Retrieve all of the configured modules.
    all_modules_ = all_modules()

    modules = []
    for name in module_names:
        # Try to get the module with the given name.
        try:
            module = all_modules_[name]
        except KeyError:
            raise ModuleNotFound(f"No module configured with name '{name}'.")
        modules.append(module)

    return modules


def all_modules() -> dict[str, base.Module]:
    """
    Import all available modules.

    Returns a mapping of casefolded module names to module instances.

    Raises RuntimeError if there is more than one module with a given name
    """
    module_paths: tuple[str, ...] = config.COMMON_MODULES
    if sys.platform == "darwin":
        module_paths = module_paths + config.MACOS_MODULES
    elif sys.platform == "Linux":
        module_paths = module_paths + config.LINUX_MODULES

    modules: dict[str, base.Module] = {}
    for module_path in module_paths:
        module = _import_module(module_path)()

        if module.name in modules:
            raise RuntimeError(f"Multiple modules configured with name '{module.name}'")
        modules[module.name.casefold()] = module

    return modules


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
