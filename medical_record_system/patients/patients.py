from typing import List

from patient import Patient


class PatientsRecord:
    def __init__(self):
        self.__patients : List[Patient] = []
        
    def add_patient_to_database(self, patient : Patient):
        self.__patients.append(patient)
        
    def get_patients(self):
        return self.__patients