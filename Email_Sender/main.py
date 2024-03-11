from smtplib import SMTP
import ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
''' This is a file containing my email data like password and email'''
import credentials

""" To implement the image all you need to do is enter the path to it"""
def create_image_attachment(path: str) -> MIMEImage:
    with open(path, 'rb') as image:
        mime_image = MIMEImage(image.read())
        mime_image.add_header('Content-Disposition', f'attachment; filename={path}')
        return mime_image


def send_email(to_email: str, subject: str, body: str, image: str|None = None):
    host: str = 'smtp.gmail.com'
    port: int = 587

    context = ssl.create_default_context()
    print('Logging in...')

    with SMTP(host=host, port=port) as connection:
        connection.starttls()
        connection.login(credentials.EMAIL, credentials.PASSWORD)
        print("Attempting to send the email...")

        message = MIMEMultipart()
        message['From'] = credentials.EMAIL
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        if image:
            file: MIMEImage = create_image_attachment(image)
            message.attach(file)

        connection.sendmail(from_addr=credentials.EMAIL, to_addrs=to_email, msg=message.as_string())
        print('Sent!')
        
        """ All you have to do is fill in the empty spaces and done."""
send_email(to_email='', subject='', body='', image=None)
