import { describe, it, expect } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import BlogPost from "./Solution.jsx";

const create = (title, description) => {
  fireEvent.change(screen.getByPlaceholderText("Title"), { target: { value: title } });
  fireEvent.change(screen.getByPlaceholderText("Description"), { target: { value: description } });
  fireEvent.click(screen.getByRole("button", { name: "Create" }));
};

describe("Blog Post", () => {
  it("starts with empty fields and no posts", () => {
    render(<BlogPost />);
    expect(screen.getByPlaceholderText("Title")).toHaveValue("");
    expect(screen.getByPlaceholderText("Description")).toHaveValue("");
    expect(screen.queryAllByTestId("post")).toHaveLength(0);
  });

  it("creates a post and clears the fields", () => {
    render(<BlogPost />);
    create("My first post", "Hello world");
    expect(screen.getByText("My first post")).toBeInTheDocument();
    expect(screen.getByText("Hello world")).toBeInTheDocument();
    expect(screen.getByPlaceholderText("Title")).toHaveValue("");
    expect(screen.getByPlaceholderText("Description")).toHaveValue("");
  });

  it("does not create a post when a field is empty", () => {
    render(<BlogPost />);
    create("Only a title", "");
    expect(screen.queryAllByTestId("post")).toHaveLength(0);
  });

  it("deletes only the chosen post", () => {
    render(<BlogPost />);
    create("Post A", "first");
    create("Post B", "second");
    fireEvent.click(screen.getAllByRole("button", { name: "Delete" })[0]);
    expect(screen.queryByText("Post A")).not.toBeInTheDocument();
    expect(screen.getByText("Post B")).toBeInTheDocument();
  });
});
