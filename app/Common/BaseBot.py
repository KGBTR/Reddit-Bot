from praw import Reddit
from abc import ABC, abstractmethod
from configparser import ConfigParser, ExtendedInterpolation
import logging
from asyncio import sleep

from Utils.Enums import LOGIN_METHOD, BOT_TYPE, BOT_TRIGGER_WORD, BOT_TRIGGER_MARK

class BaseBot(ABC):
	_BOT_TYPE: BOT_TYPE
	_LOGIN_METHOD: LOGIN_METHOD
	_BOT_TRIGGER_WORD: BOT_TRIGGER_WORD
	_BOT_TRIGGER_MARK: BOT_TRIGGER_MARK

	cfg: ConfigParser
	Answer: str

	def __init__(
		self,
		login_method: LOGIN_METHOD,
		bot_type: BOT_TYPE,
		bot_trigger_mark: BOT_TRIGGER_MARK,
		bot_trigger_word: BOT_TRIGGER_WORD
	):
		cfg = ConfigParser(interpolation=ExtendedInterpolation())
		cfg.read('praw.ini')

		if login_method == LOGIN_METHOD.STANDART:
			self.Bot = Reddit(
				"STANDART",
				config_interpolation="extended"
			)

		# FIXME: 
		elif login_method == LOGIN_METHOD.TWO_FACTOR_AUTH:
			self.Bot = Reddit(
				"TWO_FACTOR_AUTH",
				config_interpolation="extended"
			)
		
		self._BOT_TYPE = bot_type
		self._LOGIN_METHOD = login_method
		self._BOT_TRIGGER_WORD = bot_trigger_word
		self._BOT_TRIGGER_MARK = bot_trigger_mark

		self.ActiveSubReddit = self.Bot.subreddit(
			cfg["CONFIG"]["ACTIVE_SUBREDDIT"]
		)

	@abstractmethod
	async def ReplyComment(self, answer: str=None):
		for comment in self.Bot.inbox.mentions(mark_read=False):
			if self.Answer is None and answer is None:
				raise NotImplementedError(
					"{} not Implemented".format(
						self.Answer.name
					)
				)
			
			elif not self.Answer is None and answer is None:
				comment.reply(body=self.Answer)
				comment.mark_read()
			
			elif self.Answer is None and not answer is None:
				self.Answer = answer
				comment.reply(body=answer)
				comment.mark_read()
			
			elif not self.Answer is None and not answer is None:
				self.Answer = answer
				comment.reply(body=answer)
				comment.mark_read()

			logging.info(
				"Bot Answer is:\n{}\n{}\n{}\n".format(
					'-'*55,
					self.Answer,
					'-'*55
				)
			)

			logging.info(
				"Bot Replied Comment w/ URL: {}{}".format(
					self.cfg["DEFAULT"]["reddit_url"],
					comment.context
				)
			)
			sleep(10)

	@abstractmethod
	def ReadMD(self):
		pass