## Grey release test

In Argo rollouts, the grayscale release is divided into two processes, Replica Shifting and Traffic Shifting:

- Replica Shifting: version replacement
- Traffic Shifting: traffic access

We experiment with these two processes separately.

First, create a `sy-03-2` directory under `/home/shiyanlou/Code/devops` with the following command:

```bash
mkdir /home/shiyanlou/Code/devops/sy-03-2
```

The experimental code for this lesson will be placed in the change directory.
