### Garbage cleanup

Mirror repositories often contain useless mirrors that take up disk space and cause a certain amount of wasted resources. Fortunately, Harbor provides a place for us to clean them up.

Click **Cleanup** to enter the cleanup interface, which is divided into **Manual Cleanup** and **Automatic Cleanup**.

#### Manual Cleanup

Click the **Clean Junk Now** button directly to complete the manual cleanup, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/2a9b1da0392f6d032a3275140877c3b4-0/wm)

#### Auto Cleanup

Automatic cleanup is polled by configuring timed tasks and clicking the **Edit** button:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/6092a00468464181ccdb3dcfe98a948f-0/wm)

You can directly choose to clean up by trivia, day, or week, or you can customize the time as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/ece5c0d8ac9680f6f419f3aee88ef993-0/wm)

The custom configuration is to configure `cron`, whose configuration rule is **seconds minutes hours days months weeks**, which has more **seconds** parameters than Cron on Linux, as follows

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/c7802cf0fdcea1dd5d16eba4fe10ea78-0/wm)
