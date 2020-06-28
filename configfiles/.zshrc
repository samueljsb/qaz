# Load all config files
for file in $HOME/.zshrc.d/*.zsh; do
  source $file
done

# Load local config
if [[ -a ~/.localrc ]]
then
  source ~/.localrc
fi
