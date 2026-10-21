// Exercise picker: `npm run dev`, then choose an exercise on the left.
// The choice is kept in the URL hash (#slideshow), so a refresh keeps you on the same exercise.
import { useEffect, useState } from "react";
import { EXERCISES } from "./exercises/index.js";

const SECTIONS = [...new Set(EXERCISES.map((e) => e.section))];
const fromHash = () => window.location.hash.slice(1) || EXERCISES[0].slug;

export default function App() {
  const [slug, setSlug] = useState(fromHash);

  useEffect(() => {
    const onHash = () => setSlug(fromHash());
    window.addEventListener("hashchange", onHash);
    return () => window.removeEventListener("hashchange", onHash);
  }, []);

  const current = EXERCISES.find((e) => e.slug === slug) ?? EXERCISES[0];
  const { Component } = current;

  return (
    <div className="layout">
      <nav className="sidebar">
        <h1>⚛️ React practice</h1>
        {SECTIONS.map((section) => (
          <div key={section}>
            <h2>{section}</h2>
            {EXERCISES.filter((e) => e.section === section).map((e) => (
              <a key={e.slug} href={`#${e.slug}`} className={e.slug === current.slug ? "active" : ""}>
                {e.name} <small className={`tag ${e.difficulty.toLowerCase()}`}>{e.difficulty}</small>
              </a>
            ))}
          </div>
        ))}
      </nav>
      <main>
        <header>
          <h1>{current.name}</h1>
          <p>{current.section} · {current.difficulty} · <code>src/exercises/…/{current.slug}/Solution.jsx</code></p>
        </header>
        {/* key = slug: switching exercises mounts a fresh component (state starts over) */}
        <Component key={current.slug} />
      </main>
    </div>
  );
}
