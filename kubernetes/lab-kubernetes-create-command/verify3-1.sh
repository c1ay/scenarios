#!/bin/bash
cat ~/.zsh_history | grep kubectl | grep -Eq create
minikube kubectl -- get services -n mynamespace | grep myservice
