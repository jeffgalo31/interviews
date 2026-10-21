// Employee Validation  (Medium · Forms)  https://www.hackerrank.com/challenges/employee-validation/problem
// Description and explanation: README.md (same folder). Tests: Solution.test.jsx
//
// How it works:
// - One state object holds the four field values.
// - The errors are NOT stored in state: they are DERIVED from the values on every render
//   (validate(form)). That keeps them always in sync — no useEffect needed.
// - An error message is rendered under each field whose rule fails (also on first render, as required).
// - Submit is disabled while any error exists; on submit the form is reset to empty values.
import { useState } from "react";

const EMPTY = { name: "", email: "", employeeId: "", joinDate: "" };

export const MESSAGES = {
  name: "Name must be at least 4 characters long and only contain letters and spaces.",
  email: "Email must be a valid email address.",
  employeeId: "Employee ID must be exactly 6 digits.",
  joinDate: "Joining Date cannot be in the future.",
};

const today = () => new Date().toISOString().slice(0, 10);   // "YYYY-MM-DD" compares correctly as text

export function validate(form) {
  const errors = {};
  if (!/^[A-Za-z ]{4,}$/.test(form.name)) errors.name = MESSAGES.name;
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email)) errors.email = MESSAGES.email;
  if (!/^\d{6}$/.test(form.employeeId)) errors.employeeId = MESSAGES.employeeId;
  if (!form.joinDate || form.joinDate > today()) errors.joinDate = MESSAGES.joinDate;
  return errors;
}

export default function EmployeeValidationForm() {
  const [form, setForm] = useState(EMPTY);
  const errors = validate(form);
  const isValid = Object.keys(errors).length === 0;

  const update = (field) => (e) => setForm({ ...form, [field]: e.target.value });

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!isValid) return;
    setForm(EMPTY);   // reset after a successful submit
  };

  const field = (key, label, type, testid) => (
    <div className="field">
      <label htmlFor={key}>{label}</label>
      <input id={key} type={type} value={form[key]} onChange={update(key)} data-testid={testid} />
      {errors[key] && <p className="error">{errors[key]}</p>}
    </div>
  );

  return (
    <form className="card" onSubmit={handleSubmit}>
      {field("name", "Name", "text", "input-name-test")}
      {field("email", "Email", "text", "input-email-test")}
      {field("employeeId", "Employee ID", "text", "input-employee-id-test")}
      {field("joinDate", "Joining Date", "date", "input-joining-date-test")}
      <button type="submit" disabled={!isValid} data-testid="submit-btn">Submit</button>
    </form>
  );
}
