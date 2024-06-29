import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
import os

# Function to send email
def send_email():
    # Email credentials (use environment variables for security)
    email_user = os.getenv('EMAIL_USER')
    email_password = os.getenv('EMAIL_PASSWORD')
    email_send = 'recipient@example.com'
    subject = 'Daily Report'

    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    # Sample email body (you can customize this)
    body = 'This is your daily report.'
    msg.attach(MIMEText(body, 'plain'))

    # Set up the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    # Send the email
    text = msg.as_string()
    server.sendmail(email_user, email_send, text)
    server.quit()
    print("Email sent successfully")

# Function to schedule the email sending
def schedule_email():
    # Schedule the send_email function to run
    schedule.every().day.at("09:00").do(send_email)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    if not os.getenv('EMAIL_USER') or not os.getenv('EMAIL_PASSWORD'):
        print("Please set the EMAIL_USER and EMAIL_PASSWORD environment variables")
    else:
        schedule_email()