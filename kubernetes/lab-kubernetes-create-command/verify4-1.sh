#!/bin/bash
cat ~/.zsh_history | grep kubectl | grep -Eq create
minikube kubectl -- get secrets -n mynamespace | grep mysecret
