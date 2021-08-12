from qaz import settings
from qaz.managers import git, shell


def update_qaz() -> None:
    """
    Update QAZ.

    This pulls the latest version of QAZ and installs the necessary Python dependencies
    for this tool.
    """
    root_dir = settings.get_root_dir()
    git.pull(root_dir)
    shell.run(
        "poetry install --no-dev --remove-untracked",
        cwd=root_dir,
        env=dict(VIRTUAL_ENV=str(root_dir / "venv")),
    )
