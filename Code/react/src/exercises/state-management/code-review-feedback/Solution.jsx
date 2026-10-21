// Code Review Feedback  (Medium · State Management)  https://www.hackerrank.com/challenges/code-review-feedback/problem
// Description and explanation: README.md (same folder). Tests: Solution.test.jsx
//
// How it works:
// - One state value holds the counts for all five aspects: [{ upvotes, downvotes }, ...].
// - A click creates a NEW array with only that aspect's count changed (state must not be mutated).
// - The animation: the count's <span> gets a `key` equal to the count, so React re-creates it on every
//   change and the CSS "pop" animation (styles.css) plays again.
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
