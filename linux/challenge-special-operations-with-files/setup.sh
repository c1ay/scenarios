#!/bin/zsh

mkdir ~/project/myrepo
mkdir ~/project/myrepo/dir1 ~/project/myrepo/dir2
touch ~/project/myrepo/file1.txt ~/project/myrepo/file2.txt
echo "this is line 1..." > ~/project/myrepo/a\\.\ a.txt
echo "this is line 1..." > /tmp/verify.txt
