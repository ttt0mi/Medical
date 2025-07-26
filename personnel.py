from personal import Personal
from utilities.medical_history import MedicalHistory
from utilities.specialisations import Specialisation

class Doctor(Personal):
	__id_count = 0
	def __init__(self, first_name: str, last_name: str, date_of_birth: str, specialty: str):
		super().__init__(first_name, last_name, date_of_birth)
		self.specialisation = specialty
		self.__id = self.__assign_id()

	@classmethod
	def __assign_id(cls):
		cls.__id_count += 1
		return f"DTR-{str(cls.__id_count):>03}"

	@property
	def get_id(self): return self.__id

	@property
	def specialisation(self): return self.__specialisation

	@specialisation.setter
	def specialisation(self, specialisation: str):
		self.__specialisation = self.__find_specialty(specialisation)

	@staticmethod
	def __find_specialty(specialty):
		try: spec = Specialisation(str(specialty).strip().title())
		except ValueError:
			raise ValueError(f"Specialisation {specialty} does not exist.")
		return spec

	def __str__(self):
		return f"""
Medical ID: {self.__id}
Name: {self.first_name + " " + self.last_name}
Date of Birth: {self.date_of_birth}
Specialisation: {self.specialisation.value}
Contact Email: {self.emails}
Contact Number: {self.numbers}"""


class Patient(Personal):
	__id_count = 0
	def __init__(self, first_name: str, last_name: str, date_of_birth: str, reason: str):
		super().__init__(first_name, last_name, date_of_birth)
		self.__id = self.__assign_id()
		self.__reason = reason
		self.__medical_history = MedicalHistory()

	@classmethod
	def __assign_id(cls):
		cls.__id_count += 1
		return f"PTT-{str(cls.__id_count):>03}"

	@property
	def get_id(self): return self.__id

	def add_medical_record(self):
		pass

	def delete_medical_record(self):
		pass

	def view_medical_history(self):
		pass

	def __str__(self):
		return f"""
Patient ID: {self.__id}
Name: {self.first_name + " " +self.last_name}
Date of Birth: {self.date_of_birth}
Contact Email: {self.emails}
Contact Number: {self.numbers}"""