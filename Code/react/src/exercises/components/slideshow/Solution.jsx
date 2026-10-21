// Slideshow  (Medium · Components)  https://www.hackerrank.com/challenges/react-slideshow-1/problem
// Description and explanation: README.md (same folder). Tests: Solution.test.jsx
//
// How it works:
// - The only state is the index of the current slide (0 = first).
// - Each button changes the index; its `disabled` flag is computed from the index:
//   Restart and Prev are disabled on the first slide, Next on the last one.
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
