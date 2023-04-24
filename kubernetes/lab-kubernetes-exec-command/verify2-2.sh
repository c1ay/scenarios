#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep nginx-busybox | grep ls | grep -Eq exec
