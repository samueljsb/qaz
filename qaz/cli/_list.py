import datetime

import humanize
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from qaz.modules import base as modules_base
from qaz.modules import queries as module_queries


def output_modules_lists() -> None:
    """
    Print the installed and available modules.
    """
    console = Console()

    installed_table = Table("Name", "Last updated")
    not_installed_modules = []

    all_modules = module_queries.get_all_modules()
    for module in sorted(
        all_modules.values(), key=lambda module: module.name.casefold()
    ):
        if module_queries.is_module_installed(module):
            _add_module_to_table(installed_table, module)
        else:
            not_installed_modules.append(module)

    console.print(Panel("[bold][green]✓[/green]  Installed modules[/bold]"))
    console.print(installed_table)

    console.print(Panel("[bold]   Available modules[/bold]"))
    for module in not_installed_modules:
        console.print(module.name)


def _add_module_to_table(table: Table, module: modules_base.Module) -> None:
    if last_upgraded_at := module_queries.get_last_upgraded_at(module):
        last_upgraded = humanize.naturaltime(datetime.datetime.now() - last_upgraded_at)
    else:
        last_upgraded = "[dim]unknown[/]"

    table.add_row(module.name, last_upgraded)