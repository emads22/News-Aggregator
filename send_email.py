import smtplib
import ssl
import os
from dotenv import load_dotenv


def send_email(message):
    # Load environment variables from the .env file
    load_dotenv()
    # Access the environment variables
    username = os.getenv("USER")
    password = os.getenv("PASSWORD")
    receiver = os.getenv("RECEIVER")
    # Define SMTP server settings, SMTP server hostname and SMTP server port (SSL)
    host = "smtp.gmail.com"
    port = 465
    # SSL (Secure Sockets Layer): SSL is a protocol used to secure communication over a computer network. It provides encryption, authentication, and data integrity to ensure that data transferred between a client and a server remains confidential and tamper-proof.
    # ssl.create_default_context() creates an SSL context object (context) to establish secure connections over a network, such as when making HTTPS requests or setting up secure socket connections (secure communication)
    context = ssl.create_default_context()
    # Create email message (Subject must come directly after """ then add breakline before acual message)
    message = f"""Subject: New Email from {username}

    {message}
    """

    try:
        # smtplib.SMTP_SSL() establish an SMTP connection to SMTP server over SSL. It ensures that the communication between this application and the SMTP server is encrypted and secure.
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            # Login to SMTP server
            server.login(username, password)
            # Send email from sender to receiver
            server.sendmail(username, receiver, message)
        # # Display success message
        # print("\nEmail sent successfully\n")  
        # Return True to indicate successful email sending
        return True
    
    except stmlib.SMTPException as e:
        # # Display error message if email sending fails  
        # print(f"\nFailed to send email: {e}\n")  
        # Log the error for debugging purposes
        # logging.error(f"Failed to send email: {e}")
        # Return False to indicate email sending failure
        return False



# this_messsage = "HELLO THERE! HOW ARE YOU??"
# send_email(this_messsage)