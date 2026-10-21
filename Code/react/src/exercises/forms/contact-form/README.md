<!-- study-layout -->
# Contact Form

🟡 **Medium** · 📁 **Forms** · ⚛️ HackerRank React · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/react-contact-form/problem)

**On this page:** [📝 Problem](#-problem) · [🧪 Sample interaction](#-sample-interaction) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

You need to create a simple React application called "Contact Form" that collects user information and displays it below the form upon submission. This task will help you practice handling form inputs, validation, and conditional rendering in React.

### Detailed Requirements

### 1. Form Structure

   - The form should have the following fields:
     - **Name:** Text input for the user's name.
     - **Email:** Text input for the user's email address.
     - **Message:** Textarea for the user's message.

### 2. Form Submission

   - There should be a "Submit" button to submit the form.

### 3. Form Validation

   - Validate that none of the fields are empty upon submission.
   - If any field is empty, display an error message: "All fields are required." The form should not be submitted.

### 4. Displaying Submitted Data

   - If the form is successfully submitted, display the entered information below the form.
   - Clear the input fields after a successful submission.

## 🧪 Sample interaction

### Initial State

- The form is displayed with empty fields.
- No submitted information or error messages are shown.

### User Action 1

- User fills in all fields (Name: "John Doe", Email: "john@example.com", Message: "Hello there!").
- User clicks the "Submit" button.
- The entered information ("John Doe", "john@example.com", "Hello there!") is displayed below the form.
- The input fields are cleared.

### User Action 2

- User fills in some fields and leaves others empty.
- User clicks the "Submit" button.
- No information is displayed.
- An error message "All fields are required." is shown.

## 💡 Solution

> [!TIP]
> **Key idea:** One state object for the three fields, plus `error` and `submitted`; on submit, `preventDefault()` and validate.

### ✍️ The component

```jsx
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
```

### 🔍 How it works

- Empty check: any field whose `trim()` is `""` → show "All fields are required." and show no data.
- Valid → save a copy in `submitted`, clear the fields and the error. The data block renders only when `submitted` is set (conditional rendering with `&&`).
- `<label htmlFor="name">` + `<input id="name">` links each label to its input (also what `getByLabelText` uses in the tests).
- On HackerRank the starter project already has the markup and the `data-testid` attributes the tests look for: keep them and add the state and handlers shown here.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ⚛️ | [Solution.jsx](Solution.jsx) | The component, commented. See it with `npm run dev` (in `react`) and pick it in the sidebar |
| 🧪 | [Solution.test.jsx](Solution.test.jsx) | Tests built from HackerRank's requirements: `npm test` |

📋 **On HackerRank:** the starter project already has the markup and `data-testid`s; copy the state and handlers into its component.

---

⬅️ [CryptoRank Exchange](../../data-handling/cryptorank-exchange/README.md) · [⚛️ All React exercises](../../../../README.md) · [Employee Validation](../employee-validation/README.md) ➡️
