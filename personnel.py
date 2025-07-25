from personal import Personal
from utilities.medical_history import MedicalHistory

class Doctor(Personal):
	count = 0
	def __init__(self, first_name: str, last_name: str, date_of_birth: str, specialisation: str):
		super().__init__(first_name, last_name, date_of_birth)
		self.specialisation = specialisation

	@classmethod
	def __assign_id(cls):
		cls.count += 1
		return f"DTR-{str(cls.count):>03}"

	@property
	def get_id(self): return self.__assign_id()

	@property
	def specialisation(self): return self.__specialisation

	@specialisation.setter
	def specialisation(self, specialisation):
		self.__specialisation = specialisation

	@staticmethod
	def validate_specialisation(specialisation: str):
		pass


	def __str__(self):
		return f"""
Medical ID: {self.get_id}
Name: Dr {self.first_name + " " + self.last_name}
Date of Birth: {self.date_of_birth}
Specialisation: {self.specialisation}
Contact Email: {self.get_emails}
Contact Number: {self.get_numbers}"""


class Patient(Personal):
	count = 0
	def __init__(self, first_name: str, last_name: str, date_of_birth: str, reason: str):
		super().__init__(first_name, last_name, date_of_birth)
		self.__reason = reason
		self.__medical_history = MedicalHistory()

	@classmethod
	def __assign_id(cls):
		cls.count += 1
		return f"PTT-{str(cls.count):>03}"

	@property
	def get_id(self): return self.__assign_id()

	def add_medical_record(self):
		pass

	def delete_medical_record(self):
		pass

	def view_medical_history(self):
		pass


	def __str__(self):
		return f"""
Patient ID: {self.get_id}
Name: {self.first_name + " " +self.last_name}
Date of Birth: {self.date_of_birth}
Contact Email: {self.get_emails}
Contact Number: {self.get_numbers}"""



me = Doctor("john","smith", "1/1/2011", "doctor")
you = Doctor("mohammed","la'ad", "1/1/2010", "doctor")
print(me.first_name)
me.first_name = "marY-JaNe"
me.add_email("jm@gmail.com")
me.add_number("090")
print(me)