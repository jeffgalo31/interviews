import { describe, it, expect } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import WordOmitter from "./Solution.jsx";

const type = (value) => fireEvent.change(screen.getByPlaceholderText("Type here..."), { target: { value } });

describe("Word Omitter", () => {
  it("starts empty in omit mode", () => {
    render(<WordOmitter />);
    expect(screen.getByTestId("output-text")).toHaveTextContent("");
    expect(screen.getByTestId("action-btn")).toHaveTextContent("Show All Words");
  });

  it("HackerRank sample: omits 'a' and keeps punctuation", () => {
    render(<WordOmitter />);
    type("This is a test sentence.");
    expect(screen.getByTestId("output-text")).toHaveTextContent("This is test sentence.");
    fireEvent.click(screen.getByTestId("action-btn"));
    expect(screen.getByTestId("output-text")).toHaveTextContent("This is a test sentence.");
  });

  it("omits the listed words (any case)", () => {
    render(<WordOmitter />);
    type("The cat and a dog OR the bird but not fish");
    expect(screen.getByTestId("output-text")).toHaveTextContent("cat dog bird not fish");
  });

  it("toggles between all words and omitted words", () => {
    render(<WordOmitter />);
    type("a quick test");
    fireEvent.click(screen.getByRole("button", { name: "Show All Words" }));
    expect(screen.getByTestId("output-text")).toHaveTextContent("a quick test");
    expect(screen.getByTestId("action-btn")).toHaveTextContent("Omit Words");
    fireEvent.click(screen.getByRole("button", { name: "Omit Words" }));
    expect(screen.getByTestId("output-text")).toHaveTextContent("quick test");
  });

  it("Clear empties the input and the output", () => {
    render(<WordOmitter />);
    type("hello world");
    fireEvent.click(screen.getByRole("button", { name: "Clear" }));
    expect(screen.getByPlaceholderText("Type here...")).toHaveValue("");
    expect(screen.getByTestId("output-text")).toHaveTextContent("");
  });

  it("accepts a custom omitWords list", () => {
    render(<WordOmitter omitWords={["hello"]} />);
    type("hello big world");
    expect(screen.getByTestId("output-text")).toHaveTextContent("big world");
  });
});
