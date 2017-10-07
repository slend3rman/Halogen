import sys
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os
from PyQt4.phonon import Phonon
import frames,delete
import thread

textbox = None

class videoPlayer(QtGui.QMainWindow):
   def __init__(self,directory,x,y,width,height):
        QtGui.QMainWindow.__init__(self)
        widget = QtGui.QWidget()
        layout = QtGui.QVBoxLayout()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setGeometry(x, y, width, height)


        self.player = Phonon.VideoPlayer(widget)
        layout.addWidget(self.player)

        #vpWidget = Phonon.VideoWidget()
        mediaObject = Phonon.MediaObject()

        self.mediaSrc = Phonon.MediaSource(directory)
        self.player.play(self.mediaSrc)
        self.show()

class Window(QtGui.QMainWindow):

	def __init__(self):
		super(Window,self).__init__()
		self.setGeometry(100,60,600,500)
		self.setWindowTitle("Halogen Speedbreaker")
		self.setWindowIcon(QtGui.QIcon('traffic.jpg'))
		self.home()
		
	def home(self):
		btn = QtGui.QPushButton("Quit",self)
		btn.clicked.connect(self.close_app)
		
		btn.resize(80,40)
		btn.move(280,420)
		
		upload = QtGui.QPushButton("Upload",self)
		upload.clicked.connect(self.selectFile)
		
		upload.resize(80,40)
		upload.move(350,40)
		
		start = QtGui.QPushButton("start",self)
		start.clicked.connect(self.showVid)
		
		start.resize(80,40)
		start.move(450,40)
		
		global textbox
		textbox = QtGui.QLineEdit(self)
		textbox.setReadOnly(True)
		textbox.move(40, 40)
		textbox.resize(280,40)
		
		self.show()
		
	def close_app(self):
		print("App successfully closed!")
		global textbox
        	dirName = textbox.text()
        	dirList = [str(i) for i in dirName.split('/')[0:-1]]
        	dirList.append('Outs')
        	dirOnly = '/'.join(dirList)
		delete.deleteFolder(dirOnly)
		sys.exit()
		
	def selectFile(self):
            global textbox
            fname = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\',"Video files (*.mp4 *.avi *.mov *.flv)")
            textbox.setText(fname)
            
        def showVid(self):
        	global textbox
        	dirName = textbox.text()
        	dirList = [str(i) for i in dirName.split('/')[0:-1]]
        	vid = str(dirName.split('/')[-1])
        	dirOnly = '/'.join(dirList)
        	thread.start_new_thread( frames.getFrames, (dirOnly,vid) )
     		self.player = videoPlayer(dirName,40,60,500,500)
                               
	
app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())
