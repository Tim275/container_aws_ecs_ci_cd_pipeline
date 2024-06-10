## Overview

This project, named "nodejs-ssl-server," It utilizes a CI/CD pipeline to automate the deployment process to Amazon ECS using AWS CodePipeline, ensuring seamless integration and delivery.

### Pipeline Workflow

1. **Source Stage**: CodePipeline monitors the GitHub repository ([`package.json`]" specifies the repository  for changes. Upon detecting changes, it triggers the pipeline execution.
2. **Build Stage**: Utilizes the [`buildspec.yml`] to run build commands, including logging into Amazon ECR, building the Docker image, and pushing it to an ECR repository.
3. **Deploy Stage**: The Docker image is then deployed to an Amazon ECS service, where the application becomes accessible.

## outcome


![alt text](images/image.png)
![alt text](images/image.png)
![alt text](images/image-2.png)
![alt text](images/image-3.png)