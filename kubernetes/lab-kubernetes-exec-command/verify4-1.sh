#!/bin/bash

minikube kubectl -- describe pod nginx-env | grep MY_VAR | grep my-value
