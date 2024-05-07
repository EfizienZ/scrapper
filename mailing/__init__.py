import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(address):

    # Email configuration
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT'))

    # Email content
    sender = email
    receiver = address
    subject = "Cómo ser la gestoría Top 1% de [Provincia]"

    with open("./mailing/template.html", "r") as file:
        html_content = file.read()

    # Create a multipart message
    message = MIMEMultipart("alternative")
    message["From"] = email
    message["To"] = address
    message["Subject"] = subject

    # Attach HTML content
    message.attach(MIMEText(html_content, "html"))

    # Attach image
    with open("image.png", "rb") as img_file:
        img_data = img_file.read()

    # Connect to SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Start TLS encryption
        server.login(email, password)
        server.sendmail(sender, receiver, message.as_string())
        print("Email sent successfully!")
