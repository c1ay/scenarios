#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep get | grep -Eq nodes
