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

The installation script will install [asdf][] and Python and use these to set up
the tool and install zsh (which it will set as the default shell).

## Usage

The installation script links the installed entrypoint to `/usr/local/bin`, so
as long as that's in your `PATH` you can run qaz with:

```shell
qaz [OPTIONS] COMMAND [ARGS]...
```

## Adding modules

To add a module, create a class in the `qaz_modules` package that inherits from
`qaz.modules.base.Module` and implements its attributes and methods. The module
must then be configured by adding it to one of the tuples in
`qaz.modules.config`.

Any configuration files should be placed in `configfiles/`.

Any files that should be loaded by zsh at login (`.zshrc` files) must be placed
in `zshrc/`.

## Rationale

I used to manage my dotfiles with a fork of [holman does dotfiles][]. I liked
the modular approach, but found myself wanting to select which modules were used
on different machines (I don't need VS Code plugins installed on my headless
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
[pipx]: https://pipxproject.github.io/pipx/
[holman does dotfiles]: https://github.com/holman/dotfiles
