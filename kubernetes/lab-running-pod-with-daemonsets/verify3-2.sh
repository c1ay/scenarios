#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep get | grep pod | grep app=myapp
