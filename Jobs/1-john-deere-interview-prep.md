# Interview Prep: Senior Software Engineer, OF/OM Data Enablement (John Deere Financial)

**Job:** [Job #1 description](1-john-deere-senior-software-engineer-data-enablement.md) · **Hiring manager:** Devendra Singh · **Location:** Chicago, onsite

| Round | Who | What they're checking |
|---|---|---|
| 1️⃣ **Tomorrow** | Hiring manager | Your story, why this role, fit with the team, depth on 2–3 projects, how you work |
| 2️⃣ | Behavioral | Deere competencies, one STAR story per competency → [Behavioral guide](../Behavior/Behavioral-Interview-Questions.md) |
| 3️⃣ | Technical | Java/Spring REST, SQL & data modeling, ETL/Spark, AWS, TDD, CI/CD → [Overview sheets](../Overview/All-Topics.md) · [Code](../Code/) |

---

## 🎯 The one thing to get across

> You're **already a data engineer who builds APIs**, not a full-stack engineer trying to switch.
> Your whole career has been about moving and serving data accurately: PL/SQL and OLAP cubes at Tigo → ETL for credit reporting at Equifax → Spring Boot services on AWS serving Databricks data at Deere.

Your LinkedIn title says *Full-Stack Software Engineer*; the job says *Data Engineer*. Expect the manager to probe that gap. Lead with the data thread every time.

---

## 1️⃣ Tomorrow: the manager round

### What to expect (usually 30–60 min)

1. **"Walk me through your background"**: 2 minutes, not 10. Use the pitch below.
2. **"Why this role / why Data Enablement / why John Deere Financial?"**: you're an internal candidate, so expect **"why move from your current team?"** too.
3. **Deep dive on 1–3 projects**: architecture, *your* part, decisions, trade-offs, results. Not code.
4. **How you work**: Agile ceremonies, code reviews, pair programming, onboarding people, handling production issues, tech debt.
5. **Fit and logistics**: onsite Chicago (you're hybrid today), timing of a move, maybe salary expectations.
6. **Your questions for them**: always have 4–6 ready (see [Questions to ask](#-questions-to-ask-the-manager)).

### Your 60-second pitch (practice it out loud)

> "I'm a software engineer with over 10 years of experience, the last four at John Deere, and data has been the thread through all of it.
> I started in Honduras at Tigo building PL/SQL data processing, OLAP cubes and dashboards for leadership.
> At Equifax I maintained the ETL pipelines that onboarded banks onto the PayNet credit-reporting platform and helped migrate it to Google Cloud with Apache Beam, where data accuracy was everything.
> At Deere I build Spring Boot services on AWS. Most recently I built the Users Service from scratch: it pulls from the Databricks EDL and is now the platform's single source of truth for user data.
> I also lead the work that keeps teams fast and secure: moving our critical pipeline from Jenkins to GitHub Actions, centralising 30+ secrets in AWS Secrets Manager, and an agentic GitHub workflow that auto-fixes security findings.
> This role brings together what I enjoy most: data models and pipelines, REST APIs that serve that data downstream, and the security and CI/CD around them. And doing it for John Deere Financial, where data has to be right, feels like a natural fit after Equifax."

### "Why this move?" (internal candidate)

Keep it positive about your current team: **pull, not push**.
- You want to go deeper on **data engineering** (pipelines, modeling, warehousing) rather than spreading across frontend + backend + DevOps in 35+ repos.
- Financial data is where your Equifax background (credit data, accuracy, compliance) adds the most.
- You already know Deere's platforms, AWS accounts, Databricks EDL, security tooling and ways of working: **short ramp-up**.

---

## 🧩 Your experience vs. the job

| Job asks for | Your evidence | Strength |
|---|---|---|
| **ETL, data modeling, warehousing (4+ yrs)** | Equifax ETL (SSIS, Perl, SQL, stored procs) for PayNet; Apache Beam on GCP Data Fabric; Tigo OLAP cubes for revenue/budget/forecast; DB2 → PostgreSQL migration (20 tables) | ✅ Strong |
| **REST APIs in Java / Spring Boot (4+ yrs)** | 4+ yrs at Deere: Users Service, Conversations, MOCI server-core (375+ commits) | ✅ Strong |
| **TDD (2+ yrs)** | Automated Java test scripts at Equifax, TSQLT; tests in your Deere services | ⚠️ Prepare one concrete TDD story |
| **CI/CD, Git, Jenkins** | Led Jenkins → GitHub Actions migration for the most critical pipeline; release admin at Equifax | ✅ Strong |
| **Spark, Databricks, Python, SQL, NoSQL, Data Lake** | Databricks EDL integration (OAuth service principal); Apache Beam (same model as Spark); deep SQL | ⚠️ Python / Spark / NoSQL: be ready to talk about what you know and how you'd ramp |
| **AWS: Lambda, RDS, ECS, DynamoDB, API Gateway, S3** | Lambda JWT authorizer, RDS/Aurora, ECS, WebSocket APIs, Secrets Manager, CloudFormation | ✅ Strong (DynamoDB lighter) |
| **Gen AI & agentic patterns** | Agentic GitHub Actions workflow that auto-remediates Mend / CodeQL / GitHub Security findings with verified fix PRs | ⭐ Standout |
| **Graph databases** | Not in your experience | ⚠️ Know the basics (nodes, edges, Cypher, when to use one) |
| **Security by Design** | Secrets Manager migration, Okta JWT authorizer closing a Shield finding, Equifax anonymization tool | ✅ Strong |
| **Root cause, production support** | 15+ production incidents resolved; ES logging cluster retired with zero data loss | ✅ Strong |
| **Reduce tech debt** | Jenkins → GHA, DB2 → Postgres, ES retirement, Storybook v8 → v10 | ✅ Strong |
| **Onboard new team members** | Onboarding Coach for engineers and interns | ✅ Strong |
| **Explain to non-technical people** | Equifax stakeholder scoping; Motorola billing ↔ IT requirements; bilingual | ✅ Strong |

**How to handle a ⚠️:** be honest, connect it to something close, and show how you'd close it.
> "I haven't run graph databases in production. I understand the model, nodes and relationships queried with Cypher, and it's a good fit for things like account hierarchies or ownership chains. I've been studying Neo4j and would expect to be productive quickly, the same way I picked up Databricks for the Users Service."

---

## 📚 Stories to have ready (STAR: Situation, Task, Action, Result)

Have the numbers ready. Say **"I"** for your part, **"we"** for the team's.

| # | Story | Shows | Key numbers |
|---|---|---|---|
| 1 | **Users Service from scratch**: Spring Boot + Databricks EDL via OAuth-federated service principal; now single source of truth | Data APIs, ownership, design | Platform-wide source of truth |
| 2 | **DB2 → PostgreSQL on RDS + retiring the Elasticsearch logging cluster** | Data migration, data modeling, zero-downtime, risk management | 20 tables, 6 repos, zero data loss |
| 3 | **Equifax ETL for PayNet + GCP / Apache Beam migration** | ETL, data quality, stakeholder work | Bank onboarding, Perl → Java/Beam |
| 4 | **Agentic security workflow** | Gen AI / agentic patterns, innovation | 100% vulnerability coverage, triage → review-and-merge |
| 5 | **Secrets Manager migration + Okta JWT authorizer** | Security by Design | 10+ repos, 30+ secrets, Shield finding closed |
| 6 | **Jenkins → GitHub Actions for the most critical pipeline** | CI/CD, tech debt, leading change | Most critical pipeline |
| 7 | **A production incident you root-caused** | Debugging, accountability | Pick 1 of the 15+ |
| 8 | **Conversations + translation pipeline** | End-to-end delivery, real-time systems | 4+ languages, every PR |
| 9 | **Global User Preferences platform** | Reusable design, adoption | Used by multiple teams |
| 10 | **Onboarding Coach** | Mentoring, team building | Engineers and interns |

For the manager round, rehearse **1, 2, 3 and 4** in depth. Expect follow-ups like *"what would you do differently?"*, *"what was the hardest part?"*, *"how did you test it?"*, *"how did you know it worked?"*.

---

## ❓ Likely manager questions

- Tell me about yourself.
- Why are you interested in this role? Why leave your current team?
- What's the most complex data pipeline or data model you've built? Walk me through it.
- How do you make sure data is accurate and trustworthy end to end?
- Tell me about a time you reduced technical debt. How did you convince people it was worth it?
- How do you approach testing? Do you practise TDD? Give an example.
- Describe a production issue you owned from alert to root cause to prevention.
- How do you handle code reviews: giving and receiving feedback?
- How have you used Gen AI in your work? What are the risks?
- How would you onboard a new engineer to this team?
- How do you work with product owners or business users who aren't technical?
- What are you looking for in your next manager / team?
- Where do you want to be in 2–3 years?
- This role is onsite in Chicago. Does that work for you?

---

## 🙋 Questions to ask the manager

Pick 4–6. Ask the logistics ones near the end, after you've shown interest in the work.

### Work model and travel

> The posting says **Work Model: Onsite** (Chicago, World Hq), and travel isn't mentioned. Ask to confirm, without sounding like a condition.

1. The posting lists the role as onsite. What does a typical week look like for the team: how many days in the office, and is there any flexibility?
2. Where does the team sit day to day: World Hq downtown, or another Chicago office? Is everyone in the same location?
3. Does the role involve any travel, for example to Moline, Johnston (JDF), or partner sites? Roughly how often?
4. Is there an on-call or production-support rotation? How does it work?

### The team

5. How big is the team, and what's the mix of roles (data engineers, backend, QA, product owner, architects)?
6. Is the team all in Chicago, or spread across locations and time zones? How do you collaborate across them?
7. Who are the main customers of the team's data and APIs, and how closely do engineers work with them?
8. How does work flow from idea to production: backlog refinement, sprint length, how releases go out?
9. How do code reviews and pair programming work day to day?
10. What do you value most in the engineers on your team? What separates the great ones?
11. How long have people been on the team? Why is this position open (new role or backfill)?

### The work

12. What does the team own today: which data domains, pipelines and APIs?
13. What's the current stack in practice: Databricks vs. Spark elsewhere, which warehouse or lake, where graph databases fit?
14. What's the biggest technical-debt or data-quality pain right now?
15. How do you see Gen AI and agentic patterns being used in Data Enablement?

### Success and growth

16. What would success look like for this person in the first 90 days? In the first year?
17. What are the biggest challenges the team will face in the next 6–12 months?
18. How do you support growth: training, AWS certifications, a path toward Staff/Lead?
19. How would you describe your management style? How do you like to give feedback?

### To close

20. Is there anything in my background that makes you hesitate? I'd like the chance to address it.
21. What are the next steps, and when should I expect to hear back?

---

## ✅ Tonight's checklist

- [ ] Say the 60-second pitch out loud 3 times (time it).
- [ ] Rehearse stories 1–4 in STAR form, with numbers.
- [ ] Prepare a 1-minute answer for "why leave your current team?"
- [ ] Prepare the honest answers for the ⚠️ gaps: TDD example, Python/Spark, NoSQL/DynamoDB, graph databases.
- [ ] Re-read the job description's *Responsibilities* and *What Makes You Stand Out*.
- [ ] Write down your questions for the manager.
- [ ] Look up Devendra Singh on LinkedIn / Deere's directory: team, background, what they've worked on.
- [ ] If you haven't already, check Deere's internal-transfer rules on telling your current manager.
- [ ] Have a salary range ready in case it comes up (posted range: $124,584 – $186,864).

## After tomorrow

- **Behavioral round:** the 12 competencies in the [Behavioral guide](../Behavior/Behavioral-Interview-Questions.md) are what Deere-style behavioral interviews use. Map one story from the table above to each competency.
- **Technical round:** [Practices](../Overview/Practices.md) · [AWS](../Overview/AWS.md) · [Data](../Overview/Data.md) · [Spring Boot](../Overview/Frameworks.md) · [DevOps](../Overview/DevOps.md) · [Gen AI](../Overview/GenAI.md), plus Java/SQL exercises in [Code](../Code/).
