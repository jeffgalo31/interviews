import { describe, it, expect } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import Articles from "./Solution.jsx";
import { ARTICLES } from "./data.js";

const titles = () => screen.getAllByTestId("article-title").map((td) => td.textContent);

describe("Article Sorting", () => {
  it("shows the articles by upvotes (descending) by default", () => {
    render(<Articles articles={ARTICLES} />);
    expect(screen.getAllByTestId("article")).toHaveLength(7);
    expect(titles()).toEqual([
      "Scaling to 100k Users", "the Emu War", "Alphabet earnings", "A message to our customers",
      "Simple text editor has 15k monthly users", "Artificial Mountains", "What's SAP",
    ]);
  });

  it("sorts by date when clicking Most Recent, and back by upvotes", () => {
    render(<Articles articles={ARTICLES} />);
    fireEvent.click(screen.getByRole("button", { name: "Most Recent" }));
    expect(titles()).toEqual([
      "A message to our customers", "Alphabet earnings", "Artificial Mountains", "What's SAP",
      "the Emu War", "Scaling to 100k Users", "Simple text editor has 15k monthly users",
    ]);
    fireEvent.click(screen.getByRole("button", { name: "Most Upvoted" }));
    expect(titles()[0]).toBe("Scaling to 100k Users");
  });

  it("does not change the array it receives", () => {
    const input = [...ARTICLES];
    render(<Articles articles={input} />);
    fireEvent.click(screen.getByRole("button", { name: "Most Recent" }));
    expect(input).toEqual(ARTICLES);
  });
});
