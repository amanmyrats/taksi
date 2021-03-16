# import os
# from  twilio.rest import Client

# account_sid=os.environ['ACa0b0646156f095b60fc6a159cad21464']
# auth_token=os.environ['1ba680297b4b5ec2f695a961e88e8985']
# client=Client(account_sid, auth_token)

# message=client.messages.create(body="Join Earth's mightiest heroes. Like Kevin Bacon.",from_='+12057360756',to='+99365555833')

# print(message.sid)


# import os
# from twilio.rest import Client

import os
from twilio.rest import Client
import time
# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure

account_sid = os.environ['ACa0b0646156f095b60fc6a159cad21464']
time.sleep(5)
auth_token = os.environ['1ba680297b4b5ec2f695a961e88e8985']
client = Client(account_sid, auth_token)
time.sleep(5)
message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12057360756',
                     to='+99365555833'
                 )

print(message.sid)
time.sleep(5)