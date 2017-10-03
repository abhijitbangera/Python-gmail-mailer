from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
import smtplib

def mail_send(username,password,emaillist,text):
	try:
		server="smtp.gmail.com"
		port=587
		session = smtplib.SMTP(server, port)
		session.ehlo()
		session.starttls()
		session.ehlo
		session.login(username, password)
		msg = MIMEMultipart('mixed')
		msg['Subject'] = 'Email Subject' # Enter your mail subject
		msg['From'] = username
		msg['To'] = ', '.join(emaillist)
		headers = [ "From: " + msg['From'],
		            "Subject: " + msg['Subject'],
		            "To: " + msg['To'],
		            "MIME-Version: 1.0",
		           "Content-Type: text/html"]
		headers = "\r\n".join(headers)
		session.sendmail(username,
			            emaillist,
			            headers + "\r\n\r\n" + text)
	except Exception as e:
		print ("Error sending mail:", e)

# User Inputs		
mail_username="xyz@gmail.com" # Enter your gmail id
mail_password="YourPassword" # Enter your gmail password
emaillist="abc@hotmail.com" # Enter your recepient mail id
msg="Body of the email" # Enter you mail content

mail_send(mail_username,mail_password,emaillist,msg)