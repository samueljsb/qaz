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
