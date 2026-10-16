# Engineering Practices Interview Cheat Sheet

TDD · Agile/Scrum · Pair Programming · Code Reviews · Security by Design

---

## Quick Overview

| Practice | What it is | Why it matters |
|---|---|---|
| **TDD** | Write a failing test first, then code, then refactor | Better design, fast feedback, safe refactoring |
| **Agile/Scrum** | Iterative delivery in sprints with defined roles/events | Adaptability, frequent delivery, transparency |
| **Pair programming** | Two developers on one task (driver/navigator) | Knowledge sharing, fewer defects |
| **Code reviews** | Peers inspect changes before merge | Quality, consistency, shared ownership |
| **Security by Design** | Build security in from the start, not bolted on | Fewer vulnerabilities, cheaper fixes |

**How they fit together:** Scrum planning defines stories → developers pair and use TDD to build → PR with automated checks and code review → security checks in CI → release and retrospective.

---

## 1. TDD (Test-Driven Development)

**Key points**
- **Red → Green → Refactor:** write a failing test, make it pass with the simplest code, then clean up.
- Test pyramid: many **unit** tests, fewer **integration**, few **end-to-end**.
- Tools (Java): JUnit 5, Mockito, AssertJ, Testcontainers; Python: pytest.
- Test doubles: dummy, stub, fake, mock, spy.
- Good tests are **FIRST:** Fast, Independent, Repeatable, Self-validating, Timely.
- Structure: Arrange-Act-Assert (Given-When-Then for BDD).

**Questions**
1. **What is TDD and its benefits?** Tests drive design; yields high coverage, simpler modular code, fast feedback, confidence to refactor.
2. **Walk me through Red-Green-Refactor.** Write a failing test (red), minimal code to pass (green), then refactor while tests stay green.
3. **TDD vs BDD?** TDD focuses on developer-level unit behavior; BDD uses business-readable scenarios (Given/When/Then, Cucumber) to align with stakeholders.
4. **Mock vs stub vs fake?** Stub returns canned data; mock verifies interactions; fake is a working lightweight implementation (in-memory DB).
5. **What makes a good unit test?** Tests one behavior, isolated, deterministic, readable name, no logic, fails for one reason.
6. **How do you test code that hits a DB or external API?** Mock the boundary in unit tests; use Testcontainers/WireMock for integration; contract tests between services.
7. **Is 100% coverage the goal?** No. Coverage shows what's untested, not test quality; focus on meaningful behavior and critical paths (mutation testing helps).
8. **How do you handle legacy code without tests?** Add characterization tests around behavior, refactor safely (seams), then TDD new changes.
9. **Drawbacks of TDD?** Learning curve, slower start, brittle tests if over-mocked or coupled to implementation.
10. **Where do tests run?** Locally and in CI on every commit; gate merges on passing tests.

---

## 2. Agile / Scrum

**Key points**
- **Agile values:** individuals and interactions, working software, customer collaboration, responding to change.
- **Scrum roles:** Product Owner (what/priority), Scrum Master (process facilitator), Developers (build).
- **Events:** Sprint (1-4 weeks), Sprint Planning, Daily Scrum (15 min), Sprint Review, Sprint Retrospective.
- **Artifacts:** Product Backlog, Sprint Backlog, Increment; **Definition of Done** and **Definition of Ready**.
- Estimation: story points, planning poker; track **velocity**; burndown charts.
- Kanban: continuous flow, WIP limits. Other: XP, SAFe at scale.

**Questions**
1. **Agile vs Waterfall?** Agile: iterative, adaptive, continuous feedback. Waterfall: sequential phases, late feedback, rigid scope.
2. **Describe a Scrum sprint.** Planning → daily scrums → development → review (demo) → retrospective → next sprint.
3. **Roles of PO, SM, and team?** PO owns backlog/value, SM removes impediments and coaches, team is self-organizing and delivers the increment.
4. **What is the Definition of Done?** Shared checklist (code reviewed, tested, deployed to staging, documented) for a story to count as complete.
5. **Scrum vs Kanban?** Scrum: timeboxed sprints, roles, commitments. Kanban: continuous flow, WIP limits, no fixed iterations.
6. **How do you estimate?** Relative sizing with story points and planning poker; based on complexity, effort, risk.
7. **What is velocity, and how is it misused?** Average points per sprint, used for forecasting, not for comparing teams or pressuring people.
8. **What happens in a retrospective?** Team reflects on what went well/poorly and picks actionable improvements.
9. **How do you handle changing requirements mid-sprint?** Protect the sprint goal; new items go to the backlog unless the PO and team renegotiate scope.
10. **What is a good user story?** "As a [user], I want [goal], so that [value]" with acceptance criteria; INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable).
11. **How do you handle a blocker or a missed sprint goal?** Raise early in the daily scrum, escalate through the SM, inspect root cause in the retro.
12. **Technical debt in Scrum?** Make it visible in the backlog and allocate capacity each sprint.

---

## 3. Pair Programming

**Key points**
- **Driver** writes code; **navigator** reviews, thinks ahead, and spots issues; swap roles often.
- Styles: ping-pong (with TDD: one writes the test, the other makes it pass), strong-style, remote pairing (VS Code Live Share, screen share), mob programming.
- Best for complex problems, onboarding, critical code, and knowledge transfer.

**Questions**
1. **What is pair programming and its benefits?** Real-time collaboration giving higher quality, fewer bugs, shared knowledge, faster onboarding.
2. **Driver vs navigator?** Driver types and handles tactics; navigator handles strategy, edge cases, and reviews as it happens.
3. **Drawbacks?** Can feel slower, tiring, personality friction; not needed for trivial tasks.
4. **Ping-pong pairing?** One writes a failing test, the other writes code to pass it, then swap.
5. **How do you pair remotely?** Shared IDE (Live Share), video call, clear communication, regular role switching and breaks.
6. **How do you handle a big skill gap?** Junior drives while the senior navigates; explain reasoning, not just solutions.
7. **Pairing vs code review?** Pairing is real-time feedback during writing; review is asynchronous after. They complement each other.
8. **When not to pair?** Routine/boilerplate work, deep solo research or spikes.

