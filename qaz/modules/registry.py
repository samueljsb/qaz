from __future__ import annotations

from .base import Module

registry = {}


def register(cls: type[Module]) -> Module:
    assert (
        cls.name not in registry
    ), f"Module with name '{cls.name}' is already registered"

    module = cls()
    registry[cls.name.casefold()] = module

    return module


def populate() -> None:
    """
    Populate the registry.
    """
    import qaz_modules  # noqa: F401
