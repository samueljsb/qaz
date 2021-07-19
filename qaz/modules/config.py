COMMON_MODULES = (
    "qaz_modules.asdf.ASDF",
    "qaz_modules.brew.Homebrew",
    "qaz_modules.docker.LazyDocker",
    "qaz_modules.fonts.NerdFonts",
    "qaz_modules.git.Git",
    "qaz_modules.git.GitHubCLI",
    "qaz_modules.git.LazyGit",
    "qaz_modules.git.DiffSoFancy",
    "qaz_modules.nodejs.NodeJS",
    "qaz_modules.nodejs.Yarn",
    "qaz_modules.python.Python",
    "qaz_modules.python.Poetry",
    "qaz_modules.python.Rich",
    "qaz_modules.python.Pipx",
    "qaz_modules.python.Bpython",
    "qaz_modules.python.Tox",
    "qaz_modules.ruby.Ruby",
    "qaz_modules.rust.Rust",
    "qaz_modules.starship.Starship",
    "qaz_modules.tools.Bat",
    "qaz_modules.tools.Exa",
    "qaz_modules.tools.Figlet",
    "qaz_modules.tools.Less",
    "qaz_modules.tools.TrashCLI",
    "qaz_modules.vim.Vim",
    "qaz_modules.vscode.VSCode",
    "qaz_modules.zsh.OhMyZSH",
)

# These modules are only available on MacOS.
MACOS_MODULES = (
    "qaz_modules.docker.MacOSDocker",
    "qaz_modules.iterm2.ITerm2",
    "qaz_modules.latex.MacTex",
    "qaz_modules.macos.MacOS",
    "qaz_modules.macos.QuickLookExtensions",
    "qaz_modules.macos.Bartender",
    "qaz_modules.macos.Rectangle",
    "qaz_modules.tools.GNUSed",
    "qaz_modules.zsh.MacOSZsh",
)

# These modules are only available on Linux.
LINUX_MODULES = (
    "qaz_modules.docker.LinuxDocker",
    "qaz_modules.zsh.LinuxZsh",
)