## Introduction to Grayscale Releases

Grayscale publishing is also called canary publishing. It refers to a way to smooth the transition between black and white.

In the enterprise, many companies use grayscale release for version update. The principle is to have both A and B versions in the production environment, where A is the old version and B is the new version, and let some users continue to use A and let a small number of users to use B. If this small number of users do not give any feedback about the problem, the number of accesses to B will be slowly increased until all users use B.

![图片描述](assets/lab-example-of-a-grayscale-release-using-argo-rollouts-0-0.png)

The main effect of using grayscale releases is as follows:

- Reduce the impact of the release, although the features are tested in the test environment, but after all, not released to the production environment, if first let a small number of users first use the new version, in advance to find bugs, or performance problems, in advance to do a good job of repair, you can reduce the impact of the new version;
- By comparing the old and new versions, we can observe the effect brought by the new version.