# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACfb78325b02e06e7a48e6b7e9508d00fa'
auth_token = '1cd511db84d6950525e1fb22b38ebb03'
client = Client(account_sid, auth_token)

def sendMessage():
    message = client.messages \
                    .create(
                         body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                         from_='+12403496055',
                         to='+17033216471'
                     )


sendMessage()
#print(message.sid)
