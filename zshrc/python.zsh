export PYTHONSTARTUP=~/.config/pythonstartup.py

# Django
alias django='python manage.py'

# Create a new directory with virtual environment in /tmp.
function tmpvenv(){
  # Create the new tmp directory.
  # Exit early if this fails.
  mkdir /tmp/$1 || return 1
  cd /tmp/$1

  python -m venv .venv
  ./.venv/bin/pip install black isort flake8 mypy

  . .venv/bin/activate

  return 0
}

# Kill mypy processes.
# Sometimes I end up with lots of concurrent mypy processes, which hog the CPU.
# This kills them all.
alias kill-mypy="'ps -x | grep 'python3 -m mypy' | grep -v grep | awk '{print $2}' | xargs kill -9'"
