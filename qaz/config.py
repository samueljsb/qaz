import json
from pathlib import Path
from typing import Dict, List, TypedDict


CONFIG_FILE = Path.home() / ".config/qaz.json"


class ModuleConfig(TypedDict):
    installed: bool


class Config(TypedDict):
    root_dir: str
    modules: Dict[str, ModuleConfig]


def create_new_config_file(root_dir: str):
    assert not CONFIG_FILE.exists(), f"Config file already exists at {CONFIG_FILE}"

    config = Config(root_dir=root_dir, modules=dict())
    _save_config_to_file(config)


def get_root_dir() -> Path:
    config = _load_config_from_file()
    return Path(config["root_dir"])


def is_module_installed(name: str) -> bool:
    return name in get_installed_module_names()


def set_module_installed(name: str):
    config = _load_config_from_file()

    if module_cfg := config["modules"].get(name):
        module_cfg["installed"] = True
    else:
        config["modules"]["name"] = ModuleConfig(installed=True)

    _save_config_to_file(config)


def get_installed_module_names() -> List[str]:
    config = _load_config_from_file()
    return [
        name
        for name, module_cfg in config["modules"].items()
        if module_cfg["installed"]
    ]


def _load_config_from_file() -> Config:
    return json.loads(CONFIG_FILE.read_text())


def _save_config_to_file(config: Config):
    CONFIG_FILE.write_text(json.dumps(config))
