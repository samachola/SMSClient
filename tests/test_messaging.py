import unittest

from app import App

app = App
class TestStringMethods(unittest.TestCase):
	def test_add_message_to_queue(self):
			response = app.add_message('sample message')
			self.assertEqual(len(response), 1);
			app.clear_message_queue()

	def test_displays_queue(self):
		app.add_message('sample message')
		app.add_message('sample message 1')
		app.add_message('sample message 2')

		response = app.view_message_queue()
		self.assertEqual(len(response), 3)
		self.assertEqual(response[0], 'sample message')
		self.assertEqual(response[2], 'sample message 2')

		app.clear_message_queue()

	def test_clear_queue(self): 
		app.add_message('sample message')
		app.add_message('sample message 1')
		app.add_message('sample message 2')

		response = app.view_message_queue()
		self.assertEqual(len(response), 3)

		app.clear_message_queue()
		response = app.view_message_queue()
		self.assertEqual(len(response), 0)

	def test_send_message(self):
		app.add_message('sample message')

		response = app.send_message()
		print(response)

		self.assertEqual(response, 'message sent successfully')

