import re
from abc import ABC
from datetime import datetime
from typing import Optional
from utilities.contact import Contact

class Personal(ABC):
	def __init__(self, first_name: str, last_name: str, date_of_birth: str):
		self.__validate_name(first_name)
		self.first_name = first_name.title()

		self.__validate_name(last_name)
		self.last_name = last_name.title()

		self.date_of_birth = self.__validate_dob(date_of_birth)
		self.__contact_information = Contact()

	@property
	def first_name(self) -> str: return self.__first_name

	@first_name.setter
	def first_name(self, first_name: str):
		self.__validate_name(first_name)
		self.__first_name = first_name.title()

	@property
	def last_name(self) -> str: return self.__last_name

	@last_name.setter
	def last_name(self, last_name: str):
		self.__validate_name(last_name)
		self.__last_name = last_name.title()

	@property
	def date_of_birth(self) -> str: return self.__date_of_birth

	@date_of_birth.setter
	def date_of_birth(self, date_of_birth: str):
		self.__date_of_birth = self.__validate_dob(date_of_birth)

	@property
	def get_emails(self):
		return self.__contact_information.view_emails()

	def add_email(self, email: str):
		self.__contact_information.add_email(email)

	def edit_email(self, old_email: str, new_email: str):
		self.__contact_information.edit_email(old_email, new_email)

	def delete_email(self, email: str):
		self.__contact_information.delete_email(email)

	@property
	def get_numbers(self):
		return self.__contact_information.view_numbers()

	def add_number(self, number: str):
		self.__contact_information.add_number(number)

	def edit_number(self, old_number: str, new_number: str):
		self.__contact_information.edit_number(old_number, new_number)

	def delete_number(self, number: str):
		self.__contact_information.delete_number(number)

	@staticmethod
	def __validate_name(name: str):
		if re.fullmatch(r"^([a-z]+)([-']?)([a-z]+)$", name, re.I) is None: raise ValueError("Invalid name")
		"""maybe allow space/underscore character for middle names"""

	@staticmethod
	def __validate_dob(date_of_birth: str) -> Optional[str]:
		try: dob = datetime.strptime(date_of_birth, "%d/%m/%Y")
		except ValueError: raise ValueError("Invalid, date of birth should be in format DD/MM/YYYY. eg. 31/01/2025")
		if dob > datetime.now(): raise ValueError("Invalid date of birth")
		return dob.strftime("%d/%m/%Y")