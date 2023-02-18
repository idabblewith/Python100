from days.day_039.files.helpers import Client

# Class responsible for handling sending notifications with Twilio API
class NotificationManager:
    def __init__(self, TWILIO_ID, TWILIO_TOKEN, TWILIO_NUMBER, MY_PHONE_NUMBER):
        self.client = Client(TWILIO_ID, TWILIO_TOKEN)
        self.twilio_number = TWILIO_NUMBER
        self.my_number = MY_PHONE_NUMBER

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=self.twilio_number,
            to=self.my_number,
        )
        # Prints if successfully sent.
        print(f"PRICE UNDER TARGET -- Message sent: {message.sid}")
