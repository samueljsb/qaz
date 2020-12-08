import click


def message(msg: str):
    click.secho(msg, bold=True, err=True)


def error(msg: str):
    click.secho(msg, fg="red", bold=True, err=True)


def command(command: str):
    click.secho(f"$ {command}", bold=True, fg="yellow", err=True)
