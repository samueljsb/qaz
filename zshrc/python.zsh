export PYTHONSTARTUP=~/.config/pythonstartup.py

export PIP_REQUIRE_VIRTUALENV=1

if [ -x "$(command -v py)" ]; then
  alias python=py
else
  alias python=python3
fi

# Django
alias django='python manage.py'

alias zen="python -c 'import this'"

# Create a new directory with virtual environment in /tmp.
function tmpvenv(){
  if [ $1 ]; then
    dirname=$1
  else
    dirname="tmpvenv-$RANDOM"
  fi

  # Create the new tmp directory.
  # Exit early if this fails.
  mkdir /tmp/$dirname || return 1
  cd /tmp/$dirname

  if [ -x "$(command -v virtualenv)" ]; then
    virtualenv venv
  else
    python -m venv venv
  fi

  ./venv/bin/pip install black isort flake8 mypy rich

  . venv/bin/activate

  return 0
}

# Kill mypy processes.
# Sometimes I end up with lots of concurrent mypy processes, which hog the CPU.
# This kills them all.
alias kill-mypy="ps -x | grep -E 'python[\d.]* -m mypy' | grep -v grep | tee /dev/stderr | awk '{print \$1}' | xargs kill -9"
