# git fixup alias to select the commit to fix up
alias gfu='git log --pretty=format:"%h %s" --no-merges $(git_main_branch).. | fzf | cut -c -7 | xargs -o git commit --fixup'
alias gfun='git log --pretty=format:"%h %s" --no-merges $(git_main_branch).. | fzf | cut -c -7 | xargs -o git commit -n --fixup'

# Use fzf to find a file in a git repo and open it in the editor.
function ef(){
  git ls-files | fzf --select-1 --multi --print0 --query=$@ | xargs -0 $EDITOR
}
