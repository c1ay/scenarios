### Adding triggers

We need to add the following code to the Pipeline:

```groovy
  triggers {
    GenericTrigger(
     genericVariables: [
      [key: 'ref', value: '$.ref']
     ].
     causeString: 'Triggered on $ref'.
     token: 'go-hello-world'.
     printContributedVariables: true.
     printPostContent: true.
     silentResponse: false.
     regexpFilterText: '$ref'.
     regexpFilterExpression: 'refs/heads/(dev|test|uat|pre|prod)'
    )
  }
```

This code does the following:

- Add a Webhook to the pipeline
- Get the branch that triggered the pipeline
- Match the filter branch
