# Merging Branches

Once you have made changes to a branch, you can merge it back into the master codebase using the `merge` command. First, switch back to the master branch:

```bash
git checkout master
```

Then, use the `merge` command followed by the name of the branch you want to merge:

```bash
git merge new-name
```

This command will merge the changes from `new-name` into the `master` branch.
