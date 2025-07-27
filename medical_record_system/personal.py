#import re
from abc import ABC, abstractmethod
from datetime import datetime
from utilities.contact import Contact

class Personal(ABC):
	def __init__(self, name, date_of_birth: str):
		self.__name = name
		self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date() #user should enter d.o.b in this format
		self.__contact_information = Contact()

	@property
	@abstractmethod
	def id(self): pass

	@property
	def name(self) -> str:
		return self.__name

	@name.setter
	def name(self, full_name: str):
		self.__name = full_name.title().strip()

	@property
	def date_of_birth(self) -> str: return str(self.__date_of_birth)

	@date_of_birth.setter
	def date_of_birth(self, date_of_birth_input: str):
		self.__date_of_birth = datetime.strptime(date_of_birth_input, "%Y-%m-%d").date()
"""
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

	def __validate_email(self, email: str):
		if re.fullmatch(r"^([\w.-]+)@([a-z]+)\.([a-z.]+)$" ,email, re.I) is None:	#email must be in format "a-z|0-9@a-z.a-z"
			raise ValueError("Invalid email")
		if email in self.__contact_information.get_emails:
			raise ValueError(f"Email {email} already exists")		#does not allow duplicates

	def __validate_number(self, number: str):
		if re.fullmatch(r"^\d+$", number, re.I) is None:		#number must be all digits
			raise ValueError("Invalid number")
		#add proper number validation pattern after testing
		if number in self.__contact_information.get_numbers:
			raise ValueError(f"Number {number} already exists")		#does not allow duplicates
"""
