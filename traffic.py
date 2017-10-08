import sys
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os
from PyQt4.phonon import Phonon
import frames,delete
import thread
textbox = None


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
        
        

data = {'col1':['1','2','3'], 'col2':['4','5','6'], 'col3':['7','8','9']}
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
		self.setGeometry(100,60,600,600)
		self.setFixedSize(600, 600)
		self.setWindowTitle("Halogen Speedbreaker")
		self.setWindowIcon(QtGui.QIcon('traffic.jpg'))
		self.home()
		
	def home(self):
		self.btn = QtGui.QPushButton("Quit", self)
		self.btn.clicked.connect(self.close_app)
		
		self.btn.resize(80,40)
		self.btn.move(280,520)
		
		self.upload = QtGui.QPushButton("Upload",self)
		self.upload.clicked.connect(self.selectFile)
		
		self.upload.resize(80,40)
		self.upload.move(350,40)
		
		self.start = QtGui.QPushButton("start",self)
		self.start.clicked.connect(self.showVid)
		
		self.start.resize(80,40)
		self.start.move(450,40)
		
		global textbox
		textbox = QtGui.QLineEdit(self)
		textbox.setReadOnly(True)
		textbox.move(40, 40)
		textbox.resize(280,40)
		
		table = QTableWidget()
	        tableItem = QTableWidgetItem()
	        
	        self.progressLabel = QtGui.QLabel(self)
	        self.progressLabel.setGeometry(QtCore.QRect(100, 110, 170, 23))
	        self.progressLabel.setText("Processing...")
		self.progressLabel.setVisible(False)
	        
	        self.progressBar = QtGui.QProgressBar(self)
		self.progressBar.setGeometry(QtCore.QRect(200, 110, 250, 23))
		self.progressBar.setMaximum(0)
		self.progressBar.setProperty("value", -1)
		self.progressBar.setObjectName(_fromUtf8("progressBar"))
		self.progressBar.setVisible(False)
	        
		self.setupUi()
		self.show()
		
	def setupUi(self):
		self.label = QtGui.QLabel(self)
		self.label.setGeometry(QtCore.QRect(40, 170, 141, 20))
		self.label.setObjectName(_fromUtf8("label"))
		self.tableWidget = QtGui.QTableWidget(self)
		self.tableWidget.setGeometry(QtCore.QRect(40, 200, 502, 300))
		self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
		self.tableWidget.setColumnCount(6)
		self.tableWidget.setRowCount(0)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(0, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(1, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(2, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(3, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(4, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(5, item)
		
	        self.retranslateUi()
		
	def retranslateUi(self):
		self.label.setText(_translate("self", "Law Violators:", None))
		item = self.tableWidget.horizontalHeaderItem(0)
		item.setText(_translate("self", "name", None))
		item = self.tableWidget.horizontalHeaderItem(1)
		item.setText(_translate("self", "number plate", None))
		item = self.tableWidget.horizontalHeaderItem(2)
		item.setText(_translate("self", "email", None))
		item = self.tableWidget.horizontalHeaderItem(3)
		item.setText(_translate("self", "contact", None))
		item = self.tableWidget.horizontalHeaderItem(4)
		item.setText(_translate("self", "address", None))
		item = self.tableWidget.horizontalHeaderItem(5)
		item.setText(_translate("self", "License No.", None))
		
	def insertInTable(self, userDetail):
		if(self.progressBar.isVisible()):
			self.progressBar.setVisible(False)
			self.progressLabel.setVisible(False)
			self.btn.setEnabled(True)
        		self.upload.setEnabled(True)
        		self.start.setEnabled(True)   
        		textbox.setEnabled(True)
		
		rowPosition = self.tableWidget.rowCount()
		
		self.tableWidget.insertRow(rowPosition)
		
		self.tableWidget.setItem(rowPosition , 0, QtGui.QTableWidgetItem(userDetail[0]))
		self.tableWidget.setItem(rowPosition , 1, QtGui.QTableWidgetItem(userDetail[1]))
		self.tableWidget.setItem(rowPosition , 2, QtGui.QTableWidgetItem(userDetail[2]))
		self.tableWidget.setItem(rowPosition , 3, QtGui.QTableWidgetItem(userDetail[3]))
		self.tableWidget.setItem(rowPosition , 4, QtGui.QTableWidgetItem(userDetail[4]))
		self.tableWidget.setItem(rowPosition , 5, QtGui.QTableWidgetItem(userDetail[5]))
		
	def close_app(self):
		print("App successfully closed!")
		global textbox
        	dirName = textbox.text()
        	dirList = [str(i) for i in dirName.split('/')[0:-1]]
        	try:
			dirList.append('Outs')
			dirOnly = '/'.join(dirList)
			delete.deleteFolder(dirOnly)
			print('Deleting..' + dirOnly)
		except:
			print("Force Quit...")
		finally:
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
		
		self.progressLabel.setVisible(True)
        	self.progressBar.setVisible(True)
        	self.btn.setEnabled(False)
        	self.upload.setEnabled(False)
        	self.start.setEnabled(False)   
        	textbox.setEnabled(False)
        	
        	
        	thread.start_new_thread(frames.getFrames, (dirOnly,vid,self))
     		self.player = videoPlayer(dirName,500,60,800,600)
                               
	
app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())

def putInTable(userDetail):
	GUI.insertInTable(userDetail)
