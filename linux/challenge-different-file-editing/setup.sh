#!/bin/zsh

mkdir ~/project/myrepo

touch ~/project/myrepo/file1.txt ~/project/myrepo/file2.txt ~/project/access.log
mkdir ~/project/myrepo/dir1 ~/project/myrepo/dir2

echo "line1" >> ~/project/access.log
echo "line2" >> ~/project/access.log

echo "1;2;3;4;5" >> ~/project/split-me.txt
echo "1" >> /tmp/verify.txt
echo "2" >> /tmp/verify.txt
echo "3" >> /tmp/verify.txt
echo "4" >> /tmp/verify.txt
echo "5" >> /tmp/verify.txt
