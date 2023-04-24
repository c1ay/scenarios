#!/bin/zsh

if [ -f ~/project/result.txt ]; then

  RS=$(diff ~/project/result.txt /tmp/verify.txt | wc -l)
  if [ $RS -eq 0 ]; then
    exit 0
  else
    exit 1
  fi

else
  exit 1
fi
