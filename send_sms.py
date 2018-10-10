from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "Your Account Number"
# Your Auth Token from twilio.com/console
auth_token  = "Your Private Token"
client = Client(account_sid, auth_token)

message = client.messages.create(
                            to="Number you want to send an SMS",
                            from_="Number configured in Twilio",
                            body="This is an example of how to send SMS using Python"
                            )
print(message.sid)
