import subprocess

from .base import InstallResult, Manager, UpgradeResult


class Homebrew(Manager):
    @classmethod
    def install(cls, name: str, /) -> InstallResult:
        # Get the current version of this formula.
        if version := cls._version(name):
            return InstallResult.already_installed(version=version)

        # Install.
        proc = subprocess.run(
            f"brew install {name}",
            shell=True,
            text=True,
            capture_output=True,
        )
        if proc.returncode != 0:
            return InstallResult.error(process=proc)

        # Get the new version.
        version = cls._version(name)
        return InstallResult.installed(version=version, process=proc)

    @classmethod
    def upgrade(cls, name: str, /) -> UpgradeResult:
        # Get the current version of this formula.
        from_version = cls._version(name)

        # Upgrade.
        proc = subprocess.run(
            f"brew upgrade {name}",
            shell=True,
            text=True,
            capture_output=True,
        )
        if proc.returncode != 0:
            return UpgradeResult.error(process=proc)

        # Get the new version.
        version = cls._version(name)
        return UpgradeResult.upgraded(
            from_version=from_version, to_version=version, process=proc
        )

    @staticmethod
    def _version(name: str) -> str:
        proc = subprocess.run(
            f"brew list --versions {name}",
            shell=True,
            text=True,
            capture_output=True,
        )

        if not proc.stdout:  # not installed
            return ""
        return proc.stdout.split()[-1]
