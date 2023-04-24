# Creating Branches

In Git, a branch is a separate line of development that allows you to work on a feature or bug fix without affecting the main codebase. To create a new branch, use the `branch` command followed by the name of the new branch:

```bash
cd ~/project/myrepo
git branch new-feature
```

This command creates a new branch named `new-feature` that is identical to the current branch. You can now switch to this new branch using the `checkout` command:

```bash
git checkout new-feature
```
