#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep run | grep job1
minikube kubectl -- describe pods job1
