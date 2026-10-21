<!-- study-layout -->
# Word Omitter

🔴 **Hard** · 📁 **Components** · ⚛️ HackerRank React · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/react-word-omitter/problem)

**On this page:** [📝 Problem](#-problem) · [🧪 Sample interaction](#-sample-interaction) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

You are tasked with creating a simple React application called "Word Omitter" that dynamically filters out specific words from the user input in real-time. The application requirements are detailed below, and the finished application must pass all of the unit tests.

### Detailed Requirements

1. The WordOmitter component takes an array of words to omit as a prop called omitWords. Each element of this array is a string representing a word that should be filtered out of the user's input.
2. The application should display a text input field where the user can type a sentence.
3. As the user types, the output area below the input field should display the sentence with the specified words omitted.
4. The application should have a toggle button to switch between omitting the specified words and showing all words.
5. The application should have a clear button that clears both the input field and the output area.
6. If the input field is empty, the output area should also be empty.

## 🧪 Sample interaction

### Initial State

- The input field is empty.
- The output area is empty.
- The button displays "Show All Words" i.e. Omit Mode is enabled

### User Action 1

- User types "This is a test sentence." in the input field.
- The output area displays "This is test sentence." (assuming "a" is omitted).

### User Action 2

- User clicks the toggle button.
- The output area now displays "This is a test sentence." (showing all words).

### User Action 3

- User clicks the clear button.
- Both the input field and the output area are cleared.

## 💡 Solution

> [!TIP]
> **Key idea:** Keep only the raw text and an "omit mode" boolean in state; the output is **derived** on each render.

### ✍️ The component

```jsx
import { useState } from "react";

const OMITTED_WORDS = ["a", "the", "and", "or", "but"];

export default function WordOmitter({ omitWords = OMITTED_WORDS }) {
  const [inputText, setInputText] = useState("");
  const [omit, setOmit] = useState(true);

  const omitted = new Set(omitWords.map((w) => w.toLowerCase()));
  const words = inputText.split(/\s+/).filter(Boolean);
  const output = (omit ? words.filter((w) => !omitted.has(w.toLowerCase())) : words).join(" ");

  return (
    <div className="card wide">
      <textarea
        placeholder="Type here..."
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        data-testid="input-area"
      />
      <div className="row">
        <button onClick={() => setOmit(!omit)} data-testid="action-btn">
          {omit ? "Show All Words" : "Omit Words"}
        </button>
        <button onClick={() => setInputText("")} data-testid="clear-btn">Clear</button>
      </div>
      <div>
        <h2>Output:</h2>
        <p data-testid="output-text">{output}</p>
      </div>
    </div>
  );
}
```

### 🔍 How it works

- Split on whitespace, drop words whose lower-case form is in `omitWords` (only in omit mode), join with spaces.
- The toggle's label tells what the next click does: "Show All Words" while omitting, "Omit Words" while showing all.
- Clear sets the text to `""`; empty text gives empty output automatically.
- On HackerRank the starter project already has the markup and the `data-testid` attributes the tests look for: keep them and add the state and handlers shown here.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ⚛️ | [Solution.jsx](Solution.jsx) | The component, commented. See it with `npm run dev` (in `react`) and pick it in the sidebar |
| 🧪 | [Solution.test.jsx](Solution.test.jsx) | Tests built from HackerRank's requirements: `npm test` |

📋 **On HackerRank:** the starter project already has the markup and `data-testid`s; copy the state and handlers into its component.

---

⬅️ [Slideshow](../slideshow/README.md) · [⚛️ All React exercises](../../../../README.md) · [Code Review Feedback](../../state-management/code-review-feedback/README.md) ➡️
