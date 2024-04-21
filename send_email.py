import smtplib
import ssl
from constants import SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL


def send_email(message, subject):

    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    # encoding the message as UTF-8 to ensure that all characters are properly encoded and can be sent without causing encoding errors
    message = f"""Subject: {subject}

    {message}
    """.encode("utf-8")

    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)
        # Return True to indicate successful email sending
        return True

    except smtplib.SMTPException as e:
        # Log the error for debugging purposes
        # logging.error(f"Failed to send email: {e}")
        # Return False to indicate email sending failure
        return False
