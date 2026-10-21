# ⚛️ React Coding Practice

All **10** challenges from the [HackerRank React track](https://www.hackerrank.com/domains/react), grouped by HackerRank section, with the same names and difficulty. Every problem is in text (the animated previews are described in words), solved, explained, and covered by tests built from HackerRank's requirements.

| | Section | Challenges | 🟢 Easy | 🟡 Medium | 🔴 Hard |
|---|---|---|---|---|---|
| 1️⃣ | [Components](#1-components-3) | 3 | 0 | 2 | 1 |
| 2️⃣ | [State Management](#2-state-management-1) | 1 | 0 | 1 | 0 |
| 3️⃣ | [Data Handling](#3-data-handling-3) | 3 | 0 | 2 | 1 |
| 4️⃣ | [Forms](#4-forms-2) | 2 | 0 | 2 | 0 |
| 5️⃣ | [Interaction](#5-interaction-1) | 1 | 0 | 1 | 0 |
| | **Total** | **10** | **0** | **8** | **2** |

## 📖 How to study one exercise

1. Read the problem in the exercise's `README.md` and try building the component yourself.
2. Check **🧪 Sample interaction**: what the user does and what must appear.
3. Read **💡 Solution**: the key idea first, then the component and how it works.
4. Run it with `npm run dev` and click through it; run `npm test` to check it against the requirements.
5. Solve it on HackerRank (its starter project already has the markup and `data-testid`s) and mark it ✅ below.

## ▶️ Running

Needs [Node.js](https://nodejs.org) 20 or newer. In a terminal in this `react` folder:

```
npm install        # once: downloads React, Vite, Vitest, Testing Library
npm run dev        # opens the exercise picker at http://localhost:5173
npm test           # runs every Solution.test.jsx
npx vitest run src/exercises/components/slideshow   # only one exercise
```

> [!TIP]
> Practise by renaming a `Solution.jsx`, writing your own version in its place, and running `npm run test:watch`: the tests rerun every time you save.

## 📄 What's in each exercise

| | File | What it's for |
|---|---|---|
| 📝 | `README.md` | The problem, the sample interaction, and the explained solution |
| ⚛️ | `Solution.jsx` | The component, commented |
| 🧪 | `Solution.test.jsx` | Vitest + Testing Library tests from the requirements |
| 🗂️ | `data.js` / `medicalRecords.js` | Sample data, when the exercise needs some |

## 1️⃣ Components (3)

| # | Challenge | Level | Component | Tests | Done |
|---|---|---|---|---|---|
| 1 | [Item List Manager](src/exercises/components/item-list-manager/README.md) | 🟡 Medium | [⚛️ Solution.jsx](src/exercises/components/item-list-manager/Solution.jsx) | [🧪 tests](src/exercises/components/item-list-manager/Solution.test.jsx) | ⬜ |
| 2 | [Slideshow](src/exercises/components/slideshow/README.md) | 🟡 Medium | [⚛️ Solution.jsx](src/exercises/components/slideshow/Solution.jsx) | [🧪 tests](src/exercises/components/slideshow/Solution.test.jsx) | ⬜ |
| 3 | [Word Omitter](src/exercises/components/word-omitter/README.md) | 🔴 Hard | [⚛️ Solution.jsx](src/exercises/components/word-omitter/Solution.jsx) | [🧪 tests](src/exercises/components/word-omitter/Solution.test.jsx) | ⬜ |

## 2️⃣ State Management (1)

| # | Challenge | Level | Component | Tests | Done |
|---|---|---|---|---|---|
| 1 | [Code Review Feedback](src/exercises/state-management/code-review-feedback/README.md) | 🟡 Medium | [⚛️ Solution.jsx](src/exercises/state-management/code-review-feedback/Solution.jsx) | [🧪 tests](src/exercises/state-management/code-review-feedback/Solution.test.jsx) | ⬜ |

## 3️⃣ Data Handling (3)

| # | Challenge | Level | Component | Tests | Done |
|---|---|---|---|---|---|
| 1 | [Article Sorting](src/exercises/data-handling/article-sorting/README.md) | 🔴 Hard | [⚛️ Solution.jsx](src/exercises/data-handling/article-sorting/Solution.jsx) | [🧪 tests](src/exercises/data-handling/article-sorting/Solution.test.jsx) | ⬜ |
| 2 | [Blog Post](src/exercises/data-handling/blog-post/README.md) | 🟡 Medium | [⚛️ Solution.jsx](src/exercises/data-handling/blog-post/Solution.jsx) | [🧪 tests](src/exercises/data-handling/blog-post/Solution.test.jsx) | ⬜ |
| 3 | [CryptoRank Exchange](src/exercises/data-handling/cryptorank-exchange/README.md) | 🟡 Medium | [⚛️ Solution.jsx](src/exercises/data-handling/cryptorank-exchange/Solution.jsx) | [🧪 tests](src/exercises/data-handling/cryptorank-exchange/Solution.test.jsx) | ⬜ |

## 4️⃣ Forms (2)

| # | Challenge | Level | Component | Tests | Done |
|---|---|---|---|---|---|
| 1 | [Contact Form](src/exercises/forms/contact-form/README.md) | 🟡 Medium | [⚛️ Solution.jsx](src/exercises/forms/contact-form/Solution.jsx) | [🧪 tests](src/exercises/forms/contact-form/Solution.test.jsx) | ⬜ |
| 2 | [Employee Validation](src/exercises/forms/employee-validation/README.md) | 🟡 Medium | [⚛️ Solution.jsx](src/exercises/forms/employee-validation/Solution.jsx) | [🧪 tests](src/exercises/forms/employee-validation/Solution.test.jsx) | ⬜ |

## 5️⃣ Interaction (1)

| # | Challenge | Level | Component | Tests | Done |
|---|---|---|---|---|---|
| 1 | [Patient Medical Records](src/exercises/interaction/patient-medical-records/README.md) | 🟡 Medium | [⚛️ Solution.jsx](src/exercises/interaction/patient-medical-records/Solution.jsx) | [🧪 tests](src/exercises/interaction/patient-medical-records/Solution.test.jsx) | ⬜ |

> [!TIP]
> Change ⬜ to ✅ in the **Done** column as you finish each challenge.

---

🛠️ How this was built (and how to do the same for another tech): [HACKERRANK-IMPORT.md](../HACKERRANK-IMPORT.md) · generator: [_tools/readmes.py](_tools/readmes.py)

**Back to:** [All Topics](../../Overview/All-Topics.md) · [Practices](../../Overview/Practices.md) · [🗄️ SQL exercises](../sql/README.md) · [☕ Java exercises](../java/README.md)
