#! /usr/bin/env python
#circular linked list python image viewer/manager




import sys, os
from PyQt4 import QtGui
from PyQt4 import QtCore
from PIL import Image
import webbrowser
import pyimgur

class ImageListNode():
	def __init__(self, filedir):
		self.next = self
		self.previous = self
		self.filedirectory = filedir
	def deleteNode(self, node):
		left = node.previous
		right = node.next
		left.next = right
		right.previous = left
		os.remove(node.filedirectory)
		printNode(node)

class PyImageViewer(QtGui.QWidget):
	def __init__(self):
		super(PyImageViewer, self).__init__()
		self.head = genImageList()
		self.setWindowTitle('pyimageviewer')
		self.setFixedSize(500,500)
		self.label = QtGui.QLabel()
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.gridlayout = QtGui.QGridLayout()
		#do initial image, subsequent images are handled in keyPressEvent
		#self.curr = imagelist[self.curridx]
		self.curr = self.head
		self.display(self.curr)
		#self.label.setScaledContents(True)
		self.setLayout(self.gridlayout)
		#self.setGeometry(0,0, 200, 200)
		self.show()

	def display(self, node):
		print node.filedirectory
		if node.filedirectory.lower().endswith('.gif'):
			gif = QtGui.QMovie(node.filedirectory)
			self.label.setMovie(gif)
		else:
			pixmap = QtGui.QPixmap(node.filedirectory)
			self.label.setPixmap(pixmap.scaled(500,500,QtCore.Qt.KeepAspectRatio))
		
		self.gridlayout.addWidget(self.label)
		if node.filedirectory.lower().endswith('.gif'):			
			gif.start()

	def keyPressEvent(self, keyevent):
		global app
		if keyevent.key() == QtCore.Qt.Key_Left:
			self.display(self.curr.previous)
			self.curr = self.curr.previous
		elif keyevent.key() == QtCore.Qt.Key_Right:
			self.display(self.curr.next)
			self.curr = self.curr.next
		elif keyevent.key() == QtCore.Qt.Key_C:
			#copy file to clipboard
			print ''
		elif keyevent.key() == QtCore.Qt.Key_R:
			#open reverse search in browser for current image
			#use temp hosting on imgur to enable reverse search via url 
			CLIENT_ID = "c9959b70315750d"
			PATH = self.curr.filedirectory

			im = pyimgur.Imgur(CLIENT_ID)
			uploaded_image = im.upload_image(PATH, title="img")
			print(uploaded_image.title)
			#print(uploaded_image.url)
			print(uploaded_image.link)
			webbrowser.open('https://www.google.com/searchbyimage?&image_url=' + uploaded_image.link)
		elif keyevent.key() == QtCore.Qt.Key_X:
			#cut file to clipboard
			print ''
		elif keyevent.key() == QtCore.Qt.Key_Escape:
			#exit program
			sys.exit(app.exec_())
		elif keyevent.key() == QtCore.Qt.Key_D:
			print 'deletion!'
			#self.curr.previous = self.curr.next
			self.curr.deleteNode(self.curr)
			self.display(self.curr.next)
			self.curr = self.curr.next

def printNode(node):
	print 'NODE: ' + node.filedirectory
	print 'NEXT: ' + node.next.filedirectory
	print 'PREV: ' + node.previous.filedirectory
	
		
def genImageList():
	global currdir
	head = ImageListNode('')
	imagelist = os.walk(currdir).next()[2]
	for i in imagelist:
		if not i.lower().endswith('.jpg') and not i.lower().endswith('.jpeg') and not i.lower().endswith('.png') and not i.lower().endswith('.gif'):
			imagelist.remove(i)
	print imagelist
	last = ImageListNode('')
	for image in imagelist:
		
		if head.filedirectory == '':#if head is None
			#do head
			head = ImageListNode(currdir + image)
			last = head
			print last.filedirectory
		elif image == imagelist[len(imagelist)-1]:#if last element
			#do last element
			last.next = ImageListNode(currdir + image)
			last.next.previous = last
			head.previous = last.next
			last = last.next
			last.next = head
		else:
			#do normal element
			last.next = ImageListNode(currdir + image)
			last.next.previous = last
			last = last.next
			
	return head

def main():
	global currdir, app
	genImageList()#get directory + filename from calling context
	piv = PyImageViewer()
	sys.exit(app.exec_())

imagelist = []
currdir = sys.argv[1]
print currdir
app = QtGui.QApplication(sys.argv)
#http://images.google.com/searchbyimage/upload
CLIENT_ID = "c9959b70315750d"
CLIENT_SECRET = "8d4ee9cf1fe047645abf8e8541d1848f58225a83"   # Needed for step 2 and 3

im = pyimgur.Imgur(CLIENT_ID, CLIENT_SECRET)
auth_url = im.authorization_url('code')
webbrowser.open(auth_url)
#pin = input("What is the pin? ") # Python 3x
#pin = raw_input("What is the pin? ") # Python 2x


if __name__ == '__main__':
	main()
