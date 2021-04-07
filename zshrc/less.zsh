# The -X flag breaks mouse-wheel support, but it's unneeded for less >= 530.
# We remove it from the default set in `_zsh.zsh` when we upgrade less.
export LESS='-SRF --tabs=4'
