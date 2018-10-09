import smtplib
 
def sendEmail(mailId):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("yourmail", "password")
	 
	msg = "YOU VIOLATED TRAFFIC RULES!!"
	
	try:
		server.sendmail("mail_address", mailId, msg)
		print("mail sent to : " + mailId)
		
	except:
		print("mail not sent")
			
	server.quit()
