#!/bin/zsh

if [ -d ~/project/tmp ] && [ -d ~/project/tmp/dir ]; then
  exit 0
else
  exit 1
fi
