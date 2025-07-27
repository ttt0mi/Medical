from enum import Enum

class Status(Enum):
    PENDING = "Appointment has been scheduled"
    CONFIRMED = "Appointment has been confirmed"
    RESCHEDULED = "Appointment has been rescheduled"
    CANCELED ="Appointment has been canceled"
    RESOLVED = "Appointment has been resolved"
