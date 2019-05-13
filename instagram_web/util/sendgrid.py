import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email():
    message = Mail(
        from_email='k.zhengkhai@gmail.com',
        to_emails='k.zhengkhai@gmail.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')

    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
