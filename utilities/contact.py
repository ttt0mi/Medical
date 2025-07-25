import re

class Contact:
	def __init__(self):
		self.__emails: list = []
		self.__numbers: list = []

	def add_email(self, email: str):
		self.__validate_email(email)
		self.__emails.append(email)
		
	def edit_email(self, old_email: str, new_email: str):
		found_email = self.__find_email(old_email)
		found_email_index = self.__emails.index(found_email)
		del self.__emails[found_email_index]
		self.__emails.insert(found_email_index, new_email)

	def delete_email(self, email: str):
		found_email = self.__find_email(email)
		self.__emails.remove(found_email)

	def view_emails(self) -> str:
		emails_list = [f"{email}" for email in self.__emails]
		return ", ".join(emails_list) if emails_list else "No emails"

	def __validate_email(self, email: str):
		if re.fullmatch(r"^([\w.-]+)@([a-z]+)\.([a-z.]+)$" ,email, re.I) is None:	#email must be in format "a-z|0-9@a-z.a-z"
			raise ValueError("Invalid email")
		if email in self.__emails: raise ValueError(f"Email {email} already exists")		#does not allow duplicates
		
	def __find_email(self, find_email: str):
		for email in self.__emails:
			if email == find_email: return email
		raise ValueError(f"Email {find_email} not found")


	def add_number(self, number: str):
		self.validate_number(number)
		self.__numbers.append(number)

	def edit_number(self, old_number: str, new_number: str):
		found_number = self.__find_number(old_number)
		found_number_index = self.__numbers.index(found_number)
		del self.__numbers[found_number_index]
		self.__numbers.insert(found_number_index, new_number)

	def delete_number(self, number: str):
		found_number = self.__find_number(number)
		self.__numbers.remove(found_number)

	def view_numbers(self) -> str:
		numbers_list = [f"{number}" for no, number in self.__numbers]
		return ", ".join(numbers_list) if numbers_list else "No Phone Numbers"

	def validate_number(self, number: str):
		if re.fullmatch(r"^\d+$", number, re.I) is None:		#number must be all digits
			raise ValueError("Invalid number")
		"""add proper number validation pattern after testing"""
		if number in self.__numbers: raise ValueError(f"Number {number} already exists")		#does not allow duplicates

	def __find_number(self, find_number: str):
		for number in self.__numbers:
			if number == find_number: return number
		raise ValueError(f"Email {find_number} not found")