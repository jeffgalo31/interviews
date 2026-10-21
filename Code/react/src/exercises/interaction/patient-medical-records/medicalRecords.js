// Sample data for local practice. HackerRank's starter project ships its own medicalRecords.js
// (3 patients); its exact contents are only visible in the challenge's editor.
const medicalRecords = [
  {
    id: 1,
    name: "John Oliver",
    dob: "1985-03-12",
    height: "180 cm",
    weight: "78 kg",
    records: [
      { date: "2024-01-10", diagnosis: "Seasonal flu", prescription: "Rest, fluids", doctor: "Dr. Smith" },
      { date: "2024-06-02", diagnosis: "Sprained ankle", prescription: "Ice, compression", doctor: "Dr. Patel" },
    ],
  },
  {
    id: 2,
    name: "Maria Lopez",
    dob: "1990-07-25",
    height: "165 cm",
    weight: "60 kg",
    records: [
      { date: "2023-11-18", diagnosis: "Annual check-up", prescription: "None", doctor: "Dr. Chen" },
    ],
  },
  {
    id: 3,
    name: "Ahmed Khan",
    dob: "1978-12-03",
    height: "175 cm",
    weight: "82 kg",
    records: [
      { date: "2024-02-14", diagnosis: "High blood pressure", prescription: "Daily walk, low salt", doctor: "Dr. Smith" },
      { date: "2024-08-30", diagnosis: "Follow-up", prescription: "Continue plan", doctor: "Dr. Smith" },
    ],
  },
];

export default medicalRecords;
