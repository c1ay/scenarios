### Node

A node is a machine, either a master or a slave node in Jenkins.

```groovy
pipeline {
    agent any
    stages{
    //
    }
}
```

This means that you can use any agent to run Pipeline.

In addition to any agent, there are none and label, where none means that no agent is specified and label means that the agent is selected using a label, as follows:

```groovy
pipeline {
    agent {
        label 'jenkins-jnlp'
    }
    stages {
    //
    }
}
```
