#!/bin/zsh

mkdir ~/project/myrepo
cd ~/project/myrepo
git init
git config --global user.email "labex@example.com"
git config --global user.name "lab"
touch a.txt
git add a.txt
git commit -m 'add a.txt'
git branch old-name
git branch branch-to-delete
git checkout old-name
touch b.txt
git add b.txt
git commit -m 'add b.txt'
git checkout master
