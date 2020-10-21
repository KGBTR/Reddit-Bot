from pika import BlockingConnection, ConnectionParameters
from sys import exit

from Common import BaseBot, BotCreator
from Utils.Enums import BOT_TYPE, LOGIN_METHOD, BOT_TRIGGER_MARK


def main():
	connection = BlockingConnection(
		ConnectionParameters('localhost')
	)
	channel = connection.channel()

	channel.queue_declare(queue='HORT')

	def callback(ch, method, properties, body):
		print(" [x] Received %r" % body)

	channel.basic_consume(
		queue='hello',
  	on_message_callback=callback,
   	auto_ack=True
  )

	print(' [*] Waiting for messages. To exit press CTRL+C')
	channel.start_consuming()


if __name__ == '__main__':
	main()
	exit(0) 