from typing import List


class DotfilesError(Exception):
    """Base Exception for qaz management tool."""

    pass


class DependenciesMissing(DotfilesError):
    """Error raised when dependencies of a module are not installed."""

    def __init__(self, dependencies: List[str]) -> None:
        self.dependencies = dependencies

    def __str__(self) -> str:
        return f"Dependencies missing: {', '.join(self.dependencies)}."


class ModuleDoesNotExist(DotfilesError):
    """Error raised when the requested module does not exist."""

    def __init__(self, module_name: str) -> None:
        self.module_name = module_name

    def __str__(self) -> str:
        return f"Module '{self.module_name}' does not exist."
