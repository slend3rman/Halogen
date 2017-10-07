import os
import open_api


def getFrames(directory,video):
	os.chdir(directory)
	os.system ('mkdir Outs')
	os.system('ffmpeg -i '+ video +' -vf fps=2 Outs/out%d.png')
	os.chdir('Outs')
	open_api.detectNumberPlate('out10.png')
