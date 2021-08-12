import datetime
import json
import logging
from pathlib import Path
from typing import Dict, Optional, TypedDict


logger = logging.getLogger(__name__)


SETTINGS_FILE_PATH = Path("~/.config/qaz.json").expanduser()


class ModuleSettings(TypedDict):
    """
    Saved settings for a module.
    """

    installed: bool  # is this module installed?
    last_upgraded: str  # timestamp of last upgrade in ISO 8601 format


class Settings(TypedDict):
    root_dir: str  # the root of the `qaz` repo
    modules: Dict[str, ModuleSettings]  # mappping of module name to module settings


# -------
# Queries
# -------


def get_root_dir() -> Path:
    """
    Get the root directory of the qaz repo.
    """
    settings = _load_settings_from_file()
    return Path(settings["root_dir"])


def is_module_installed(name: str) -> bool:
    """
    Check whether a module with the given name is recorded as having been installed.
    """
    settings = _load_settings_from_file()
    return name in settings["modules"]


def get_last_upgraded_at(name: str) -> Optional[datetime.datetime]:
    """
    Retrieve the timestamp of the last update to this module.
    """
    settings = _load_settings_from_file()

    if module_settings := settings["modules"].get(name):
        if timestamp := module_settings.get("last_upgraded"):
            return datetime.datetime.fromisoformat(timestamp)

    return None


# --------
# Mutators
# --------


def set_root_dir(root_dir: str) -> None:
    """
    Set the root directory of the qaz repo.
    """
    settings = _load_settings_from_file()
    settings["root_dir"] = root_dir
    _save_settings_to_file(settings)
    logger.debug("qaz root directory set to '%s'", root_dir)


def set_module_installed(name: str):
    """
    Set a module as having been installed
    """
    config = _load_settings_from_file()

    if module_settings := config["modules"].get(name):
        module_settings["installed"] = True
    else:
        # If there are no settings for this module yet, create them.
        config["modules"][name] = ModuleSettings(
            installed=True, last_upgraded=datetime.datetime.now().isoformat()
        )

    _save_settings_to_file(config)


def record_module_upgraded(
    name: str, upgraded_at: Optional[datetime.datetime] = None
) -> None:
    """
    Mark a module as having been upgraded.

    If no timestamp is passed in, the current time will be used.
    """
    upgraded_at = upgraded_at or datetime.datetime.now()

    config = _load_settings_from_file()

    if module_settings := config["modules"].get(name):
        module_settings["last_upgraded"] = upgraded_at.isoformat()
    else:
        # If there are no settings for this module yet, we cannot mark it as upgraded.
        raise ValueError(f"There is no information saved for the module '{name}'.")

    _save_settings_to_file(config)


# ---
# I/O
# ---


def _load_settings_from_file() -> Settings:
    if not SETTINGS_FILE_PATH.exists():
        logger.warning("Creating new settings file with no root directory.")
        return Settings(root_dir="", modules={})

    return json.loads(SETTINGS_FILE_PATH.read_text())


def _save_settings_to_file(settings: Settings):
    SETTINGS_FILE_PATH.write_text(json.dumps(settings))
