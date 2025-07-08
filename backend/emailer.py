import smtplib
from email.message import EmailMessage

def send_weekly_email(to_email, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = '📅 Your Weekly Study Schedule Check-In'
    msg['From'] = 'your_email@example.com'
    msg['To'] = to_email

    # Send the message via Gmail's SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('your_email@example.com', 'your_app_password')
        smtp.send_message(msg)
