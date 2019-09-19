import os
import africastalking

username = os.getenv('AT_USERNAME')
api_key = os.getenv('API_KEY')

africastalking.initialize(username, api_key)
sms = africastalking.SMS

class AfricasTalkingClient(object):
	""" Africas Talking Client.
	"""
	@classmethod
	def send_message(cls, message):
		""" Sends message to Africa's Talking API
		
			Params:
			--------------
				message - The top most message from the message queue

			Returns:
			-------------
				payload - dict 
		"""
		try:
			resp = sms.send(message, ["+254720637837"])
			response = {
				"message": "message sent successfully",
				"status": True,
				"resp": resp
			}
		except:
			response = {
				"message": "failed sending message",
				"status": False,
			}
		if response: return response