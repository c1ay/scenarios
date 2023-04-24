#!/bin/zsh

test -f "/home/labex/my-secret.yaml"
cat ~/.zsh_history | grep "apply.*my-secret.yaml"
kubectl get secrets | grep my-secret
cat ~/.zsh_history | grep "get.*secrets"
