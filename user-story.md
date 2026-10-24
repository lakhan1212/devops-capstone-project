# User Stories for Customer Accounts Microservice

## Sprint 1 User Stories
- **Title:** As a User, I want to create a new account
  - **Description:** As a user, I need to be able to create a new customer account by providing account details so that my information is stored in the system.
  - **Priority:** High
  - **Estimate:** 5 pts

- **Title:** As an Admin, I want to delete an account
  - **Description:** As an administrator, I need the ability to delete an existing customer account so that obsolete or requested account records are removed.
  - **Priority:** High
  - **Estimate:** 5 pts

- **Title:** As a User, I want to read an account's details
  - **Description:** As a user, I need to view the details of a specific account using its account ID so that I can verify account information.
  - **Priority:** Medium
  - **Estimate:** 2 pts

- **Title:** As a User, I want to update my account
  - **Description:** As a user, I need to update my existing account information so that my profile reflects current data.
  - **Priority:** Medium
  - **Estimate:** 3 pts

- **Title:** As a User, I want to list all accounts
  - **Description:** As a user, I need to view a list of all customer accounts stored in the system.
  - **Priority:** Medium
  - **Estimate:** 3 pts

- **Title:** As a Developer, I want to set up the development environment
  - **Description:** As a developer, I need to configure the local environment, dependencies, and database connection to build the microservice.
  - **Priority:** High
  - **Estimate:** 3 pts

## Sprint 2 User Stories
- **Title:** Need the ability to automate continuous integration checks
  - **Description:** As a developer, I need to configure GitHub Actions workflows to automatically run linting and unit tests on pull requests.
  - **Priority:** High
  - **Estimate:** 5 pts

- **Title:** Need to add security headers and CORS policies
  - **Description:** As a security administrator, I need Talisman and CORS header policies integrated into the Flask API routes to secure the microservice against web vulnerabilities.
  - **Priority:** Medium
  - **Estimate:** 3 pts

## Sprint 3 User Stories
- **Title:** Need the ability to build microservice images and push them to a registry
  - **Description:** As a DevOps engineer, I need a Dockerfile configured to containerize the accounts microservice and push the image to Docker Hub / OpenShift Registry.
  - **Priority:** High
  - **Estimate:** 5 pts

- **Title:** Need the ability to deploy microservices to Kubernetes
  - **Description:** As a DevOps engineer, I need Kubernetes deployment and service manifests configured to deploy the microservice to a cluster.
  - **Priority:** High
  - **Estimate:** 5 pts

- **Title:** Need the ability to automate continuous delivery with Tekton
  - **Description:** As a DevOps engineer, I need Tekton pipelines and tasks to automate building, testing, and deploying the container image to Kubernetes.
  - **Priority:** High
  - **Estimate:** 5 pts
