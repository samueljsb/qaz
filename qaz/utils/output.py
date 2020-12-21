import rich.console


console = rich.console.Console()


def message(msg: str):
    console.print(msg, style="bold")


def error(msg: str):
    console.print("[bold red]Error:[/bold red]", msg, highlight=False)


def command(command: str):
    console.print(f"$ {command}", style="bold yellow", highlight=False)
