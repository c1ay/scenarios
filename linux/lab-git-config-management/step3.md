# Modifying Git Configuration

You can modify your Git configuration by using the `git config` command with the appropriate options. For example, to change the value of the `color.ui` setting to `true`, you can use the following command:

```bash
git config --global color.ui true
```

To remove a configuration setting, you can use the `--unset` option. For example, to remove the `color.ui` setting, you can use the following command:

```bash
git config --global --unset color.ui
```

You can also edit the configuration files directly by hand. The global configuration file is located at `~/.gitconfig` on Unix-like systems, and `C:\Users\YourUserName\.gitconfig` on Windows. The local repository configuration file is located at `.git/config` in the root of your repository.
