import os

def getFrames(directory,video):
	os.chdir(directory)
	os.system ('mkdir Outs')
	os.system('ffmpeg -i '+ video +' -vf fps=2 Outs/out%d.png')
	
getFrames('/home/manas/Desktop/Halogen/ffmpeg','2_1.mp4')
