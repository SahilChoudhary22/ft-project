"""
This file contains the constants that are used throughout the project
Change them according to your requirements and it'll affect the whole project
"""
#importing enum lib for creating enumerating constants
from enum import IntEnum

# the date and time format
DATE_FORMAT = "%b %-d %Y %-I:%-M%p"

# input date time format
INPUT_DATE_FORMAT = "%Y/%m/%d %I:%M%p"


# class that inherits IntEnum, popular way of pagination in django
class PageSize(IntEnum):
	TEN = 10
	TWENTY_FIVE = 25
	FIFTY = 50
	HUNDRED = 100


# Server errors in string format
INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
PAGE_NOT_FOUND = "PAGE_NOT_FOUND"
INVALID_PAGE_SIZE = "INVALID_PAGE_SIZE"
INVALID_USER_ID = "INVALID_USER_ID"
INVALID_PARAMETER = "INVALID_PARAMETER"
VALIDATION_ERROR = "VALIDATION_ERROR"
UNAUTHORIZED_ACCESS = "UNAUTHORIZED_ACCESS"