# Show/hide hidden files in the Finder
alias showfiles="defaults write com.apple.finder AppleShowAllFiles -bool true && killall Finder"
alias hidefiles="defaults write com.apple.finder AppleShowAllFiles -bool false && killall Finder"

# Prefer GNU tools over the MacOS BSD ones.
export GNUBINS="$(find /usr/local/opt -type d -follow -name gnubin -print)";
for bindir in ${GNUBINS[@]}; do
  export PATH=$bindir:$PATH;
done;
