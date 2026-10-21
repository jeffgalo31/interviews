<!-- study-layout -->
# Patient Medical Records

🟡 **Medium** · 📁 **Interaction** · ⚛️ HackerRank React · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/patient-medical-records/problem)

**On this page:** [📝 Problem](#-problem) · [🧪 Sample interaction](#-sample-interaction) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

In this challenge, you will create a React application called "Patient Medical Records" that allows users to view and cycle through patients' medical records. The application requirements are outlined below, and your finished implementation must pass all provided unit tests.

### Detailed Requirements

1. The application consists of two components: Search and Records.
    - Search: Contains a dropdown select menu and a "Show" button.
    - Records: Displays the selected patient's records in a table and includes a "Next" button to navigate to the next patient's records.
2. The Search component must have a dropdown select menu populated with 3 patient names from a file named medicalRecords.js. By default, the dropdown should display "Select Patient" with both selected and disabled attributes.
3. When the application is first loaded, no record table or "Next" button should be visible.
4. Show Button Functionality:
    - If the user clicks "Show" without selecting a patient, an alert should appear with the message: "Please select a patient name".
    - If a patient is selected, clicking "Show" should display a table containing all of the selected patient’s details and medical records. The table must also include a "Next" button to navigate through records.
5. Next Button Functionality:
    - Clicking "Next" should display the medical records for the next patient in the list based on their ID.
    - If the last patient's records are being displayed, clicking "Next" should loop back to the first patient's records.

## 🧪 Sample interaction

### Initial State

- The select menu displays "Select Patient".
- No records or "Next" button is visible.

### User Action 1

- The user selects a patient from the dropdown menu and clicks "Show"
- The patient's details and records appear in a table along with a "Next" button.

### User Action 2

- The user clicks "Next" to view the next patient's records.
- The table updates with the next patient's details.

### User Action 3

- If the user is on the last patient and clicks "Next", the records cycle back to the first patient

## 💡 Solution

> [!TIP]
> **Key idea:** The parent owns **one** piece of state, the id of the patient being shown (`null` = nothing yet); `Search` and `Records` get props and callbacks.

### ✍️ The component

```jsx
import { useState } from "react";
import medicalRecords from "./medicalRecords.js";

function Search({ patients, onShow }) {
  const [selectedId, setSelectedId] = useState("");

  const handleShow = () => {
    if (!selectedId) {
      window.alert("Please select a patient name");
      return;
    }
    onShow(Number(selectedId));
  };

  return (
    <div className="row">
      <select value={selectedId} onChange={(e) => setSelectedId(e.target.value)} data-testid="patient-name">
        <option value="" disabled>Select Patient</option>
        {patients.map((p) => (
          <option key={p.id} value={p.id}>{p.name}</option>
        ))}
      </select>
      <button onClick={handleShow} data-testid="show">Show</button>
    </div>
  );
}

function Records({ patient, onNext }) {
  return (
    <div data-testid="patient-records">
      <table>
        <tbody>
          <tr><th>Name</th><td data-testid="patient-name-cell">{patient.name}</td></tr>
          <tr><th>Date of birth</th><td>{patient.dob}</td></tr>
          <tr><th>Height</th><td>{patient.height}</td></tr>
          <tr><th>Weight</th><td>{patient.weight}</td></tr>
        </tbody>
      </table>
      <table>
        <thead>
          <tr><th>Date</th><th>Diagnosis</th><th>Prescription</th><th>Doctor</th></tr>
        </thead>
        <tbody>
          {patient.records.map((r) => (
            <tr key={r.date}>
              <td>{r.date}</td><td>{r.diagnosis}</td><td>{r.prescription}</td><td>{r.doctor}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <button onClick={onNext} data-testid="next-btn">Next</button>
    </div>
  );
}

export default function PatientMedicalRecords({ patients = medicalRecords }) {
  const [currentId, setCurrentId] = useState(null);
  const ordered = [...patients].sort((a, b) => a.id - b.id);
  const index = ordered.findIndex((p) => p.id === currentId);

  const showNext = () => {
    const next = ordered[(index + 1) % ordered.length];   // last -> first
    setCurrentId(next.id);
  };

  return (
    <div className="card wide">
      <Search patients={ordered} onShow={setCurrentId} />
      {index !== -1 && <Records patient={ordered[index]} onNext={showNext} />}
    </div>
  );
}
```

### 🔍 How it works

- Placeholder option: `<option value="" disabled>Select Patient</option>` with the select's value starting at `""`, so it is selected and disabled.
- Show with nothing chosen → `alert("Please select a patient name")`; otherwise call `onShow(id)`.
- Next: index of the current patient + 1, wrapped with `% patients.length`, so the last one goes back to the first.
- `medicalRecords.js` here has 3 made-up patients for practice; HackerRank's starter ships its own file with the same shape.
- On HackerRank the starter project already has the markup and the `data-testid` attributes the tests look for: keep them and add the state and handlers shown here.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ⚛️ | [Solution.jsx](Solution.jsx) | The component, commented. See it with `npm run dev` (in `react`) and pick it in the sidebar |
| 🧪 | [Solution.test.jsx](Solution.test.jsx) | Tests built from HackerRank's requirements: `npm test` |
| 🗂️ | [medicalRecords.js](medicalRecords.js) | Data the component uses (same shape as in HackerRank's starter project) |

📋 **On HackerRank:** the starter project already has the markup and `data-testid`s; copy the state and handlers into its component.

---

⬅️ [Employee Validation](../../forms/employee-validation/README.md) · [⚛️ All React exercises](../../../../README.md)
