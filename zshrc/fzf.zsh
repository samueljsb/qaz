function gfu(){
  commit_sha=$(git log --pretty=format:"%h %s" --no-merges $(_git_main_branch).. | fzf | cut -c -7)

  git commit --fixup $commit_sha $@
}

# Use fzf to find a file in a git repo and open it in the editor.
function ef(){
  git ls-files | fzf --select-1 --multi --print0 --query=$@ | xargs -0 $EDITOR
}
