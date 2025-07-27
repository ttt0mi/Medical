from medical_record_system.appointments_package.appointment import Appointment
from medical_history import MedicalHistory
from medical_record_system.personal import Personal


class Patient(Personal):

    def __init__(self, first_name: str, last_name: str, date_of_birth: str):
        super().__init__(name = first_name + " " + last_name, date_of_birth = date_of_birth)
        self.__id = None
        self.__medical_history = MedicalHistory()

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def book_appointment(self, reason) -> Appointment:
        pending_appointment = Appointment(reason)
        pending_appointment.patient_name = self.name
        return pending_appointment

    def add_appointment(self, appointment: Appointment) -> None:
        self.__medical_history.add_confirmed_appointment(appointment)

    @property
    def view_medical_history(self)-> MedicalHistory:
        return self.__medical_history.get_medical_history()

    def __str__(self):
        return f"""
Patient ID: {self.__id}
Name: {self.name}
Date of Birth: {self.date_of_birth}
Contact Email: {self.emails}
Contact Number: {self.numbers}"""