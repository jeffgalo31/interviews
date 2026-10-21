<!-- study-layout -->
# Item List Manager

🟡 **Medium** · 📁 **Components** · ⚛️ HackerRank React · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/item-list-manager/problem)

**On this page:** [📝 Problem](#-problem) · [🧪 Sample interaction](#-sample-interaction) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

You are tasked with creating a simple React application called "Item List Manager" that displays a list of items and allows users to add new items to the list. The items will be displayed in an unordered list (`<ul>`), and there will be an input field along with a button to add new items to this list.

> [!NOTE]
> 🎞️ **Preview (an animated GIF on HackerRank), in words:** A page with a header bar and an **Item List** heading, an input with the placeholder *Enter item* and a green **Add Item** button. Typing an item and clicking the button adds it as a new bullet in the list below and empties the input.

### Detailed Requirements

1. When the application loads, it should display an empty list.
2. The input field should accept user text input.
3. When the button is clicked:
4. The text from the input field should be added to the list.
5. The input field should be cleared.
6. If the input field is empty and the button is clicked, nothing should be added to the list.

## 🧪 Sample interaction

### Initial State

- The list is empty.
- The input field is empty.

### User Action 1

- User types "First Item" in the input field.
- User clicks "Add Item" button.
- The list displays "First Item".

### User Action 2

- User types "Second Item" in the input field.
- User clicks "Add Item" button.
- The list displays:
    - "First Item"
    - "Second Item"

## 💡 Solution

> [!TIP]
> **Key idea:** Keep two pieces of state, the list and the input text; render the list with `map()`.

### ✍️ The component

```jsx
import { useState } from "react";

export default function ItemListManager() {
  const [items, setItems] = useState([]);      // starts empty
  const [text, setText] = useState("");        // what's typed in the input

  const handleAddItem = () => {
    const value = text.trim();
    if (!value) return;                        // empty input: add nothing
    setItems((prev) => [...prev, value]);      // new array (never mutate state)
    setText("");                               // clear the input
  };

  return (
    <div className="card">
      <h2>Item List</h2>
      <input
        type="text"
        placeholder="Enter item"
        value={text}
        onChange={(e) => setText(e.target.value)}
        data-testid="input-field"
      />
      <button onClick={handleAddItem} data-testid="add-button">
        Add Item
      </button>
      <ul data-testid="item-list">
        {items.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
}
```

### 🔍 How it works

- The input is **controlled**: `value={text}` + `onChange` keeps React state and the box in sync.
- On click, ignore blank text (`trim()`), otherwise add it with `[...items, text]` (a **new** array, never `push`) and reset `text` to `""`.
- Each `<li>` needs a `key` so React can tell the items apart.
- On HackerRank the starter project already has the markup and the `data-testid` attributes the tests look for: keep them and add the state and handlers shown here.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ⚛️ | [Solution.jsx](Solution.jsx) | The component, commented. See it with `npm run dev` (in `react`) and pick it in the sidebar |
| 🧪 | [Solution.test.jsx](Solution.test.jsx) | Tests built from HackerRank's requirements: `npm test` |

📋 **On HackerRank:** the starter project already has the markup and `data-testid`s; copy the state and handlers into its component.

---

[⚛️ All React exercises](../../../../README.md) · [Slideshow](../slideshow/README.md) ➡️
