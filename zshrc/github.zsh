alias clg='clear && gh pr status && git branch'

# "Git refresh"
# This assumes the oh-my-zsh git plugin is installed:
#   - gcml: checkout the main branch and pull
#   - gbda: delete all local merged branches
alias grf=': \
  && gcml \
  && gbda \
  && clear \
  && gh pr status \
  && git branch \
  && :'

# Create a new PR in the origin repo
function newpr() {
  currentBranch=$(git branch --show-current)

  git push --set-upstream origin $currentBranch
  gh pr create --draft --fill --web --head $currentBranch
}

alias gh-merged='\
  gh pr list \
  --author=@me --state=merged \
  --search="closed:>$(date -v-7d +%Y-%m-%d) sort:updated-desc"\
'
