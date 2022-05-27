alias clg='clear && gh pr status && git branch'

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
