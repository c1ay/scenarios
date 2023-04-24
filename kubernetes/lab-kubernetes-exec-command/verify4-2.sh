#!/bin/bash
minikube kubectl -- describe pod nginx-env | grep MY_VAR | grep my-value
cat ~/.zsh_history | grep kubectl | grep nginx-env | grep c | grep -Eq exec
