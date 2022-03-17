alias gpp='git push --set-upstream origin $(git branch --show-current)'
alias glrbom='git pull --rebase origin master'

# These assume the oh-my-zsh git plugin is installed.
# A shortcut for 'git checkout $(git_main_branch) && git pull'.
alias gcml='gcm && gl'
alias clb='clear; PAGER= git log $(git_main_branch)..HEAD --oneline'

function co-author(){
  git log --author=$1 | grep -m 1 $1 | gsed 's/Author/Co-authored-by/'
}
