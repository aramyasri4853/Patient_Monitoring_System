from twilio.rest import Client

ACCOUNT_SID = "AC7df857fd80e4c273674b1af3dbda9ea7"
AUTH_TOKEN = "63d1804d1aac4bba4da8f91e81c2dccf"

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