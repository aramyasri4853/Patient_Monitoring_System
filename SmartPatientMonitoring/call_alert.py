from twilio.rest import Client

ACCOUNT_SID = "xxxxxxxxxxxxxxxxxxxxxx"
AUTH_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

TWILIO_NUMBER = "+17656844699"
RECEIVER_NUMBER = "+91xxxxxxxxxx"


def make_call(message):

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    call = client.calls.create(
        twiml=f'<Response><Say>{message}</Say></Response>',
        from_=TWILIO_NUMBER,
        to=RECEIVER_NUMBER
    )

    print("📞 Call sent!")
