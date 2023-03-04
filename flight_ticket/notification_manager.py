import smtplib
EMAIL = "devowoyemi123@gmail.com"
PASSWORD = "rzlabgccspkwtwey"


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_mails(self, emails, message, flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=emails,
                msg=f"{message} \nClick here to readMore... {flight_link}".encode('utf-8')

            )
            print("Succesfull.")


# fall = NotificationManager()
# fall.send_mails("owoyemiidrisolamilekan@gmail.com","Hello guy, welcome to our fields", "www.facebook.com")


