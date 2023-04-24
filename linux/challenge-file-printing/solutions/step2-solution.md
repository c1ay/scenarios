# Solution

- Input `cd ~/project/myrepo` to into the working directory.
- Input `find . ! -name "*.sh" ! -name "*.bat" -type f -delete` command or `find . -type f -not \( -name ‘*.bat’ -or -name ‘*.sh’ \) -delete` command to remove all files without the `.sh` and `.bat` extensions recursively in the current working directory.
