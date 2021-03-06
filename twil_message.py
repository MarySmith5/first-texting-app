# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hi, Mary! I'm so proud of you for learning to use Twilio!!!",
                     media_url=['https://demo.twilio.com/owl.png'],
                     from_=os.environ['TWILIO_NUMBER'],
                     to='+17192142929'
                 )

print(message.sid)
