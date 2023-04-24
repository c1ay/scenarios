#!/bin/zsh

cd ~/project/myrepo

git branch | grep 'branch-to-delete'
RS=$?
git branch | grep 'new-name'
RS1=$?
if [ $RS -eq 1 ] && [ $RS1 -eq 0 ]; then
  exit 0
else
  exit 1
fi
