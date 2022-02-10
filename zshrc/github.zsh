alias clg='clear && gh pr status && git branch'

# "Git refresh"
# This assumes the oh-my-zsh git plugin is installed as well as my git config.
# It's a shortcut for 'gcml && git gone && clg', which I use a lot.
alias grf=': \
  && git checkout $(git_main_branch) \
  && git pull \
  && git gone \
  && clear \
  && gh pr status \
  && git branch \
  && :'

# Create a new PR in the origin repo
function newpr() {
  currentBranch=$(git branch --show-current)

  git push --set-upstream origin $currentBranch
  gh pr create --fill --web --head $currentBranch
}

alias gh-merged='\
  gh pr list \
  --author=@me --state=merged \
  --search="closed:>$(date -v-7d +%Y-%m-%d) sort:updated-desc"\
'
