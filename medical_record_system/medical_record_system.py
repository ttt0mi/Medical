from medical_record_system.appointments_package.appointment import Appointment
from medical_record_system.doctors.doctors import Doctors
from medical_record_system.patients.patients import PatientsRecord
import random

from medical_record_system.doctors.doctor import Patient, Doctor
from utilities.contact import Contact


class MedicalRecordSystem:
    __id_count_for_patient = 0
    __id_count_for_doctor = 0

    def __init__(self):
        self.__patients = PatientsRecord()
        self.__doctors = Doctors()

    def schedule_appointment_for(self, patient_id, reason: str):
        patient : Patient = self.__search_patient_using(patient_id)
        appointment: Appointment = patient.book_appointment(reason)
        doctor: Doctor = random.choice(self.__doctors.get_doctors())
        appointment = doctor.give_patient_a_date(appointment, patient)
        patient.add_appointment(appointment)
        doctor.add_appointment(appointment)

    def __search_doctor_using(self, doctor_id):
        found_doctor = None
        for doctor in self.__doctors.get_doctors():
            if doctor.id == doctor_id:
                found_doctor = doctor
        MedicalRecordSystem.raise_exception_if_doctor_is_not_registered(found_doctor)
        return found_doctor

    def __search_patient_using(self, patient_id):
        found_patient = None
        for patient in self.__patients.get_patients():
            if patient.id == patient_id:
                found_patient = patient
        MedicalRecordSystem.raise_exception_if(found_patient)
        return found_patient

    @staticmethod
    def raise_exception_if(patient_is_not_registered: bool | None):
        if patient_is_not_registered:
            raise Exception("Patient is not registered")

    @staticmethod
    def raise_exception_if_doctor_is_not_registered(doctor_is_not_registered: bool | None):
        if doctor_is_not_registered:
            raise Exception("Doctor is not registered")

    def register_patient(self, first_name: str, last_name: str, contact: Contact, date_of_birth: str):
        patient = Patient(first_name, last_name, date_of_birth)
        MedicalRecordSystem.__id_count_for_patient += 1
        patient.id = f"PTT-{str(MedicalRecordSystem.__id_count_for_patient):>03}"
        self.__patients.add_patient_to_database(patient)

    def register_doctor(self, first_name: str, last_name: str, contact: Contact, date_of_birth: str):
        doctor = Doctor(first_name, last_name, date_of_birth)
        MedicalRecordSystem.__id_count_for_doctor += 1
        doctor.id = f"DTR-{str(MedicalRecordSystem.__id_count_for_doctor):>03}"
        self.__doctors.add_doctor_to_database(doctor)

    def remove_doctor_from_database(self, doctor: Doctor): #doctor leaves organization
        self.__doctors.remove_doctor(doctor)

    def view_appointment_schedule_for_doctor(self, doctor_id):
        doctor = self.__search_doctor_using(doctor_id)
        return doctor.get_appointments()

    def view_medical_history_for(self, patient_id):
        patient = self.__search_patient_using(patient_id)
        return patient.view_medical_history()

"""
 @staticmethod
   def __validate_name(name: str):
       if not name: raise ValueError("Name cannot be empty")
       if re.fullmatch(r"^([a-z]+)([-']?)([a-z]+)$", name.strip(), re.I) is None: raise ValueError("Invalid name")


   @staticmethod
   def __validate_dob(date_of_birth: str):
       try:
           dob = datetime.strptime(date_of_birth, "%d/%m/%Y")
       except ValueError:
           raise ValueError("Invalid, date of birth should be in format DD/MM/YYYY. eg. 31/01/2025")
       if dob > datetime.now(): raise ValueError("Invalid date of birth")
       
"""
