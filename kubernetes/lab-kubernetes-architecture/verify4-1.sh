#!/bin/bash
cat ~/.zsh_history | grep kubectl | grep -Eq apply
minikube kubectl -- describe services nginx-service
