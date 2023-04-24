#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep -Eq apply
minikube kubectl -- get namespace | grep mynamespace
