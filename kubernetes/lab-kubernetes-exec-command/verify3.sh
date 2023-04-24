#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep nginx-busybox | grep 'it' | grep -Eq exec
