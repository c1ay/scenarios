#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep run | grep nginx-pod
minikube kubectl -- get pods | grep nginx-pod
