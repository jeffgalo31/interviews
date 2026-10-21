// Word Omitter  (Hard · Components)  https://www.hackerrank.com/challenges/react-word-omitter/problem
// Description and explanation: README.md (same folder). Tests: Solution.test.jsx
//
// How it works:
// - State: the textarea text and a boolean "omit mode" (on by default).
// - The output is DERIVED on each render: split the text into words, drop the ones in omitWords
//   (compared in lower case) when omit mode is on, and join them back with spaces.
// - The toggle button's label shows what clicking it will do next.
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
