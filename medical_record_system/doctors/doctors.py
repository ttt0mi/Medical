from typing import List
from medical_record_system.doctors.doctor import Doctor


class Doctors:
    def __init__(self) -> None:
       self.__doctors : List[Doctor] = []
       
    def add_doctor_to_database(self, doctor : Doctor):
        self.__doctors.append(doctor)
        
    def remove_doctor(self, doctor : Doctor):
        self.__doctors.remove(doctor)
    
    def get_doctors(self) -> List[Doctor]:
        return self.__doctors