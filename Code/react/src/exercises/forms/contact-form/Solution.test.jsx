import { describe, it, expect } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import ContactForm from "./Solution.jsx";

const fill = (name, email, message) => {
  fireEvent.change(screen.getByLabelText("Name"), { target: { value: name } });
  fireEvent.change(screen.getByLabelText("Email"), { target: { value: email } });
  fireEvent.change(screen.getByLabelText("Message"), { target: { value: message } });
};

describe("Contact Form", () => {
  it("starts with empty fields, no error and no submitted data", () => {
    render(<ContactForm />);
    expect(screen.getByLabelText("Name")).toHaveValue("");
    expect(screen.queryByText("All fields are required.")).not.toBeInTheDocument();
    expect(screen.queryByTestId("submitted-data")).not.toBeInTheDocument();
  });

  it("shows the submitted data and clears the fields", () => {
    render(<ContactForm />);
    fill("John Doe", "john@example.com", "Hello there!");
    fireEvent.click(screen.getByRole("button", { name: "Submit" }));

    const result = screen.getByTestId("submitted-data");
    expect(result).toHaveTextContent("John Doe");
    expect(result).toHaveTextContent("john@example.com");
    expect(result).toHaveTextContent("Hello there!");
    expect(screen.getByLabelText("Name")).toHaveValue("");
    expect(screen.getByLabelText("Email")).toHaveValue("");
    expect(screen.getByLabelText("Message")).toHaveValue("");
  });

  it("shows an error and no data when a field is empty", () => {
    render(<ContactForm />);
    fill("John Doe", "", "Hello there!");
    fireEvent.click(screen.getByRole("button", { name: "Submit" }));

    expect(screen.getByText("All fields are required.")).toBeInTheDocument();
    expect(screen.queryByTestId("submitted-data")).not.toBeInTheDocument();
  });
});
