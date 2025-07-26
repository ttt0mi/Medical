import re
from abc import ABC, abstractmethod
from datetime import datetime
from utilities.contact import Contact

class Personal(ABC):
	def __init__(self, first_name: str, last_name: str, date_of_birth: str):
		self.first_name = first_name
		self.last_name = last_name
		self.date_of_birth = date_of_birth
		self.__contact_information = Contact()

	@abstractmethod
	def get_id(self): pass

	@property
	def first_name(self) -> str: return self.__first_name

	@first_name.setter
	def first_name(self, first_name: str):
		self.__validate_name(first_name)
		self.__first_name = first_name.title().strip()

	@property
	def last_name(self) -> str: return self.__last_name

	@last_name.setter
	def last_name(self, last_name: str):
		self.__validate_name(last_name)
		self.__last_name = last_name.title().strip()

	@property
	def date_of_birth(self) -> str: return self.__date_of_birth

	@date_of_birth.setter
	def date_of_birth(self, date_of_birth: str):
		self.__validate_dob(date_of_birth)
		self.__date_of_birth = date_of_birth

	@property
	def emails(self)-> str:
		return self.__contact_information.view_emails()

	def add_email(self, email: str):
		self.__validate_email(email)
		self.__contact_information.add_email(email)

	def edit_email(self, old_email: str, new_email: str):
		self.__validate_email(new_email)
		self.__contact_information.edit_email(old_email, new_email)

	def delete_email(self, email: str):
		self.__contact_information.delete_email(email)

	@property
	def numbers(self) -> str:
		return self.__contact_information.view_numbers()

	def add_number(self, number: str):
		self.__validate_number(number)
		self.__contact_information.add_number(number)

	def edit_number(self, old_number: str, new_number: str):
		self.__validate_number(new_number)
		self.__contact_information.edit_number(old_number, new_number)

	def delete_number(self, number: str):
		self.__contact_information.delete_number(number)

	@staticmethod
	def __validate_name(name: str):
		if not name: raise ValueError("Name cannot be empty")
		if re.fullmatch(r"^([a-z]+)([-']?)([a-z]+)$", name.strip(), re.I) is None: raise ValueError("Invalid name")
		"""maybe allow space/underscore character for middle names"""

	@staticmethod
	def __validate_dob(date_of_birth: str):
		try: dob = datetime.strptime(date_of_birth, "%d/%m/%Y")
		except ValueError: raise ValueError("Invalid, date of birth should be in format DD/MM/YYYY. eg. 31/01/2025")
		if dob > datetime.now(): raise ValueError("Invalid date of birth")

	def __validate_email(self, email: str):
		if re.fullmatch(r"^([\w.-]+)@([a-z]+)\.([a-z.]+)$" ,email, re.I) is None:	#email must be in format "a-z|0-9@a-z.a-z"
			raise ValueError("Invalid email")
		if email in self.__contact_information.get_emails:
			raise ValueError(f"Email {email} already exists")		#does not allow duplicates

	def __validate_number(self, number: str):
		if re.fullmatch(r"^\d+$", number, re.I) is None:		#number must be all digits
			raise ValueError("Invalid number")
		"""add proper number validation pattern after testing"""
		if number in self.__contact_information.get_numbers:
			raise ValueError(f"Number {number} already exists")		#does not allow duplicates