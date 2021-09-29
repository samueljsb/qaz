from pathlib import Path

import invoke


PROJECT_ROOT = Path(__file__).parent


# -------
# Linting
# -------


@invoke.task
def lint(ctx, fix=False):
    """
    Run all linting tasks.
    """
    with ctx.cd(PROJECT_ROOT):
        _isort(ctx, fix=fix)
        _black(ctx, fix=fix)
        _flake8(ctx)
        _mypy(ctx)
        _poetry_check(ctx)


def _isort(ctx, fix=False):
    if fix:
        print(">>> sorting imports...")
        ctx.run("isort .", pty=True)
    else:
        print(">>> checking imports...")
        ctx.run("isort --check-only .", pty=True)


def _black(ctx, fix=False):
    if fix:
        print(">>> auto-formatting...")
        ctx.run("black .", pty=True)
    else:
        print(">>> checking formatting...")
        ctx.run("black --check .", pty=True)


def _flake8(ctx):
    print(">>> linting...")
    ctx.run("flake8", pty=True)


def _mypy(ctx):
    print(">>> type-checking...")
    ctx.run("mypy .", pty=True)


def _poetry_check(ctx):
    print(">>> checking pyproject.toml...")
    ctx.run("poetry check", pty=True)
