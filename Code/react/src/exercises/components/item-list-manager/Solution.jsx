// Item List Manager  (Medium · Components)  https://www.hackerrank.com/challenges/item-list-manager/problem
// Description and explanation: README.md (same folder). Tests: Solution.test.jsx
//
// How it works:
// - Two pieces of state: the list of items, and the text currently in the input.
// - The input is "controlled": its value comes from state and every keystroke updates the state.
// - Add Item ignores empty (or spaces-only) text; otherwise it appends the text and clears the input.
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
