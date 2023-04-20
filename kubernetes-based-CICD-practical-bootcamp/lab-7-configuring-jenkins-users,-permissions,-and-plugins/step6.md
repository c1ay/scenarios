### Create role

`Manage And Assign Roles` provides three kinds of roles, which are:

- Global roles: Global roles, advanced users such as administrators can create global based roles
- Item roles: Project roles, roles for a particular item or items
- Node roles: Node roles, node-related permissions

We need to add a global role and give it read-only permissions, mainly to bind Jenkins users to the most basic access rights, otherwise it will report an error.

Click **System Configuration** -> **Manage And Assign Roles** and select `Manage Roles`, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/715fa9f0d6db7f8b5100175365288714-0/wm)

Add the `View` role at `Global roles` and grant `Read` permissions as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/c1e21c74d12c514672f532666ae436ba-0/wm)

Add an `ops` role and grant global `Read` and `Create` permissions to it, as follows

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/65b6b4ec34c3d5313efe65099e409900-0/wm)

Then create `dev` and `test` roles in `Item roles`, with `dev` matching items starting with `dev-.*` and `test` matches the item starting with `test-.*` for items starting with `test-:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/db6df9b2d67c9354391c475799b57df9-0/wm)

Then click Save to complete the role configuration.
