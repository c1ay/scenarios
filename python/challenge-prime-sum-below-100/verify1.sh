#!/bin/zsh
python3 /home/labex/project/PrimeTotal.py | grep -vE '2|3|4|5|7|8|9' | grep 1060
