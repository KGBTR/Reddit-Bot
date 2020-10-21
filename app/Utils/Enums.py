from enum import Enum

# class BASE_ENUM(Enum):
# 	@classmethod
# 	def __contains__(cls, item):
# 		return item.value in cls._value2member_map_


class BOT_TYPE(Enum):
	CURSER=1
	HORT=2
	LMGTFY=3

	@classmethod
	def __contains__(cls, item):
			return item.value in cls._value2member_map_ 

class LOGIN_METHOD(Enum):
	STANDART=1
	TWO_FACTOR_AUTH=2

	@classmethod
	def __contains__(cls, item):
		return item.value in cls._value2member_map_

class BOT_TRIGGER_MARK(Enum):
	EXCLAMATION='!'
	QUESTION='?'
	PERCENT='%'
	AMPERSAND='&'
	ASTERISK='*'
	OCTOTHORPE='#'
	COLON=':'
	AT_SIGN="@"

	@classmethod
	def __contains__(cls, item):
		return item.value in cls._value2member_map_

class BOT_TRIGGER_WORD(Enum):
	CURSER="CURSER"
	HORT="HORT"
	LMGTFY="LMGTFY"

	@classmethod
	def __contains__(cls, item):
			return item.value in cls._value2member_map_ 