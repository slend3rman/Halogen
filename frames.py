import os
import open_api
import mail,bigMail

# import the necessary packages
from imutils import paths
import argparse
import cv2
import generatePDF

def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()

def getFrames(directory,video):
	os.chdir(directory)
	os.system ('mkdir Outs')
	os.system('ffmpeg -i ' + video + ' -vf crop=in_w:in_h/2:in_w:in_h/2,fps=2 Outs/output%d.png')
	os.chdir('Outs')
	#print("In Outs")
	sent=[]
	maxTh = 0
	toSend = None
	
	for imagePath in paths.list_images('.'):
		#print(imagePath)
		# load the image, convert it to grayscale, and compute the
		# focus measure of the image using the Variance of Laplacian
		# method
		image = cv2.imread(imagePath)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		fm = variance_of_laplacian(gray)
		if (fm>maxTh):
			maxTh = fm
			toSend = imagePath
		"""text = "Blurry"
		#print(text)

		# if the focus measure is less than the supplied threshold,
		# then the image should be considered "blurry"
		if fm > 302:
			text = "Not Blurry"
			print("In if : " + text)

		# show the image
		cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
			cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
		cv2.imshow("Image", image)
		key = cv2.waitKey(0)"""
	print("chose : " + toSend)
	user = open_api.detectNumberPlate(toSend)
	email = user[2]
	if(email not in sent):
				#mail.sendEmail(email)
				generatePDF.gPDF(user[0],user[1],user[5])
				bigMail.sendEmail(email)
				sent.append(email)
	
	#email = open_api.detectNumberPlate('out10.png')
	#mail.sendEmail(email)
