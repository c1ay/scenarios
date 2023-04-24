#!/bin/bash
cat ~/.zsh_history | grep kubectl | grep apply
minikube kubectl -- describe daemonset myapp-daemonset | grep busybox
