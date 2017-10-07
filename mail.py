import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("ff043095@gmail.com", "qaz2ws3c")

""" sdfg95361@gmail.com , zxcg456q"""
 
msg = "YOU VIOLATED TRAFFIC RULES!!"
server.sendmail("ff043095@gmail.com", "99manas99@gmail.com", msg)
server.quit()
