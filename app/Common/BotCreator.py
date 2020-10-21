from Tasks import *
from Utils.Enums import BOT_TYPE, LOGIN_METHOD, BOT_TRIGGER_MARK
from .BaseBot import BaseBot

class BotCreator():
	@staticmethod
	def CreateBot(self, login_method, bot_type) -> BaseBot:
		if BOT_TYPE.__contains__(bot_type):
			self._BOT_TYPE = bot_type
			
			if bot_type == BOT_TYPE.CURSER:
				return CurseBot(login_method, bot_trigger_mark=BOT_TRIGGER_MARK.AT_SIGN)
			elif bot_type == BOT_TYPE.LMGTFY:
				return LMGTFYBot(login_method, bot_trigger_mark=BOT_TRIGGER_MARK.AT_SIGN)
			elif bot_type == BOT_TYPE.HORT:
				return HORTBot(login_method, bot_trigger_mark=BOT_TRIGGER_MARK.AT_SIGN)