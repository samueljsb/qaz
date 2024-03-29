function gfu(){
  commit_sha=$(git log --pretty=format:"%h %s" --no-merges origin/HEAD.. | fzf | cut -c -7)

  git commit --fixup $commit_sha $@
}

function gswf(){
  git branch --format='%(refname:short)' | fzf --select-1 --query=$@ | xargs git switch
}

# Use fzf to find a file in a git repo and open it in the editor.
function ef(){
  git ls-files | fzf --select-1 --multi --print0 --query=$@ | xargs -0 $EDITOR
}
