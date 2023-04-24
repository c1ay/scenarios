## Create a view

Now whether you log in as the `admin` or `joker` user, all the items you see are under the **all** view, as follows

![图片描述](assets/lab-configuring-jenkins-users,-permissions,-and-plugins-8-0.png)

This default view is fine when there are very few projects, but when there are a lot of projects, it can be very confusing and hard to distinguish them if they are not managed differently. You can distinguish by project group, you can distinguish by environment, etc. I use the environment distinction here, mainly to demonstrate this effect.

We define the view rules as follows:

- Dev view manages development environment projects, which all start with `dev-`.
- Test view manages the test environment items, which all start with `test-`.

Click on **My Views** -> **New View**, as follows:

![图片描述](assets/lab-configuring-jenkins-users,-permissions,-and-plugins-8-1.png)

Fill in **View Name** and select **List View**, as follows:

![图片描述](assets/lab-configuring-jenkins-users,-permissions,-and-plugins-8-2.png)

Select **Display tasks in view using regular expressions**, enter `dev-.*` expression, as follows:

![图片描述](assets/lab-configuring-jenkins-users,-permissions,-and-plugins-8-3.png)

and click Save.

Test The `Test` view is created in the same way as above, except that the regular expression is `test-.*`, which is not described here.

After it has been created, it looks like this:

- Click on the `Dev` view to display only the items starting with `dev-`, as follows:

![图片描述](assets/lab-configuring-jenkins-users,-permissions,-and-plugins-8-4.png)

- Click on the `Test` view to display only items starting with `test-`, as follows

![图片描述](assets/lab-configuring-jenkins-users,-permissions,-and-plugins-8-5.png)
