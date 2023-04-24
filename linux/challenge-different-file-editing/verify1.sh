#!/bin/zsh

cd ~/project/myrepo
RS=$(ls | wc -l)
if [ $RS -eq 0 ]; then
  exit 0
else
  exit 1
fi
