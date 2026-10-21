import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import PatientMedicalRecords from "./Solution.jsx";
import medicalRecords from "./medicalRecords.js";

describe("Patient Medical Records", () => {
  it("starts with 'Select Patient' selected and disabled, and no records", () => {
    render(<PatientMedicalRecords />);
    const placeholder = screen.getByRole("option", { name: "Select Patient" });
    expect(placeholder.selected).toBe(true);
    expect(placeholder).toBeDisabled();
    expect(screen.getAllByRole("option")).toHaveLength(medicalRecords.length + 1);
    expect(screen.queryByRole("button", { name: "Next" })).not.toBeInTheDocument();
  });

  it("alerts when Show is clicked without choosing a patient", () => {
    const alert = vi.spyOn(window, "alert").mockImplementation(() => {});
    render(<PatientMedicalRecords />);
    fireEvent.click(screen.getByRole("button", { name: "Show" }));
    expect(alert).toHaveBeenCalledWith("Please select a patient name");
    expect(screen.queryByTestId("patient-records")).not.toBeInTheDocument();
    alert.mockRestore();
  });

  it("shows the chosen patient, then cycles with Next (last -> first)", () => {
    render(<PatientMedicalRecords />);
    fireEvent.change(screen.getByRole("combobox"), { target: { value: "2" } });
    fireEvent.click(screen.getByRole("button", { name: "Show" }));
    expect(screen.getByTestId("patient-name-cell")).toHaveTextContent("Maria Lopez");

    fireEvent.click(screen.getByRole("button", { name: "Next" }));
    expect(screen.getByTestId("patient-name-cell")).toHaveTextContent("Ahmed Khan");

    fireEvent.click(screen.getByRole("button", { name: "Next" }));
    expect(screen.getByTestId("patient-name-cell")).toHaveTextContent("John Oliver");
  });
});
