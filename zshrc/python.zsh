export PYTHONSTARTUP=~/.config/pythonstartup.py

export PIP_REQUIRE_VIRTUALENV=1

alias python=python3

export VIRTUALENV_CONFIG_FILE="$XDG_CONFIG_HOME/virtualenv/virtualenv.ini"

alias zen="python -c 'import this'"

alias tmpvenv='cd $(mktmpvenv -p black flake8 isort mypy rich); . venv/bin/activate'

# Kill mypy processes.
# Sometimes I end up with lots of concurrent mypy processes, which hog the CPU.
# This kills them all.
alias kill-mypy="ps -x | grep -E 'python[\d.]* -m mypy' | grep -v grep | tee /dev/stderr | awk '{print \$1}' | xargs kill -9"
