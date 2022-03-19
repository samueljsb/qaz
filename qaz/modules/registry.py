from __future__ import annotations

from collections.abc import Iterator

from .base import Module


class Registry:
    def __init__(self) -> None:
        self.modules: dict[str, Module] = {}

    @property
    def installed_modules(self) -> Iterator[Module]:
        for module in self.modules.values():
            if module.is_installed:
                yield module

    def register(self, cls: type[Module]) -> Module:
        assert (
            cls.name not in self.modules
        ), f"Module with name '{cls.name}' is already registered"

        module = cls()
        self.modules[cls.name.casefold()] = module

        return module

    def populate(self) -> None:
        """Populate the registry."""
        import qaz_modules  # noqa: F401


registry = Registry()
registry.populate()
