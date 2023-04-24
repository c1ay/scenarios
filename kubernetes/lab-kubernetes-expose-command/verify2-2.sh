#!/bin/bash

NODE_PORT=$(minikube kubectl -- get svc hello-service -o jsonpath='{.spec.ports[0].nodePort}')
NODE_IP=$(minikube kubectl -- get nodes -o jsonpath='{.items[0].status.addresses[?(@.type=="InternalIP")].address}')
cat ~/.zsh_history | grep curl | grep $NODE_PORT | grep $NODE_IP
