from datetime import datetime
from typing import List
from appointment import Appointment
from status import Status

class Appointments:
    def __init__(self):
        self.__appointments : List[Appointment] = []

    def add_appointment(self, appointment: Appointment):
        appointment.status = Status.CONFIRMED
        self.__appointments.append(appointment)
    
    def date_is_occupied(self, date : datetime) -> bool:
        for appointment in self.__appointments:
            if appointment.date == date:
                return True
        return False
    
    def get_appointments(self) -> List[Appointment]:
        return self.__appointments

    



