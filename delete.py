import os

def deleteFolder(directory):
	os.chdir(directory)
	os.system("rm -r " + directory)
