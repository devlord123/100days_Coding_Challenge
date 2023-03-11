import smtplib
EMAIL = "devowoyemi123@gmail.com"
PASSWORD = "rzlabgccspkwtwey"


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_mails(self, emails, name, phone):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=emails,
                msg=f"Subject: Welcome To Owoyemi BlogPost\n"
                    f"Hello {name} \n"
                    f"Thanks for subcribing to Owoyemi BlogPost, your email is {emails}, you willl be receiving our mails now.\n"
                    f"Your phone number is {phone}"


            )
            return True
