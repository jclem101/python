#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class Example(QtGui.QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('filemanager')
		QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
		
		gridlayout = QtGui.QGridLayout(self)
		sldr = QtGui.QSlider(1,self)
		sldr.setTickPosition(QtGui.QSlider.TicksBelow)
		gridlayout.addWidget(sldr, 0,0, QtCore.Qt.AlignTop)#enum type orientation, 1 = hor, 2 = vertical
		#print gridlayout.columnCount()
		scene = QtGui.QGraphicsScene(self)
		view = QtGui.QGraphicsView(scene, self)
		gridlayout.addWidget(view)
		#QtGui.QGraphicsView(self)
		self.setGeometry(0,0, 200, 200)

		self.show()
        
def main():
	app = QtGui.QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
