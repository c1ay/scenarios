#!/bin/zsh

cd ~/project/myrepo
RS=$(git config color.ui)
if [[ $RS = "true" ]]; then
  exit 0
else
  exit 1
fi
