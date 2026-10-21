<!-- study-layout -->
# Slideshow

🟡 **Medium** · 📁 **Components** · ⚛️ HackerRank React · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/react-slideshow-1/problem)

**On this page:** [📝 Problem](#-problem) · [🧪 Sample interaction](#-sample-interaction) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

You are tasked with creating a simple React application called "Basic Slideshow" that displays a series of slides and allows users to navigate through them. The application requirements are detailed below, and the finished application must pass all of the unit tests.

> [!NOTE]
> 🎞️ **Preview (an animated GIF on HackerRank), in words:** Three buttons **Restart · Prev · Next** above a slide card with a title and a line of text. Clicking Next moves through the workout slides until **Great job!** ("You made it, have a nice day and see you next time!"), where Next becomes disabled; on the first slide Restart and Prev are disabled.

### Detailed Requirements

1. The Slides component takes an array of slides as a prop. Each element of this array denotes a single slide and is an object with two properties: a string title and a string text.
2. When the application loads, the first slide must be rendered.
3. Clicking on the "Next" button shows the next slide. This button should be disabled when the current slide is the last one.
4. Clicking on the "Prev" button shows the previous slide. This button should be disabled when the current slide is the first one.
5. Clicking on the "Restart" button returns to the first slide. This button should be disabled when the current slide is the first one.
6. You can assume that the passed slides array contains at least one slide.

## 🧪 Sample interaction

### Initial State

- The first slide is displayed.
- The "Prev" and "Restart" buttons are disabled.

### User Action 1

- User clicks "Next" button.
- The next slide is displayed.
- The "Prev" and "Restart" buttons are enabled.

### User Action 2

- User clicks "Prev" button.
- The previous slide is displayed.
- The "Prev" button is disabled if the first slide is shown.

### User Action 3

- User clicks "Restart" button.
- The first slide is displayed.
- The "Prev" and "Restart" buttons are disabled.

## 💡 Solution

> [!TIP]
> **Key idea:** The only state is the current slide index; every button's `disabled` flag is **computed** from it.

### ✍️ The component

```jsx
import { useState } from "react";
import { SLIDES } from "./data.js";

export default function Slides({ slides = SLIDES }) {
  const [index, setIndex] = useState(0);
  const isFirst = index === 0;
  const isLast = index === slides.length - 1;

  return (
    <div className="card wide">
      <div className="row center">
        <button onClick={() => setIndex(0)} disabled={isFirst} data-testid="button-restart">Restart</button>
        <button onClick={() => setIndex((i) => i - 1)} disabled={isFirst} data-testid="button-prev">Prev</button>
        <button onClick={() => setIndex((i) => i + 1)} disabled={isLast} data-testid="button-next">Next</button>
      </div>
      <div className="slide" data-testid="slide">
        <h1 data-testid="title">{slides[index].title}</h1>
        <p data-testid="text">{slides[index].text}</p>
      </div>
    </div>
  );
}
```

### 🔍 How it works

- Restart → `setIndex(0)`, Prev → `i - 1`, Next → `i + 1`.
- Restart and Prev are disabled when `index === 0`; Next when `index === slides.length - 1` (so with one slide, all three are disabled).
- `data.js` holds the slides from HackerRank's starter project.
- On HackerRank the starter project already has the markup and the `data-testid` attributes the tests look for: keep them and add the state and handlers shown here.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ⚛️ | [Solution.jsx](Solution.jsx) | The component, commented. See it with `npm run dev` (in `react`) and pick it in the sidebar |
| 🧪 | [Solution.test.jsx](Solution.test.jsx) | Tests built from HackerRank's requirements: `npm test` |
| 🗂️ | [data.js](data.js) | Data the component uses (same shape as in HackerRank's starter project) |

📋 **On HackerRank:** the starter project already has the markup and `data-testid`s; copy the state and handlers into its component.

---

⬅️ [Item List Manager](../item-list-manager/README.md) · [⚛️ All React exercises](../../../../README.md) · [Word Omitter](../word-omitter/README.md) ➡️
