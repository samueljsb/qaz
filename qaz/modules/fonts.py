from pathlib import Path

from qaz.modules.git import GitModule
from qaz.utils import output, shell


FONTS = ["Hack"]


class NerdFonts(GitModule):
    name = "nerd-fonts"
    repo_url = "https://github.com/ryanoasis/nerd-fonts.git"
    repo_path = Path().home() / ".nerd-fonts"
    additional_clone_options = ["--depth=1"]

    def install_action(self):
        output.message("... this might take a while!")
        super().install_action()

        for font_name in FONTS:
            shell.run(f"{self.repo_path / 'install.sh'} {font_name}")

    def upgrade_action(self):
        super().upgrade_action()

        for font_name in FONTS:
            shell.run(f"{self.repo_path / 'install.sh'} {font_name}")
