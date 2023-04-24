#!/bin/zsh

test -f "/home/labex/pod.yaml"
cat ~/.zsh_history | grep "apply.*pod.yaml"
kubectl get pods | grep secret-pod
