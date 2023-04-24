#!/bin/zsh

test -f "/home/labex/my-app.yaml"
cat ~/.zsh_history | grep "apply.*my-app.yaml"
kubectl get deployments | grep my-app
cat ~/.zsh_history | grep "get.*deployments"
