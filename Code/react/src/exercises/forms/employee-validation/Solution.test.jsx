import { describe, it, expect } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import EmployeeValidationForm, { MESSAGES } from "./Solution.jsx";

const type = (label, value) => fireEvent.change(screen.getByLabelText(label), { target: { value } });
const fillValid = () => {
  type("Name", "Jane Doe");
  type("Email", "jane@example.com");
  type("Employee ID", "123456");
  type("Joining Date", "2020-05-01");
};

describe("Employee Validation", () => {
  it("shows every error at first and disables Submit", () => {
    render(<EmployeeValidationForm />);
    Object.values(MESSAGES).forEach((m) => expect(screen.getByText(m)).toBeInTheDocument());
    expect(screen.getByRole("button", { name: "Submit" })).toBeDisabled();
  });

  it("removes each error once its field is valid", () => {
    render(<EmployeeValidationForm />);
    type("Name", "Jo");                       // too short
    expect(screen.getByText(MESSAGES.name)).toBeInTheDocument();
    type("Name", "John 2");                   // digits not allowed
    expect(screen.getByText(MESSAGES.name)).toBeInTheDocument();
    type("Name", "John Smith");
    expect(screen.queryByText(MESSAGES.name)).not.toBeInTheDocument();

    type("Employee ID", "12345");
    expect(screen.getByText(MESSAGES.employeeId)).toBeInTheDocument();
    type("Employee ID", "123456");
    expect(screen.queryByText(MESSAGES.employeeId)).not.toBeInTheDocument();
  });

  it("rejects a joining date in the future", () => {
    render(<EmployeeValidationForm />);
    type("Joining Date", "2999-01-01");
    expect(screen.getByText(MESSAGES.joinDate)).toBeInTheDocument();
  });

  it("enables Submit when all fields are valid, and resets the form on submit", () => {
    render(<EmployeeValidationForm />);
    fillValid();
    const submit = screen.getByRole("button", { name: "Submit" });
    expect(submit).toBeEnabled();
    fireEvent.click(submit);
    expect(screen.getByLabelText("Name")).toHaveValue("");
    expect(screen.getByLabelText("Employee ID")).toHaveValue("");
    expect(submit).toBeDisabled();
  });
});
