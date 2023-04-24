#!/bin/zsh

if [ -f ~/project/myrepo/file3.txt ] || [ -f ~/project/myrepo/dir2/file5.exe ]; then
  exit 1
else
  exit 0
fi
