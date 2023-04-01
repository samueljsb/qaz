#!/bin/bash

set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
HOOKS_DIR="$HERE/../git-hooks"

if [ $# -eq 0 ]; then
  REPO_ROOT="$(git rev-parse --show-toplevel)"
  cp $HOOKS_DIR/* $REPO_ROOT/.git/hooks
else
  cp $HOOKS_DIR/* $1
fi
