from typing import List

from qaz.utils import capture, run


def install(name: str) -> None:
    """Install an extension.

    Args:
        name: The name of the extension to install.

    """
    run(f"code --install-extension {name}")


def installed() -> List[str]:
    """Get a list of installed extensions."""
    return capture("code --list-extensions").split()
