// Contact Form  (Medium · Forms)  https://www.hackerrank.com/challenges/react-contact-form/problem
// Description and explanation: README.md (same folder). Tests: Solution.test.jsx
//
// How it works:
// - One state object holds the three controlled fields; one onChange handler updates any of them by name.
// - On submit: preventDefault() stops the browser from reloading the page.
// - Any empty field (after trimming spaces) -> show the error and show NO submitted data.
// - Otherwise -> save a copy of the values to display, clear the fields and the error.
import { useState } from "react";

const EMPTY = { name: "", email: "", message: "" };

export default function ContactForm() {
  const [form, setForm] = useState(EMPTY);
  const [submitted, setSubmitted] = useState(null);   // the data shown below the form
  const [error, setError] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const isEmpty = Object.values(form).some((v) => v.trim() === "");
    if (isEmpty) {
      setError("All fields are required.");
      setSubmitted(null);
      return;
    }
    setSubmitted(form);
    setForm(EMPTY);
    setError("");
  };

  return (
    <div className="card">
      <form onSubmit={handleSubmit}>
        <label htmlFor="name">Name</label>
        <input id="name" name="name" type="text" value={form.name} onChange={handleChange} data-testid="name-input" />

        <label htmlFor="email">Email</label>
        <input id="email" name="email" type="text" value={form.email} onChange={handleChange} data-testid="email-input" />

        <label htmlFor="message">Message</label>
        <textarea id="message" name="message" value={form.message} onChange={handleChange} data-testid="message-input" />

        <button type="submit" data-testid="submit-button">Submit</button>
      </form>

      {error && <p className="error" data-testid="error-message">{error}</p>}

      {submitted && (
        <div className="result" data-testid="submitted-data">
          <h3>Submitted Information</h3>
          <p><strong>Name:</strong> {submitted.name}</p>
          <p><strong>Email:</strong> {submitted.email}</p>
          <p><strong>Message:</strong> {submitted.message}</p>
        </div>
      )}
    </div>
  );
}
