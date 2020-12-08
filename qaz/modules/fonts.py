from pathlib import Path

from qaz.modules.git import GitModule
from qaz.utils import output, shell


FONTS = ["Hack"]


class NerdFonts(GitModule):
    name = "nerd-fonts"
    repo_url = "https://github.com/ryanoasis/nerd-fonts.git"
    repo_path = Path().home() / ".nerd-fonts"
    additional_clone_options = ["--depth=1"]

    def install_action(self) -> None:
        output.message("... this might take a while!")
        super().install_action()

        for font_name in FONTS:
            output.message(f"... installing font: {font_name} ...")
            shell.run(f"{self.repo_path / 'install.sh'} {font_name}")
            output.message(f"... ... {font_name} installed!")

    def upgrade_action(self) -> None:
        super().upgrade_action()

        for font_name in FONTS:
            output.message(f"... installing font: {font_name} ...")
            shell.run(f"{self.repo_path / 'install.sh'} {font_name}")
            output.message(f"... ... {font_name} installed!")
