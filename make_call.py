from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "Your Account Number"
# Your Auth Token from twilio.com/console
auth_token  = "Your Private Token"
client = Client(account_sid, auth_token)

message = client.calls.create(
                            #You can use the demo or your own TwinML created with your account.
                            url='http://demo.twilio.com/docs/voice.xml',
                            to="Number you want to send an SMS",
                            from_="Number configured in Twilio",
                            )
print(message.sid)
