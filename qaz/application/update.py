from qaz import settings
from qaz.managers import shell


def update_qaz() -> None:
    """
    Update QAZ.

    This pulls the latest version of QAZ and installs the necessary Python dependencies
    for this tool.
    """
    root_dir = settings.get_root_dir()
    shell.run(f"git -C {root_dir} pull")
    shell.run(f"{root_dir}/.venv/bin/python -m pip install --upgrade pip")
    shell.run(f"{root_dir}/.venv/bin/python -m pip install {root_dir}")
