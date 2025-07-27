from datetime import datetime, timedelta
import random

from medical_record_system.appointments_package.appointment import Appointment
from medical_record_system.appointments_package.appointments import Appointments
from medical_record_system.patients.patient import Patient
from medical_record_system.personal import Personal
from medical_record_system.appointments_package.status import Status

class Doctor(Personal):

	def __init__(self, first_name: str, last_name: str, date_of_birth: str):
		super().__init__(name = first_name + " " + last_name, date_of_birth = date_of_birth)
		self.__appointments = Appointments()
		self.__id = None

	@property
	def id(self): return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	def __is_not_free_for(self, date):
		occupied = self.__appointments.date_is_occupied(date)
		return occupied

	def give_patient_a_date(self, appointment : Appointment, patient : Patient)-> Appointment: #doctor is the one to assign a potential appointment date
		generated_date = Doctor.date_generator()
		patient_upcoming_appointment_dates = []

		for upcoming_appointment in patient.view_medical_history.get_upcoming_appointments(): #doctor has access to patient files
			patient_upcoming_appointment_dates.append(upcoming_appointment.date)

		if self.__is_not_free_for(generated_date) and generated_date in patient_upcoming_appointment_dates:
			self.give_patient_a_date(appointment, patient)

		appointment.date = generated_date
		return appointment

	@staticmethod
	def date_generator()-> datetime:
		today = datetime.now()
		# Only generate if today is still in 2025
		start_date = today + timedelta(days=1)
		end_date = datetime(2025, 12, 31, 23, 59, 59)
		# Total seconds range
		delta_seconds = int((end_date - start_date).total_seconds())
		# Pick a random second in that range
		random_offset = random.randint(0, delta_seconds)
		return start_date + timedelta(seconds=random_offset)

	def add_appointment(self, appointment: Appointment):
		appointment.status = Status.CONFIRMED
		self.__appointments.add_appointment(appointment)

	def get_appointments(self):
		return self.__appointments

	#view patient medical history
	def __str__(self):
		return f"""
Medical ID: {self.__id}
Name: {self.name}
Date of Birth: {self.date_of_birth}
Contact Email: {self.emails}
Contact Number: {self.numbers}"""


