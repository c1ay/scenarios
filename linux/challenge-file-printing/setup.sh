#!/bin/zsh

echo "1 2 3 4 5 6 7 8 9 10" > /tmp/verify.txt
mkdir ~/project/myrepo

touch ~/project/myrepo/file1.sh ~/project/myrepo/file2.bat ~/project/myrepo/file3.txt
mkdir ~/project/myrepo/dir1 ~/project/myrepo/dir2
touch ~/project/myrepo/dir1/file4.sh ~/project/myrepo/dir2/file5.exe

echo "This is the first line." >> ~/project/example.txt
echo "This is the second line." >> ~/project/example.txt
echo "This is the third line." >> ~/project/example.txt
echo "This is the fourth line." >> ~/project/example.txt
echo "This is the fifth line." >> ~/project/example.txt
echo "This is the sixth line." >> ~/project/example.txt
echo "This is the seventh line." >> ~/project/example.txt
echo "This is the eighth line." >> ~/project/example.txt
echo "This is the ninth line." >> ~/project/example.txt
echo "This is the tenth line." >> ~/project/example.txt
echo "This is the eleventh line." >> ~/project/example.txt
echo "This is the twelfth line." >> ~/project/example.txt
echo "This is the thirteenth line." >> ~/project/example.txt
echo "This is the fourteenth line." >> ~/project/example.txt
echo "This is the fifteenth line." >> ~/project/example.txt
echo "This is the sixteenth line." >> ~/project/example.txt

echo "This is the fifteenth line." >> /tmp/verify1.txt
