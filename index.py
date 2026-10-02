import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
triageSystem = [
    {
        'RN': "Adriana Juárez",
        'BED': 3, 
        'ARR': "09:34",
        'LOS': "",
        'HRI': "",
        'NAME': "Juan Sanchéz",
        'S': "H",
        'AGE': 28, 
        'MRN': 123123123, 
        'COMPLAINT': "Abdominal pain",
        'MD': "",
        'AT': "", 
        'CONSULT': "", 
        'LR': "",
        'RD': "", 
        'DCRN': "",
        'RLAN': ""
    },
    {
        'RN': "Mariano Rivera",
        'BED': 8, 
        'ARR': "10:05",
        'LOS': "",
        'HRI': "",
        'NAME': "María Soriano",
        'S': "M",
        'AGE': 35, 
        'MRN': 321321321, 
        'COMPLAINT': "Chest pain",
        'MD': "",
        'AT': "", 
        'CONSULT': "", 
        'LR': "",
        'RD': "", 
        'DCRN': "",
        'RLAN': ""
    },
    {
        'RN': "Fernando Rivas",
        'BED': 4, 
        'ARR': "10:37",
        'LOS': "",
        'HRI': "",
        'NAME': "Marín Martínez",
        'S': "H",
        'AGE': 25, 
        'MRN': 3434343434, 
        'COMPLAINT': "Stroke",
        'MD': "",
        'AT': "", 
        'CONSULT': "", 
        'LR': "",
        'RD': "", 
        'DCRN': "",
        'RLAN': ""
    },
    {
        'RN': "Adriana Juárez",
        'BED': 7, 
        'ARR': "11:23",
        'LOS': "",
        'HRI': "",
        'NAME': "Fernando Juárez",
        'S': "H",
        'AGE': 30, 
        'MRN': 565656565, 
        'COMPLAINT': "Cold",
        'MD': "",
        'AT': "", 
        'CONSULT': "", 
        'LR': "",
        'RD': "", 
        'DCRN': "",
        'RLAN': ""
    },
     {
            'RN': "Fernando Rivas",
            'BED': 4, 
            'ARR': "10:37",
            'LOS': "",
            'HRI': "",
            'NAME': "Marín Martínez",
            'S': "H",
            'AGE': 25, 
            'MRN': 3434343434, 
            'COMPLAINT': "Stroke",
            'MD': "",
            'AT': "", 
            'CONSULT': "", 
            'LR': "",
            'RD': "", 
            'DCRN': "",
            'RLAN': ""
        },
 {
        'RN': "Fernando Rivas",
        'BED': 4, 
        'ARR': "10:37",
        'LOS': "",
        'HRI': "",
        'NAME': "Marín Martínez",
        'S': "H",
        'AGE': 25, 
        'MRN': 3434343434, 
        'COMPLAINT': "Stroke",
        'MD': "",
        'AT': "", 
        'CONSULT': "", 
        'LR': "",
        'RD': "", 
        'DCRN': "",
        'RLAN': ""
    },
 {
        'RN': "Fernando Rivas",
        'BED': 4, 
        'ARR': "10:37",
        'LOS': "",
        'HRI': "",
        'NAME': "Marín Martínez",
        'S': "H",
        'AGE': 25, 
        'MRN': 3434343434, 
        'COMPLAINT': "Stroke",
        'MD': "",
        'AT': "", 
        'CONSULT': "", 
        'LR': "",
        'RD': "", 
        'DCRN': "",
        'RLAN': ""
    },
 {
        'RN': "Fernando Rivas",
        'BED': 4, 
        'ARR': "10:37",
        'LOS': "",
        'HRI': "",
        'NAME': "Marín Martínez",
        'S': "H",
        'AGE': 25, 
        'MRN': 3434343434, 
        'COMPLAINT': "Stroke",
        'MD': "",
        'AT': "", 
        'CONSULT': "", 
        'LR': "",
        'RD': "", 
        'DCRN': "",
        'RLAN': ""
    },
 {
        'RN': "Fernando Rivas",
        'BED': 4, 
        'ARR': "10:37",
        'LOS': "",
        'HRI': "",
        'NAME': "Marín Martínez",
        'S': "H",
        'AGE': 25, 
        'MRN': 3434343434, 
        'COMPLAINT': "Stroke",
        'MD': "",
        'AT': "", 
        'CONSULT': "", 
        'LR': "",
        'RD': "", 
        'DCRN': "",
        'RLAN': ""
    },
 {
        'RN': "Fernando Rivas",
        'BED': 4, 
        'ARR': "10:37",
        'LOS': "",
        'HRI': "",
        'NAME': "Marín Martínez",
        'S': "H",
        'AGE': 25, 
        'MRN': 3434343434, 
        'COMPLAINT': "Stroke",
        'MD': "",
        'AT': "", 
        'CONSULT': "", 
        'LR': "",
        'RD': "", 
        'DCRN': "",
        'RLAN': ""
    },
 {
        'RN': "Fernando Rivas",
        'BED': 4, 
        'ARR': "10:37",
        'LOS': "",
        'HRI': "",
        'NAME': "Marín Martínez",
        'S': "H",
        'AGE': 25, 
        'MRN': 3434343434, 
        'COMPLAINT': "Stroke",
        'MD': "",
        'AT': "", 
        'CONSULT': "", 
        'LR': "",
        'RD': "", 
        'DCRN': "",
        'RLAN': ""
    },
 {
        'RN': "Fernando Rivas",
        'BED': 4, 
        'ARR': "10:37",
        'LOS': "",
        'HRI': "",
        'NAME': "Marín Martínez",
        'S': "H",
        'AGE': 25, 
        'MRN': 3434343434, 
        'COMPLAINT': "Stroke",
        'MD': "",
        'AT': "", 
        'CONSULT': "", 
        'LR': "",
        'RD': "", 
        'DCRN': "",
        'RLAN': ""
    },
 {
        'RN': "Fernando Rivas",
        'BED': 4, 
        'ARR': "10:37",
        'LOS': "",
        'HRI': "",
        'NAME': "Marín Martínez",
        'S': "H",
        'AGE': 25, 
        'MRN': 3434343434, 
        'COMPLAINT': "Stroke",
        'MD': "",
        'AT': "", 
        'CONSULT': "", 
        'LR': "",
        'RD': "", 
        'DCRN': "",
        'RLAN': ""
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

st.title("EMERGENCY ROOM CONTROL BOARD", )
st.dataframe(triageSystem)

col1, col2 = st.columns(2, gap="small")
with col1: 
    st.button("Add a patient record")
with col2:
    st.button("Edit a patient record")


"""
#patient[''] = input("")
for column in patient: 
    if(column != None):
        print(patient[column])

def seeAllPatientsInfo():
    st.dataframe(triageSystem)
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
                    print("Write the name of the data you want to add/change:
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
                    ")
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
    print("What do you want to do?")
    print("Write one option: 
       1. See all patients information. 
       2. Add a patient record.
       3. Edit a patient's record. 
       4. Exit. 
    ")
    chosenOption = int(input("Write a number: "))
    goOn = switch(chosenOption)
    if (goOn == False): 
        print('You exited the program.')
        break
"""
