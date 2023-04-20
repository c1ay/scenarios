## Credential Management

Credential management is not very relevant to this experiment because it is relatively simple, but will be used later in the experiment, so I will briefly introduce it here.

Click **System Configuration** -> **Manege Credentials** to enter the credential management interface as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/3b9d87fddb4ffee55421cc3f9b7066dd-0/wm)

Click **Global** above, then enter the global credentials configuration interface as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/cda4342632242b1148f4892488bfbb7c-0/wm)

Click **Add Credentials** to add different types of credentials, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/de34f1f7aaa7c0e9744b4e1b59678359-0/wm)

Among the commonly used types are:

- Secret text - A token such as an API token (e.g. GitHub personal access token).
- Username and password - either as separate fields or as a colon separated string: username:password.
- Secret file - The encrypted content stored in the file.
- Certificate - a PKCS#12 certificate file and an optional password

Let's take the example of adding credentials for Gitlab authentication by selecting `Username with password` and entering the username password and description as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/d87f78ae9e50db23b4110451b473b65b-0/wm)

Clicking OK completes the creation of the credentials, which can be referenced later when you create the pipeline, which will be covered later in the experiment.
