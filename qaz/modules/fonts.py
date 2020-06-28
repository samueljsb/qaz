from pathlib import Path

from qaz.modules.git import GitModule
from qaz.utils import message, run


FONTS = ["Hack"]


class NerdFonts(GitModule):
    """Developer targeted fonts with a high number of glyphs."""

    name = "nerd-fonts"
    repo_url = "https://github.com/ryanoasis/nerd-fonts.git"
    repo_path = Path().home() / ".nerd-fonts"
    additional_clone_options = ["--depth=1"]

    def install_action(self) -> None:
        """Clone the repo and install fonts."""
        message("... this might take a while!")
        super().install_action()

        for font_name in FONTS:
            message(f"... installing font: {font_name} ...")
            run(f"{self.repo_path / 'install.sh'} {font_name}")
            message(f"... ... {font_name} installed!")

    def upgrade_action(self) -> None:
        """Pull the repo and install fonts."""
        super().upgrade_action()

        for font_name in FONTS:
            message(f"... installing font: {font_name} ...")
            run(f"{self.repo_path / 'install.sh'} {font_name}")
            message(f"... ... {font_name} installed!")
