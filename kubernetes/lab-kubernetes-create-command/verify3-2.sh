#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep get | grep mynamespace | grep -Eq services
