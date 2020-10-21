import logging
from asyncio import sleep

from Common import BaseBot, BotCreator
from Utils.Enums import BOT_TYPE, LOGIN_METHOD, BOT_TRIGGER_MARK

if __name__ == "__main__":
	# try:
	logging.basicConfig(
		format='%(asctime)s: %(message)s',
		datefmt='%d/%m/%Y %H:%M:%S',
		level=logging.INFO
	)

	CurseBot = BotCreator.CreateBot(
		BaseBot,
		login_method=LOGIN_METHOD.STANDART,
		bot_type=BOT_TYPE.CURSER
	)

	logging.info("Bot Logged In as u/{}".format(CurseBot.Bot.user.me()))

	logging.info(
		"Bot Type: {}".format(
			CurseBot._BOT_TYPE.name
		)
	)

	logging.info(
		"Active Subreddit: r/{}".format(
			CurseBot.ActiveSubReddit
		)
	)

	while True:
		CurseBot.Answer = """####MERHABA"""
		CurseBot.ReplyComment(answer="""####HELLO""")
		sleep(1)
	# except Exception as ex:
		# print(ex)
		# exit(-1)
	# else:
	