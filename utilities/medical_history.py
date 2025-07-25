from datetime import datetime

class MedicalHistory:
	def __init__(self):
		self.__records: dict[str, dict[str, str]] = {}
		self.__counter = 0

	def __assign_id(self):
		self.__counter += 1
		return f"R-{str(self.__counter):>03}"

	def add(self, record):
		date_added = datetime.now().ctime()
		self.__records.update(
				{self.__assign_id(): {record: date_added}}
		)

	def edit(self,  record_id, new_record):
		self.__validate_id(record_id)
		date_edited = datetime.now().ctime()
		self.__records.update(
				{record_id: {new_record: date_edited}}
		)

	def view_all(self):
		for ID, record in self.__records.items():
			for detail, date in record.items():
				print(f"{ID}: {detail} at {date}")

	def __validate_id(self, record_id):
		if record_id not in self.__records.keys(): raise ValueError(f"record with ID {record_id} not found")