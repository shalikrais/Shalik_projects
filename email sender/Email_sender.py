import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# Read the HTML template from a file
html_template = Template(Path('index.html').read_text())

# List of recipients with names and email addresses
recipients = [
    {'name': 'ABC', 'email': ''},
    {'name': 'XYZ', 'email': ''},
    # Add more recipients as needed
]

# Email details
sender_email = '<>'
sender_password = '<>'
subject = 'Support'

# Send personalized emails to each recipient
for recipient in recipients:
    # Create an EmailMessage object
    email = EmailMessage()
    email['From'] = sender_email
    email['To'] = recipient['email']
    email['Subject'] = subject

    # Substitute the recipient's name in the HTML template
    html_content = html_template.substitute({'name': recipient['name']})
    email.set_content(html_content, 'html')

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        smtp.send_message(email)
        print(f"Email sent to {recipient['email']}")

print('All emails sent successfully!')
