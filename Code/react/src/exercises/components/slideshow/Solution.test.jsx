import { describe, it, expect } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import Slides from "./Solution.jsx";
import { SLIDES } from "./data.js";

const button = (name) => screen.getByRole("button", { name });

describe("Slideshow", () => {
  it("shows the first slide with Restart and Prev disabled", () => {
    render(<Slides slides={SLIDES} />);
    expect(screen.getByTestId("title")).toHaveTextContent(SLIDES[0].title);
    expect(screen.getByTestId("text")).toHaveTextContent(SLIDES[0].text);
    expect(button("Restart")).toBeDisabled();
    expect(button("Prev")).toBeDisabled();
    expect(button("Next")).toBeEnabled();
  });

  it("moves forward and back", () => {
    render(<Slides slides={SLIDES} />);
    fireEvent.click(button("Next"));
    expect(screen.getByTestId("title")).toHaveTextContent(SLIDES[1].title);
    expect(button("Prev")).toBeEnabled();
    expect(button("Restart")).toBeEnabled();
    fireEvent.click(button("Prev"));
    expect(screen.getByTestId("title")).toHaveTextContent(SLIDES[0].title);
    expect(button("Prev")).toBeDisabled();
  });

  it("disables Next on the last slide, and Restart goes back to the first", () => {
    render(<Slides slides={SLIDES} />);
    for (let i = 1; i < SLIDES.length; i++) fireEvent.click(button("Next"));
    expect(screen.getByTestId("title")).toHaveTextContent("Great job!");
    expect(button("Next")).toBeDisabled();
    fireEvent.click(button("Restart"));
    expect(screen.getByTestId("title")).toHaveTextContent(SLIDES[0].title);
    expect(button("Restart")).toBeDisabled();
  });

  it("works with a single slide", () => {
    render(<Slides slides={[{ title: "Only", text: "one" }]} />);
    expect(button("Next")).toBeDisabled();
    expect(button("Prev")).toBeDisabled();
  });
});
