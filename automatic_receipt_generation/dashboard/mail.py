import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

username = "theshreyansdubey@gmail.com"
passwd = "thebelltollsforthelordoftrolls"

def mail(to, subject, text, d):
	msg = MIMEMultipart()

	msg['From'] = username
	msg['To'] = to
	msg['Subject'] = subject

	html = """
	<html>
	  <head></head>
	  <body>
	    <p>Hi!<br>
	       <table style="border : 1px solid black">
		   		<tr> 
					<td> Invoice # : </td>
					<td>""" + str(d[0]) + """</td>
				</tr>
				<tr> 
					<td> Vendor Email : </td>
					<td>""" + str(d[1]) + """</td>
				</tr>
				<tr> 
					<td> Method of Payment : </td>
					<td>""" + str(d[2]) + """</td>
				</tr>
				<tr> 
					<td> Transaction ID : </td>
					<td>""" + str(d[3]) + """</td>
				</tr>
				<tr> 
					<td> Total Amount : </td>
					<td>""" + str(d[4]) + """</td>
				</tr>
				<tr> 
					<td> Tax : </td>
					<td>""" + str(d[5]) + """</td>
				</tr>
		   </table>
	    </p>
	  </body>
	</html>
	""" 
	part1 = MIMEText(html, 'html')
	msg.attach(part1)

   #part = MIMEBase('application', 'octet-stream')
   #part.set_payload(open(attach, 'rb').read())
   #encoders.encode_base64(part)
   #part.add_header('Content-Disposition',
   #        'attachment; filename="%s"' % os.path.basename(attach))
   #msg.attach(part)

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(username, passwd)
	server.sendmail(username, to, msg.as_string())
	server.close()
