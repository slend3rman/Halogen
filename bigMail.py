import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

def sendEmail(toaddr): 
	fromaddr = "ff043095@gmail.com"
	#toaddr = "99manas99@gmail.com"
	password = "qaz2ws3c"
	 
	msg = MIMEMultipart()
	 
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Traffic Alert!"
	 
	body = "You have failed your country!"
	 
	msg.attach(MIMEText(body, 'plain'))
	 
	filename = "receipt.pdf"
	attachment = open("receipt.pdf", "rb")
	 
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	 
	msg.attach(part)
	 
	server = smtplib.SMTP('smtp.gmail.com', 587)

	#print('Server SET!')

	server.starttls()
	server.login(fromaddr, password)
	print('Logged in!')

	text = msg.as_string()
	try:
		server.sendmail(fromaddr, toaddr, text)
		print('Sent!')
	except:
		print('Email not sent')

	server.quit()
