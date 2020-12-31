from qaz.utils import shell


def install_or_upgrade_package(package: str):
    shell.run(f"python -m pip install --upgrade {package}")
