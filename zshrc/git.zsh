# Find the main branch of this repo.
_git_main_branch () {
  git branch 2> /dev/null \
  | grep -o -m 1 \
    -e ' main$' \
    -e ' master$' \
  | xargs \
  || return
}

_git_main_branch_origin () {
    git rev-parse --abbrev-ref origin/HEAD | cut -d/ -f2-
}


alias gpp='git push --set-upstream origin $(git branch --show-current)'
alias glrbom='git pull --rebase origin master'

alias gcml='gcm && gl'
alias clb='clear; PAGER= git log $(_git_main_branch)..HEAD --oneline'

function co-author(){
  git log --author=$1 | grep -m 1 $1 | gsed 's/Author/Co-authored-by/'
}

# Aliases from OMZ
alias ga='git add'
alias gb='git branch'
alias gbda='git branch --no-color --merged | command grep -vE "^([+*]|\s*$(_git_main_branch)\s*$)" | command xargs -r git branch -d 2>/dev/null'
alias gc='git commit'
alias gc!='git commit --amend'
alias gcn!='git commit --no-edit --amend'
alias gca='git commit --all'
alias gca!='git commit --all --amend'
alias gcan!='git commit --all --no-edit --amend'
alias gcm='git checkout $(_git_main_branch)'
alias gco='git checkout'
alias gcp='git cherry-pick'
alias gd='git diff'
alias gl='git pull'
alias glog='git log --oneline --decorate --graph'
alias gpf='git push --force-with-lease'
alias grb='git rebase'
alias grbc='git rebase --continue'
alias grbm='git rebase $(_git_main_branch)'
alias gst='git status'
alias gsw='git switch'
alias gswc='git switch -c'
alias gswm='git switch $(_git_main_branch)'

alias gwip='git add -A; git rm $(git ls-files --deleted) 2> /dev/null; git commit --no-verify --no-gpg-sign -m "--wip-- [skip ci]"'

alias git-branches="git branch --format='%(color:green)%(HEAD)%(color:reset) %(if)%(upstream)%(then)%(else)%(color:dim)%(end)%(refname:short)%(color:reset) %(color:blue)%(upstream:track)%(color:reset)'"

# "Git refresh"
#   - gbda: delete all local merged branches
alias grf=': \
  && git checkout $(_git_main_branch) \
  && git pull origin $(_git_main_branch_origin) \
  && gbda \
  && clear \
  && git-branches \
  && :'
