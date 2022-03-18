# Create a new directory with virtual environment in /tmp.
# This overwrites the function from python.zsh
function tmpvenv(){
  # Create the new tmp directory.
  # Exit early if this fails.
  mkdir /tmp/$1 || return 1
  cd /tmp/$1

  virtualenv venv
  ./venv/bin/pip install black flake8 isort mypy rich

  . venv/bin/activate

  return 0
}
