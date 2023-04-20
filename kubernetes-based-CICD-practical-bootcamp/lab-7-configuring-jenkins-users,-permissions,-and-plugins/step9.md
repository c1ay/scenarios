## Create a view

Now whether you log in as the `admin` or `joker` user, all the items you see are under the **all** view, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/9aec0d17f61aa21400ecf287683d5e74-0/wm)

This default view is fine when there are very few projects, but when there are a lot of projects, it can be very confusing and hard to distinguish them if they are not managed differently. You can distinguish by project group, you can distinguish by environment, etc. I use the environment distinction here, mainly to demonstrate this effect.

We define the view rules as follows:

- Dev view manages development environment projects, which all start with `dev-`.
- Test view manages the test environment items, which all start with `test-`.

Click on **My Views** -> **New View**, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/b93bb2df4a3259c7147d5bd6407afd01-0/wm)

Fill in **View Name** and select **List View**, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/e02d3a8368db3693508eb5971aef4e77-0/wm)

Select **Display tasks in view using regular expressions**, enter `dev-.*` expression, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/f0b59305370ba8b971d0b24ddaf82281-0/wm)

and click Save.

Test The `Test` view is created in the same way as above, except that the regular expression is `test-.*`, which is not described here.

After it has been created, it looks like this:

- Click on the `Dev` view to display only the items starting with `dev-`, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/3c99b8265c3ac4964f25e348ba6ebf89-0/wm)

- Click on the `Test` view to display only items starting with `test-`, as follows

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/de672ed6978956a3bd5ca2dfce47b715-0/wm)
