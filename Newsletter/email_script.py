import generate_letter as gen
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def generate_and_send_email(receiver):

    gen.generate_letter()

    fromaddr = "letterastra@gmail.com"
    toaddr = receiver

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Today's Space News Briefing"

    body = "Hi!\n\n These are the big things that happened in Space Today! \n Please view the pdf attached."

    msg.attach(MIMEText(body, 'plain'))

    filename = "letter.pdf"
    attachment = open("./letter.pdf", "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, os.environ.get('PASS'))
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

