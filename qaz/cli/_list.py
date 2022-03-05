from __future__ import annotations

import humanize

from qaz.modules.registry import registry


def output_modules_lists() -> None:
    """
    Print the installed and available modules.
    """
    installed_modules: list[tuple[str, str]] = []
    not_installed_modules: list[str] = []
    for module in sorted(
        registry.modules.values(), key=lambda module: module.name.casefold()
    ):
        if module.is_installed:
            installed_modules.append(
                (
                    module.name,
                    humanize.naturaltime(module.last_upgraded_at) or "",
                )
            )
        else:
            not_installed_modules.append(module.name)

    title_row = ("Module", "Last updated at")
    col_widths = (
        max(len(m[0]) for m in installed_modules + [title_row]),
        max(len(m[1]) for m in installed_modules + [title_row]),
    )

    _print_row(title_row, col_widths)
    print("-" * col_widths[0], "-" * col_widths[1])
    for row in installed_modules:
        _print_row(row, col_widths)

    print()
    print("Available modules:")
    for name in not_installed_modules:
        print("-", name)


def _print_row(row: tuple[str, str], col_widths: tuple[int, int]) -> None:
    cells = (r.ljust(w) for r, w in zip(row, col_widths))
    print(*cells)
