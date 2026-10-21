import { describe, it, expect } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import CodeReviewFeedback from "./Solution.jsx";

const ASPECTS = ["Readability", "Performance", "Security", "Documentation", "Testing"];

describe("Code Review Feedback", () => {
  it("shows the five aspects, each with 0 upvotes and 0 downvotes", () => {
    render(<CodeReviewFeedback />);
    ASPECTS.forEach((aspect) => expect(screen.getByText(aspect)).toBeInTheDocument());
    expect(screen.getAllByRole("button", { name: /Upvote/ })).toHaveLength(5);
    expect(screen.getAllByRole("button", { name: /Downvote/ })).toHaveLength(5);
    ASPECTS.forEach((_, i) => {
      expect(screen.getByTestId(`upvote-count-${i}`)).toHaveTextContent("Upvotes: 0");
      expect(screen.getByTestId(`downvote-count-${i}`)).toHaveTextContent("Downvotes: 0");
    });
  });

  it("counts votes per aspect (sample interaction)", () => {
    render(<CodeReviewFeedback />);
    const up = screen.getAllByRole("button", { name: /Upvote/ });
    const down = screen.getAllByRole("button", { name: /Downvote/ });

    fireEvent.click(up[0]);                          // Readability
    fireEvent.click(down[1]);                        // Performance
    fireEvent.click(up[2]); fireEvent.click(up[2]);  // Security x2
    fireEvent.click(up[3]); fireEvent.click(up[3]); fireEvent.click(up[3]); // Documentation x3

    expect(screen.getByTestId("upvote-count-0")).toHaveTextContent("Upvotes: 1");
    expect(screen.getByTestId("downvote-count-1")).toHaveTextContent("Downvotes: 1");
    expect(screen.getByTestId("upvote-count-2")).toHaveTextContent("Upvotes: 2");
    expect(screen.getByTestId("upvote-count-3")).toHaveTextContent("Upvotes: 3");
    expect(screen.getByTestId("upvote-count-4")).toHaveTextContent("Upvotes: 0");
  });
});
