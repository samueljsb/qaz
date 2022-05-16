# Find the main branch of this repo.
_git_main_branch () {
  git branch 2> /dev/null \
  | grep -o -m 1 \
    -e ' main$' \
    -e ' master$' \
  | xargs \
  || return
}


alias gpp='git push --set-upstream origin $(git branch --show-current)'
alias glrbom='git pull --rebase origin master'

alias gcml='gcm && gl'
alias clb='clear; PAGER= git log $(_git_main_branch)..HEAD --oneline'

function co-author(){
  git log --author=$1 | grep -m 1 $1 | gsed 's/Author/Co-authored-by/'
}
