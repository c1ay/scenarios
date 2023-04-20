### Application rollback

The rollback is also based on Git, and we can look at the Git History as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/f3cb5df22e007eae5d19276136f365c2-0/wm)

Then you can find the last commit we committed and click on it:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/db2ad2d01b20b3ec9458036e66486797-0/wm)

Find `options` and select `revert`, which will create a new Merage Request, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/e7e9831f094eedc7a072e525d3e41f21-0/wm)

Clicking submit will take you to the `merge` page, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/7601fc45d6603834cc74428aedd1c3a4-0/wm)

Then click `merge` to roll back the image, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/8d9c50a7a4f2b33d45246515f6e844f5-0/wm)

Finally, just go to Argocd and click sync.
