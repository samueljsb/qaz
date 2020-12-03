import json
from dataclasses import dataclass
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


@dataclass
class LegacyModuleConfig:
    """Configuration for a module."""

    installed: bool

    def to_dict(self) -> dict:
        """Create a dict representation of this configuration."""
        return dict(installed=self.installed)

    @staticmethod
    def to_dataclass(data: dict) -> "LegacyModuleConfig":
        """Create a ModuleConfig object from a dict representation."""
        return LegacyModuleConfig(installed=data["installed"])


class LegacyConfig:
    """Configuration object."""

    # Values to save
    modules: Dict[str, LegacyModuleConfig] = {}
    root_dir: Path  # The location of this repo

    # Properties
    fpath = Path.home() / ".config/qaz.json"  # The location of the configuration file

    def __init__(self, root_dir: str = "~/.qaz"):
        self.root_dir = Path(root_dir)

    @property
    def installed_modules(self) -> List[str]:
        """Modules which have been installed."""
        return [name for name, module in self.modules.items() if module.installed]

    def is_module_installed(self, name: str) -> bool:
        return name in self.installed_modules

    def set_module_installed(self, name: str):
        if name in self.modules:
            self.modules[name].installed = True
        else:
            self.modules[name] = LegacyModuleConfig(installed=True)
        self.save_to_file()

    def load_from_file(self) -> None:
        """Load the configuration from ~/.config/qaz.json."""
        if not self.fpath.exists():
            return
        with self.fpath.open() as fd:
            config = json.load(fd)
        self.modules = {
            name: LegacyModuleConfig.to_dataclass(cfg)
            for name, cfg in config["modules"].items()
        }
        self.root_dir = Path(config["root_dir"])

    def save_to_file(self):
        config = {
            "root_dir": str(self.root_dir),
            "modules": {name: cfg.to_dict() for name, cfg in self.modules.items()},
        }
        with self.fpath.open("w+") as fd:
            json.dump(config, fd)


legacy_config = LegacyConfig()
legacy_config.load_from_file()
