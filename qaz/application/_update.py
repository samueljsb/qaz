from qaz import settings
from qaz.managers import git
from qaz.managers import shell


def update() -> None:
    """
    Update QAZ.

    This pulls the latest version of QAZ and installs the necessary Python dependencies
    for this tool.
    """
    root_dir = settings.root_dir()
    git.pull(root_dir, with_stash=True)
    shell.run(f"{root_dir}/.venv/bin/python -m pip install --upgrade pip")
    shell.run(f"{root_dir}/.venv/bin/python -m pip install {root_dir}")

    shell.run("qaz configure")
