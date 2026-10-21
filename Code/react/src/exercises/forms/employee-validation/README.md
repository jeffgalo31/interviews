<!-- study-layout -->
# Employee Validation

🟡 **Medium** · 📁 **Forms** · ⚛️ HackerRank React · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/employee-validation/problem)

**On this page:** [📝 Problem](#-problem) · [🧪 Sample interaction](#-sample-interaction) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Your task is to create a React app that helps employees validate and update their existing information through a survey form. The application requirements are detailed below, and the finished application must pass all of the unit tests.

> [!NOTE]
> 🎞️ **Preview (an animated GIF on HackerRank), in words:** A form with **Name, Email, Employee ID** and **Joining Date** (a date picker). Every empty field shows its red error message underneath, and the **Submit** button is faded (disabled). As each field becomes valid its message disappears; when all four are valid Submit turns active, and clicking it empties the form again.

### Detailed Requirements

1. The EmployeeValidationForm component collects employee details through four input fields: Name, Email, Employee ID, and Joining Date.
2. Each input field should have validation logic to ensure that the data entered meets the specified requirements.
3. A Submit button should be present at the bottom of the form but remain disabled until all fields are valid.
4. If a field does not meet the criteria, an error message should be displayed below that field.
5. When the form is valid and submitted, all input fields should be cleared, and the form should be reset to its initial state.

### Validation Criteria

- Name Field: Must be at least 4 characters long and can only contain alphabetical characters (A-Z, a-z) and spaces.
- Email Field: Must be in a valid email format (e.g., user@example.com).
- Employee ID Field: Must be exactly 6 numeric digits.
- Joining Date Field: Cannot be set to a date in the future.

### Error Messages

- Name: "Name must be at least 4 characters long and only contain letters and spaces."
- Email: "Email must be a valid email address."
- Employee ID: "Employee ID must be exactly 6 digits."
- Joining Date: "Joining Date cannot be in the future."

### Form Submission Requirements

- Form State Reset: Upon successful form submission, all fields should be cleared, and the form should revert to its initial state.
- Submit Button: Should only be enabled when all input fields are valid.

## 🧪 Sample interaction

### Initial State

1. All input fields are empty.
2. The Submit button is disabled.
3. Error messages are displayed below each empty input field.

### User Action 1

1. The user types "John" into the Name field.
2. The error message below the Name field disappears if it meets the criteria.
3. The Submit button remains disabled as not all fields are valid.

### User Action 2

1. The user types "john.doe@example.com" into the Email field.
2. The error message below the Email field disappears if it meets the criteria.

### User Action 3

1. The user enters "123456" in the Employee ID field and selects a Joining Date that is not in the future.
2. All input fields are now valid, and the Submit button becomes enabled.

### User Action 3

1. The user clicks the Submit button.
2. All input fields are cleared, the Submit button is disabled, and the form resets to its initial state.

## 💡 Solution

> [!TIP]
> **Key idea:** Don't store errors in state: **derive** them from the values on every render with a `validate(form)` function, so they're always in sync.

### ✍️ The component

```jsx
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
```

### 🔍 How it works

- Rules: name `/^[A-Za-z ]{4,}$/`, email `/^[^\s@]+@[^\s@]+\.[^\s@]+$/`, ID `/^\d{6}$/`, date not empty and not after today (`YYYY-MM-DD` strings compare correctly as text).
- Each field renders its message only when it has an error, which means all four show at first, as the statement requires.
- Submit is `disabled={!isValid}`; on submit, `preventDefault()` and reset the form to the empty values.
- On HackerRank the starter project already has the markup and the `data-testid` attributes the tests look for: keep them and add the state and handlers shown here.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ⚛️ | [Solution.jsx](Solution.jsx) | The component, commented. See it with `npm run dev` (in `react`) and pick it in the sidebar |
| 🧪 | [Solution.test.jsx](Solution.test.jsx) | Tests built from HackerRank's requirements: `npm test` |

📋 **On HackerRank:** the starter project already has the markup and `data-testid`s; copy the state and handlers into its component.

---

⬅️ [Contact Form](../contact-form/README.md) · [⚛️ All React exercises](../../../../README.md) · [Patient Medical Records](../../interaction/patient-medical-records/README.md) ➡️
