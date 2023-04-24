#!/bin/zsh

cd ~/project/myrepo
git config --list | grep "labex"
RS=$?
git config --list | grep "janesmith"
RS1=$?

if [[ $RS -eq 0 || $RS1 -eq 0 ]]; then
  exit 0
else
  exit 1
fi
