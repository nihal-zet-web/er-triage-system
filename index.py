triageSystem = [
    {
        'Bedside nurse': "Adriana Juárez",
        'Bed': 3, 
        'Arrival time': "09:34",
        'Length stay': "",
        'Health risk indicators': "",
        'Patient name': "Juan Sanchéz",
        'Gender': "H",
        'Age': 28, 
        'Medical record number': 123123123, 
        'Chief complaint': "Abdominal pain",
        'Resident name': "",
        'Attending name': "", 
        'Consultation': "", 
        'Laboratory notification': "",
        'Radiology notification': "", 
        'Discharge': "",
        'Comments': ""
    },
    {
        'Bedside nurse': "Mariano Rivera",
        'Bed': 8, 
        'Arrival time': "10:05",
        'Length stay': "",
        'Health risk indicators': "",
        'Patient name': "María Soriano",
        'Gender': "M",
        'Age': 35, 
        'Medical record number': 321321321, 
        'Chief complaint': "Chest pain",
        'Resident name': "",
        'Attending name': "", 
        'Consultation': "", 
        'Laboratory notification': "",
        'Radiology notification': "", 
        'Discharge': "",
        'Comments': ""
    },
    {
        'Bedside nurse': "Fernando Rivas",
        'Bed': 4, 
        'Arrival time': "10:37",
        'Length stay': "",
        'Health risk indicators': "",
        'Patient name': "Marín Martínez",
        'Gender': "H",
        'Age': 25, 
        'Medical record number': 3434343434, 
        'Chief complaint': "Stroke",
        'Resident name': "",
        'Attending name': "", 
        'Consultation': "", 
        'Laboratory notification': "",
        'Radiology notification': "", 
        'Discharge': "",
        'Comments': ""
    },
    {
        'Bedside nurse': "Adriana Juárez",
        'Bed': 7, 
        'Arrival time': "11:23",
        'Length stay': "",
        'Health risk indicators': "",
        'Patient name': "Fernando Juárez",
        'Gender': "H",
        'Age': 30, 
        'Medical record number': 565656565, 
        'Chief complaint': "Cold",
        'Resident name': "",
        'Attending name': "", 
        'Consultation': "", 
        'Laboratory notification': "",
        'Radiology notification': "", 
        'Discharge': "",
        'Comments': ""
    }
]

patient = {
    'Bedside nurse': "",
    'Bed': 0, 
    'Arrival time': "",
    'Length stay': "",
    'Health risk indicators': "",
    'Patient name': "",
    'Gender': "",
    'Age': 0, 
    'Medical record number': 0, 
    'Chief complaint': "",
    'Resident name': "",
    'Attending name': "", 
    'Consultation': "", 
    'Laboratory notification': "",
    'Radiology notification': "", 
    'Discharge': "",
    'Comments': ""
} 


#patient[''] = input("")
for column in patient: 
    if(column != None):
        print(patient[column])

def seeAllPatientsInfo():
    for patient in triageSystem: 
        for column in patient: 
            if (patient[column] != ""): 
                print(patient[column])


def editPatientRecord():
    def editRecord(patientFullname):
        global triageSystem
        for patientRecord in triageSystem: 
            if (patientRecord['Patient name'] == patientFullname): 
                print(patientRecord)
                def switch(chosenOption):
                    if (chosenOption == "Exit"):
                        return False
                    else: 
                        for column in patientRecord: 
                            print(column)
                            if (column == chosenOption): 
                                patientRecord[column] = input("Write the new value: ")
                                print("SUCCESS")
                                return True
                        else: 
                            print("There's no such value in our system.")

                    
                while(True): 
                    print("Which data do you want to edit?")
                    print("""Write the name of the data you want to add/change:
                        1. Bedside nurse
                        2. Bed
                        3. Arrival time
                        4. Length stay
                        5. Health risk indicators
                        6. Patient name
                        7. Gender
                        8. Age
                        9. Medical Record Number
                        10. Chief complaint
                        11. Resident name
                        12. Attending name
                        13. Consultation 
                        14. Laboratory notification
                        15. Radiology notification
                        16. Discharge
                        17. Comments
                        18. Exit
                    """)
                    chosenOption = input()
                    goOn = switch(chosenOption)
                    if(goOn == False):
                        print("Thank you for providing the correct data.")
                        return False
        else: 
            print("It seems like we don't have that name in our system. Review any ortographic errors and try again.")
    
    
    while(True): 
        print("Which patient's record do you want to edit?")
        patientFullname = input("Write the full name of the patient: ")
        editRecord(patientFullname)
        return True


def addPatientRecord():
    global patient
    global triageSystem
    print("Please write the details available about the patient:")
    patient['Bedside nurse'] = input("Bedside nurse: ")
    patient['Bed'] = input("Bed: ")
    patient['Arrival time'] = input("Arrival time: ")
    patient['Length stay'] = input("Length stay: ")
    patient['Health risk indicators'] = input("Health risk indicators: ")
    patient['Patient name'] = input("Patient name: ")
    patient['Gender'] = input("Gender: ")
    patient['Age'] = input("Age: ")
    patient['Medical record number'] = input("Medical record number: ")
    patient['Chief complaint'] = input("Chief complaint: ")
    patient['Resident name'] = input("Resident name: ")
    patient['Attending name'] = input("Attending name: ")
    patient['Consultation'] = input("Consultation: ")
    patient['Laboratory notification'] = input("Laboratory notification: ")
    patient['Radiology notification'] = input("Radiology notification: ")
    patient['Discharge'] = input("Discharge: ")
    patient['Comments'] = input("Comments: ")
    triageSystem.append(patient)
    print(triageSystem)
    return True



def exit():
    return False

def switch(chosenOption):
    if (chosenOption == 1): 
        return seeAllPatientsInfo()
    elif (chosenOption == 2):
        return addPatientRecord()
    elif (chosenOption == 3):
        return editPatientRecord()
    elif (chosenOption == 4):
        return exit()
    else: 
        print('Chose an option available.')

while(True):
    print("What do you want to do?:")
    print("""Write one option: 
       1. See all patients information. 
       2. Add a patient record.
       3. Edit a patient's record. 
       4. Exit. 
    """)
    chosenOption = int(input("Write a number: "))
    goOn = switch(chosenOption)
    if (goOn == False): 
        print('You exited the program.')
        break

