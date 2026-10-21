<!-- study-layout -->
# Article Sorting

🔴 **Hard** · 📁 **Data Handling** · ⚛️ HackerRank React · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/react-article-sorting/problem)

**On this page:** [📝 Problem](#-problem) · [🧪 Sample interaction](#-sample-interaction) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Create a React application called "Article Sorting" that displays a list of articles and allows users to sort them based on upvotes and publication date. Some core functionalities have already been implemented, but the application is not complete. Application requirements are detailed below, and the finished application must pass all of the unit tests.

> [!NOTE]
> 🎞️ **Preview (an animated GIF on HackerRank), in words:** A **Sorting Articles** page with two buttons, *Most Upvoted* and *Most Recent*, above a table:
>
> | Title | Upvotes | Date |
> |---|---|---|
> | Scaling to 100k Users | 72 | 2019-01-21 |
> | the Emu War | 24 | 2019-10-21 |
> | Alphabet earnings | 22 | 2019-11-23 |
> | A message to our customers | 12 | 2020-01-24 |
> | Simple text editor has 15k monthly users | 7 | 2010-12-31 |
> | Artificial Mountains | 2 | 2019-11-22 |
> | What's SAP | 1 | 2019-11-21 |
>
> Clicking *Most Recent* reorders the rows by date (2020-01-24 first); *Most Upvoted* puts them back in the order above.

### Detailed Requirements

1. The Articles component takes an array of articles as a prop. Each element of this array is an object with three properties: a string title, a number upvotes, and a string date in the format YYYY-MM-DD.
2. By default, the articles should be displayed in a table ordered by the number of upvotes in descending order.
3. Clicking on the "Most Upvoted" button should reorder and display the articles by the number of upvotes in descending order.
4. Clicking on the "Most Recent" button should reorder and display the articles by date in descending order.
5. You can assume that each article has a unique publish date and number of upvotes.

## 🧪 Sample interaction

### Initial State

1. The articles are displayed in the table, ordered by the number of upvotes in descending order.
2. The "Most Upvoted" button and the "Most Recent" button are displayed.

### User Action 1

1. User clicks "Most Recent" button.
2. The articles are reordered and displayed by date in descending order.

### User Action 2

1. User clicks "Most Upvoted" button.
2. The articles are reordered and displayed by the number of upvotes in descending order.

## 💡 Solution

> [!TIP]
> **Key idea:** Store only **how** to sort (`"upvotes"` or `"date"`), and sort a **copy** of the prop on every render: `[...articles].sort(...)`.

### ✍️ The component

```jsx
import { useState } from "react";
import { ARTICLES } from "./data.js";

const SORTERS = {
  upvotes: (a, b) => b.upvotes - a.upvotes,          // most upvoted first
  date: (a, b) => b.date.localeCompare(a.date),      // most recent first
};

export default function Articles({ articles = ARTICLES }) {
  const [sortBy, setSortBy] = useState("upvotes");   // default: most upvoted
  const sorted = [...articles].sort(SORTERS[sortBy]);

  return (
    <div className="card wide">
      <div className="row">
        <span className="label">Sort by</span>
        <button onClick={() => setSortBy("upvotes")} data-testid="most-upvoted-link">Most Upvoted</button>
        <button onClick={() => setSortBy("date")} data-testid="most-recent-link">Most Recent</button>
      </div>
      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Upvotes</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {sorted.map((article) => (
            <tr data-testid="article" key={article.title}>
              <td data-testid="article-title">{article.title}</td>
              <td data-testid="article-upvotes">{article.upvotes}</td>
              <td data-testid="article-date">{article.date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
```

### 🔍 How it works

- `sort()` changes the array in place, so sorting the prop directly would mutate data owned by the parent; `[...articles]` avoids that.
- Upvotes: `b.upvotes - a.upvotes` (descending). Dates in `YYYY-MM-DD` form can be compared as text: `b.date.localeCompare(a.date)`.
- The default order is by upvotes, so `useState("upvotes")`.
- On HackerRank the starter project already has the markup and the `data-testid` attributes the tests look for: keep them and add the state and handlers shown here.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ⚛️ | [Solution.jsx](Solution.jsx) | The component, commented. See it with `npm run dev` (in `react`) and pick it in the sidebar |
| 🧪 | [Solution.test.jsx](Solution.test.jsx) | Tests built from HackerRank's requirements: `npm test` |
| 🗂️ | [data.js](data.js) | Data the component uses (same shape as in HackerRank's starter project) |

📋 **On HackerRank:** the starter project already has the markup and `data-testid`s; copy the state and handlers into its component.

---

⬅️ [Code Review Feedback](../../state-management/code-review-feedback/README.md) · [⚛️ All React exercises](../../../../README.md) · [Blog Post](../blog-post/README.md) ➡️
