// Article Sorting  (Hard · Data Handling)  https://www.hackerrank.com/challenges/react-article-sorting/problem
// Description and explanation: README.md (same folder). Tests: Solution.test.jsx
//
// How it works:
// - Keep only the sort KEY in state ("upvotes" or "date"), not a sorted copy of the articles.
// - Derive the sorted list while rendering: copy the prop with [...articles] and sort the copy
//   (sort() changes the array in place, and props must never be mutated).
// - Dates are "YYYY-MM-DD" strings, so comparing them as text already orders them by date.
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
