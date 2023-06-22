#create a function in PyCharm that counts the number of patience in a hospital that are currently checked in, 
# and then prints out in the console area their name, patient number, room number:

def count_num_patients(patient_data):
    count = 0
    for patient in patient_data:
        if patient[3] == "Yes":
            count += 1
            print("Patient Name: "+patient[0]+"\n"+"Patient Number: "+patient[1]+"\n"+"Room Number: "+patient[2]+"\n")
    return count




patient_data = [
    ["Eric","50215","511","Yes"],
    ["Ryan","50123","521","No"],
    ["Karen","50168","520","Yes"],
    ["Matthew","50898","410","No"],
    ["Kim","50999","120","No"],
    ["Toby","50741","123","No"],
    ["Johanna","50233","330","Yes"],
]

checked_in_patients = count_num_patients(patient_data)
print("Total patients checked in: ",checked_in_patients)