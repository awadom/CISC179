# Function to print out patient info for those that are checked in
def count_checked_in_patients(patient_data):
    checked_in_count = 0

    for patient in patient_data:
        name = patient[0]
        patient_number = patient[1]
        room_number = patient[2]
        checked_in = patient[3]

        if checked_in == "Yes":
            checked_in_count += 1
            print("Patient Name:", name)
            print("Patient Number:", patient_number)
            print("Room Number:", room_number)
            print()

    return checked_in_count


# Patient data from the table provided in the assignment
patient_data = [
    ["Eric", 50215, 511, "Yes"],
    ["Ryan", 50123, 521, "No"],
    ["Karen", 50168, 520, "Yes"],
    ["Matthew", 50898, 410, "No"],
    ["Kim", 50999, 120, "No"],
    ["Toby", 50741, 123, "No"],
    ["Johanna", 50233, 330, "Yes"],
]

# Run the function and get the total patients
checked_in_patients = count_checked_in_patients(patient_data)
print("Total Checked-In Patients:", checked_in_patients)
