# DevOps Interview Cheat Sheet

Git · Jenkins · CI/CD · Lean Principles

---

## Quick Overview

| Tech | What it is | Type | Use it for |
|---|---|---|---|
| **Git** | Distributed version control | Source control | Branching, collaboration, history |
| **Jenkins** | Open-source automation server (pipelines as code) | CI/CD tool | Build, test, deploy automation |
| **CI** | Continuous Integration: merge often, auto build + test | Practice | Catch integration bugs early |
| **CD** | Continuous Delivery/Deployment: automated release | Practice | Fast, safe, repeatable releases |

**Typical flow:** Developer push/PR → webhook triggers Jenkins → build → unit tests → static analysis/security scan → package (JAR/Docker image) → push to registry → deploy to dev/staging → integration tests → approval → production → monitor.

---

## 1. Git

**Key points**
- Distributed: every clone has the full history. Three areas: **working tree → staging (index) → repository**.
- Commits are snapshots identified by SHA; branches are lightweight pointers.
- Remote workflow: `fetch`, `pull` (= fetch + merge/rebase), `push`.
- Branching strategies: **GitFlow**, **GitHub Flow**, **trunk-based development** (best fit for CI/CD).

**Questions**
1. **`merge` vs `rebase`?** Merge preserves history with a merge commit. Rebase replays commits on a new base for linear history. Never rebase shared/public branches.
2. **`fetch` vs `pull`?** Fetch downloads changes without applying; pull = fetch + merge (or rebase).
3. **`reset` vs `revert`?** Reset moves the branch pointer (rewrites history; `--soft/--mixed/--hard`). Revert creates a new commit undoing a change (safe for shared branches).
4. **How do you undo the last commit?** Local: `git reset --soft HEAD~1`. Pushed: `git revert <sha>`.
5. **What is `cherry-pick`?** Apply a specific commit onto the current branch (hotfix backports).
6. **`git stash`?** Temporarily shelve uncommitted changes.
7. **How do you resolve merge conflicts?** Open conflicted files, choose/merge changes, `git add`, then continue the merge/rebase.
8. **Squash commits?** `git rebase -i` or squash-merge to keep history clean.
9. **GitFlow vs trunk-based?** GitFlow: long-lived develop/release branches, heavier. Trunk-based: short-lived branches, feature flags, supports frequent releases.
10. **What is `git bisect`?** Binary search through history to find the commit that introduced a bug.
11. **What is a detached HEAD?** HEAD points to a commit, not a branch; create a branch to keep new commits.
12. **How do you remove a leaked secret?** Rotate it immediately; then clean history (`git filter-repo`/BFG). Rewriting history alone isn't enough.
13. **Good PR/commit practices?** Small focused PRs, clear messages (Conventional Commits), required reviews, protected branches, status checks.

---

## 2. Jenkins

**Key points**
- Controller (scheduling, UI) + **agents/nodes** (execute builds); scale with dynamic agents (Docker/Kubernetes).
- **Pipeline as Code** via `Jenkinsfile` in the repo. Two syntaxes: **Declarative** (structured, recommended) and **Scripted** (Groovy, flexible).
- Structure: `pipeline { agent, stages { stage { steps } }, post { } }`.
- Triggers: webhook, SCM polling, cron, upstream job. **Multibranch pipelines** auto-create jobs per branch/PR.
- Plugins: Git, Pipeline, Docker, Credentials, Blue Ocean, SonarQube, JUnit.
- **Credentials store** keeps secrets out of code; **shared libraries** reuse pipeline logic.

**Sample Jenkinsfile**
```groovy
pipeline {
  agent any
  stages {
    stage('Build')  { steps { sh './mvnw -B clean package -DskipTests' } }
    stage('Test')   { steps { sh './mvnw -B test' } post { always { junit '**/target/surefire-reports/*.xml' } } }
    stage('Scan')   { steps { sh './mvnw sonar:sonar' } }
    stage('Docker') { steps { sh 'docker build -t app:${GIT_COMMIT} .' } }
    stage('Deploy') { when { branch 'main' } steps { sh './deploy.sh' } }
  }
  post { failure { echo 'Build failed' } }
}
```

**Questions**
1. **Declarative vs scripted pipeline?** Declarative: opinionated, easier, validated. Scripted: full Groovy, more flexible but complex.
2. **What is a Jenkinsfile?** Pipeline definition stored in source control, versioned with the code.
3. **How do you manage secrets?** Jenkins Credentials (`withCredentials`), Vault/Secrets Manager; never hard-code, mask in logs.
4. **How do you scale Jenkins?** Controller + many agents; ephemeral Docker/K8s agents; keep builds off the controller.
5. **How do you run stages in parallel?** `parallel { stage(...) {...} }` for tests/lint/scans.
6. **How do you trigger builds on commit?** Webhook from GitHub/GitLab (preferred) over polling.
7. **How do you handle failures?** `post { failure/always }`, notifications (Slack/email), retries (`retry`), `timeout`.
8. **Multibranch pipeline?** Auto-discovers branches/PRs containing a Jenkinsfile and builds each.
9. **How do you secure Jenkins?** RBAC, SSO, patched plugins, no builds on controller, credentials scoping, audit logs.
10. **Jenkins vs GitHub Actions/GitLab CI?** Jenkins: self-hosted, extremely flexible, more maintenance. Actions/GitLab CI: integrated, managed, less ops overhead.
11. **How to share logic across pipelines?** Shared libraries.

---

## 3. CI/CD

