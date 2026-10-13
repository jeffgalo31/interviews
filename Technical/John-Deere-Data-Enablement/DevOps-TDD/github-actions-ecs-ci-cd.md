# GitHub Actions: Java API to Amazon ECS

**Type:** Supplemental original CI/CD exercise
**Sources:** [GitHub Actions workflows](https://docs.github.com/en/actions/writing-workflows/about-workflows) · [GitHub Actions security hardening](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions) · [Amazon ECS rolling deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html)
**Focus:** Git, GitHub Actions, Java tests, container publishing, AWS OIDC, ECS deployment and rollback

## Exercise

For a Java 21 Spring Boot API, define a GitHub Actions workflow that:

1. Runs on pull requests to `main` and pushes to `main`.
2. Builds the application and runs automated tests before any deployment.
3. On a successful push to `main`, builds a container tagged with the commit SHA and publishes it to Amazon ECR.
4. Authenticates to AWS without storing long-lived AWS access keys in GitHub secrets.
5. Updates an ECS service to the exact image built by the workflow, waits for service stability, and supports a protected production environment.

If the repository also owns Lambda code, explain how you would add a separate SAM/CDK deployment job that uses the same test gate and AWS identity boundary.

Example event outcomes:

| Trigger/result | Expected workflow behavior |
|---|---|
| Pull request to `main`, tests pass | Report checks and test artifact; do not assume AWS deployment credentials or deploy. |
| Push to `main`, tests fail | Mark the workflow failed; skip the ECS deploy job. |
| Push to `main`, tests pass | Build and push an image tagged with that commit SHA, deploy its task definition, and wait for ECS stability. |
| ECS deployment fails health checks | Fail the deployment and rely on the configured ECS circuit breaker/rollback; do not report a successful release. |

## Solution

Save as `.github/workflows/api-ci-cd.yml`. The workflow assumes the repository already has an ECR repository, ECS task definition, cluster, service, and an AWS IAM role configured for GitHub's OIDC provider. The task-definition file must contain a container named `api`.

```yaml
name: Java API CI/CD

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Check out source
        uses: actions/checkout@v4

      - name: Set up Java
        uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: '21'
          cache: gradle

      - name: Build and test
        run: ./gradlew clean test bootJar

      - name: Publish test reports
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: junit-reports
          path: build/test-results/test/*.xml
          if-no-files-found: ignore

  deploy-ecs:
    needs: test
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment: production
    permissions:
      contents: read
      id-token: write
    env:
      AWS_REGION: us-east-1
      ECR_REPOSITORY: data-enablement-api
      ECS_CLUSTER: data-enablement
      ECS_SERVICE: data-enablement-api
      TASK_DEFINITION: .aws/task-definition.json
      CONTAINER_NAME: api

    steps:
      - name: Check out source
        uses: actions/checkout@v4

      - name: Assume AWS role with OIDC
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{ vars.AWS_DEPLOY_ROLE_ARN }}
          aws-region: ${{ env.AWS_REGION }}

      - name: Sign in to Amazon ECR
        id: ecr
        uses: aws-actions/amazon-ecr-login@v2

      - name: Build and push immutable image
        id: image
        env:
          REGISTRY: ${{ steps.ecr.outputs.registry }}
        run: |
          image_uri="${REGISTRY}/${ECR_REPOSITORY}:${GITHUB_SHA}"
          docker build --tag "$image_uri" .
          docker push "$image_uri"
          echo "uri=$image_uri" >> "$GITHUB_OUTPUT"

      - name: Render task definition with new image
        id: task-definition
        uses: aws-actions/amazon-ecs-render-task-definition@v1
        with:
          task-definition: ${{ env.TASK_DEFINITION }}
          container-name: ${{ env.CONTAINER_NAME }}
          image: ${{ steps.image.outputs.uri }}

      - name: Deploy and wait for ECS stability
        uses: aws-actions/amazon-ecs-deploy-task-definition@v2
        with:
          task-definition: ${{ steps.task-definition.outputs.task-definition }}
          service: ${{ env.ECS_SERVICE }}
          cluster: ${{ env.ECS_CLUSTER }}
          wait-for-service-stability: true
```

### Why this design

- `needs: test` prevents deployment when the build or tests fail. Pull requests run checks but do not receive AWS deployment permissions.
- `id-token: write` is scoped to the deploy job; AWS trusts the repository/environment OIDC claims and issues short-lived credentials. The IAM role should be limited to the required ECR and ECS resources. Store `AWS_DEPLOY_ROLE_ARN` as a GitHub Actions variable: it identifies the role and is not a long-lived access key.
- The commit SHA tags the image so the task definition deploys exactly the artifact produced for that commit. Protect ECR tags from overwrite where possible.
- The `production` GitHub environment can require reviewers and restrict allowed branches. ECS health checks and the deployment circuit breaker/rollback protect service availability.
- Pin third-party actions to reviewed full commit SHAs in a production workflow; version tags are shown above for readability. Keep `GITHUB_TOKEN` permissions minimal and do not expose deployment secrets to untrusted pull-request code.
- For Lambda, use a separate deploy job for the SAM/CDK stack, gated on the same successful tests and protected environment. Scope its OIDC role to the Lambda/CloudFormation resources it needs rather than reusing broad ECS permissions.
