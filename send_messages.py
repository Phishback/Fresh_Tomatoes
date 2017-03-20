from twilio import rest

# My Account Sid and Auth Token
account_sid = "AC5fe6cbb03f1394d9b11396f60783de0b"
auth_token = "eda47c6ba7d03690e424b118a9591938"
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body="IF YOU GET THIS IS TEXT ME ON MY NORMAL NUMBER NOT THIS NUMBER ",
    to="+15137226672",
    from_="+15139018136")
print message.sid
