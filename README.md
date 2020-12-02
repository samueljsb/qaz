# qaz

A tool for managing installation, upgrading, and configurations.

## Installation

Install this tool by cloning the repo and running the installation script:

```shell
git clone https://github.com/samueljsb/qaz.git .qaz
.qaz/install
```

The location of the cloned repo doesn't matter much. I like to put mine in
`~/.qaz`.

The installation script will install [asdf][], Python, and [Poetry][] and use
these to set up the tool and install zsh (which it will set as the default
shell).

## Usage

The installation script links the installed entrypoint to `/usr/local/bin`, so
as long as that's in your `PATH` you can run qaz with:

```shell
qaz [OPTIONS] COMMAND [ARGS]...
```

## Adding modules

To add a module, create a class that inherits from `qaz.module.Module` and
implements its attributes. If some action should be taken to install/upgrade the
module, these should be written in `install_action` and `upgrade_action`
methods. The module must then be imported in `qaz.modules.__init__` and added to
the `modules` or `mac_modules` list.

There are some subclasses of `qaz.module.Module` to help with common
installation methods:

- `qaz.modules.asdf.ASDFModule`: a plugin for [asdf][]
- `qaz.module.brew.BrewModule`: a formula from Homebrew
- `qaz.module.brew.BrewCaskModule`: a cask from Homebrew
- `qaz.module.git.GitModule`: a module installed by cloning a git repo
- `qaz.module.python.PipxModule`: a python package installed with [pipx][]

More detail on the usage of any `Module` subclass can be found in the class
definition.

Any configuration files should be placed in `configfiles/`.

Any files that should be loaded by zsh at login (`.zshrc` files) should be
placed in `zshrc/` with the lowercase of the name of the module followed by
`.zsh` (e.g. the module named `Python` would have a corresponding zsh file
`python.zsh`). If the name of the config file needs to differ from this pattern,
the name used can be included as a class attribute `zshrc_file`.

## Rationale

I used to manage my dotfiles with a fork of [holman does dotfiles][]. I liked
the modular approach, but found myself wanting to select which modules were used
on different machines (I don't ned VSCode plugins installed on my headless
Raspberry Pi). This led to writing installation and upgrade scripts and trying
to manage the installation status of different modules and only load their
configuration if they were installed. Quite frankly, this became a bit messy.
So I decided to rewrite the python CLI tool I'd made to manage everything and to
use Python classes as the module definitions. This makes everything neater and
more robust and a little easier for me to add modules in the future.

### Why "qaz"?

It's easy to type and `asdf` was taken. My previous repo was called `dotfiles`
but this is more than just symlinking some config files so I wanted it to have a
name that reflected that (`dotfiles upgrade python` doesn't make much sense to
me).

[asdf]: https://asdf-vm.com
[Poetry]: https://python-poetry.org
[pipx]: https://pipxproject.github.io/pipx/
[holman does dotfiles]: https://github.com/holman/dotfiles
