import pika

from Common import BaseBot, BotCreator
from Utils.Enums import BOT_TYPE, LOGIN_METHOD, BOT_TRIGGER_MARK

if __name__ == "__main__":
	connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
	)
	channel = connection.channel()

	channel.queue_declare(queue='hello')

	channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
	print(" [x] Sent 'Hello World!'")
	connection.close()