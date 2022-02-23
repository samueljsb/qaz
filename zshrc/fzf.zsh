# git fixup alias to select the commit to fix up
alias gfu="git log --pretty=format:'%h %s' --no-merges $(git_main_branch).. | fzf | cut -c -7 | xargs -o git commit --fixup"
