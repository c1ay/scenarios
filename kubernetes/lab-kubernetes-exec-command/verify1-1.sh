#!/bin/bash

minikube kubectl -- get pod | grep "nginx"
