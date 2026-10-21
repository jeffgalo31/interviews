import { describe, it, expect } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import ItemListManager from "./Solution.jsx";

describe("Item List Manager", () => {
  it("starts with an empty list and an empty input", () => {
    render(<ItemListManager />);
    expect(screen.queryAllByRole("listitem")).toHaveLength(0);
    expect(screen.getByPlaceholderText("Enter item")).toHaveValue("");
  });

  it("adds items in order and clears the input", () => {
    render(<ItemListManager />);
    const input = screen.getByPlaceholderText("Enter item");
    const button = screen.getByRole("button", { name: "Add Item" });

    fireEvent.change(input, { target: { value: "First Item" } });
    fireEvent.click(button);
    expect(input).toHaveValue("");

    fireEvent.change(input, { target: { value: "Second Item" } });
    fireEvent.click(button);

    const items = screen.getAllByRole("listitem");
    expect(items).toHaveLength(2);
    expect(items[0]).toHaveTextContent("First Item");
    expect(items[1]).toHaveTextContent("Second Item");
  });

  it("does not add anything when the input is empty", () => {
    render(<ItemListManager />);
    fireEvent.click(screen.getByRole("button", { name: "Add Item" }));
    expect(screen.queryAllByRole("listitem")).toHaveLength(0);
  });
});
