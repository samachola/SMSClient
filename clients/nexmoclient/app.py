import os
import nexmo

nexmo_key = os.getenv('NEXMO_KEY')
nexmo_secret = os.getenv('NEXMO_SECRET')

client = nexmo.Client(key=nexmo_key, secret=nexmo_secret)

class NexmoClient(object):
    """ Nexmo Client
    """
    @classmethod
    def send_message(cls, message):
        """ Sends message using the nexmo client

        Params:
        ----------
          message - String. Message being sent to the recepient.

        Response:
        -------------
          payload - dict
        """
        try:
          resp = client.send_message({
              'from': 'Nexmo',
              'to': '254720637837',
              'text': message,
          })

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