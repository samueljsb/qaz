# git fixup alais to select the commit to fix up
alias gfu="git log -n 50 --pretty=format:'%h %s' --no-merges | fzf | cut -c -7 | xargs -o git commit --fixup"
