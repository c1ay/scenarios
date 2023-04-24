#!/bin/zsh

if [ -f ~/project/result1.txt ]; then

  RS=$(diff ~/project/result1.txt /tmp/verify.txt | wc -l)
  if [ $RS -eq 0 ]; then
    exit 0
  else
    exit 1
  fi
else
  exit 1
fi
