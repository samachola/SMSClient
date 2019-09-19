from messages import messages

messaging_client = messages.Messages();

class App: 
	def add_message(message):
		response = messaging_client.add_message_to_queue(message)
		return response # list showing the current queue

	def send_message():
		response = messaging_client.send_message()
		if response:
			return response

	def view_message_queue():
		return messaging_client.message_queue

	def clear_message_queue():
		return messaging_client.clear_queue()

