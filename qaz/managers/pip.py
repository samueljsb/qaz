from . import shell


def install_or_upgrade_package(package: str) -> None:
    shell.run(f"python -m pip install --upgrade {package}")
