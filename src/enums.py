from enum import Enum


class CarServiceType(Enum):
    OIL_CHANGE = 0
    REPAIR = 1
    REGISTRATION = 2
    INSURANCE = 3


class DayOfWeek(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6
