import os

def deleteFolder(directory):
	print('my Dir : ' + directory)
	os.chdir(directory)
	os.system("rm -r " + directory)