---

## 4. Code Reviews

**Key points**
- Peer review via pull/merge requests before merge to main.
- Check: **correctness, readability, design, tests, security, performance, error handling, consistency with standards**.
- Automate the trivial: linters, formatters, static analysis, and CI checks so humans focus on logic/design.
- Keep PRs small (~200-400 lines), with a clear description and linked ticket.
- Culture: review the code, not the person; be specific, kind, and constructive.

**Questions**
1. **What do you look for in a code review?** Correctness and edge cases, tests, readability/naming, design and duplication, security issues, performance, error handling, backward compatibility.
2. **How do you give feedback?** Specific, actionable, respectful; ask questions, explain why, separate blocking issues from nits; praise good work.
3. **How do you receive feedback?** Stay open, assume good intent, ask for clarification, don't take it personally, follow up on changes.
4. **What makes a good PR?** Small, single purpose, clear description (what/why), tests included, passing CI, screenshots if UI.
5. **A reviewer and you disagree. What now?** Discuss with data/examples, refer to team standards, involve a third person or tech lead if needed; decide and move on.
6. **How do you review a very large PR?** Ask to split it, review by commit/module, or walk through it together.
7. **Which checks should be automated?** Formatting, lint, tests, coverage, dependency and secret scanning, SonarQube quality gates.
8. **How quickly should reviews happen?** Within about a business day; long delays hurt flow. Set team SLAs.
9. **Blocking vs non-blocking comments?** Blocking: bugs, security, broken design. Non-blocking (nit): style or preference.
10. **Benefits beyond bugs?** Knowledge sharing, consistent standards, mentoring, collective ownership.

---

## 5. Security by Design

**Key points**
- Build security in from requirements and design, not as a late add-on ("shift left").
- Principles: **least privilege, defense in depth, secure defaults, fail securely, minimize attack surface, separation of duties, zero trust, don't trust input**.
- **Threat modeling** (STRIDE): Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege.
- **OWASP Top 10** awareness: broken access control, injection, cryptographic failures, insecure design, misconfiguration, vulnerable components, auth failures, logging failures, SSRF.
- Secure SDLC: threat model → secure coding → SAST/SCA/secret scanning → DAST → pen test → monitoring.
- Data protection: encryption in transit (TLS) and at rest (KMS), PII minimization/masking, secrets management.

**Questions**
1. **What does Security by Design mean?** Considering security from the start of design and development, making it a default property of the system.
2. **What is least privilege?** Grant only the minimum permissions needed (IAM roles, DB users, service accounts).
3. **What is defense in depth?** Layered controls (WAF, network, auth, validation, encryption, monitoring) so one failure isn't fatal.
4. **What is threat modeling?** Systematically identifying assets, entry points, threats (STRIDE), and mitigations during design.
5. **How do you prevent SQL injection?** Parameterized queries/ORM, input validation, least-privilege DB accounts.
6. **How do you prevent XSS and CSRF?** XSS: output encoding, CSP, sanitize input. CSRF: tokens, SameSite cookies.
7. **How do you handle secrets?** Never in code or repo; Secrets Manager/Vault, rotation, scanning for leaks.
8. **How do you secure APIs?** AuthN/AuthZ (OAuth2/JWT), TLS, rate limiting, validation, no sensitive data in logs, proper error messages.
9. **How do you manage vulnerable dependencies?** SCA tools (Dependabot, Snyk, OWASP Dependency-Check), regular updates, SBOM.
10. **Authentication vs authorization?** Verifying identity vs determining permissions.
11. **What security checks go into CI/CD?** SAST, SCA, secret scanning, container/IaC scanning, DAST in staging, signed artifacts.
12. **How do you handle PII/compliance?** Data classification, encryption, masking, access controls, audit logs, retention/deletion (GDPR, SOC 2, HIPAA).
13. **Why is logging/monitoring a security matter?** Detect attacks and support incident response; don't log secrets or PII.

---

## Cross-Practice / Behavioral Questions

1. **Describe how your team delivers a feature end to end.** Backlog refinement → sprint planning → pair/TDD development → PR + review + CI (tests, scans) → deploy → demo in review → retro.
2. **How do TDD and code review improve quality together?** Tests prove behavior and protect refactors; reviews catch design, security, and readability issues tests don't.
3. **Tell me about a disagreement with a teammate.** Use STAR: listen, use data, find common goals, agree and commit.
4. **How do you balance speed and quality?** Automate checks, keep PRs small, enforce Definition of Done, manage tech debt explicitly.
5. **How do you onboard onto an unfamiliar codebase?** Pair with teammates, read tests and docs, run the app, make small first PRs.
6. **How do you embed security in an agile team?** Security acceptance criteria in stories, threat modeling in refinement, automated scans in CI, security champions.
7. **Tell me about a time you made a mistake in production.** Own it, restore service, root-cause (blameless postmortem), add safeguards.

---

## Core Concepts to Know Cold

- **Red-Green-Refactor**, test pyramid, mocks vs stubs.
- **Scrum roles/events/artifacts**, Definition of Done, velocity, user stories (INVEST).
- **Driver/navigator**, ping-pong pairing.
- **Code review checklist** and respectful feedback.
- **Least privilege, defense in depth, threat modeling (STRIDE), OWASP Top 10.**
- **Shift-left:** automated tests and security scans in CI.
- **STAR method** for behavioral answers.
