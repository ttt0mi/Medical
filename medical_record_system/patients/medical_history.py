from medical_record_system.appointments_package.appointment import Appointment
from medical_record_system.appointments_package.appointments import Appointments

class MedicalHistory:
    def __init__(self):
        self.__appointments = Appointments()

    def get_upcoming_appointments(self):
        upcoming_appointments = []
        for ap in self.__appointments.get_appointments():
            if ap.is_upcoming():
                upcoming_appointments.append(ap)
        return upcoming_appointments

    def get_medical_history(self):
        return self.__appointments
    
    def add_confirmed_appointment(self, appointment: Appointment):
        self.__appointments.add_appointment(appointment)



