<!-- study-layout -->
# Code Review Feedback

🟡 **Medium** · 📁 **State Management** · ⚛️ HackerRank React · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/code-review-feedback/problem)

**On this page:** [📝 Problem](#-problem) · [🧪 Sample interaction](#-sample-interaction) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Your task is to create a React application called "Code Review Feedback" that tracks and manages feedback on various aspects of code quality. The component should have upvote and downvote functionality for each aspect, and it must meet all specified requirements.

> [!NOTE]
> 🎞️ **Preview (an animated GIF on HackerRank), in words:** Five cards in a row (**Readability, Performance, Security, Documentation, Testing**). Each card has a green **👍 Upvote** and a red **👎 Downvote** button and two lines, *Upvotes: 0* and *Downvotes: 0*. Clicking a button increases that card's count by 1 with a small "pop" animation on the number.

### Detailed Requirements

1. The CodeReviewFeedback component displays five aspects: Readability, Performance, Security, Documentation, and Testing.
2. Each aspect has two buttons labeled "Upvote" and "Downvote" to allow users to vote.
3. The initial count for upvotes and downvotes for each aspect is set to zero.
4. Clicking the "Upvote" button should increment the upvote count for that aspect by 1.
5. Clicking the "Downvote" button should increment the downvote count for that aspect by 1.
6. Ensure the counts update in the UI immediately upon clicking.
7. The component should have a subtle animation when the voting count is updated to enhance the user experience.

## 🧪 Sample interaction

### Initial State

1. Display all five aspects with their respective upvote and downvote buttons.
2. Each aspect shows an initial count of 0 for upvotes and downvotes.

### User Action 1

1. User clicks "Upvote" for Readability.
2. The upvote count for Readability displays 1.

### User Action 2

1. User clicks "Downvote" for Performance.
2. The downvote count for Performance displays 1.

### User Action 3

3. User clicks "Upvote" for Security and Documentation multiple times.
4. The upvote count for Security displays 2 and Documentation displays 3.

## 💡 Solution

> [!TIP]
> **Key idea:** One array of `{ upvotes, downvotes }` objects (one per aspect) in state; a click copies the array and changes only that aspect.

### ✍️ The component

```jsx
import { useState } from "react";

const ASPECTS = ["Readability", "Performance", "Security", "Documentation", "Testing"];

export default function CodeReviewFeedback() {
  const [votes, setVotes] = useState(ASPECTS.map(() => ({ upvotes: 0, downvotes: 0 })));

  const vote = (index, type) => {
    setVotes((prev) =>
      prev.map((v, i) => (i === index ? { ...v, [type]: v[type] + 1 } : v))
    );
  };

  return (
    <div className="grid">
      {ASPECTS.map((aspect, index) => (
        <div className="card" key={aspect}>
          <h2>{aspect}</h2>
          <div className="row">
            <button className="good" onClick={() => vote(index, "upvotes")} data-testid={`upvote-btn-${index}`}>
              👍 Upvote
            </button>
            <button className="bad" onClick={() => vote(index, "downvotes")} data-testid={`downvote-btn-${index}`}>
              👎 Downvote
            </button>
          </div>
          <p data-testid={`upvote-count-${index}`}>
            Upvotes: <strong key={votes[index].upvotes} className="pop">{votes[index].upvotes}</strong>
          </p>
          <p data-testid={`downvote-count-${index}`}>
            Downvotes: <strong key={votes[index].downvotes} className="pop">{votes[index].downvotes}</strong>
          </p>
        </div>
      ))}
    </div>
  );
}
```

### 🔍 How it works

- `setVotes(prev => prev.map((v, j) => j === i ? { ...v, upvotes: v.upvotes + 1 } : v))`: the updater form always uses the latest state.
- The "subtle animation": the number is rendered with `key={count}`, so every new count mounts a fresh element and the CSS `pop` animation plays again.
- Upvote / downvote buttons and counts use `data-testid` like `upvote-btn-0`, `upvote-count-0` (the starter project's names).
- On HackerRank the starter project already has the markup and the `data-testid` attributes the tests look for: keep them and add the state and handlers shown here.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ⚛️ | [Solution.jsx](Solution.jsx) | The component, commented. See it with `npm run dev` (in `react`) and pick it in the sidebar |
| 🧪 | [Solution.test.jsx](Solution.test.jsx) | Tests built from HackerRank's requirements: `npm test` |

📋 **On HackerRank:** the starter project already has the markup and `data-testid`s; copy the state and handlers into its component.

---

⬅️ [Word Omitter](../../components/word-omitter/README.md) · [⚛️ All React exercises](../../../../README.md) · [Article Sorting](../../data-handling/article-sorting/README.md) ➡️
