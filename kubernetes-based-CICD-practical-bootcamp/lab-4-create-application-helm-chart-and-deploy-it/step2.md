## Introduction to Helm

Helm has both Helm2 and Helm3, but Helm2 is now obsolete and we use Helm3.

The application objects on K8S are composed of specific resource descriptions, including deployment, service and so on. They are stored in their own files or written centrally to a configuration file. Then `kubectl apply -f` does the deployment, just like in the previous section, we created many Deployment, Service.

This is easy to manage when the project is relatively small, but if the project is large or some projects are complex, there will be many resource description files, such as microservice architecture applications, which may have as many as ten or dozens of services that make up the application. If there is a need to update or roll back the application, you may have to modify and maintain the large number of resource files involved, and this way of organizing and managing the application becomes overwhelming.

This is where we can use Helm for application package management.

Helm has several important concepts:

- helm: A command-line client tool that is primarily used for Kubernetes application chart creation, packaging, publishing, and management.
- Chart: An application description, a collection of files used to describe k8s resources.
- Release: A Chart-based deployment entity, a chart run by Helm will generate a corresponding release; a real running resource object will be created in k8s.
