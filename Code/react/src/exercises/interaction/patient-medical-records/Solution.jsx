// Patient Medical Records  (Medium · Interaction)  https://www.hackerrank.com/challenges/patient-medical-records/problem
// Description and explanation: README.md (same folder). Tests: Solution.test.jsx
//
// How it works:
// - The parent (PatientMedicalRecords) owns ONE piece of state: the id of the patient being shown
//   (null = nothing shown yet). Search and Records are children that receive props/callbacks.
// - Search keeps the dropdown's current value; "Show" either alerts (nothing chosen) or calls onShow(id).
// - The placeholder <option> is `disabled` and the select's value starts as "", so "Select Patient"
//   is selected and can't be picked again.
// - Next: move to the following patient by id order; after the last one, wrap around with % (modulo).
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