**Key points**
- **Continuous Integration:** frequent merges to main, automated build + tests on every change.
- **Continuous Delivery:** every change is releasable; deploy to prod is a manual approval.
- **Continuous Deployment:** every passing change deploys to prod automatically.
- Pipeline stages: build → unit test → static analysis (SonarQube) → security scan (SAST/SCA/secrets, container scan) → artifact → deploy → integration/smoke tests → promote.
- **Build once, deploy the same artifact** to every environment; config injected per environment.
- **Deployment strategies:** rolling, blue/green, canary, feature flags.
- **IaC:** Terraform, CloudFormation/CDK; **GitOps** (ArgoCD/Flux) with Git as source of truth.
- **DORA metrics:** deployment frequency, lead time, change failure rate, MTTR.

**Questions**
1. **CI vs Continuous Delivery vs Continuous Deployment?** CI: integrate and test. Delivery: always releasable with manual gate. Deployment: fully automated to prod.
2. **Blue/green vs canary vs rolling?** Blue/green: two environments, instant switch and rollback. Canary: small traffic % first. Rolling: replace instances gradually.
3. **How do you roll back?** Redeploy previous artifact version, switch blue/green back, disable feature flag, `git revert` + pipeline.
4. **What makes a good pipeline?** Fast, reliable, automated, tests at the right level, reproducible, immutable artifacts, observable.
5. **Where does security fit (shift-left)?** SAST, dependency scanning (SCA), secret scanning, container scanning, IaC scanning in the pipeline; DAST in staging.
6. **How do you handle DB changes in CD?** Versioned migrations (Flyway/Liquibase), backward-compatible (expand/contract) changes.
7. **How do you handle flaky tests?** Quarantine, fix root cause, retries only as a stopgap, track flakiness.
8. **How do you manage environments and config?** Same artifact, per-env config via env vars/Parameter Store/Secrets Manager; IaC for parity.
9. **What are feature flags for?** Decouple deploy from release; enable gradual rollouts and quick kill switches.
10. **How do you deploy to AWS?** Build image → ECR → ECS/Fargate (CodeDeploy blue/green), or Lambda via SAM/CDK; or CodePipeline/CodeBuild.
11. **How do you measure pipeline health?** DORA metrics, build duration, failure rate, mean time to recovery.
12. **Docker's role?** Packages app + dependencies into an immutable image; consistent across environments.

---

## 4. Lean Development Principles

**Key points**
- Adapted from Toyota's lean manufacturing; goal is to **maximize customer value while minimizing waste**.
- **7 lean software principles (Poppendieck):** eliminate waste, build quality in, create knowledge, defer commitment, deliver fast, respect people, optimize the whole.
- **Waste in software:** partially done work, extra features, relearning, handoffs, task switching, delays, defects.
- Core practices: small batch sizes, limited **WIP**, continuous flow (Kanban), fast feedback loops, automation, **value stream mapping**, continuous improvement (kaizen), MVP and build-measure-learn.
- Lean and DevOps align: CI/CD shortens lead time, automation removes manual waste, monitoring feeds learning.

**Questions**
1. **What is lean software development?** Delivering value fast by removing waste, building quality in, and learning continuously.
2. **Examples of waste in software?** Unused features, long-lived branches and big batches, manual deploys, waiting for approvals, rework from late bugs, context switching.
3. **How does CI/CD support lean?** Small frequent changes, automated checks, and fast feedback reduce batch size, lead time, and defects.
4. **Why limit work in progress?** Less context switching, faster completion, bottlenecks become visible (Kanban).
5. **What is value stream mapping?** Mapping each step from idea to production to find delays and waste (wait vs. touch time).
6. **Lean vs Agile?** Agile: iterative team delivery practices. Lean: flow and waste-removal philosophy. They complement each other (Scrum + Kanban "Scrumban").
7. **What is "build quality in"?** Prevent defects with TDD, automated tests, code review, and CI instead of inspecting at the end.
8. **How do you apply lean to a delivery pipeline?** Measure lead time and deploy frequency (DORA), remove manual gates, shrink PRs, automate tests, fix the biggest bottleneck first.
9. **What is MVP / build-measure-learn?** Ship the smallest valuable version, measure real usage, and decide what to build next.

---

## Cross-Topic / Scenario Questions

1. **Design a CI/CD pipeline for a Spring Boot service.** PR → build + unit tests + Sonar + dependency scan → Docker image to ECR → deploy to staging (ECS) → integration/smoke tests → approval → blue/green to prod → monitor and auto-rollback on alarms.
2. **A deployment broke production. What next?** Roll back first (restore service), then investigate via logs/metrics, write a postmortem, add tests/guards.
3. **Two developers changed the same file. How do you resolve it?** Rebase/merge, resolve conflicts, rerun tests, review.
4. **Builds take 40 minutes. How do you speed up?** Cache dependencies, parallelize stages, incremental builds, faster agents, split test suites, remove unnecessary steps.
5. **How do you enforce quality?** Branch protection, required reviews and status checks, quality gates (coverage, Sonar), linting.
6. **How do you keep secrets safe in CI/CD?** Credential store/Vault, short-lived OIDC credentials, secret scanning, masked logs.

---

## Core Concepts to Know Cold

- **Git:** rebase vs merge, reset vs revert, branching strategies, PR workflow.
- **Jenkins:** Jenkinsfile, declarative pipeline, agents, credentials, webhooks.
- **CI/CD:** build once deploy many, automated tests, deployment strategies, rollback.
- **Shift-left security** and quality gates.
- **IaC / GitOps / containers** as supporting practices.
- **DORA metrics.**
