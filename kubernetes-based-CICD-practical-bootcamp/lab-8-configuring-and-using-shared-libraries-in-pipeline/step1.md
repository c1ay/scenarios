## Pipeline Introduction

Pipeline is a workflow framework that runs on Jenkins and connects tasks that were running independently on a single or multiple nodes, enabling complex process orchestration and visualization that would be difficult to accomplish with a single task.
Jenkins Pipeline has several core concepts:

- Node: Node, a Node is a Jenkins node, Master or Agent, which is the specific runtime environment for executing Step, for example, the Jenkins Slave we dynamically ran before is a Node node
- Stage: Stage, a Pipeline can be divided into several Stages, each Stage represents a set of operations, for example: Build, Test, Deploy, Stage is a logical grouping concept, can be across multiple Node
- Step: Step is the most basic unit of operation, either printing a sentence or building a Docker image, provided by various Jenkins plugins, such as the command: `sh 'make'`, which is equivalent to executing the make command in our usual shell terminal.

Use of Pipeline:

- Pipeline scripts are implemented in the Groovy language
- Pipeline supports two syntaxes: Declarative and Scripted Pipeline.
- Pipelines can also be created in two ways: you can enter the script directly into the Jenkins web UI interface, or you can create a Jenkinsfile script file and put it in the project source code repository.
- We generally recommend loading a Jenkinsfile Pipeline directly from the source code control (SCMD) in Jenkins
