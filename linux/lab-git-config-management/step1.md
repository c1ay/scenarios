# Viewing Git Configuration

## Quick-start

All operations need to be done in the `myrepo` directory, so the first thing you should do is run the `cd ~/project/myrepo` command to get into the working directory.

```bash
cd ~/project/myrepo
```

To view your current Git configuration, you can use the `git config --list` command. This command will display all the configuration settings that are currently set in your Git environment. Git configuration is hierarchical, with settings in your user configuration file taking precedence over settings in your global configuration file, which in turn take precedence over system configuration files.

```bash
git config --list
```

This command will output something like this:

```bash
user.name=John Doe
user.email=johndoe@example.com
color.ui=auto
```

You can also view specific configuration values by specifying the key, like this:

```bash
git config user.name
```

This command will output the value of the `user.name` configuration variable.
