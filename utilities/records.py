from typing import Callable

class MedicalRecords:
	def __init__(self):
		self.__database: dict[str, Callable] = {}
		"""Patient|Doctor' is a type annotation saying that personnel can be a Patient instance or a Doctor instance"""

	def save(self, personnel_id: str, personnel: Callable):
		self.__database.update({personnel_id: personnel})

	def retrieve(self, personnel_id: str):
		found_personnel = self.__find(personnel_id)
		return found_personnel

	def __find(self, personnel_id: str):			#this is a private method(double underscore before name)
		for ID, personnel in self.__database.items():
			if ID == personnel_id: return personnel
		raise ValueError(f"database with ID {personnel_id} not found")