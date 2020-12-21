from contextlib import contextmanager

import rich.console


console = rich.console.Console()


def message(msg: str):
    console.print(msg, style="bold")


def error(msg: str):
    console.print("[bold red]Error:[/bold red]", msg, highlight=False)


def command(command: str):
    console.print(f"$ {command}", style="bold yellow", highlight=False)


@contextmanager
def status(status_msg: str, complete_msg: str = ""):
    with console.status(status_msg):
        yield

    if complete_msg:
        message(complete_msg)
