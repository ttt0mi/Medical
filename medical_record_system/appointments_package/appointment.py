from status import Status
from reason import Reason
from datetime import datetime


class Appointment:
    def __init__(self, reason: Reason) -> None:
        self.__date_and_time  = None
        self.__reason: Reason = reason
        self.__status: Status = Status.PENDING
        self.__patient_name = None

    @property
    def date(self) -> datetime:
        return self.__date_and_time

    @date.setter
    def date(self, date_and_time: datetime) -> None:
        self.__date_and_time = str(date_and_time) 

    @property
    def reason(self) -> Reason:
        return self.__reason

    @reason.setter
    def reason(self, reason_for_appointment: Reason) -> None:
        self.__reason = reason_for_appointment

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, _status: Status) -> None:
        self.__status = _status

    @property
    def patient_name(self) -> str:
        return self.__patient_name

    @patient_name.setter
    def patient_name(self, the_patient_name: str) -> None:
        self.__patient_name = the_patient_name
        
    def is_upcoming(self) -> bool:
        return self.__status != Status.RESOLVED





