import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

username = "theshreyansdubey@gmail.com"
passwd = "pass"

def mail(to, subject, text, attach):
   msg = MIMEMultipart()

   msg['From'] = username
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text)) 

   part = MIMEBase('application', 'octet-stream')
   part.set_payload(open(attach, 'rb').read())
   encoders.encode_base64(part)
   part.add_header('Content-Disposition',
           'attachment; filename="%s"' % os.path.basename(attach))
   msg.attach(part)

   server = smtplib.SMTP("smtp.gmail.com", 587)
   server.ehlo()
   server.starttls()
   server.ehlo()
   server.login(username, passwd)
   server.sendmail(username, to, msg.as_string())
   server.close()
