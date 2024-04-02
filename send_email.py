import smtplib
import ssl
import os
from dotenv import load_dotenv


def send_email(message, subject):

    load_dotenv()
    username = os.getenv("USER")
    password = os.getenv("PASSWORD")
    receiver = os.getenv("RECEIVER")

    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    # encoding the message as UTF-8 to ensure that all characters are properly encoded and can be sent without causing encoding errors
    message = f"""Subject: {subject}

    {message}
    """.encode("utf-8")

    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
        # Return True to indicate successful email sending
        return True
    
    except smtplib.SMTPException as e:
        # Log the error for debugging purposes
        # logging.error(f"Failed to send email: {e}")
        # Return False to indicate email sending failure
        return False
        

    