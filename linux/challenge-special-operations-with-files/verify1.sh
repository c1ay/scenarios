#!/bin/zsh

RS=`cat ~/project/result.txt`
if [ $RS -eq 3 ];then
	exit 0
else
	exit 1
fi