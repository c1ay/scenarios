#!/bin/zsh

cat ~/.zsh_history | grep "rm.*my-network2"

test -z "$(docker network ls | grep my-network2)"
