from clients.nexmoclient.app import NexmoClient
from clients.africastalkingclient.app import AfricasTalkingClient

nexmo = NexmoClient
africas_talking = AfricasTalkingClient

class Messages(object):
		""" 
			- Adds messages to a queue.
			- Sends priority message and removes from queue.
		"""
		def __init__(self): 
				self.message_queue = []

		def add_message_to_queue(self, message):
				""" Add new message to a queue

					Params: 
					-----------
					message - string. this is the message body

					Returns:
					-----------
					message_queue - list. This is the list of our queue

				"""
				self.message_queue.append(message)
				return self.message_queue

		def send_message(self):
				""" Sends priority message to either Nexmo or Africas Talking

					Returns:
					----------
					String - Success and Failure Message.

				"""
				priority_message = self.message_queue.pop(0)
				# send this message to Africa's Talking or NexmoClient
				response = nexmo.send_message(priority_message)
				# response = africas_talking.send_message(priority_message)
				print(response);
				return response['message']

		def clear_queue(self):
			""" Clears/Deletes the whole queue.

				Returns:
				----------
				message_queue - an empy message queue
			"""
			self.message_queue.clear()
			return self.message_queue
	
	