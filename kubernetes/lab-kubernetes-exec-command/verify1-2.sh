#!/bin/bash
cat ~/.zsh_history | grep kubectl | grep create
cat ~/.zsh_history | grep kubectl | grep nginx | grep v | grep -Eq exec
