### Project management

When we deploy Harbor, there will be a `library` project by default, which is public, meaning that all images under this project can be uploaded and downloaded.

But in production, for security, we will create some private projects that need to be authenticated to access, which can be divided by project group, by application, or by environment, depending on your needs.

Click **Project** -> **New Target**, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/0480b8ab5f84a4b701c497ccd34ba45b-0/wm)

Enter the necessary information as required, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/fc14742055b768b48b2b713f02d6f6ae-0/wm)

After clicking OK, the private project is created.
