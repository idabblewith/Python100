from days.day_040.files.helpers import Client, smtplib, nls, bcolors

# Class responsible for handling sending notifications with Twilio API
class NotificationManager:
    def __init__(
        self,
        MY_EMAIL,
        MY_PASSWORD,
        TWILIO_ID="",
        TWILIO_TOKEN="",
        TWILIO_NUMBER="",
        MY_PHONE_NUMBER="",
    ):
        self.client = Client(TWILIO_ID, TWILIO_TOKEN) if TWILIO_ID != "" else None
        self.twilio_number = TWILIO_NUMBER
        self.my_number = MY_PHONE_NUMBER
        self.MY_EMAIL = MY_EMAIL
        self.MY_PASSWORD = MY_PASSWORD

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=self.twilio_number,
            to=self.my_number,
        )
        # Prints if successfully sent.
        print(f"PRICE UNDER TARGET -- Message sent: {message.sid}")

    def send_emails(self, message, person):
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
                conn.starttls()
                conn.login(user=self.MY_EMAIL, password=self.MY_PASSWORD)
                conn.sendmail(from_addr=self.MY_EMAIL, to_addrs=person, msg=message)
                nls(
                    f"{bcolors.OKBLUE}Sent message to {person}:\n{message}{bcolors.ENDC}"
                )
        except Exception as e:
            nls(f"{bcolors.FAIL}{e}{bcolors.ENDC}")
            nls(f"{bcolors.FAIL}Attempted Message:{bcolors.ENDC} {message}")
