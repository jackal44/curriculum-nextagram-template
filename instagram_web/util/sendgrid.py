import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email():
    message = Mail(
        from_email='k.zhengkhai@gmail.com',
        to_emails='yeeyond1997@gmail.com',
        subject="You've been hacked! =)",
        html_content='< strong > <h1> Hahahahahahha!!!!</h1> </strong >< h1 > Enjoy deleting these!< /h1 >')

    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
