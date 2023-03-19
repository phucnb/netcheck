import os, sys
from twilio.rest import Client
import datetime as dt
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")
FROM_PHONE_NUMBER = os.environ.get("FROM_PHONE_NUMBER")

with open('/home/netcheck/log/connection1.log', 'r') as file:
    log = file.readlines()

if ('------' in log[-1]):
    msg = ' '.join(log[-4:-2])
else:
    msg = log[-1]
# print(msg)


client = Client(TWILIO_SID, TWILIO_TOKEN)
message = client.messages.create(
body=msg,
from_=FROM_PHONE_NUMBER,
to=PHONE_NUMBER
)
