alias gpp='git push --set-upstream origin $(git branch --show-current)'
alias gfu='git fu'
alias glrbom='git pull --rebase origin master'

# These assume the oh-my-zsh git plugin is installed.
# A shortcut for 'git checkout $(git_main_branch) && git pull'.
alias gcml='gcm && gl'
alias clb='clear; PAGER= git log $(git_main_branch)..HEAD --oneline'
