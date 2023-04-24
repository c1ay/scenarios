# Setting the Username and Email Address

It's important to set your username and email address in Git because it is used for authorship when you make commits. To set your username and email address, you can use the `git config` command with the `--global` option.

```bash
git config --global user.name "labex"
git config --global user.email labex@example.com
```

You can also set these values on a per-repository basis by omitting the `--global` option and running the command within a specific repository. This will override the global values for that repository.

```bash
git config user.name "Jane Smith"
git config user.email janesmith@example.com
```
