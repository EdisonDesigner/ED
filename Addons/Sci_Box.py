from __future__ import division
#-*- coding: utf-8 -*- # 반드시 코드 2번째나 3번째 줄에 있어야함.
#!/usr/bin/python
__author__ = 'apple'
# import statements
PI = 3.141592
import FreeCAD as ED
from FreeCAD import Base, Vector
import PartDesign, Part, PartGui
from Part import BSplineCurve, Shape, Wire, Face, makePolygon, BRepOffsetAPI, Shell, makeLoft, Solid, Line, BSplineSurface, Compound, show, makePolygon, makeLoft, makeHelix
from PySide import QtGui, QtCore
from numpy import tan, sin, sqrt, arctan, pi, array, linspace, transpose, vstack, ndarray, dot, cos       #ED-PyCharm
from math import sin, sqrt, cos, pi
from numpy.linalg import solve
import numpy as np

import FreeCAD as App

import os
addonPath = os.path.dirname(os.path.abspath(__file__))

# UI Class definitions
class Sci(QtGui.QWidget):
	def __init__(self):           # 생성자 소멸자 : def __del__(self)
		super(Sci, self).__init__()
		self.initUI()

	def initUI(self):
		self.treeWidget = QtGui.QTreeWidget(self) # treeview
		#self.treeWidget.setHeaderLabels([u"과학상자 부품 트리", "path"]) # headerlabel명
		#self.treeWidget.setColumnCount(2) # headerlabel 칼럼 갯수
		self.treeWidget.setHeaderLabels([u"                  과학상자 부품 트리"]) # headerlabel명
		self.treeWidget.setColumnCount(1) # headerlabel 칼럼 갯수
		#self.treeWidget.addTopLevelItem(QtGui.QTreeWidgetItem(["test2", "ABCDE"])) # toplevelitems
		#item1 = QtGui.QTreeWidgetItem(self.treeWidget)
		#item1.setText(0, "Item 1") # setText 0 -> Item 1
		#item1.setText(1, "abcde") # setText 1 -> abcde
		#item1_1 = QtGui.QTreeWidgetItem(["child", "100"])
		#item1.addChild(item1_1)

		root0 = QtGui.QTreeWidgetItem(self.treeWidget)
		root0.setText(0,u'★부품 리스트★')
		child1 = QtGui.QTreeWidgetItem(root0)
		child1.setText(0,u'부품 이미지 및 분류')
		root0.setExpanded(1)
		self.treeWidget.addTopLevelItem(root0)

		root1 = QtGui.QTreeWidgetItem(self.treeWidget)
		root1.setText(0,u'축용 부품 설계')
		child1 = QtGui.QTreeWidgetItem(root1)
		child1.setText(0,u'축')
		#child1.setText(1,'name1')
		child2 = QtGui.QTreeWidgetItem(root1)
		child2.setText(0,u'베어링')
		#child2.setText(1,'name2')
		#hild4 = QtGui.QTreeWidgetItem(child3)
		#child4.setText(0,'child4')
		#child4.setText(1,'name4')
		self.treeWidget.addTopLevelItem(root1)

		root2 = QtGui.QTreeWidgetItem(self.treeWidget)
		root2.setText(0,u'판용 부품 설계')
		child1 = QtGui.QTreeWidgetItem(root2)
		child1.setText(0,u'앵글')
		child2 = QtGui.QTreeWidgetItem(root2)
		child2.setText(0,u'플라스틱판')
		child3 = QtGui.QTreeWidgetItem(root2)
		child3.setText(0,u'스트립')
		child4 = QtGui.QTreeWidgetItem(root2)
		child4.setText(0,u'플랜지판')
		child5 = QtGui.QTreeWidgetItem(root2)
		child5.setText(0,u'평판')
		child6 = QtGui.QTreeWidgetItem(root2)
		child6.setText(0,u'브래킷')
		child7 = QtGui.QTreeWidgetItem(root2)
		child7.setText(0,u'기타 판')
		self.treeWidget.addTopLevelItem(root2)

		root3 = QtGui.QTreeWidgetItem(self.treeWidget)
		root3.setText(0,u'결합용 부품 설계')
		child1 = QtGui.QTreeWidgetItem(root3)
		child1.setText(0,u'볼트')
		child2 = QtGui.QTreeWidgetItem(root3)
		child2.setText(0,u'너트')
		child3 = QtGui.QTreeWidgetItem(root3)
		child3.setText(0,u'와셔')
		child4 = QtGui.QTreeWidgetItem(root3)
		child4.setText(0,u'멈춤나사')
		self.treeWidget.addTopLevelItem(root3)

		root4 = QtGui.QTreeWidgetItem(self.treeWidget)
		root4.setText(0,u'전동용 부품 설계')
		child1 = QtGui.QTreeWidgetItem(root4)
		child1.setText(0,u'기어')
		child2 = QtGui.QTreeWidgetItem(root4)
		child2.setText(0,u'체인')
		child3 = QtGui.QTreeWidgetItem(root4)
		child3.setText(0,u'풀리')
		child4 = QtGui.QTreeWidgetItem(root4)
		child4.setText(0,u'래크')
		child5 = QtGui.QTreeWidgetItem(root4)
		child5.setText(0,u'피니언')
		self.treeWidget.addTopLevelItem(root4)

		root5 = QtGui.QTreeWidgetItem(self.treeWidget)
		root5.setText(0,u'기타 부품 설계')
		child1 = QtGui.QTreeWidgetItem(root5)
		child1.setText(0,u'타이어')
		child2 = QtGui.QTreeWidgetItem(root5)
		child2.setText(0,u'나사봉')
		child3 = QtGui.QTreeWidgetItem(root5)
		child3.setText(0,u'부싱')
		child4 = QtGui.QTreeWidgetItem(root5)
		child4.setText(0,u'기타 부품')     #기타부품으로 바꾸고 모든 부품을 하나의 group 안에서 처리
		self.treeWidget.addTopLevelItem(root5)

		self.treeWidget.setGeometry(10, 10, 260, 380)
		#self.treeWidget.expandAll()      # 트리 리스트 보여주기
		self.treeWidget.itemClicked.connect(self.clickedItem)

		self.group0 = QtGui.QGroupBox(self)
		self.group0.setGeometry(290, 10, 300, 360)
		self.group0.hide()
		self.group1 = QtGui.QGroupBox(self)
		self.group1.setGeometry(290, 10, 300, 360)
		self.group1.hide()
		self.group2 = QtGui.QGroupBox(self)
		self.group2.setGeometry(290, 10, 300, 360)
		self.group2.hide()
		self.group3 = QtGui.QGroupBox(self)
		self.group3.setGeometry(290, 10, 300, 360)
		self.group3.hide()
		self.group4 = QtGui.QGroupBox(self)
		self.group4.setGeometry(290, 10, 300, 360)
		self.group4.hide()
		self.group5 = QtGui.QGroupBox(self)
		self.group5.setGeometry(290, 10, 300, 360)
		self.group5.hide()
		self.group6 = QtGui.QGroupBox(self)
		self.group6.setGeometry(290, 10, 300, 360)
		self.group6.hide()
		self.group7 = QtGui.QGroupBox(self)
		self.group7.setGeometry(290, 10, 300, 360)
		self.group7.hide()
		self.group8 = QtGui.QGroupBox(self)
		self.group8.setGeometry(290, 10, 300, 360)
		self.group8.hide()
		self.group9 = QtGui.QGroupBox(self)
		self.group9.setGeometry(290, 10, 300, 360)
		self.group9.hide()
		self.group10 = QtGui.QGroupBox(self)
		self.group10.setGeometry(290, 10, 300, 360)
		self.group10.hide()
		self.group11 = QtGui.QGroupBox(self)
		self.group11.setGeometry(290, 10, 300, 360)
		self.group11.hide()
		self.group12 = QtGui.QGroupBox(self)
		self.group12.setGeometry(290, 10, 300, 360)
		self.group12.hide()
		self.group13 = QtGui.QGroupBox(self)
		self.group13.setGeometry(290, 10, 300, 360)
		self.group13.hide()
		self.group14 = QtGui.QGroupBox(self)
		self.group14.setGeometry(290, 10, 300, 360)
		self.group14.hide()
		self.group15 = QtGui.QGroupBox(self)
		self.group15.setGeometry(290, 10, 300, 360)
		self.group15.hide()
		self.group16 = QtGui.QGroupBox(self)
		self.group16.setGeometry(290, 10, 300, 360)
		self.group16.hide()
		self.group17 = QtGui.QGroupBox(self)
		self.group17.setGeometry(290, 10, 300, 360)
		self.group17.hide()
		self.group18 = QtGui.QGroupBox(self)
		self.group18.setGeometry(290, 10, 300, 360)
		self.group18.hide()
		self.group19 = QtGui.QGroupBox(self)
		self.group19.setGeometry(290, 10, 300, 360)
		self.group19.hide()
		self.group20 = QtGui.QGroupBox(self)
		self.group20.setGeometry(290, 10, 300, 360)
		self.group20.hide()
		self.group21 = QtGui.QGroupBox(self)
		self.group21.setGeometry(290, 10, 300, 360)
		self.group21.hide()
		self.group22 = QtGui.QGroupBox(self)
		self.group22.setGeometry(290, 10, 300, 360)
		self.group22.hide()

		#mainLayout = QtGui.QHBoxLayout()
		#mainLayout.addWidget(self.treeWidget)

		self.quitButton = QtGui.QPushButton("Quit", self)
		self.quitButton.setFixedWidth(100)
		self.quitButton.move(480,370)
		self.quitButton.setAutoDefault(True)
		self.quitButton.clicked.connect(self.onQuit)

		self.setGeometry(20, 250, 600, 400)
		self.setFixedWidth(600)
		self.setFixedHeight(400)
		self.setWindowTitle(u"과학상자 부품 모듈")
		self.show()

	def clickedItem(self, parent):
		if self.treeWidget.currentItem().text(0) == u"부품 이미지 및 분류":
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()
			self.group10.hide()
			self.group11.hide()
			self.group12.hide()
			self.group13.hide()
			self.group14.hide()
			self.group15.hide()
			self.group16.hide()
			self.group17.hide()
			self.group18.hide()
			self.group19.hide()
			self.group20.hide()
			self.group21.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"과학상자 부품리스트 링크",self.group0)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(20,15)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label0 = QtGui.QLabel('''<a href = 'http://www.jeilscience.co.kr/2007new/bupum/bupum_ilst2.html'>http://www.jeilscience.co.kr</a>''',self.group0)
			self.label0.setOpenExternalLinks(True)
			#self.label0.linkActivated(self._label0_linkActivated)
			self.label0.setFont('Courier')
			self.label0.setStyleSheet("font: bold;")
			self.label0.move(20,35)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"부품 이미지 및 분류",self.group0)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(20,100)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.imageButton = QtGui.QPushButton("image",self.group0)
			self.imageButton.setFixedWidth(100)
			self.imageButton.clicked.connect(self.onImage0)
			self.imageButton.move(40,130)

			self.imageButton = QtGui.QPushButton("categorization",self.group0)
			self.imageButton.setFixedWidth(100)
			self.imageButton.clicked.connect(self.onImage00)
			self.imageButton.move(160,130)

			self.label3 = QtGui.QLabel(u"빠른 모델 생성",self.group0)
			self.label3.setFont('Courier')
			self.label3.setStyleSheet("font-size: 10pt;")
			self.label3.move(20,190)

			self.label3 = QtGui.QLabel(u"부품 번호 입력",self.group0)
			self.label3.setFont('Courier')
			self.label3.setStyleSheet(" font-size: 9pt;")
			self.label3.move(50,220)

			self.numericInput0 = QtGui.QLineEdit(self.group0)
			self.numericInput0.setFixedWidth(50)
			self.numericInput0.move(190,220)

			self.imageButton = QtGui.QPushButton("Generate",self.group0)
			self.imageButton.setFixedWidth(100)
			self.imageButton.clicked.connect(self.onDesign0)
			self.imageButton.move(160,250)

			self.label4 = QtGui.QLabel(u"예) '3' 입력 : 스트립  - 9 생성 ",self.group0)
			self.label4.setFont('Courier')
			self.label4.setStyleSheet("color: red; font-size: 10pt;")
			self.label4.move(20,285)

			self.label5 = QtGui.QLabel(u"    '110a' 입력 : 베어링뭉치(상) 생성 ",self.group0)
			self.label5.setFont('Courier')
			self.label5.setStyleSheet("color: red; font-size: 10pt;")
			self.label5.move(20,305)


			self.group0.show()

		elif self.treeWidget.currentItem().text(0) == u"축":
			self.group0.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()
			self.group10.hide()
			self.group11.hide()
			self.group12.hide()
			self.group13.hide()
			self.group14.hide()
			self.group15.hide()
			self.group16.hide()
			self.group17.hide()
			self.group18.hide()
			self.group19.hide()
			self.group20.hide()
			self.group21.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"축 설계",self.group1)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(130,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group1)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"축 - 29cm", u"축 - 14cm", u"축 - 10cm", u"축 - 9cm", u"축 - 7.5cm", u"축 - 6.5cm", u"축 - 5cm", u"축 - 4cm", u"십자축 - 5cm")
			self.popup1 = QtGui.QComboBox(self.group1)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg1)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----", u"축 - 29cm", u"축 - 14cm", u"축 - 10cm", u"축 - 9cm", u"축 - 7.5cm", u"축 - 6.5cm", u"축 - 5cm", u"축 - 4cm", u"십자축 - 5cm")
			self.popup2 = QtGui.QComboBox(self.group1)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes1)
			self.popup2.move(160,80)

			self.label3 = QtGui.QLabel(u"사용자 부품(축)",self.group1)
			self.label3.setStyleSheet("font-size: 10pt;")
			self.label3.setFont('Courier')
			self.label3.move(10,140)

			self.imageButton = QtGui.QPushButton("image",self.group1)
			self.imageButton.setFixedWidth(200)
			self.imageButton.clicked.connect(self.onImage1)
			self.imageButton.move(50,170)

			self.label4 = QtGui.QLabel(u"원 지름(mm)",self.group1)
			self.label4.move(55,200)
			self.numericInput0 = QtGui.QLineEdit(self.group1)
			self.numericInput0.setFixedWidth(50)
			self.numericInput0.move(190,200)
			self.label5 = QtGui.QLabel(u"길이(mm)",self.group1)
			self.label5.move(55,225)
			self.numericInput2 = QtGui.QLineEdit(self.group1)
			self.numericInput2.setFixedWidth(50)
			self.numericInput2.move(190,225)

			self.designButton = QtGui.QPushButton("Design",self.group1)
			self.designButton.clicked.connect(self.onDesign1)
			self.designButton.setFixedWidth(200)
			self.designButton.setAutoDefault(True)
			self.designButton.move(50,325)

			self.group1.show()

		elif self.treeWidget.currentItem().text(0) == u"베어링":
			self.group0.hide()
			self.group1.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()
			self.group10.hide()
			self.group11.hide()
			self.group12.hide()
			self.group13.hide()
			self.group14.hide()
			self.group15.hide()
			self.group16.hide()
			self.group17.hide()
			self.group18.hide()
			self.group19.hide()
			self.group20.hide()
			self.group21.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"베어링 설계",self.group2)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(120,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group2)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"상자형베어링", u"베어링뭉치(상)", u"베어링뭉치(가이드)", u"베어링뭉치(하)")
			self.popup1 = QtGui.QComboBox(self.group2)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg2)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----",  u"상자형베어링", u"베어링뭉치(상)", u"베어링뭉치(가이드)", u"베어링뭉치(하)")
			self.popup2 = QtGui.QComboBox(self.group2)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes2)
			self.popup2.move(160,80)

			self.group2.show()
		elif self.treeWidget.currentItem().text(0) == u"앵글":
			self.group0.hide()
			self.group1.hide()
			self.group2.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()
			self.group10.hide()
			self.group11.hide()
			self.group12.hide()
			self.group13.hide()
			self.group14.hide()
			self.group15.hide()
			self.group16.hide()
			self.group17.hide()
			self.group18.hide()
			self.group19.hide()
			self.group20.hide()
			self.group21.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"앵글 설계",self.group3)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(130,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group3)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"앵글 - 25", u"앵글 - 19", u"앵글 - 11", u"앵글 - 9", u"앵글 - 7", u"앵글 - 3", u"앵글 - 2")
			self.popup1 = QtGui.QComboBox(self.group3)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg3)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----", u"앵글 - 25", u"앵글 - 19", u"앵글 - 11", u"앵글 - 9", u"앵글 - 7", u"앵글 - 3", u"앵글 - 2")
			self.popup2 = QtGui.QComboBox(self.group3)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes3)
			self.popup2.move(160,80)

			self.label3 = QtGui.QLabel(u"사용자 부품(앵글)",self.group3)
			self.label3.setStyleSheet("font-size: 10pt;")
			self.label3.setFont('Courier')
			self.label3.move(10,120)

			self.imageButton = QtGui.QPushButton("image",self.group3)
			self.imageButton.setFixedWidth(200)
			self.imageButton.clicked.connect(self.onImage3)
			self.imageButton.move(50,145)

			self.label4 = QtGui.QLabel(u"가로(mm)",self.group3)
			self.label4.move(55,175)
			self.numericInput1 = QtGui.QLineEdit(self.group3)
			self.numericInput1.setFixedWidth(50)
			self.numericInput1.move(190,175)
			self.label5 = QtGui.QLabel(u"세로(mm)",self.group3)
			self.label5.move(55,200)
			self.numericInput2 = QtGui.QLineEdit(self.group3)
			self.numericInput2.setFixedWidth(50)
			self.numericInput2.move(190,200)
			self.label6 = QtGui.QLabel(u"높이(mm)",self.group3)
			self.label6.move(55,225)
			self.numericInput3 = QtGui.QLineEdit(self.group3)
			self.numericInput3.setFixedWidth(50)
			self.numericInput3.move(190,225)
			self.label7 = QtGui.QLabel(u"두께(mm)",self.group3)
			self.label7.move(55,250)
			self.numericInput4 = QtGui.QLineEdit(self.group3)
			self.numericInput4.setFixedWidth(50)
			self.numericInput4.move(190,250)
			self.label8 = QtGui.QLabel(u"홀의 지름(mm)",self.group3)
			self.label8.move(55,275)
			self.numericInput5 = QtGui.QLineEdit(self.group3)
			self.numericInput5.setFixedWidth(50)
			self.numericInput5.move(190,275)
			self.label9 = QtGui.QLabel(u"홀의 개수",self.group3)
			self.label9.move(55,300)
			self.numericInput6 = QtGui.QLineEdit(self.group3)
			self.numericInput6.setFixedWidth(50)
			self.numericInput6.move(190,300)

			self.designButton = QtGui.QPushButton("Design",self.group3)
			self.designButton.clicked.connect(self.onDesign3)
			self.designButton.setFixedWidth(200)
			self.designButton.setAutoDefault(True)
			self.designButton.move(50,325)

			self.group3.show()

		elif self.treeWidget.currentItem().text(0) == u"플라스틱판":
			self.group0.hide()
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()
			self.group10.hide()
			self.group11.hide()
			self.group12.hide()
			self.group13.hide()
			self.group14.hide()
			self.group15.hide()
			self.group16.hide()
			self.group17.hide()
			self.group18.hide()
			self.group19.hide()
			self.group20.hide()
			self.group21.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"플라스틱판 설계",self.group4)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(110,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group4)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"플라스틱판 11X5", u"플라스틱판 11X3", u"플라스틱판 7X5", u"플라스틱판 5X5", u"플라스틱판 5X3", u"삼각플라스틱판",u"반원플라스틱판")
			self.popup1 = QtGui.QComboBox(self.group4)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg4)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----", u"플라스틱판 11X5", u"플라스틱판 11X3", u"플라스틱판 7X5", u"플라스틱판 5X5", u"플라스틱판 5X3", u"삼각플라스틱판",u"반원플라스틱판")
			self.popup2 = QtGui.QComboBox(self.group4)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes4)
			self.popup2.move(160,80)

			self.label3 = QtGui.QLabel(u"사용자 부품(플라스틱판)",self.group4)
			self.label3.setStyleSheet("font-size: 10pt;")
			self.label3.setFont('Courier')
			self.label3.move(10,120)

			self.imageButton = QtGui.QPushButton("image",self.group4)
			self.imageButton.setFixedWidth(200)
			self.imageButton.clicked.connect(self.onImage4)
			self.imageButton.move(50,145)

			self.label4 = QtGui.QLabel(u"가로(mm)",self.group4)
			self.label4.move(55,175)
			self.numericInput1 = QtGui.QLineEdit(self.group4)
			self.numericInput1.setFixedWidth(50)
			self.numericInput1.move(190,175)
			self.label5 = QtGui.QLabel(u"세로(mm)",self.group4)
			self.label5.move(55,200)
			self.numericInput2 = QtGui.QLineEdit(self.group4)
			self.numericInput2.setFixedWidth(50)
			self.numericInput2.move(190,200)
			self.label6 = QtGui.QLabel(u"두께(mm)",self.group4)
			self.label6.move(55,225)
			self.numericInput3 = QtGui.QLineEdit(self.group4)
			self.numericInput3.setFixedWidth(50)
			self.numericInput3.move(190,225)
			self.label7 = QtGui.QLabel(u"홀의 지름(mm)",self.group4)
			self.label7.move(55,250)
			self.numericInput4 = QtGui.QLineEdit(self.group4)
			self.numericInput4.setFixedWidth(50)
			self.numericInput4.move(190,250)
			self.label8 = QtGui.QLabel(u"가로 홀 갯수",self.group4)
			self.label8.move(55,275)
			self.numericInput5 = QtGui.QLineEdit(self.group4)
			self.numericInput5.setFixedWidth(50)
			self.numericInput5.move(190,275)
			self.label9 = QtGui.QLabel(u"세로 홀 갯수",self.group4)
			self.label9.move(55,300)
			self.numericInput6 = QtGui.QLineEdit(self.group4)
			self.numericInput6.setFixedWidth(50)
			self.numericInput6.move(190,300)

			self.designButton = QtGui.QPushButton("Design",self.group4)
			self.designButton.clicked.connect(self.onDesign4)
			self.designButton.setFixedWidth(200)
			self.designButton.setAutoDefault(True)
			self.designButton.move(50,325)
			self.group4.show()

		elif self.treeWidget.currentItem().text(0) == u"스트립":
			self.group0.hide()
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()
			self.group10.hide()
			self.group11.hide()
			self.group12.hide()
			self.group13.hide()
			self.group14.hide()
			self.group15.hide()
			self.group16.hide()
			self.group17.hide()
			self.group18.hide()
			self.group19.hide()
			self.group20.hide()
			self.group21.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"스트립 설계",self.group5)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(120,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group5)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"스트립 - 25", u"스트립 - 15", u"스트립 - 11", u"스트립 - 9", u"스트립 - 5", u"좁은스트립 - 9", u"좁은스트립 - 7", u"좁은스트립 - 6", u"좁은스트립 - 5", u"좁은스트립 - 3", u"스트립 - 5(s)", u"ㄷ형스트립 - 3", u"ㄷ형스트립 - 5", u"ㄷ형스트립 - 7", u"원형스트립", u"곡면스트립", u"트러스스트립")
			self.popup1 = QtGui.QComboBox(self.group5)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg5)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----", u"스트립 - 25", u"스트립 - 15", u"스트립 - 11", u"스트립 - 9", u"스트립 - 5", u"좁은스트립 - 9", u"좁은스트립 - 7", u"좁은스트립 - 6", u"좁은스트립 - 5", u"좁은스트립 - 3", u"스트립 - 5(s)", u"ㄷ형스트립 - 3", u"ㄷ형스트립 - 5", u"ㄷ형스트립 - 7", u"원형스트립", u"곡면스트립", u"트러스스트립")
			self.popup2 = QtGui.QComboBox(self.group5)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes5)
			self.popup2.move(160,80)

			self.label3 = QtGui.QLabel(u"사용자 부품(스트립)",self.group5)
			self.label3.setStyleSheet("font-size: 10pt;")
			self.label3.setFont('Courier')
			self.label3.move(10,140)

			self.imageButton = QtGui.QPushButton("image",self.group5)
			self.imageButton.setFixedWidth(200)
			self.imageButton.clicked.connect(self.onImage5)
			self.imageButton.move(50,170)

			self.label4 = QtGui.QLabel(u"가로(mm)",self.group5)
			self.label4.move(55,200)
			self.numericInput1 = QtGui.QLineEdit(self.group5)
			self.numericInput1.setFixedWidth(50)
			self.numericInput1.move(190,200)
			self.label5 = QtGui.QLabel(u"세로(mm)",self.group5)
			self.label5.move(55,225)
			self.numericInput2 = QtGui.QLineEdit(self.group5)
			self.numericInput2.setFixedWidth(50)
			self.numericInput2.move(190,225)
			self.label6 = QtGui.QLabel(u"두께(mm)",self.group5)
			self.label6.move(55,250)
			self.numericInput3 = QtGui.QLineEdit(self.group5)
			self.numericInput3.setFixedWidth(50)
			self.numericInput3.move(190,250)
			self.label7 = QtGui.QLabel(u"홀의 지름(mm)",self.group5)
			self.label7.move(55,275)
			self.numericInput4 = QtGui.QLineEdit(self.group5)
			self.numericInput4.setFixedWidth(50)
			self.numericInput4.move(190,275)
			self.label8 = QtGui.QLabel(u"홀의 갯수(n>1)",self.group5)
			self.label8.move(55,300)
			self.numericInput5 = QtGui.QLineEdit(self.group5)
			self.numericInput5.setFixedWidth(50)
			self.numericInput5.move(190,300)

			self.designButton = QtGui.QPushButton("Design",self.group5)
			self.designButton.clicked.connect(self.onDesign5)
			self.designButton.setFixedWidth(200)
			self.designButton.setAutoDefault(True)
			self.designButton.move(50,325)

			self.group5.show()

		elif self.treeWidget.currentItem().text(0) == u"플랜지판":
			self.group0.hide()
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()
			self.group10.hide()
			self.group11.hide()
			self.group12.hide()
			self.group13.hide()
			self.group14.hide()
			self.group15.hide()
			self.group16.hide()
			self.group17.hide()
			self.group18.hide()
			self.group19.hide()
			self.group20.hide()
			self.group21.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"플랜지판 설계",self.group6)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(110,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group6)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"플랜지판(소)", u"플랜지판(대)", u"사다리꼴플랜지판", u"플랜지판 2X5", u"플랜지판 2X7")
			self.popup1 = QtGui.QComboBox(self.group6)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg6)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----", u"플랜지판(소)", u"플랜지판(대)", u"사다리꼴플랜지판", u"플랜지판 2X5", u"플랜지판 2X7")
			self.popup2 = QtGui.QComboBox(self.group6)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes6)
			self.popup2.move(160,80)

			self.label3 = QtGui.QLabel(u"사용자 부품(플랜지판)",self.group6)
			self.label3.setStyleSheet("font-size: 10pt;")
			self.label3.setFont('Courier')
			self.label3.move(10,120)

			self.imageButton = QtGui.QPushButton("image",self.group6)
			self.imageButton.setFixedWidth(200)
			self.imageButton.clicked.connect(self.onImage6)
			self.imageButton.move(50,145)

			self.label4 = QtGui.QLabel(u"가로(mm)",self.group6)
			self.label4.move(55,175)
			self.numericInput1 = QtGui.QLineEdit(self.group6)
			self.numericInput1.setFixedWidth(50)
			self.numericInput1.move(190,175)
			self.label5 = QtGui.QLabel(u"세로(mm)",self.group6)
			self.label5.move(55,200)
			self.numericInput2 = QtGui.QLineEdit(self.group6)
			self.numericInput2.setFixedWidth(50)
			self.numericInput2.move(190,200)
			self.label6 = QtGui.QLabel(u"높이(mm)",self.group6)
			self.label6.move(55,225)
			self.numericInput3 = QtGui.QLineEdit(self.group6)
			self.numericInput3.setFixedWidth(50)
			self.numericInput3.move(190,225)
			self.label7 = QtGui.QLabel(u"홀의 지름(mm)",self.group6)
			self.label7.move(55,250)
			self.numericInput4 = QtGui.QLineEdit(self.group6)
			self.numericInput4.setFixedWidth(50)
			self.numericInput4.move(190,250)
			self.label8 = QtGui.QLabel(u"가로 홀 개수",self.group6)
			self.label8.move(55,275)
			self.numericInput5 = QtGui.QLineEdit(self.group6)
			self.numericInput5.setFixedWidth(50)
			self.numericInput5.move(190,275)
			self.label9 = QtGui.QLabel(u"세로 홀 개수",self.group6)
			self.label9.move(55,300)
			self.numericInput6 = QtGui.QLineEdit(self.group6)
			self.numericInput6.setFixedWidth(50)
			self.numericInput6.move(190,300)

			self.designButton = QtGui.QPushButton("Design",self.group6)
			self.designButton.clicked.connect(self.onDesign6)
			self.designButton.setFixedWidth(200)
			self.designButton.setAutoDefault(True)
			self.designButton.move(50,325)

			self.group6.show()

		elif self.treeWidget.currentItem().text(0) == u"평판":
			self.group0.hide()
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group8.hide()
			self.group9.hide()
			self.group10.hide()
			self.group11.hide()
			self.group12.hide()
			self.group13.hide()
			self.group14.hide()
			self.group15.hide()
			self.group16.hide()
			self.group17.hide()
			self.group18.hide()
			self.group19.hide()
			self.group20.hide()
			self.group21.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"평판 설계",self.group7)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(130,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group7)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"평판(대)", u"평판(소)", u"평판 - 9", u"평판 - 7", u"평판 - 5", u"평판 - 3", u"오각평판", u"사각평판 3X5", u"삼각평판 3X5", u"바퀴평판")
			self.popup1 = QtGui.QComboBox(self.group7)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg7)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----", u"평판(대)", u"평판(소)", u"평판 - 9", u"평판 - 7", u"평판 - 5", u"평판 - 3", u"오각평판", u"사각평판 3X5", u"삼각평판 3X5", u"바퀴평판")
			self.popup2 = QtGui.QComboBox(self.group7)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes7)
			self.popup2.move(160,80)

			self.label3 = QtGui.QLabel(u"사용자 부품(평판)",self.group7)
			self.label3.setStyleSheet("font-size: 10pt;")
			self.label3.setFont('Courier')
			self.label3.move(10,140)

			self.imageButton = QtGui.QPushButton("image",self.group7)
			self.imageButton.setFixedWidth(200)
			self.imageButton.clicked.connect(self.onImage7)
			self.imageButton.move(50,170)

			self.label4 = QtGui.QLabel(u"가로(mm)",self.group7)
			self.label4.move(55,200)
			self.numericInput1 = QtGui.QLineEdit(self.group7)
			self.numericInput1.setFixedWidth(50)
			self.numericInput1.move(190,200)
			self.label5 = QtGui.QLabel(u"세로(mm)",self.group7)
			self.label5.move(55,225)
			self.numericInput2 = QtGui.QLineEdit(self.group7)
			self.numericInput2.setFixedWidth(50)
			self.numericInput2.move(190,225)
			self.label6 = QtGui.QLabel(u"홀의 지름(mm)",self.group7)
			self.label6.move(55,250)
			self.numericInput3 = QtGui.QLineEdit(self.group7)
			self.numericInput3.setFixedWidth(50)
			self.numericInput3.move(190,250)
			self.label7 = QtGui.QLabel(u"가로 홀 개수",self.group7)
			self.label7.move(55,275)
			self.numericInput4 = QtGui.QLineEdit(self.group7)
			self.numericInput4.setFixedWidth(50)
			self.numericInput4.move(190,275)
			self.label8 = QtGui.QLabel(u"세로 홀 개수",self.group7)
			self.label8.move(55,300)
			self.numericInput5 = QtGui.QLineEdit(self.group7)
			self.numericInput5.setFixedWidth(50)
			self.numericInput5.move(190,300)

			self.designButton = QtGui.QPushButton("Design",self.group7)
			self.designButton.clicked.connect(self.onDesign7)
			self.designButton.setFixedWidth(200)
			self.designButton.setAutoDefault(True)
			self.designButton.move(50,325)

			self.group7.show()

		elif self.treeWidget.currentItem().text(0) == u"브래킷":
			self.group0.hide()
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group9.hide()
			self.group10.hide()
			self.group11.hide()
			self.group12.hide()
			self.group13.hide()
			self.group14.hide()
			self.group15.hide()
			self.group16.hide()
			self.group17.hide()
			self.group18.hide()
			self.group19.hide()
			self.group20.hide()
			self.group21.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"브래킷 설계",self.group8)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(120,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group8)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"ㄷ형 브래킷(소)", u"ㄷ형 브래킷(대)", u"ㄱ형 브래킷(소)", u"ㄱ형 브래킷(대)", u"ㄱ형 브래킷 2X2", u"둔각브래킷", u"역각브래킷", u"삼각브래킷", u"모서리브래킷(좌)", u"모서리브래킷(우)",u"조향브래킷")
			self.popup1 = QtGui.QComboBox(self.group8)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg8)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----", u"ㄷ형 브래킷(소)", u"ㄷ형 브래킷(대)", u"ㄱ형 브래킷(소)", u"ㄱ형 브래킷(대)", u"ㄱ형 브래킷 2X2", u"둔각브래킷", u"역각브래킷", u"삼각브래킷", u"모서리브래킷(좌)", u"모서리브래킷(우)",u"조향브래킷")
			self.popup2 = QtGui.QComboBox(self.group8)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes8)
			self.popup2.move(160,80)

			self.group8.show()

		elif self.treeWidget.currentItem().text(0) == u"기타 판":
			self.group0.hide()
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group10.hide()
			self.group11.hide()
			self.group12.hide()
			self.group13.hide()
			self.group14.hide()
			self.group15.hide()
			self.group16.hide()
			self.group17.hide()
			self.group18.hide()
			self.group19.hide()
			self.group20.hide()
			self.group21.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"기타 판 설계",self.group9)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(110,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group9)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"이음판", u"휠판 - 8", u"반원판")
			self.popup1 = QtGui.QComboBox(self.group9)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg9)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----", u"이음판", u"휠판 - 8", u"반원판")
			self.popup2 = QtGui.QComboBox(self.group9)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes9)
			self.popup2.move(160,80)

			self.group9.show()

		elif self.treeWidget.currentItem().text(0) == u"볼트":
			self.group0.hide()
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()
			self.group11.hide()
			self.group12.hide()
			self.group13.hide()
			self.group14.hide()
			self.group15.hide()
			self.group16.hide()
			self.group17.hide()
			self.group18.hide()
			self.group19.hide()
			self.group20.hide()
			self.group21.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"볼트 설계",self.group10)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(130,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group10)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"볼트 0.6cm", u"볼트 1.3cm", u"볼트 2cm", u"볼트 3cm", u"사각머리볼트 0.8cm")
			self.popup1 = QtGui.QComboBox(self.group10)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg10)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----", u"볼트 0.6cm", u"볼트 1.3cm", u"볼트 2cm", u"볼트 3cm", u"사각머리볼트 0.8cm")
			self.popup2 = QtGui.QComboBox(self.group10)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes10)
			self.popup2.move(160,80)

			self.group10.show()

		elif self.treeWidget.currentItem().text(0) == u"너트":
			self.group0.hide()
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()
			self.group10.hide()
			self.group12.hide()
			self.group13.hide()
			self.group14.hide()
			self.group15.hide()
			self.group16.hide()
			self.group17.hide()
			self.group18.hide()
			self.group19.hide()
			self.group20.hide()
			self.group21.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"너트 설계",self.group11)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(130,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group11)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"너트")
			self.popup1 = QtGui.QComboBox(self.group11)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg11)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----", u"너트")
			self.popup2 = QtGui.QComboBox(self.group11)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes11)
			self.popup2.move(160,80)

			self.group11.show()

		elif self.treeWidget.currentItem().text(0) == u"와셔":
			self.group0.hide()
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()
			self.group10.hide()
			self.group11.hide()
			self.group13.hide()
			self.group14.hide()
			self.group15.hide()
			self.group16.hide()
			self.group17.hide()
			self.group18.hide()
			self.group19.hide()
			self.group20.hide()
			self.group21.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"와셔 설계",self.group12)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(130,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group12)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"와셔(소)", u"와셔(대)")
			self.popup1 = QtGui.QComboBox(self.group12)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg12)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----", u"와셔(소)", u"와셔(대)")
			self.popup2 = QtGui.QComboBox(self.group12)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes12)
			self.popup2.move(160,80)

			self.label3 = QtGui.QLabel(u"사용자 부품(와셔)",self.group12)
			self.label3.setStyleSheet("font-size: 10pt;")
			self.label3.setFont('Courier')
			self.label3.move(10,140)

			self.imageButton = QtGui.QPushButton("image",self.group12)
			self.imageButton.setFixedWidth(200)
			self.imageButton.clicked.connect(self.onImage12)
			self.imageButton.move(50,170)

			self.label4 = QtGui.QLabel(u"바깥 지름(mm)",self.group12)
			self.label4.move(55,200)
			self.numericInput1 = QtGui.QLineEdit(self.group12)
			self.numericInput1.setFixedWidth(50)
			self.numericInput1.move(190,200)
			self.label5 = QtGui.QLabel(u"안 지름(mm)",self.group12)
			self.label5.move(55,225)
			self.numericInput2 = QtGui.QLineEdit(self.group12)
			self.numericInput2.setFixedWidth(50)
			self.numericInput2.move(190,225)
			self.label6 = QtGui.QLabel(u"두께(mm)",self.group12)
			self.label6.move(55,250)
			self.numericInput3 = QtGui.QLineEdit(self.group12)
			self.numericInput3.setFixedWidth(50)
			self.numericInput3.move(190,250)

			self.designButton = QtGui.QPushButton("Design",self.group12)
			self.designButton.clicked.connect(self.onDesign12)
			self.designButton.setFixedWidth(200)
			self.designButton.setAutoDefault(True)
			self.designButton.move(50,325)

			self.group12.show()

		elif self.treeWidget.currentItem().text(0) == u"멈춤나사":
			self.group0.hide()
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()
			self.group10.hide()
			self.group11.hide()
			self.group12.hide()
			self.group14.hide()
			self.group15.hide()
			self.group16.hide()
			self.group17.hide()
			self.group18.hide()
			self.group19.hide()
			self.group20.hide()
			self.group21.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"멈춤나사 설계",self.group13)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(110,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group13)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"멈춤나사", u"구동기어 멈춤나사")
			self.popup1 = QtGui.QComboBox(self.group13)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg13)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----", u"멈춤나사", u"구동기어 멈춤나사")
			self.popup2 = QtGui.QComboBox(self.group13)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes13)
			self.popup2.move(160,80)

			self.group13.show()

		elif self.treeWidget.currentItem().text(0) == u"기어":
			self.group0.hide()
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()
			self.group10.hide()
			self.group11.hide()
			self.group12.hide()
			self.group13.hide()
			self.group15.hide()
			self.group16.hide()
			self.group17.hide()
			self.group18.hide()
			self.group19.hide()
			self.group20.hide()
			self.group21.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"기어 설계",self.group14)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(130,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group14)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"피니언기어", u"평기어(소)", u"평기어(대)", u"다목적기어", u"크라운기어", u"워엄기어", u"체인기어(소)", u"체인기어(대)", u"2단 평기어(소)",u"십자홀 2단평기어",u"십자홀 체인기어")
			self.popup1 = QtGui.QComboBox(self.group14)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg14)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----", u"피니언기어", u"평기어(소)", u"평기어(대)", u"다목적기어", u"크라운기어", u"워엄기어", u"체인기어(소)", u"체인기어(대)", u"2단 평기어(소)",u"십자홀 2단평기어",u"십자홀 체인기어")
			self.popup2 = QtGui.QComboBox(self.group14)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes14)
			self.popup2.move(160,80)

			self.label3 = QtGui.QLabel(u"사용자 부품(평기어)",self.group14)
			self.label3.setStyleSheet("font-size: 10pt;")
			self.label3.setFont('Courier')
			self.label3.move(10,140)

			self.imageButton = QtGui.QPushButton("image",self.group14)
			self.imageButton.setFixedWidth(200)
			self.imageButton.clicked.connect(self.onImage14)
			self.imageButton.move(50,170)

			self.label4 = QtGui.QLabel(u"기어의 잇수",self.group14)
			self.label4.move(55,200)
			self.numericInput1 = QtGui.QLineEdit(self.group14)
			self.numericInput1.setFixedWidth(50)
			self.numericInput1.move(190,200)
			self.label5 = QtGui.QLabel(u"모듈",self.group14)
			self.label5.move(55,225)
			self.numericInput2 = QtGui.QLineEdit(self.group14)
			self.numericInput2.setFixedWidth(50)
			self.numericInput2.move(190,225)
			self.label5 = QtGui.QLabel(u"중심-홀 거리(mm)",self.group14)
			self.label5.move(55,250)
			self.numericInput3 = QtGui.QLineEdit(self.group14)
			self.numericInput3.setFixedWidth(50)
			self.numericInput3.move(190,250)
			self.label5 = QtGui.QLabel(u"높이(mm)",self.group14)
			self.label5.move(55,275)
			self.numericInput4 = QtGui.QLineEdit(self.group14)
			self.numericInput4.setFixedWidth(50)
			self.numericInput4.move(190,275)

			self.designButton = QtGui.QPushButton("Design",self.group14)
			self.designButton.clicked.connect(self.onDesign14)
			self.designButton.setFixedWidth(200)
			self.designButton.setAutoDefault(True)
			self.designButton.move(50,325)

			self.group14.show()

		elif self.treeWidget.currentItem().text(0) == u"체인":
			self.group0.hide()
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()
			self.group10.hide()
			self.group11.hide()
			self.group12.hide()
			self.group13.hide()
			self.group14.hide()
			self.group16.hide()
			self.group17.hide()
			self.group18.hide()
			self.group19.hide()
			self.group20.hide()
			self.group21.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"체인 설계",self.group15)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(130,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group15)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"체인", u"링크체인")
			self.popup1 = QtGui.QComboBox(self.group15)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg15)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----", u"체인", u"링크체인")
			self.popup2 = QtGui.QComboBox(self.group15)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes15)
			self.popup2.move(160,80)
			self.group15.show()

		elif self.treeWidget.currentItem().text(0) == u"풀리":
			self.group0.hide()
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()
			self.group10.hide()
			self.group11.hide()
			self.group12.hide()
			self.group13.hide()
			self.group14.hide()
			self.group15.hide()
			self.group17.hide()
			self.group18.hide()
			self.group19.hide()
			self.group20.hide()
			self.group21.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"풀리 설계",self.group16)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(130,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group16)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"풀리(대)", u"풀리(중)", u"풀리(소)", u"타이어풀리", u"2단 풀리", u"피니언풀리")
			self.popup1 = QtGui.QComboBox(self.group16)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg16)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----", u"풀리(대)", u"풀리(중)", u"풀리(소)", u"타이어풀리", u"2단 풀리", u"피니언풀리")
			self.popup2 = QtGui.QComboBox(self.group16)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes16)
			self.popup2.move(160,80)
			self.group16.show()

		elif self.treeWidget.currentItem().text(0) == u"래크":
			self.group0.hide()
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()
			self.group10.hide()
			self.group11.hide()
			self.group12.hide()
			self.group13.hide()
			self.group14.hide()
			self.group15.hide()
			self.group16.hide()
			self.group18.hide()
			self.group19.hide()
			self.group20.hide()
			self.group21.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"래크 설계",self.group17)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(130,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group17)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"래크", u"래크홀더")
			self.popup1 = QtGui.QComboBox(self.group17)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg17)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----", u"래크", u"래크홀더")
			self.popup2 = QtGui.QComboBox(self.group17)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes17)
			self.popup2.move(160,80)

			self.group17.show()

		elif self.treeWidget.currentItem().text(0) == u"피니언":
			self.group0.hide()
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()
			self.group10.hide()
			self.group11.hide()
			self.group12.hide()
			self.group13.hide()
			self.group14.hide()
			self.group15.hide()
			self.group16.hide()
			self.group17.hide()
			self.group19.hide()
			self.group20.hide()
			self.group21.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"피니언 설계",self.group18)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(120,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group18)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"십자홀 피니언")
			self.popup1 = QtGui.QComboBox(self.group18)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg18)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----", u"십자홀 피니언")
			self.popup2 = QtGui.QComboBox(self.group18)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes18)
			self.popup2.move(160,80)

			self.group18.show()

		elif self.treeWidget.currentItem().text(0) == u"타이어":
			self.group0.hide()
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()
			self.group10.hide()
			self.group11.hide()
			self.group12.hide()
			self.group13.hide()
			self.group14.hide()
			self.group15.hide()
			self.group16.hide()
			self.group17.hide()
			self.group18.hide()
			self.group20.hide()
			self.group21.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"타이어 설계",self.group19)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(110,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group19)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"타이어(소)", u"타이어(중)", u"타이어(대)", u"타이어(특대)")
			self.popup1 = QtGui.QComboBox(self.group19)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg19)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----", u"타이어(소)", u"타이어(중)", u"타이어(대)", u"타이어(특대)")
			self.popup2 = QtGui.QComboBox(self.group19)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes19)
			self.popup2.move(160,80)

			self.group19.show()
		elif self.treeWidget.currentItem().text(0) == u"나사봉":
			self.group0.hide()
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()
			self.group10.hide()
			self.group11.hide()
			self.group12.hide()
			self.group13.hide()
			self.group14.hide()
			self.group15.hide()
			self.group16.hide()
			self.group17.hide()
			self.group18.hide()
			self.group19.hide()
			self.group21.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"나사봉 설계",self.group20)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(110,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group20)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"나사봉 - 5cm", u"나사봉 - 7.5cm")
			self.popup1 = QtGui.QComboBox(self.group20)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg20)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----", u"나사봉 - 5cm", u"나사봉 - 7.5cm", u"원기둥 - 5cm", u"원기둥 - 7.5cm")
			self.popup2 = QtGui.QComboBox(self.group20)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes20)
			self.popup2.move(160,80)

			self.labe20 = QtGui.QLabel(u" 나사산이 생성되지 않을시, 축 부품 이용",self.group20)
			self.labe20.setStyleSheet("font-size: 10pt; color: red;")
			self.labe20.setFont('Courier')
			self.labe20.move(10,110)

			self.label3 = QtGui.QLabel(u"사용자 부품(나사봉)",self.group20)
			self.label3.setStyleSheet("font-size: 10pt;")
			self.label3.setFont('Courier')
			self.label3.move(10,140)

			self.imageButton = QtGui.QPushButton("image",self.group20)
			self.imageButton.setFixedWidth(200)
			self.imageButton.clicked.connect(self.onImage20)
			self.imageButton.move(50,170)

			self.label4 = QtGui.QLabel(u"지름(mm)",self.group20)
			self.label4.move(55,200)
			self.numericInput1 = QtGui.QLineEdit(self.group20)
			self.numericInput1.setFixedWidth(50)
			self.numericInput1.move(190,200)
			self.label5 = QtGui.QLabel(u"길이(mm)",self.group20)
			self.label5.move(55,225)
			self.numericInput2 = QtGui.QLineEdit(self.group20)
			self.numericInput2.setFixedWidth(50)
			self.numericInput2.move(190,225)

			self.designButton = QtGui.QPushButton("Design",self.group20)
			self.designButton.clicked.connect(self.onDesign20)
			self.designButton.setFixedWidth(200)
			self.designButton.setAutoDefault(True)
			self.designButton.move(50,325)

			self.group20.show()
		elif self.treeWidget.currentItem().text(0) == u"부싱":
			self.group0.hide()
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()
			self.group10.hide()
			self.group11.hide()
			self.group12.hide()
			self.group13.hide()
			self.group14.hide()
			self.group15.hide()
			self.group16.hide()
			self.group17.hide()
			self.group18.hide()
			self.group19.hide()
			self.group20.hide()
			self.group22.hide()

			self.label1 = QtGui.QLabel(u"부싱 설계",self.group21)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(110,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group21)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"조정부싱", u"축연결부싱", u"사각홀고무부싱", u"플라스틱부싱 0.6cm", u"플라스틱부싱 1.2cm", u"실리콘부싱 0.6cm")
			self.popup1 = QtGui.QComboBox(self.group21)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg21)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----", u"조정부싱", u"축연결부싱", u"사각홀고무부싱", u"플라스틱부싱 0.6cm", u"플라스틱부싱 1.2cm", u"실리콘부싱 0.6cm")
			self.popup2 = QtGui.QComboBox(self.group21)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes21)
			self.popup2.move(160,80)

			self.group21.show()

		elif self.treeWidget.currentItem().text(0) == u"기타 부품":
			self.group0.hide()
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()
			self.group10.hide()
			self.group11.hide()
			self.group12.hide()
			self.group13.hide()
			self.group14.hide()
			self.group15.hide()
			self.group16.hide()
			self.group17.hide()
			self.group18.hide()
			self.group19.hide()
			self.group20.hide()
			self.group21.hide()

			self.label1 = QtGui.QLabel(u"기타 부품 설계",self.group22)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold;")
			self.label1.move(110,10)
			#self.label1.setAlignment(self.label1,QtCore.Qt.AlignCenter)

			self.label2 = QtGui.QLabel(u"기존 부품",self.group22)
			self.label2.setFont('Courier')
			self.label2.setStyleSheet("font-size: 10pt;")
			self.label2.move(10,50)
			#self.label2.setStyleSheet("font-size: 9pt; font-weight: bold; font-family: Arial;")

			self.popupItems1 = (" ---- Image ----", u"스프링클립", u"지지판", u"양팔크랭크", u"면판휠", u"나사핀", u"프로펠러", u"훅", u"파워핸들", u"축이음쇠", u"모터뭉치", u"구동기어뭉치", u"캐노피", u"기어드모터", u"이동클립", u"홈샤프트", u"홈샤프트캡")
			self.popup1 = QtGui.QComboBox(self.group22)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(" ---- Image ----"))
			self.popup1.setFixedWidth(120)
			self.popup1.activated[str].connect(self.onPopupImg22)
			self.popup1.move(20,80)

			self.popupItems2 = (" ---- Design ----", u"스프링클립", u"지지판", u"양팔크랭크", u"면판휠", u"나사핀", u"프로펠러", u"훅", u"파워핸들", u"축이음쇠", u"모터뭉치", u"구동기어뭉치", u"캐노피", u"기어드모터", u"이동클립", u"홈샤프트", u"홈샤프트캡")
			self.popup2 = QtGui.QComboBox(self.group22)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(" ---- Design ----"))
			self.popup2.setFixedWidth(120)
			self.popup2.activated[str].connect(self.onPopupDes22)
			self.popup2.move(160,80)

			self.group22.show()

	def onPopupImg1(self):
		if self.popup1.currentText() == u"축 - 29cm":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/shaft/18.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"축 - 14cm":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/shaft/19.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"축 - 10cm":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/shaft/20.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"축 - 9cm":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/shaft/21.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"축 - 7.5cm":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/shaft/23.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"축 - 6.5cm":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/shaft/22.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"축 - 5cm":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/shaft/24.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"축 - 4cm":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/shaft/25.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"십자축 - 5cm":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/shaft/137.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
	def onPopupImg2(self):
		if self.popup1.currentText() == u"상자형베어링":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/bearing/76.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"베어링뭉치(상)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/bearing/77.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"베어링뭉치(가이드)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/bearing/78.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"베어링뭉치(하)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/bearing/79.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

	def onPopupImg3(self):
		if self.popup1.currentText() == u"앵글 - 25":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/angle/6.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"앵글 - 19":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/angle/7.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"앵글 - 11":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/angle/8.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() ==  u"앵글 - 9":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/angle/9.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"앵글 - 7":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/angle/10.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"앵글 - 3":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/angle/11.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"앵글 - 2":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/angle/132.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

	def onPopupImg4(self):
		if self.popup1.currentText() == u"플라스틱판 11X5":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/plastic plate/85.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"플라스틱판 11X3":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/plastic plate/80.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"플라스틱판 7X5":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/plastic plate/81.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"플라스틱판 5X5":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/plastic plate/82.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"플라스틱판 5X3":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/plastic plate/83.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"삼각플라스틱판":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/plastic plate/102.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"반원플라스틱판":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/plastic plate/103.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

	def onPopupImg5(self):
		if self.popup1.currentText() == u"스트립 - 25":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/strip/127.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"스트립 - 15":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/strip/1.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"스트립 - 11":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/strip/2.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"스트립 - 9":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/strip/3.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"스트립 - 5":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/strip/4.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"좁은스트립 - 9":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/strip/92.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"좁은스트립 - 7":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/strip/91.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"좁은스트립 - 6":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/strip/90.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"좁은스트립 - 5":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/strip/89.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"좁은스트립 - 3":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/strip/93.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"스트립 - 5(s)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/strip/5.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() ==  u"ㄷ형스트립 - 3":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러
			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/strip/47.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"ㄷ형스트립 - 5":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러
			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/strip/48.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"ㄷ형스트립 - 7":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/strip/49.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"원형스트립":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/strip/59.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() ==  u"곡면스트립":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/strip/88.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"트러스스트립":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/strip/128.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

	def onPopupImg6(self):
		if self.popup1.currentText() == u"플랜지판(소)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/plange plate/50.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"플랜지판(대)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/plange plate/51.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"사다리꼴플랜지판":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/plange plate/109.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"플랜지판 2X5":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/plange plate/168.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"플랜지판 2X7":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/plange plate/169.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
	def onPopupImg7(self):
		if self.popup1.currentText() == u"평판(대)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/flat plate/55.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"평판(소)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/flat plate/56.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"평판 - 9":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/flat plate/60.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"평판 - 7":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/flat plate/61.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"평판 - 5":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/flat plate/62.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"평판 - 3":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/flat plate/63.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"오각평판":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/flat plate/71.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"사각평판 3X5":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/flat plate/129.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"삼각평판 3X5":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/flat plate/130.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"바퀴평판":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/flat plate/131.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
	def onPopupImg8(self):
		if self.popup1.currentText() == u"역각브래킷":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/bracket/70.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"ㄷ형 브래킷(소)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/bracket/13.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"ㄷ형 브래킷(대)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/bracket/14.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"ㄱ형 브래킷(소)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/bracket/15.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"ㄱ형 브래킷(대)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/bracket/16.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"ㄱ형 브래킷 2X2":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/bracket/16A.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"둔각브래킷":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/bracket/17.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"삼각브래킷":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/bracket/72.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"모서리브래킷(좌)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/bracket/74.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"모서리브래킷(우)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/bracket/75.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"조향브래킷":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/bracket/133.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
	def onPopupImg9(self):
		if self.popup1.currentText() == u"이음판":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc plate/12.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"휠판 - 8":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc plate/30.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"반원판":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc plate/87.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
	def onPopupImg10(self):
		if self.popup1.currentText() == u"볼트 0.6cm":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/bolt/41.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"볼트 1.3cm":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/bolt/65.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"볼트 2cm":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/bolt/66.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"볼트 3cm":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/bolt/67.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"사각머리볼트 0.8cm":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/bolt/177.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
	def onPopupImg11(self):
		if self.popup1.currentText() == u"너트":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/nut/42.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
	def onPopupImg12(self):
		if self.popup1.currentText() == u"와셔(소)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/washer/43.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"와셔(대)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/washer/44.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
	def onPopupImg13(self):
		if self.popup1.currentText() == u"멈춤나사":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/screw/54.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"구동기어 멈춤나사":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/screw/54A.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
	def onPopupImg14(self):
		if self.popup1.currentText() == u"평기어(소)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/gear/33.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"피니언기어":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/gear/32.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"평기어(대)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/gear/34.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"다목적기어":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/gear/35.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"크라운기어":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/gear/36.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"워엄기어":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/gear/37.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"체인기어(소)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/gear/105.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"체인기어(대)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/gear/106.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"2단 평기어(소)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/gear/140.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"2단 평기어(대)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/gear/141.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"십자홀 2단평기어":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/gear/141.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"십자홀 체인기어":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/gear/143.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
	def onPopupImg15(self):
		if self.popup1.currentText() == u"체인":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/chain/104.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"링크체인":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/chain/104A.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
	def onPopupImg16(self):
		if self.popup1.currentText() == u"풀리(대)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/pulley/26.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"풀리(중)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/pulley/27.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"풀리(소)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/pulley/28.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"타이어풀리":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/pulley/29.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"2단 풀리":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/pulley/144.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"피니언풀리":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/pulley/145.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
	def onPopupImg17(self):
		if self.popup1.currentText() == u"래크":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/rack/108.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"래크홀더":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/rack/148.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
	def onPopupImg18(self):
		if self.popup1.currentText() == u"십자홀 피니언":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/pinion/142.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

	def onPopupImg19(self):
		if self.popup1.currentText() == u"타이어(소)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/tire/94.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"타이어(중)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/tire/107.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"타이어(대)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/tire/151.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"타이어(특대)":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/tire/152.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

	def onPopupImg20(self):
		if self.popup1.currentText() == u"나사봉 - 5cm":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/nasa/58.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"나사봉 - 7.5cm":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/nasa/57.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

	def onPopupImg21(self):
		if self.popup1.currentText() == u"조정부싱":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/busing/52.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"축연결부싱":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/busing/112.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"사각홀고무부싱":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/busing/138.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"플라스틱부싱 0.6cm":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/busing/139.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"플라스틱부싱 1.2cm":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/busing/139A.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"실리콘부싱 0.6cm":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/busing/161.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()


	def onPopupImg22(self):
		if self.popup1.currentText() == u"스프링클립":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/39.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"지지판":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/46.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"양팔크랭크":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/53.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"면판휠":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/64.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"나사핀":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/68.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"프로펠러":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/69.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"훅":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/73.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"파워핸들":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/77.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"축이음쇠":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/86.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"모터뭉치":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/97.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"구동기어뭉치":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/100.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"기어드모터":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/100A.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"이동클립":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/111.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
		elif self.popup1.currentText() == u"캐노피":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/147.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"홈샤프트":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/167.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()

		elif self.popup1.currentText() == u"홈샤프트캡":
			ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

			buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/etc/171.jpg"))

			Imageview1 = QtGui.QLabel(ks)
			Imageview1.setPixmap(buf)
			Imageview1.resize(buf.width(), buf.height())
			Imageview1.move(0,0)
			Imageview1.show()

			#ks.setGeometry(580,100,610,805)
			ks.setWindowTitle("Image")
			ks.move(630,220)
			ks.show()
			ks.exec_()
	def onPopupDes1(self):
		if self.popup2.currentText() == u"축 - 29cm":
			doc=App.newDocument()

			r = 4
			l = 294

			v1=Base.Vector(0,r/2,0)
			v2=Base.Vector(-r/2,0,0)
			v3=Base.Vector(0,-r/2,0)
			v4=Base.Vector(r/2,0,0)

			C1=Part.Arc(v1,v2,v3)
			C2=Part.Arc(v3,v4,v1)

			S1=Part.Shape([C1,C2])

			W=Part.Wire(S1.Edges)
			face=Part.Face(W)
			P=face.extrude(Base.Vector(0,0,l))

			shape=doc.addObject("Part::Feature")
			shape.Shape=P
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

		elif self.popup2.currentText() == u"축 - 14cm":
			doc=App.newDocument()

			r = 4
			l = 140

			v1=Base.Vector(0,r/2,0)
			v2=Base.Vector(-r/2,0,0)
			v3=Base.Vector(0,-r/2,0)
			v4=Base.Vector(r/2,0,0)

			C1=Part.Arc(v1,v2,v3)
			C2=Part.Arc(v3,v4,v1)

			S1=Part.Shape([C1,C2])

			W=Part.Wire(S1.Edges)
			face=Part.Face(W)
			P=face.extrude(Base.Vector(0,0,l))

			shape=doc.addObject("Part::Feature")
			shape.Shape=P
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

		elif self.popup2.currentText() == u"축 - 10cm":
			doc=App.newDocument()

			r = 4
			l = 102

			v1=Base.Vector(0,r/2,0)
			v2=Base.Vector(-r/2,0,0)
			v3=Base.Vector(0,-r/2,0)
			v4=Base.Vector(r/2,0,0)

			C1=Part.Arc(v1,v2,v3)
			C2=Part.Arc(v3,v4,v1)

			S1=Part.Shape([C1,C2])

			W=Part.Wire(S1.Edges)
			face=Part.Face(W)
			P=face.extrude(Base.Vector(0,0,l))

			shape=doc.addObject("Part::Feature")
			shape.Shape=P
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

		elif self.popup2.currentText() == u"축 - 9cm":
			doc=App.newDocument()

			r = 4
			l = 90

			v1=Base.Vector(0,r/2,0)
			v2=Base.Vector(-r/2,0,0)
			v3=Base.Vector(0,-r/2,0)
			v4=Base.Vector(r/2,0,0)

			C1=Part.Arc(v1,v2,v3)
			C2=Part.Arc(v3,v4,v1)

			S1=Part.Shape([C1,C2])

			W=Part.Wire(S1.Edges)
			face=Part.Face(W)
			P=face.extrude(Base.Vector(0,0,l))

			shape=doc.addObject("Part::Feature")
			shape.Shape=P
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

		elif self.popup2.currentText() == u"축 - 7.5cm":
			doc=App.newDocument()

			r = 4
			l = 75

			v1=Base.Vector(0,r/2,0)
			v2=Base.Vector(-r/2,0,0)
			v3=Base.Vector(0,-r/2,0)
			v4=Base.Vector(r/2,0,0)

			C1=Part.Arc(v1,v2,v3)
			C2=Part.Arc(v3,v4,v1)

			S1=Part.Shape([C1,C2])

			W=Part.Wire(S1.Edges)
			face=Part.Face(W)
			P=face.extrude(Base.Vector(0,0,l))

			shape=doc.addObject("Part::Feature")
			shape.Shape=P
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

		elif self.popup2.currentText() == u"축 - 6.5cm":
			doc=App.newDocument()

			r = 4
			l = 65

			v1=Base.Vector(0,r/2,0)
			v2=Base.Vector(-r/2,0,0)
			v3=Base.Vector(0,-r/2,0)
			v4=Base.Vector(r/2,0,0)

			C1=Part.Arc(v1,v2,v3)
			C2=Part.Arc(v3,v4,v1)

			S1=Part.Shape([C1,C2])

			W=Part.Wire(S1.Edges)
			face=Part.Face(W)
			P=face.extrude(Base.Vector(0,0,l))

			shape=doc.addObject("Part::Feature")
			shape.Shape=P
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

		elif self.popup2.currentText() == u"축 - 5cm":
			doc=App.newDocument()

			r = 4
			l = 51

			v1=Base.Vector(0,r/2,0)
			v2=Base.Vector(-r/2,0,0)
			v3=Base.Vector(0,-r/2,0)
			v4=Base.Vector(r/2,0,0)

			C1=Part.Arc(v1,v2,v3)
			C2=Part.Arc(v3,v4,v1)

			S1=Part.Shape([C1,C2])

			W=Part.Wire(S1.Edges)
			face=Part.Face(W)
			P=face.extrude(Base.Vector(0,0,l))

			shape=doc.addObject("Part::Feature")
			shape.Shape=P
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

		elif self.popup2.currentText() == u"축 - 4cm":
			doc=App.newDocument()

			r = 4
			l = 40

			v1=Base.Vector(0,r/2,0)
			v2=Base.Vector(-r/2,0,0)
			v3=Base.Vector(0,-r/2,0)
			v4=Base.Vector(r/2,0,0)

			C1=Part.Arc(v1,v2,v3)
			C2=Part.Arc(v3,v4,v1)

			S1=Part.Shape([C1,C2])

			W=Part.Wire(S1.Edges)
			face=Part.Face(W)
			P=face.extrude(Base.Vector(0,0,l))

			shape=doc.addObject("Part::Feature")
			shape.Shape=P
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"십자축 - 5cm":
			doc=App.newDocument()

			plate1 = Part.makeCylinder(1.98, 54, Vector(0,0,0))
			box1 = Part.makeBox(1.92,5.24,54,Vector(-0.96,-2.62,0))
			plate1 = plate1.fuse(box1)
			box2 = Part.makeBox(1.92,5.24,54,Vector(-0.96,-2.62,0))
			box2.rotate(Vector(0,0,0),Vector(0,0,1),90)
			plate1 = plate1.fuse(box2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

	def onPopupDes2(self):
		if self.popup2.currentText() == u"상자형베어링":
			doc=App.newDocument()

			l = 37.53
			w = 14.17
			h = 26.62
			t = 0.71
			d = 4.15
			n = 3
			f = 6.07

			plate1 = Part.makeBox(l,h,w,Vector(0,0,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(f, [plate1.Edges[2],plate1.Edges[6]])

			cir = []
			cir.append(Part.makeCylinder(d/2,w,Vector(4.1+d/2,5.06,0)))
			cir.append(Part.makeCylinder(d/2,w,Vector(4.1+d/2,17.84,0)))
			cir.append(Part.makeCylinder(d/2,w,Vector(16.63+d/2,5.06,0)))
			cir.append(Part.makeCylinder(d/2,w,Vector(16.63+d/2,17.84,0)))
			cir.append(Part.makeCylinder(d/2,w,Vector(29.29+d/2,5.06,0)))
			cir.append(Part.makeCylinder(d/2,w,Vector(29.29+d/2,17.84,0)))
			cir.append(Part.makeCylinder(d/2,h,Vector(4.1+d/2,0,4.96+d/2),Vector(0,1,0)))
			cir.append(Part.makeCylinder(d/2,h,Vector(16.63+d/2,0,4.96+d/2),Vector(0,1,0)))
			cir.append(Part.makeCylinder(d/2,h,Vector(29.29+d/2,0,4.96+d/2),Vector(0,1,0)))

			for i in cir:
				plate1 = plate1.cut(i)

			plate2 = Part.makeBox(l,h-0.7,w-1.4,Vector(0,0.7,0.7),Vector(0,0,1))
			plate1 = plate1.cut(plate2)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

		elif self.popup2.currentText() == u"베어링뭉치(상)":
			doc=App.newDocument()

			D = 41.77
			D1 = 59.59
			D2 = 57.57
			D3 = 53.63
			D4 = 46.60
			D5 = 37.53
			x = 0.9
			D6 = 12.60
			D7 = 8.36
			t = 1
			t1 = 2.57
			t2 = 5.73

			d = 4.11
			i = 0
			j = 0
			n = 2



			circle = Part.makeCylinder(D1/2,t1,Vector(0,0,t))

			#Front
			circle1 = Part.makeCylinder(D/2,t2-t1,Vector(0,0,t1))
			circle = circle.fuse(circle1)

			#Back
			circle_1 = Part.makeCylinder(D2/2,t,Vector(0,0,0))
			circle_2 = Part.makeCylinder(D3/2,t,Vector(0,0,0))
			circle_3 = Part.makeCylinder(D4/2,t,Vector(0,0,0))
			circle_4 = Part.makeCylinder(D5/2,t1-1,Vector(0,0,0))
			box_1 = Part.makeBox(x,D5,t1-1,Vector(-x/2,-D5/2,0))
			box_2 = Part.makeBox(D5,x,t1-1,Vector(-D5/2,-x/2,0))
			box_3 = Part.makeBox(D5,t1-1,x,Vector(-D5/2/1.414-0.3,D5/2/1.414-0.3,t1-1),Vector(1,1,0))
			box_4 = Part.makeBox(D5,t1-1,x,Vector(-D5/2/1.414+0.3,-D5/2/1.414-0.3,t1-1),Vector(-1,1,0))
			circle_5 = Part.makeCylinder(D6/2,t1-1,Vector(0,0,0))
			circle_6 = Part.makeCylinder(D7/2,t1-1,Vector(0,0,0))
			circle = circle.fuse(circle_1)
			circle = circle.cut(circle_2)
			circle = circle.fuse(circle_3)
			circle = circle.cut(circle_4)
			circle = circle.fuse(box_1)
			circle = circle.fuse(box_2)
			circle = circle.fuse(box_3)
			circle = circle.fuse(box_4)
			circle = circle.cut(circle_5)
			circle = circle.fuse(circle_5)
			circle = circle.cut(circle_6)

			x = 4.11
			y = 11.04



			#Hole
			cir = Part.makeCylinder(d/2,t2,Vector(0,0,0))
			cir1 = []
			cir2 = []
			for i in range(n):
				for j in range(n):
					cir1.append(Part.makeCylinder(d/2,t2,Vector(x-2*x*i,y-2*y*j,0)))
					cir2.append(Part.makeCylinder(d/2,t2,Vector(y-2*y*i,x-2*x*j,0)))
			for i in cir1:
				circle = circle.cut(i)
			for i in cir2:
				circle = circle.cut(i)

			#for i in range(n):
			#	for j in range(n):
			#		cir4.append(Part.makeCylinder(d/2,t,Vector((14-d)/2-(14-d)*j,(27.7-d)/2-(27.7-d)*i,0)))
			#
			#for i in cir4:
			#	circle = circle.cut(i)

			circle = circle.cut(cir)


			#Part.show(circle)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

		elif self.popup2.currentText() == u"베어링뭉치(가이드)":
			doc=App.newDocument()

			#D = 41.77
			D1 = 59.53
			D2 = 57.17
			D3 = 7.97
			d = 4.11
			d1 = 2.81
			x = 15.95
			t = 6.8
			t1 = 2
			t2 = 10.12

			circle = Part.makeCylinder(D1/2,t,Vector(0,0,0))
			circle1 = Part.makeCylinder(D2/2,t1,Vector(0,0,t-t1))
			circle2 = Part.makeCylinder(D2/2,t1,Vector(0,0,0))
			circle3 = Part.makeCylinder(D3/2,t2,Vector(0,0,t/2-t2/2))
			circle4 = Part.makeCylinder(d/2,t2,Vector(0,0,t/2-t2/2))
			circle5 = Part.makeCylinder(d1/2,t-2*t1,Vector(x,0,t1))
			circle6 = Part.makeCylinder(d1/2,t-2*t1,Vector(-x,0,t1))
			circle = circle.cut(circle1)
			circle = circle.cut(circle2)
			circle = circle.fuse(circle3)
			circle = circle.cut(circle4)
			circle = circle.cut(circle5)
			circle = circle.cut(circle6)

			#Part.show(circle)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

		elif self.popup2.currentText() == u"베어링뭉치(하)":

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=0.678, z=95, alpha=20 * pi / 180., clearence=0, shift=0., beta=0., undercut=False, simple=False, height=3.6, backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                H = 3.6

			                #Front
			                h1 = 1
			                D1 = 57.51
			                D2 = 53.16
			                D3 = 46.97
			                D4 = 37.43
			                D5 = 12.60
			                D6 = 8.36
			                x = 0.9
			                self.cir_f1 = Part.makeCylinder(D1/2,h1,Vector(0,0,H))
			                self.cir_f2 = Part.makeCylinder(D2/2,h1,Vector(0,0,H))
			                self.cir_f3 = Part.makeCylinder(D3/2,h1,Vector(0,0,H))
			                self.cir_f4 = Part.makeCylinder(D4/2,H,Vector(0,0,1))
			                self.Shape = self.Shape.fuse(self.cir_f1)
			                self.Shape = self.Shape.cut(self.cir_f2)
			                self.Shape = self.Shape.fuse(self.cir_f3)
			                self.Shape = self.Shape.cut(self.cir_f4)
			                self.box_f1 = Part.makeBox(x,D4,H,Vector(-x/2,-D4/2,1))
			                self.box_f2 = Part.makeBox(D4,x,H,Vector(-D4/2,-x/2,1))
			                self.box_f3 = Part.makeBox(D4,H,x,Vector(-D4/2+5.424,D4/2-5.424,H+h1),Vector(1,1,0))
			                self.box_f4 = Part.makeBox(D4,H,x,Vector(-D4/2+5.424,-D4/2+5.424,H+h1),Vector(-1,1,0))
			                self.Shape = self.Shape.fuse(self.box_f1)
			                self.Shape = self.Shape.fuse(self.box_f2)
			                self.Shape = self.Shape.fuse(self.box_f3)
			                self.Shape = self.Shape.fuse(self.box_f4)
			                self.cir_f5 = Part.makeCylinder(D5/2,H,Vector(0,0,1))
			                self.cir_f6 = Part.makeCylinder(D6/2,H,Vector(0,0,1))
			                self.Shape = self.Shape.cut(self.cir_f5)
			                self.Shape = self.Shape.fuse(self.cir_f5)
			                self.Shape = self.Shape.cut(self.cir_f6)

			                #Back
			                D_1 = 59.7
			                D_2 = 42.22
			                h_1 = 5.63
			                self.cir_b1 = Part.makeCylinder(D_1/2,h_1-H,Vector(0,0,0))
			                self.cir_b2 = Part.makeCylinder(D_2/2,h_1-H+1,Vector(0,0,-1))
			                self.Shape = self.Shape.cut(self.cir_b1)
			                self.Shape = self.Shape.fuse(self.cir_b2)

			                #Hole
			                hx = 4.11
			                hy = 11.04
			                d = 4.11
			                self.cir_h = Part.makeCylinder(d/2,h_1,Vector(0,0,-1))
			                self.cir_h1 = Part.makeCylinder(d/2,h_1,Vector(hx,hy,-1))
			                self.cir_h2 = Part.makeCylinder(d/2,h_1,Vector(-hx,hy,-1))
			                self.cir_h3 = Part.makeCylinder(d/2,h_1,Vector(-hx,-hy,-1))
			                self.cir_h4 = Part.makeCylinder(d/2,h_1,Vector(hx,-hy,-1))
			                self.cir_h5 = Part.makeCylinder(d/2,h_1,Vector(hy,hx,-1))
			                self.cir_h6 = Part.makeCylinder(d/2,h_1,Vector(-hy,hx,-1))
			                self.cir_h7 = Part.makeCylinder(d/2,h_1,Vector(-hy,-hx,-1))
			                self.cir_h8 = Part.makeCylinder(d/2,h_1,Vector(hy,-hx,-1))
			                self.Shape = self.Shape.cut(self.cir_h)
			                self.Shape = self.Shape.cut(self.cir_h1)
			                self.Shape = self.Shape.cut(self.cir_h2)
			                self.Shape = self.Shape.cut(self.cir_h3)
			                self.Shape = self.Shape.cut(self.cir_h4)
			                self.Shape = self.Shape.cut(self.cir_h5)
			                self.Shape = self.Shape.cut(self.cir_h6)
			                self.Shape = self.Shape.cut(self.cir_h7)
			                self.Shape = self.Shape.cut(self.cir_h8)


			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])


			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()
			Gui.SendMsgToActiveView("ViewFit")

	def onPopupDes3(self):
		if self.popup2.currentText() == u"앵글 - 25":
			doc=App.newDocument()

			l = 318
			w = 15.0
			h = 13.5
			t = 0.7
			d = 4.11
			n = 25
			b = n-1

			box = []
			cir = []
			mir = []
			hole = []
			plate1 = Part.makeBox(l,w,t,Vector(0,-w,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(w/2, [plate1.Edges[0],plate1.Edges[4]])
			box1 = Part.makeBox(d,5,t,Vector(6-d/2,-10,0))
			box2 = Part.makeBox(d,5,t,Vector(6+l-12.0-d/2,-10,0))
			cir1 = Part.makeCylinder(d/2,t,Vector(6,-10,0))
			mir1 = Part.makeCylinder(d/2,t,Vector(6,-5,0))
			cir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-10,0))
			mir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-5,0))
			for i in range(1,b):
				box.append(Part.makeBox(d,5,t,Vector(6+(l-12.0)/b*i-d/2,-10,0)))
				cir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-10,0)))
				mir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-5,0)))

			plate1 = plate1.cut(box1)
			plate1 = plate1.cut(box2)
			plate1 = plate1.cut(cir1)
			plate1 = plate1.cut(mir1)
			plate1 = plate1.cut(cir2)
			plate1 = plate1.cut(mir2)

			#print(len(box))
			#print(list(range(1,b)))
			#print(box[22])
			for i in box:
				plate1 = plate1.cut(i)
			for i in cir:
				plate1 = plate1.cut(i)
			for i in mir:
				plate1 = plate1.cut(i)

			plate2 = Part.makeBox(l,t,h-t,Vector(0,-t,t))
			plate2 = plate2.makeFillet(h/2, [plate2.Edges[1],plate2.Edges[5]])
			hole1 = Part.makeCylinder(d/2,t,Vector(6,-t,7),Vector(0,1,0))
			hole2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-t,7),Vector(0,1,0))
			for i in range(1,b):
				hole.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-t,7),Vector(0,1,0)))

			plate2 = plate2.cut(hole1)
			plate2 = plate2.cut(hole2)
			for i in hole:
				plate2 = plate2.cut(i)

			plate1 = plate1.fuse(plate2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"앵글 - 19":
			doc=App.newDocument()

			l = 241
			w = 15.0
			h = 13.5
			t = 0.7
			d = 4.11
			n = 19
			b = n-1

			box = []
			cir = []
			mir = []
			hole = []
			plate1 = Part.makeBox(l,w,t,Vector(0,-w,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(w/2, [plate1.Edges[0],plate1.Edges[4]])
			box1 = Part.makeBox(d,5,t,Vector(6-d/2,-10,0))
			box2 = Part.makeBox(d,5,t,Vector(6+l-12.0-d/2,-10,0))
			cir1 = Part.makeCylinder(d/2,t,Vector(6,-10,0))
			mir1 = Part.makeCylinder(d/2,t,Vector(6,-5,0))
			cir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-10,0))
			mir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-5,0))
			for i in range(1,b):
				box.append(Part.makeBox(d,5,t,Vector(6+(l-12.0)/b*i-d/2,-10,0)))
				cir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-10,0)))
				mir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-5,0)))

			plate1 = plate1.cut(box1)
			plate1 = plate1.cut(box2)
			plate1 = plate1.cut(cir1)
			plate1 = plate1.cut(mir1)
			plate1 = plate1.cut(cir2)
			plate1 = plate1.cut(mir2)

			#print(len(box))
			#print(list(range(1,b)))
			#print(box[22])
			for i in box:
				plate1 = plate1.cut(i)
			for i in cir:
				plate1 = plate1.cut(i)
			for i in mir:
				plate1 = plate1.cut(i)

			plate2 = Part.makeBox(l,t,h-t,Vector(0,-t,t))
			plate2 = plate2.makeFillet(h/2, [plate2.Edges[1],plate2.Edges[5]])
			hole1 = Part.makeCylinder(d/2,t,Vector(6,-t,7),Vector(0,1,0))
			hole2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-t,7),Vector(0,1,0))
			for i in range(1,b):
				hole.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-t,7),Vector(0,1,0)))

			plate2 = plate2.cut(hole1)
			plate2 = plate2.cut(hole2)
			for i in hole:
				plate2 = plate2.cut(i)

			plate1 = plate1.fuse(plate2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"앵글 - 11":
			doc=App.newDocument()

			l = 139
			w = 15.0
			h = 13.5
			t = 0.7
			d = 4.11
			n = 11
			b = n-1

			box = []
			cir = []
			mir = []
			hole = []
			plate1 = Part.makeBox(l,w,t,Vector(0,-w,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(w/2, [plate1.Edges[0],plate1.Edges[4]])
			box1 = Part.makeBox(d,5,t,Vector(6-d/2,-10,0))
			box2 = Part.makeBox(d,5,t,Vector(6+l-12.0-d/2,-10,0))
			cir1 = Part.makeCylinder(d/2,t,Vector(6,-10,0))
			mir1 = Part.makeCylinder(d/2,t,Vector(6,-5,0))
			cir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-10,0))
			mir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-5,0))
			for i in range(1,b):
				box.append(Part.makeBox(d,5,t,Vector(6+(l-12.0)/b*i-d/2,-10,0)))
				cir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-10,0)))
				mir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-5,0)))

			plate1 = plate1.cut(box1)
			plate1 = plate1.cut(box2)
			plate1 = plate1.cut(cir1)
			plate1 = plate1.cut(mir1)
			plate1 = plate1.cut(cir2)
			plate1 = plate1.cut(mir2)

			#print(len(box))
			#print(list(range(1,b)))
			#print(box[22])
			for i in box:
				plate1 = plate1.cut(i)
			for i in cir:
				plate1 = plate1.cut(i)
			for i in mir:
				plate1 = plate1.cut(i)

			plate2 = Part.makeBox(l,t,h-t,Vector(0,-t,t))
			plate2 = plate2.makeFillet(h/2, [plate2.Edges[1],plate2.Edges[5]])
			hole1 = Part.makeCylinder(d/2,t,Vector(6,-t,7),Vector(0,1,0))
			hole2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-t,7),Vector(0,1,0))
			for i in range(1,b):
				hole.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-t,7),Vector(0,1,0)))

			plate2 = plate2.cut(hole1)
			plate2 = plate2.cut(hole2)
			for i in hole:
				plate2 = plate2.cut(i)

			plate1 = plate1.fuse(plate2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"앵글 - 9":
			doc=App.newDocument()

			l = 113.6
			w = 15.0
			h = 13.5
			t = 0.7
			d = 4.11
			n = 9
			b = n-1

			box = []
			cir = []
			mir = []
			hole = []
			plate1 = Part.makeBox(l,w,t,Vector(0,-w,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(w/2, [plate1.Edges[0],plate1.Edges[4]])
			box1 = Part.makeBox(d,5,t,Vector(6-d/2,-10,0))
			box2 = Part.makeBox(d,5,t,Vector(6+l-12.0-d/2,-10,0))
			cir1 = Part.makeCylinder(d/2,t,Vector(6,-10,0))
			mir1 = Part.makeCylinder(d/2,t,Vector(6,-5,0))
			cir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-10,0))
			mir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-5,0))
			for i in range(1,b):
				box.append(Part.makeBox(d,5,t,Vector(6+(l-12.0)/b*i-d/2,-10,0)))
				cir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-10,0)))
				mir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-5,0)))

			plate1 = plate1.cut(box1)
			plate1 = plate1.cut(box2)
			plate1 = plate1.cut(cir1)
			plate1 = plate1.cut(mir1)
			plate1 = plate1.cut(cir2)
			plate1 = plate1.cut(mir2)

			#print(len(box))
			#print(list(range(1,b)))
			#print(box[22])
			for i in box:
				plate1 = plate1.cut(i)
			for i in cir:
				plate1 = plate1.cut(i)
			for i in mir:
				plate1 = plate1.cut(i)

			plate2 = Part.makeBox(l,t,h-t,Vector(0,-t,t))
			plate2 = plate2.makeFillet(h/2, [plate2.Edges[1],plate2.Edges[5]])
			hole1 = Part.makeCylinder(d/2,t,Vector(6,-t,7),Vector(0,1,0))
			hole2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-t,7),Vector(0,1,0))
			for i in range(1,b):
				hole.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-t,7),Vector(0,1,0)))

			plate2 = plate2.cut(hole1)
			plate2 = plate2.cut(hole2)
			for i in hole:
				plate2 = plate2.cut(i)

			plate1 = plate1.fuse(plate2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"앵글 - 7":
			doc=App.newDocument()

			l = 88.2
			w = 15.0
			h = 13.5
			t = 0.7
			d = 4.11
			n = 7
			b = n-1

			box = []
			cir = []
			mir = []
			hole = []
			plate1 = Part.makeBox(l,w,t,Vector(0,-w,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(w/2, [plate1.Edges[0],plate1.Edges[4]])
			box1 = Part.makeBox(d,5,t,Vector(6-d/2,-10,0))
			box2 = Part.makeBox(d,5,t,Vector(6+l-12.0-d/2,-10,0))
			cir1 = Part.makeCylinder(d/2,t,Vector(6,-10,0))
			mir1 = Part.makeCylinder(d/2,t,Vector(6,-5,0))
			cir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-10,0))
			mir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-5,0))
			for i in range(1,b):
				box.append(Part.makeBox(d,5,t,Vector(6+(l-12.0)/b*i-d/2,-10,0)))
				cir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-10,0)))
				mir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-5,0)))

			plate1 = plate1.cut(box1)
			plate1 = plate1.cut(box2)
			plate1 = plate1.cut(cir1)
			plate1 = plate1.cut(mir1)
			plate1 = plate1.cut(cir2)
			plate1 = plate1.cut(mir2)

			#print(len(box))
			#print(list(range(1,b)))
			#print(box[22])
			for i in box:
				plate1 = plate1.cut(i)
			for i in cir:
				plate1 = plate1.cut(i)
			for i in mir:
				plate1 = plate1.cut(i)

			plate2 = Part.makeBox(l,t,h-t,Vector(0,-t,t))
			plate2 = plate2.makeFillet(h/2, [plate2.Edges[1],plate2.Edges[5]])
			hole1 = Part.makeCylinder(d/2,t,Vector(6,-t,7),Vector(0,1,0))
			hole2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-t,7),Vector(0,1,0))
			for i in range(1,b):
				hole.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-t,7),Vector(0,1,0)))

			plate2 = plate2.cut(hole1)
			plate2 = plate2.cut(hole2)
			for i in hole:
				plate2 = plate2.cut(i)

			plate1 = plate1.fuse(plate2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"앵글 - 3":
			doc=App.newDocument()

			l = 37.4
			w = 15.0
			h = 13.5
			t = 0.7
			d = 4.11
			n = 3
			b = n-1

			box = []
			cir = []
			mir = []
			hole = []
			plate1 = Part.makeBox(l,w,t,Vector(0,-w,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(w/2, [plate1.Edges[0],plate1.Edges[4]])
			box1 = Part.makeBox(d,5,t,Vector(6-d/2,-10,0))
			box2 = Part.makeBox(d,5,t,Vector(6+l-12.0-d/2,-10,0))
			cir1 = Part.makeCylinder(d/2,t,Vector(6,-10,0))
			mir1 = Part.makeCylinder(d/2,t,Vector(6,-5,0))
			cir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-10,0))
			mir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-5,0))
			for i in range(1,b):
				box.append(Part.makeBox(d,5,t,Vector(6+(l-12.0)/b*i-d/2,-10,0)))
				cir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-10,0)))
				mir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-5,0)))

			plate1 = plate1.cut(box1)
			plate1 = plate1.cut(box2)
			plate1 = plate1.cut(cir1)
			plate1 = plate1.cut(mir1)
			plate1 = plate1.cut(cir2)
			plate1 = plate1.cut(mir2)

			#print(len(box))
			#print(list(range(1,b)))
			#print(box[22])
			for i in box:
				plate1 = plate1.cut(i)
			for i in cir:
				plate1 = plate1.cut(i)
			for i in mir:
				plate1 = plate1.cut(i)

			plate2 = Part.makeBox(l,t,h-t,Vector(0,-t,t))
			plate2 = plate2.makeFillet(h/2, [plate2.Edges[1],plate2.Edges[5]])
			hole1 = Part.makeCylinder(d/2,t,Vector(6,-t,7),Vector(0,1,0))
			hole2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-t,7),Vector(0,1,0))
			for i in range(1,b):
				hole.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-t,7),Vector(0,1,0)))

			plate2 = plate2.cut(hole1)
			plate2 = plate2.cut(hole2)
			for i in hole:
				plate2 = plate2.cut(i)

			plate1 = plate1.fuse(plate2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"앵글 - 2":
			doc=App.newDocument()

			l = 24.7
			w = 15.0
			h = 13.5
			t = 0.7
			d = 4.11
			n = 2
			b = n-1

			box = []
			cir = []
			mir = []
			hole = []
			plate1 = Part.makeBox(l,w,t,Vector(0,-w,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(w/2, [plate1.Edges[0],plate1.Edges[4]])
			box1 = Part.makeBox(d,5,t,Vector(6-d/2,-10,0))
			box2 = Part.makeBox(d,5,t,Vector(6+l-12.0-d/2,-10,0))
			cir1 = Part.makeCylinder(d/2,t,Vector(6,-10,0))
			mir1 = Part.makeCylinder(d/2,t,Vector(6,-5,0))
			cir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-10,0))
			mir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-5,0))
			for i in range(1,b):
				box.append(Part.makeBox(d,5,t,Vector(6+(l-12.0)/b*i-d/2,-10,0)))
				cir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-10,0)))
				mir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-5,0)))

			plate1 = plate1.cut(box1)
			plate1 = plate1.cut(box2)
			plate1 = plate1.cut(cir1)
			plate1 = plate1.cut(mir1)
			plate1 = plate1.cut(cir2)
			plate1 = plate1.cut(mir2)

			#print(len(box))
			#print(list(range(1,b)))
			#print(box[22])
			for i in box:
				plate1 = plate1.cut(i)
			for i in cir:
				plate1 = plate1.cut(i)
			for i in mir:
				plate1 = plate1.cut(i)

			plate2 = Part.makeBox(l,t,h-t,Vector(0,-t,t))
			plate2 = plate2.makeFillet(h/2, [plate2.Edges[1],plate2.Edges[5]])
			hole1 = Part.makeCylinder(d/2,t,Vector(6,-t,7),Vector(0,1,0))
			hole2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-t,7),Vector(0,1,0))
			for i in range(1,b):
				hole.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-t,7),Vector(0,1,0)))

			plate2 = plate2.cut(hole1)
			plate2 = plate2.cut(hole2)
			for i in hole:
				plate2 = plate2.cut(i)

			plate1 = plate1.fuse(plate2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
	def onPopupDes4(self):
		if self.popup2.currentText() == u"플라스틱판 7X5":
			doc=App.newDocument()

			x = 89
			y = 63.6
			r = 6.4
			t = 0.41
			d = 4.2
			n = 7
			m = 5
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5
			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(r, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			hole1 = Part.makeCylinder(d/2,t,Vector(x/2,-y/2,0))
			hole_up = []
			hole_down = []
			for i in range(n):
				hole_up.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-25-y/2,0)))
				hole_down.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,25-y/2,0)))
			plate1 = plate1.cut(hole1)
			for i in hole_up:
				plate1 = plate1.cut(i)
			for i in hole_down:
				plate1 = plate1.cut(i)

			left = []
			right = []
			box = []
			left2 = []
			right2 = []
			box2 = []
			for i in range(m):
				box.append(Part.makeBox(5,d,t,Vector(4.5,-cc-a*i-d/2,0)))
				left.append(Part.makeCylinder(d/2,t,Vector(bb-2.5,-cc-a*i,0)))
				right.append(Part.makeCylinder(d/2,t,Vector(bb+2.5,-cc-a*i,0)))
			for i in range(m):
				box2.append(Part.makeBox(5,d,t,Vector(x-bb-2.5,-cc-a*i-d/2,0)))
				left2.append(Part.makeCylinder(d/2,t,Vector(x-bb-2.5,-cc-a*i,0)))
				right2.append(Part.makeCylinder(d/2,t,Vector(x-bb+2.5,-cc-a*i,0)))
			for i in left:
				plate1 = plate1.cut(i)
			for i in right:
				plate1 = plate1.cut(i)
			for i in box:
				plate1 = plate1.cut(i)
			for i in left2:
				plate1 = plate1.cut(i)
			for i in right2:
				plate1 = plate1.cut(i)
			for i in box2:
				plate1 = plate1.cut(i)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"플라스틱판 11X5":
			doc=App.newDocument()

			x = 139.8
			y = 63.6
			r = 6.4
			t = 0.41
			d = 4.2
			n = 11
			m = 5
			b = n-1
			p = m-1
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5
			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(r, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			hole1 = Part.makeCylinder(d/2,t,Vector(x/2,-y/2,0))
			hole_up = []
			hole_down = []
			for i in range(n):
				hole_up.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-25-y/2,0)))
				hole_down.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,25-y/2,0)))
			plate1 = plate1.cut(hole1)
			for i in hole_up:
				plate1 = plate1.cut(i)
			for i in hole_down:
				plate1 = plate1.cut(i)

			left = []
			right = []
			box = []
			left2 = []
			right2 = []
			box2 = []
			for i in range(m):
				box.append(Part.makeBox(5,d,t,Vector(4.5,-cc-a*i-d/2,0)))
				left.append(Part.makeCylinder(d/2,t,Vector(bb-2.5,-cc-a*i,0)))
				right.append(Part.makeCylinder(d/2,t,Vector(bb+2.5,-cc-a*i,0)))
			for i in range(m):
				box2.append(Part.makeBox(5,d,t,Vector(x-bb-2.5,-cc-a*i-d/2,0)))
				left2.append(Part.makeCylinder(d/2,t,Vector(x-bb-2.5,-cc-a*i,0)))
				right2.append(Part.makeCylinder(d/2,t,Vector(x-bb+2.5,-cc-a*i,0)))
			for i in left:
				plate1 = plate1.cut(i)
			for i in right:
				plate1 = plate1.cut(i)
			for i in box:
				plate1 = plate1.cut(i)
			for i in left2:
				plate1 = plate1.cut(i)
			for i in right2:
				plate1 = plate1.cut(i)
			for i in box2:
				plate1 = plate1.cut(i)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 0.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"플라스틱판 11X3":
			doc=App.newDocument()

			x = 139.8
			y = 38.2
			r = 6.4
			t = 0.41
			d = 4.2
			n = 11
			m = 3
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5
			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(r, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			hole1 = Part.makeCylinder(d/2,t,Vector(x/2,-y/2,0))
			hole_up = []
			hole_down = []
			for i in range(n):
				hole_up.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-12.5-y/2,0)))
				hole_down.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,12.5-y/2,0)))
			plate1 = plate1.cut(hole1)
			for i in hole_up:
				plate1 = plate1.cut(i)
			for i in hole_down:
				plate1 = plate1.cut(i)

			left = []
			right = []
			box = []
			left2 = []
			right2 = []
			box2 = []
			for i in range(m):
				box.append(Part.makeBox(5,d,t,Vector(4.5,-cc-a*i-d/2,0)))
				left.append(Part.makeCylinder(d/2,t,Vector(bb-2.5,-cc-a*i,0)))
				right.append(Part.makeCylinder(d/2,t,Vector(bb+2.5,-cc-a*i,0)))
			for i in range(m):
				box2.append(Part.makeBox(5,d,t,Vector(x-bb-2.5,-cc-a*i-d/2,0)))
				left2.append(Part.makeCylinder(d/2,t,Vector(x-bb-2.5,-cc-a*i,0)))
				right2.append(Part.makeCylinder(d/2,t,Vector(x-bb+2.5,-cc-a*i,0)))
			for i in left:
				plate1 = plate1.cut(i)
			for i in right:
				plate1 = plate1.cut(i)
			for i in box:
				plate1 = plate1.cut(i)
			for i in left2:
				plate1 = plate1.cut(i)
			for i in right2:
				plate1 = plate1.cut(i)
			for i in box2:
				plate1 = plate1.cut(i)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 0.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"플라스틱판 5X5":
			doc=App.newDocument()

			x = 63.6
			y = 63.6
			r = 6.4
			t = 0.41
			d = 4.2
			n = 5
			m = 5
			b = n-1
			p = m-1
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5
			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(r, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			hole1 = Part.makeCylinder(d/2,t,Vector(x/2,-y/2,0))
			hole_up = []
			hole_down = []
			for i in range(n):
				hole_up.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-25-y/2,0)))
				hole_down.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,25-y/2,0)))
			plate1 = plate1.cut(hole1)
			for i in hole_up:
				plate1 = plate1.cut(i)
			for i in hole_down:
				plate1 = plate1.cut(i)

			left = []
			right = []
			box = []
			left2 = []
			right2 = []
			box2 = []
			for i in range(m):
				box.append(Part.makeBox(5,d,t,Vector(4.5,-cc-a*i-d/2,0)))
				left.append(Part.makeCylinder(d/2,t,Vector(bb-2.5,-cc-a*i,0)))
				right.append(Part.makeCylinder(d/2,t,Vector(bb+2.5,-cc-a*i,0)))
			for i in range(m):
				box2.append(Part.makeBox(5,d,t,Vector(x-bb-2.5,-cc-a*i-d/2,0)))
				left2.append(Part.makeCylinder(d/2,t,Vector(x-bb-2.5,-cc-a*i,0)))
				right2.append(Part.makeCylinder(d/2,t,Vector(x-bb+2.5,-cc-a*i,0)))
			for i in left:
				plate1 = plate1.cut(i)
			for i in right:
				plate1 = plate1.cut(i)
			for i in box:
				plate1 = plate1.cut(i)
			for i in left2:
				plate1 = plate1.cut(i)
			for i in right2:
				plate1 = plate1.cut(i)
			for i in box2:
				plate1 = plate1.cut(i)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"플라스틱판 5X3":
			doc=App.newDocument()

			x = 63.6
			y = 38.2
			r = 6.4
			t = 0.41
			d = 4.2
			n = 5
			m = 3
			b = n-1
			p = m-1
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5
			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(r, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			hole1 = Part.makeCylinder(d/2,t,Vector(x/2,-y/2,0))
			hole_up = []
			hole_down = []
			for i in range(n):
				hole_up.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-12.5-y/2,0)))
				hole_down.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,12.5-y/2,0)))
			plate1 = plate1.cut(hole1)
			for i in hole_up:
				plate1 = plate1.cut(i)
			for i in hole_down:
				plate1 = plate1.cut(i)

			left = []
			right = []
			box = []
			left2 = []
			right2 = []
			box2 = []
			for i in range(m):
				box.append(Part.makeBox(5,d,t,Vector(4.5,-cc-a*i-d/2,0)))
				left.append(Part.makeCylinder(d/2,t,Vector(bb-2.5,-cc-a*i,0)))
				right.append(Part.makeCylinder(d/2,t,Vector(bb+2.5,-cc-a*i,0)))
			for i in range(m):
				box2.append(Part.makeBox(5,d,t,Vector(x-bb-2.5,-cc-a*i-d/2,0)))
				left2.append(Part.makeCylinder(d/2,t,Vector(x-bb-2.5,-cc-a*i,0)))
				right2.append(Part.makeCylinder(d/2,t,Vector(x-bb+2.5,-cc-a*i,0)))
			for i in left:
				plate1 = plate1.cut(i)
			for i in right:
				plate1 = plate1.cut(i)
			for i in box:
				plate1 = plate1.cut(i)
			for i in left2:
				plate1 = plate1.cut(i)
			for i in right2:
				plate1 = plate1.cut(i)
			for i in box2:
				plate1 = plate1.cut(i)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 0.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"삼각플라스틱판":
			doc=App.newDocument()

			x=89
			y=78.8
			t=0.42
			f=3
			d=4.25
			i=0
			j=0
			n=4
			m=3
			cir = []
			cir2 = []
			cir3 = []
			box = []
			tri = Part.makePolygon([(0,0,0),(x,0,0),(x/2,y,0),(0,0,0)])
			fa = Part.Face(tri)
			p = fa.extrude(Vector(0,0,t))
			p = p.makeFillet(f, [p.Edges[0],p.Edges[1],p.Edges[4]])

			for i in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(6.62+25.25*i,4.3,0)))
			for i in cir:
			        p = p.cut(i)
			for j in range(m):
					cir2.append(Part.makeCylinder(d/2,t,Vector(17.105+25.25*j,4.3,0)))
					box.append(Part.makeBox(4.28,4.25,t,Vector(17.105+25.25*j,2.18,0)))
					cir3.append(Part.makeCylinder(d/2,t,Vector(21.385+25.25*j,4.3,0)))
			for j in cir2:
					p = p.cut(j)
			for j in cir3:
					p = p.cut(j)
			for j in box:
					p = p.cut(j)
			for i in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(6.62+12.47*i,4.3+25.25*0.866*i,0)))
			for i in cir:
			        p = p.cut(i)
			for j in range(m):
					cir2.append(Part.makeCylinder(d/2,t,Vector(6.62+5.24+12.47*j,4.3+10.485*0.866+25.25*0.866*j,0)))
					box.append(Part.makeBox(4.28,4.25,4.25,Vector(4.78+5.24+12.47*j,14.44751+25.25*0.866*j,0),Vector(0.5,-0.29,0)))
					cir3.append(Part.makeCylinder(d/2,t,Vector(6.62+7.38+12.47*j,4.3+14.765*0.866+25.25*0.866*j,0)))
			for j in cir2:
					p = p.cut(j)
			for j in cir3:
					p = p.cut(j)
			for j in box:
					p = p.cut(j)
			for j in range(m):
					cir2.append(Part.makeCylinder(d/2,t,Vector(89-(6.62+5.24+12.47*j),4.3+10.485*0.866+25.25*0.866*j,0)))
					box.append(Part.makeBox(4.28,4.25,4.25,Vector(89-(3.68+4.78+5.24+12.47*j),14.44751-2.125+25.25*0.866*j,0),Vector(0.5,0.29,0)))
					cir3.append(Part.makeCylinder(d/2,t,Vector(89-(6.62+7.38+12.47*j),4.3+14.765*0.866+25.25*0.866*j,0)))
			for j in cir2:
					p = p.cut(j)
			for j in cir3:
					p = p.cut(j)
			for j in box:
					p = p.cut(j)
			for i in range(3):
					cir.append(Part.makeCylinder(d/2,t,Vector(89-(6.62+12.47*i),4.3+25.25*0.866*i,0)))
			for i in cir:
			        p = p.cut(i)

			cir4 = Part.makeCylinder(d/2,t,Vector(44.5,27,0))
			p = p.cut(cir4)
			#Part.show(p)
			shape=doc.addObject("Part::Feature")
			shape.Shape=p
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

		elif self.popup2.currentText() == u"반원플라스틱판":

			doc=App.newDocument()

			D = 64
			d = 4.11
			f = 6
			t = 0.97
			i = 0
			n = 5

			plate1 = Part.makeBox(D,D/2,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(D/2-0.01, [plate1.Edges[2],plate1.Edges[6]])

			plate2 = Part.makeBox(D,f,t,Vector(0,-f,0))
			plate2 = plate2.makeFillet(f-0.01, [plate2.Edges[0],plate2.Edges[4]])

			plate1 = plate1.fuse(plate2)

			cir = []
			for i in range(n):
				cir.append(Part.makeCylinder(d/2, t, Vector(f+12.7*i,-2,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			cir2 = []
			for i in range(n):
				cir2.append(Part.makeCylinder(d/2, t, Vector(f+12.7*i,2.5,0)))
			for i in cir2:
				plate1 = plate1.cut(i)

			box3 = []
			for i in range(n):
				box3.append(Part.makeBox(d, 4.5, t, Vector((f-d/2)+12.7*i,-2,0)))
			for i in box3:
				plate1 = plate1.cut(i)

			#가운데 사각형 회전
			box4 = Part.makeBox(d, 4.5, 50, Vector(f-d/2,-2,0))
			box4.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),-30)
			plate1 = plate1.cut(box4)

			box5 = Part.makeBox(d, 4.5, 50, Vector(f-d/2,-2,0))
			box5.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),-60)
			plate1 = plate1.cut(box5)

			box6 = Part.makeBox(d, 4.5, 50, Vector(f-d/2,-2,0))
			box6.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),-90)
			plate1 = plate1.cut(box6)

			box7 = Part.makeBox(d, 4.5, 50, Vector(f-d/2,-2,0))
			box7.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),-120)
			plate1 = plate1.cut(box7)

			box8 = Part.makeBox(d, 4.5, 50, Vector(f-d/2,-2,0))
			box8.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),-150)
			plate1 = plate1.cut(box8)

			#왼쪽 반원 회전
			circle1 = Part.makeCylinder(d/2, t, Vector(f+12.7*2-d/2,12.7*2,0))
			plate1 = plate1.cut(circle1)

			circle2 = Part.makeCylinder(d/2, t, Vector(f+12.7*2-d/2,12.7*2,0))
			circle2.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),-30)
			plate1 = plate1.cut(circle2)

			circle3 = Part.makeCylinder(d/2, t, Vector(f+12.7*2-d/2,12.7*2,0))
			circle3.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),-60)
			plate1 = plate1.cut(circle3)

			circle4 = Part.makeCylinder(d/2, t, Vector(f+12.7*2-d/2,12.7*2,0))
			circle4.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),30)
			plate1 = plate1.cut(circle4)

			circle5 = Part.makeCylinder(d/2, t, Vector(f+12.7*2-d/2,12.7*2,0))
			circle5.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),60)
			plate1 = plate1.cut(circle5)

			#오른쪽 반원 회전
			circle6 = Part.makeCylinder(d/2, t, Vector(f+12.7*2+d/2,12.7*2,0))
			plate1 = plate1.cut(circle6)

			circle7 = Part.makeCylinder(d/2, t, Vector(f+12.7*2+d/2,12.7*2,0))
			circle7.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),-30)
			plate1 = plate1.cut(circle7)

			circle8 = Part.makeCylinder(d/2, t, Vector(f+12.7*2+d/2,12.7*2,0))
			circle8.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),-60)
			plate1 = plate1.cut(circle8)

			circle9 = Part.makeCylinder(d/2, t, Vector(f+12.7*2+d/2,12.7*2,0))
			circle9.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),30)
			plate1 = plate1.cut(circle9)

			circle10 = Part.makeCylinder(d/2, t, Vector(f+12.7*2+d/2,12.7*2,0))
			circle10.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),60)
			plate1 = plate1.cut(circle10)
			#가운데
			circle11 = Part.makeCylinder(d/2, t, Vector(f+12.7*2,12.7,0))
			plate1 = plate1.cut(circle11)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 0.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")


	def onPopupDes5(self):
		if self.popup2.currentText() == u"스트립 - 15":

			doc=App.newDocument()
			v=12.7
			x=189.75
			t=1
			r=6.35
			n=15
			a=12.5
			f=(x-a*(n-1))/2 #6.5
			i=0
			d=4.1

			plate1=Part.makeBox(x,v,t,Vector(0,0,0))
			plate1=plate1.makeFillet(r-0.01,[plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir=[]
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,r,0)))
			for i in cir:
				plate1=plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif self.popup2.currentText() == u"스트립 - 11":

			doc=App.newDocument()
			v=12.7
			x=139.05
			t=1
			r=6.35
			n=11
			a=12.5
			f=(x-a*(n-1))/2 #6.5
			i=0
			d=4.1

			plate1=Part.makeBox(x,v,t,Vector(0,0,0))
			plate1=plate1.makeFillet(r-0.01,[plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir=[]
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,r,0)))
			for i in cir:
				plate1=plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

		elif self.popup2.currentText() == u"스트립 - 9":

			doc=App.newDocument()
			v=12.7
			x=113.7
			t=1
			r=6.35
			n=9
			a=12.5
			f=(x-a*(n-1))/2 #6.5
			i=0
			d=4.1

			plate1=Part.makeBox(x,v,t,Vector(0,0,0))
			plate1=plate1.makeFillet(r-0.01,[plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir=[]
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,r,0)))
			for i in cir:
				plate1=plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

		elif self.popup2.currentText() == u"스트립 - 5":

			doc=App.newDocument()
			v=12.7
			x=63
			t=1
			r=6.35 #v/2
			n=5
			a=12.5
			f=(x-a*(n-1))/2 #6.5
			i=0
			d=4.1

			plate1=Part.makeBox(x,v,t,Vector(0,0,0))
			plate1=plate1.makeFillet(r-0.01,[plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir=[]
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,r,0)))
			for i in cir:
				plate1=plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

		elif self.popup2.currentText() == u"좁은스트립 - 5":

			doc=App.newDocument()
			v=8.9
			x=63
			t=1
			r=4.45 #v/2
			n=5
			a=12.5
			f=(x-a*(n-1))/2 #6.5
			i=0
			d=4.1

			plate1=Part.makeBox(x,v,t,Vector(0,0,0))
			plate1=plate1.makeFillet(r-0.01,[plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir=[]
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,r,0)))
			for i in cir:
				plate1=plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

		elif self.popup2.currentText() == u"좁은스트립 - 6":
			doc=App.newDocument()
			v=8.9
			x=75.6
			t=1
			r=4.45
			n=6
			a=12.5
			f=(x-a*(n-1))/2 #6.5
			i=0
			d=4.1

			plate1=Part.makeBox(x,v,t,Vector(0,0,0))
			plate1=plate1.makeFillet(r-0.01,[plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir=[]
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,r,0)))
			for i in cir:
				plate1=plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

		elif self.popup2.currentText() == u"좁은스트립 - 7":
			doc=App.newDocument()
			v=8.9
			x=88.2
			t=1
			r=4.45
			n=7
			a=12.5
			f=(x-a*(n-1))/2 #6.5
			i=0
			d=4.1

			plate1=Part.makeBox(x,v,t,Vector(0,0,0))
			plate1=plate1.makeFillet(r-0.01,[plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir=[]
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,r,0)))
			for i in cir:
				plate1=plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

		elif self.popup2.currentText() == u"좁은스트립 - 9":
			doc=App.newDocument()
			v=8.9
			x=113.7
			t=1
			r=4.45
			n=9
			a=12.5
			f=(x-a*(n-1))/2 #6.5
			i=0
			d=4.1

			plate1=Part.makeBox(x,v,t,Vector(0,0,0))
			plate1=plate1.makeFillet(r-0.01,[plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir=[]
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,r,0)))
			for i in cir:
				plate1=plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif self.popup2.currentText() == u"좁은스트립 - 3":

			doc=App.newDocument()
			v=8.9
			x=37.4
			t=1
			r=4.45
			n=3
			a=12.5
			f=(x-a*(n-1))/2 #6.5
			i=0
			d=4.1

			plate1=Part.makeBox(x,v,t,Vector(0,0,0))
			plate1=plate1.makeFillet(r-0.01,[plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir=[]
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,r,0)))
			for i in cir:
				plate1=plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

		elif self.popup2.currentText() == u"스트립 - 25":

			doc=App.newDocument()
			v=12.7
			x=316.5
			t=1
			r=6.35
			n=25
			a=12.5
			f=(x-a*(n-1))/2 #6.5
			i=0
			d=4.1

			plate1=Part.makeBox(x,v,t,Vector(0,0,0))
			plate1=plate1.makeFillet(r-0.01,[plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir=[]
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,r,0)))
			for i in cir:
				plate1=plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

		elif self.popup2.currentText() == u"스트립 - 5(s)":

			doc=App.newDocument()

			x = 50.44
			y = 12.81
			t = 0.85
			d = 4.11
			f = 6.4

			plate1 = Part.makeBox(x,y,t,Vector(0,0,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir = []
			cir.append(Part.makeCylinder(d/2,t,Vector(4.1+d/2,y/2,0)))
			cir.append(Part.makeCylinder(d/2,t,Vector(17.1+d/2,y/2,0)))
			cir.append(Part.makeCylinder(d/2,t,Vector(23.1+d/2,y/2,0)))
			cir.append(Part.makeCylinder(d/2,t,Vector(29.5+d/2,y/2,0)))
			cir.append(Part.makeCylinder(d/2,t,Vector(42.1+d/2,y/2,0)))

			for i in cir:
				plate1 = plate1.cut(i)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=plate1      	                           #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif self.popup2.currentText() ==  u"ㄷ형스트립 - 3":

			doc=App.newDocument()

			x = 37.4
			y = 12.7
			z = 14.3
			t = 0.7
			d = 4.2
			n = 3
			m = 1
			r = 6.34
			i = 0
			j = 0
			a=12.5
			f=(x-a*(n-1))/2

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate2 = Part.makeBox(t,y,z,Vector(0,-y,0),Vector(0,0,1))
			plate3 = Part.makeBox(t,y,z,Vector(x-t,-y,0),Vector(0,0,1))

			plate2 = plate2.makeFillet(r, [plate2.Edges[9],plate2.Edges[11]])
			plate3 = plate3.makeFillet(r, [plate3.Edges[9],plate3.Edges[11]])

			cir = []
			lt = []
			rt = []

			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,-y/2,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			for j in range(m):
				lt.append(Part.makeCylinder(d/2,t,Vector(0,-y/2,8),Vector(1,0,0)))
			for j in range(m):
				rt.append(Part.makeCylinder(d/2,t,Vector(x-t,-y/2,8),Vector(1,0,0)))
			for i in lt:
				plate2 = plate2.cut(i)
			for i in rt:
				plate3 = plate3.cut(i)

			plate1 = plate1.fuse(plate2)
			plate1 = plate1.fuse(plate3)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=plate1      	                           #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

		elif self.popup2.currentText() == u"ㄷ형스트립 - 5":
			doc=App.newDocument()

			x = 62.8
			y = 12.7
			z = 14.3
			t = 0.7
			d = 4.2
			n = 5
			m = 1
			r = 6.34
			i = 0
			j = 0
			a=12.5
			f=(x-a*(n-1))/2

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate2 = Part.makeBox(t,y,z,Vector(0,-y,0),Vector(0,0,1))
			plate3 = Part.makeBox(t,y,z,Vector(x-t,-y,0),Vector(0,0,1))

			plate2 = plate2.makeFillet(r, [plate2.Edges[9],plate2.Edges[11]])
			plate3 = plate3.makeFillet(r, [plate3.Edges[9],plate3.Edges[11]])

			cir = []
			lt = []
			rt = []

			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,-y/2,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			for j in range(m):
				lt.append(Part.makeCylinder(d/2,t,Vector(0,-y/2,8),Vector(1,0,0)))
			for j in range(m):
				rt.append(Part.makeCylinder(d/2,t,Vector(x-t,-y/2,8),Vector(1,0,0)))
			for i in lt:
				plate2 = plate2.cut(i)
			for i in rt:
				plate3 = plate3.cut(i)

			plate1 = plate1.fuse(plate2)
			plate1 = plate1.fuse(plate3)


			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=plate1      	                           #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

		elif self.popup2.currentText() == u"ㄷ형스트립 - 7":
			doc=App.newDocument()

			x = 88.2
			y = 12.7
			z = 14.3
			t = 0.7
			d = 4.2
			n = 7
			m = 1
			r = 6.34
			i = 0
			j = 0
			a=12.5
			f=(x-a*(n-1))/2

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate2 = Part.makeBox(t,y,z,Vector(0,-y,0),Vector(0,0,1))
			plate3 = Part.makeBox(t,y,z,Vector(x-t,-y,0),Vector(0,0,1))

			plate2 = plate2.makeFillet(r, [plate2.Edges[9],plate2.Edges[11]])
			plate3 = plate3.makeFillet(r, [plate3.Edges[9],plate3.Edges[11]])

			cir = []
			lt = []
			rt = []

			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,-y/2,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			for j in range(m):
				lt.append(Part.makeCylinder(d/2,t,Vector(0,-y/2,8),Vector(1,0,0)))
			for j in range(m):
				rt.append(Part.makeCylinder(d/2,t,Vector(x-t,-y/2,8),Vector(1,0,0)))
			for i in lt:
				plate2 = plate2.cut(i)
			for i in rt:
				plate3 = plate3.cut(i)

			plate1 = plate1.fuse(plate2)
			plate1 = plate1.fuse(plate3)


			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=plate1      	                           #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.popup2.currentText() == u"원형스트립":

			doc=App.newDocument()
			d1=83
			d2=57
			t=0.8

			d3=6.5
			d4=4.11/2

			plate1 = Part.makeCylinder(d1/2,t,Vector(0,0,0),Vector(0,0,1),91)
			plate2 = Part.makeCylinder(d2/2,t,Vector(0,0,0),Vector(0,0,1),91)
			plate1 = plate1.cut(plate2)

			cir1 = Part.makeCylinder(d3,t,Vector(34.5,0,0),Vector(0,0,1),180)
			cir1.rotate(Vector(34.5,0,0),Vector(0,0,1),180)
			cir2 = Part.makeCylinder(d3,t,Vector(34.5,0,0),Vector(0,0,1),180)
			cir2.rotate(Vector(0,0,0),Vector(0,0,1),91)
			plate1 = plate1.fuse(cir1)
			plate1 = plate1.fuse(cir2)

			cir3 = Part.makeCylinder(d4,t,Vector(34.5,0,0),Vector(0,0,1))
			cir4 = Part.makeCylinder(d4,t,Vector(34.5,0,0),Vector(0,0,1))
			cir4.rotate(Vector(0,0,0),Vector(0,0,1),91)
			cir5 = Part.makeCylinder(d4,t,Vector(34.5,0,0),Vector(0,0,1))
			cir5.rotate(Vector(0,0,0),Vector(0,0,1),45.5)
			plate1 = plate1.cut(cir3)
			plate1 = plate1.cut(cir4)
			plate1 = plate1.cut(cir5)

			box1 = Part.makeBox(4.0,3,t,Vector(34.5-2.0,-1.5,0),Vector(0,0,1))
			box1.rotate(Vector(0,0,0),Vector(0,0,1),23)
			plate1 = plate1.cut(box1)

			cir_up = Part.makeCylinder(2., t, Vector(34.5,+1.5,0),Vector(0,0,1))
			cir_up.rotate(Vector(0,0,0),Vector(0,0,1),23)
			plate1 = plate1.cut(cir_up)

			cir_dw = Part.makeCylinder(2.0, t, Vector(34.5,-1.5,0),Vector(0,0,1))
			cir_dw.rotate(Vector(0,0,0),Vector(0,0,1),23)
			plate1 = plate1.cut(cir_dw)

			box2 = Part.makeBox(4.0,3,t,Vector(34.5-2.0,-1.5,0),Vector(0,0,1))
			box2.rotate(Vector(0,0,0),Vector(0,0,1),68)
			plate1 = plate1.cut(box2)

			cir_up2 = Part.makeCylinder(2., t, Vector(34.5,+1.5,0),Vector(0,0,1))
			cir_up2.rotate(Vector(0,0,0),Vector(0,0,1),68)
			plate1 = plate1.cut(cir_up2)

			cir_dw3 = Part.makeCylinder(2.0, t, Vector(34.5,-1.5,0),Vector(0,0,1))
			cir_dw3.rotate(Vector(0,0,0),Vector(0,0,1),68)
			plate1 = plate1.cut(cir_dw3)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() ==  u"곡면스트립":

			doc=App.newDocument()

			plate1 = Part.makeCylinder(44.5,12.7,Vector(0,0,0),Vector(0,0,1),90)
			plate2 = Part.makeCylinder(43.8,12.7,Vector(0,0,0),Vector(0,0,1),90)
			plate1 = plate1.cut(plate2)

			cir1 = Part.makeCylinder(6.35,0.7,Vector(43.8,0,6.35),Vector(1,0,0),180)
			plate1 = plate1.fuse(cir1)
			cir2 = Part.makeCylinder(6.35,0.7,Vector(0,43.8,6.35),Vector(0,-1,0),180)
			cir2.rotate(Vector(0,43.8,6.35),Vector(0,0,1),180)
			plate1 = plate1.fuse(cir2)

			cir3 = Part.makeCylinder(4.0/2,50,Vector(0,0,6.35),Vector(0,1,0))
			plate1 = plate1.cut(cir3)

			cir4 = Part.makeCylinder(4.0/2,50,Vector(0,0,6.35),Vector(0,1,0))
			cir4.rotate(Vector(0,0,0),Vector(0,0,1),-45)
			plate1 = plate1.cut(cir4)

			cir5 = Part.makeCylinder(4.0/2,50,Vector(0,0,6.35),Vector(0,1,0))
			cir5.rotate(Vector(0,0,0),Vector(0,0,1),-90)
			plate1 = plate1.cut(cir5)

			cir6 = Part.makeCylinder(4.0/2,50,Vector(0,0,6.35),Vector(0,1,0))
			cir6.rotate(Vector(0,0,0),Vector(0,0,1),-20)
			plate1 = plate1.cut(cir6)

			cir7 = Part.makeCylinder(4.0/2,50,Vector(0,0,6.35),Vector(0,1,0))
			cir7.rotate(Vector(0,0,0),Vector(0,0,1),-70)
			plate1 = plate1.cut(cir7)

			box1 = Part.makeBox(4.0,50,15,Vector(0,0,4.36),Vector(0,1,0))
			plate1 = plate1.cut(box1)
			box2 = Part.makeBox(4.0,50,15,Vector(0,0,8.36),Vector(0,-1,0))
			box2.rotate(Vector(0,0,0),Vector(0,0,1),90)
			plate1 = plate1.cut(box2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"트러스스트립":
			doc=App.newDocument()

			x = 315.8
			y = 50.8
			t = 0.68
			d = 4.11
			f = 6.35
			n = 25
			n1 = 3
			n2 = 2
			i = 0
			j = 0
			l = 42
			l1 = 46
			w = 25
			plate1 = Part.makeBox(x,y,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir = []
			cir1 = []
			for i in range(n):
				for j in range(n2):
					cir.append(Part.makeCylinder(d/2,t,Vector(((x-(d+4*2))/(n-1))*i+4+d/2,j*(y-(d+4*2))+4+d/2,0)))
			for i in range(n1):
				for j in range(n1):
					cir1.append(Part.makeCylinder(d/2,t,Vector(((x-(d+4*2))/(n-1))*(n-1)*j/2+4+d/2,((16.64-d)/(n1-1))*i+17.1+d/2,0)))
			for i in cir:
				plate1 = plate1.cut(i)
			for i in cir1:
				plate1 = plate1.cut(i)

			box = []
			box1 = []
			box2 = []
			for i in range(n2):
				box1.append(Part.makeBox(l1,w,t,Vector((y-w)/2+47+152*i,(y-w)/2,0)))
				for j in range(n2):
					box.append(Part.makeBox(l,w,t,Vector((y-w)/2+152*i+98*j,(y-w)/2,0)))
			for i in box:
				plate1 = plate1.cut(i)
			for i in box1:
				plate1 = plate1.cut(i)

			tri = Part.makePolygon([((y-w)/2,(y-w)/2+w,0),((y-w)/2+l-7,(y-w)/2,0),((y-w)/2+l,(y-w)/2,0),((y-w)/2+7,(y-w)/2+w,0),((y-w)/2,(y-w)/2+w,0)])
			fa = Part.Face(tri)
			p = fa.extrude(Vector(0,0,t))
			plate1 = plate1.fuse(p)
			tri1 = Part.makePolygon([((y-w)/2+98,(y-w)/2+w,0),((y-w)/2+l-7+98,(y-w)/2,0),((y-w)/2+l+98,(y-w)/2,0),((y-w)/2+7+98,(y-w)/2+w,0),((y-w)/2+98,(y-w)/2+w,0)])
			fa1 = Part.Face(tri1)
			p1 = fa1.extrude(Vector(0,0,t))
			plate1 = plate1.fuse(p1)
			tri2 = Part.makePolygon([((y-w)/2+199,(y-w)/2+w,0),((y-w)/2+l1-7+199,(y-w)/2,0),((y-w)/2+l1+199,(y-w)/2,0),((y-w)/2+7+199,(y-w)/2+w,0),((y-w)/2+199,(y-w)/2+w,0)])
			fa2 = Part.Face(tri2)
			p2 = fa2.extrude(Vector(0,0,t))
			plate1 = plate1.fuse(p2)

			tri3 = Part.makePolygon([((y-w)/2+47,(y-w)/2,0),((y-w)/2+47+7,(y-w)/2,0),((y-w)/2+47+l1,(y-w)/2+w,0),((y-w)/2+47+l1-7,(y-w)/2+w,0),((y-w)/2+47,(y-w)/2,0)])
			fa3 = Part.Face(tri3)
			p3 = fa3.extrude(Vector(0,0,t))
			plate1 = plate1.fuse(p3)
			tri4 = Part.makePolygon([((y-w)/2+47+105,(y-w)/2,0),((y-w)/2+47+7+105,(y-w)/2,0),((y-w)/2+47+l+105,(y-w)/2+w,0),((y-w)/2+47+l-7+105,(y-w)/2+w,0),((y-w)/2+47+105,(y-w)/2,0)])
			fa4 = Part.Face(tri4)
			p4 = fa4.extrude(Vector(0,0,t))
			plate1 = plate1.fuse(p4)
			tri5 = Part.makePolygon([((y-w)/2+47+203,(y-w)/2,0),((y-w)/2+47+7+203,(y-w)/2,0),((y-w)/2+47+l+203,(y-w)/2+w,0),((y-w)/2+47+l-7+203,(y-w)/2+w,0),((y-w)/2+47+203,(y-w)/2,0)])
			fa5 = Part.Face(tri5)
			p5 = fa5.extrude(Vector(0,0,t))
			plate1 = plate1.fuse(p5)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


	def onPopupDes6(self):
		if self.popup2.currentText() == u"플랜지판(소)":

			doc=App.newDocument()
			x = 62.0
			y = 36.6
			z = 13.5
			t = 0.7
			d = 4.1
			n = 5
			m = 3
			f = 6.35
			i = 0
			j = 0
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate2 = Part.makeBox(t,y,z,Vector(0,-y,0),Vector(0,0,1))
			plate3 = Part.makeBox(t,y,z,Vector(x-t,-y,0),Vector(0,0,1))

			plate2 = plate2.makeFillet(f, [plate2.Edges[9],plate2.Edges[11]])
			plate3 = plate3.makeFillet(f, [plate3.Edges[9],plate3.Edges[11]])

			cir = []
			lt = []
			rt = []
			lt_up = []
			rt_up = []
			lt_box = []
			rt_box = []
			for j in range(m):
				for i in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-cc-a*j,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			for j in range(m):
				lt.append(Part.makeCylinder(d/2,t,Vector(0,-((y-11.0)/(m-1))*j-5.5,6),Vector(1,0,0)))
				lt_up.append(Part.makeCylinder(d/2,t,Vector(0,-((y-11.0)/(m-1))*j-5.5,8),Vector(1,0,0)))
				lt_box.append(Part.makeBox(2,d,t,Vector(0,-((y-11.0)/(m-1))*j-5.5+d/2,6),Vector(1,0,0)))
			for j in range(m):
				rt.append(Part.makeCylinder(d/2,t,Vector(x-t,-((y-11.0)/(m-1))*j-5.5,6),Vector(1,0,0)))
				rt_up.append(Part.makeCylinder(d/2,t,Vector(x-t,-((y-11.0)/(m-1))*j-5.5,8),Vector(1,0,0)))
				rt_box.append(Part.makeBox(2,d,t,Vector(x-t,-((y-11.0)/(m-1))*j-5.5+d/2,6),Vector(1,0,0)))

			for i in lt:
				plate2 = plate2.cut(i)
			for i in lt_up:
				plate2 = plate2.cut(i)
			for i in lt_box:
				plate2 = plate2.cut(i)
			for i in rt:
				plate3 = plate3.cut(i)
			for i in rt_up:
				plate3 = plate3.cut(i)
			for i in rt_box:
				plate3 = plate3.cut(i)

			plate1 = plate1.fuse(plate2)
			plate1 = plate1.fuse(plate3)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 1.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

		elif self.popup2.currentText() == u"플랜지판(대)":
			doc=App.newDocument()

			x = 90.2
			y = 60
			z = 13.5
			t = 0.7
			d = 4.2
			n = 7
			m = 5
			f = 6.35
			i = 0
			j = 0
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate2 = Part.makeBox(t,y,z,Vector(0,-y,0),Vector(0,0,1))
			plate3 = Part.makeBox(t,y,z,Vector(x-t,-y,0),Vector(0,0,1))

			plate2 = plate2.makeFillet(f, [plate2.Edges[9],plate2.Edges[11]])
			plate3 = plate3.makeFillet(f, [plate3.Edges[9],plate3.Edges[11]])

			cir = []
			lt = []
			rt = []
			lt_up = []
			rt_up = []
			lt_box = []
			rt_box = []

			for j in range(m):
				for i in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-cc-a*j,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			for j in range(m):
				lt.append(Part.makeCylinder(d/2,t,Vector(0,-((y-11.0)/(m-1))*j-5.5,6),Vector(1,0,0)))
				lt_up.append(Part.makeCylinder(d/2,t,Vector(0,-((y-11.0)/(m-1))*j-5.5,8),Vector(1,0,0)))
				lt_box.append(Part.makeBox(2,d,t,Vector(0,-((y-11.0)/(m-1))*j-5.5+d/2,6),Vector(1,0,0)))
			for j in range(m):
				rt.append(Part.makeCylinder(d/2,t,Vector(x-t,-((y-11.0)/(m-1))*j-5.5,6),Vector(1,0,0)))
				rt_up.append(Part.makeCylinder(d/2,t,Vector(x-t,-((y-11.0)/(m-1))*j-5.5,8),Vector(1,0,0)))
				rt_box.append(Part.makeBox(2,d,t,Vector(x-t,-((y-11.0)/(m-1))*j-5.5+d/2,6),Vector(1,0,0)))

			for i in lt:
				plate2 = plate2.cut(i)
			for i in lt_up:
				plate2 = plate2.cut(i)
			for i in lt_box:
				plate2 = plate2.cut(i)
			for i in rt:
				plate3 = plate3.cut(i)
			for i in rt_up:
				plate3 = plate3.cut(i)
			for i in rt_box:
				plate3 = plate3.cut(i)

			plate1 = plate1.fuse(plate2)
			plate1 = plate1.fuse(plate3)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 1.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.popup2.currentText() == u"사다리꼴플랜지판":
			doc=App.newDocument()
			y=87.33
			t=0.73
			d=4.15
			l=12.46333333
			z=13.5
			i=0
			n=7
			cir1 = []
			cir2 = []
			cir3 = []
			cir6 = []
			cir7 = []
			box = []
			tri = Part.makePolygon([(0,0,0),(13.7,y,0),(59.5,y,0),(73.2,0,0),(0,0,0)])
			fa = Part.Face(tri)
			p = fa.extrude(Vector(0,0,t))

			tri2 = Part.makePolygon([(0,0,t),(0,0,z),(13.7,y,z),(13.7,y,t),(0,0,t)])
			fa = Part.Face(tri2)
			p2 = fa.extrude(Vector(t,0,0))

			for i in range(n):
					cir1.append(Part.makeCylinder(d/2,t,Vector(23.925,6.275+i*l,0)))
					cir2.append(Part.makeCylinder(d/2,t,Vector(36.6,6.275+i*l,0)))
					cir3.append(Part.makeCylinder(d/2,t,Vector(49.275,6.275+i*l,0)))
			for i in cir1:
			        p = p.cut(i)
			for i in cir2:
			        p = p.cut(i)
			for i in cir3:
			        p = p.cut(i)
			cir4 = Part.makeCylinder(d/2,t,Vector(11.25,6.275,0))
			cir5 = Part.makeCylinder(d/2,t,Vector(61.95,6.275,0))
			p = p.cut(cir4)
			p = p.cut(cir5)
			p = p.fuse(p2)
			for i in range(n):
					cir6.append(Part.makeCylinder(d/2,150,Vector(0,6.275+i*l,3+d/2),Vector(1,0,0)))
					cir7.append(Part.makeCylinder(d/2,150,Vector(0,6.275+i*l,z-3-d/2),Vector(1,0,0)))
					box.append(Part.makeBox(150,d,3.35,Vector(0,4.2+i*l,3+d/2)))

			p2 = p2.mirror(Vector(36.6,43.665,0),Vector(1,0,0))
			p = p.fuse(p2)
			for i in cir6:
					p= p.cut(i)
			for i in cir7:
					p= p.cut(i)
			for i in box:
					p= p.cut(i)
			#Part.show(p)
			shape=doc.addObject("Part::Feature")
			shape.Shape=p
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 1.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"플랜지판 2X5":
			doc=App.newDocument()

			x = 62.8
			y = 25.4
			z = 14.3
			t = 0.7
			d = 4.2
			n = 5
			m = 2
			f = 6.35
			i = 0
			j = 0

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate2 = Part.makeBox(t,y,z,Vector(0,-y,0),Vector(0,0,1))
			plate3 = Part.makeBox(t,y,z,Vector(x-t,-y,0),Vector(0,0,1))

			plate2 = plate2.makeFillet(f, [plate2.Edges[9],plate2.Edges[11]])
			plate3 = plate3.makeFillet(f, [plate3.Edges[9],plate3.Edges[11]])

			cir = []
			lt = []
			rt = []

			for j in range(m):
				for i in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(((x-11.0)/(n-1))*i+5.5,-((y-11.0)/(m-1))*j-5.5,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			for j in range(m):
				lt.append(Part.makeCylinder(d/2,t,Vector(0,-((y-11.0)/(m-1))*j-5.5,z/2),Vector(1,0,0)))
			for j in range(m):
				rt.append(Part.makeCylinder(d/2,t,Vector(x-t,-((y-11.0)/(m-1))*j-5.5,z/2),Vector(1,0,0)))
			for i in lt:
				plate2 = plate2.cut(i)
			for i in rt:
				plate3 = plate3.cut(i)

			plate1 = plate1.fuse(plate2)
			plate1 = plate1.fuse(plate3)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.popup2.currentText() == u"플랜지판 2X7":
			doc=App.newDocument()

			x = 90.2
			y = 25.4
			z = 14.3
			t = 0.7
			d = 4.2
			n = 7
			m = 2
			f = 6.35
			i = 0
			j = 0

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate2 = Part.makeBox(t,y,z,Vector(0,-y,0),Vector(0,0,1))
			plate3 = Part.makeBox(t,y,z,Vector(x-t,-y,0),Vector(0,0,1))

			plate2 = plate2.makeFillet(f, [plate2.Edges[9],plate2.Edges[11]])
			plate3 = plate3.makeFillet(f, [plate3.Edges[9],plate3.Edges[11]])

			cir = []
			lt = []
			rt = []

			for j in range(m):
				for i in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(((x-11.0)/(n-1))*i+5.5,-((y-11.0)/(m-1))*j-5.5,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			for j in range(m):
				lt.append(Part.makeCylinder(d/2,t,Vector(0,-((y-11.0)/(m-1))*j-5.5,z/2),Vector(1,0,0)))
			for j in range(m):
				rt.append(Part.makeCylinder(d/2,t,Vector(x-t,-((y-11.0)/(m-1))*j-5.5,z/2),Vector(1,0,0)))
			for i in lt:
				plate2 = plate2.cut(i)
			for i in rt:
				plate3 = plate3.cut(i)

			plate1 = plate1.fuse(plate2)
			plate1 = plate1.fuse(plate3)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

	def onPopupDes7(self):
		if self.popup2.currentText() == u"평판(대)":
			doc=App.newDocument()

			x = 139.7
			y = 63.5
			t = 0.7
			d = 4.2
			n = 11
			m = 5
			f = 6.35
			i = 0
			j = 0
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir = []

			for j in range(m):
				for i in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-cc-a*j,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 1.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.popup2.currentText() == u"평판(소)":
			doc=App.newDocument()

			x = 38.1
			y = 38.1
			t = 0.7
			d = 4.2
			n = 3
			m = 3
			f = 6.35
			i = 0
			j = 0
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir = []

			for j in range(m):
				for i in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-cc-a*j,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.popup2.currentText() == u"평판 - 9":

			doc=App.newDocument()

			x = 113.6
			y = 27.3
			t = 0.7
			d = 4.2
			n = 9
			f = 7
			i = 0
			j = 0
			a=12.5
			bb=(x-a*(n-1))/2 #6.5

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir = []
			cir1 = []
			cir2 = []
			box = []
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-6,0)))
				cir1.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,6-y+4,0)))
				cir2.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,6-y,0)))
			for i in range(n):
				box.append(Part.makeBox(d,4,t,Vector(bb+a*i-d/2,6-y,0)))
			for i in cir:
				plate1 = plate1.cut(i)
			for i in cir1:
				plate1 = plate1.cut(i)
			for i in cir2:
				plate1 = plate1.cut(i)
			for i in box:
				plate1 = plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.popup2.currentText() == u"평판 - 7":

			doc=App.newDocument()

			x = 88.2
			y = 27.3
			t = 0.7
			d = 4.2
			n = 7
			f = 7
			i = 0
			j = 0
			a=12.5
			bb=(x-a*(n-1))/2 #6.5

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir = []
			cir1 = []
			cir2 = []
			box = []
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-6,0)))
				cir1.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,6-y+4,0)))
				cir2.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,6-y,0)))
			for i in range(n):
				box.append(Part.makeBox(d,4,t,Vector(bb+a*i-d/2,6-y,0)))
			for i in cir:
				plate1 = plate1.cut(i)
			for i in cir1:
				plate1 = plate1.cut(i)
			for i in cir2:
				plate1 = plate1.cut(i)
			for i in box:
				plate1 = plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.popup2.currentText() == u"평판 - 5":

			doc=App.newDocument()

			x = 62.8
			y = 27.3
			t = 0.7
			d = 4.2
			n = 5
			f = 7
			i = 0
			j = 0
			a=12.5
			bb=(x-a*(n-1))/2 #6.5

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir = []
			cir1 = []
			cir2 = []
			box = []
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-6,0)))
				cir1.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,6-y+4,0)))
				cir2.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,6-y,0)))
			for i in range(n):
				box.append(Part.makeBox(d,4,t,Vector(bb+a*i-d/2,6-y,0)))
			for i in cir:
				plate1 = plate1.cut(i)
			for i in cir1:
				plate1 = plate1.cut(i)
			for i in cir2:
				plate1 = plate1.cut(i)
			for i in box:
				plate1 = plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.popup2.currentText() == u"평판 - 3":

			doc=App.newDocument()

			x = 37.4
			y = 27.3
			t = 0.7
			d = 4.2
			n = 3
			f = 7
			i = 0
			j = 0
			a=12.5
			bb=(x-a*(n-1))/2 #6.5

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir = []
			cir1 = []
			cir2 = []
			box = []
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-6,0)))
				cir1.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,6-y+4,0)))
				cir2.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,6-y,0)))
			for i in range(n):
				box.append(Part.makeBox(d,4,t,Vector(bb+a*i-d/2,6-y,0)))
			for i in cir:
				plate1 = plate1.cut(i)
			for i in cir1:
				plate1 = plate1.cut(i)
			for i in cir2:
				plate1 = plate1.cut(i)
			for i in box:
				plate1 = plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.popup2.currentText() == u"오각평판":
			doc=App.newDocument()

			x = 37.4
			y = 18.7
			y1= 37.7
			t = 0.68
			l=5.96
			d = 4.11
			f = 6

			n = 2
			n1 = 3
			i = 0
			j = 0

			plate1 = Part.makeBox(x,y,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[4]])
			tri = Part.makePolygon([(0,y,0),(x,y,0),(x/2,y1,0),(0,y,0)])
			fa = Part.Face(tri)
			p = fa.extrude(Vector(0,0,t))
			plate1 = plate1.fuse(p)

			tri1 = Part.makePolygon([(l,y,0),(2*l,y,0),(2*l,y+l,0),(l,y,0)])
			fa1 = Part.Face(tri1)
			p1 = fa1.extrude(Vector(0,0,t))
			plate1 = plate1.cut(p1)
			tri2 = Part.makePolygon([(x-l,y,0),(x-2*l,y,0),(x-2*l,y+l,0),(x-l,y,0)])
			fa2 = Part.Face(tri2)
			p2 = fa2.extrude(Vector(0,0,t))
			plate1 = plate1.cut(p2)

			pl = []
			cir = []
			cir1 = []
			for i in range(n):
				pl.append(Part.makeBox(l,l,t,Vector(l+(x-3*l)*i,y-l,0)))
			for i in pl:
				plate1 = plate1.cut(i)

			for i in range(n1):
				cir1.append(Part.makeCylinder(d/2,t,Vector(f+(x/2-f)*i,f,0)))
				if i == 2:
					for j in range(n):
						cir.append(Part.makeCylinder(d/2,t,Vector(x/2,f+(y1/2-f)*(j+1),0)))

			for i in cir:
				plate1 = plate1.cut(i)
			for i in cir1:
				plate1 = plate1.cut(i)


			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"사각평판 3X5":
			doc=App.newDocument()

			x = 63.5
			y = 38.1
			t = 0.7
			d = 4.2
			n = 5
			m = 3
			f = 6
			i = 0
			j = 0
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir = []

			for j in range(m):
				for i in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-cc-a*j,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 1.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.popup2.currentText() == u"삼각평판 3X5":
			doc=App.newDocument()

			x=85.5
			y=43.5
			t=0.7
			f=6.35
			d=4.2
			i=0
			j=1
			n=5
			n2=3

			cir = []
			cir2 = []
			tri = Part.makePolygon([(0,0,0),(x,0,0),(x,y,0),(0,0,0)])
			fa = Part.Face(tri)
			p = fa.extrude(Vector(0,0,t))
			p = p.makeFillet(f, [p.Edges[0],p.Edges[1],p.Edges[4]])

			for i in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(78.15-2*f*i,6.35,0)))

			for j in range(n2):
					cir2.append(Part.makeCylinder(d/2,t,Vector(78.15,6.35+2*f*j,0)))

			for i in cir:
			        p = p.cut(i)

			for j in cir2:
			        p = p.cut(j)

			cir3 = Part.makeCylinder(d/2,t,Vector(78.15-2*f*2,6.35+2*f,0))
			cir4 = Part.makeCylinder(d/2,t,Vector(27.35+16.3*0.8944,6.35+16.3*0.4472,0))
			cir5 = Part.makeCylinder(d/2,t,Vector(27.35+(16.3+4.1)*0.8944,6.35+(16.3+4.1)*0.4472,0))
			cir6 = Part.makeCylinder(d/2,t,Vector(78.15-2*f*2+8.15*0.8944,6.35+2*f+8.15*0.4472,0))
			cir7 = Part.makeCylinder(d/2,t,Vector(78.15-2*f*2+(8.15+12.6)*0.8944,6.35+2*f+(8.15+12.6)*0.4472,0))
			box = Part.makeBox(4.2,0.7,4.1, Vector(27.35+16.3*0.8944+2.1*0.4472,6.35+16.3*0.4472-2.1*0.8944,0), Vector(0.8944,0.4472,0))
			box1 = Part.makeBox(4.2,0.7,12.6, Vector(78.15-2*f*2+8.15*0.8944+2.1*0.4472,6.35+2*f+8.15*0.4472-2.1*0.8944,0), Vector(0.8944,0.4472,0))

			p=p.cut(cir3)
			p=p.cut(cir4)
			p=p.cut(cir5)
			p=p.cut(cir6)
			p=p.cut(cir7)
			p=p.cut(box)
			p=p.cut(box1)

			#Part.show(p)
			shape=doc.addObject("Part::Feature")
			shape.Shape=p
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

		elif self.popup2.currentText() == u"바퀴평판":
			doc=App.newDocument()

			l=63.5
			t=0.85
			d=4.11
			R=6.35
			i=0
			j=0
			n=4
			n1=2
			n2=3

			v1=Vector(0,0,0)
			v2=Vector((l-13.5)/2,0,0)
			v3=Vector(l,(l+13.5)/2,0)
			v4=Vector(l,l,0)
			v5=Vector(0,l,0)


			Arc1=Part.makeCircle((l+13.5)/2,Vector(l,0,0),Vector(0,0,1),90,180)
			Line1=Part.makeLine(v1,v2)
			Line2=Part.makeLine(v3,v4)
			Line3=Part.makeLine(v4,v5)
			Line4=Part.makeLine(v5,v1)
			Sket=Arc1.fuse(Line1)
			Sket=Sket.fuse(Line2)
			Sket=Sket.fuse(Line3)
			Sket=Sket.fuse(Line4)
			W=Part.Wire(Sket.Edges)
			face=Part.Face(W)
			P=face.extrude(Vector(0,0,t))
			P = P.makeFillet(R, [P.Edges[0],P.Edges[1],P.Edges[4],P.Edges[7],P.Edges[10]])

			cir=[]
			cir1=[]
			cir2=[]
			cir3=[]
			for i in range(n):
				for j in range(n1):
					cir.append(Part.makeCylinder(d/2,t,Vector(R+(17-d)*i,l-R-(17-d)*j,0)))
					cir1.append(Part.makeCylinder(d/2,t,Vector(R+(17-d)*j,l-R-(17-d)*i,0)))
					cir2.append(Part.makeCylinder(d/2,t,Vector(R+(17-d)*j,R,0)))
					cir3.append(Part.makeCylinder(d/2,t,Vector(l-R,l-R-(17-d)*j,0)))
			cir4=Part.makeCylinder(d/2,t,Vector(25.5,l-25.5,0))


			for i in cir:
				P = P.cut(i)
			for i in cir1:
				P = P.cut(i)
			for i in cir2:
				P = P.cut(i)
			for i in cir3:
				P = P.cut(i)
			P=P.cut(cir4)

			shape=doc.addObject("Part::Feature")
			shape.Shape=P
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 1.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


	def onPopupDes8(self):
		if self.popup2.currentText() == u"역각브래킷":
			doc=App.newDocument()

			x = 13.7
			x1 = 12
			y = 12.7
			h = 14.4
			t = 0.85
			d = 4.11
			i = 0
			n = 2

			plate1 = Part.makeBox(x,y,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(y/2-0.001, [plate1.Edges[0],plate1.Edges[2]])
			plate2 = Part.makeBox(t,y,h,Vector(x,0,0),Vector(0,0,1))
			plate1 = plate1.fuse(plate2)
			plate3 = Part.makeBox(x1+t,y,t,Vector(x,0,h),Vector(0,0,1))
			plate3 = plate3.makeFillet(y/2-0.001, [plate3.Edges[4],plate3.Edges[6]])
			plate1 = plate1.fuse(plate3)

			plate4 = Part.makeBox(d,d,t,Vector((x-d)/2,(y-d)/2,0))
			plate1 = plate1.cut(plate4)

			cir1 = Part.makeCylinder(d/2,t,Vector(x,y/2,h/2),Vector(1,0,0))
			plate1 = plate1.cut(cir1)
			cir2 = Part.makeCylinder(d/2,t,Vector((x-d)/2,y/2,0))
			plate1 = plate1.cut(cir2)
			cir3 = Part.makeCylinder(d/2,t,Vector((x+d)/2,y/2,0))
			plate1 = plate1.cut(cir3)
			cir4 = Part.makeCylinder(d/2,t,Vector(x+x1/2,y/2,h))
			plate1 = plate1.cut(cir4)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0,1.0,1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

		elif self.popup2.currentText() == u"ㄷ형 브래킷(소)":

			doc=App.newDocument()

			x=15
			z=12.7
			y=12.5
			r=4.22
			t=0.77

			plate1=Part.makeBox(x,t,z,Vector(0,-t,0),Vector(0,0,1))
			plate2=Part.makeBox(t,y-t,z,Vector(x-t,0,0),Vector(0,0,1))
			plate3=Part.makeBox(t,y-t,z,Vector(0,0,0),Vector(0,0,1))

			plate1=plate1.makeFillet(0.75,[plate1.Edges[0],plate1.Edges[4]])
			plate2=plate2.makeFillet(3,[plate2.Edges[10],plate2.Edges[11]])
			plate3=plate3.makeFillet(3,[plate3.Edges[10],plate3.Edges[11]])


			cir1 = Part.makeCylinder(2.11,t,Vector(x/2,-t,z/2),Vector(0,1,0))
			plate1=plate1.cut(cir1)
			cir3 = Part.makeCylinder(2.11,t,Vector(0,8.11,6.35),Vector(1,0,0))
			plate3 = plate3.cut(cir3)
			cir2 = Part.makeCylinder(2.11,t,Vector(x-t,8.11,6.35),Vector(1,0,0))
			plate2 = plate2.cut(cir2)
			plate1= plate1.fuse(plate2)
			plate1= plate1.fuse(plate3)
			#Part.show(plate1)


			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

		elif self.popup2.currentText() == u"ㄷ형 브래킷(대)":
			doc=App.newDocument()

			x=15
			z=12.7
			y=24.7
			r=4.22
			t=0.77

			plate1=Part.makeBox(x,t,z,Vector(0,-t,0),Vector(0,0,1))
			plate2=Part.makeBox(t,y-t,z,Vector(x-t,0,0),Vector(0,0,1))
			plate3=Part.makeBox(t,y-t,z,Vector(0,0,0),Vector(0,0,1))

			plate1=plate1.makeFillet(0.75,[plate1.Edges[0],plate1.Edges[4]])
			plate2=plate2.makeFillet(6.34,[plate2.Edges[10],plate2.Edges[11]])
			plate3=plate3.makeFillet(6.34,[plate3.Edges[10],plate3.Edges[11]])


			cir1 = Part.makeCylinder(2.11,t,Vector(x/2,-t,z/2),Vector(0,1,0))
			plate1=plate1.cut(cir1)
			cir3 = Part.makeCylinder(2.11,t,Vector(0,6.41,6.35),Vector(1,0,0))
			plate3 = plate3.cut(cir3)
			cir2 = Part.makeCylinder(2.11,t,Vector(x-t,6.41,6.35),Vector(1,0,0))
			plate2 = plate2.cut(cir2)
			cir4 = Part.makeCylinder(2.11,t,Vector(0,+8.45+2.11+6.41,6.35),Vector(1,0,0))
			plate3 = plate3.cut(cir4)
			cir5 = Part.makeCylinder(2.11,t,Vector(x-t,+8.45+2.11+6.41,6.35),Vector(1,0,0))
			plate2 = plate2.cut(cir5)
			plate1= plate1.fuse(plate2)
			plate1= plate1.fuse(plate3)
			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

		elif self.popup2.currentText() == u"ㄱ형 브래킷(소)":

			doc=App.newDocument()
			x=13.5
			z=12.7
			y=11
			r=4.18
			t=0.75

			plate1=Part.makeBox(x,t,z,Vector(0,-t,0),Vector(0,0,1))
			plate2=Part.makeBox(t,y-t,z,Vector(0,0,0),Vector(0,0,1))

			plate1=plate1.makeFillet(6.34,[plate1.Edges[5],plate1.Edges[7]])
			plate2=plate2.makeFillet(6.34,[plate2.Edges[10],plate2.Edges[11]])

			cir1 = Part.makeCylinder(2.09,t,Vector(4.8,-t,6.385),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			cir1 = Part.makeCylinder(2.09,t,Vector(9.12,-t,6.385),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			box = Part.makeBox(4.18,4.18,4.18,Vector(6.96-2.09,-t,6.385-2.09),Vector(0,1,0))
			plate1 = plate1.cut(box)
			cir2 = Part.makeCylinder(2.09,t,Vector(0,6.075,6.385),Vector(1,0,0))
			plate2 = plate2.cut(cir2)

			plate1= plate1.fuse(plate2)
			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"ㄱ형 브래킷(대)":

			doc=App.newDocument()
			x=26.4
			z=13
			y=12.3
			r=4.18
			t=0.75

			plate1=Part.makeBox(x,t,z,Vector(0,-t,0),Vector(0,0,1))
			plate2=Part.makeBox(t,y-t,z,Vector(0,0,0),Vector(0,0,1))

			plate1=plate1.makeFillet(6.49,[plate1.Edges[5],plate1.Edges[7]])
			plate2=plate2.makeFillet(6.49,[plate2.Edges[10],plate2.Edges[11]])

			cir1 = Part.makeCylinder(2.09,t,Vector(x-8.61,-t,6.5),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			cir1 = Part.makeCylinder(2.09,t,Vector(x-4.29,-t,6.5),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			box = Part.makeBox(4.18,4.18,4.18,Vector(x-8.61,-t,6.5-2.09),Vector(0,1,0))
			plate1 = plate1.cut(box)
			cir1 = Part.makeCylinder(2.09,t,Vector(7.19,-t,6.5),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			cir2 = Part.makeCylinder(2.09,t,Vector(0,y-6.05,6.5),Vector(1,0,0))
			plate2 = plate2.cut(cir2)

			plate1= plate1.fuse(plate2)
			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"ㄱ형 브래킷 2X2":
			doc=App.newDocument()
			x=26.3
			z=25.5
			y=12.18
			r=4
			t=0.7

			plate1=Part.makeBox(x,t,z,Vector(0,-t,0),Vector(0,0,1))
			plate2=Part.makeBox(t,y-t,z,Vector(0,0,0),Vector(0,0,1))

			plate1=plate1.makeFillet(6.4,[plate1.Edges[5],plate1.Edges[7]])
			plate2=plate2.makeFillet(6.4,[plate2.Edges[10],plate2.Edges[11]])

			cir1 = Part.makeCylinder(2,t,Vector(x-6.25,-t,6.38),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			cir1 = Part.makeCylinder(2,t,Vector(7.25,-t,6.38),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			cir1 = Part.makeCylinder(2,t,Vector(x-6.25,-t,z-6.38),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			cir1 = Part.makeCylinder(2,t,Vector(7.25,-t,z-6.38),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			cir2 = Part.makeCylinder(2,t,Vector(0,y-6.05,6.38),Vector(1,0,0))
			plate2 = plate2.cut(cir2)
			cir2 = Part.makeCylinder(2,t,Vector(0,y-6.05,z-6.38),Vector(1,0,0))
			plate2 = plate2.cut(cir2)
			plate1= plate1.fuse(plate2)
			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"둔각브래킷":

			doc=App.newDocument()
			x=13.5
			z=12.45
			y=10.75
			r=4.18
			t=0.75

			plate1=Part.makeBox(x,t,z,Vector(0,0,0),Vector(0,0,1))
			plate2=Part.makeBox(t,z,y,Vector(0,0,z),Vector(-1,1,0))

			plate1=plate1.makeFillet(6.22,[plate1.Edges[5],plate1.Edges[7]])
			plate2=plate2.makeFillet(6.22,[plate2.Edges[9],plate2.Edges[11]])

			cir1 = Part.makeCylinder(2.09,t,Vector(4.69,0,6.385),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			cir1 = Part.makeCylinder(2.09,t,Vector(x-4.47,0,6.385),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			box = Part.makeBox(4.18,4.18,4.18,Vector(6.96-2.09,-t,6.385-2.09),Vector(0,1,0))
			plate1 = plate1.cut(box)
			cir2 = Part.makeCylinder(2.09,10,Vector(-4,6.225,6.225),Vector(-1,-1,0))
			plate2 = plate2.cut(cir2)

			plate1= plate1.fuse(plate2)
			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"삼각브래킷":
			doc=App.newDocument()

			x=12.7
			t=0.7
			f=6.3
			d=4.2

			box = Part.makeBox(x,x,t,Vector(0,0,0))
			box = box.makeFillet(f,[box.Edges[6]])
			box2 = Part.makeBox(x,x,t,Vector(-12.7,0,0))
			box2 = box2.makeFillet(f,[box2.Edges[2],box2.Edges[0]])
			box3 = Part.makeBox(x,x,t,Vector(0,-12.7,0))
			box3 = box3.makeFillet(f,[box3.Edges[0],box3.Edges[4]])
			box4 = Part.makeBox(x,x,t,Vector(-12.7,-12.7,0))
			box4 = box4.makeFillet(f,[box4.Edges[6]])
			box5 = Part.makeBox(x,x,t,Vector(-12.7,-12.7,0))
			box = box.fuse(box2)
			box = box.fuse(box3)
			box = box.fuse(box4)
			box = box.fuse(box5)
			box = box.cut(box4)
			cir1 = Part.makeCylinder(d/2,t,Vector(6.35,6.35,0))
			box = box.cut(cir1)
			cir2 = Part.makeCylinder(d/2,t,Vector(-6.35,6.35,0))
			box = box.cut(cir2)
			cir3 = Part.makeCylinder(d/2,t,Vector(6.35,-6.35,0))
			box = box.cut(cir3)
			#Part.show(box)
			shape=doc.addObject("Part::Feature")
			shape.Shape=box
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"모서리브래킷(좌)":
			doc=App.newDocument()

			x = 12.7
			y = 12.7
			t = 0.7
			h = 13.4
			d = 4.2

			plate1 = Part.makeBox(x,y,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(y/2-0.001, [plate1.Edges[0],plate1.Edges[2]])
			plate2 = Part.makeBox(t,y,h,Vector(x,0,0),Vector(0,0,1))
			plate2 = plate2.makeFillet(y/2-0.001, [plate2.Edges[11]])
			plate1 = plate1.fuse(plate2)
			plate3 = Part.makeBox(x,t,y,Vector (x,-t,t),Vector(0,0,1))
			plate3 = plate3.makeFillet(y/2-0.01, [plate3.Edges[5],plate3.Edges[7]])
			plate1 = plate1.fuse(plate3)

			cir1 = Part.makeCylinder(d/2,t,Vector(x/2,y/2,0))
			plate1 = plate1.cut(cir1)
			cir2 = Part.makeCylinder(d/2,t,Vector(x,y/2,y/2+t),Vector(1,0,0))
			plate1 = plate1.cut(cir2)
			plate4 = Part.makeBox(d,d,t,Vector(x+3.95,0,y/2+t+2.1),Vector(0,-1,0))
			cir3 = Part.makeCylinder(d/2,t,Vector(x+8.15,0,y/2+t),Vector(0,-1,0))
			cir4 = Part.makeCylinder(d/2,t,Vector(x+3.95,0,y/2+t),Vector(0,-1,0))
			plate1 = plate1.cut(plate4)
			plate1 = plate1.cut(cir4)
			plate1 = plate1.cut(cir3)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

		elif self.popup2.currentText() == u"모서리브래킷(우)":
			doc=App.newDocument()

			x = 12.7
			y = 12.7
			t = 0.7
			h = 13.4
			d = 4.2

			plate1 = Part.makeBox(x,y,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(y/2-0.001, [plate1.Edges[0],plate1.Edges[2]])
			plate2 = Part.makeBox(t,y,h,Vector(x,0,0),Vector(0,0,1))
			plate2 = plate2.makeFillet(y/2-0.001, [plate2.Edges[9]])
			plate1 = plate1.fuse(plate2)
			plate3 = Part.makeBox(x,t,y,Vector (x,y,t),Vector(0,0,1))
			plate3 = plate3.makeFillet(y/2-0.01, [plate3.Edges[5],plate3.Edges[7]])
			plate1 = plate1.fuse(plate3)

			cir1 = Part.makeCylinder(d/2,t,Vector(x/2,y/2,0))
			plate1 = plate1.cut(cir1)
			cir2 = Part.makeCylinder(d/2,t,Vector(x,y/2,y/2+t),Vector(1,0,0))
			plate1 = plate1.cut(cir2)
			plate4 = Part.makeBox(d,d,t,Vector(x+3.95,y,y/2+t-2.1),Vector(0,1,0))
			cir3 = Part.makeCylinder(d/2,t,Vector(x+8.15,y,y/2+t),Vector(0,1,0))
			cir4 = Part.makeCylinder(d/2,t,Vector(x+3.95,y,y/2+t),Vector(0,1,0))
			plate1 = plate1.cut(plate4)
			plate1 = plate1.cut(cir4)
			plate1 = plate1.cut(cir3)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"조향브래킷":
			doc=App.newDocument()

			x = 36.5
			y = 12.8
			t = 1.20
			h = 17.9
			d = 4.2

			plate1 = Part.makeBox(x,y,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(y/2-0.001, [plate1.Edges[0],plate1.Edges[2], plate1.Edges[4],plate1.Edges[6]])
			plate2 = Part.makeBox(y,y,t,Vector(11.85,12.8,0),Vector(0,0,1))
			plate2 = plate2.makeFillet(y/2-0.001, [plate2.Edges[2],plate2.Edges[6]])
			plate1 = plate1.fuse(plate2)
			plate3 = Part.makeBox(y,t,h,Vector (11.8,0,0),Vector(0,0,1))
			plate1 = plate1.fuse(plate3)
			plate4 = Part.makeBox(y,11.5,t,Vector(11.8,0,h-t),Vector(0,0,1))
			plate4 = plate4.makeFillet(y/2-0.001, [plate4.Edges[2],plate4.Edges[6]])
			plate1 = plate1.fuse(plate4)

			cir1 = Part.makeCylinder(d/2,t,Vector(5.6,y/2,0))
			cir2 = Part.makeCylinder(d/2,t,Vector(x/2,y/2,0))
			cir3 = Part.makeCylinder(d/2,t,Vector(36.5-5.6,y/2,0))
			cir4 = Part.makeCylinder(d/2,t,Vector(x/2,18.9,0))
			cir5 = Part.makeCylinder(d/2,t,Vector(x/2,y/2,h-t))
			cir6 = Part.makeCylinder(d/2,t,Vector(x/2,0,h/2), Vector(0,1,0))

			plate1 = plate1.cut(cir1)
			plate1 = plate1.cut(cir2)
			plate1 = plate1.cut(cir3)
			plate1 = plate1.cut(cir4)
			plate1 = plate1.cut(cir5)
			plate1 = plate1.cut(cir6)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

	def onPopupDes9(self):
		if self.popup2.currentText() == u"이음판":
			doc=App.newDocument()

			x=23.5
			y=12.78
			t=0.77
			f=6.35

			plate=Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate=plate.makeFillet(f, [plate.Edges[0],plate.Edges[2],plate.Edges[4],plate.Edges[6]])

			cir1 = Part.makeCylinder(2.11,t,Vector(4.41,-6.31,0))
			cir2 = Part.makeCylinder(2.11,t,Vector(8.74,-6.31,0))
			cir3 = Part.makeCylinder(2.11,t,Vector(18.64,-6.31,0))
			box = Part.makeBox(4.22,4.22,t,Vector(4.465,-8.42,0))

			plate = plate.cut(cir1)
			plate = plate.cut(cir2)
			plate = plate.cut(cir3)
			plate = plate.cut(box)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

		elif self.popup2.currentText() == u"휠판 - 8":
			doc=App.newDocument()

			D1 = 36
			D2 = 9.43
			h = 9.11
			h1 = 0.5
			d = 4.11
			d1 = 3.33
			t = 0.7

			i = 0
			n = 2

			circle = Part.makeCylinder(D1/2,t,Vector(0,0,0))
			circle1 = Part.makeCylinder(D2/2,h,Vector(0,0,-h1))
			circle = circle.fuse(circle1)

			cir1 = Part.makeCylinder(d1/2,D2,Vector(-D2/2,0,6.75-d/2),Vector(1,0,0))
			circle = circle.cut(cir1)
			cir2 = Part.makeCylinder(d/2,h,Vector(0,0,-h1))
			circle = circle.cut(cir2)

			cir3 = []
			cir4 = []
			for i in range(n):
				for j in range(n):
					cir3.append(Part.makeCylinder(d/2,t,Vector((27.7-d)/2-(27.7-d)*i,(14-d)/2-(14-d)*j,0)))

			for i in cir3:
				circle = circle.cut(i)

			for i in range(n):
				for j in range(n):
					cir4.append(Part.makeCylinder(d/2,t,Vector((14-d)/2-(14-d)*j,(27.7-d)/2-(27.7-d)*i,0)))

			for i in cir4:
				circle = circle.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

		elif self.popup2.currentText() == u"반원판":
			doc=App.newDocument()

			D = 64
			d = 4.11
			f = 6
			t = 0.97
			i = 0
			n = 5
			cir = []

			plate1 = Part.makeBox(D,D/2,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(D/2-0.01, [plate1.Edges[2],plate1.Edges[6]])

			plate2 = Part.makeBox(D,f,t,Vector(0,-f,0))
			plate2 = plate2.makeFillet(f-0.01, [plate2.Edges[0],plate2.Edges[4]])

			plate1 = plate1.fuse(plate2)

			for i in range(n):
				cir.append(Part.makeCylinder(d/2, t, Vector(f+12.7*i,0,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			circle1 = Part.makeCylinder(d/2, t, Vector(f+12.7*2,12.7,0))
			circle2 = Part.makeCylinder(d/2, t, Vector(f+12.7*2,12.7*2,0))
			plate1 = plate1.cut(circle1)
			plate1 = plate1.cut(circle2)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


	def onPopupDes10(self):
		if self.popup2.currentText() == u"볼트 0.6cm":
			doc=App.newDocument()

			# 기본형상 hexagon, circle
			s_hex=5.6 #hexagon_diameter
			cir_hex=4 #circle_diameter
			k_hex=2.1 #height

			mhex=Base.Matrix()
			mhex.rotateZ(math.radians(60.0))
			polygon = []
			vhex=Base.Vector(s_hex/math.sqrt(3.0),0.0,-k_hex)
			for i in range(6):
				polygon.append(vhex)
				vhex = mhex.multiply(vhex)
			polygon.append(vhex)
			hexagon = Part.makePolygon(polygon)
			face=Part.Face(hexagon)
			exHex=face.extrude(Base.Vector(0.0,0.0,k_hex)) #높이

			d=6
			circ=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))
			exHex=exHex.fuse(circ)

			# 나사선 helix
			helix = Part.makeHelix(0.797,15,2)             #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((1.7,0,-0.125), (1.7,0,0.125))
			edge2 = Part.makeLine((1.7,0,0.125), (2.3,0,0.419))
			edge3 = Part.makeLine((2.3,0,0.419), (2.3,0,-0.419))
			edge4 = Part.makeLine((2.3,0,-0.419), (1.7,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)
		elif self.popup2.currentText() == u"볼트 1.3cm":
			doc=App.newDocument()

			# 기본형상 hexagon, circle
			s_hex=5.6 #hexagon_diameter
			cir_hex=4 #circle_diameter
			k_hex=2.1 #height

			mhex=Base.Matrix()
			mhex.rotateZ(math.radians(60.0))
			polygon = []
			vhex=Base.Vector(s_hex/math.sqrt(3.0),0.0,-k_hex)
			for i in range(6):
				polygon.append(vhex)
				vhex = mhex.multiply(vhex)
			polygon.append(vhex)
			hexagon = Part.makePolygon(polygon)
			face=Part.Face(hexagon)
			exHex=face.extrude(Base.Vector(0.0,0.0,k_hex)) #높이

			d=13
			circ=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))
			exHex=exHex.fuse(circ)

			# 나사선 helix
			helix = Part.makeHelix(0.797,15,2)             #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((1.7,0,-0.125), (1.7,0,0.125))
			edge2 = Part.makeLine((1.7,0,0.125), (2.3,0,0.419))
			edge3 = Part.makeLine((2.3,0,0.419), (2.3,0,-0.419))
			edge4 = Part.makeLine((2.3,0,-0.419), (1.7,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)

		elif self.popup2.currentText() == u"볼트 2cm":
			doc=App.newDocument()

			# 기본형상 hexagon, circle
			s_hex=5.6 #hexagon_diameter
			cir_hex=4 #circle_diameter
			k_hex=2.1 #height

			mhex=Base.Matrix()
			mhex.rotateZ(math.radians(60.0))
			polygon = []
			vhex=Base.Vector(s_hex/math.sqrt(3.0),0.0,-k_hex)
			for i in range(6):
				polygon.append(vhex)
				vhex = mhex.multiply(vhex)
			polygon.append(vhex)
			hexagon = Part.makePolygon(polygon)
			face=Part.Face(hexagon)
			exHex=face.extrude(Base.Vector(0.0,0.0,k_hex)) #높이

			d=20
			circ=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))
			exHex=exHex.fuse(circ)

			# 나사선 helix
			helix = Part.makeHelix(0.797,30,2)             #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((1.7,0,-0.125), (1.7,0,0.125))
			edge2 = Part.makeLine((1.7,0,0.125), (2.3,0,0.419))
			edge3 = Part.makeLine((2.3,0,0.419), (2.3,0,-0.419))
			edge4 = Part.makeLine((2.3,0,-0.419), (1.7,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)

		elif self.popup2.currentText() == u"볼트 3cm":
			doc=App.newDocument()

			# 기본형상 hexagon, circle
			s_hex=5.6 #hexagon_diameter
			cir_hex=4 #circle_diameter
			k_hex=2.1 #height

			mhex=Base.Matrix()
			mhex.rotateZ(math.radians(60.0))
			polygon = []
			vhex=Base.Vector(s_hex/math.sqrt(3.0),0.0,-k_hex)
			for i in range(6):
				polygon.append(vhex)
				vhex = mhex.multiply(vhex)
			polygon.append(vhex)
			hexagon = Part.makePolygon(polygon)
			face=Part.Face(hexagon)
			exHex=face.extrude(Base.Vector(0.0,0.0,k_hex)) #높이

			d=30
			circ=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))
			exHex=exHex.fuse(circ)

			# 나사선 helix
			helix = Part.makeHelix(0.797,30,2)             #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((1.7,0,-0.125), (1.7,0,0.125))
			edge2 = Part.makeLine((1.7,0,0.125), (2.3,0,0.419))
			edge3 = Part.makeLine((2.3,0,0.419), (2.3,0,-0.419))
			edge4 = Part.makeLine((2.3,0,-0.419), (1.7,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)

		elif self.popup2.currentText() == u"사각머리볼트 0.8cm":
			doc=App.newDocument()

			# 기본형상 box
			cir_hex=4 #circle_diameter

			exHex = Part.makeBox(5.5,5.5,1.4,Vector(-5.5/2,-5.5/2,-1.4))

			d=8
			circ=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))
			exHex=exHex.fuse(circ)

			# 나사선 helix
			helix = Part.makeHelix(0.797,30,2)             #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((1.7,0,-0.125), (1.7,0,0.125))
			edge2 = Part.makeLine((1.7,0,0.125), (2.3,0,0.419))
			edge3 = Part.makeLine((2.3,0,0.419), (2.3,0,-0.419))
			edge4 = Part.makeLine((2.3,0,-0.419), (1.7,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)
	def onPopupDes11(self):
		if self.popup2.currentText() == u"너트":
			doc=App.newDocument()

			# 기본형상 hexagon, circle
			s_hex=7.9 #hexagon_diameter
			cir_hex=4 #circle_diameter
			k_hex=2.1 #height

			mhex=Base.Matrix()
			mhex.rotateZ(math.radians(60.0))
			polygon = []
			vhex=Base.Vector(s_hex/math.sqrt(3.0),0.0,0.0)
			for i in range(6):
				polygon.append(vhex)
				vhex = mhex.multiply(vhex)
			polygon.append(vhex)
			hexagon = Part.makePolygon(polygon)
			circ=Part.makeCircle(cir_hex/2.0)
			face=Part.Face([hexagon, Part.Wire(circ)]) #hexagon, Part.wire(circ) 순서에 따라 형상이 바뀜
			exHex=face.extrude(Base.Vector(0.0,0.0,k_hex)) #높이

			# 나사선 helix
			helix = Part.makeHelix(0.797,3,2)             #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((2.3,0,-0.125), (2.3,0,0.125))
			edge2 = Part.makeLine((2.3,0,0.125), (1.7,0,0.419))
			edge3 = Part.makeLine((1.7,0,0.419), (1.7,0,-0.419))
			edge4 = Part.makeLine((1.7,0,-0.419), (2.3,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)

	def onPopupDes12(self):
		if self.popup2.currentText() == u"와셔(소)":
			doc=App.newDocument()

			D = 9.2
			d = 4.25
			t = 1.2

			plate1 = Part.makeCylinder(D/2,t,Vector(0,0,0))
			plate2 = Part.makeCylinder(d/2,t,Vector(0,0,0))
			plate1 = plate1.cut(plate2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

		elif self.popup2.currentText() == u"와셔(대)":
			doc=App.newDocument()

			D = 18.5
			d = 4.25
			t = 0.7

			plate1 = Part.makeCylinder(D/2,t,Vector(0,0,0))
			plate2 = Part.makeCylinder(d/2,t,Vector(0,0,0))
			plate1 = plate1.cut(plate2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

	def onPopupDes13(self):
		if self.popup2.currentText() == u"멈춤나사":

			doc=App.newDocument()

			# 기본형상 hexagon, circle
			s_hex=5.6 #hexagon_diameter
			cir_hex=4 #circle_diameter
			k_hex=2.1 #height

			exHex=Part.makeCylinder(s_hex/2,k_hex,Vector(0,0,-k_hex))

			d=3.8
			circ=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))
			exHex=exHex.fuse(circ)

			# 나사선 helix
			helix = Part.makeHelix(0.797,30,2)             #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((1.7,0,-0.125), (1.7,0,0.125))
			edge2 = Part.makeLine((1.7,0,0.125), (2.3,0,0.419))
			edge3 = Part.makeLine((2.3,0,0.419), (2.3,0,-0.419))
			edge4 = Part.makeLine((2.3,0,-0.419), (1.7,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)

		elif self.popup2.currentText() == u"구동기어 멈춤나사":
			doc=App.newDocument()

			# 기본형상 hexagon, circle
			s_hex=5.6 #hexagon_diameter
			cir_hex=3.5 #circle_diameter
			k_hex=2.1 #height

			exHex=Part.makeCylinder(s_hex/2,k_hex,Vector(0,0,-k_hex))

			d=3.5
			circ=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))
			exHex=exHex.fuse(circ)

			# 나사선 helix
			helix = Part.makeHelix(0.797,30,2)             #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((1.5,0,-0.125), (1.5,0,0.125))
			edge2 = Part.makeLine((1.5,0,0.125), (2.1,0,0.419))
			edge3 = Part.makeLine((2.1,0,0.419), (2.1,0,-0.419))
			edge4 = Part.makeLine((2.1,0,-0.419), (1.5,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(0.6,0.22,0.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)

	def onPopupDes14(self):
		if self.popup2.currentText() == u"평기어(소)":

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=0.65, z=57, alpha=20 * pi / 180., clearence=0.75, shift=0., beta=0., undercut=False, simple=False, height=5., backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                d = 4.11
			                self.cir = Part.makeCylinder(17,4,Vector(0,0,0))
			                self.cir2 = Part.makeCylinder(5.4,5,Vector(0,0,-1))
			                self.cir3 = Part.makeCylinder(4.7,7.6,Vector(0,0,-8.6))
			                self.cir4 = Part.makeCylinder(d/2,13.6,Vector(0,0,-8.6))
			                self.cir_1 = Part.makeCylinder(d/2,13.6,Vector(12.5,0,0))
			                self.cir_2 = Part.makeCylinder(d/2,13.6,Vector(-12.5,0,0))
			                self.cir_3 = Part.makeCylinder(d/2,13.6,Vector(0,12.5,0))
			                self.cir_4 = Part.makeCylinder(d/2,13.6,Vector(0,-12.5,0))
			                self.cir_5 = Part.makeCylinder(d/2,13.6,Vector(12.5*cos(45 * pi / 180.),12.5*sin(45 * pi / 180.),0))
			                self.cir_6 = Part.makeCylinder(d/2,13.6,Vector(-12.5*cos(45 * pi / 180.),12.5*sin(45 * pi / 180.),0))
			                self.cir_7 = Part.makeCylinder(d/2,13.6,Vector(12.5*cos(45 * pi / 180.),-12.5*sin(45 * pi / 180.),0))
			                self.cir_8 = Part.makeCylinder(d/2,13.6,Vector(-12.5*cos(45 * pi / 180.),-12.5*sin(45 * pi / 180.),0))
			                self.cir_0 = Part.makeCylinder(d/2,13.6,Vector(0,-6.8,-4.6),Vector(0,1,0))
			                self.Shape = self.Shape.cut(self.cir)
			                self.Shape = self.Shape.fuse(self.cir2)
			                self.Shape = self.Shape.fuse(self.cir3)
			                self.Shape = self.Shape.cut(self.cir4)
			                self.Shape = self.Shape.cut(self.cir_1)
			                self.Shape = self.Shape.cut(self.cir_2)
			                self.Shape = self.Shape.cut(self.cir_3)
			                self.Shape = self.Shape.cut(self.cir_4)
			                self.Shape = self.Shape.cut(self.cir_5)
			                self.Shape = self.Shape.cut(self.cir_6)
			                self.Shape = self.Shape.cut(self.cir_7)
			                self.Shape = self.Shape.cut(self.cir_8)
			                self.Shape = self.Shape.cut(self.cir_0)
			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])

			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()

		elif self.popup2.currentText() == u"피니언기어":

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=0.736, z=19, alpha=20 * pi / 180., clearence=0, shift=0., beta=0., undercut=False, simple=False, height=5.6, backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                d = 9.48
			                d1 = 4.11
			                d2 = 3.11
			                h = 14.5
			                self.cir = Part.makeCylinder(d/2,h-5.6,Vector(0,0,5.6))
			                self.cir2 = Part.makeCylinder(d1/2,h,Vector(0,0,0))
			                self.cir3 = Part.makeCylinder(d2/2,d,Vector(0,-d/2,10.8),Vector(0,1,0))
			                self.Shape = self.Shape.fuse(self.cir)
			                self.Shape = self.Shape.cut(self.cir2)
			                self.Shape = self.Shape.cut(self.cir3)

			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])


			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"평기어(대)":

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=0.681, z=95, alpha=20 * pi / 180., clearence=0, shift=0., beta=0., undercut=False, simple=False, height=3.27, backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                d = 12.43
			                d1 = 9.48
			                d2 = 4.11
			                d3 = 3.11
			                t = 3.27
			                h = 6.16
			                h1 = 14
			                x =8.5
			                x1 = 17.1
			                y = 16.7
			                self.cir = Part.makeCylinder(d/2,h,Vector(0,0,-1.4))
			                self.cir2 = Part.makeCylinder(d1/2,h1-1.4,Vector(0,0,1.4))
			                self.cir3 = Part.makeCylinder(d2/2,h1+1.4,Vector(0,0,-1.4))
			                self.cir4 = Part.makeCylinder(d3/2,d1,Vector(0,-d1/2,d1),Vector(0,1,0))
			                self.cir5 = Part.makeCylinder(d2/2,t,Vector(-x,x,0))
			                self.cir6 = Part.makeCylinder(d2/2,t,Vector(x,x,0))
			                self.cir7 = Part.makeCylinder(d2/2,t,Vector(x,-x,0))
			                self.cir8 = Part.makeCylinder(d2/2,t,Vector(-x,-x,0))
			                self.cir9 = Part.makeCylinder(d2/2,t,Vector(-x1,x1,0))
			                self.cir10 = Part.makeCylinder(d2/2,t,Vector(x1,x1,0))
			                self.cir11 = Part.makeCylinder(d2/2,t,Vector(x1,-x1,0))
			                self.cir12 = Part.makeCylinder(d2/2,t,Vector(-x1,-x1,0))
			                self.box = Part.makeBox(d2,y-d2,t,Vector(-d2/2,x+d2,0))
			                self.box1 = Part.makeBox(d2,y-d2,t,Vector(-d2/2,-x-d2-(y-d2),0))
			                self.box2 = Part.makeBox(y-d2,d2,t,Vector(x+d2,-d2/2,0))
			                self.box3 = Part.makeBox(y-d2,d2,t,Vector(-x-d2-(y-d2),-d2/2,0))
			                self.cir13 = Part.makeCylinder(d2/2,t,Vector(0,x+d2,0))
			                self.cir14 = Part.makeCylinder(d2/2,t,Vector(0,x+y,0))
			                self.cir15 = Part.makeCylinder(d2/2,t,Vector(0,-x-d2,0))
			                self.cir16 = Part.makeCylinder(d2/2,t,Vector(0,-x-y,0))
			                self.cir17 = Part.makeCylinder(d2/2,t,Vector(x+d2,0,0))
			                self.cir18 = Part.makeCylinder(d2/2,t,Vector(x+y,0,0))
			                self.cir19 = Part.makeCylinder(d2/2,t,Vector(-x-d2,0,0))
			                self.cir20 = Part.makeCylinder(d2/2,t,Vector(-x-y,0,0))

			                self.Shape = self.Shape.fuse(self.cir)
			                self.Shape = self.Shape.fuse(self.cir2)
			                self.Shape = self.Shape.cut(self.cir3)
			                self.Shape = self.Shape.cut(self.cir4)
			                self.Shape = self.Shape.cut(self.cir5)
			                self.Shape = self.Shape.cut(self.cir6)
			                self.Shape = self.Shape.cut(self.cir7)
			                self.Shape = self.Shape.cut(self.cir8)
			                self.Shape = self.Shape.cut(self.cir9)
			                self.Shape = self.Shape.cut(self.cir10)
			                self.Shape = self.Shape.cut(self.cir11)
			                self.Shape = self.Shape.cut(self.cir12)
			                self.Shape = self.Shape.cut(self.box)
			                self.Shape = self.Shape.cut(self.box1)
			                self.Shape = self.Shape.cut(self.box2)
			                self.Shape = self.Shape.cut(self.box3)
			                self.Shape = self.Shape.cut(self.cir13)
			                self.Shape = self.Shape.cut(self.cir14)
			                self.Shape = self.Shape.cut(self.cir15)
			                self.Shape = self.Shape.cut(self.cir16)
			                self.Shape = self.Shape.cut(self.cir17)
			                self.Shape = self.Shape.cut(self.cir18)
			                self.Shape = self.Shape.cut(self.cir19)
			                self.Shape = self.Shape.cut(self.cir20)
			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])


			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"다목적기어":
			doc=App.newDocument()

			plate1 = Part.makeCylinder(10.0,3.0,Vector(0,0,-1.5),Vector(0,0,1),360)
			plate2 = Part.makeCylinder(4.75,12.5,Vector(0,0,0),Vector(0,0,1),360)

			plate1 = plate1.fuse(plate2)

			inC = Part.makeCylinder(2.0,50,Vector(0,0,-25),Vector(0,0,1))
			plate1 = plate1.cut(inC)

			outC=Part.makeCylinder(3.29/2,50,Vector(0,-25.0,9.5),Vector(0,1,0))
			plate1=plate1.cut(outC)

			teeth = Part.makePolygon([(9,0,1.5),(10,0,3.3),(14,0,3.3),(14,0,1.5),(10,0,0),(9,0,1.5)])
			face = Part.Face(teeth)
			ee1 = face.extrude(Vector(0,1,0))

			ee2 = ee1.mirror(Vector(0,0,0),Vector(0,1,0))
			ee1 = ee1.fuse(ee2)

			ee3 = ee1.mirror(Vector(0,0,0),Vector(0,0,1))
			ee1 = ee1.fuse(ee3)

			plate1 = plate1.fuse(ee1)

			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"크라운기어":
			doc=App.newDocument()

			R1 = 18
			R2 = 2.0

			base1 = Part.makeCylinder(R1,5.3,Vector(0,0,0),Vector(0,-1,0),360)

			base2 = Part.makeCylinder(4.75,9.5,Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.fuse(base2)

			outC = Part.makeCylinder(3.29/2,50,Vector(-25.0,7.0,0),Vector(1,0,0))
			base1 = base1.cut(outC)

			base3 = Part.makeCylinder(6.3,2.0,Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.fuse(base3)

			base4 = Part.makeCylinder(16.0,10.0,Vector(0,-2.0,0),Vector(0,-1,0),360)
			base1 = base1.cut(base4)

			base5 = Part.makeCylinder(6.3,1.0,Vector(0,-2.0,0),Vector(0,-1,0),360)
			base1 = base1.fuse(base5)

			acir1 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			base1 = base1.cut(acir1)
			acir2 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir2.rotate(Vector(0,0,0),Vector(0,1,0),45)
			base1 = base1.cut(acir2)
			acir3 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir3.rotate(Vector(0,0,0),Vector(0,1,0),90)
			base1 = base1.cut(acir3)
			acir4 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir4.rotate(Vector(0,0,0),Vector(0,1,0),135)
			base1 = base1.cut(acir4)
			acir5 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir5.rotate(Vector(0,0,0),Vector(0,1,0),180)
			base1 = base1.cut(acir5)
			acir6 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir6.rotate(Vector(0,0,0),Vector(0,1,0),225)
			base1 = base1.cut(acir6)
			acir7 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir7.rotate(Vector(0,0,0),Vector(0,1,0),270)
			base1 = base1.cut(acir7)
			acir8 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir8.rotate(Vector(0,0,0),Vector(0,1,0),315)
			base1 = base1.cut(acir8)

			inC = Part.makeCylinder(R2,50,Vector(0,-25,0),Vector(0,1,0),360)
			base1 = base1.cut(inC)

			extend1 = Part.makePolygon([(18.0,-5.3+1.3,0),(18.0,-5.3,0.75),(18.0,-5.3,-0.75),(18.0,-5.3+1.3,0)])
			fa2 = Part.Face(extend1)
			p2 = fa2.extrude(Vector(-50,0,0))
			base1 = base1.cut(p2)

			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)

			#Part.show(base1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=base1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"워엄기어":
			doc=App.newDocument()

			# 기본형상
			cir_hex=9.5 #circle_diameter

			d=26.2
			exHex=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,-2.7))
			inC=Part.makeCylinder(4.17/2,d,Vector(0,0,-2.7))
			exHex=exHex.cut(inC)

			# 나사선 helix
			helix = Part.makeHelix(2,15,2) #75넣으면 메모리 문제로 실행 안될 수 있음.            #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((6.95,0,-0.125),(6.95,0,0.125))
			edge2 = Part.makeLine((6.95,0,0.125), (4.45,0,0.419))
			edge3 = Part.makeLine((4.45,0,0.419), (4.45,0,-0.419))
			edge4 = Part.makeLine((4.45,0,-0.419),(6.95,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.fuse(pipe)

			outC=Part.makeCylinder(3.29/2,20,Vector(0,-10,26.2-3.6-2.7),Vector(0,1,0))
			exHex=exHex.cut(outC)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)

		elif self.popup2.currentText() == u"체인기어(소)":

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=2.35, z=12, alpha=20 * pi / 180., clearence=0., shift=0., beta=0., undercut=False, simple=False, height=5.8, backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                d = 4.11
			                d1 = 15.56
			                d2 = 11.4
			                d3 = 9.5
			                d4 = 3.11
			                d5 = 7.62
			                self.cir = Part.makeCylinder(d1/2,4.8,Vector(0,0,1))
			                self.cir2 = Part.makeCylinder(d2/2,4.8,Vector(0,0,1))
			                self.cir3 = Part.makeCylinder(d3/2,8.8,Vector(0,0,5.8))
			                self.cir4 = Part.makeCylinder(d/2,14.6,Vector(0,0,0))
			                self.cir5 = Part.makeCylinder(d4/2,d3,Vector(0,d3/2,d3+d4/2),Vector(0,-1,0))
			                self.cir6 = Part.makeCylinder(d5/2,0.5,Vector(0,0,0))

			                self.Shape = self.Shape.cut(self.cir)
			                self.Shape = self.Shape.fuse(self.cir2)
			                self.Shape = self.Shape.fuse(self.cir3)
			                self.Shape = self.Shape.cut(self.cir4)
			                self.Shape = self.Shape.cut(self.cir5)
			                self.Shape = self.Shape.cut(self.cir6)

			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(1.0, 0.0, 0.0)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])

			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()

		elif self.popup2.currentText() == u"체인기어(대)":

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=2.18, z=25, alpha=20 * pi / 180., clearence=0., shift=0., beta=0., undercut=False, simple=False, height=6.36, backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                d = 4.11
			                d1 = 41.5
			                d2 = 10.8
			                d3 = 9.5
			                d4 = 3.11
			                y = 12.75
			                y1 = 17.89
			                t = 6.36-2
			                self.cir = Part.makeCylinder(d1/2,4.36,Vector(0,0,2))
			                self.cir2 = Part.makeCylinder(d2/2,5.86,Vector(0,0,2))
			                self.cir3 = Part.makeCylinder(d3/2,7.64,Vector(0,0,5.86))
			                self.cir4 = Part.makeCylinder(d/2,15.5,Vector(0,0,0))
			                self.cir_1 = Part.makeCylinder(d/2,t,Vector(y,0,0))
			                self.cir_2 = Part.makeCylinder(d/2,t,Vector(-y,0,0))
			                self.cir_3 = Part.makeCylinder(d/2,t,Vector(0,y,0))
			                self.cir_4 = Part.makeCylinder(d/2,t,Vector(0,-y,0))
			                self.cir_5 = Part.makeCylinder(d/2,t,Vector(y1/2,y1/2,0))
			                self.cir_6 = Part.makeCylinder(d/2,t,Vector(-y1/2,y1/2,0))
			                self.cir_7 = Part.makeCylinder(d/2,t,Vector(-y1/2,-y1/2,0))
			                self.cir_8 = Part.makeCylinder(d/2,t,Vector(y1/2,-y1/2,0))
			                self.cir_0 = Part.makeCylinder(d4/2,d2,Vector(0,d2/2,11),Vector(0,-1,0))
			                self.Shape = self.Shape.cut(self.cir)
			                self.Shape = self.Shape.fuse(self.cir2)
			                self.Shape = self.Shape.fuse(self.cir3)
			                self.Shape = self.Shape.cut(self.cir4)
			                self.Shape = self.Shape.cut(self.cir_1)
			                self.Shape = self.Shape.cut(self.cir_2)
			                self.Shape = self.Shape.cut(self.cir_3)
			                self.Shape = self.Shape.cut(self.cir_4)
			                self.Shape = self.Shape.cut(self.cir_5)
			                self.Shape = self.Shape.cut(self.cir_6)
			                self.Shape = self.Shape.cut(self.cir_7)
			                self.Shape = self.Shape.cut(self.cir_8)
			                self.Shape = self.Shape.cut(self.cir_0)
			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(1.0, 0.0, 0.0)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])

			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()
		elif self.popup2.currentText() == u"2단 평기어(소)":

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=0.68, z=58, alpha=20 * pi / 180., clearence=0, shift=0., beta=0., undercut=False, simple=False, height=5.25, backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                self.m_n = 0.73
			                self.z = 19
			                self.height = 6.6
			                self.m = self.m_n / cos(self.beta)
			                self.c = self.clearence * self.m_n
			                self.midpoint = [0., 0]
			                self.d = self.z * self.m
			                self.dw = self.m * self.z
			                self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			                self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			                self.dg = self.d * cos(self.alpha_t)
			                self.phipart = 2 * pi / self.z
			                self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			                self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			                self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			                self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			                self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot = self.involute_rot1 + self.involute_rot2
			                self.involute_start = 0.
			                if self.dg <= self.df:
			                    self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg

			                pts = self.points(self.numpoints)
			                if not self.simple:
			                    wi = []
			                    for i in pts:
			                        out = BSplineCurve()
			                        out.interpolate(map(fcvec, i))
			                        wi.append(out)
			                    s = Wire(Shape(wi).Edges)
			                    wi = []
			                    for i in range(self.z):
			                        rot = App.Matrix()
			                        rot.rotateZ(-i * self.phipart)
			                        tooth_rot = s.transformGeometry(rot)
			                        if i != 0:
			                            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                            pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                            wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                        wi.append(tooth_rot)
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                    wi = Wire(wi)
			                    self.Shapea = wi
			                    if self.beta == 0:
			                        sh = Face(wi)
			                        self.Shapea = sh.extrude(App.Vector(0, 0, self.height))
			                        self.Shapea.translate(Vector(0,0,5.7))
			                    self.Shape = self.Shape.fuse(self.Shapea)

			                cy1 = Part.makeCylinder(16.8,5,Vector(0,0,1.5))
			                cy2 = Part.makeCylinder(7.8,5,Vector(0,0,1.5))
			                cy1 = cy1.cut(cy2)
			                self.Shape = self.Shape.cut(cy1)
			                cy3 = Part.makeCylinder(7.5,0.75,Vector(0,0,5.25))
			                self.Shape = self.Shape.fuse(cy3)
			                cy4 = Part.makeCylinder(3.85,13.5,Vector(0,0,-1))
			                self.Shape = self.Shape.fuse(cy4)

			                cir1 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                self.Shape = self.Shape.cut(cir1)
			                cir2 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir2.rotate(Vector(0,0,0),Vector(0,0,1),45)
			                self.Shape = self.Shape.cut(cir2)
			                cir3 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir3.rotate(Vector(0,0,0),Vector(0,0,1),90)
			                self.Shape = self.Shape.cut(cir3)
			                cir4 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir4.rotate(Vector(0,0,0),Vector(0,0,1),135)
			                self.Shape = self.Shape.cut(cir4)
			                cir5 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir5.rotate(Vector(0,0,0),Vector(0,0,1),180)
			                self.Shape = self.Shape.cut(cir5)
			                cir6 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir6.rotate(Vector(0,0,0),Vector(0,0,1),225)
			                self.Shape = self.Shape.cut(cir6)
			                cir7 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir7.rotate(Vector(0,0,0),Vector(0,0,1),270)
			                self.Shape = self.Shape.cut(cir7)
			                cir8 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir8.rotate(Vector(0,0,0),Vector(0,0,1),315)
			                self.Shape = self.Shape.cut(cir8)

			                base1 = Part.makeCylinder(4.75,7.7,Vector(0,0,12.3),Vector(0,0,1))
			                self.Shape = self.Shape.fuse(base1)

			                base2 = Part.makeCylinder(2.0,50,Vector(0,0,-12.3),Vector(0,0,1))
			                self.Shape = self.Shape.cut(base2)

			                outC=Part.makeCylinder(3.29/2,50,Vector(-25,0,16.0),Vector(1,0,0))

			                self.Shape=self.Shape.cut(outC)

			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])


			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"십자홀 2단평기어":

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=0.67, z=58, alpha=20 * pi / 180., clearence=0, shift=0., beta=0., undercut=False, simple=False, height=4.95, backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                self.m_n = 0.64
			                self.z = 19
			                self.height = 6.0
			                self.m = self.m_n / cos(self.beta)
			                self.c = self.clearence * self.m_n
			                self.midpoint = [0., 0]
			                self.d = self.z * self.m
			                self.dw = self.m * self.z
			                self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			                self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			                self.dg = self.d * cos(self.alpha_t)
			                self.phipart = 2 * pi / self.z
			                self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			                self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			                self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			                self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			                self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot = self.involute_rot1 + self.involute_rot2
			                self.involute_start = 0.
			                if self.dg <= self.df:
			                    self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg

			                pts = self.points(self.numpoints)
			                if not self.simple:
			                    wi = []
			                    for i in pts:
			                        out = BSplineCurve()
			                        out.interpolate(map(fcvec, i))
			                        wi.append(out)
			                    s = Wire(Shape(wi).Edges)
			                    wi = []
			                    for i in range(self.z):
			                        rot = App.Matrix()
			                        rot.rotateZ(-i * self.phipart)
			                        tooth_rot = s.transformGeometry(rot)
			                        if i != 0:
			                            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                            pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                            wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                        wi.append(tooth_rot)
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                    wi = Wire(wi)
			                    self.Shapea = wi
			                    if self.beta == 0:
			                        sh = Face(wi)
			                        self.Shapea = sh.extrude(App.Vector(0, 0, self.height))
			                        self.Shapea.translate(Vector(0,0,5.7))
			                    self.Shape = self.Shape.fuse(self.Shapea)


			                cy1 = Part.makeCylinder(16.8,5,Vector(0,0,1.5))
			                cy2 = Part.makeCylinder(7.8,5,Vector(0,0,1.5))
			                cy1 = cy1.cut(cy2)
			                self.Shape = self.Shape.cut(cy1)
			                cy3 = Part.makeCylinder(7.5,0.75,Vector(0,0,4.95))
			                self.Shape = self.Shape.fuse(cy3)
			                cy4 = Part.makeCylinder(3.85,13.5,Vector(0,0,-1))
			                self.Shape = self.Shape.fuse(cy4)
			                cy5 = Part.makeCylinder(4.5,13.5,Vector(0,0,9.5))
			                cy5 = cy5.cut(cy4)
			                self.Shape = self.Shape.cut(cy5)

			                plate1 = Part.makeCylinder(1.98, 54, Vector(0,0,-2))
			                box1 = Part.makeBox(1.92,5.24,54,Vector(-0.96,-2.62,-2))
			                plate1 = plate1.fuse(box1)
			                box2 = Part.makeBox(1.92,5.24,54,Vector(-0.96,-2.62,-2))
			                box2.rotate(Vector(0,0,0),Vector(0,0,1),90)
			                plate1 = plate1.fuse(box2)
			                self.Shape = self.Shape.cut(plate1)

			                cir1 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                self.Shape = self.Shape.cut(cir1)
			                cir2 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir2.rotate(Vector(0,0,0),Vector(0,0,1),45)
			                self.Shape = self.Shape.cut(cir2)
			                cir3 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir3.rotate(Vector(0,0,0),Vector(0,0,1),90)
			                self.Shape = self.Shape.cut(cir3)
			                cir4 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir4.rotate(Vector(0,0,0),Vector(0,0,1),135)
			                self.Shape = self.Shape.cut(cir4)
			                cir5 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir5.rotate(Vector(0,0,0),Vector(0,0,1),180)
			                self.Shape = self.Shape.cut(cir5)
			                cir6 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir6.rotate(Vector(0,0,0),Vector(0,0,1),225)
			                self.Shape = self.Shape.cut(cir6)
			                cir7 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir7.rotate(Vector(0,0,0),Vector(0,0,1),270)
			                self.Shape = self.Shape.cut(cir7)
			                cir8 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir8.rotate(Vector(0,0,0),Vector(0,0,1),315)
			                self.Shape = self.Shape.cut(cir8)

			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])


			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"십자홀 체인기어":

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=2.05, z=12, alpha=20 * pi / 180., clearence=0., shift=0., beta=0., undercut=False, simple=False, height=5.8, backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                d = 4.11
			                d1 = 17.2
			                d2 = 7.96
			                l = 5.43
			                self.cir = Part.makeCylinder(d1/2,4.8,Vector(0,0,1))
			                self.cir2 = Part.makeCylinder(d2/2,11.7,Vector(0,0,-1))
			                self.box = Part.makeBox(l/2,l,11.7,Vector(-l/4,-l/2,-1))
			                self.box1 = Part.makeBox(l,l/2,11.7,Vector(-l/2,-l/4,-1))
			                self.Shape = self.Shape.cut(self.cir)
			                self.Shape = self.Shape.fuse(self.cir2)
			                self.Shape = self.Shape.cut(self.box)
			                self.Shape = self.Shape.cut(self.box1)

			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])

			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()


	def onPopupDes15(self):
		if self.popup2.currentText() == u"체인":
			doc=App.newDocument()

			cy1 = Part.makeCylinder(2.5,1.25,Vector(-6.0,0,5.6-1.25),Vector(0,0,1),300)
			cy2 = Part.makeCylinder(0.75,1.25,Vector(-6.0,0,5.6-1.25),Vector(0,0,1),300)
			cy1 = cy1.cut(cy2)
			cy1.rotate(Vector(-6.0,0,5.6-1.25),Vector(0,0,-1),240)

			box1 = Part.makeBox(2.4,3.5,1.25,Vector(-3.0-1.2-0.7,-1.75,5.6-1.25))
			cy1 = cy1.fuse(box1)

			cy3 = Part.makeCylinder(2.5,1.25,Vector(0,0,5.6-2.5),Vector(0,0,1),360)
			cy4 = Part.makeCylinder(0.75,1.25,Vector(0,0,5.6-1.25),Vector(0,0,1),360)
			cy3 = cy3.fuse(cy4)

			box2 = Part.makeBox(2.4,3.5,1.25,Vector(-3.0-1.2+0.7,-1.75,5.6-2.5))
			cy3 = cy3.fuse(box2)

			cy1 = cy1.fuse(cy3)
			cy2 = cy1.mirror(Vector(0,0,0),Vector(0,0,1))
			cy1 = cy1.fuse(cy2)

			cy4 = Part.makeCylinder(1.44,8.1,Vector(0,0,-4.05),Vector(0,0,1))
			cy1 = cy1.fuse(cy4)

			#Part.show(cy1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=cy1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"링크체인":
			doc=App.newDocument()

			cy1 = Part.makeCylinder(2.5,1.25,Vector(-6.0,0,5.6-1.25),Vector(0,0,1),300)
			cy2 = Part.makeCylinder(0.75,1.25,Vector(-6.0,0,5.6-1.25),Vector(0,0,1),300)
			cy1 = cy1.cut(cy2)
			cy1.rotate(Vector(-6.0,0,5.6-1.25),Vector(0,0,-1),240)

			box1 = Part.makeBox(2.4,3.5,1.25,Vector(-3.0-1.2-0.7,-1.75,5.6-1.25))
			cy1 = cy1.fuse(box1)

			cy3 = Part.makeCylinder(2.5,1.25,Vector(0,0,5.6-2.5),Vector(0,0,1),360)
			cy4 = Part.makeCylinder(0.75,1.25,Vector(0,0,5.6-1.25),Vector(0,0,1),360)
			cy3 = cy3.fuse(cy4)

			box2 = Part.makeBox(2.4,3.5,1.25,Vector(-3.0-1.2+0.7,-1.75,5.6-2.5))
			cy3 = cy3.fuse(box2)

			cy1 = cy1.fuse(cy3)
			cy2 = cy1.mirror(Vector(0,0,0),Vector(0,0,1))
			cy1 = cy1.fuse(cy2)

			cy4 = Part.makeCylinder(3.3,5.9,Vector(0,-2.95,0),Vector(0,1,0))
			cy1 = cy1.fuse(cy4)

			cy5 = Part.makeCylinder(2.0,5.9,Vector(0,-2.95,0),Vector(0,1,0))
			cy1 = cy1.cut(cy5)

			#Part.show(cy1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=cy1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
	def onPopupDes16(self):
		if self.popup2.currentText() == u"풀리(대)":
			doc=App.newDocument()

			R1 = 37.75
			R2 = 2.0
			H_f1 = 3.3
			H_f2 = 1.0

			base1 = Part.makeCylinder(R1,H_f1*2,Vector(0,-H_f1,0),Vector(0,1,0),360)

			tri = Part.makePolygon([(R1-(H_f1-H_f2)*sqrt(3),0,0),(R1,-H_f1+H_f2,0),(R1,H_f1-H_f2,0),(R1-(H_f1-H_f2)*sqrt(3),0,0)])
			face = Part.Face(tri)
			angle = 360
			solid = face.revolve(Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.cut(solid)

			base3 = Part.makeCylinder(33.0,H_f2,Vector(0,H_f1-H_f2,0),Vector(0,1,0),360)
			base1 = base1.cut(base3)
			base5 = Part.makeCylinder(33.0,H_f2,Vector(0,-H_f1+H_f2,0),Vector(0,-1,0),360)
			base1 = base1.cut(base5)

			base7 = Part.makeCylinder(4.75,10.9+3,Vector(0,-3,0),Vector(0,1,0),360)
			base1 = base1.fuse(base7)

			base2 = Part.makeCylinder(R2,50,Vector(0,-25,0),Vector(0,1,0),360)
			base1 = base1.cut(base2)
			outC=Part.makeCylinder(3.29/2,50,Vector(-25.0,8.0,0),Vector(1,0,0))
			base1=base1.cut(outC)

			cir1 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			base1 = base1.cut(cir1)
			cir2 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir2.rotate(Vector(0,0,0),Vector(0,1,0),45)
			base1 = base1.cut(cir2)
			cir3 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir3.rotate(Vector(0,0,0),Vector(0,1,0),90)
			base1 = base1.cut(cir3)
			cir4 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir4.rotate(Vector(0,0,0),Vector(0,1,0),135)
			base1 = base1.cut(cir4)
			cir5 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir5.rotate(Vector(0,0,0),Vector(0,1,0),180)
			base1 = base1.cut(cir5)
			cir6 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir6.rotate(Vector(0,0,0),Vector(0,1,0),225)
			base1 = base1.cut(cir6)
			cir7 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir7.rotate(Vector(0,0,0),Vector(0,1,0),270)
			base1 = base1.cut(cir7)
			cir8 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir8.rotate(Vector(0,0,0),Vector(0,1,0),315)
			base1 = base1.cut(cir8)

			acir1 = Part.makeCylinder(2.1,50,Vector(24.0,-25.0,0),Vector(0,1,0))
			base1 = base1.cut(acir1)
			acir2 = Part.makeCylinder(2.1,50,Vector(24.0,-25.0,0),Vector(0,1,0))
			acir2.rotate(Vector(0,0,0),Vector(0,1,0),45)
			base1 = base1.cut(acir2)
			acir3 = Part.makeCylinder(2.1,50,Vector(24.0,-25.0,0),Vector(0,1,0))
			acir3.rotate(Vector(0,0,0),Vector(0,1,0),90)
			base1 = base1.cut(acir3)
			acir4 = Part.makeCylinder(2.1,50,Vector(24.0,-25.0,0),Vector(0,1,0))
			acir4.rotate(Vector(0,0,0),Vector(0,1,0),135)
			base1 = base1.cut(acir4)
			acir5 = Part.makeCylinder(2.1,50,Vector(24.0,-25.0,0),Vector(0,1,0))
			acir5.rotate(Vector(0,0,0),Vector(0,1,0),180)
			base1 = base1.cut(acir5)
			acir6 = Part.makeCylinder(2.1,50,Vector(24.0,-25.0,0),Vector(0,1,0))
			acir6.rotate(Vector(0,0,0),Vector(0,1,0),225)
			base1 = base1.cut(acir6)
			acir7 = Part.makeCylinder(2.1,50,Vector(24.0,-25.0,0),Vector(0,1,0))
			acir7.rotate(Vector(0,0,0),Vector(0,1,0),270)
			base1 = base1.cut(acir7)
			acir8 = Part.makeCylinder(2.1,50,Vector(24.0,-25.0,0),Vector(0,1,0))
			acir8.rotate(Vector(0,0,0),Vector(0,1,0),315)
			base1 = base1.cut(acir8)

			box1 = Part.makeBox(4.2,12,50,Vector(12.0,-25.0,-2.1),Vector(0,1,0))
			base1 = base1.cut(box1)
			box2 = Part.makeBox(4.2,12,50,Vector(12.0,-25.0,-2.1),Vector(0,1,0))
			box2.rotate(Vector(0,0,0),Vector(0,1,0),90)
			base1 = base1.cut(box2)
			box3 = Part.makeBox(4.2,12,50,Vector(12.0,-25.0,-2.1),Vector(0,1,0))
			box3.rotate(Vector(0,0,0),Vector(0,1,0),180)
			base1 = base1.cut(box3)
			box4 = Part.makeBox(4.2,12,50,Vector(12.0,-25.0,-2.1),Vector(0,1,0))
			box4.rotate(Vector(0,0,0),Vector(0,1,0),270)
			base1 = base1.cut(box4)

			#Part.show(base1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=base1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"풀리(중)":
			doc=App.newDocument()

			R1 = 18.9
			R2 = 2.0
			H_f1 = 3.0
			H_f2 = 1.25

			base1 = Part.makeCylinder(R1,H_f1*2,Vector(0,-H_f1,0),Vector(0,1,0),360)

			tri = Part.makePolygon([(R1-(H_f1-H_f2)*sqrt(3),0,0),(R1,-H_f1+H_f2,0),(R1,H_f1-H_f2,0),(R1-(H_f1-H_f2)*sqrt(3),0,0)])
			face = Part.Face(tri)
			angle = 360
			solid = face.revolve(Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.cut(solid)

			base7 = Part.makeCylinder(4.75,10.9,Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.fuse(base7)

			base2 = Part.makeCylinder(R2,50,Vector(0,-25,0),Vector(0,1,0),360)
			base1 = base1.cut(base2)

			outC=Part.makeCylinder(3.29/2,50,Vector(-25.0,8.0,0),Vector(1,0,0))
			base1=base1.cut(outC)

			cir1 = Part.makeCylinder(3.0,50,Vector(12,-2.0,0),Vector(0,1,0))
			base1 = base1.cut(cir1)
			cir2 = Part.makeCylinder(3.0,50,Vector(12,-2.0,0),Vector(0,1,0))
			cir2.rotate(Vector(0,0,0),Vector(0,1,0),45)
			base1 = base1.cut(cir2)
			cir3 = Part.makeCylinder(3.0,50,Vector(12,-2.0,0),Vector(0,1,0))
			cir3.rotate(Vector(0,0,0),Vector(0,1,0),90)
			base1 = base1.cut(cir3)
			cir4 = Part.makeCylinder(3.0,50,Vector(12,-2.0,0),Vector(0,1,0))
			cir4.rotate(Vector(0,0,0),Vector(0,1,0),135)
			base1 = base1.cut(cir4)
			cir5 = Part.makeCylinder(3.0,50,Vector(12,-2.0,0),Vector(0,1,0))
			cir5.rotate(Vector(0,0,0),Vector(0,1,0),180)
			base1 = base1.cut(cir5)
			cir6 = Part.makeCylinder(3.0,50,Vector(12,-2.0,0),Vector(0,1,0))
			cir6.rotate(Vector(0,0,0),Vector(0,1,0),225)
			base1 = base1.cut(cir6)
			cir7 = Part.makeCylinder(3.0,50,Vector(12,-2.0,0),Vector(0,1,0))
			cir7.rotate(Vector(0,0,0),Vector(0,1,0),270)
			base1 = base1.cut(cir7)
			cir8 = Part.makeCylinder(3.0,50,Vector(12,-2.0,0),Vector(0,1,0))
			cir8.rotate(Vector(0,0,0),Vector(0,1,0),315)
			base1 = base1.cut(cir8)

			acir1 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			base1 = base1.cut(acir1)
			acir2 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir2.rotate(Vector(0,0,0),Vector(0,1,0),45)
			base1 = base1.cut(acir2)
			acir3 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir3.rotate(Vector(0,0,0),Vector(0,1,0),90)
			base1 = base1.cut(acir3)
			acir4 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir4.rotate(Vector(0,0,0),Vector(0,1,0),135)
			base1 = base1.cut(acir4)
			acir5 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir5.rotate(Vector(0,0,0),Vector(0,1,0),180)
			base1 = base1.cut(acir5)
			acir6 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir6.rotate(Vector(0,0,0),Vector(0,1,0),225)
			base1 = base1.cut(acir6)
			acir7 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir7.rotate(Vector(0,0,0),Vector(0,1,0),270)
			base1 = base1.cut(acir7)
			acir8 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir8.rotate(Vector(0,0,0),Vector(0,1,0),315)
			base1 = base1.cut(acir8)

			#Part.show(base1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=base1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"풀리(소)":
			doc=App.newDocument()

			R1 = 12.7
			R2 = 2.0
			H_f1 = 2.2
			H_f2 = 0.8

			base1 = Part.makeCylinder(R1,H_f1*2,Vector(0,-H_f1,0),Vector(0,1,0),360)

			tri = Part.makePolygon([(R1-(H_f1-H_f2)*sqrt(3),0,0),(R1,-H_f1+H_f2,0),(R1,H_f1-H_f2,0),(R1-(H_f1-H_f2)*sqrt(3),0,0)])
			face = Part.Face(tri)
			angle = 360
			solid = face.revolve(Vector(0,0,0),Vector(0,1,0),360)

			base1 = base1.cut(solid)

			base3 = Part.makeCylinder(10.0,H_f2,Vector(0,H_f1-H_f2,0),Vector(0,1,0),360)
			base4 = Part.makeCylinder(5.9,H_f2,Vector(0,H_f1-H_f2,0),Vector(0,1,0),360)
			base3 = base3.cut(base4)
			base1 = base1.cut(base3)

			base5 = Part.makeCylinder(10.0,H_f2,Vector(0,-H_f1+H_f2,0),Vector(0,-1,0),360)
			base6 = Part.makeCylinder(5.9,H_f2,Vector(0,-H_f1+H_f2,0),Vector(0,-1,0),360)
			base5 = base5.cut(base6)
			base1 = base1.cut(base5)

			base7 = Part.makeCylinder(4.75,10.9,Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.fuse(base7)
			base8 = Part.makeCylinder(5.9,3.1,Vector(0,0,0),Vector(0,-1,0),360)
			base1 = base1.fuse(base8)

			base2 = Part.makeCylinder(R2,50,Vector(0,-25,0),Vector(0,1,0),360)
			base1 = base1.cut(base2)

			outC=Part.makeCylinder(3.29/2,50,Vector(-25.0,7.5,0),Vector(1,0,0))
			base1=base1.cut(outC)

			#Part.show(base1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=base1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"타이어풀리":
			doc=App.newDocument()

			R1 = 7.7
			R2 = 2.1
			H_f1 = 2.45
			H_f2 = 0.8

			base1 = Part.makeCylinder(R1,H_f1*2,Vector(0,-H_f1,0),Vector(0,1,0),360)
			base2 = Part.makeCylinder(R2,H_f1*2,Vector(0,-H_f1,0),Vector(0,1,0),360)

			base1 = base1.cut(base2)

			tri = Part.makePolygon([(R1-(H_f1-H_f2)*sqrt(3),0,0),(R1,-H_f1+H_f2,0),(R1,H_f1-H_f2,0),(R1-(H_f1-H_f2)*sqrt(3),0,0)])
			face = Part.Face(tri)
			angle = 360
			solid = face.revolve(Vector(0,0,0),Vector(0,1,0),360)

			base1 = base1.cut(solid)

			base3 = Part.makeCylinder(6.3,H_f2,Vector(0,H_f1-H_f2,0),Vector(0,1,0),360)
			base4 = Part.makeCylinder(4,H_f2,Vector(0,H_f1-H_f2,0),Vector(0,1,0),360)
			base3 = base3.cut(base4)
			base1 = base1.cut(base3)

			base5 = Part.makeCylinder(6.3,H_f2,Vector(0,-H_f1+H_f2,0),Vector(0,-1,0),360)
			base6 = Part.makeCylinder(4,H_f2,Vector(0,-H_f1+H_f2,0),Vector(0,-1,0),360)
			base5 = base5.cut(base6)
			base1 = base1.cut(base5)

			#Part.show(base1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=base1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"2단 풀리":
			doc=App.newDocument()

			R1 = 28.4
			R3 = 2.0
			H_f1 = 3.0
			H_f2 = 1.0

			base1 = Part.makeCylinder(R1,H_f1*2,Vector(0,-H_f1,0),Vector(0,1,0),360)

			tri = Part.makePolygon([(R1-(H_f1-H_f2)*sqrt(3),0,0),(R1,-H_f1+H_f2,0),(R1,H_f1-H_f2,0),(R1-(H_f1-H_f2)*sqrt(3),0,0)])
			face = Part.Face(tri)
			angle = 360
			solid = face.revolve(Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.cut(solid)

			cir1 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			base1 = base1.cut(cir1)
			cir2 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir2.rotate(Vector(0,0,0),Vector(0,1,0),45)
			base1 = base1.cut(cir2)
			cir3 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir3.rotate(Vector(0,0,0),Vector(0,1,0),90)
			base1 = base1.cut(cir3)
			cir4 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir4.rotate(Vector(0,0,0),Vector(0,1,0),135)
			base1 = base1.cut(cir4)
			cir5 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir5.rotate(Vector(0,0,0),Vector(0,1,0),180)
			base1 = base1.cut(cir5)
			cir6 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir6.rotate(Vector(0,0,0),Vector(0,1,0),225)
			base1 = base1.cut(cir6)
			cir7 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir7.rotate(Vector(0,0,0),Vector(0,1,0),270)
			base1 = base1.cut(cir7)
			cir8 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir8.rotate(Vector(0,0,0),Vector(0,1,0),315)
			base1 = base1.cut(cir8)

			acir1 = Part.makeCylinder(2.1,50,Vector(18.0,-25.0,0),Vector(0,1,0))
			base1 = base1.cut(acir1)
			acir3 = Part.makeCylinder(2.1,50,Vector(18.0,-25.0,0),Vector(0,1,0))
			acir3.rotate(Vector(0,0,0),Vector(0,1,0),90)
			base1 = base1.cut(acir3)
			acir5 = Part.makeCylinder(2.1,50,Vector(18.0,-25.0,0),Vector(0,1,0))
			acir5.rotate(Vector(0,0,0),Vector(0,1,0),180)
			base1 = base1.cut(acir5)
			acir7 = Part.makeCylinder(2.1,50,Vector(18.0,-25.0,0),Vector(0,1,0))
			acir7.rotate(Vector(0,0,0),Vector(0,1,0),270)
			base1 = base1.cut(acir7)

			box1 = Part.makeBox(4.2,6.0,50,Vector(12.0,-25.0,-2.1),Vector(0,1,0))
			base1 = base1.cut(box1)
			box2 = Part.makeBox(4.2,6.0,50,Vector(12.0,-25.0,-2.1),Vector(0,1,0))
			box2.rotate(Vector(0,0,0),Vector(0,1,0),90)
			base1 = base1.cut(box2)
			box3 = Part.makeBox(4.2,6.0,50,Vector(12.0,-25.0,-2.1),Vector(0,1,0))
			box3.rotate(Vector(0,0,0),Vector(0,1,0),180)
			base1 = base1.cut(box3)
			box4 = Part.makeBox(4.2,6.0,50,Vector(12.0,-25.0,-2.1),Vector(0,1,0))
			box4.rotate(Vector(0,0,0),Vector(0,1,0),270)
			base1 = base1.cut(box4)

			base3 = Part.makeCylinder(4.75,19.4,Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.fuse(base3)
			outC=Part.makeCylinder(3.29/2,50,Vector(-25.0,15.0,0),Vector(1,0,0))
			base1=base1.cut(outC)

			R2 = 7.8
			base2 = Part.makeCylinder(R2,H_f1*2,Vector(0,4.7,0),Vector(0,1,0),360)

			tri = Part.makePolygon([(R2-(H_f1-H_f2)*sqrt(3),7.7,0),(R2,7.7-H_f1+H_f2,0),(R2,7.7+H_f1-H_f2,0),(R2-(H_f1-H_f2)*sqrt(3),7.7,0)])
			face = Part.Face(tri)
			angle = 360
			solid = face.revolve(Vector(0,0,0),Vector(0,1,0),360)
			base2 = base2.cut(solid)

			base1 = base1.fuse(base2)

			base2 = Part.makeCylinder(R3,50,Vector(0,-25,0),Vector(0,1,0),360)
			base1 = base1.cut(base2)

			#Part.show(base1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=base1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"피니언풀리":

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=0.72, z=19, alpha=20 * pi / 180., clearence=0, shift=0., beta=0., undercut=False, simple=False, height=7., backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                cy1 = Part.makeCylinder(4.75,7.5,Vector(0,0,7),Vector(0,0,1),360)
			                self.Shape = self.Shape.fuse(cy1)
			                outC=Part.makeCylinder(3.29/2,50,Vector(-25.0,0,11.0),Vector(1,0,0))
			                self.Shape=self.Shape.cut(outC)

			                cy2 = Part.makeCylinder(19.0,5.6,Vector(0,0,0),Vector(0,0,-1),360)
			                self.Shape = self.Shape.fuse(cy2)
			                H_f1 = 5.6
			                H_f2 = 1.0
			                tri = Part.makePolygon([(19.0-(1.8)*sqrt(3),0,-2.8),(19.0,0,-H_f2),(19.0,0,-H_f1+H_f2),(19.0-(1.8)*sqrt(3),0,-2.8)])
			                face = Part.Face(tri)
			                solid = face.revolve(Vector(0,0,-2.8),Vector(0,0,1),360)
			                self.Shape = self.Shape.cut(solid)

			                cir1 = Part.makeCylinder(3.0,50,Vector(12,0,-4.6),Vector(0,0,1))
			                self.Shape = self.Shape.cut(cir1)
			                cir2 = Part.makeCylinder(3.0,50,Vector(12,0,-4.6),Vector(0,0,1))
			                cir2.rotate(Vector(0,0,0),Vector(0,0,1),45)
			                self.Shape = self.Shape.cut(cir2)
			                cir3 = Part.makeCylinder(3.0,50,Vector(12,0,-4.6),Vector(0,0,1))
			                cir3.rotate(Vector(0,0,0),Vector(0,0,1),90)
			                self.Shape = self.Shape.cut(cir3)
			                cir4 = Part.makeCylinder(3.0,50,Vector(12,0,-4.6),Vector(0,0,1))
			                cir4.rotate(Vector(0,0,0),Vector(0,0,1),135)
			                self.Shape = self.Shape.cut(cir4)
			                cir5 = Part.makeCylinder(3.0,50,Vector(12,0,-4.6),Vector(0,0,1))
			                cir5.rotate(Vector(0,0,0),Vector(0,0,1),180)
			                self.Shape = self.Shape.cut(cir5)
			                cir6 = Part.makeCylinder(3.0,50,Vector(12,0,-4.6),Vector(0,0,1))
			                cir6.rotate(Vector(0,0,0),Vector(0,0,1),225)
			                self.Shape = self.Shape.cut(cir6)
			                cir7 = Part.makeCylinder(3.0,50,Vector(12,0,-4.6),Vector(0,0,1))
			                cir7.rotate(Vector(0,0,0),Vector(0,0,1),270)
			                self.Shape = self.Shape.cut(cir7)
			                cir8 = Part.makeCylinder(3.0,50,Vector(12,0,-4.6),Vector(0,0,1))
			                cir8.rotate(Vector(0,0,0),Vector(0,0,1),315)
			                self.Shape = self.Shape.cut(cir8)

			                acir1 = Part.makeCylinder(2.1,50,Vector(12,0,-5.6),Vector(0,0,1))
			                self.Shape = self.Shape.cut(acir1)
			                acir2 = Part.makeCylinder(2.1,50,Vector(12,0,-5.6),Vector(0,0,1))
			                acir2.rotate(Vector(0,0,0),Vector(0,0,1),45)
			                self.Shape = self.Shape.cut(acir2)
			                acir3 = Part.makeCylinder(2.1,50,Vector(12,0,-5.6),Vector(0,0,1))
			                acir3.rotate(Vector(0,0,0),Vector(0,0,1),90)
			                self.Shape = self.Shape.cut(acir3)
			                acir4 = Part.makeCylinder(2.1,50,Vector(12,0,-5.6),Vector(0,0,1))
			                acir4.rotate(Vector(0,0,0),Vector(0,0,1),135)
			                self.Shape = self.Shape.cut(acir4)
			                acir5 = Part.makeCylinder(2.1,50,Vector(12,0,-5.6),Vector(0,0,1))
			                acir5.rotate(Vector(0,0,0),Vector(0,0,1),180)
			                self.Shape = self.Shape.cut(acir5)
			                acir6 = Part.makeCylinder(2.1,50,Vector(12,0,-5.6),Vector(0,0,1))
			                acir6.rotate(Vector(0,0,0),Vector(0,0,1),225)
			                self.Shape = self.Shape.cut(acir6)
			                acir7 = Part.makeCylinder(2.1,50,Vector(12,0,-5.6),Vector(0,0,1))
			                acir7.rotate(Vector(0,0,0),Vector(0,0,1),270)
			                self.Shape = self.Shape.cut(acir7)
			                acir8 = Part.makeCylinder(2.1,50,Vector(12,0,-5.6),Vector(0,0,1))
			                acir8.rotate(Vector(0,0,0),Vector(0,0,1),315)
			                self.Shape = self.Shape.cut(acir8)

			                cir1 = Part.makeCylinder(2.0,50,Vector(0,0,-25),Vector(0,0,1),360)
			                self.Shape = self.Shape.cut(cir1)
			                #Part.show(self.Shape) #보여주기
			                #Part.show(tri) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(1.0, 0.0, 0.0)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])


			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()
			Gui.SendMsgToActiveView("ViewFit")

	def onPopupDes17(self):
		if self.popup2.currentText() == u"래크":

			doc=App.newDocument()

			class involute_gear_rack():
				def __init__(self, numpoints=10, m=0.65, z=67, alpha=20 * pi / 180., thickness=11, height=6.5 ):
					self.alpha = alpha
					self.thickness = thickness
					self.m = m
					self.z = z
					self.teeth = z
					self.height = height
					self.numpoints = numpoints
					self.execute()
				def execute(self):
					pts = self.points(self.numpoints)
					wire = Part.Wire(makePolygon(map(fcvec, pts)))
					face = Part.Face(wire)
					self.Shape = face.extrude(fcvec([0., 0., self.height]))
					#여기서부터 수정
					box = Part.makeBox(4.0,self.thickness*self.z,0.9,Vector(-self.m+6.8-2,-self.thickness,0))
					box2 = Part.makeBox(4.0,self.thickness*self.z,0.9,Vector(-self.m+6.8-2,-self.thickness,self.height-0.9))
					self.Shape = self.Shape.cut(box)
					self.Shape = self.Shape.cut(box2)
					cir = []
					n = 6
					for i in range(n):
						cir.append(Part.makeCylinder(4.0/2, self.height, Vector(-self.m+6.8,5.5-self.m+25.42*i,0)))
					for i in cir:
						self.Shape = self.Shape.cut(i)
					box3 = []
					for i in range(n-1):
						box3.append(Part.makeBox(4.0, 4.3, self.height, Vector(-self.m+6.8-2,16-2*self.m*tan(self.alpha)-((self.m * pi)/2-2*self.m*tan(self.alpha))/2+25.42*i,0)))
					for i in box3:
						self.Shape = self.Shape.cut(i)
					cir2 = []
					for i in range(n-1):
						cir2.append(Part.makeCylinder(4.3/2, self.height, Vector(-self.m+6.8-1.8,16-2*self.m*tan(self.alpha)-((self.m * pi)/2-2*self.m*tan(self.alpha))/2+4.3/2+25.42*i,0)))
					for i in cir2:
						self.Shape = self.Shape.cut(i)
					cir3 = []
					for i in range(n-1):
						cir3.append(Part.makeCylinder(4.3/2, self.height, Vector(-self.m+6.8+1.8,16-2*self.m*tan(self.alpha)-((self.m * pi)/2-2*self.m*tan(self.alpha))/2+4.3/2+25.42*i,0)))
					for i in cir3:
						self.Shape = self.Shape.cut(i)

					#Part.show(self.Shape)
					shape=doc.addObject("Part::Feature")
					shape.Shape=self.Shape
					doc.recompute()
					shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
					Gui.activeDocument().activeView().viewAxometric()
					Gui.SendMsgToActiveView("ViewFit")
				def points(self, num):
					a = 2 * self.m * tan(self.alpha)
					b = ((self.m * pi) / 2 - a) / 2
					tooth = [[self.m, -a - b],[-self.m, -b],[-self.m, b],[self.m, a + b]]
					tooth2 = [[self.m+self.thickness, a + b],[3*self.m+self.thickness, b],[3*self.m+self.thickness, -b],[self.m+self.thickness, -a - b]]
					teeth = [tooth]
					teeth2 = [tooth2]
					trans = translation([0., self.m * pi, 0.])
					for i in range(self.z):
						teeth.append(trans(teeth[-1]))
					#	teeth3.append(trans(teeth[-1]))
					#for i in range(self.z):
					#	teeth2.append(trans(teeth2[-1]))
					#teeth2=teeth2.reverse()
					#for i in range(self.z):
					#	teeth3.append(trans(teeth2[0]))
					teeth = list(np.vstack(teeth))#array로 변환
					for i in range(self.z):
						teeth2.append(trans(teeth2[-1]))
					teeth2 = teeth2[::-1]
					teeth2 = list(np.vstack(teeth2))
					teeth.append(teeth2)#array로 변환
					#teeth.append(list(teeth[-1])) #teeth list의 마지막 array인 [1.0, 48.....]을 list 항목의 마지막에 다시 추가
					#teeth[-1][0] += self.thickness #새로추가된 list의 마지막 항목의 x에 두께를 더함
					#teeth.append(list(teeth[-1]))
					teeth = list(np.vstack(teeth))
					teeth.append(list(teeth[0])) #teeth list의 마지막에 list로 첫번째 array인 항을 list 항목으로 추가
					#teeth[-1][0] += self.thickness
					#print(teeth)
					return(teeth)

			def fcvec(x):
				if len(x) == 2:
					return(App.Vector(x[0], x[1], 0))
				else:
					return(App.Vector(x[0], x[1], x[2]))

			def translation(vec):
				def trans(x):
					return([x[0] + vec[0], x[1] + vec[1]])
				def func(x):
					return(array(map(trans, x)))
				return(func)

			ex = involute_gear_rack()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"래크홀더":
			doc=App.newDocument()

			t=1.95
			h=11.85
			l=139.50
			w= 29.70
			f=6.43
			D=11.10
			d1=5.45
			d2=4.05
			l1=15.10
			l2=45.70
			w1=26.70
			w2=10.20
			wt1=9.40
			wt2=10.60
			wt3=11.80
			h1=1.43
			h2=3.90
			l3=1
			t1=1.34
			i=0
			n=11
			cir4=[]

			plate1 = Part.makeBox(l,w,t,Vector(0,0,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(f, [plate1.Edges[2],plate1.Edges[6]])
			plate2 = Part.makeBox(l,w,t,Vector(0,0,h-t),Vector(0,0,1))
			plate2 = plate2.makeFillet(f, [plate2.Edges[2],plate2.Edges[6]])
			cir1 = Part.makeCylinder(D/2,h,Vector(D/2,w-w1-D/2,0),Vector(0,0,1))
			cir2 = Part.makeCylinder(D/2,h,Vector(l/2,w-w1-D/2,0),Vector(0,0,1))
			cir3 = Part.makeCylinder(D/2,h,Vector(l-D/2,w-w1-D/2,0),Vector(0,0,1))
			plate1 = plate1.fuse(cir1)
			plate1 = plate1.fuse(cir2)
			plate1 = plate1.fuse(cir3)
			plate1 = plate1.fuse(plate2)
			box1= Part.makeBox(D,D/2,h,Vector(0,w-w1-D/2,0),Vector(0,0,1))
			box2= Part.makeBox(D,D/2,h,Vector(l/2-D/2,w-w1-D/2,0),Vector(0,0,1))
			box3= Part.makeBox(D,D/2,h,Vector(l-D,w-w1-D/2,0),Vector(0,0,1))
			plate1 = plate1.fuse(box1)
			plate1 = plate1.fuse(box2)
			plate1 = plate1.fuse(box3)
			box4= Part.makeBox(l1,w-w1,h-2*t,Vector(0,0,t),Vector(0,0,1))
			box5= Part.makeBox(l2,w-w1,h-2*t,Vector((l-l2)/2,0,t),Vector(0,0,1))
			box6= Part.makeBox(l1,w-w1,h-2*t,Vector(l-l1,0,t),Vector(0,0,1))
			plate1 = plate1.fuse(box4)
			plate1 = plate1.fuse(box5)
			plate1 = plate1.fuse(box6)

			for i in range(n):
					cir4.append(Part.makeCylinder(d2/2,h,Vector(6.525+12.7*i,w-(4.15+d2/2),0)))

			for i in cir4:
			        plate1 = plate1.cut(i)

			cir5 = Part.makeCylinder(d1/2,h,Vector(6.525+12.7,w-(4.15+d2/2),0))
			cir6 = Part.makeCylinder(d1/2,h,Vector(6.525+12.7*7,w-(4.15+d2/2),0))
			cir7 = Part.makeCylinder(d1/2,h,Vector(6.525+12.7*8,w-(4.15+d2/2),0))
			cir8 = Part.makeCylinder(d1/2,h,Vector(6.525+12.7*10,w-(4.15+d2/2),0))
			plate1 = plate1.cut(cir5)
			plate1 = plate1.cut(cir6)
			plate1 = plate1.cut(cir7)
			plate1 = plate1.cut(cir8)

			tri = Part.makePolygon([(0,11.80,0),(0,10.60,1.43),(0,9.40,0),(0,11.80,0)])
			fa = Part.Face(tri)
			p = fa.extrude(Vector(l,0,0))
			plate1 = plate1.cut(p)

			tri1 = Part.makePolygon([(0,11.80,h),(0,10.60,h-1.43),(0,9.40,h),(0,11.80,h)])
			fa1 = Part.Face(tri1)
			p1 = fa1.extrude(Vector(l,0,0))
			plate1 = plate1.cut(p1)

			extend1 = Part.makePolygon([(0,10.60+0.5+t1,t),(0,10.60+t1+0.5,3.9),(0,10.60+0.5,3.9),(0,10.6+0.5,3.9-h1),(0,10.6-0.5,3.9-h1),(0,10.6-0.5,3.9),(0,10.6-0.5-t1,3.9),(0,10.60-t1-0.5,t),(0,10.60+0.5+t1,t)])
			fa2 = Part.Face(extend1)
			p2 = fa2.extrude(Vector(l,0,0))
			plate1 = plate1.fuse(p2)

			extend2 = Part.makePolygon([(0,10.60+0.5+t1,h-t),(0,10.60+t1+0.5,h-3.9),(0,10.60+0.5,h-3.9),(0,10.6+0.5,h-3.9+h1),(0,10.6-0.5,h-3.9+h1),(0,10.6-0.5,h-3.9),(0,10.6-0.5-t1,h-3.9),(0,10.60-t1-0.5,h-t),(0,10.60+0.5+t1,h-t)])
			fa3 = Part.Face(extend2)
			p3 = fa3.extrude(Vector(l,0,0))
			plate1 = plate1.fuse(p3)

			#Part.show(plate1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
	def onPopupDes18(self):
		if self.popup2.currentText() == u"십자홀 피니언":

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=0.637, z=19, alpha=20 * pi / 180., clearence=0, shift=0., beta=0., undercut=False, simple=False, height=5.88, backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정

			                x =5.47
			                y = 2
			                h = 7
			                h1 = 5.88
			                D = 8.77
			                D1 = 6.68
			                self.box = Part.makeBox(x,y,h,Vector(-x/2,-y/2,-(h-h1)/2))
			                self.box1 = Part.makeBox(y,x,h,Vector(-y/2,-x/2,-(h-h1)/2))
			                self.cir1 = Part.makeCylinder(D/2,(h-h1)/2,Vector(0,0,h1))
			                self.cir2 = Part.makeCylinder(D1/2,(h-h1)/2,Vector(0,0,h1))
			                self.cir3 = Part.makeCylinder(D/2,(h-h1)/2,Vector(0,0,-(h-h1)/2))
			                self.cir5 = Part.makeCylinder(D1/2,(h-h1)/2,Vector(0,0,-(h-h1)/2))

			                self.Shape = self.Shape.fuse(self.cir1)
			                self.Shape = self.Shape.fuse(self.cir3)
			                self.Shape = self.Shape.cut(self.box)
			                self.Shape = self.Shape.cut(self.box1)
			                self.Shape = self.Shape.cut(self.cir2)
			                self.Shape = self.Shape.cut(self.cir2)
			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])


			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()
			Gui.SendMsgToActiveView("ViewFit")

	def onPopupDes19(self):
		if self.popup2.currentText() == u"타이어(소)":
			doc=App.newDocument()

			d = 27
			t = 7.7
			d1 = 18.48
			d2 = 15.47
			d3 = 13.24
			h1 = 1.43
			h2 = 4.38
			n = 2
			i = 0

			circle = Part.makeCylinder(d/2,t,Vector(0,0,0))
			circle = circle.makeFillet((t-h1)/2,[circle.Edges[0],circle.Edges[2]])

			cir = []
			cir1 = []
			for i in range(n):
				cir.append(Part.makeCylinder(d1/2,(t-h2)/2,Vector(0,0,(t-(t-h2)/2)*i)))
				cir1.append(Part.makeCylinder(d2/2,(t-h1)/2,Vector(0,0,(t-(t-h1)/2)*i)))
			for i in cir:
				circle = circle.cut(i)
			for i in cir1:
				circle = circle.cut(i)

			circle1 = Part.makeCylinder(d3/2,h1,Vector(0,0,(t-h1)/2))
			circle = circle.cut(circle1)

			#Part.show(circle)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

		if self.popup2.currentText() == u"타이어(중)":
			doc=App.newDocument()

			d = 37
			t = 8.5
			d1 = 24.46
			d2 = 22.41
			h1 = 1.8
			n = 2
			i = 0

			circle = Part.makeCylinder(d/2,t,Vector(0,0,0))
			circle = circle.makeFillet((t-h1)/2,[circle.Edges[0],circle.Edges[2]])

			cir = []
			for i in range(n):
				cir.append(Part.makeCylinder(d1/2,(t-h1)/2,Vector(0,0,(t-(t-h1)/2)*i)))
			for i in cir:
				circle = circle.cut(i)

			circle1 = Part.makeCylinder(d2/2,h1,Vector(0,0,(t-h1)/2))
			circle = circle.cut(circle1)

			#Part.show(circle)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		if self.popup2.currentText() == u"타이어(대)":
			doc=App.newDocument()

			d = 50
			t = 10
			d1 = 36.92
			d2 = 34.96
			h1 = 2.29
			n = 2
			i = 0

			circle = Part.makeCylinder(d/2,t,Vector(0,0,0))
			circle = circle.makeFillet((t-h1)/2,[circle.Edges[0],circle.Edges[2]])

			cir = []
			for i in range(n):
				cir.append(Part.makeCylinder(d1/2,(t-h1)/2,Vector(0,0,(t-(t-h1)/2)*i)))
			for i in cir:
				circle = circle.cut(i)

			circle1 = Part.makeCylinder(d2/2,h1,Vector(0,0,(t-h1)/2))
			circle = circle.cut(circle1)

			#Part.show(circle)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		if self.popup2.currentText() == u"타이어(특대)":
			doc=App.newDocument()

			d = 70
			t = 10
			d1 = 57.31
			d2 = 55.24
			h1 = 2.81
			n = 2
			i = 0

			circle = Part.makeCylinder(d/2,t,Vector(0,0,0))
			circle = circle.makeFillet((t-h1)/2,[circle.Edges[0],circle.Edges[2]])

			cir = []
			for i in range(n):
				cir.append(Part.makeCylinder(d1/2,(t-h1)/2,Vector(0,0,(t-(t-h1)/2)*i)))
			for i in cir:
				circle = circle.cut(i)

			circle1 = Part.makeCylinder(d2/2,h1,Vector(0,0,(t-h1)/2))
			circle = circle.cut(circle1)

			#Part.show(circle)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
	def onPopupDes20(self):
		if self.popup2.currentText() == u"나사봉 - 5cm":
			doc=App.newDocument()

			# 기본형상
			cir_hex=4 #circle_diameter

			d=50
			exHex=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))

			# 나사선 helix
			helix = Part.makeHelix(0.797,50,2) #50넣으면 메모리 문제로 실행 안될 수 있음.            #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((1.7,0,-0.125), (1.7,0,0.125))
			edge2 = Part.makeLine((1.7,0,0.125), (2.3,0,0.419))
			edge3 = Part.makeLine((2.3,0,0.419), (2.3,0,-0.419))
			edge4 = Part.makeLine((2.3,0,-0.419), (1.7,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)

		elif self.popup2.currentText() == u"나사봉 - 7.5cm":
			doc=App.newDocument()

			# 기본형상
			cir_hex=4 #circle_diameter

			d=75 #d 조절
			exHex=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))

			# 나사선 helix
			helix = Part.makeHelix(0.797,75,2) #75넣으면 메모리 문제로 실행 안될 수 있음. height 조절하기 #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((1.7,0,-0.125), (1.7,0,0.125))
			edge2 = Part.makeLine((1.7,0,0.125), (2.3,0,0.419))
			edge3 = Part.makeLine((2.3,0,0.419), (2.3,0,-0.419))
			edge4 = Part.makeLine((2.3,0,-0.419), (1.7,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)
		elif self.popup2.currentText() == u"원기둥 - 5cm":
			doc=App.newDocument()

			# 기본형상
			cir_hex=4 #circle_diameter

			d=50 #d 조절
			exHex=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)
		elif self.popup2.currentText() == u"원기둥 - 7.5cm":
			doc=App.newDocument()

			# 기본형상
			cir_hex=4 #circle_diameter

			d=75 #d 조절
			exHex=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)

	def onPopupDes21(self):
		if self.popup2.currentText() == u"축연결부싱":
			doc=App.newDocument()

			D = 9.5
			l = 20
			d = 4.11
			d1 = 3.33
			i = 0
			n = 2

			cir = Part.makeCylinder(D/2,l,Vector(0,0,0))
			cir1 = Part.makeCylinder(d/2,l,Vector(0,0,0))
			cir = cir.cut(cir1)

			hole=[]
			for i in range(n):
				hole.append(Part.makeCylinder(d1/2,100,Vector(0,D,(D+d)*i+1.5+d/2),Vector(0,-1,0)))

			for i in hole:
				cir = cir.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=cir
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		if self.popup2.currentText() == u"조정부싱":
			doc=App.newDocument()

			D = 9.44
			D1 = 10.13
			D2 = 7.30
			h = 6.5
			h1 = 6.20
			h2 = 18.10
			t = 2.75
			d = 4.11
			d1 = 3.33
			d2 = 3.94


			circle = Part.makeCylinder(D/2,h,Vector(0,0,0))
			cir1 = Part.makeCylinder(d1/2,D,Vector(-D/2,0,6.5/2),Vector(1,0,0))
			circle = circle.cut(cir1)
			cir2 = Part.makeCylinder(d/2,h+h1,Vector(0,0,0), Vector(0,0,1))
			circle = circle.cut(cir2)


			#Part.show(circle)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

		if self.popup2.currentText() == u"사각홀고무부싱":
			doc=App.newDocument()

			R1 = 7.0
			H = 3.45
			H_f1 = 2.3
			H_f2 = 0.8
			D1 = 3.0

			base1 = Part.makeCylinder(R1,H*2,Vector(0,-H,0),Vector(0,1,0),360)

			tri = Part.makePolygon([(R1-(H_f1-H_f2)*sqrt(3),0,0),(R1,-H_f1+H_f2,0),(R1,H_f1-H_f2,0),(R1-(H_f1-H_f2)*sqrt(3),0,0)])
			face = Part.Face(tri)
			solid = face.revolve(Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.cut(solid)

			tri1 = Part.makePolygon([(R1-(H_f1-H_f2)*sqrt(3),3.45,0),(R1,3.45-H_f1+H_f2,0),(R1,3.45+H_f1-H_f2,0),(R1-(H_f1-H_f2)*sqrt(3),3.45,0)])
			face1 = Part.Face(tri1)
			solid1 = face1.revolve(Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.cut(solid1)

			tri2 = Part.makePolygon([(R1-(H_f1-H_f2)*sqrt(3),-3.45,0),(R1,-3.45-H_f1+H_f2,0),(R1,H_f1-H_f2-3.45,0),(R1-(H_f1-H_f2)*sqrt(3),-3.45,0)])
			face2 = Part.Face(tri2)
			solid2 = face2.revolve(Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.cut(solid2)

			base3 = Part.makeCylinder(5.0,H_f2+10,Vector(0,H_f1,0),Vector(0,1,0),360)
			base4 = Part.makeCylinder(3.9,H_f2+10,Vector(0,H_f1,0),Vector(0,1,0),360)
			base3 = base3.cut(base4)
			base1 = base1.cut(base3)

			base5 = Part.makeCylinder(5.0,H_f2+10,Vector(0,-H_f1,0),Vector(0,-1,0),360)
			base6 = Part.makeCylinder(3.9,H_f2+10,Vector(0,-H_f1,0),Vector(0,-1,0),360)
			base5 = base5.cut(base6)
			base1 = base1.cut(base5)

			base2 = Part.makeBox(3.0,3.0,50,Vector(-1.5,-25,-1.5),Vector(0,1,0))
			base1 = base1.cut(base2)

			#Part.show(base1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=base1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

		if self.popup2.currentText() == u"플라스틱부싱 0.6cm":
			doc=App.newDocument()

			D = 8
			t = 6
			d = 4.48
			f = 0.5

			circle = Part.makeCylinder(D/2,t,Vector(0,0,0))
			circle = circle.makeFillet(f,[circle.Edges[0],circle.Edges[2]])
			circle1 = Part.makeCylinder(d/2,t,Vector(0,0,0))
			circle = circle.cut(circle1)

			#Part.show(circle)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

		if self.popup2.currentText() == u"플라스틱부싱 1.2cm":
			doc=App.newDocument()

			D = 8
			t = 12
			d = 4.48
			f = 0.5

			circle = Part.makeCylinder(D/2,t,Vector(0,0,0))
			circle = circle.makeFillet(f,[circle.Edges[0],circle.Edges[2]])
			circle1 = Part.makeCylinder(d/2,t,Vector(0,0,0))
			circle = circle.cut(circle1)

			#Part.show(circle)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

		if self.popup2.currentText() == u"실리콘부싱 0.6cm":
			doc=App.newDocument()

			D = 8
			h = 6
			d=2.8
			circle = Part.makeCylinder(D/2,h,Vector(0,0,0))
			box = Part.makeBox(d,d,h,Vector(-1.4,-1.4,0))
			circle = circle.cut(box)


			#Part.show(circle)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.8,0.8,0.8)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")


	def onPopupDes22(self):
		if self.popup2.currentText() == u"지지판":
			doc=App.newDocument()

			x = 36.4
			x1 = 15
			y = 12.7
			h = 13.8
			t = 0.85
			d = 4.11
			i = 0
			n = 3

			plate1 = Part.makeBox(x,y,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(y/2-0.001, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])
			plate2 = Part.makeBox(x1,y,t,Vector((x-x1)/2,0,0))
			plate3 = Part.makeBox(t,y,h,Vector((x-x1)/2,0,0),Vector(0,0,1))
			plate4 = Part.makeBox(t,y,h,Vector(x-(x-x1)/2-t,0,0),Vector(0,0,1))
			plate1 = plate1.cut(plate2)
			plate1 = plate1.fuse(plate3)
			plate1 = plate1.fuse(plate4)

			plate5 = Part.makeBox(x1,y,t,Vector((x-x1)/2,0,h),Vector(0,0,1))
			plate1 = plate1.fuse(plate5)

			cir = []
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,h+t,Vector((x-y)/(n-1)*i+y/2,y/2,0)))
			for i in cir:
				plate1 = plate1.cut(i)\

			cir1 = Part.makeCylinder(d/2,x1,Vector((x-x1)/2,y/2,h/2),Vector(1,0,0))
			plate1 = plate1.cut(cir1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.popup2.currentText() == u"스프링클립":
			doc=App.newDocument()

			D = 6.35
			d = 3.59
			x = 6.44
			y = 5.27
			t = 1.34
			l = 2.86
			h = 9
			circle = Part.makeCylinder(D/2,y,Vector(0,0,0),Vector(0,1,0))
			circle1 = Part.makeCylinder(d/2,y,Vector(0,0,0),Vector(0,1,0))
			box = Part.makeBox(l,y,D/2,Vector(-D/2,y,-l/2),Vector(1,0,0))
			box1 = Part.makeBox(l,y,t,Vector(-1.108-0.65,0,-1.43+1.158),Vector(1,0,-1.732))
			box2 = Part.makeBox(l,y,t,Vector(-1.108,0,1.43),Vector(-1,0,-1.732))
			plate1 = Part.makeBox(x,y,t,Vector(-1.084,0,-1.43),Vector(1,0,-1.732))
			plate2 = Part.makeBox(x,y,t,Vector(-1.084+0.65,0,1.43+1.158),Vector(-1,0,-1.732))
			plate1 = plate1.makeFillet(y/2-0.001,[plate1.Edges[4],plate1.Edges[6]])
			plate2 = plate2.makeFillet(y/2-0.001,[plate2.Edges[4],plate2.Edges[6]])

			#circle1 = Part.makeCylinder(d3/2,h1,Vector(0,0,(t-h1)/2))
			circle = circle.cut(circle1)
			circle = circle.cut(box)
			circle = circle.cut(box1)
			circle = circle.cut(box2)
			circle = circle.fuse(plate1)
			circle = circle.fuse(plate2)
			#Part.show(circle)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"양팔크랭크":
			doc=App.newDocument()

			x = 38
			y = 12.7
			h = 9.3
			t = 0.71
			D = 9.25
			d = 4.11
			d1= 3.33

			plate1 = Part.makeBox(x,y,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(y/2-0.01, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])
			plate2 = Part.makeBox(2*d,d,t,Vector(x-5*d/2,(y-d)/2,0))
			plate2 = plate2.makeFillet(d/2-0.01, [plate2.Edges[0],plate2.Edges[2],plate2.Edges[4],plate2.Edges[6]])
			plate1 = plate1.cut(plate2)

			circle1 = Part.makeCylinder(D/2,h,Vector(x/2,y/2,0))
			plate1 = plate1.fuse(circle1)

			cir1 = Part.makeCylinder(d/2,t,Vector(y/2,y/2,0))
			plate1 = plate1.cut(cir1)
			cir2 = Part.makeCylinder(d/2,t,Vector(x/2,y/2,0))
			plate1 = plate1.cut(cir2)
			cir3 = Part.makeCylinder(d/2,h,Vector(x/2,y/2,0))
			plate1 = plate1.cut(cir3)
			cir4 = Part.makeCylinder(d1/2,y,Vector(x/2,0,3*d/2),Vector(0,1,0))
			plate1 = plate1.cut(cir4)


			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"면판휠":
			doc=App.newDocument()

			D1 = 63
			D2 = 8.9
			h = 9.11
			h1 = 0.5
			d = 4.11
			d1 = 3.33
			t = 0.7
			x = 16.5
			x1 = 8.73
			x2 = 17.76
			a = 6.5

			i = 0
			j = 0
			n = 2

			circle = Part.makeCylinder(D1/2,t,Vector(0,0,0))
			circle1 = Part.makeCylinder(D2/2,h,Vector(0,0,-h1))
			circle = circle.fuse(circle1)


			plate1 = Part.makeBox(d,x,t,Vector(-d/2,D2/2+a,0))
			plate1 = plate1.makeFillet(d/2-0.01, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])
			circle = circle.cut(plate1)
			plate2 = Part.makeBox(d,x,t,Vector(-d/2,-D2/2-a-x,0))
			plate2 = plate2.makeFillet(d/2-0.01, [plate2.Edges[0],plate2.Edges[2],plate2.Edges[4],plate2.Edges[6]])
			circle = circle.cut(plate2)
			plate3 = Part.makeBox(x,d,t,Vector(D2/2+a,-d/2,0))
			plate3 = plate3.makeFillet(d/2-0.01, [plate3.Edges[0],plate3.Edges[2],plate3.Edges[4],plate3.Edges[6]])
			circle = circle.cut(plate3)
			plate4 = Part.makeBox(x,d,t,Vector(-D2/2-a-x,-d/2,0))
			plate4 = plate4.makeFillet(d/2-0.01, [plate4.Edges[0],plate4.Edges[2],plate4.Edges[4],plate4.Edges[6]])
			circle = circle.cut(plate4)

			cir1 = Part.makeCylinder(d1/2,D2,Vector(0,-D2/2,3*d/2),Vector(0,1,0))
			circle = circle.cut(cir1)
			cir2 = Part.makeCylinder(d/2,h,Vector(0,0,-h1))
			circle = circle.cut(cir2)

			cir3 = []
			cir4 = []
			for i in range(n):
				for j in range(n):
					cir3.append(Part.makeCylinder(d/2,t,Vector(-x1+2*x1*i,-x1+2*x1*j,0)))
			for i in cir3:
				circle = circle.cut(i)

			for i in range(n):
				for j in range(n):
					cir4.append(Part.makeCylinder(d/2,t,Vector(-x2+2*x2*i,-x2+2*x2*j,0)))
			for i in cir4:
				circle = circle.cut(i)


			#Part.show(circle)
			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"나사핀":
			doc=App.newDocument()

			# 기본형상
			cir_hex=3.8 #circle_diameter

			d=34.2
			exHex=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))

			# 나사선 helix
			helix = Part.makeHelix(0.797,8.8,2) #50넣으면 메모리 문제로 실행 안될 수 있음.            #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((1.6,0,-0.125), (1.6,0,0.125))
			edge2 = Part.makeLine((1.6,0,0.125), (2.2,0,0.419))
			edge3 = Part.makeLine((2.2,0,0.419), (2.2,0,-0.419))
			edge4 = Part.makeLine((2.2,0,-0.419), (1.6,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)

		elif self.popup2.currentText() == u"프로펠러":
			doc=App.newDocument()

			pro = Part.makeCone(7.2,1.2,14.7)
			#box1 = Part.makeBox(55,12,2.5,Vector(0,-6,3))
			#box2 = Part.makeBox(55,12,2.5,Vector(-55,-6,3))
			#box1 = box1.makeFillet(4,[box1.Edges[4],box1.Edges[6]])

			#pro = pro.fuse(box1)
			#pro = pro.fuse(box2)

			extend1 = Part.makePolygon([(0,2.5,3),(4,3,3),(32,5,3),(52,2.5,3),(52,-2.5,3),(32,-5,3),(4,-3,3),(0,-2.5,3),(-4,-3,3),(-32,-5,3),(-52,-2.5,3),(-52,2.5,3),(-32,5,3),(-4,3,3),(0,2.5,3)])
			fa2 = Part.Face(extend1)
			p2 = fa2.extrude(Vector(0,0,1))
			pro = pro.fuse(p2)

			#Part.show(pro)
			shape=doc.addObject("Part::Feature")
			shape.Shape=pro
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"훅":
			doc=App.newDocument()

			cy1 = Part.makeCylinder(3.9,5.8,Vector(0,0,0),Vector(0,0,1),360)
			cy2 = Part.makeCylinder(1.95,5.8,Vector(0,0,0),Vector(0,0,1),360)
			cy1 = cy1.cut(cy2)

			cy3 = Part.makeCylinder(2.5,10.0,Vector(-3.0,0,2.9),Vector(-1,0,0),360)
			cy1 = cy1.fuse(cy3)

			tor = Part.makeTorus(8.5, 2.5,Vector(-22.0,0,2.9),Vector(0,0,1),0,360,300)
			tor.rotate(Vector(-22,0,2.9),Vector(0,0,-1),13)

			tri1 = Part.makePolygon([(-16.126,-1.38,0),(-9.96,-2.77,0),(-13.126,-5,0),(-16.126,-1.38,0)])
			fa1 = Part.Face(tri1)
			p1 = fa1.extrude(Vector(0,0,6))
			cy1 = cy1.cut(p1)

			cy1 = cy1.fuse(tor)
			#Part.show(cy1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=cy1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0,0.4,1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"파워핸들":
			doc=App.newDocument()

			D = 9.44
			D1 = 10.13
			D2 = 7.30
			h = 7.5
			h1 = 6.20
			h2 = 18.10
			t = 2.75
			d = 4.11
			d1 = 3.33
			d2 = 3.94


			circle = Part.makeCylinder(D/2,h,Vector(0,0,0))
			cir1 = Part.makeCylinder(d1/2,D,Vector(-D/2,0,1.65+d/2),Vector(1,0,0))
			circle = circle.cut(cir1)
			cir3 = Part.makeCylinder(D1/2,h1,Vector(0,0,h))
			circle = circle.fuse(cir3)
			plate1 = Part.makePolygon([(0.556226,5.025,h+h1),(12.885+0.400834,3.627654,h+h1),(12.885+0.400834,-3.627654,h+h1),(0.556226,-5.025,h+h1),(0.556226,5.025,h+h1)])
			plate1 = Part.Face(plate1)
			plate1 = plate1.extrude(Vector(0,0,-t))
			circle = circle.fuse(plate1)
			cir2 = Part.makeCylinder(d/2,h+h1,Vector(0,0,0), Vector(0,0,1))
			circle = circle.cut(cir2)
			cir4 = Part.makeCylinder(D2/2,t,Vector(12.885,0,h+h1),Vector(0,0,-1))
			circle = circle.cut(cir2)
			circle = circle.fuse(cir4)
			cir5 = Part.makeCylinder(d2/2,h2-t-d2/2,Vector(12.885,0,h+h1),Vector(0,0,1))
			circle = circle.fuse(cir5)
			sphere = Part.makeSphere(d2/2,Vector(12.885,0,h+h1+h2-t-d2/2),Vector(0,0,1),0,90,360)
			circle = circle.fuse(sphere)

			#Part.show(circle)
			#Part.show(sphere)
			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"축이음쇠":
			doc=App.newDocument()

			# 기본형상 hexagon, circle
			s_hex=6.9 #hexagon_diameter
			k_hex=20 #height

			mhex=Base.Matrix()
			mhex.rotateZ(math.radians(60.0))
			polygon = []
			vhex=Base.Vector(s_hex/math.sqrt(3.0),0.0,-k_hex)
			for i in range(6):
				polygon.append(vhex)
				vhex = mhex.multiply(vhex)
			polygon.append(vhex)
			hexagon = Part.makePolygon(polygon)
			face=Part.Face(hexagon)
			exHex=face.extrude(Base.Vector(0.0,0.0,k_hex)) #높이

			d=30
			cir_hex=6.8 #circle_diameter
			circ=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,-25))
			exHex=exHex.fuse(circ)

			d=40
			cir_hex1=4.0 #circle_diameter
			circ1=Part.makeCylinder(cir_hex1/2.0,d,Vector(0,0,-35))
			exHex=exHex.cut(circ1)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)
		elif self.popup2.currentText() == u"모터뭉치":
			doc=App.newDocument()

			x=34.8
			x1= 16.82
			y1=17.25
			t=1.8
			d=4.2
			d1=11.20
			d2=32
			d3=21
			d4=3.95
			h1=16.23
			h2=30
			h3=3.0
			h4=1.95
			h5=15.6
			h6=29.75
			h7=15.3
			f=4.95
			n=3
			i=0
			j=0
			cir=[]

			plate1 = Part.makeBox(x,x,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])
			plate2 = Part.makeBox(x1,y1,h1,Vector(8.99,8.775,0))
			plate3 = Part.makeBox(x1-2*t,y1-2*t,h7,Vector(8.99+t,8.775+t,0))
			plate1 = plate1.fuse(plate2)
			plate1 = plate1.cut(plate3)

			for i in range(n):
			   for j in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(4.65+12.75*i,4.65+12.75*j,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			circle1 = Part.makeCylinder(d2/2,h6,Vector(x/2,8.775-3.6,h2),Vector(0,1,0))
			circle2 = Part.makeCylinder(d1/2,h3,Vector(x/2,8.775-3.6,h2),Vector(0,-1,0))
			circle3 = Part.makeCylinder(d3/2,h4,Vector(x/2,8.775-3.6+h6,h2),Vector(0,1,0))
			circle4 = Part.makeCylinder(d4/2,h5,Vector(x/2,8.775-3.6+h6+h4,h2),Vector(0,1,0))
			plate1 = plate1.fuse(circle1)
			plate1 = plate1.fuse(circle2)
			plate1 = plate1.fuse(circle3)
			plate1 = plate1.fuse(circle4)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"구동기어뭉치":

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=0.48, z=54, alpha=20 * pi / 180., clearence=0, shift=0., beta=0., undercut=False, simple=False, height=3.0, backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                self.m_n = 0.5
			                self.z = 36
			                self.height = 3.0
			                self.m = self.m_n / cos(self.beta)
			                self.c = self.clearence * self.m_n
			                self.midpoint = [0., 0]
			                self.d = self.z * self.m
			                self.dw = self.m * self.z
			                self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			                self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			                self.dg = self.d * cos(self.alpha_t)
			                self.phipart = 2 * pi / self.z
			                self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			                self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			                self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			                self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			                self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot = self.involute_rot1 + self.involute_rot2
			                self.involute_start = 0.
			                if self.dg <= self.df:
			                    self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			                pts = self.points(self.numpoints)
			                if not self.simple:
			                    wi = []
			                    for i in pts:
			                        out = BSplineCurve()
			                        out.interpolate(map(fcvec, i))
			                        wi.append(out)
			                    s = Wire(Shape(wi).Edges)
			                    wi = []
			                    for i in range(self.z):
			                        rot = App.Matrix()
			                        rot.rotateZ(-i * self.phipart)
			                        tooth_rot = s.transformGeometry(rot)
			                        if i != 0:
			                            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                            pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                            wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                        wi.append(tooth_rot)
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                    wi = Wire(wi)
			                    self.Shapea = wi
			                    if self.beta == 0:
			                        sh = Face(wi)
			                        self.Shapea = sh.extrude(App.Vector(0, 0, self.height))
			                        self.Shapea.translate(Vector(11.0,-5.0,-3.5))
			                    self.Shape = self.Shape.fuse(self.Shapea)


			                self.m_n = 0.57
			                self.z = 10
			                self.height = 6.6
			                self.m = self.m_n / cos(self.beta)
			                self.c = self.clearence * self.m_n
			                self.midpoint = [0., 0]
			                self.d = self.z * self.m
			                self.dw = self.m * self.z
			                self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			                self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			                self.dg = self.d * cos(self.alpha_t)
			                self.phipart = 2 * pi / self.z
			                self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			                self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			                self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			                self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			                self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot = self.involute_rot1 + self.involute_rot2
			                self.involute_start = 0.
			                if self.dg <= self.df:
			                    self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			                pts = self.points(self.numpoints)
			                if not self.simple:
			                    wi = []
			                    for i in pts:
			                        out = BSplineCurve()
			                        out.interpolate(map(fcvec, i))
			                        wi.append(out)
			                    s = Wire(Shape(wi).Edges)
			                    wi = []
			                    for i in range(self.z):
			                        rot = App.Matrix()
			                        rot.rotateZ(-i * self.phipart)
			                        tooth_rot = s.transformGeometry(rot)
			                        if i != 0:
			                            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                            pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                            wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                        wi.append(tooth_rot)
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                    wi = Wire(wi)
			                    self.Shapea = wi
			                    if self.beta == 0:
			                        sh = Face(wi)
			                        self.Shapea = sh.extrude(App.Vector(0, 0, self.height))
			                        self.Shapea.translate(Vector(11.0,-5.0,-9.5))
			                    self.Shape = self.Shape.fuse(self.Shapea)


			                self.m_n = 0.52
			                self.z = 10
			                self.height = 9.5
			                self.m = self.m_n / cos(self.beta)
			                self.c = self.clearence * self.m_n
			                self.midpoint = [0., 0]
			                self.d = self.z * self.m
			                self.dw = self.m * self.z
			                self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			                self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			                self.dg = self.d * cos(self.alpha_t)
			                self.phipart = 2 * pi / self.z
			                self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			                self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			                self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			                self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			                self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot = self.involute_rot1 + self.involute_rot2
			                self.involute_start = 0.
			                if self.dg <= self.df:
			                    self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			                pts = self.points(self.numpoints)
			                if not self.simple:
			                    wi = []
			                    for i in pts:
			                        out = BSplineCurve()
			                        out.interpolate(map(fcvec, i))
			                        wi.append(out)
			                    s = Wire(Shape(wi).Edges)
			                    wi = []
			                    for i in range(self.z):
			                        rot = App.Matrix()
			                        rot.rotateZ(-i * self.phipart)
			                        tooth_rot = s.transformGeometry(rot)
			                        if i != 0:
			                            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                            pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                            wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                        wi.append(tooth_rot)
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                    wi = Wire(wi)
			                    self.Shapea = wi
			                    if self.beta == 0:
			                        sh = Face(wi)
			                        self.Shapea = sh.extrude(App.Vector(0, 0, self.height))
			                        self.Shapea.translate(Vector(0,0,-9.5))
			                        self.Shapea.rotate(Vector(0,0,0),Vector(0,0,1),15)
			                    self.Shape = self.Shape.fuse(self.Shapea)

			                self.m_n = 0.48
			                self.z = 10
			                self.height = 7.5
			                self.m = self.m_n / cos(self.beta)
			                self.c = self.clearence * self.m_n
			                self.midpoint = [0., 0]
			                self.d = self.z * self.m
			                self.dw = self.m * self.z
			                self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			                self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			                self.dg = self.d * cos(self.alpha_t)
			                self.phipart = 2 * pi / self.z
			                self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			                self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			                self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			                self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			                self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot = self.involute_rot1 + self.involute_rot2
			                self.involute_start = 0.
			                if self.dg <= self.df:
			                    self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			                pts = self.points(self.numpoints)
			                if not self.simple:
			                    wi = []
			                    for i in pts:
			                        out = BSplineCurve()
			                        out.interpolate(map(fcvec, i))
			                        wi.append(out)
			                    s = Wire(Shape(wi).Edges)
			                    wi = []
			                    for i in range(self.z):
			                        rot = App.Matrix()
			                        rot.rotateZ(-i * self.phipart)
			                        tooth_rot = s.transformGeometry(rot)
			                        if i != 0:
			                            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                            pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                            wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                        wi.append(tooth_rot)
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                    wi = Wire(wi)
			                    self.Shapea = wi
			                    if self.beta == 0:
			                        sh = Face(wi)
			                        self.Shapea = sh.extrude(App.Vector(0, 0, self.height))
			                        self.Shapea.translate(Vector(-15.7,0,-4.5))
			                        self.Shapea.rotate(Vector(-15.7,0,-4.5),Vector(0,0,1),15)
			                    self.Shape = self.Shape.fuse(self.Shapea)

			                self.m_n = 0.57
			                self.z = 20
			                self.height = 5.0
			                self.m = self.m_n / cos(self.beta)
			                self.c = self.clearence * self.m_n
			                self.midpoint = [0., 0]
			                self.d = self.z * self.m
			                self.dw = self.m * self.z
			                self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			                self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			                self.dg = self.d * cos(self.alpha_t)
			                self.phipart = 2 * pi / self.z
			                self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			                self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			                self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			                self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			                self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot = self.involute_rot1 + self.involute_rot2
			                self.involute_start = 0.
			                if self.dg <= self.df:
			                    self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			                pts = self.points(self.numpoints)
			                if not self.simple:
			                    wi = []
			                    for i in pts:
			                        out = BSplineCurve()
			                        out.interpolate(map(fcvec, i))
			                        wi.append(out)
			                    s = Wire(Shape(wi).Edges)
			                    wi = []
			                    for i in range(self.z):
			                        rot = App.Matrix()
			                        rot.rotateZ(-i * self.phipart)
			                        tooth_rot = s.transformGeometry(rot)
			                        if i != 0:
			                            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                            pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                            wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                        wi.append(tooth_rot)
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                    wi = Wire(wi)
			                    self.Shapea = wi
			                    if self.beta == 0:
			                        sh = Face(wi)
			                        self.Shapea = sh.extrude(App.Vector(0, 0, self.height))
			                        self.Shapea.translate(Vector(18.5,-9.5,-9.1))
			                    self.Shape = self.Shape.fuse(self.Shapea)

			                self.cy1 = Part.makeCylinder(2.0,35.4,Vector(18.5,-9.5,-9.1),Vector(0,0,-1))
			                self.Shape = self.Shape.fuse(self.cy1)
			                self.cy2 = Part.makeCylinder(1.3,35.4,Vector(11.0,-5.0,-9.5),Vector(0,0,-1))
			                self.Shape = self.Shape.fuse(self.cy2)
			                self.cy3 = Part.makeCylinder(1.3,35.4,Vector(0,0,-9.5),Vector(0,0,-1))
			                self.Shape = self.Shape.fuse(self.cy3)
			                self.cy4 = Part.makeCylinder(1.0,40.0,Vector(-15.7,0,-4.5),Vector(0,0,-1))
			                self.Shape = self.Shape.fuse(self.cy4)
			                self.cy5 = Part.makeCylinder(10.5,3.8,Vector(-15.7,0,-11.5),Vector(0,0,-1))
			                self.Shape = self.Shape.fuse(self.cy5)
			                self.cy6 = Part.makeCylinder(13.6,26.3,Vector(-15.7,0,-15.3),Vector(0,0,-1))
			                self.Shape = self.Shape.fuse(self.cy6)
			                self.cy7 = Part.makeCylinder(4.2,2.0,Vector(-15.7,0,-15.3-26.3),Vector(0,0,-1))
			                self.Shape = self.Shape.fuse(self.cy7)

			                extend1 = Part.makePolygon([(0,11,-9.5),(-30,11,-9.5),(-30,-17.4,-9.5),(13.5,-17.4,-9.5),(23.0,-13,-9.5),(23.0,-8.9,-9.5),(0,11,-9.5)])
			                fa1 = Part.Face(extend1)
			                p1 = fa1.extrude(Vector(0,0,-0.8))
			                self.Shape = self.Shape.fuse(p1)
			                p2 = p1.mirror(Vector(0,0,-26.5),Vector(0,0,1))
			                self.Shape = self.Shape.fuse(p2)

			                extend3 = Part.makePolygon([(-30,-17.4,-9.5),(-30,-17.4,-43),(13.5,-17.4,-43),(13.5,-17.4,-9.5),(-30.0,-17.4,-9.5)])
			                fa3 = Part.Face(extend3)
			                p3 = fa3.extrude(Vector(0,0.8,0))
			                self.Shape = self.Shape.fuse(p3)

			                self.cy8 = Part.makeCylinder(2.1,2,Vector(6.0,-17.4,-20),Vector(0,1,0))
			                self.Shape = self.Shape.cut(self.cy8)
			                self.cy9 = Part.makeCylinder(2.1,2,Vector(-6.0,-17.4,-20),Vector(0,1,0))
			                self.Shape = self.Shape.cut(self.cy9)
			                self.cy10 = Part.makeCylinder(2.1,2,Vector(6.0,-17.4,-32),Vector(0,1,0))
			                self.Shape = self.Shape.cut(self.cy10)
			                self.cy11 = Part.makeCylinder(2.1,2,Vector(-6.0,-17.4,-32),Vector(0,1,0))
			                self.Shape = self.Shape.cut(self.cy11)

			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])


			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"캐노피":

			doc=App.newDocument()

			A = Part.makeSphere(33.0,Vector(0,0,0),Vector(0,0,1),0,90,90)
			B = Part.makeSphere(31.5,Vector(0,0,0),Vector(0,0,1),0,90,90)
			A = A.cut(B)

			cy4 = Part.makeCylinder(6.0 ,1.5,Vector(0,0,31.5),Vector(0,0,1),90)
			cy4.rotate(Vector(0,0,31.5),Vector(0,0,1),180)
			A = A.fuse(cy4)
			cy5 = Part.makeCylinder(6.0 ,1.5,Vector(0,31.5,0),Vector(0,1,0),90)
			cy5.rotate(Vector(0,31.5,0),Vector(0,1,0),180)
			A = A.fuse(cy5)
			cy6 = Part.makeCylinder(6.0 ,1.5,Vector(31.5,0,0),Vector(1,0,0),90)
			cy6.rotate(Vector(31.5,0,0),Vector(1,0,0),90)
			A = A.fuse(cy6)

			arc1=Part.makeCircle(33.0,Vector(0,0,0),Vector(0,0,1),0,90)
			Line1=Part.makeLine(Vector(0,33.0,0),Vector(0,31.5,0))
			arc2=Part.makeCircle(31.5,Vector(0,0,0),Vector(0,0,1),0,90)
			Line2=Part.makeLine(Vector(33.0,0,0),Vector(31.5,0,0))
			arc1=arc1.fuse(arc2)
			arc1=arc1.fuse(Line1)
			arc1=arc1.fuse(Line2)
			w1 = Part.Wire(arc1.Edges)
			face = Part.Face(w1)
			p = face.extrude(Vector(0,0,-6.0))
			A=A.fuse(p)

			aarc1=Part.makeCircle(33.0,Vector(0,0,0),Vector(1,0,0),0,90)
			aLine1=Part.makeLine(Vector(0,33.0,0),Vector(0,31.5,0))
			aarc2=Part.makeCircle(31.5,Vector(0,0,0),Vector(1,0,0),0,90)
			aLine2=Part.makeLine(Vector(0,0,33.0),Vector(0,0,31.5))
			aarc1=aarc1.fuse(aarc2)
			aarc1=aarc1.fuse(aLine1)
			aarc1=aarc1.fuse(aLine2)
			aw1 = Part.Wire(aarc1.Edges)
			aface = Part.Face(aw1)
			ap = aface.extrude(Vector(-6.0,0,0))
			A=A.fuse(ap)

			barc1=Part.makeCircle(33.0,Vector(0,0,0),Vector(0,-1,0),0,90)
			barc2=Part.makeCircle(31.5,Vector(0,0,0),Vector(0,-1,0),0,90)
			bLine1=Part.makeLine(Vector(33.0,0,0),Vector(31.5,0,0))
			bLine2=Part.makeLine(Vector(0,0,33.0),Vector(0,0,31.5))
			barc1=barc1.fuse(barc2)
			barc1=barc1.fuse(bLine1)
			barc1=barc1.fuse(bLine2)
			bw1 = Part.Wire(barc1.Edges)
			bface = Part.Face(bw1)
			bp = bface.extrude(Vector(0,-6.0,0))
			A=A.fuse(bp)

			cy1 = Part.makeCylinder(2.0 ,5,Vector(0,0,31),Vector(0,0,1))
			A = A.cut(cy1)
			cy2 = Part.makeCylinder(2.0 ,5,Vector(0,31,0),Vector(0,1,0))
			A = A.cut(cy2)
			cy3 = Part.makeCylinder(2.0 ,5,Vector(31,0,0),Vector(1,0,0))
			A = A.cut(cy3)

			#Part.show(A)

			shape=doc.addObject("Part::Feature")
			shape.Shape=A
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

		elif self.popup2.currentText() == u"기어드모터":
			doc=App.newDocument()

			x=34.8
			y=34.3
			h=24.7
			h1=3
			h2=3.95
			h3=14.3
			d=3.9
			d1=3.95
			x1= 16.0
			l=4.45
			l1=12.7
			n=3
			n1=2
			n2=5
			i=0
			j=0

			cir=[]
			cir1=[]
			cir5=[]
			cir6=[]
			cir7=[]
			cir8=[]
			cir9=[]
			cir10=[]
			cir11=[]
			cir12=[]

			plate1 = Part.makeBox(x,y,h,Vector(0,0,0))
			plate2 = Part.makeBox(x1,y,h2,Vector((x-x1)/2,0,h))
			plate1 = plate1.fuse(plate2)

			for i in range(n):
					cir.append(Part.makeCylinder(d/2,h1,Vector(x/2,l+l1*i,h+h2)))
			for i in cir:
				plate1 = plate1.fuse(i)

			for i in range(n):
					cir1.append(Part.makeCylinder(d/2,h1,Vector(x/2,l+l1*i,0),Vector(0,0,-1)))
			for i in cir1:
				plate1 = plate1.fuse(i)

			cir3 = Part.makeCylinder(d1/2,h3,Vector(x/2,y,h-4.045),Vector(0,1,0))
			cir4 = Part.makeCylinder(d/2,h1,Vector(x/2,y,h-4.045-12.66),Vector(0,1,0))
			plate1 = plate1.fuse(cir3)
			plate1 = plate1.fuse(cir4)

			for i in range(n):
			        cir5.append(Part.makeCylinder(d/2,h1,Vector((x-28.6+d)/2+((28.6-d)/2)*i,0,h-4.045-12.66),Vector(0,-1,0)))
			for i in cir5:
				plate1 = plate1.fuse(i)

			for i in range(n1):
			        cir6.append(Part.makeCylinder(d/2,h1,Vector((x-28.6+d)/2+(28.6-d)*i,0,h-4.045),Vector(0,-1,0)))
			for i in cir6:
				plate1 = plate1.fuse(i)

			plate3 = Part.makeBox(7.25,3.25,7.06,Vector(x/2-7.25/2,-3.25,h+h2-9.21-7.06))
			plate1 = plate1.fuse(plate3)

			for i in range(n2):
					cir7.append(Part.makeCylinder(d/2,h1,Vector(0,l+(l1*2)/4*i,h-4.045-12.66/2), Vector(1,0,0)))
			for i in cir7:
				plate1 = plate1.cut(i)

			for i in range(n2):
					cir8.append(Part.makeCylinder(d/2,h1,Vector(x,l+(l1*2)/4*i,h-4.045-12.66/2), Vector(-1,0,0)))
			for i in cir8:
				plate1 = plate1.cut(i)

			for i in range(n2):
					cir9.append(Part.makeCylinder(d/2,h1,Vector((x-28.6+d)/2,l+(l1*2)/4*i,0), Vector(0,0,1)))
			for i in cir9:
				plate1 = plate1.cut(i)

			for i in range(n2):
					cir10.append(Part.makeCylinder(d/2,h1,Vector((x-28.6+d)/2+(28.6-d),l+(l1*2)/4*i,0), Vector(0,0,1)))
			for i in cir10:
				plate1 = plate1.cut(i)


			for i in range(n1):
			   for j in range(n1):
					cir11.append(Part.makeCylinder(d/2,h1,Vector(0,l+(l1)/2+l1*i,h-4.045-12.66*j),Vector(1,0,0)))

			for i in cir11:
				plate1 = plate1.cut(i)

			for i in range(n1):
			   for j in range(n1):
					cir12.append(Part.makeCylinder(d/2,h1,Vector(x,l+(l1)/2+l1*i,h-4.045-12.66*j),Vector(-1,0,0)))

			for i in cir12:
				plate1 = plate1.cut(i)


			#Part.show(plate1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.8,0.8,0.8)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"이동클립":
			doc=App.newDocument()

			h1 = 3.52
			y1 = 12.7
			x1 = 14.4
			f = 1
			t = 0.7
			D = 9.5
			d = 4.11
			d1 = 3.11
			h2 = 5
			H = 14.6-2*h1

			plate=Part.makeBox(x1,y1,h1,Vector(-x1/2,-y1/2,0))
			plate1=Part.makeBox(y1,y1,h1,Vector(-y1/2,-y1/2,h1))
			plate2=Part.makeBox(x1-2*t,y1,h1-2*t,Vector(-x1/2+t,-y1/2,t))
			plate3=Part.makeBox(y1-2*t,y1,2*h1-t,Vector(-y1/2+t,-y1/2,0))
			plate=plate.makeFillet(f,[plate.Edges[1],plate.Edges[3],plate.Edges[5],plate.Edges[7]])
			plate1=plate1.makeFillet(f,[plate1.Edges[1],plate1.Edges[5]])
			plate2=plate2.makeFillet(f-t/2,[plate2.Edges[1],plate2.Edges[3],plate2.Edges[5],plate2.Edges[7]])
			plate3=plate3.makeFillet(f-t/2,[plate3.Edges[1],plate3.Edges[5]])
			plate=plate.fuse(plate1)
			plate=plate.cut(plate2)
			plate=plate.cut(plate3)

			circle=Part.makeCylinder(D/2,H,Vector(0,0,2*h1))
			circle1=Part.makeCylinder(d/2,H+t,Vector(0,0,2*h1-t))
			circle2=Part.makeCylinder(d1/2,D,Vector(0,-D/2,2*h1+h2),Vector(0,1,0))
			plate=plate.fuse(circle)
			plate=plate.cut(circle1)
			plate=plate.cut(circle2)
			#Part.show(plate)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.popup2.currentText() == u"홈샤프트":
			doc=App.newDocument()

			h = 0
			mat = []
			p1 = Base.Vector( 4,  2,  h)
			p2 = Base.Vector( 4, -2,  h)
			p3 = Base.Vector( 2, -4,  h)
			p4 = Base.Vector(-2, -4,  h)
			p5 = Base.Vector(-4, -2,  h)
			p6 = Base.Vector(-4,  2,  h)
			p7 = Base.Vector(-2,  4,  h)
			p8 = Base.Vector( 2,  4,  h)
			mat.append(p1)
			mat.append(p2)
			mat.append(p3)
			mat.append(p4)
			mat.append(p5)
			mat.append(p6)
			mat.append(p7)
			mat.append(p8)
			mat.append(p1)
			box1_poly = Part.makePolygon(mat)
			box1_face = Part.Face(box1_poly)
			box1_body = box1_face.extrude(Base.Vector(0,0,-1))

			h = -2.4
			mat = []
			p1 = Base.Vector( 4,  2,  h)
			p2 = Base.Vector( 4, -2,  h)
			p3 = Base.Vector( 2, -4,  h)
			p4 = Base.Vector(-2, -4,  h)
			p5 = Base.Vector(-4, -2,  h)
			p6 = Base.Vector(-4,  2,  h)
			p7 = Base.Vector(-2,  4,  h)
			p8 = Base.Vector( 2,  4,  h)
			mat.append(p1)
			mat.append(p2)
			mat.append(p3)
			mat.append(p4)
			mat.append(p5)
			mat.append(p6)
			mat.append(p7)
			mat.append(p8)
			mat.append(p1)
			box2_poly = Part.makePolygon(mat)
			box2_face = Part.Face(box2_poly)
			box2_body = box2_face.extrude(Base.Vector(0,0,-1))

			cylinder1 = Part.makeCylinder(2.5, 15.4, Base.Vector(0,0,-1),    Base.Vector(0,0,-1))
			cylinder2 = Part.makeCylinder(  2,    6, Base.Vector(0,0,-16.4), Base.Vector(0,0,-1))

			model = box1_body.fuse(box2_body)
			model = model.fuse(cylinder1)
			model = model.fuse(cylinder2)

			shape=doc.addObject("Part::Feature")
			shape.Shape = model
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

		elif self.popup2.currentText() == u"홈샤프트캡":
			doc=App.newDocument()

			h = 0
			mat = []
			p1 = Base.Vector( 4,  2,  h)
			p2 = Base.Vector( 4, -2,  h)
			p3 = Base.Vector( 2, -4,  h)
			p4 = Base.Vector(-2, -4,  h)
			p5 = Base.Vector(-4, -2,  h)
			p6 = Base.Vector(-4,  2,  h)
			p7 = Base.Vector(-2,  4,  h)
			p8 = Base.Vector( 2,  4,  h)
			mat.append(p1)
			mat.append(p2)
			mat.append(p3)
			mat.append(p4)
			mat.append(p5)
			mat.append(p6)
			mat.append(p7)
			mat.append(p8)
			mat.append(p1)
			box1_poly = Part.makePolygon(mat)
			box1_face = Part.Face(box1_poly)
			box1_body = box1_face.extrude(Base.Vector(0,0,-2))

			cylinder1 = Part.makeCylinder(2.5, 6, Base.Vector(0,0,0), Base.Vector(0,0,-1))
			cylinder2 = Part.makeCylinder(  2, 6, Base.Vector(0,0,0), Base.Vector(0,0,-1))
			box1_body = box1_body.cut(cylinder2)
			cylinder = cylinder1.cut(cylinder2)
			box2 = Part.makeBox(10, 2.4, 2, Base.Vector(5, -1.2, -2), Base.Vector(0,0,-1))
			cylinder = cylinder.common(box2)

			model = box1_body.fuse(cylinder)

			shape=doc.addObject("Part::Feature")
			shape.Shape = model
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

	def onImage0(self):
		ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

		buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/0.jpg"))

		Imageview1 = QtGui.QLabel(ks)
		Imageview1.setPixmap(buf)
		Imageview1.resize(buf.width(), buf.height())
		Imageview1.move(0,0)
		Imageview1.show()

		ks.setWindowTitle("Image")
		ks.move(650,120)
		ks.show()
		ks.exec_()


	def onImage00(self):
		ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

		buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/00.jpg"))

		Imageview1 = QtGui.QLabel(ks)
		Imageview1.setPixmap(buf)
		Imageview1.resize(buf.width(), buf.height())
		Imageview1.move(0,0)
		Imageview1.show()

		ks.setWindowTitle("categorization")
		ks.move(250,120)
		ks.show()
		ks.exec_()

	def onImage1(self):
		ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

		buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/user/ex1.jpg"))

		Imageview1 = QtGui.QLabel(ks)
		Imageview1.setPixmap(buf)
		Imageview1.resize(buf.width(), buf.height())
		Imageview1.move(0,0)
		Imageview1.show()

		ks.setWindowTitle("Image")
		ks.move(680,200)
		ks.show()
		ks.exec_()

	def onImage3(self):
		ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

		buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/user/ex2.jpg"))

		Imageview1 = QtGui.QLabel(ks)
		Imageview1.setPixmap(buf)
		Imageview1.resize(buf.width(), buf.height())
		Imageview1.move(0,0)
		Imageview1.show()

		ks.setWindowTitle("Image")
		ks.move(680,200)
		ks.show()
		ks.exec_()

	def onImage4(self):
		ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

		buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/user/ex3.jpg"))

		Imageview1 = QtGui.QLabel(ks)
		Imageview1.setPixmap(buf)
		Imageview1.resize(buf.width(), buf.height())
		Imageview1.move(0,0)
		Imageview1.show()

		ks.setWindowTitle("Image")
		ks.move(680,200)
		ks.show()
		ks.exec_()

	def onImage5(self):
		ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

		buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/user/ex4.jpg"))

		Imageview1 = QtGui.QLabel(ks)
		Imageview1.setPixmap(buf)
		Imageview1.resize(buf.width(), buf.height())
		Imageview1.move(0,0)
		Imageview1.show()

		ks.setWindowTitle("Image")
		ks.move(680,200)
		ks.show()
		ks.exec_()

	def onImage6(self):
		ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

		buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/user/ex5.jpg"))

		Imageview1 = QtGui.QLabel(ks)
		Imageview1.setPixmap(buf)
		Imageview1.resize(buf.width(), buf.height())
		Imageview1.move(0,0)
		Imageview1.show()

		ks.setWindowTitle("Image")
		ks.move(680,200)
		ks.show()
		ks.exec_()
	def onImage7(self):
		ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

		buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/user/ex6.jpg"))

		Imageview1 = QtGui.QLabel(ks)
		Imageview1.setPixmap(buf)
		Imageview1.resize(buf.width(), buf.height())
		Imageview1.move(0,0)
		Imageview1.show()

		ks.setWindowTitle("Image")
		ks.move(680,200)
		ks.show()
		ks.exec_()
	def onImage12(self):
		ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

		buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/user/ex7.jpg"))

		Imageview1 = QtGui.QLabel(ks)
		Imageview1.setPixmap(buf)
		Imageview1.resize(buf.width(), buf.height())
		Imageview1.move(0,0)
		Imageview1.show()

		ks.setWindowTitle("Image")
		ks.move(680,200)
		ks.show()
		ks.exec_()

	def onImage14(self):
		ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

		buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/user/ex9.jpg"))

		Imageview1 = QtGui.QLabel(ks)
		Imageview1.setPixmap(buf)
		Imageview1.resize(buf.width(), buf.height())
		Imageview1.move(0,0)
		Imageview1.show()

		ks.setWindowTitle("Image")
		ks.move(680,200)
		ks.show()
		ks.exec_()
	def onImage20(self):
		ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

		buf = QtGui.QPixmap(os.path.join(addonPath, "sci_box/user/ex12.jpg"))

		Imageview1 = QtGui.QLabel(ks)
		Imageview1.setPixmap(buf)
		Imageview1.resize(buf.width(), buf.height())
		Imageview1.move(0,0)
		Imageview1.show()

		ks.setWindowTitle("Image")
		ks.move(680,200)
		ks.show()
		ks.exec_()

	def onDesign0(self):
		if self.numericInput0.text() == '1':
			doc=App.newDocument()
			v=12.7
			x=189.75
			t=1
			r=6.35
			n=15
			a=12.5
			f=(x-a*(n-1))/2 #6.5
			i=0
			d=4.1

			plate1=Part.makeBox(x,v,t,Vector(0,0,0))
			plate1=plate1.makeFillet(r-0.01,[plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir=[]
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,r,0)))
			for i in cir:
				plate1=plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '2':

			doc=App.newDocument()
			v=12.7
			x=139.05
			t=1
			r=6.35
			n=11
			a=12.5
			f=(x-a*(n-1))/2 #6.5
			i=0
			d=4.1

			plate1=Part.makeBox(x,v,t,Vector(0,0,0))
			plate1=plate1.makeFillet(r-0.01,[plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir=[]
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,r,0)))
			for i in cir:
				plate1=plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '3':

			doc=App.newDocument()
			v=12.7
			x=113.7
			t=1
			r=6.35
			n=9
			a=12.5
			f=(x-a*(n-1))/2 #6.5
			i=0
			d=4.1

			plate1=Part.makeBox(x,v,t,Vector(0,0,0))
			plate1=plate1.makeFillet(r-0.01,[plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir=[]
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,r,0)))
			for i in cir:
				plate1=plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '4':

			doc=App.newDocument()
			v=12.7
			x=63
			t=1
			r=6.35 #v/2
			n=5
			a=12.5
			f=(x-a*(n-1))/2 #6.5
			i=0
			d=4.1

			plate1=Part.makeBox(x,v,t,Vector(0,0,0))
			plate1=plate1.makeFillet(r-0.01,[plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir=[]
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,r,0)))
			for i in cir:
				plate1=plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '5':

			doc=App.newDocument()

			x = 50.44
			y = 12.81
			t = 0.85
			d = 4.11
			f = 6.4

			plate1 = Part.makeBox(x,y,t,Vector(0,0,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir = []
			cir.append(Part.makeCylinder(d/2,t,Vector(4.1+d/2,y/2,0)))
			cir.append(Part.makeCylinder(d/2,t,Vector(17.1+d/2,y/2,0)))
			cir.append(Part.makeCylinder(d/2,t,Vector(23.1+d/2,y/2,0)))
			cir.append(Part.makeCylinder(d/2,t,Vector(29.5+d/2,y/2,0)))
			cir.append(Part.makeCylinder(d/2,t,Vector(42.1+d/2,y/2,0)))

			for i in cir:
				plate1 = plate1.cut(i)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=plate1      	                           #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

		elif self.numericInput0.text() == '6':
			doc=App.newDocument()

			l = 318
			w = 15.0
			h = 13.5
			t = 0.7
			d = 4.11
			n = 25
			b = n-1

			box = []
			cir = []
			mir = []
			hole = []
			plate1 = Part.makeBox(l,w,t,Vector(0,-w,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(w/2, [plate1.Edges[0],plate1.Edges[4]])
			box1 = Part.makeBox(d,5,t,Vector(6-d/2,-10,0))
			box2 = Part.makeBox(d,5,t,Vector(6+l-12.0-d/2,-10,0))
			cir1 = Part.makeCylinder(d/2,t,Vector(6,-10,0))
			mir1 = Part.makeCylinder(d/2,t,Vector(6,-5,0))
			cir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-10,0))
			mir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-5,0))
			for i in range(1,b):
				box.append(Part.makeBox(d,5,t,Vector(6+(l-12.0)/b*i-d/2,-10,0)))
				cir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-10,0)))
				mir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-5,0)))

			plate1 = plate1.cut(box1)
			plate1 = plate1.cut(box2)
			plate1 = plate1.cut(cir1)
			plate1 = plate1.cut(mir1)
			plate1 = plate1.cut(cir2)
			plate1 = plate1.cut(mir2)

			#print(len(box))
			#print(list(range(1,b)))
			#print(box[22])
			for i in box:
				plate1 = plate1.cut(i)
			for i in cir:
				plate1 = plate1.cut(i)
			for i in mir:
				plate1 = plate1.cut(i)

			plate2 = Part.makeBox(l,t,h-t,Vector(0,-t,t))
			plate2 = plate2.makeFillet(h/2, [plate2.Edges[1],plate2.Edges[5]])
			hole1 = Part.makeCylinder(d/2,t,Vector(6,-t,7),Vector(0,1,0))
			hole2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-t,7),Vector(0,1,0))
			for i in range(1,b):
				hole.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-t,7),Vector(0,1,0)))

			plate2 = plate2.cut(hole1)
			plate2 = plate2.cut(hole2)
			for i in hole:
				plate2 = plate2.cut(i)

			plate1 = plate1.fuse(plate2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '7':
			doc=App.newDocument()

			l = 241
			w = 15.0
			h = 13.5
			t = 0.7
			d = 4.11
			n = 19
			b = n-1

			box = []
			cir = []
			mir = []
			hole = []
			plate1 = Part.makeBox(l,w,t,Vector(0,-w,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(w/2, [plate1.Edges[0],plate1.Edges[4]])
			box1 = Part.makeBox(d,5,t,Vector(6-d/2,-10,0))
			box2 = Part.makeBox(d,5,t,Vector(6+l-12.0-d/2,-10,0))
			cir1 = Part.makeCylinder(d/2,t,Vector(6,-10,0))
			mir1 = Part.makeCylinder(d/2,t,Vector(6,-5,0))
			cir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-10,0))
			mir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-5,0))
			for i in range(1,b):
				box.append(Part.makeBox(d,5,t,Vector(6+(l-12.0)/b*i-d/2,-10,0)))
				cir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-10,0)))
				mir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-5,0)))

			plate1 = plate1.cut(box1)
			plate1 = plate1.cut(box2)
			plate1 = plate1.cut(cir1)
			plate1 = plate1.cut(mir1)
			plate1 = plate1.cut(cir2)
			plate1 = plate1.cut(mir2)

			#print(len(box))
			#print(list(range(1,b)))
			#print(box[22])
			for i in box:
				plate1 = plate1.cut(i)
			for i in cir:
				plate1 = plate1.cut(i)
			for i in mir:
				plate1 = plate1.cut(i)

			plate2 = Part.makeBox(l,t,h-t,Vector(0,-t,t))
			plate2 = plate2.makeFillet(h/2, [plate2.Edges[1],plate2.Edges[5]])
			hole1 = Part.makeCylinder(d/2,t,Vector(6,-t,7),Vector(0,1,0))
			hole2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-t,7),Vector(0,1,0))
			for i in range(1,b):
				hole.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-t,7),Vector(0,1,0)))

			plate2 = plate2.cut(hole1)
			plate2 = plate2.cut(hole2)
			for i in hole:
				plate2 = plate2.cut(i)

			plate1 = plate1.fuse(plate2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '8':
			doc=App.newDocument()

			l = 139
			w = 15.0
			h = 13.5
			t = 0.7
			d = 4.11
			n = 11
			b = n-1

			box = []
			cir = []
			mir = []
			hole = []
			plate1 = Part.makeBox(l,w,t,Vector(0,-w,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(w/2, [plate1.Edges[0],plate1.Edges[4]])
			box1 = Part.makeBox(d,5,t,Vector(6-d/2,-10,0))
			box2 = Part.makeBox(d,5,t,Vector(6+l-12.0-d/2,-10,0))
			cir1 = Part.makeCylinder(d/2,t,Vector(6,-10,0))
			mir1 = Part.makeCylinder(d/2,t,Vector(6,-5,0))
			cir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-10,0))
			mir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-5,0))
			for i in range(1,b):
				box.append(Part.makeBox(d,5,t,Vector(6+(l-12.0)/b*i-d/2,-10,0)))
				cir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-10,0)))
				mir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-5,0)))

			plate1 = plate1.cut(box1)
			plate1 = plate1.cut(box2)
			plate1 = plate1.cut(cir1)
			plate1 = plate1.cut(mir1)
			plate1 = plate1.cut(cir2)
			plate1 = plate1.cut(mir2)

			#print(len(box))
			#print(list(range(1,b)))
			#print(box[22])
			for i in box:
				plate1 = plate1.cut(i)
			for i in cir:
				plate1 = plate1.cut(i)
			for i in mir:
				plate1 = plate1.cut(i)

			plate2 = Part.makeBox(l,t,h-t,Vector(0,-t,t))
			plate2 = plate2.makeFillet(h/2, [plate2.Edges[1],plate2.Edges[5]])
			hole1 = Part.makeCylinder(d/2,t,Vector(6,-t,7),Vector(0,1,0))
			hole2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-t,7),Vector(0,1,0))
			for i in range(1,b):
				hole.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-t,7),Vector(0,1,0)))

			plate2 = plate2.cut(hole1)
			plate2 = plate2.cut(hole2)
			for i in hole:
				plate2 = plate2.cut(i)

			plate1 = plate1.fuse(plate2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '9':
			doc=App.newDocument()

			l = 113.6
			w = 15.0
			h = 13.5
			t = 0.7
			d = 4.11
			n = 9
			b = n-1

			box = []
			cir = []
			mir = []
			hole = []
			plate1 = Part.makeBox(l,w,t,Vector(0,-w,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(w/2, [plate1.Edges[0],plate1.Edges[4]])
			box1 = Part.makeBox(d,5,t,Vector(6-d/2,-10,0))
			box2 = Part.makeBox(d,5,t,Vector(6+l-12.0-d/2,-10,0))
			cir1 = Part.makeCylinder(d/2,t,Vector(6,-10,0))
			mir1 = Part.makeCylinder(d/2,t,Vector(6,-5,0))
			cir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-10,0))
			mir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-5,0))
			for i in range(1,b):
				box.append(Part.makeBox(d,5,t,Vector(6+(l-12.0)/b*i-d/2,-10,0)))
				cir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-10,0)))
				mir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-5,0)))

			plate1 = plate1.cut(box1)
			plate1 = plate1.cut(box2)
			plate1 = plate1.cut(cir1)
			plate1 = plate1.cut(mir1)
			plate1 = plate1.cut(cir2)
			plate1 = plate1.cut(mir2)

			#print(len(box))
			#print(list(range(1,b)))
			#print(box[22])
			for i in box:
				plate1 = plate1.cut(i)
			for i in cir:
				plate1 = plate1.cut(i)
			for i in mir:
				plate1 = plate1.cut(i)

			plate2 = Part.makeBox(l,t,h-t,Vector(0,-t,t))
			plate2 = plate2.makeFillet(h/2, [plate2.Edges[1],plate2.Edges[5]])
			hole1 = Part.makeCylinder(d/2,t,Vector(6,-t,7),Vector(0,1,0))
			hole2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-t,7),Vector(0,1,0))
			for i in range(1,b):
				hole.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-t,7),Vector(0,1,0)))

			plate2 = plate2.cut(hole1)
			plate2 = plate2.cut(hole2)
			for i in hole:
				plate2 = plate2.cut(i)

			plate1 = plate1.fuse(plate2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '10':
			doc=App.newDocument()

			l = 88.2
			w = 15.0
			h = 13.5
			t = 0.7
			d = 4.11
			n = 7
			b = n-1

			box = []
			cir = []
			mir = []
			hole = []
			plate1 = Part.makeBox(l,w,t,Vector(0,-w,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(w/2, [plate1.Edges[0],plate1.Edges[4]])
			box1 = Part.makeBox(d,5,t,Vector(6-d/2,-10,0))
			box2 = Part.makeBox(d,5,t,Vector(6+l-12.0-d/2,-10,0))
			cir1 = Part.makeCylinder(d/2,t,Vector(6,-10,0))
			mir1 = Part.makeCylinder(d/2,t,Vector(6,-5,0))
			cir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-10,0))
			mir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-5,0))
			for i in range(1,b):
				box.append(Part.makeBox(d,5,t,Vector(6+(l-12.0)/b*i-d/2,-10,0)))
				cir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-10,0)))
				mir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-5,0)))

			plate1 = plate1.cut(box1)
			plate1 = plate1.cut(box2)
			plate1 = plate1.cut(cir1)
			plate1 = plate1.cut(mir1)
			plate1 = plate1.cut(cir2)
			plate1 = plate1.cut(mir2)

			#print(len(box))
			#print(list(range(1,b)))
			#print(box[22])
			for i in box:
				plate1 = plate1.cut(i)
			for i in cir:
				plate1 = plate1.cut(i)
			for i in mir:
				plate1 = plate1.cut(i)

			plate2 = Part.makeBox(l,t,h-t,Vector(0,-t,t))
			plate2 = plate2.makeFillet(h/2, [plate2.Edges[1],plate2.Edges[5]])
			hole1 = Part.makeCylinder(d/2,t,Vector(6,-t,7),Vector(0,1,0))
			hole2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-t,7),Vector(0,1,0))
			for i in range(1,b):
				hole.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-t,7),Vector(0,1,0)))

			plate2 = plate2.cut(hole1)
			plate2 = plate2.cut(hole2)
			for i in hole:
				plate2 = plate2.cut(i)

			plate1 = plate1.fuse(plate2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '11':
			doc=App.newDocument()

			l = 37.4
			w = 15.0
			h = 13.5
			t = 0.7
			d = 4.11
			n = 3
			b = n-1

			box = []
			cir = []
			mir = []
			hole = []
			plate1 = Part.makeBox(l,w,t,Vector(0,-w,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(w/2, [plate1.Edges[0],plate1.Edges[4]])
			box1 = Part.makeBox(d,5,t,Vector(6-d/2,-10,0))
			box2 = Part.makeBox(d,5,t,Vector(6+l-12.0-d/2,-10,0))
			cir1 = Part.makeCylinder(d/2,t,Vector(6,-10,0))
			mir1 = Part.makeCylinder(d/2,t,Vector(6,-5,0))
			cir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-10,0))
			mir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-5,0))
			for i in range(1,b):
				box.append(Part.makeBox(d,5,t,Vector(6+(l-12.0)/b*i-d/2,-10,0)))
				cir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-10,0)))
				mir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-5,0)))

			plate1 = plate1.cut(box1)
			plate1 = plate1.cut(box2)
			plate1 = plate1.cut(cir1)
			plate1 = plate1.cut(mir1)
			plate1 = plate1.cut(cir2)
			plate1 = plate1.cut(mir2)

			#print(len(box))
			#print(list(range(1,b)))
			#print(box[22])
			for i in box:
				plate1 = plate1.cut(i)
			for i in cir:
				plate1 = plate1.cut(i)
			for i in mir:
				plate1 = plate1.cut(i)

			plate2 = Part.makeBox(l,t,h-t,Vector(0,-t,t))
			plate2 = plate2.makeFillet(h/2, [plate2.Edges[1],plate2.Edges[5]])
			hole1 = Part.makeCylinder(d/2,t,Vector(6,-t,7),Vector(0,1,0))
			hole2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-t,7),Vector(0,1,0))
			for i in range(1,b):
				hole.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-t,7),Vector(0,1,0)))

			plate2 = plate2.cut(hole1)
			plate2 = plate2.cut(hole2)
			for i in hole:
				plate2 = plate2.cut(i)

			plate1 = plate1.fuse(plate2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '12':
			doc=App.newDocument()

			x=23.5
			y=12.78
			t=0.77
			f=6.35

			plate=Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate=plate.makeFillet(f, [plate.Edges[0],plate.Edges[2],plate.Edges[4],plate.Edges[6]])

			cir1 = Part.makeCylinder(2.11,t,Vector(4.41,-6.31,0))
			cir2 = Part.makeCylinder(2.11,t,Vector(8.74,-6.31,0))
			cir3 = Part.makeCylinder(2.11,t,Vector(18.64,-6.31,0))
			box = Part.makeBox(4.22,4.22,t,Vector(4.465,-8.42,0))

			plate = plate.cut(cir1)
			plate = plate.cut(cir2)
			plate = plate.cut(cir3)
			plate = plate.cut(box)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '13':

			doc=App.newDocument()

			x=15
			z=12.7
			y=12.5
			r=4.22
			t=0.77

			plate1=Part.makeBox(x,t,z,Vector(0,-t,0),Vector(0,0,1))
			plate2=Part.makeBox(t,y-t,z,Vector(x-t,0,0),Vector(0,0,1))
			plate3=Part.makeBox(t,y-t,z,Vector(0,0,0),Vector(0,0,1))

			plate1=plate1.makeFillet(0.75,[plate1.Edges[0],plate1.Edges[4]])
			plate2=plate2.makeFillet(3,[plate2.Edges[10],plate2.Edges[11]])
			plate3=plate3.makeFillet(3,[plate3.Edges[10],plate3.Edges[11]])


			cir1 = Part.makeCylinder(2.11,t,Vector(x/2,-t,z/2),Vector(0,1,0))
			plate1=plate1.cut(cir1)
			cir3 = Part.makeCylinder(2.11,t,Vector(0,8.11,6.35),Vector(1,0,0))
			plate3 = plate3.cut(cir3)
			cir2 = Part.makeCylinder(2.11,t,Vector(x-t,8.11,6.35),Vector(1,0,0))
			plate2 = plate2.cut(cir2)
			plate1= plate1.fuse(plate2)
			plate1= plate1.fuse(plate3)
			#Part.show(plate1)


			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '14':
			doc=App.newDocument()

			x=15
			z=12.7
			y=24.7
			r=4.22
			t=0.77

			plate1=Part.makeBox(x,t,z,Vector(0,-t,0),Vector(0,0,1))
			plate2=Part.makeBox(t,y-t,z,Vector(x-t,0,0),Vector(0,0,1))
			plate3=Part.makeBox(t,y-t,z,Vector(0,0,0),Vector(0,0,1))

			plate1=plate1.makeFillet(0.75,[plate1.Edges[0],plate1.Edges[4]])
			plate2=plate2.makeFillet(6.34,[plate2.Edges[10],plate2.Edges[11]])
			plate3=plate3.makeFillet(6.34,[plate3.Edges[10],plate3.Edges[11]])


			cir1 = Part.makeCylinder(2.11,t,Vector(x/2,-t,z/2),Vector(0,1,0))
			plate1=plate1.cut(cir1)
			cir3 = Part.makeCylinder(2.11,t,Vector(0,6.41,6.35),Vector(1,0,0))
			plate3 = plate3.cut(cir3)
			cir2 = Part.makeCylinder(2.11,t,Vector(x-t,6.41,6.35),Vector(1,0,0))
			plate2 = plate2.cut(cir2)
			cir4 = Part.makeCylinder(2.11,t,Vector(0,+8.45+2.11+6.41,6.35),Vector(1,0,0))
			plate3 = plate3.cut(cir4)
			cir5 = Part.makeCylinder(2.11,t,Vector(x-t,+8.45+2.11+6.41,6.35),Vector(1,0,0))
			plate2 = plate2.cut(cir5)
			plate1= plate1.fuse(plate2)
			plate1= plate1.fuse(plate3)
			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

		elif self.numericInput0.text() == '15':

			doc=App.newDocument()
			x=13.5
			z=12.7
			y=11
			r=4.18
			t=0.75

			plate1=Part.makeBox(x,t,z,Vector(0,-t,0),Vector(0,0,1))
			plate2=Part.makeBox(t,y-t,z,Vector(0,0,0),Vector(0,0,1))

			plate1=plate1.makeFillet(6.34,[plate1.Edges[5],plate1.Edges[7]])
			plate2=plate2.makeFillet(6.34,[plate2.Edges[10],plate2.Edges[11]])

			cir1 = Part.makeCylinder(2.09,t,Vector(4.8,-t,6.385),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			cir1 = Part.makeCylinder(2.09,t,Vector(9.12,-t,6.385),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			box = Part.makeBox(4.18,4.18,4.18,Vector(6.96-2.09,-t,6.385-2.09),Vector(0,1,0))
			plate1 = plate1.cut(box)
			cir2 = Part.makeCylinder(2.09,t,Vector(0,6.075,6.385),Vector(1,0,0))
			plate2 = plate2.cut(cir2)

			plate1= plate1.fuse(plate2)
			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '16':

			doc=App.newDocument()
			x=26.4
			z=13
			y=12.3
			r=4.18
			t=0.75

			plate1=Part.makeBox(x,t,z,Vector(0,-t,0),Vector(0,0,1))
			plate2=Part.makeBox(t,y-t,z,Vector(0,0,0),Vector(0,0,1))

			plate1=plate1.makeFillet(6.49,[plate1.Edges[5],plate1.Edges[7]])
			plate2=plate2.makeFillet(6.49,[plate2.Edges[10],plate2.Edges[11]])

			cir1 = Part.makeCylinder(2.09,t,Vector(x-8.61,-t,6.5),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			cir1 = Part.makeCylinder(2.09,t,Vector(x-4.29,-t,6.5),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			box = Part.makeBox(4.18,4.18,4.18,Vector(x-8.61,-t,6.5-2.09),Vector(0,1,0))
			plate1 = plate1.cut(box)
			cir1 = Part.makeCylinder(2.09,t,Vector(7.19,-t,6.5),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			cir2 = Part.makeCylinder(2.09,t,Vector(0,y-6.05,6.5),Vector(1,0,0))
			plate2 = plate2.cut(cir2)

			plate1= plate1.fuse(plate2)
			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '16a':
			doc=App.newDocument()
			x=26.3
			z=25.5
			y=12.18
			r=4
			t=0.7

			plate1=Part.makeBox(x,t,z,Vector(0,-t,0),Vector(0,0,1))
			plate2=Part.makeBox(t,y-t,z,Vector(0,0,0),Vector(0,0,1))

			plate1=plate1.makeFillet(6.4,[plate1.Edges[5],plate1.Edges[7]])
			plate2=plate2.makeFillet(6.4,[plate2.Edges[10],plate2.Edges[11]])

			cir1 = Part.makeCylinder(2,t,Vector(x-6.25,-t,6.38),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			cir1 = Part.makeCylinder(2,t,Vector(7.25,-t,6.38),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			cir1 = Part.makeCylinder(2,t,Vector(x-6.25,-t,z-6.38),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			cir1 = Part.makeCylinder(2,t,Vector(7.25,-t,z-6.38),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			cir2 = Part.makeCylinder(2,t,Vector(0,y-6.05,6.38),Vector(1,0,0))
			plate2 = plate2.cut(cir2)
			cir2 = Part.makeCylinder(2,t,Vector(0,y-6.05,z-6.38),Vector(1,0,0))
			plate2 = plate2.cut(cir2)
			plate1= plate1.fuse(plate2)
			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '17':

			doc=App.newDocument()
			x=13.5
			z=12.45
			y=10.75
			r=4.18
			t=0.75

			plate1=Part.makeBox(x,t,z,Vector(0,0,0),Vector(0,0,1))
			plate2=Part.makeBox(t,z,y,Vector(0,0,z),Vector(-1,1,0))

			plate1=plate1.makeFillet(6.22,[plate1.Edges[5],plate1.Edges[7]])
			plate2=plate2.makeFillet(6.22,[plate2.Edges[9],plate2.Edges[11]])

			cir1 = Part.makeCylinder(2.09,t,Vector(4.69,0,6.385),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			cir1 = Part.makeCylinder(2.09,t,Vector(x-4.47,0,6.385),Vector(0,1,0))
			plate1 = plate1.cut(cir1)
			box = Part.makeBox(4.18,4.18,4.18,Vector(6.96-2.09,-t,6.385-2.09),Vector(0,1,0))
			plate1 = plate1.cut(box)
			cir2 = Part.makeCylinder(2.09,10,Vector(-4,6.225,6.225),Vector(-1,-1,0))
			plate2 = plate2.cut(cir2)

			plate1= plate1.fuse(plate2)
			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '18':
			doc=App.newDocument()

			r = 4
			l = 294

			v1=Base.Vector(0,r/2,0)
			v2=Base.Vector(-r/2,0,0)
			v3=Base.Vector(0,-r/2,0)
			v4=Base.Vector(r/2,0,0)

			C1=Part.Arc(v1,v2,v3)
			C2=Part.Arc(v3,v4,v1)

			S1=Part.Shape([C1,C2])

			W=Part.Wire(S1.Edges)
			face=Part.Face(W)
			P=face.extrude(Base.Vector(0,0,l))

			shape=doc.addObject("Part::Feature")
			shape.Shape=P
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '19':
			doc=App.newDocument()

			r = 4
			l = 140

			v1=Base.Vector(0,r/2,0)
			v2=Base.Vector(-r/2,0,0)
			v3=Base.Vector(0,-r/2,0)
			v4=Base.Vector(r/2,0,0)

			C1=Part.Arc(v1,v2,v3)
			C2=Part.Arc(v3,v4,v1)

			S1=Part.Shape([C1,C2])

			W=Part.Wire(S1.Edges)
			face=Part.Face(W)
			P=face.extrude(Base.Vector(0,0,l))

			shape=doc.addObject("Part::Feature")
			shape.Shape=P
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '20':
			doc=App.newDocument()

			r = 4
			l = 102

			v1=Base.Vector(0,r/2,0)
			v2=Base.Vector(-r/2,0,0)
			v3=Base.Vector(0,-r/2,0)
			v4=Base.Vector(r/2,0,0)

			C1=Part.Arc(v1,v2,v3)
			C2=Part.Arc(v3,v4,v1)

			S1=Part.Shape([C1,C2])

			W=Part.Wire(S1.Edges)
			face=Part.Face(W)
			P=face.extrude(Base.Vector(0,0,l))

			shape=doc.addObject("Part::Feature")
			shape.Shape=P
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '21':
			doc=App.newDocument()

			r = 4
			l = 90

			v1=Base.Vector(0,r/2,0)
			v2=Base.Vector(-r/2,0,0)
			v3=Base.Vector(0,-r/2,0)
			v4=Base.Vector(r/2,0,0)

			C1=Part.Arc(v1,v2,v3)
			C2=Part.Arc(v3,v4,v1)

			S1=Part.Shape([C1,C2])

			W=Part.Wire(S1.Edges)
			face=Part.Face(W)
			P=face.extrude(Base.Vector(0,0,l))

			shape=doc.addObject("Part::Feature")
			shape.Shape=P
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '22':
			doc=App.newDocument()

			r = 4
			l = 65

			v1=Base.Vector(0,r/2,0)
			v2=Base.Vector(-r/2,0,0)
			v3=Base.Vector(0,-r/2,0)
			v4=Base.Vector(r/2,0,0)

			C1=Part.Arc(v1,v2,v3)
			C2=Part.Arc(v3,v4,v1)

			S1=Part.Shape([C1,C2])

			W=Part.Wire(S1.Edges)
			face=Part.Face(W)
			P=face.extrude(Base.Vector(0,0,l))

			shape=doc.addObject("Part::Feature")
			shape.Shape=P
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '23':
			doc=App.newDocument()

			r = 4
			l = 75

			v1=Base.Vector(0,r/2,0)
			v2=Base.Vector(-r/2,0,0)
			v3=Base.Vector(0,-r/2,0)
			v4=Base.Vector(r/2,0,0)

			C1=Part.Arc(v1,v2,v3)
			C2=Part.Arc(v3,v4,v1)

			S1=Part.Shape([C1,C2])

			W=Part.Wire(S1.Edges)
			face=Part.Face(W)
			P=face.extrude(Base.Vector(0,0,l))

			shape=doc.addObject("Part::Feature")
			shape.Shape=P
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '24':
			doc=App.newDocument()

			r = 4
			l = 51

			v1=Base.Vector(0,r/2,0)
			v2=Base.Vector(-r/2,0,0)
			v3=Base.Vector(0,-r/2,0)
			v4=Base.Vector(r/2,0,0)

			C1=Part.Arc(v1,v2,v3)
			C2=Part.Arc(v3,v4,v1)

			S1=Part.Shape([C1,C2])

			W=Part.Wire(S1.Edges)
			face=Part.Face(W)
			P=face.extrude(Base.Vector(0,0,l))

			shape=doc.addObject("Part::Feature")
			shape.Shape=P
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '25':
			doc=App.newDocument()

			r = 4
			l = 40

			v1=Base.Vector(0,r/2,0)
			v2=Base.Vector(-r/2,0,0)
			v3=Base.Vector(0,-r/2,0)
			v4=Base.Vector(r/2,0,0)

			C1=Part.Arc(v1,v2,v3)
			C2=Part.Arc(v3,v4,v1)

			S1=Part.Shape([C1,C2])

			W=Part.Wire(S1.Edges)
			face=Part.Face(W)
			P=face.extrude(Base.Vector(0,0,l))

			shape=doc.addObject("Part::Feature")
			shape.Shape=P
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '26':
			doc=App.newDocument()

			R1 = 37.75
			R2 = 2.0
			H_f1 = 3.3
			H_f2 = 1.0

			base1 = Part.makeCylinder(R1,H_f1*2,Vector(0,-H_f1,0),Vector(0,1,0),360)

			tri = Part.makePolygon([(R1-(H_f1-H_f2)*sqrt(3),0,0),(R1,-H_f1+H_f2,0),(R1,H_f1-H_f2,0),(R1-(H_f1-H_f2)*sqrt(3),0,0)])
			face = Part.Face(tri)
			angle = 360
			solid = face.revolve(Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.cut(solid)

			base3 = Part.makeCylinder(33.0,H_f2,Vector(0,H_f1-H_f2,0),Vector(0,1,0),360)
			base1 = base1.cut(base3)
			base5 = Part.makeCylinder(33.0,H_f2,Vector(0,-H_f1+H_f2,0),Vector(0,-1,0),360)
			base1 = base1.cut(base5)

			base7 = Part.makeCylinder(4.75,10.9+3,Vector(0,-3,0),Vector(0,1,0),360)
			base1 = base1.fuse(base7)

			base2 = Part.makeCylinder(R2,50,Vector(0,-25,0),Vector(0,1,0),360)
			base1 = base1.cut(base2)
			outC=Part.makeCylinder(3.29/2,50,Vector(-25.0,8.0,0),Vector(1,0,0))
			base1=base1.cut(outC)

			cir1 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			base1 = base1.cut(cir1)
			cir2 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir2.rotate(Vector(0,0,0),Vector(0,1,0),45)
			base1 = base1.cut(cir2)
			cir3 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir3.rotate(Vector(0,0,0),Vector(0,1,0),90)
			base1 = base1.cut(cir3)
			cir4 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir4.rotate(Vector(0,0,0),Vector(0,1,0),135)
			base1 = base1.cut(cir4)
			cir5 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir5.rotate(Vector(0,0,0),Vector(0,1,0),180)
			base1 = base1.cut(cir5)
			cir6 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir6.rotate(Vector(0,0,0),Vector(0,1,0),225)
			base1 = base1.cut(cir6)
			cir7 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir7.rotate(Vector(0,0,0),Vector(0,1,0),270)
			base1 = base1.cut(cir7)
			cir8 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir8.rotate(Vector(0,0,0),Vector(0,1,0),315)
			base1 = base1.cut(cir8)

			acir1 = Part.makeCylinder(2.1,50,Vector(24.0,-25.0,0),Vector(0,1,0))
			base1 = base1.cut(acir1)
			acir2 = Part.makeCylinder(2.1,50,Vector(24.0,-25.0,0),Vector(0,1,0))
			acir2.rotate(Vector(0,0,0),Vector(0,1,0),45)
			base1 = base1.cut(acir2)
			acir3 = Part.makeCylinder(2.1,50,Vector(24.0,-25.0,0),Vector(0,1,0))
			acir3.rotate(Vector(0,0,0),Vector(0,1,0),90)
			base1 = base1.cut(acir3)
			acir4 = Part.makeCylinder(2.1,50,Vector(24.0,-25.0,0),Vector(0,1,0))
			acir4.rotate(Vector(0,0,0),Vector(0,1,0),135)
			base1 = base1.cut(acir4)
			acir5 = Part.makeCylinder(2.1,50,Vector(24.0,-25.0,0),Vector(0,1,0))
			acir5.rotate(Vector(0,0,0),Vector(0,1,0),180)
			base1 = base1.cut(acir5)
			acir6 = Part.makeCylinder(2.1,50,Vector(24.0,-25.0,0),Vector(0,1,0))
			acir6.rotate(Vector(0,0,0),Vector(0,1,0),225)
			base1 = base1.cut(acir6)
			acir7 = Part.makeCylinder(2.1,50,Vector(24.0,-25.0,0),Vector(0,1,0))
			acir7.rotate(Vector(0,0,0),Vector(0,1,0),270)
			base1 = base1.cut(acir7)
			acir8 = Part.makeCylinder(2.1,50,Vector(24.0,-25.0,0),Vector(0,1,0))
			acir8.rotate(Vector(0,0,0),Vector(0,1,0),315)
			base1 = base1.cut(acir8)

			box1 = Part.makeBox(4.2,12,50,Vector(12.0,-25.0,-2.1),Vector(0,1,0))
			base1 = base1.cut(box1)
			box2 = Part.makeBox(4.2,12,50,Vector(12.0,-25.0,-2.1),Vector(0,1,0))
			box2.rotate(Vector(0,0,0),Vector(0,1,0),90)
			base1 = base1.cut(box2)
			box3 = Part.makeBox(4.2,12,50,Vector(12.0,-25.0,-2.1),Vector(0,1,0))
			box3.rotate(Vector(0,0,0),Vector(0,1,0),180)
			base1 = base1.cut(box3)
			box4 = Part.makeBox(4.2,12,50,Vector(12.0,-25.0,-2.1),Vector(0,1,0))
			box4.rotate(Vector(0,0,0),Vector(0,1,0),270)
			base1 = base1.cut(box4)

			#Part.show(base1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=base1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '27':
			doc=App.newDocument()

			R1 = 18.9
			R2 = 2.0
			H_f1 = 3.0
			H_f2 = 1.25

			base1 = Part.makeCylinder(R1,H_f1*2,Vector(0,-H_f1,0),Vector(0,1,0),360)

			tri = Part.makePolygon([(R1-(H_f1-H_f2)*sqrt(3),0,0),(R1,-H_f1+H_f2,0),(R1,H_f1-H_f2,0),(R1-(H_f1-H_f2)*sqrt(3),0,0)])
			face = Part.Face(tri)
			angle = 360
			solid = face.revolve(Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.cut(solid)

			base7 = Part.makeCylinder(4.75,10.9,Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.fuse(base7)

			base2 = Part.makeCylinder(R2,50,Vector(0,-25,0),Vector(0,1,0),360)
			base1 = base1.cut(base2)

			outC=Part.makeCylinder(3.29/2,50,Vector(-25.0,8.0,0),Vector(1,0,0))
			base1=base1.cut(outC)

			cir1 = Part.makeCylinder(3.0,50,Vector(12,-2.0,0),Vector(0,1,0))
			base1 = base1.cut(cir1)
			cir2 = Part.makeCylinder(3.0,50,Vector(12,-2.0,0),Vector(0,1,0))
			cir2.rotate(Vector(0,0,0),Vector(0,1,0),45)
			base1 = base1.cut(cir2)
			cir3 = Part.makeCylinder(3.0,50,Vector(12,-2.0,0),Vector(0,1,0))
			cir3.rotate(Vector(0,0,0),Vector(0,1,0),90)
			base1 = base1.cut(cir3)
			cir4 = Part.makeCylinder(3.0,50,Vector(12,-2.0,0),Vector(0,1,0))
			cir4.rotate(Vector(0,0,0),Vector(0,1,0),135)
			base1 = base1.cut(cir4)
			cir5 = Part.makeCylinder(3.0,50,Vector(12,-2.0,0),Vector(0,1,0))
			cir5.rotate(Vector(0,0,0),Vector(0,1,0),180)
			base1 = base1.cut(cir5)
			cir6 = Part.makeCylinder(3.0,50,Vector(12,-2.0,0),Vector(0,1,0))
			cir6.rotate(Vector(0,0,0),Vector(0,1,0),225)
			base1 = base1.cut(cir6)
			cir7 = Part.makeCylinder(3.0,50,Vector(12,-2.0,0),Vector(0,1,0))
			cir7.rotate(Vector(0,0,0),Vector(0,1,0),270)
			base1 = base1.cut(cir7)
			cir8 = Part.makeCylinder(3.0,50,Vector(12,-2.0,0),Vector(0,1,0))
			cir8.rotate(Vector(0,0,0),Vector(0,1,0),315)
			base1 = base1.cut(cir8)

			acir1 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			base1 = base1.cut(acir1)
			acir2 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir2.rotate(Vector(0,0,0),Vector(0,1,0),45)
			base1 = base1.cut(acir2)
			acir3 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir3.rotate(Vector(0,0,0),Vector(0,1,0),90)
			base1 = base1.cut(acir3)
			acir4 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir4.rotate(Vector(0,0,0),Vector(0,1,0),135)
			base1 = base1.cut(acir4)
			acir5 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir5.rotate(Vector(0,0,0),Vector(0,1,0),180)
			base1 = base1.cut(acir5)
			acir6 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir6.rotate(Vector(0,0,0),Vector(0,1,0),225)
			base1 = base1.cut(acir6)
			acir7 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir7.rotate(Vector(0,0,0),Vector(0,1,0),270)
			base1 = base1.cut(acir7)
			acir8 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir8.rotate(Vector(0,0,0),Vector(0,1,0),315)
			base1 = base1.cut(acir8)

			#Part.show(base1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=base1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '28':
			doc=App.newDocument()

			R1 = 12.7
			R2 = 2.0
			H_f1 = 2.2
			H_f2 = 0.8

			base1 = Part.makeCylinder(R1,H_f1*2,Vector(0,-H_f1,0),Vector(0,1,0),360)

			tri = Part.makePolygon([(R1-(H_f1-H_f2)*sqrt(3),0,0),(R1,-H_f1+H_f2,0),(R1,H_f1-H_f2,0),(R1-(H_f1-H_f2)*sqrt(3),0,0)])
			face = Part.Face(tri)
			angle = 360
			solid = face.revolve(Vector(0,0,0),Vector(0,1,0),360)

			base1 = base1.cut(solid)

			base3 = Part.makeCylinder(10.0,H_f2,Vector(0,H_f1-H_f2,0),Vector(0,1,0),360)
			base4 = Part.makeCylinder(5.9,H_f2,Vector(0,H_f1-H_f2,0),Vector(0,1,0),360)
			base3 = base3.cut(base4)
			base1 = base1.cut(base3)

			base5 = Part.makeCylinder(10.0,H_f2,Vector(0,-H_f1+H_f2,0),Vector(0,-1,0),360)
			base6 = Part.makeCylinder(5.9,H_f2,Vector(0,-H_f1+H_f2,0),Vector(0,-1,0),360)
			base5 = base5.cut(base6)
			base1 = base1.cut(base5)

			base7 = Part.makeCylinder(4.75,10.9,Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.fuse(base7)
			base8 = Part.makeCylinder(5.9,3.1,Vector(0,0,0),Vector(0,-1,0),360)
			base1 = base1.fuse(base8)

			base2 = Part.makeCylinder(R2,50,Vector(0,-25,0),Vector(0,1,0),360)
			base1 = base1.cut(base2)

			outC=Part.makeCylinder(3.29/2,50,Vector(-25.0,7.5,0),Vector(1,0,0))
			base1=base1.cut(outC)

			#Part.show(base1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=base1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '29':
			doc=App.newDocument()

			R1 = 7.7
			R2 = 2.1
			H_f1 = 2.45
			H_f2 = 0.8

			base1 = Part.makeCylinder(R1,H_f1*2,Vector(0,-H_f1,0),Vector(0,1,0),360)
			base2 = Part.makeCylinder(R2,H_f1*2,Vector(0,-H_f1,0),Vector(0,1,0),360)

			base1 = base1.cut(base2)

			tri = Part.makePolygon([(R1-(H_f1-H_f2)*sqrt(3),0,0),(R1,-H_f1+H_f2,0),(R1,H_f1-H_f2,0),(R1-(H_f1-H_f2)*sqrt(3),0,0)])
			face = Part.Face(tri)
			angle = 360
			solid = face.revolve(Vector(0,0,0),Vector(0,1,0),360)

			base1 = base1.cut(solid)

			base3 = Part.makeCylinder(6.3,H_f2,Vector(0,H_f1-H_f2,0),Vector(0,1,0),360)
			base4 = Part.makeCylinder(4,H_f2,Vector(0,H_f1-H_f2,0),Vector(0,1,0),360)
			base3 = base3.cut(base4)
			base1 = base1.cut(base3)

			base5 = Part.makeCylinder(6.3,H_f2,Vector(0,-H_f1+H_f2,0),Vector(0,-1,0),360)
			base6 = Part.makeCylinder(4,H_f2,Vector(0,-H_f1+H_f2,0),Vector(0,-1,0),360)
			base5 = base5.cut(base6)
			base1 = base1.cut(base5)

			#Part.show(base1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=base1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '30':
			doc=App.newDocument()

			D1 = 36
			D2 = 9.43
			h = 9.11
			h1 = 0.5
			d = 4.11
			d1 = 3.33
			t = 0.7

			i = 0
			n = 2

			circle = Part.makeCylinder(D1/2,t,Vector(0,0,0))
			circle1 = Part.makeCylinder(D2/2,h,Vector(0,0,-h1))
			circle = circle.fuse(circle1)

			cir1 = Part.makeCylinder(d1/2,D2,Vector(-D2/2,0,6.75-d/2),Vector(1,0,0))
			circle = circle.cut(cir1)
			cir2 = Part.makeCylinder(d/2,h,Vector(0,0,-h1))
			circle = circle.cut(cir2)

			cir3 = []
			cir4 = []
			for i in range(n):
				for j in range(n):
					cir3.append(Part.makeCylinder(d/2,t,Vector((27.7-d)/2-(27.7-d)*i,(14-d)/2-(14-d)*j,0)))

			for i in cir3:
				circle = circle.cut(i)

			for i in range(n):
				for j in range(n):
					cir4.append(Part.makeCylinder(d/2,t,Vector((14-d)/2-(14-d)*j,(27.7-d)/2-(27.7-d)*i,0)))

			for i in cir4:
				circle = circle.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '32':

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=0.736, z=19, alpha=20 * pi / 180., clearence=0, shift=0., beta=0., undercut=False, simple=False, height=5.6, backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                d = 9.48
			                d1 = 4.11
			                d2 = 3.11
			                h = 14.5
			                self.cir = Part.makeCylinder(d/2,h-5.6,Vector(0,0,5.6))
			                self.cir2 = Part.makeCylinder(d1/2,h,Vector(0,0,0))
			                self.cir3 = Part.makeCylinder(d2/2,d,Vector(0,-d/2,10.8),Vector(0,1,0))
			                self.Shape = self.Shape.fuse(self.cir)
			                self.Shape = self.Shape.cut(self.cir2)
			                self.Shape = self.Shape.cut(self.cir3)

			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])


			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '33':

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=0.65, z=57, alpha=20 * pi / 180., clearence=0.75, shift=0., beta=0., undercut=False, simple=False, height=5., backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                d = 4.11
			                self.cir = Part.makeCylinder(17,4,Vector(0,0,0))
			                self.cir2 = Part.makeCylinder(5.4,5,Vector(0,0,-1))
			                self.cir3 = Part.makeCylinder(4.7,7.6,Vector(0,0,-8.6))
			                self.cir4 = Part.makeCylinder(d/2,13.6,Vector(0,0,-8.6))
			                self.cir_1 = Part.makeCylinder(d/2,13.6,Vector(12.5,0,0))
			                self.cir_2 = Part.makeCylinder(d/2,13.6,Vector(-12.5,0,0))
			                self.cir_3 = Part.makeCylinder(d/2,13.6,Vector(0,12.5,0))
			                self.cir_4 = Part.makeCylinder(d/2,13.6,Vector(0,-12.5,0))
			                self.cir_5 = Part.makeCylinder(d/2,13.6,Vector(12.5*cos(45 * pi / 180.),12.5*sin(45 * pi / 180.),0))
			                self.cir_6 = Part.makeCylinder(d/2,13.6,Vector(-12.5*cos(45 * pi / 180.),12.5*sin(45 * pi / 180.),0))
			                self.cir_7 = Part.makeCylinder(d/2,13.6,Vector(12.5*cos(45 * pi / 180.),-12.5*sin(45 * pi / 180.),0))
			                self.cir_8 = Part.makeCylinder(d/2,13.6,Vector(-12.5*cos(45 * pi / 180.),-12.5*sin(45 * pi / 180.),0))
			                self.cir_0 = Part.makeCylinder(d/2,13.6,Vector(0,-6.8,-4.6),Vector(0,1,0))
			                self.Shape = self.Shape.cut(self.cir)
			                self.Shape = self.Shape.fuse(self.cir2)
			                self.Shape = self.Shape.fuse(self.cir3)
			                self.Shape = self.Shape.cut(self.cir4)
			                self.Shape = self.Shape.cut(self.cir_1)
			                self.Shape = self.Shape.cut(self.cir_2)
			                self.Shape = self.Shape.cut(self.cir_3)
			                self.Shape = self.Shape.cut(self.cir_4)
			                self.Shape = self.Shape.cut(self.cir_5)
			                self.Shape = self.Shape.cut(self.cir_6)
			                self.Shape = self.Shape.cut(self.cir_7)
			                self.Shape = self.Shape.cut(self.cir_8)
			                self.Shape = self.Shape.cut(self.cir_0)
			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])

			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()
		elif self.numericInput0.text() == '34':

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=0.681, z=95, alpha=20 * pi / 180., clearence=0, shift=0., beta=0., undercut=False, simple=False, height=3.27, backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                d = 12.43
			                d1 = 9.48
			                d2 = 4.11
			                d3 = 3.11
			                t = 3.27
			                h = 6.16
			                h1 = 14
			                x =8.5
			                x1 = 17.1
			                y = 16.7
			                self.cir = Part.makeCylinder(d/2,h,Vector(0,0,-1.4))
			                self.cir2 = Part.makeCylinder(d1/2,h1-1.4,Vector(0,0,1.4))
			                self.cir3 = Part.makeCylinder(d2/2,h1+1.4,Vector(0,0,-1.4))
			                self.cir4 = Part.makeCylinder(d3/2,d1,Vector(0,-d1/2,d1),Vector(0,1,0))
			                self.cir5 = Part.makeCylinder(d2/2,t,Vector(-x,x,0))
			                self.cir6 = Part.makeCylinder(d2/2,t,Vector(x,x,0))
			                self.cir7 = Part.makeCylinder(d2/2,t,Vector(x,-x,0))
			                self.cir8 = Part.makeCylinder(d2/2,t,Vector(-x,-x,0))
			                self.cir9 = Part.makeCylinder(d2/2,t,Vector(-x1,x1,0))
			                self.cir10 = Part.makeCylinder(d2/2,t,Vector(x1,x1,0))
			                self.cir11 = Part.makeCylinder(d2/2,t,Vector(x1,-x1,0))
			                self.cir12 = Part.makeCylinder(d2/2,t,Vector(-x1,-x1,0))
			                self.box = Part.makeBox(d2,y-d2,t,Vector(-d2/2,x+d2,0))
			                self.box1 = Part.makeBox(d2,y-d2,t,Vector(-d2/2,-x-d2-(y-d2),0))
			                self.box2 = Part.makeBox(y-d2,d2,t,Vector(x+d2,-d2/2,0))
			                self.box3 = Part.makeBox(y-d2,d2,t,Vector(-x-d2-(y-d2),-d2/2,0))
			                self.cir13 = Part.makeCylinder(d2/2,t,Vector(0,x+d2,0))
			                self.cir14 = Part.makeCylinder(d2/2,t,Vector(0,x+y,0))
			                self.cir15 = Part.makeCylinder(d2/2,t,Vector(0,-x-d2,0))
			                self.cir16 = Part.makeCylinder(d2/2,t,Vector(0,-x-y,0))
			                self.cir17 = Part.makeCylinder(d2/2,t,Vector(x+d2,0,0))
			                self.cir18 = Part.makeCylinder(d2/2,t,Vector(x+y,0,0))
			                self.cir19 = Part.makeCylinder(d2/2,t,Vector(-x-d2,0,0))
			                self.cir20 = Part.makeCylinder(d2/2,t,Vector(-x-y,0,0))

			                self.Shape = self.Shape.fuse(self.cir)
			                self.Shape = self.Shape.fuse(self.cir2)
			                self.Shape = self.Shape.cut(self.cir3)
			                self.Shape = self.Shape.cut(self.cir4)
			                self.Shape = self.Shape.cut(self.cir5)
			                self.Shape = self.Shape.cut(self.cir6)
			                self.Shape = self.Shape.cut(self.cir7)
			                self.Shape = self.Shape.cut(self.cir8)
			                self.Shape = self.Shape.cut(self.cir9)
			                self.Shape = self.Shape.cut(self.cir10)
			                self.Shape = self.Shape.cut(self.cir11)
			                self.Shape = self.Shape.cut(self.cir12)
			                self.Shape = self.Shape.cut(self.box)
			                self.Shape = self.Shape.cut(self.box1)
			                self.Shape = self.Shape.cut(self.box2)
			                self.Shape = self.Shape.cut(self.box3)
			                self.Shape = self.Shape.cut(self.cir13)
			                self.Shape = self.Shape.cut(self.cir14)
			                self.Shape = self.Shape.cut(self.cir15)
			                self.Shape = self.Shape.cut(self.cir16)
			                self.Shape = self.Shape.cut(self.cir17)
			                self.Shape = self.Shape.cut(self.cir18)
			                self.Shape = self.Shape.cut(self.cir19)
			                self.Shape = self.Shape.cut(self.cir20)
			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])


			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '35':
			doc=App.newDocument()

			plate1 = Part.makeCylinder(10.0,3.0,Vector(0,0,-1.5),Vector(0,0,1),360)
			plate2 = Part.makeCylinder(4.75,12.5,Vector(0,0,0),Vector(0,0,1),360)

			plate1 = plate1.fuse(plate2)

			inC = Part.makeCylinder(2.0,50,Vector(0,0,-25),Vector(0,0,1))
			plate1 = plate1.cut(inC)

			outC=Part.makeCylinder(3.29/2,50,Vector(0,-25.0,9.5),Vector(0,1,0))
			plate1=plate1.cut(outC)

			teeth = Part.makePolygon([(9,0,1.5),(10,0,3.3),(14,0,3.3),(14,0,1.5),(10,0,0),(9,0,1.5)])
			face = Part.Face(teeth)
			ee1 = face.extrude(Vector(0,1,0))

			ee2 = ee1.mirror(Vector(0,0,0),Vector(0,1,0))
			ee1 = ee1.fuse(ee2)

			ee3 = ee1.mirror(Vector(0,0,0),Vector(0,0,1))
			ee1 = ee1.fuse(ee3)

			plate1 = plate1.fuse(ee1)

			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)
			ee1.rotate(Vector(0,0,0),Vector(0,0,1),25.7)
			plate1 = plate1.fuse(ee1)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '36':
			doc=App.newDocument()

			R1 = 18
			R2 = 2.0

			base1 = Part.makeCylinder(R1,5.3,Vector(0,0,0),Vector(0,-1,0),360)

			base2 = Part.makeCylinder(4.75,9.5,Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.fuse(base2)

			outC = Part.makeCylinder(3.29/2,50,Vector(-25.0,7.0,0),Vector(1,0,0))
			base1 = base1.cut(outC)

			base3 = Part.makeCylinder(6.3,2.0,Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.fuse(base3)

			base4 = Part.makeCylinder(16.0,10.0,Vector(0,-2.0,0),Vector(0,-1,0),360)
			base1 = base1.cut(base4)

			base5 = Part.makeCylinder(6.3,1.0,Vector(0,-2.0,0),Vector(0,-1,0),360)
			base1 = base1.fuse(base5)

			acir1 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			base1 = base1.cut(acir1)
			acir2 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir2.rotate(Vector(0,0,0),Vector(0,1,0),45)
			base1 = base1.cut(acir2)
			acir3 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir3.rotate(Vector(0,0,0),Vector(0,1,0),90)
			base1 = base1.cut(acir3)
			acir4 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir4.rotate(Vector(0,0,0),Vector(0,1,0),135)
			base1 = base1.cut(acir4)
			acir5 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir5.rotate(Vector(0,0,0),Vector(0,1,0),180)
			base1 = base1.cut(acir5)
			acir6 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir6.rotate(Vector(0,0,0),Vector(0,1,0),225)
			base1 = base1.cut(acir6)
			acir7 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir7.rotate(Vector(0,0,0),Vector(0,1,0),270)
			base1 = base1.cut(acir7)
			acir8 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			acir8.rotate(Vector(0,0,0),Vector(0,1,0),315)
			base1 = base1.cut(acir8)

			inC = Part.makeCylinder(R2,50,Vector(0,-25,0),Vector(0,1,0),360)
			base1 = base1.cut(inC)

			extend1 = Part.makePolygon([(18.0,-5.3+1.3,0),(18.0,-5.3,0.75),(18.0,-5.3,-0.75),(18.0,-5.3+1.3,0)])
			fa2 = Part.Face(extend1)
			p2 = fa2.extrude(Vector(-50,0,0))
			base1 = base1.cut(p2)

			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)
			p2.rotate(Vector(0,0,0),Vector(0,1,0),7.2)
			base1 = base1.cut(p2)

			#Part.show(base1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=base1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '37':
			doc=App.newDocument()

			# 기본형상
			cir_hex=9.5 #circle_diameter

			d=26.2
			exHex=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,-2.7))
			inC=Part.makeCylinder(4.17/2,d,Vector(0,0,-2.7))
			exHex=exHex.cut(inC)

			# 나사선 helix
			helix = Part.makeHelix(2,15,2) #75넣으면 메모리 문제로 실행 안될 수 있음.            #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((6.95,0,-0.125),(6.95,0,0.125))
			edge2 = Part.makeLine((6.95,0,0.125), (4.45,0,0.419))
			edge3 = Part.makeLine((4.45,0,0.419), (4.45,0,-0.419))
			edge4 = Part.makeLine((4.45,0,-0.419),(6.95,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.fuse(pipe)

			outC=Part.makeCylinder(3.29/2,20,Vector(0,-10,26.2-3.6-2.7),Vector(0,1,0))
			exHex=exHex.cut(outC)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)
		elif self.numericInput0.text() == '39':
			doc=App.newDocument()

			D = 6.35
			d = 3.59
			x = 6.44
			y = 5.27
			t = 1.34
			l = 2.86
			h = 9
			circle = Part.makeCylinder(D/2,y,Vector(0,0,0),Vector(0,1,0))
			circle1 = Part.makeCylinder(d/2,y,Vector(0,0,0),Vector(0,1,0))
			box = Part.makeBox(l,y,D/2,Vector(-D/2,y,-l/2),Vector(1,0,0))
			box1 = Part.makeBox(l,y,t,Vector(-1.108-0.65,0,-1.43+1.158),Vector(1,0,-1.732))
			box2 = Part.makeBox(l,y,t,Vector(-1.108,0,1.43),Vector(-1,0,-1.732))
			plate1 = Part.makeBox(x,y,t,Vector(-1.084,0,-1.43),Vector(1,0,-1.732))
			plate2 = Part.makeBox(x,y,t,Vector(-1.084+0.65,0,1.43+1.158),Vector(-1,0,-1.732))
			plate1 = plate1.makeFillet(y/2-0.001,[plate1.Edges[4],plate1.Edges[6]])
			plate2 = plate2.makeFillet(y/2-0.001,[plate2.Edges[4],plate2.Edges[6]])

			#circle1 = Part.makeCylinder(d3/2,h1,Vector(0,0,(t-h1)/2))
			circle = circle.cut(circle1)
			circle = circle.cut(box)
			circle = circle.cut(box1)
			circle = circle.cut(box2)
			circle = circle.fuse(plate1)
			circle = circle.fuse(plate2)
			#Part.show(circle)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '41':
			doc=App.newDocument()

			# 기본형상 hexagon, circle
			s_hex=5.6 #hexagon_diameter
			cir_hex=4 #circle_diameter
			k_hex=2.1 #height

			mhex=Base.Matrix()
			mhex.rotateZ(math.radians(60.0))
			polygon = []
			vhex=Base.Vector(s_hex/math.sqrt(3.0),0.0,-k_hex)
			for i in range(6):
				polygon.append(vhex)
				vhex = mhex.multiply(vhex)
			polygon.append(vhex)
			hexagon = Part.makePolygon(polygon)
			face=Part.Face(hexagon)
			exHex=face.extrude(Base.Vector(0.0,0.0,k_hex)) #높이

			d=6
			circ=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))
			exHex=exHex.fuse(circ)

			# 나사선 helix
			helix = Part.makeHelix(0.797,15,2)             #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((1.7,0,-0.125), (1.7,0,0.125))
			edge2 = Part.makeLine((1.7,0,0.125), (2.3,0,0.419))
			edge3 = Part.makeLine((2.3,0,0.419), (2.3,0,-0.419))
			edge4 = Part.makeLine((2.3,0,-0.419), (1.7,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)
		elif self.numericInput0.text() == '42':
			doc=App.newDocument()

			# 기본형상 hexagon, circle
			s_hex=7.9 #hexagon_diameter
			cir_hex=4 #circle_diameter
			k_hex=2.1 #height

			mhex=Base.Matrix()
			mhex.rotateZ(math.radians(60.0))
			polygon = []
			vhex=Base.Vector(s_hex/math.sqrt(3.0),0.0,0.0)
			for i in range(6):
				polygon.append(vhex)
				vhex = mhex.multiply(vhex)
			polygon.append(vhex)
			hexagon = Part.makePolygon(polygon)
			circ=Part.makeCircle(cir_hex/2.0)
			face=Part.Face([hexagon, Part.Wire(circ)]) #hexagon, Part.wire(circ) 순서에 따라 형상이 바뀜
			exHex=face.extrude(Base.Vector(0.0,0.0,k_hex)) #높이

			# 나사선 helix
			helix = Part.makeHelix(0.797,3,2)             #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((2.3,0,-0.125), (2.3,0,0.125))
			edge2 = Part.makeLine((2.3,0,0.125), (1.7,0,0.419))
			edge3 = Part.makeLine((1.7,0,0.419), (1.7,0,-0.419))
			edge4 = Part.makeLine((1.7,0,-0.419), (2.3,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)
		elif self.numericInput0.text() == '43':
			doc=App.newDocument()

			D = 9.2
			d = 4.25
			t = 1.2

			plate1 = Part.makeCylinder(D/2,t,Vector(0,0,0))
			plate2 = Part.makeCylinder(d/2,t,Vector(0,0,0))
			plate1 = plate1.cut(plate2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

		elif self.numericInput0.text() == '44':
			doc=App.newDocument()

			D = 18.5
			d = 4.25
			t = 0.7

			plate1 = Part.makeCylinder(D/2,t,Vector(0,0,0))
			plate2 = Part.makeCylinder(d/2,t,Vector(0,0,0))
			plate1 = plate1.cut(plate2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '46':
			doc=App.newDocument()

			x = 36.4
			x1 = 15
			y = 12.7
			h = 13.8
			t = 0.85
			d = 4.11
			i = 0
			n = 3

			plate1 = Part.makeBox(x,y,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(y/2-0.001, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])
			plate2 = Part.makeBox(x1,y,t,Vector((x-x1)/2,0,0))
			plate3 = Part.makeBox(t,y,h,Vector((x-x1)/2,0,0),Vector(0,0,1))
			plate4 = Part.makeBox(t,y,h,Vector(x-(x-x1)/2-t,0,0),Vector(0,0,1))
			plate1 = plate1.cut(plate2)
			plate1 = plate1.fuse(plate3)
			plate1 = plate1.fuse(plate4)

			plate5 = Part.makeBox(x1,y,t,Vector((x-x1)/2,0,h),Vector(0,0,1))
			plate1 = plate1.fuse(plate5)

			cir = []
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,h+t,Vector((x-y)/(n-1)*i+y/2,y/2,0)))
			for i in cir:
				plate1 = plate1.cut(i)\

			cir1 = Part.makeCylinder(d/2,x1,Vector((x-x1)/2,y/2,h/2),Vector(1,0,0))
			plate1 = plate1.cut(cir1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '47':
			doc=App.newDocument()

			x = 37.4
			y = 12.7
			z = 14.3
			t = 0.7
			d = 4.2
			n = 3
			m = 1
			r = 6.34
			i = 0
			j = 0
			a=12.5
			f=(x-a*(n-1))/2

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate2 = Part.makeBox(t,y,z,Vector(0,-y,0),Vector(0,0,1))
			plate3 = Part.makeBox(t,y,z,Vector(x-t,-y,0),Vector(0,0,1))

			plate2 = plate2.makeFillet(r, [plate2.Edges[9],plate2.Edges[11]])
			plate3 = plate3.makeFillet(r, [plate3.Edges[9],plate3.Edges[11]])

			cir = []
			lt = []
			rt = []

			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,-y/2,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			for j in range(m):
				lt.append(Part.makeCylinder(d/2,t,Vector(0,-y/2,8),Vector(1,0,0)))
			for j in range(m):
				rt.append(Part.makeCylinder(d/2,t,Vector(x-t,-y/2,8),Vector(1,0,0)))
			for i in lt:
				plate2 = plate2.cut(i)
			for i in rt:
				plate3 = plate3.cut(i)

			plate1 = plate1.fuse(plate2)
			plate1 = plate1.fuse(plate3)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=plate1      	                           #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '48':
			doc=App.newDocument()

			x = 62.8
			y = 12.7
			z = 14.3
			t = 0.7
			d = 4.2
			n = 5
			m = 1
			r = 6.34
			i = 0
			j = 0
			a=12.5
			f=(x-a*(n-1))/2

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate2 = Part.makeBox(t,y,z,Vector(0,-y,0),Vector(0,0,1))
			plate3 = Part.makeBox(t,y,z,Vector(x-t,-y,0),Vector(0,0,1))

			plate2 = plate2.makeFillet(r, [plate2.Edges[9],plate2.Edges[11]])
			plate3 = plate3.makeFillet(r, [plate3.Edges[9],plate3.Edges[11]])

			cir = []
			lt = []
			rt = []

			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,-y/2,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			for j in range(m):
				lt.append(Part.makeCylinder(d/2,t,Vector(0,-y/2,8),Vector(1,0,0)))
			for j in range(m):
				rt.append(Part.makeCylinder(d/2,t,Vector(x-t,-y/2,8),Vector(1,0,0)))
			for i in lt:
				plate2 = plate2.cut(i)
			for i in rt:
				plate3 = plate3.cut(i)

			plate1 = plate1.fuse(plate2)
			plate1 = plate1.fuse(plate3)


			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=plate1      	                           #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '49':
			doc=App.newDocument()

			x = 88.2
			y = 12.7
			z = 14.3
			t = 0.7
			d = 4.2
			n = 7
			m = 1
			r = 6.34
			i = 0
			j = 0
			a=12.5
			f=(x-a*(n-1))/2

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate2 = Part.makeBox(t,y,z,Vector(0,-y,0),Vector(0,0,1))
			plate3 = Part.makeBox(t,y,z,Vector(x-t,-y,0),Vector(0,0,1))

			plate2 = plate2.makeFillet(r, [plate2.Edges[9],plate2.Edges[11]])
			plate3 = plate3.makeFillet(r, [plate3.Edges[9],plate3.Edges[11]])

			cir = []
			lt = []
			rt = []

			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,-y/2,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			for j in range(m):
				lt.append(Part.makeCylinder(d/2,t,Vector(0,-y/2,8),Vector(1,0,0)))
			for j in range(m):
				rt.append(Part.makeCylinder(d/2,t,Vector(x-t,-y/2,8),Vector(1,0,0)))
			for i in lt:
				plate2 = plate2.cut(i)
			for i in rt:
				plate3 = plate3.cut(i)

			plate1 = plate1.fuse(plate2)
			plate1 = plate1.fuse(plate3)


			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=plate1      	                           #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '50':

			doc=App.newDocument()
			x = 62.0
			y = 36.6
			z = 13.5
			t = 0.7
			d = 4.1
			n = 5
			m = 3
			f = 6.35
			i = 0
			j = 0
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate2 = Part.makeBox(t,y,z,Vector(0,-y,0),Vector(0,0,1))
			plate3 = Part.makeBox(t,y,z,Vector(x-t,-y,0),Vector(0,0,1))

			plate2 = plate2.makeFillet(f, [plate2.Edges[9],plate2.Edges[11]])
			plate3 = plate3.makeFillet(f, [plate3.Edges[9],plate3.Edges[11]])

			cir = []
			lt = []
			rt = []
			lt_up = []
			rt_up = []
			lt_box = []
			rt_box = []
			for j in range(m):
				for i in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-cc-a*j,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			for j in range(m):
				lt.append(Part.makeCylinder(d/2,t,Vector(0,-((y-11.0)/(m-1))*j-5.5,6),Vector(1,0,0)))
				lt_up.append(Part.makeCylinder(d/2,t,Vector(0,-((y-11.0)/(m-1))*j-5.5,8),Vector(1,0,0)))
				lt_box.append(Part.makeBox(2,d,t,Vector(0,-((y-11.0)/(m-1))*j-5.5+d/2,6),Vector(1,0,0)))
			for j in range(m):
				rt.append(Part.makeCylinder(d/2,t,Vector(x-t,-((y-11.0)/(m-1))*j-5.5,6),Vector(1,0,0)))
				rt_up.append(Part.makeCylinder(d/2,t,Vector(x-t,-((y-11.0)/(m-1))*j-5.5,8),Vector(1,0,0)))
				rt_box.append(Part.makeBox(2,d,t,Vector(x-t,-((y-11.0)/(m-1))*j-5.5+d/2,6),Vector(1,0,0)))

			for i in lt:
				plate2 = plate2.cut(i)
			for i in lt_up:
				plate2 = plate2.cut(i)
			for i in lt_box:
				plate2 = plate2.cut(i)
			for i in rt:
				plate3 = plate3.cut(i)
			for i in rt_up:
				plate3 = plate3.cut(i)
			for i in rt_box:
				plate3 = plate3.cut(i)

			plate1 = plate1.fuse(plate2)
			plate1 = plate1.fuse(plate3)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 1.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '51':
			doc=App.newDocument()

			x = 90.2
			y = 60
			z = 13.5
			t = 0.7
			d = 4.2
			n = 7
			m = 5
			f = 6.35
			i = 0
			j = 0
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate2 = Part.makeBox(t,y,z,Vector(0,-y,0),Vector(0,0,1))
			plate3 = Part.makeBox(t,y,z,Vector(x-t,-y,0),Vector(0,0,1))

			plate2 = plate2.makeFillet(f, [plate2.Edges[9],plate2.Edges[11]])
			plate3 = plate3.makeFillet(f, [plate3.Edges[9],plate3.Edges[11]])

			cir = []
			lt = []
			rt = []
			lt_up = []
			rt_up = []
			lt_box = []
			rt_box = []

			for j in range(m):
				for i in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-cc-a*j,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			for j in range(m):
				lt.append(Part.makeCylinder(d/2,t,Vector(0,-((y-11.0)/(m-1))*j-5.5,6),Vector(1,0,0)))
				lt_up.append(Part.makeCylinder(d/2,t,Vector(0,-((y-11.0)/(m-1))*j-5.5,8),Vector(1,0,0)))
				lt_box.append(Part.makeBox(2,d,t,Vector(0,-((y-11.0)/(m-1))*j-5.5+d/2,6),Vector(1,0,0)))
			for j in range(m):
				rt.append(Part.makeCylinder(d/2,t,Vector(x-t,-((y-11.0)/(m-1))*j-5.5,6),Vector(1,0,0)))
				rt_up.append(Part.makeCylinder(d/2,t,Vector(x-t,-((y-11.0)/(m-1))*j-5.5,8),Vector(1,0,0)))
				rt_box.append(Part.makeBox(2,d,t,Vector(x-t,-((y-11.0)/(m-1))*j-5.5+d/2,6),Vector(1,0,0)))

			for i in lt:
				plate2 = plate2.cut(i)
			for i in lt_up:
				plate2 = plate2.cut(i)
			for i in lt_box:
				plate2 = plate2.cut(i)
			for i in rt:
				plate3 = plate3.cut(i)
			for i in rt_up:
				plate3 = plate3.cut(i)
			for i in rt_box:
				plate3 = plate3.cut(i)

			plate1 = plate1.fuse(plate2)
			plate1 = plate1.fuse(plate3)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 1.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '52':
			doc=App.newDocument()

			D = 9.44
			D1 = 10.13
			D2 = 7.30
			h = 6.5
			h1 = 6.20
			h2 = 18.10
			t = 2.75
			d = 4.11
			d1 = 3.33
			d2 = 3.94


			circle = Part.makeCylinder(D/2,h,Vector(0,0,0))
			cir1 = Part.makeCylinder(d1/2,D,Vector(-D/2,0,6.5/2),Vector(1,0,0))
			circle = circle.cut(cir1)
			cir2 = Part.makeCylinder(d/2,h+h1,Vector(0,0,0), Vector(0,0,1))
			circle = circle.cut(cir2)


			#Part.show(circle)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '53':
			doc=App.newDocument()

			x = 38
			y = 12.7
			h = 9.3
			t = 0.71
			D = 9.25
			d = 4.11
			d1= 3.33

			plate1 = Part.makeBox(x,y,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(y/2-0.01, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])
			plate2 = Part.makeBox(2*d,d,t,Vector(x-5*d/2,(y-d)/2,0))
			plate2 = plate2.makeFillet(d/2-0.01, [plate2.Edges[0],plate2.Edges[2],plate2.Edges[4],plate2.Edges[6]])
			plate1 = plate1.cut(plate2)

			circle1 = Part.makeCylinder(D/2,h,Vector(x/2,y/2,0))
			plate1 = plate1.fuse(circle1)

			cir1 = Part.makeCylinder(d/2,t,Vector(y/2,y/2,0))
			plate1 = plate1.cut(cir1)
			cir2 = Part.makeCylinder(d/2,t,Vector(x/2,y/2,0))
			plate1 = plate1.cut(cir2)
			cir3 = Part.makeCylinder(d/2,h,Vector(x/2,y/2,0))
			plate1 = plate1.cut(cir3)
			cir4 = Part.makeCylinder(d1/2,y,Vector(x/2,0,3*d/2),Vector(0,1,0))
			plate1 = plate1.cut(cir4)


			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '54':

			doc=App.newDocument()

			# 기본형상 hexagon, circle
			s_hex=5.6 #hexagon_diameter
			cir_hex=4 #circle_diameter
			k_hex=2.1 #height

			exHex=Part.makeCylinder(s_hex/2,k_hex,Vector(0,0,-k_hex))

			d=3.8
			circ=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))
			exHex=exHex.fuse(circ)

			# 나사선 helix
			helix = Part.makeHelix(0.797,30,2)             #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((1.7,0,-0.125), (1.7,0,0.125))
			edge2 = Part.makeLine((1.7,0,0.125), (2.3,0,0.419))
			edge3 = Part.makeLine((2.3,0,0.419), (2.3,0,-0.419))
			edge4 = Part.makeLine((2.3,0,-0.419), (1.7,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)
		elif self.numericInput0.text() == '54a':
			doc=App.newDocument()

			# 기본형상 hexagon, circle
			s_hex=5.6 #hexagon_diameter
			cir_hex=3.5 #circle_diameter
			k_hex=2.1 #height

			exHex=Part.makeCylinder(s_hex/2,k_hex,Vector(0,0,-k_hex))

			d=3.5
			circ=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))
			exHex=exHex.fuse(circ)

			# 나사선 helix
			helix = Part.makeHelix(0.797,30,2)             #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((1.5,0,-0.125), (1.5,0,0.125))
			edge2 = Part.makeLine((1.5,0,0.125), (2.1,0,0.419))
			edge3 = Part.makeLine((2.1,0,0.419), (2.1,0,-0.419))
			edge4 = Part.makeLine((2.1,0,-0.419), (1.5,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(0.6,0.22,0.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)
		elif self.numericInput0.text() == '55':
			doc=App.newDocument()

			x = 139.7
			y = 63.5
			t = 0.7
			d = 4.2
			n = 11
			m = 5
			f = 6.35
			i = 0
			j = 0
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir = []

			for j in range(m):
				for i in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-cc-a*j,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 1.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '56':
			doc=App.newDocument()

			x = 38.1
			y = 38.1
			t = 0.7
			d = 4.2
			n = 3
			m = 3
			f = 6.35
			i = 0
			j = 0
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir = []

			for j in range(m):
				for i in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-cc-a*j,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '57':
			doc=App.newDocument()

			# 기본형상
			cir_hex=4 #circle_diameter

			d=75 #d 조절
			exHex=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))

			# 나사선 helix
			helix = Part.makeHelix(0.797,75,2) #75넣으면 메모리 문제로 실행 안될 수 있음. height 조절하기 #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((1.7,0,-0.125), (1.7,0,0.125))
			edge2 = Part.makeLine((1.7,0,0.125), (2.3,0,0.419))
			edge3 = Part.makeLine((2.3,0,0.419), (2.3,0,-0.419))
			edge4 = Part.makeLine((2.3,0,-0.419), (1.7,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)
		elif self.numericInput0.text() == '58':
			doc=App.newDocument()

			# 기본형상
			cir_hex=4 #circle_diameter

			d=50
			exHex=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))

			# 나사선 helix
			helix = Part.makeHelix(0.797,50,2) #50넣으면 메모리 문제로 실행 안될 수 있음.            #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((1.7,0,-0.125), (1.7,0,0.125))
			edge2 = Part.makeLine((1.7,0,0.125), (2.3,0,0.419))
			edge3 = Part.makeLine((2.3,0,0.419), (2.3,0,-0.419))
			edge4 = Part.makeLine((2.3,0,-0.419), (1.7,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)
		elif self.numericInput0.text() == '59':

			doc=App.newDocument()
			d1=83
			d2=57
			t=0.8

			d3=6.5
			d4=4.11/2

			plate1 = Part.makeCylinder(d1/2,t,Vector(0,0,0),Vector(0,0,1),91)
			plate2 = Part.makeCylinder(d2/2,t,Vector(0,0,0),Vector(0,0,1),91)
			plate1 = plate1.cut(plate2)

			cir1 = Part.makeCylinder(d3,t,Vector(34.5,0,0),Vector(0,0,1),180)
			cir1.rotate(Vector(34.5,0,0),Vector(0,0,1),180)
			cir2 = Part.makeCylinder(d3,t,Vector(34.5,0,0),Vector(0,0,1),180)
			cir2.rotate(Vector(0,0,0),Vector(0,0,1),91)
			plate1 = plate1.fuse(cir1)
			plate1 = plate1.fuse(cir2)

			cir3 = Part.makeCylinder(d4,t,Vector(34.5,0,0),Vector(0,0,1))
			cir4 = Part.makeCylinder(d4,t,Vector(34.5,0,0),Vector(0,0,1))
			cir4.rotate(Vector(0,0,0),Vector(0,0,1),91)
			cir5 = Part.makeCylinder(d4,t,Vector(34.5,0,0),Vector(0,0,1))
			cir5.rotate(Vector(0,0,0),Vector(0,0,1),45.5)
			plate1 = plate1.cut(cir3)
			plate1 = plate1.cut(cir4)
			plate1 = plate1.cut(cir5)

			box1 = Part.makeBox(4.0,3,t,Vector(34.5-2.0,-1.5,0),Vector(0,0,1))
			box1.rotate(Vector(0,0,0),Vector(0,0,1),23)
			plate1 = plate1.cut(box1)

			cir_up = Part.makeCylinder(2., t, Vector(34.5,+1.5,0),Vector(0,0,1))
			cir_up.rotate(Vector(0,0,0),Vector(0,0,1),23)
			plate1 = plate1.cut(cir_up)

			cir_dw = Part.makeCylinder(2.0, t, Vector(34.5,-1.5,0),Vector(0,0,1))
			cir_dw.rotate(Vector(0,0,0),Vector(0,0,1),23)
			plate1 = plate1.cut(cir_dw)

			box2 = Part.makeBox(4.0,3,t,Vector(34.5-2.0,-1.5,0),Vector(0,0,1))
			box2.rotate(Vector(0,0,0),Vector(0,0,1),68)
			plate1 = plate1.cut(box2)

			cir_up2 = Part.makeCylinder(2., t, Vector(34.5,+1.5,0),Vector(0,0,1))
			cir_up2.rotate(Vector(0,0,0),Vector(0,0,1),68)
			plate1 = plate1.cut(cir_up2)

			cir_dw3 = Part.makeCylinder(2.0, t, Vector(34.5,-1.5,0),Vector(0,0,1))
			cir_dw3.rotate(Vector(0,0,0),Vector(0,0,1),68)
			plate1 = plate1.cut(cir_dw3)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '60':

			doc=App.newDocument()

			x = 113.6
			y = 27.3
			t = 0.7
			d = 4.2
			n = 9
			f = 7
			i = 0
			j = 0
			a=12.5
			bb=(x-a*(n-1))/2 #6.5

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir = []
			cir1 = []
			cir2 = []
			box = []
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-6,0)))
				cir1.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,6-y+4,0)))
				cir2.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,6-y,0)))
			for i in range(n):
				box.append(Part.makeBox(d,4,t,Vector(bb+a*i-d/2,6-y,0)))
			for i in cir:
				plate1 = plate1.cut(i)
			for i in cir1:
				plate1 = plate1.cut(i)
			for i in cir2:
				plate1 = plate1.cut(i)
			for i in box:
				plate1 = plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '61':

			doc=App.newDocument()

			x = 88.2
			y = 27.3
			t = 0.7
			d = 4.2
			n = 7
			f = 7
			i = 0
			j = 0
			a=12.5
			bb=(x-a*(n-1))/2 #6.5

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir = []
			cir1 = []
			cir2 = []
			box = []
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-6,0)))
				cir1.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,6-y+4,0)))
				cir2.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,6-y,0)))
			for i in range(n):
				box.append(Part.makeBox(d,4,t,Vector(bb+a*i-d/2,6-y,0)))
			for i in cir:
				plate1 = plate1.cut(i)
			for i in cir1:
				plate1 = plate1.cut(i)
			for i in cir2:
				plate1 = plate1.cut(i)
			for i in box:
				plate1 = plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '62':

			doc=App.newDocument()

			x = 62.8
			y = 27.3
			t = 0.7
			d = 4.2
			n = 5
			f = 7
			i = 0
			j = 0
			a=12.5
			bb=(x-a*(n-1))/2 #6.5

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir = []
			cir1 = []
			cir2 = []
			box = []
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-6,0)))
				cir1.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,6-y+4,0)))
				cir2.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,6-y,0)))
			for i in range(n):
				box.append(Part.makeBox(d,4,t,Vector(bb+a*i-d/2,6-y,0)))
			for i in cir:
				plate1 = plate1.cut(i)
			for i in cir1:
				plate1 = plate1.cut(i)
			for i in cir2:
				plate1 = plate1.cut(i)
			for i in box:
				plate1 = plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '63':

			doc=App.newDocument()

			x = 37.4
			y = 27.3
			t = 0.7
			d = 4.2
			n = 3
			f = 7
			i = 0
			j = 0
			a=12.5
			bb=(x-a*(n-1))/2 #6.5

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir = []
			cir1 = []
			cir2 = []
			box = []
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-6,0)))
				cir1.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,6-y+4,0)))
				cir2.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,6-y,0)))
			for i in range(n):
				box.append(Part.makeBox(d,4,t,Vector(bb+a*i-d/2,6-y,0)))
			for i in cir:
				plate1 = plate1.cut(i)
			for i in cir1:
				plate1 = plate1.cut(i)
			for i in cir2:
				plate1 = plate1.cut(i)
			for i in box:
				plate1 = plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '64':
			doc=App.newDocument()

			D1 = 63
			D2 = 8.9
			h = 9.11
			h1 = 0.5
			d = 4.11
			d1 = 3.33
			t = 0.7
			x = 16.5
			x1 = 8.73
			x2 = 17.76
			a = 6.5

			i = 0
			j = 0
			n = 2

			circle = Part.makeCylinder(D1/2,t,Vector(0,0,0))
			circle1 = Part.makeCylinder(D2/2,h,Vector(0,0,-h1))
			circle = circle.fuse(circle1)


			plate1 = Part.makeBox(d,x,t,Vector(-d/2,D2/2+a,0))
			plate1 = plate1.makeFillet(d/2-0.01, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])
			circle = circle.cut(plate1)
			plate2 = Part.makeBox(d,x,t,Vector(-d/2,-D2/2-a-x,0))
			plate2 = plate2.makeFillet(d/2-0.01, [plate2.Edges[0],plate2.Edges[2],plate2.Edges[4],plate2.Edges[6]])
			circle = circle.cut(plate2)
			plate3 = Part.makeBox(x,d,t,Vector(D2/2+a,-d/2,0))
			plate3 = plate3.makeFillet(d/2-0.01, [plate3.Edges[0],plate3.Edges[2],plate3.Edges[4],plate3.Edges[6]])
			circle = circle.cut(plate3)
			plate4 = Part.makeBox(x,d,t,Vector(-D2/2-a-x,-d/2,0))
			plate4 = plate4.makeFillet(d/2-0.01, [plate4.Edges[0],plate4.Edges[2],plate4.Edges[4],plate4.Edges[6]])
			circle = circle.cut(plate4)

			cir1 = Part.makeCylinder(d1/2,D2,Vector(0,-D2/2,3*d/2),Vector(0,1,0))
			circle = circle.cut(cir1)
			cir2 = Part.makeCylinder(d/2,h,Vector(0,0,-h1))
			circle = circle.cut(cir2)

			cir3 = []
			cir4 = []
			for i in range(n):
				for j in range(n):
					cir3.append(Part.makeCylinder(d/2,t,Vector(-x1+2*x1*i,-x1+2*x1*j,0)))
			for i in cir3:
				circle = circle.cut(i)

			for i in range(n):
				for j in range(n):
					cir4.append(Part.makeCylinder(d/2,t,Vector(-x2+2*x2*i,-x2+2*x2*j,0)))
			for i in cir4:
				circle = circle.cut(i)


			#Part.show(circle)
			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '65':
			doc=App.newDocument()

			# 기본형상 hexagon, circle
			s_hex=5.6 #hexagon_diameter
			cir_hex=4 #circle_diameter
			k_hex=2.1 #height

			mhex=Base.Matrix()
			mhex.rotateZ(math.radians(60.0))
			polygon = []
			vhex=Base.Vector(s_hex/math.sqrt(3.0),0.0,-k_hex)
			for i in range(6):
				polygon.append(vhex)
				vhex = mhex.multiply(vhex)
			polygon.append(vhex)
			hexagon = Part.makePolygon(polygon)
			face=Part.Face(hexagon)
			exHex=face.extrude(Base.Vector(0.0,0.0,k_hex)) #높이

			d=13
			circ=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))
			exHex=exHex.fuse(circ)

			# 나사선 helix
			helix = Part.makeHelix(0.797,15,2)             #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((1.7,0,-0.125), (1.7,0,0.125))
			edge2 = Part.makeLine((1.7,0,0.125), (2.3,0,0.419))
			edge3 = Part.makeLine((2.3,0,0.419), (2.3,0,-0.419))
			edge4 = Part.makeLine((2.3,0,-0.419), (1.7,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)
		elif self.numericInput0.text() == '66':
			doc=App.newDocument()

			# 기본형상 hexagon, circle
			s_hex=5.6 #hexagon_diameter
			cir_hex=4 #circle_diameter
			k_hex=2.1 #height

			mhex=Base.Matrix()
			mhex.rotateZ(math.radians(60.0))
			polygon = []
			vhex=Base.Vector(s_hex/math.sqrt(3.0),0.0,-k_hex)
			for i in range(6):
				polygon.append(vhex)
				vhex = mhex.multiply(vhex)
			polygon.append(vhex)
			hexagon = Part.makePolygon(polygon)
			face=Part.Face(hexagon)
			exHex=face.extrude(Base.Vector(0.0,0.0,k_hex)) #높이

			d=20
			circ=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))
			exHex=exHex.fuse(circ)

			# 나사선 helix
			helix = Part.makeHelix(0.797,30,2)             #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((1.7,0,-0.125), (1.7,0,0.125))
			edge2 = Part.makeLine((1.7,0,0.125), (2.3,0,0.419))
			edge3 = Part.makeLine((2.3,0,0.419), (2.3,0,-0.419))
			edge4 = Part.makeLine((2.3,0,-0.419), (1.7,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)
		elif self.numericInput0.text() == '67':
			doc=App.newDocument()

			# 기본형상 hexagon, circle
			s_hex=5.6 #hexagon_diameter
			cir_hex=4 #circle_diameter
			k_hex=2.1 #height

			mhex=Base.Matrix()
			mhex.rotateZ(math.radians(60.0))
			polygon = []
			vhex=Base.Vector(s_hex/math.sqrt(3.0),0.0,-k_hex)
			for i in range(6):
				polygon.append(vhex)
				vhex = mhex.multiply(vhex)
			polygon.append(vhex)
			hexagon = Part.makePolygon(polygon)
			face=Part.Face(hexagon)
			exHex=face.extrude(Base.Vector(0.0,0.0,k_hex)) #높이

			d=30
			circ=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))
			exHex=exHex.fuse(circ)

			# 나사선 helix
			helix = Part.makeHelix(0.797,30,2)             #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((1.7,0,-0.125), (1.7,0,0.125))
			edge2 = Part.makeLine((1.7,0,0.125), (2.3,0,0.419))
			edge3 = Part.makeLine((2.3,0,0.419), (2.3,0,-0.419))
			edge4 = Part.makeLine((2.3,0,-0.419), (1.7,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)
		elif self.numericInput0.text() == '68':
			doc=App.newDocument()

			# 기본형상
			cir_hex=3.8 #circle_diameter

			d=34.2
			exHex=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))

			# 나사선 helix
			helix = Part.makeHelix(0.797,8.8,2) #50넣으면 메모리 문제로 실행 안될 수 있음.            #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((1.6,0,-0.125), (1.6,0,0.125))
			edge2 = Part.makeLine((1.6,0,0.125), (2.2,0,0.419))
			edge3 = Part.makeLine((2.2,0,0.419), (2.2,0,-0.419))
			edge4 = Part.makeLine((2.2,0,-0.419), (1.6,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)
		elif self.numericInput0.text() == '69':
			doc=App.newDocument()

			pro = Part.makeCone(7.2,1.2,14.7)
			#box1 = Part.makeBox(55,12,2.5,Vector(0,-6,3))
			#box2 = Part.makeBox(55,12,2.5,Vector(-55,-6,3))
			#box1 = box1.makeFillet(4,[box1.Edges[4],box1.Edges[6]])

			#pro = pro.fuse(box1)
			#pro = pro.fuse(box2)

			extend1 = Part.makePolygon([(0,2.5,3),(4,3,3),(32,5,3),(52,2.5,3),(52,-2.5,3),(32,-5,3),(4,-3,3),(0,-2.5,3),(-4,-3,3),(-32,-5,3),(-52,-2.5,3),(-52,2.5,3),(-32,5,3),(-4,3,3),(0,2.5,3)])
			fa2 = Part.Face(extend1)
			p2 = fa2.extrude(Vector(0,0,1))
			pro = pro.fuse(p2)

			#Part.show(pro)
			shape=doc.addObject("Part::Feature")
			shape.Shape=pro
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '70':
			doc=App.newDocument()

			x = 13.7
			x1 = 12
			y = 12.7
			h = 14.4
			t = 0.85
			d = 4.11
			i = 0
			n = 2

			plate1 = Part.makeBox(x,y,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(y/2-0.001, [plate1.Edges[0],plate1.Edges[2]])
			plate2 = Part.makeBox(t,y,h,Vector(x,0,0),Vector(0,0,1))
			plate1 = plate1.fuse(plate2)
			plate3 = Part.makeBox(x1+t,y,t,Vector(x,0,h),Vector(0,0,1))
			plate3 = plate3.makeFillet(y/2-0.001, [plate3.Edges[4],plate3.Edges[6]])
			plate1 = plate1.fuse(plate3)

			plate4 = Part.makeBox(d,d,t,Vector((x-d)/2,(y-d)/2,0))
			plate1 = plate1.cut(plate4)

			cir1 = Part.makeCylinder(d/2,t,Vector(x,y/2,h/2),Vector(1,0,0))
			plate1 = plate1.cut(cir1)
			cir2 = Part.makeCylinder(d/2,t,Vector((x-d)/2,y/2,0))
			plate1 = plate1.cut(cir2)
			cir3 = Part.makeCylinder(d/2,t,Vector((x+d)/2,y/2,0))
			plate1 = plate1.cut(cir3)
			cir4 = Part.makeCylinder(d/2,t,Vector(x+x1/2,y/2,h))
			plate1 = plate1.cut(cir4)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0,1.0,1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '71':
			doc=App.newDocument()

			x = 37.4
			y = 18.7
			y1= 37.7
			t = 0.68
			l=5.96
			d = 4.11
			f = 6

			n = 2
			n1 = 3
			i = 0
			j = 0

			plate1 = Part.makeBox(x,y,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[4]])
			tri = Part.makePolygon([(0,y,0),(x,y,0),(x/2,y1,0),(0,y,0)])
			fa = Part.Face(tri)
			p = fa.extrude(Vector(0,0,t))
			plate1 = plate1.fuse(p)

			tri1 = Part.makePolygon([(l,y,0),(2*l,y,0),(2*l,y+l,0),(l,y,0)])
			fa1 = Part.Face(tri1)
			p1 = fa1.extrude(Vector(0,0,t))
			plate1 = plate1.cut(p1)
			tri2 = Part.makePolygon([(x-l,y,0),(x-2*l,y,0),(x-2*l,y+l,0),(x-l,y,0)])
			fa2 = Part.Face(tri2)
			p2 = fa2.extrude(Vector(0,0,t))
			plate1 = plate1.cut(p2)

			pl = []
			cir = []
			cir1 = []
			for i in range(n):
				pl.append(Part.makeBox(l,l,t,Vector(l+(x-3*l)*i,y-l,0)))
			for i in pl:
				plate1 = plate1.cut(i)

			for i in range(n1):
				cir1.append(Part.makeCylinder(d/2,t,Vector(f+(x/2-f)*i,f,0)))
				if i == 2:
					for j in range(n):
						cir.append(Part.makeCylinder(d/2,t,Vector(x/2,f+(y1/2-f)*(j+1),0)))

			for i in cir:
				plate1 = plate1.cut(i)
			for i in cir1:
				plate1 = plate1.cut(i)


			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '72':
			doc=App.newDocument()

			x=12.7
			t=0.7
			f=6.3
			d=4.2

			box = Part.makeBox(x,x,t,Vector(0,0,0))
			box = box.makeFillet(f,[box.Edges[6]])
			box2 = Part.makeBox(x,x,t,Vector(-12.7,0,0))
			box2 = box2.makeFillet(f,[box2.Edges[2],box2.Edges[0]])
			box3 = Part.makeBox(x,x,t,Vector(0,-12.7,0))
			box3 = box3.makeFillet(f,[box3.Edges[0],box3.Edges[4]])
			box4 = Part.makeBox(x,x,t,Vector(-12.7,-12.7,0))
			box4 = box4.makeFillet(f,[box4.Edges[6]])
			box5 = Part.makeBox(x,x,t,Vector(-12.7,-12.7,0))
			box = box.fuse(box2)
			box = box.fuse(box3)
			box = box.fuse(box4)
			box = box.fuse(box5)
			box = box.cut(box4)
			cir1 = Part.makeCylinder(d/2,t,Vector(6.35,6.35,0))
			box = box.cut(cir1)
			cir2 = Part.makeCylinder(d/2,t,Vector(-6.35,6.35,0))
			box = box.cut(cir2)
			cir3 = Part.makeCylinder(d/2,t,Vector(6.35,-6.35,0))
			box = box.cut(cir3)
			#Part.show(box)
			shape=doc.addObject("Part::Feature")
			shape.Shape=box
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '73':
			doc=App.newDocument()

			cy1 = Part.makeCylinder(3.9,5.8,Vector(0,0,0),Vector(0,0,1),360)
			cy2 = Part.makeCylinder(1.95,5.8,Vector(0,0,0),Vector(0,0,1),360)
			cy1 = cy1.cut(cy2)

			cy3 = Part.makeCylinder(2.5,10.0,Vector(-3.0,0,2.9),Vector(-1,0,0),360)
			cy1 = cy1.fuse(cy3)

			tor = Part.makeTorus(8.5, 2.5,Vector(-22.0,0,2.9),Vector(0,0,1),0,360,300)
			tor.rotate(Vector(-22,0,2.9),Vector(0,0,-1),13)

			tri1 = Part.makePolygon([(-16.126,-1.38,0),(-9.96,-2.77,0),(-13.126,-5,0),(-16.126,-1.38,0)])
			fa1 = Part.Face(tri1)
			p1 = fa1.extrude(Vector(0,0,6))
			cy1 = cy1.cut(p1)

			cy1 = cy1.fuse(tor)
			#Part.show(cy1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=cy1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0,0.4,1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '74':
			doc=App.newDocument()

			x = 12.7
			y = 12.7
			t = 0.7
			h = 13.4
			d = 4.2

			plate1 = Part.makeBox(x,y,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(y/2-0.001, [plate1.Edges[0],plate1.Edges[2]])
			plate2 = Part.makeBox(t,y,h,Vector(x,0,0),Vector(0,0,1))
			plate2 = plate2.makeFillet(y/2-0.001, [plate2.Edges[11]])
			plate1 = plate1.fuse(plate2)
			plate3 = Part.makeBox(x,t,y,Vector (x,-t,t),Vector(0,0,1))
			plate3 = plate3.makeFillet(y/2-0.01, [plate3.Edges[5],plate3.Edges[7]])
			plate1 = plate1.fuse(plate3)

			cir1 = Part.makeCylinder(d/2,t,Vector(x/2,y/2,0))
			plate1 = plate1.cut(cir1)
			cir2 = Part.makeCylinder(d/2,t,Vector(x,y/2,y/2+t),Vector(1,0,0))
			plate1 = plate1.cut(cir2)
			plate4 = Part.makeBox(d,d,t,Vector(x+3.95,0,y/2+t+2.1),Vector(0,-1,0))
			cir3 = Part.makeCylinder(d/2,t,Vector(x+8.15,0,y/2+t),Vector(0,-1,0))
			cir4 = Part.makeCylinder(d/2,t,Vector(x+3.95,0,y/2+t),Vector(0,-1,0))
			plate1 = plate1.cut(plate4)
			plate1 = plate1.cut(cir4)
			plate1 = plate1.cut(cir3)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '75':
			doc=App.newDocument()

			x = 12.7
			y = 12.7
			t = 0.7
			h = 13.4
			d = 4.2

			plate1 = Part.makeBox(x,y,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(y/2-0.001, [plate1.Edges[0],plate1.Edges[2]])
			plate2 = Part.makeBox(t,y,h,Vector(x,0,0),Vector(0,0,1))
			plate2 = plate2.makeFillet(y/2-0.001, [plate2.Edges[9]])
			plate1 = plate1.fuse(plate2)
			plate3 = Part.makeBox(x,t,y,Vector (x,y,t),Vector(0,0,1))
			plate3 = plate3.makeFillet(y/2-0.01, [plate3.Edges[5],plate3.Edges[7]])
			plate1 = plate1.fuse(plate3)

			cir1 = Part.makeCylinder(d/2,t,Vector(x/2,y/2,0))
			plate1 = plate1.cut(cir1)
			cir2 = Part.makeCylinder(d/2,t,Vector(x,y/2,y/2+t),Vector(1,0,0))
			plate1 = plate1.cut(cir2)
			plate4 = Part.makeBox(d,d,t,Vector(x+3.95,y,y/2+t-2.1),Vector(0,1,0))
			cir3 = Part.makeCylinder(d/2,t,Vector(x+8.15,y,y/2+t),Vector(0,1,0))
			cir4 = Part.makeCylinder(d/2,t,Vector(x+3.95,y,y/2+t),Vector(0,1,0))
			plate1 = plate1.cut(plate4)
			plate1 = plate1.cut(cir4)
			plate1 = plate1.cut(cir3)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '76':
			doc=App.newDocument()

			l = 37.53
			w = 14.17
			h = 26.62
			t = 0.71
			d = 4.15
			n = 3
			f = 6.07

			plate1 = Part.makeBox(l,h,w,Vector(0,0,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(f, [plate1.Edges[2],plate1.Edges[6]])

			cir = []
			cir.append(Part.makeCylinder(d/2,w,Vector(4.1+d/2,5.06,0)))
			cir.append(Part.makeCylinder(d/2,w,Vector(4.1+d/2,17.84,0)))
			cir.append(Part.makeCylinder(d/2,w,Vector(16.63+d/2,5.06,0)))
			cir.append(Part.makeCylinder(d/2,w,Vector(16.63+d/2,17.84,0)))
			cir.append(Part.makeCylinder(d/2,w,Vector(29.29+d/2,5.06,0)))
			cir.append(Part.makeCylinder(d/2,w,Vector(29.29+d/2,17.84,0)))
			cir.append(Part.makeCylinder(d/2,h,Vector(4.1+d/2,0,4.96+d/2),Vector(0,1,0)))
			cir.append(Part.makeCylinder(d/2,h,Vector(16.63+d/2,0,4.96+d/2),Vector(0,1,0)))
			cir.append(Part.makeCylinder(d/2,h,Vector(29.29+d/2,0,4.96+d/2),Vector(0,1,0)))

			for i in cir:
				plate1 = plate1.cut(i)

			plate2 = Part.makeBox(l,h-0.7,w-1.4,Vector(0,0.7,0.7),Vector(0,0,1))
			plate1 = plate1.cut(plate2)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '77':
			doc=App.newDocument()

			D = 9.44
			D1 = 10.13
			D2 = 7.30
			h = 7.5
			h1 = 6.20
			h2 = 18.10
			t = 2.75
			d = 4.11
			d1 = 3.33
			d2 = 3.94


			circle = Part.makeCylinder(D/2,h,Vector(0,0,0))
			cir1 = Part.makeCylinder(d1/2,D,Vector(-D/2,0,1.65+d/2),Vector(1,0,0))
			circle = circle.cut(cir1)
			cir3 = Part.makeCylinder(D1/2,h1,Vector(0,0,h))
			circle = circle.fuse(cir3)
			plate1 = Part.makePolygon([(0.556226,5.025,h+h1),(12.885+0.400834,3.627654,h+h1),(12.885+0.400834,-3.627654,h+h1),(0.556226,-5.025,h+h1),(0.556226,5.025,h+h1)])
			plate1 = Part.Face(plate1)
			plate1 = plate1.extrude(Vector(0,0,-t))
			circle = circle.fuse(plate1)
			cir2 = Part.makeCylinder(d/2,h+h1,Vector(0,0,0), Vector(0,0,1))
			circle = circle.cut(cir2)
			cir4 = Part.makeCylinder(D2/2,t,Vector(12.885,0,h+h1),Vector(0,0,-1))
			circle = circle.cut(cir2)
			circle = circle.fuse(cir4)
			cir5 = Part.makeCylinder(d2/2,h2-t-d2/2,Vector(12.885,0,h+h1),Vector(0,0,1))
			circle = circle.fuse(cir5)
			sphere = Part.makeSphere(d2/2,Vector(12.885,0,h+h1+h2-t-d2/2),Vector(0,0,1),0,90,360)
			circle = circle.fuse(sphere)

			#Part.show(circle)
			#Part.show(sphere)
			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '80':
			doc=App.newDocument()

			x = 139.8
			y = 38.2
			r = 6.4
			t = 0.41
			d = 4.2
			n = 11
			m = 3
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5
			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(r, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			hole1 = Part.makeCylinder(d/2,t,Vector(x/2,-y/2,0))
			hole_up = []
			hole_down = []
			for i in range(n):
				hole_up.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-12.5-y/2,0)))
				hole_down.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,12.5-y/2,0)))
			plate1 = plate1.cut(hole1)
			for i in hole_up:
				plate1 = plate1.cut(i)
			for i in hole_down:
				plate1 = plate1.cut(i)

			left = []
			right = []
			box = []
			left2 = []
			right2 = []
			box2 = []
			for i in range(m):
				box.append(Part.makeBox(5,d,t,Vector(4.5,-cc-a*i-d/2,0)))
				left.append(Part.makeCylinder(d/2,t,Vector(bb-2.5,-cc-a*i,0)))
				right.append(Part.makeCylinder(d/2,t,Vector(bb+2.5,-cc-a*i,0)))
			for i in range(m):
				box2.append(Part.makeBox(5,d,t,Vector(x-bb-2.5,-cc-a*i-d/2,0)))
				left2.append(Part.makeCylinder(d/2,t,Vector(x-bb-2.5,-cc-a*i,0)))
				right2.append(Part.makeCylinder(d/2,t,Vector(x-bb+2.5,-cc-a*i,0)))
			for i in left:
				plate1 = plate1.cut(i)
			for i in right:
				plate1 = plate1.cut(i)
			for i in box:
				plate1 = plate1.cut(i)
			for i in left2:
				plate1 = plate1.cut(i)
			for i in right2:
				plate1 = plate1.cut(i)
			for i in box2:
				plate1 = plate1.cut(i)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 0.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '81':
			doc=App.newDocument()

			x = 89
			y = 63.6
			r = 6.4
			t = 0.41
			d = 4.2
			n = 7
			m = 5
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5
			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(r, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			hole1 = Part.makeCylinder(d/2,t,Vector(x/2,-y/2,0))
			hole_up = []
			hole_down = []
			for i in range(n):
				hole_up.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-25-y/2,0)))
				hole_down.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,25-y/2,0)))
			plate1 = plate1.cut(hole1)
			for i in hole_up:
				plate1 = plate1.cut(i)
			for i in hole_down:
				plate1 = plate1.cut(i)

			left = []
			right = []
			box = []
			left2 = []
			right2 = []
			box2 = []
			for i in range(m):
				box.append(Part.makeBox(5,d,t,Vector(4.5,-cc-a*i-d/2,0)))
				left.append(Part.makeCylinder(d/2,t,Vector(bb-2.5,-cc-a*i,0)))
				right.append(Part.makeCylinder(d/2,t,Vector(bb+2.5,-cc-a*i,0)))
			for i in range(m):
				box2.append(Part.makeBox(5,d,t,Vector(x-bb-2.5,-cc-a*i-d/2,0)))
				left2.append(Part.makeCylinder(d/2,t,Vector(x-bb-2.5,-cc-a*i,0)))
				right2.append(Part.makeCylinder(d/2,t,Vector(x-bb+2.5,-cc-a*i,0)))
			for i in left:
				plate1 = plate1.cut(i)
			for i in right:
				plate1 = plate1.cut(i)
			for i in box:
				plate1 = plate1.cut(i)
			for i in left2:
				plate1 = plate1.cut(i)
			for i in right2:
				plate1 = plate1.cut(i)
			for i in box2:
				plate1 = plate1.cut(i)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '82':
			doc=App.newDocument()

			x = 63.6
			y = 63.6
			r = 6.4
			t = 0.41
			d = 4.2
			n = 5
			m = 5
			b = n-1
			p = m-1
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5
			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(r, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			hole1 = Part.makeCylinder(d/2,t,Vector(x/2,-y/2,0))
			hole_up = []
			hole_down = []
			for i in range(n):
				hole_up.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-25-y/2,0)))
				hole_down.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,25-y/2,0)))
			plate1 = plate1.cut(hole1)
			for i in hole_up:
				plate1 = plate1.cut(i)
			for i in hole_down:
				plate1 = plate1.cut(i)

			left = []
			right = []
			box = []
			left2 = []
			right2 = []
			box2 = []
			for i in range(m):
				box.append(Part.makeBox(5,d,t,Vector(4.5,-cc-a*i-d/2,0)))
				left.append(Part.makeCylinder(d/2,t,Vector(bb-2.5,-cc-a*i,0)))
				right.append(Part.makeCylinder(d/2,t,Vector(bb+2.5,-cc-a*i,0)))
			for i in range(m):
				box2.append(Part.makeBox(5,d,t,Vector(x-bb-2.5,-cc-a*i-d/2,0)))
				left2.append(Part.makeCylinder(d/2,t,Vector(x-bb-2.5,-cc-a*i,0)))
				right2.append(Part.makeCylinder(d/2,t,Vector(x-bb+2.5,-cc-a*i,0)))
			for i in left:
				plate1 = plate1.cut(i)
			for i in right:
				plate1 = plate1.cut(i)
			for i in box:
				plate1 = plate1.cut(i)
			for i in left2:
				plate1 = plate1.cut(i)
			for i in right2:
				plate1 = plate1.cut(i)
			for i in box2:
				plate1 = plate1.cut(i)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '83':
			doc=App.newDocument()

			x = 63.6
			y = 38.2
			r = 6.4
			t = 0.41
			d = 4.2
			n = 5
			m = 3
			b = n-1
			p = m-1
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5
			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(r, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			hole1 = Part.makeCylinder(d/2,t,Vector(x/2,-y/2,0))
			hole_up = []
			hole_down = []
			for i in range(n):
				hole_up.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-12.5-y/2,0)))
				hole_down.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,12.5-y/2,0)))
			plate1 = plate1.cut(hole1)
			for i in hole_up:
				plate1 = plate1.cut(i)
			for i in hole_down:
				plate1 = plate1.cut(i)

			left = []
			right = []
			box = []
			left2 = []
			right2 = []
			box2 = []
			for i in range(m):
				box.append(Part.makeBox(5,d,t,Vector(4.5,-cc-a*i-d/2,0)))
				left.append(Part.makeCylinder(d/2,t,Vector(bb-2.5,-cc-a*i,0)))
				right.append(Part.makeCylinder(d/2,t,Vector(bb+2.5,-cc-a*i,0)))
			for i in range(m):
				box2.append(Part.makeBox(5,d,t,Vector(x-bb-2.5,-cc-a*i-d/2,0)))
				left2.append(Part.makeCylinder(d/2,t,Vector(x-bb-2.5,-cc-a*i,0)))
				right2.append(Part.makeCylinder(d/2,t,Vector(x-bb+2.5,-cc-a*i,0)))
			for i in left:
				plate1 = plate1.cut(i)
			for i in right:
				plate1 = plate1.cut(i)
			for i in box:
				plate1 = plate1.cut(i)
			for i in left2:
				plate1 = plate1.cut(i)
			for i in right2:
				plate1 = plate1.cut(i)
			for i in box2:
				plate1 = plate1.cut(i)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 0.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '84':
			doc=App.newDocument()

			x = 63.6
			y = 38.2
			r = 6.4
			t = 0.41
			d = 4.2
			n = 5
			m = 3
			b = n-1
			p = m-1
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5
			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(r, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			hole1 = Part.makeCylinder(d/2,t,Vector(x/2,-y/2,0))
			hole_up = []
			hole_down = []
			for i in range(n):
				hole_up.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-12.5-y/2,0)))
				hole_down.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,12.5-y/2,0)))
			plate1 = plate1.cut(hole1)
			for i in hole_up:
				plate1 = plate1.cut(i)
			for i in hole_down:
				plate1 = plate1.cut(i)

			left = []
			right = []
			box = []
			left2 = []
			right2 = []
			box2 = []
			for i in range(m):
				box.append(Part.makeBox(5,d,t,Vector(4.5,-cc-a*i-d/2,0)))
				left.append(Part.makeCylinder(d/2,t,Vector(bb-2.5,-cc-a*i,0)))
				right.append(Part.makeCylinder(d/2,t,Vector(bb+2.5,-cc-a*i,0)))
			for i in range(m):
				box2.append(Part.makeBox(5,d,t,Vector(x-bb-2.5,-cc-a*i-d/2,0)))
				left2.append(Part.makeCylinder(d/2,t,Vector(x-bb-2.5,-cc-a*i,0)))
				right2.append(Part.makeCylinder(d/2,t,Vector(x-bb+2.5,-cc-a*i,0)))
			for i in left:
				plate1 = plate1.cut(i)
			for i in right:
				plate1 = plate1.cut(i)
			for i in box:
				plate1 = plate1.cut(i)
			for i in left2:
				plate1 = plate1.cut(i)
			for i in right2:
				plate1 = plate1.cut(i)
			for i in box2:
				plate1 = plate1.cut(i)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 0.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '85':
			doc=App.newDocument()

			x = 139.8
			y = 63.6
			r = 6.4
			t = 0.41
			d = 4.2
			n = 11
			m = 5
			b = n-1
			p = m-1
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5
			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(r, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			hole1 = Part.makeCylinder(d/2,t,Vector(x/2,-y/2,0))
			hole_up = []
			hole_down = []
			for i in range(n):
				hole_up.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-25-y/2,0)))
				hole_down.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,25-y/2,0)))
			plate1 = plate1.cut(hole1)
			for i in hole_up:
				plate1 = plate1.cut(i)
			for i in hole_down:
				plate1 = plate1.cut(i)

			left = []
			right = []
			box = []
			left2 = []
			right2 = []
			box2 = []
			for i in range(m):
				box.append(Part.makeBox(5,d,t,Vector(4.5,-cc-a*i-d/2,0)))
				left.append(Part.makeCylinder(d/2,t,Vector(bb-2.5,-cc-a*i,0)))
				right.append(Part.makeCylinder(d/2,t,Vector(bb+2.5,-cc-a*i,0)))
			for i in range(m):
				box2.append(Part.makeBox(5,d,t,Vector(x-bb-2.5,-cc-a*i-d/2,0)))
				left2.append(Part.makeCylinder(d/2,t,Vector(x-bb-2.5,-cc-a*i,0)))
				right2.append(Part.makeCylinder(d/2,t,Vector(x-bb+2.5,-cc-a*i,0)))
			for i in left:
				plate1 = plate1.cut(i)
			for i in right:
				plate1 = plate1.cut(i)
			for i in box:
				plate1 = plate1.cut(i)
			for i in left2:
				plate1 = plate1.cut(i)
			for i in right2:
				plate1 = plate1.cut(i)
			for i in box2:
				plate1 = plate1.cut(i)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 0.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '86':
			doc=App.newDocument()

			# 기본형상 hexagon, circle
			s_hex=6.9 #hexagon_diameter
			k_hex=20 #height

			mhex=Base.Matrix()
			mhex.rotateZ(math.radians(60.0))
			polygon = []
			vhex=Base.Vector(s_hex/math.sqrt(3.0),0.0,-k_hex)
			for i in range(6):
				polygon.append(vhex)
				vhex = mhex.multiply(vhex)
			polygon.append(vhex)
			hexagon = Part.makePolygon(polygon)
			face=Part.Face(hexagon)
			exHex=face.extrude(Base.Vector(0.0,0.0,k_hex)) #높이

			d=30
			cir_hex=6.8 #circle_diameter
			circ=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,-25))
			exHex=exHex.fuse(circ)

			d=40
			cir_hex1=4.0 #circle_diameter
			circ1=Part.makeCylinder(cir_hex1/2.0,d,Vector(0,0,-35))
			exHex=exHex.cut(circ1)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)
		elif self.numericInput0.text() == '87':
			doc=App.newDocument()

			D = 64
			d = 4.11
			f = 6
			t = 0.97
			i = 0
			n = 5
			cir = []

			plate1 = Part.makeBox(D,D/2,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(D/2-0.01, [plate1.Edges[2],plate1.Edges[6]])

			plate2 = Part.makeBox(D,f,t,Vector(0,-f,0))
			plate2 = plate2.makeFillet(f-0.01, [plate2.Edges[0],plate2.Edges[4]])

			plate1 = plate1.fuse(plate2)

			for i in range(n):
				cir.append(Part.makeCylinder(d/2, t, Vector(f+12.7*i,0,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			circle1 = Part.makeCylinder(d/2, t, Vector(f+12.7*2,12.7,0))
			circle2 = Part.makeCylinder(d/2, t, Vector(f+12.7*2,12.7*2,0))
			plate1 = plate1.cut(circle1)
			plate1 = plate1.cut(circle2)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '88':

			doc=App.newDocument()

			plate1 = Part.makeCylinder(44.5,12.7,Vector(0,0,0),Vector(0,0,1),90)
			plate2 = Part.makeCylinder(43.8,12.7,Vector(0,0,0),Vector(0,0,1),90)
			plate1 = plate1.cut(plate2)

			cir1 = Part.makeCylinder(6.35,0.7,Vector(43.8,0,6.35),Vector(1,0,0),180)
			plate1 = plate1.fuse(cir1)
			cir2 = Part.makeCylinder(6.35,0.7,Vector(0,43.8,6.35),Vector(0,-1,0),180)
			cir2.rotate(Vector(0,43.8,6.35),Vector(0,0,1),180)
			plate1 = plate1.fuse(cir2)

			cir3 = Part.makeCylinder(4.0/2,50,Vector(0,0,6.35),Vector(0,1,0))
			plate1 = plate1.cut(cir3)

			cir4 = Part.makeCylinder(4.0/2,50,Vector(0,0,6.35),Vector(0,1,0))
			cir4.rotate(Vector(0,0,0),Vector(0,0,1),-45)
			plate1 = plate1.cut(cir4)

			cir5 = Part.makeCylinder(4.0/2,50,Vector(0,0,6.35),Vector(0,1,0))
			cir5.rotate(Vector(0,0,0),Vector(0,0,1),-90)
			plate1 = plate1.cut(cir5)

			cir6 = Part.makeCylinder(4.0/2,50,Vector(0,0,6.35),Vector(0,1,0))
			cir6.rotate(Vector(0,0,0),Vector(0,0,1),-20)
			plate1 = plate1.cut(cir6)

			cir7 = Part.makeCylinder(4.0/2,50,Vector(0,0,6.35),Vector(0,1,0))
			cir7.rotate(Vector(0,0,0),Vector(0,0,1),-70)
			plate1 = plate1.cut(cir7)

			box1 = Part.makeBox(4.0,50,15,Vector(0,0,4.36),Vector(0,1,0))
			plate1 = plate1.cut(box1)
			box2 = Part.makeBox(4.0,50,15,Vector(0,0,8.36),Vector(0,-1,0))
			box2.rotate(Vector(0,0,0),Vector(0,0,1),90)
			plate1 = plate1.cut(box2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '89':

			doc=App.newDocument()
			v=8.9
			x=63
			t=1
			r=4.45 #v/2
			n=5
			a=12.5
			f=(x-a*(n-1))/2 #6.5
			i=0
			d=4.1

			plate1=Part.makeBox(x,v,t,Vector(0,0,0))
			plate1=plate1.makeFillet(r-0.01,[plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir=[]
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,r,0)))
			for i in cir:
				plate1=plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '90':
			doc=App.newDocument()
			v=8.9
			x=75.6
			t=1
			r=4.45
			n=6
			a=12.5
			f=(x-a*(n-1))/2 #6.5
			i=0
			d=4.1

			plate1=Part.makeBox(x,v,t,Vector(0,0,0))
			plate1=plate1.makeFillet(r-0.01,[plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir=[]
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,r,0)))
			for i in cir:
				plate1=plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '91':
			doc=App.newDocument()
			v=8.9
			x=88.2
			t=1
			r=4.45
			n=7
			a=12.5
			f=(x-a*(n-1))/2 #6.5
			i=0
			d=4.1

			plate1=Part.makeBox(x,v,t,Vector(0,0,0))
			plate1=plate1.makeFillet(r-0.01,[plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir=[]
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,r,0)))
			for i in cir:
				plate1=plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '92':
			doc=App.newDocument()
			v=8.9
			x=113.7
			t=1
			r=4.45
			n=9
			a=12.5
			f=(x-a*(n-1))/2 #6.5
			i=0
			d=4.1

			plate1=Part.makeBox(x,v,t,Vector(0,0,0))
			plate1=plate1.makeFillet(r-0.01,[plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir=[]
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,r,0)))
			for i in cir:
				plate1=plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '93':

			doc=App.newDocument()
			v=8.9
			x=37.4
			t=1
			r=4.45
			n=3
			a=12.5
			f=(x-a*(n-1))/2 #6.5
			i=0
			d=4.1

			plate1=Part.makeBox(x,v,t,Vector(0,0,0))
			plate1=plate1.makeFillet(r-0.01,[plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir=[]
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,r,0)))
			for i in cir:
				plate1=plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '94':
			doc=App.newDocument()

			d = 27
			t = 7.7
			d1 = 18.48
			d2 = 15.47
			d3 = 13.24
			h1 = 1.43
			h2 = 4.38
			n = 2
			i = 0

			circle = Part.makeCylinder(d/2,t,Vector(0,0,0))
			circle = circle.makeFillet((t-h1)/2,[circle.Edges[0],circle.Edges[2]])

			cir = []
			cir1 = []
			for i in range(n):
				cir.append(Part.makeCylinder(d1/2,(t-h2)/2,Vector(0,0,(t-(t-h2)/2)*i)))
				cir1.append(Part.makeCylinder(d2/2,(t-h1)/2,Vector(0,0,(t-(t-h1)/2)*i)))
			for i in cir:
				circle = circle.cut(i)
			for i in cir1:
				circle = circle.cut(i)

			circle1 = Part.makeCylinder(d3/2,h1,Vector(0,0,(t-h1)/2))
			circle = circle.cut(circle1)

			#Part.show(circle)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '97':
			doc=App.newDocument()

			x=34.8
			x1= 16.82
			y1=17.25
			t=1.8
			d=4.2
			d1=11.20
			d2=32
			d3=21
			d4=3.95
			h1=16.23
			h2=30
			h3=3.0
			h4=1.95
			h5=15.6
			h6=29.75
			h7=15.3
			f=4.95
			n=3
			i=0
			j=0
			cir=[]

			plate1 = Part.makeBox(x,x,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])
			plate2 = Part.makeBox(x1,y1,h1,Vector(8.99,8.775,0))
			plate3 = Part.makeBox(x1-2*t,y1-2*t,h7,Vector(8.99+t,8.775+t,0))
			plate1 = plate1.fuse(plate2)
			plate1 = plate1.cut(plate3)

			for i in range(n):
			   for j in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(4.65+12.75*i,4.65+12.75*j,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			circle1 = Part.makeCylinder(d2/2,h6,Vector(x/2,8.775-3.6,h2),Vector(0,1,0))
			circle2 = Part.makeCylinder(d1/2,h3,Vector(x/2,8.775-3.6,h2),Vector(0,-1,0))
			circle3 = Part.makeCylinder(d3/2,h4,Vector(x/2,8.775-3.6+h6,h2),Vector(0,1,0))
			circle4 = Part.makeCylinder(d4/2,h5,Vector(x/2,8.775-3.6+h6+h4,h2),Vector(0,1,0))
			plate1 = plate1.fuse(circle1)
			plate1 = plate1.fuse(circle2)
			plate1 = plate1.fuse(circle3)
			plate1 = plate1.fuse(circle4)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '100':

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=0.48, z=54, alpha=20 * pi / 180., clearence=0, shift=0., beta=0., undercut=False, simple=False, height=3.0, backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                self.m_n = 0.5
			                self.z = 36
			                self.height = 3.0
			                self.m = self.m_n / cos(self.beta)
			                self.c = self.clearence * self.m_n
			                self.midpoint = [0., 0]
			                self.d = self.z * self.m
			                self.dw = self.m * self.z
			                self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			                self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			                self.dg = self.d * cos(self.alpha_t)
			                self.phipart = 2 * pi / self.z
			                self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			                self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			                self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			                self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			                self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot = self.involute_rot1 + self.involute_rot2
			                self.involute_start = 0.
			                if self.dg <= self.df:
			                    self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			                pts = self.points(self.numpoints)
			                if not self.simple:
			                    wi = []
			                    for i in pts:
			                        out = BSplineCurve()
			                        out.interpolate(map(fcvec, i))
			                        wi.append(out)
			                    s = Wire(Shape(wi).Edges)
			                    wi = []
			                    for i in range(self.z):
			                        rot = App.Matrix()
			                        rot.rotateZ(-i * self.phipart)
			                        tooth_rot = s.transformGeometry(rot)
			                        if i != 0:
			                            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                            pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                            wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                        wi.append(tooth_rot)
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                    wi = Wire(wi)
			                    self.Shapea = wi
			                    if self.beta == 0:
			                        sh = Face(wi)
			                        self.Shapea = sh.extrude(App.Vector(0, 0, self.height))
			                        self.Shapea.translate(Vector(11.0,-5.0,-3.5))
			                    self.Shape = self.Shape.fuse(self.Shapea)


			                self.m_n = 0.57
			                self.z = 10
			                self.height = 6.6
			                self.m = self.m_n / cos(self.beta)
			                self.c = self.clearence * self.m_n
			                self.midpoint = [0., 0]
			                self.d = self.z * self.m
			                self.dw = self.m * self.z
			                self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			                self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			                self.dg = self.d * cos(self.alpha_t)
			                self.phipart = 2 * pi / self.z
			                self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			                self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			                self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			                self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			                self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot = self.involute_rot1 + self.involute_rot2
			                self.involute_start = 0.
			                if self.dg <= self.df:
			                    self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			                pts = self.points(self.numpoints)
			                if not self.simple:
			                    wi = []
			                    for i in pts:
			                        out = BSplineCurve()
			                        out.interpolate(map(fcvec, i))
			                        wi.append(out)
			                    s = Wire(Shape(wi).Edges)
			                    wi = []
			                    for i in range(self.z):
			                        rot = App.Matrix()
			                        rot.rotateZ(-i * self.phipart)
			                        tooth_rot = s.transformGeometry(rot)
			                        if i != 0:
			                            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                            pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                            wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                        wi.append(tooth_rot)
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                    wi = Wire(wi)
			                    self.Shapea = wi
			                    if self.beta == 0:
			                        sh = Face(wi)
			                        self.Shapea = sh.extrude(App.Vector(0, 0, self.height))
			                        self.Shapea.translate(Vector(11.0,-5.0,-9.5))
			                    self.Shape = self.Shape.fuse(self.Shapea)


			                self.m_n = 0.52
			                self.z = 10
			                self.height = 9.5
			                self.m = self.m_n / cos(self.beta)
			                self.c = self.clearence * self.m_n
			                self.midpoint = [0., 0]
			                self.d = self.z * self.m
			                self.dw = self.m * self.z
			                self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			                self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			                self.dg = self.d * cos(self.alpha_t)
			                self.phipart = 2 * pi / self.z
			                self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			                self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			                self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			                self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			                self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot = self.involute_rot1 + self.involute_rot2
			                self.involute_start = 0.
			                if self.dg <= self.df:
			                    self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			                pts = self.points(self.numpoints)
			                if not self.simple:
			                    wi = []
			                    for i in pts:
			                        out = BSplineCurve()
			                        out.interpolate(map(fcvec, i))
			                        wi.append(out)
			                    s = Wire(Shape(wi).Edges)
			                    wi = []
			                    for i in range(self.z):
			                        rot = App.Matrix()
			                        rot.rotateZ(-i * self.phipart)
			                        tooth_rot = s.transformGeometry(rot)
			                        if i != 0:
			                            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                            pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                            wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                        wi.append(tooth_rot)
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                    wi = Wire(wi)
			                    self.Shapea = wi
			                    if self.beta == 0:
			                        sh = Face(wi)
			                        self.Shapea = sh.extrude(App.Vector(0, 0, self.height))
			                        self.Shapea.translate(Vector(0,0,-9.5))
			                        self.Shapea.rotate(Vector(0,0,0),Vector(0,0,1),15)
			                    self.Shape = self.Shape.fuse(self.Shapea)

			                self.m_n = 0.48
			                self.z = 10
			                self.height = 7.5
			                self.m = self.m_n / cos(self.beta)
			                self.c = self.clearence * self.m_n
			                self.midpoint = [0., 0]
			                self.d = self.z * self.m
			                self.dw = self.m * self.z
			                self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			                self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			                self.dg = self.d * cos(self.alpha_t)
			                self.phipart = 2 * pi / self.z
			                self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			                self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			                self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			                self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			                self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot = self.involute_rot1 + self.involute_rot2
			                self.involute_start = 0.
			                if self.dg <= self.df:
			                    self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			                pts = self.points(self.numpoints)
			                if not self.simple:
			                    wi = []
			                    for i in pts:
			                        out = BSplineCurve()
			                        out.interpolate(map(fcvec, i))
			                        wi.append(out)
			                    s = Wire(Shape(wi).Edges)
			                    wi = []
			                    for i in range(self.z):
			                        rot = App.Matrix()
			                        rot.rotateZ(-i * self.phipart)
			                        tooth_rot = s.transformGeometry(rot)
			                        if i != 0:
			                            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                            pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                            wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                        wi.append(tooth_rot)
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                    wi = Wire(wi)
			                    self.Shapea = wi
			                    if self.beta == 0:
			                        sh = Face(wi)
			                        self.Shapea = sh.extrude(App.Vector(0, 0, self.height))
			                        self.Shapea.translate(Vector(-15.7,0,-4.5))
			                        self.Shapea.rotate(Vector(-15.7,0,-4.5),Vector(0,0,1),15)
			                    self.Shape = self.Shape.fuse(self.Shapea)

			                self.m_n = 0.57
			                self.z = 20
			                self.height = 5.0
			                self.m = self.m_n / cos(self.beta)
			                self.c = self.clearence * self.m_n
			                self.midpoint = [0., 0]
			                self.d = self.z * self.m
			                self.dw = self.m * self.z
			                self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			                self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			                self.dg = self.d * cos(self.alpha_t)
			                self.phipart = 2 * pi / self.z
			                self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			                self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			                self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			                self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			                self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot = self.involute_rot1 + self.involute_rot2
			                self.involute_start = 0.
			                if self.dg <= self.df:
			                    self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			                pts = self.points(self.numpoints)
			                if not self.simple:
			                    wi = []
			                    for i in pts:
			                        out = BSplineCurve()
			                        out.interpolate(map(fcvec, i))
			                        wi.append(out)
			                    s = Wire(Shape(wi).Edges)
			                    wi = []
			                    for i in range(self.z):
			                        rot = App.Matrix()
			                        rot.rotateZ(-i * self.phipart)
			                        tooth_rot = s.transformGeometry(rot)
			                        if i != 0:
			                            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                            pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                            wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                        wi.append(tooth_rot)
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                    wi = Wire(wi)
			                    self.Shapea = wi
			                    if self.beta == 0:
			                        sh = Face(wi)
			                        self.Shapea = sh.extrude(App.Vector(0, 0, self.height))
			                        self.Shapea.translate(Vector(18.5,-9.5,-9.1))
			                    self.Shape = self.Shape.fuse(self.Shapea)

			                self.cy1 = Part.makeCylinder(2.0,35.4,Vector(18.5,-9.5,-9.1),Vector(0,0,-1))
			                self.Shape = self.Shape.fuse(self.cy1)
			                self.cy2 = Part.makeCylinder(1.3,35.4,Vector(11.0,-5.0,-9.5),Vector(0,0,-1))
			                self.Shape = self.Shape.fuse(self.cy2)
			                self.cy3 = Part.makeCylinder(1.3,35.4,Vector(0,0,-9.5),Vector(0,0,-1))
			                self.Shape = self.Shape.fuse(self.cy3)
			                self.cy4 = Part.makeCylinder(1.0,40.0,Vector(-15.7,0,-4.5),Vector(0,0,-1))
			                self.Shape = self.Shape.fuse(self.cy4)
			                self.cy5 = Part.makeCylinder(10.5,3.8,Vector(-15.7,0,-11.5),Vector(0,0,-1))
			                self.Shape = self.Shape.fuse(self.cy5)
			                self.cy6 = Part.makeCylinder(13.6,26.3,Vector(-15.7,0,-15.3),Vector(0,0,-1))
			                self.Shape = self.Shape.fuse(self.cy6)
			                self.cy7 = Part.makeCylinder(4.2,2.0,Vector(-15.7,0,-15.3-26.3),Vector(0,0,-1))
			                self.Shape = self.Shape.fuse(self.cy7)

			                extend1 = Part.makePolygon([(0,11,-9.5),(-30,11,-9.5),(-30,-17.4,-9.5),(13.5,-17.4,-9.5),(23.0,-13,-9.5),(23.0,-8.9,-9.5),(0,11,-9.5)])
			                fa1 = Part.Face(extend1)
			                p1 = fa1.extrude(Vector(0,0,-0.8))
			                self.Shape = self.Shape.fuse(p1)
			                p2 = p1.mirror(Vector(0,0,-26.5),Vector(0,0,1))
			                self.Shape = self.Shape.fuse(p2)

			                extend3 = Part.makePolygon([(-30,-17.4,-9.5),(-30,-17.4,-43),(13.5,-17.4,-43),(13.5,-17.4,-9.5),(-30.0,-17.4,-9.5)])
			                fa3 = Part.Face(extend3)
			                p3 = fa3.extrude(Vector(0,0.8,0))
			                self.Shape = self.Shape.fuse(p3)

			                self.cy8 = Part.makeCylinder(2.1,2,Vector(6.0,-17.4,-20),Vector(0,1,0))
			                self.Shape = self.Shape.cut(self.cy8)
			                self.cy9 = Part.makeCylinder(2.1,2,Vector(-6.0,-17.4,-20),Vector(0,1,0))
			                self.Shape = self.Shape.cut(self.cy9)
			                self.cy10 = Part.makeCylinder(2.1,2,Vector(6.0,-17.4,-32),Vector(0,1,0))
			                self.Shape = self.Shape.cut(self.cy10)
			                self.cy11 = Part.makeCylinder(2.1,2,Vector(-6.0,-17.4,-32),Vector(0,1,0))
			                self.Shape = self.Shape.cut(self.cy11)

			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])


			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '100a':
			doc=App.newDocument()

			x=34.8
			y=34.3
			h=24.7
			h1=3
			h2=3.95
			h3=14.3
			d=3.9
			d1=3.95
			x1= 16.0
			l=4.45
			l1=12.7
			n=3
			n1=2
			n2=5
			i=0
			j=0

			cir=[]
			cir1=[]
			cir5=[]
			cir6=[]
			cir7=[]
			cir8=[]
			cir9=[]
			cir10=[]
			cir11=[]
			cir12=[]

			plate1 = Part.makeBox(x,y,h,Vector(0,0,0))
			plate2 = Part.makeBox(x1,y,h2,Vector((x-x1)/2,0,h))
			plate1 = plate1.fuse(plate2)

			for i in range(n):
					cir.append(Part.makeCylinder(d/2,h1,Vector(x/2,l+l1*i,h+h2)))
			for i in cir:
				plate1 = plate1.fuse(i)

			for i in range(n):
					cir1.append(Part.makeCylinder(d/2,h1,Vector(x/2,l+l1*i,0),Vector(0,0,-1)))
			for i in cir1:
				plate1 = plate1.fuse(i)

			cir3 = Part.makeCylinder(d1/2,h3,Vector(x/2,y,h-4.045),Vector(0,1,0))
			cir4 = Part.makeCylinder(d/2,h1,Vector(x/2,y,h-4.045-12.66),Vector(0,1,0))
			plate1 = plate1.fuse(cir3)
			plate1 = plate1.fuse(cir4)

			for i in range(n):
			        cir5.append(Part.makeCylinder(d/2,h1,Vector((x-28.6+d)/2+((28.6-d)/2)*i,0,h-4.045-12.66),Vector(0,-1,0)))
			for i in cir5:
				plate1 = plate1.fuse(i)

			for i in range(n1):
			        cir6.append(Part.makeCylinder(d/2,h1,Vector((x-28.6+d)/2+(28.6-d)*i,0,h-4.045),Vector(0,-1,0)))
			for i in cir6:
				plate1 = plate1.fuse(i)

			plate3 = Part.makeBox(7.25,3.25,7.06,Vector(x/2-7.25/2,-3.25,h+h2-9.21-7.06))
			plate1 = plate1.fuse(plate3)

			for i in range(n2):
					cir7.append(Part.makeCylinder(d/2,h1,Vector(0,l+(l1*2)/4*i,h-4.045-12.66/2), Vector(1,0,0)))
			for i in cir7:
				plate1 = plate1.cut(i)

			for i in range(n2):
					cir8.append(Part.makeCylinder(d/2,h1,Vector(x,l+(l1*2)/4*i,h-4.045-12.66/2), Vector(-1,0,0)))
			for i in cir8:
				plate1 = plate1.cut(i)

			for i in range(n2):
					cir9.append(Part.makeCylinder(d/2,h1,Vector((x-28.6+d)/2,l+(l1*2)/4*i,0), Vector(0,0,1)))
			for i in cir9:
				plate1 = plate1.cut(i)

			for i in range(n2):
					cir10.append(Part.makeCylinder(d/2,h1,Vector((x-28.6+d)/2+(28.6-d),l+(l1*2)/4*i,0), Vector(0,0,1)))
			for i in cir10:
				plate1 = plate1.cut(i)


			for i in range(n1):
			   for j in range(n1):
					cir11.append(Part.makeCylinder(d/2,h1,Vector(0,l+(l1)/2+l1*i,h-4.045-12.66*j),Vector(1,0,0)))

			for i in cir11:
				plate1 = plate1.cut(i)

			for i in range(n1):
			   for j in range(n1):
					cir12.append(Part.makeCylinder(d/2,h1,Vector(x,l+(l1)/2+l1*i,h-4.045-12.66*j),Vector(-1,0,0)))

			for i in cir12:
				plate1 = plate1.cut(i)


			#Part.show(plate1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.8,0.8,0.8)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '102':
			doc=App.newDocument()

			x=89
			y=78.8
			t=0.42
			f=3
			d=4.25
			i=0
			j=0
			n=4
			m=3
			cir = []
			cir2 = []
			cir3 = []
			box = []
			tri = Part.makePolygon([(0,0,0),(x,0,0),(x/2,y,0),(0,0,0)])
			fa = Part.Face(tri)
			p = fa.extrude(Vector(0,0,t))
			p = p.makeFillet(f, [p.Edges[0],p.Edges[1],p.Edges[4]])

			for i in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(6.62+25.25*i,4.3,0)))
			for i in cir:
			        p = p.cut(i)
			for j in range(m):
					cir2.append(Part.makeCylinder(d/2,t,Vector(17.105+25.25*j,4.3,0)))
					box.append(Part.makeBox(4.28,4.25,t,Vector(17.105+25.25*j,2.18,0)))
					cir3.append(Part.makeCylinder(d/2,t,Vector(21.385+25.25*j,4.3,0)))
			for j in cir2:
					p = p.cut(j)
			for j in cir3:
					p = p.cut(j)
			for j in box:
					p = p.cut(j)
			for i in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(6.62+12.47*i,4.3+25.25*0.866*i,0)))
			for i in cir:
			        p = p.cut(i)
			for j in range(m):
					cir2.append(Part.makeCylinder(d/2,t,Vector(6.62+5.24+12.47*j,4.3+10.485*0.866+25.25*0.866*j,0)))
					box.append(Part.makeBox(4.28,4.25,4.25,Vector(4.78+5.24+12.47*j,14.44751+25.25*0.866*j,0),Vector(0.5,-0.29,0)))
					cir3.append(Part.makeCylinder(d/2,t,Vector(6.62+7.38+12.47*j,4.3+14.765*0.866+25.25*0.866*j,0)))
			for j in cir2:
					p = p.cut(j)
			for j in cir3:
					p = p.cut(j)
			for j in box:
					p = p.cut(j)
			for j in range(m):
					cir2.append(Part.makeCylinder(d/2,t,Vector(89-(6.62+5.24+12.47*j),4.3+10.485*0.866+25.25*0.866*j,0)))
					box.append(Part.makeBox(4.28,4.25,4.25,Vector(89-(3.68+4.78+5.24+12.47*j),14.44751-2.125+25.25*0.866*j,0),Vector(0.5,0.29,0)))
					cir3.append(Part.makeCylinder(d/2,t,Vector(89-(6.62+7.38+12.47*j),4.3+14.765*0.866+25.25*0.866*j,0)))
			for j in cir2:
					p = p.cut(j)
			for j in cir3:
					p = p.cut(j)
			for j in box:
					p = p.cut(j)
			for i in range(3):
					cir.append(Part.makeCylinder(d/2,t,Vector(89-(6.62+12.47*i),4.3+25.25*0.866*i,0)))
			for i in cir:
			        p = p.cut(i)

			cir4 = Part.makeCylinder(d/2,t,Vector(44.5,27,0))
			p = p.cut(cir4)
			#Part.show(p)
			shape=doc.addObject("Part::Feature")
			shape.Shape=p
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '103':

			doc=App.newDocument()

			D = 64
			d = 4.11
			f = 6
			t = 0.97
			i = 0
			n = 5

			plate1 = Part.makeBox(D,D/2,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(D/2-0.01, [plate1.Edges[2],plate1.Edges[6]])

			plate2 = Part.makeBox(D,f,t,Vector(0,-f,0))
			plate2 = plate2.makeFillet(f-0.01, [plate2.Edges[0],plate2.Edges[4]])

			plate1 = plate1.fuse(plate2)

			cir = []
			for i in range(n):
				cir.append(Part.makeCylinder(d/2, t, Vector(f+12.7*i,-2,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			cir2 = []
			for i in range(n):
				cir2.append(Part.makeCylinder(d/2, t, Vector(f+12.7*i,2.5,0)))
			for i in cir2:
				plate1 = plate1.cut(i)

			box3 = []
			for i in range(n):
				box3.append(Part.makeBox(d, 4.5, t, Vector((f-d/2)+12.7*i,-2,0)))
			for i in box3:
				plate1 = plate1.cut(i)

			#가운데 사각형 회전
			box4 = Part.makeBox(d, 4.5, 50, Vector(f-d/2,-2,0))
			box4.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),-30)
			plate1 = plate1.cut(box4)

			box5 = Part.makeBox(d, 4.5, 50, Vector(f-d/2,-2,0))
			box5.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),-60)
			plate1 = plate1.cut(box5)

			box6 = Part.makeBox(d, 4.5, 50, Vector(f-d/2,-2,0))
			box6.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),-90)
			plate1 = plate1.cut(box6)

			box7 = Part.makeBox(d, 4.5, 50, Vector(f-d/2,-2,0))
			box7.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),-120)
			plate1 = plate1.cut(box7)

			box8 = Part.makeBox(d, 4.5, 50, Vector(f-d/2,-2,0))
			box8.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),-150)
			plate1 = plate1.cut(box8)

			#왼쪽 반원 회전
			circle1 = Part.makeCylinder(d/2, t, Vector(f+12.7*2-d/2,12.7*2,0))
			plate1 = plate1.cut(circle1)

			circle2 = Part.makeCylinder(d/2, t, Vector(f+12.7*2-d/2,12.7*2,0))
			circle2.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),-30)
			plate1 = plate1.cut(circle2)

			circle3 = Part.makeCylinder(d/2, t, Vector(f+12.7*2-d/2,12.7*2,0))
			circle3.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),-60)
			plate1 = plate1.cut(circle3)

			circle4 = Part.makeCylinder(d/2, t, Vector(f+12.7*2-d/2,12.7*2,0))
			circle4.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),30)
			plate1 = plate1.cut(circle4)

			circle5 = Part.makeCylinder(d/2, t, Vector(f+12.7*2-d/2,12.7*2,0))
			circle5.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),60)
			plate1 = plate1.cut(circle5)

			#오른쪽 반원 회전
			circle6 = Part.makeCylinder(d/2, t, Vector(f+12.7*2+d/2,12.7*2,0))
			plate1 = plate1.cut(circle6)

			circle7 = Part.makeCylinder(d/2, t, Vector(f+12.7*2+d/2,12.7*2,0))
			circle7.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),-30)
			plate1 = plate1.cut(circle7)

			circle8 = Part.makeCylinder(d/2, t, Vector(f+12.7*2+d/2,12.7*2,0))
			circle8.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),-60)
			plate1 = plate1.cut(circle8)

			circle9 = Part.makeCylinder(d/2, t, Vector(f+12.7*2+d/2,12.7*2,0))
			circle9.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),30)
			plate1 = plate1.cut(circle9)

			circle10 = Part.makeCylinder(d/2, t, Vector(f+12.7*2+d/2,12.7*2,0))
			circle10.rotate(Vector(f+12.7*2,0,0),Vector(0,0,1),60)
			plate1 = plate1.cut(circle10)
			#가운데
			circle11 = Part.makeCylinder(d/2, t, Vector(f+12.7*2,12.7,0))
			plate1 = plate1.cut(circle11)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 0.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '104':
			doc=App.newDocument()

			cy1 = Part.makeCylinder(2.5,1.25,Vector(-6.0,0,5.6-1.25),Vector(0,0,1),300)
			cy2 = Part.makeCylinder(0.75,1.25,Vector(-6.0,0,5.6-1.25),Vector(0,0,1),300)
			cy1 = cy1.cut(cy2)
			cy1.rotate(Vector(-6.0,0,5.6-1.25),Vector(0,0,-1),240)

			box1 = Part.makeBox(2.4,3.5,1.25,Vector(-3.0-1.2-0.7,-1.75,5.6-1.25))
			cy1 = cy1.fuse(box1)

			cy3 = Part.makeCylinder(2.5,1.25,Vector(0,0,5.6-2.5),Vector(0,0,1),360)
			cy4 = Part.makeCylinder(0.75,1.25,Vector(0,0,5.6-1.25),Vector(0,0,1),360)
			cy3 = cy3.fuse(cy4)

			box2 = Part.makeBox(2.4,3.5,1.25,Vector(-3.0-1.2+0.7,-1.75,5.6-2.5))
			cy3 = cy3.fuse(box2)

			cy1 = cy1.fuse(cy3)
			cy2 = cy1.mirror(Vector(0,0,0),Vector(0,0,1))
			cy1 = cy1.fuse(cy2)

			cy4 = Part.makeCylinder(1.44,8.1,Vector(0,0,-4.05),Vector(0,0,1))
			cy1 = cy1.fuse(cy4)

			#Part.show(cy1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=cy1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '104a':
			doc=App.newDocument()

			cy1 = Part.makeCylinder(2.5,1.25,Vector(-6.0,0,5.6-1.25),Vector(0,0,1),300)
			cy2 = Part.makeCylinder(0.75,1.25,Vector(-6.0,0,5.6-1.25),Vector(0,0,1),300)
			cy1 = cy1.cut(cy2)
			cy1.rotate(Vector(-6.0,0,5.6-1.25),Vector(0,0,-1),240)

			box1 = Part.makeBox(2.4,3.5,1.25,Vector(-3.0-1.2-0.7,-1.75,5.6-1.25))
			cy1 = cy1.fuse(box1)

			cy3 = Part.makeCylinder(2.5,1.25,Vector(0,0,5.6-2.5),Vector(0,0,1),360)
			cy4 = Part.makeCylinder(0.75,1.25,Vector(0,0,5.6-1.25),Vector(0,0,1),360)
			cy3 = cy3.fuse(cy4)

			box2 = Part.makeBox(2.4,3.5,1.25,Vector(-3.0-1.2+0.7,-1.75,5.6-2.5))
			cy3 = cy3.fuse(box2)

			cy1 = cy1.fuse(cy3)
			cy2 = cy1.mirror(Vector(0,0,0),Vector(0,0,1))
			cy1 = cy1.fuse(cy2)

			cy4 = Part.makeCylinder(3.3,5.9,Vector(0,-2.95,0),Vector(0,1,0))
			cy1 = cy1.fuse(cy4)

			cy5 = Part.makeCylinder(2.0,5.9,Vector(0,-2.95,0),Vector(0,1,0))
			cy1 = cy1.cut(cy5)

			#Part.show(cy1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=cy1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '105':

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=2.35, z=12, alpha=20 * pi / 180., clearence=0., shift=0., beta=0., undercut=False, simple=False, height=5.8, backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                d = 4.11
			                d1 = 15.56
			                d2 = 11.4
			                d3 = 9.5
			                d4 = 3.11
			                d5 = 7.62
			                self.cir = Part.makeCylinder(d1/2,4.8,Vector(0,0,1))
			                self.cir2 = Part.makeCylinder(d2/2,4.8,Vector(0,0,1))
			                self.cir3 = Part.makeCylinder(d3/2,8.8,Vector(0,0,5.8))
			                self.cir4 = Part.makeCylinder(d/2,14.6,Vector(0,0,0))
			                self.cir5 = Part.makeCylinder(d4/2,d3,Vector(0,d3/2,d3+d4/2),Vector(0,-1,0))
			                self.cir6 = Part.makeCylinder(d5/2,0.5,Vector(0,0,0))

			                self.Shape = self.Shape.cut(self.cir)
			                self.Shape = self.Shape.fuse(self.cir2)
			                self.Shape = self.Shape.fuse(self.cir3)
			                self.Shape = self.Shape.cut(self.cir4)
			                self.Shape = self.Shape.cut(self.cir5)
			                self.Shape = self.Shape.cut(self.cir6)

			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(1.0, 0.0, 0.0)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])

			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()
		elif self.numericInput0.text() == '106':

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=2.18, z=25, alpha=20 * pi / 180., clearence=0., shift=0., beta=0., undercut=False, simple=False, height=6.36, backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                d = 4.11
			                d1 = 41.5
			                d2 = 10.8
			                d3 = 9.5
			                d4 = 3.11
			                y = 12.75
			                y1 = 17.89
			                t = 6.36-2
			                self.cir = Part.makeCylinder(d1/2,4.36,Vector(0,0,2))
			                self.cir2 = Part.makeCylinder(d2/2,5.86,Vector(0,0,2))
			                self.cir3 = Part.makeCylinder(d3/2,7.64,Vector(0,0,5.86))
			                self.cir4 = Part.makeCylinder(d/2,15.5,Vector(0,0,0))
			                self.cir_1 = Part.makeCylinder(d/2,t,Vector(y,0,0))
			                self.cir_2 = Part.makeCylinder(d/2,t,Vector(-y,0,0))
			                self.cir_3 = Part.makeCylinder(d/2,t,Vector(0,y,0))
			                self.cir_4 = Part.makeCylinder(d/2,t,Vector(0,-y,0))
			                self.cir_5 = Part.makeCylinder(d/2,t,Vector(y1/2,y1/2,0))
			                self.cir_6 = Part.makeCylinder(d/2,t,Vector(-y1/2,y1/2,0))
			                self.cir_7 = Part.makeCylinder(d/2,t,Vector(-y1/2,-y1/2,0))
			                self.cir_8 = Part.makeCylinder(d/2,t,Vector(y1/2,-y1/2,0))
			                self.cir_0 = Part.makeCylinder(d4/2,d2,Vector(0,d2/2,11),Vector(0,-1,0))
			                self.Shape = self.Shape.cut(self.cir)
			                self.Shape = self.Shape.fuse(self.cir2)
			                self.Shape = self.Shape.fuse(self.cir3)
			                self.Shape = self.Shape.cut(self.cir4)
			                self.Shape = self.Shape.cut(self.cir_1)
			                self.Shape = self.Shape.cut(self.cir_2)
			                self.Shape = self.Shape.cut(self.cir_3)
			                self.Shape = self.Shape.cut(self.cir_4)
			                self.Shape = self.Shape.cut(self.cir_5)
			                self.Shape = self.Shape.cut(self.cir_6)
			                self.Shape = self.Shape.cut(self.cir_7)
			                self.Shape = self.Shape.cut(self.cir_8)
			                self.Shape = self.Shape.cut(self.cir_0)
			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(1.0, 0.0, 0.0)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])

			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()
		elif self.numericInput0.text() == '107':
			doc=App.newDocument()

			d = 37
			t = 8.5
			d1 = 24.46
			d2 = 22.41
			h1 = 1.8
			n = 2
			i = 0

			circle = Part.makeCylinder(d/2,t,Vector(0,0,0))
			circle = circle.makeFillet((t-h1)/2,[circle.Edges[0],circle.Edges[2]])

			cir = []
			for i in range(n):
				cir.append(Part.makeCylinder(d1/2,(t-h1)/2,Vector(0,0,(t-(t-h1)/2)*i)))
			for i in cir:
				circle = circle.cut(i)

			circle1 = Part.makeCylinder(d2/2,h1,Vector(0,0,(t-h1)/2))
			circle = circle.cut(circle1)

			#Part.show(circle)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '108':

			doc=App.newDocument()

			class involute_gear_rack():
				def __init__(self, numpoints=10, m=0.65, z=67, alpha=20 * pi / 180., thickness=11, height=6.5 ):
					self.alpha = alpha
					self.thickness = thickness
					self.m = m
					self.z = z
					self.teeth = z
					self.height = height
					self.numpoints = numpoints
					self.execute()
				def execute(self):
					pts = self.points(self.numpoints)
					wire = Part.Wire(makePolygon(map(fcvec, pts)))
					face = Part.Face(wire)
					self.Shape = face.extrude(fcvec([0., 0., self.height]))
					#여기서부터 수정
					box = Part.makeBox(4.0,self.thickness*self.z,0.9,Vector(-self.m+6.8-2,-self.thickness,0))
					box2 = Part.makeBox(4.0,self.thickness*self.z,0.9,Vector(-self.m+6.8-2,-self.thickness,self.height-0.9))
					self.Shape = self.Shape.cut(box)
					self.Shape = self.Shape.cut(box2)
					cir = []
					n = 6
					for i in range(n):
						cir.append(Part.makeCylinder(4.0/2, self.height, Vector(-self.m+6.8,5.5-self.m+25.42*i,0)))
					for i in cir:
						self.Shape = self.Shape.cut(i)
					box3 = []
					for i in range(n-1):
						box3.append(Part.makeBox(4.0, 4.3, self.height, Vector(-self.m+6.8-2,16-2*self.m*tan(self.alpha)-((self.m * pi)/2-2*self.m*tan(self.alpha))/2+25.42*i,0)))
					for i in box3:
						self.Shape = self.Shape.cut(i)
					cir2 = []
					for i in range(n-1):
						cir2.append(Part.makeCylinder(4.3/2, self.height, Vector(-self.m+6.8-1.8,16-2*self.m*tan(self.alpha)-((self.m * pi)/2-2*self.m*tan(self.alpha))/2+4.3/2+25.42*i,0)))
					for i in cir2:
						self.Shape = self.Shape.cut(i)
					cir3 = []
					for i in range(n-1):
						cir3.append(Part.makeCylinder(4.3/2, self.height, Vector(-self.m+6.8+1.8,16-2*self.m*tan(self.alpha)-((self.m * pi)/2-2*self.m*tan(self.alpha))/2+4.3/2+25.42*i,0)))
					for i in cir3:
						self.Shape = self.Shape.cut(i)

					#Part.show(self.Shape)
					shape=doc.addObject("Part::Feature")
					shape.Shape=self.Shape
					doc.recompute()
					shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
					Gui.activeDocument().activeView().viewAxometric()
					Gui.SendMsgToActiveView("ViewFit")
				def points(self, num):
					a = 2 * self.m * tan(self.alpha)
					b = ((self.m * pi) / 2 - a) / 2
					tooth = [[self.m, -a - b],[-self.m, -b],[-self.m, b],[self.m, a + b]]
					tooth2 = [[self.m+self.thickness, a + b],[3*self.m+self.thickness, b],[3*self.m+self.thickness, -b],[self.m+self.thickness, -a - b]]
					teeth = [tooth]
					teeth2 = [tooth2]
					trans = translation([0., self.m * pi, 0.])
					for i in range(self.z):
						teeth.append(trans(teeth[-1]))
					#	teeth3.append(trans(teeth[-1]))
					#for i in range(self.z):
					#	teeth2.append(trans(teeth2[-1]))
					#teeth2=teeth2.reverse()
					#for i in range(self.z):
					#	teeth3.append(trans(teeth2[0]))
					teeth = list(np.vstack(teeth))#array로 변환
					for i in range(self.z):
						teeth2.append(trans(teeth2[-1]))
					teeth2 = teeth2[::-1]
					teeth2 = list(np.vstack(teeth2))
					teeth.append(teeth2)#array로 변환
					#teeth.append(list(teeth[-1])) #teeth list의 마지막 array인 [1.0, 48.....]을 list 항목의 마지막에 다시 추가
					#teeth[-1][0] += self.thickness #새로추가된 list의 마지막 항목의 x에 두께를 더함
					#teeth.append(list(teeth[-1]))
					teeth = list(np.vstack(teeth))
					teeth.append(list(teeth[0])) #teeth list의 마지막에 list로 첫번째 array인 항을 list 항목으로 추가
					#teeth[-1][0] += self.thickness
					#print(teeth)
					return(teeth)

			def fcvec(x):
				if len(x) == 2:
					return(App.Vector(x[0], x[1], 0))
				else:
					return(App.Vector(x[0], x[1], x[2]))

			def translation(vec):
				def trans(x):
					return([x[0] + vec[0], x[1] + vec[1]])
				def func(x):
					return(array(map(trans, x)))
				return(func)

			ex = involute_gear_rack()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '109':
			doc=App.newDocument()
			y=87.33
			t=0.73
			d=4.15
			l=12.46333333
			z=13.5
			i=0
			n=7
			cir1 = []
			cir2 = []
			cir3 = []
			cir6 = []
			cir7 = []
			box = []
			tri = Part.makePolygon([(0,0,0),(13.7,y,0),(59.5,y,0),(73.2,0,0),(0,0,0)])
			fa = Part.Face(tri)
			p = fa.extrude(Vector(0,0,t))

			tri2 = Part.makePolygon([(0,0,t),(0,0,z),(13.7,y,z),(13.7,y,t),(0,0,t)])
			fa = Part.Face(tri2)
			p2 = fa.extrude(Vector(t,0,0))

			for i in range(n):
					cir1.append(Part.makeCylinder(d/2,t,Vector(23.925,6.275+i*l,0)))
					cir2.append(Part.makeCylinder(d/2,t,Vector(36.6,6.275+i*l,0)))
					cir3.append(Part.makeCylinder(d/2,t,Vector(49.275,6.275+i*l,0)))
			for i in cir1:
			        p = p.cut(i)
			for i in cir2:
			        p = p.cut(i)
			for i in cir3:
			        p = p.cut(i)
			cir4 = Part.makeCylinder(d/2,t,Vector(11.25,6.275,0))
			cir5 = Part.makeCylinder(d/2,t,Vector(61.95,6.275,0))
			p = p.cut(cir4)
			p = p.cut(cir5)
			p = p.fuse(p2)
			for i in range(n):
					cir6.append(Part.makeCylinder(d/2,150,Vector(0,6.275+i*l,3+d/2),Vector(1,0,0)))
					cir7.append(Part.makeCylinder(d/2,150,Vector(0,6.275+i*l,z-3-d/2),Vector(1,0,0)))
					box.append(Part.makeBox(150,d,3.35,Vector(0,4.2+i*l,3+d/2)))

			p2 = p2.mirror(Vector(36.6,43.665,0),Vector(1,0,0))
			p = p.fuse(p2)
			for i in cir6:
					p= p.cut(i)
			for i in cir7:
					p= p.cut(i)
			for i in box:
					p= p.cut(i)
			#Part.show(p)
			shape=doc.addObject("Part::Feature")
			shape.Shape=p
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 1.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '110a':
			doc=App.newDocument()

			D = 41.77
			D1 = 59.59
			D2 = 57.57
			D3 = 53.63
			D4 = 46.60
			D5 = 37.53
			x = 0.9
			D6 = 12.60
			D7 = 8.36
			t = 1
			t1 = 2.57
			t2 = 5.73

			d = 4.11
			i = 0
			j = 0
			n = 2



			circle = Part.makeCylinder(D1/2,t1,Vector(0,0,t))

			#Front
			circle1 = Part.makeCylinder(D/2,t2-t1,Vector(0,0,t1))
			circle = circle.fuse(circle1)

			#Back
			circle_1 = Part.makeCylinder(D2/2,t,Vector(0,0,0))
			circle_2 = Part.makeCylinder(D3/2,t,Vector(0,0,0))
			circle_3 = Part.makeCylinder(D4/2,t,Vector(0,0,0))
			circle_4 = Part.makeCylinder(D5/2,t1-1,Vector(0,0,0))
			box_1 = Part.makeBox(x,D5,t1-1,Vector(-x/2,-D5/2,0))
			box_2 = Part.makeBox(D5,x,t1-1,Vector(-D5/2,-x/2,0))
			box_3 = Part.makeBox(D5,t1-1,x,Vector(-D5/2/1.414-0.3,D5/2/1.414-0.3,t1-1),Vector(1,1,0))
			box_4 = Part.makeBox(D5,t1-1,x,Vector(-D5/2/1.414+0.3,-D5/2/1.414-0.3,t1-1),Vector(-1,1,0))
			circle_5 = Part.makeCylinder(D6/2,t1-1,Vector(0,0,0))
			circle_6 = Part.makeCylinder(D7/2,t1-1,Vector(0,0,0))
			circle = circle.fuse(circle_1)
			circle = circle.cut(circle_2)
			circle = circle.fuse(circle_3)
			circle = circle.cut(circle_4)
			circle = circle.fuse(box_1)
			circle = circle.fuse(box_2)
			circle = circle.fuse(box_3)
			circle = circle.fuse(box_4)
			circle = circle.cut(circle_5)
			circle = circle.fuse(circle_5)
			circle = circle.cut(circle_6)

			x = 4.11
			y = 11.04



			#Hole
			cir = Part.makeCylinder(d/2,t2,Vector(0,0,0))
			cir1 = []
			cir2 = []
			for i in range(n):
				for j in range(n):
					cir1.append(Part.makeCylinder(d/2,t2,Vector(x-2*x*i,y-2*y*j,0)))
					cir2.append(Part.makeCylinder(d/2,t2,Vector(y-2*y*i,x-2*x*j,0)))
			for i in cir1:
				circle = circle.cut(i)
			for i in cir2:
				circle = circle.cut(i)

			#for i in range(n):
			#	for j in range(n):
			#		cir4.append(Part.makeCylinder(d/2,t,Vector((14-d)/2-(14-d)*j,(27.7-d)/2-(27.7-d)*i,0)))
			#
			#for i in cir4:
			#	circle = circle.cut(i)

			circle = circle.cut(cir)


			#Part.show(circle)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '110b':
			doc=App.newDocument()

			#D = 41.77
			D1 = 59.53
			D2 = 57.17
			D3 = 7.97
			d = 4.11
			d1 = 2.81
			x = 15.95
			t = 6.8
			t1 = 2
			t2 = 10.12

			circle = Part.makeCylinder(D1/2,t,Vector(0,0,0))
			circle1 = Part.makeCylinder(D2/2,t1,Vector(0,0,t-t1))
			circle2 = Part.makeCylinder(D2/2,t1,Vector(0,0,0))
			circle3 = Part.makeCylinder(D3/2,t2,Vector(0,0,t/2-t2/2))
			circle4 = Part.makeCylinder(d/2,t2,Vector(0,0,t/2-t2/2))
			circle5 = Part.makeCylinder(d1/2,t-2*t1,Vector(x,0,t1))
			circle6 = Part.makeCylinder(d1/2,t-2*t1,Vector(-x,0,t1))
			circle = circle.cut(circle1)
			circle = circle.cut(circle2)
			circle = circle.fuse(circle3)
			circle = circle.cut(circle4)
			circle = circle.cut(circle5)
			circle = circle.cut(circle6)

			#Part.show(circle)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '110c':

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=0.678, z=95, alpha=20 * pi / 180., clearence=0, shift=0., beta=0., undercut=False, simple=False, height=3.6, backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                H = 3.6

			                #Front
			                h1 = 1
			                D1 = 57.51
			                D2 = 53.16
			                D3 = 46.97
			                D4 = 37.43
			                D5 = 12.60
			                D6 = 8.36
			                x = 0.9
			                self.cir_f1 = Part.makeCylinder(D1/2,h1,Vector(0,0,H))
			                self.cir_f2 = Part.makeCylinder(D2/2,h1,Vector(0,0,H))
			                self.cir_f3 = Part.makeCylinder(D3/2,h1,Vector(0,0,H))
			                self.cir_f4 = Part.makeCylinder(D4/2,H,Vector(0,0,1))
			                self.Shape = self.Shape.fuse(self.cir_f1)
			                self.Shape = self.Shape.cut(self.cir_f2)
			                self.Shape = self.Shape.fuse(self.cir_f3)
			                self.Shape = self.Shape.cut(self.cir_f4)
			                self.box_f1 = Part.makeBox(x,D4,H,Vector(-x/2,-D4/2,1))
			                self.box_f2 = Part.makeBox(D4,x,H,Vector(-D4/2,-x/2,1))
			                self.box_f3 = Part.makeBox(D4,H,x,Vector(-D4/2+5.424,D4/2-5.424,H+h1),Vector(1,1,0))
			                self.box_f4 = Part.makeBox(D4,H,x,Vector(-D4/2+5.424,-D4/2+5.424,H+h1),Vector(-1,1,0))
			                self.Shape = self.Shape.fuse(self.box_f1)
			                self.Shape = self.Shape.fuse(self.box_f2)
			                self.Shape = self.Shape.fuse(self.box_f3)
			                self.Shape = self.Shape.fuse(self.box_f4)
			                self.cir_f5 = Part.makeCylinder(D5/2,H,Vector(0,0,1))
			                self.cir_f6 = Part.makeCylinder(D6/2,H,Vector(0,0,1))
			                self.Shape = self.Shape.cut(self.cir_f5)
			                self.Shape = self.Shape.fuse(self.cir_f5)
			                self.Shape = self.Shape.cut(self.cir_f6)

			                #Back
			                D_1 = 59.7
			                D_2 = 42.22
			                h_1 = 5.63
			                self.cir_b1 = Part.makeCylinder(D_1/2,h_1-H,Vector(0,0,0))
			                self.cir_b2 = Part.makeCylinder(D_2/2,h_1-H+1,Vector(0,0,-1))
			                self.Shape = self.Shape.cut(self.cir_b1)
			                self.Shape = self.Shape.fuse(self.cir_b2)

			                #Hole
			                hx = 4.11
			                hy = 11.04
			                d = 4.11
			                self.cir_h = Part.makeCylinder(d/2,h_1,Vector(0,0,-1))
			                self.cir_h1 = Part.makeCylinder(d/2,h_1,Vector(hx,hy,-1))
			                self.cir_h2 = Part.makeCylinder(d/2,h_1,Vector(-hx,hy,-1))
			                self.cir_h3 = Part.makeCylinder(d/2,h_1,Vector(-hx,-hy,-1))
			                self.cir_h4 = Part.makeCylinder(d/2,h_1,Vector(hx,-hy,-1))
			                self.cir_h5 = Part.makeCylinder(d/2,h_1,Vector(hy,hx,-1))
			                self.cir_h6 = Part.makeCylinder(d/2,h_1,Vector(-hy,hx,-1))
			                self.cir_h7 = Part.makeCylinder(d/2,h_1,Vector(-hy,-hx,-1))
			                self.cir_h8 = Part.makeCylinder(d/2,h_1,Vector(hy,-hx,-1))
			                self.Shape = self.Shape.cut(self.cir_h)
			                self.Shape = self.Shape.cut(self.cir_h1)
			                self.Shape = self.Shape.cut(self.cir_h2)
			                self.Shape = self.Shape.cut(self.cir_h3)
			                self.Shape = self.Shape.cut(self.cir_h4)
			                self.Shape = self.Shape.cut(self.cir_h5)
			                self.Shape = self.Shape.cut(self.cir_h6)
			                self.Shape = self.Shape.cut(self.cir_h7)
			                self.Shape = self.Shape.cut(self.cir_h8)


			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])


			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()
			Gui.SendMsgToActiveView("ViewFit")

		elif self.numericInput0.text() == '111':
			doc=App.newDocument()

			h1 = 3.52
			y1 = 12.7
			x1 = 14.4
			f = 1
			t = 0.7
			D = 9.5
			d = 4.11
			d1 = 3.11
			h2 = 5
			H = 14.6-2*h1

			plate=Part.makeBox(x1,y1,h1,Vector(-x1/2,-y1/2,0))
			plate1=Part.makeBox(y1,y1,h1,Vector(-y1/2,-y1/2,h1))
			plate2=Part.makeBox(x1-2*t,y1,h1-2*t,Vector(-x1/2+t,-y1/2,t))
			plate3=Part.makeBox(y1-2*t,y1,2*h1-t,Vector(-y1/2+t,-y1/2,0))
			plate=plate.makeFillet(f,[plate.Edges[1],plate.Edges[3],plate.Edges[5],plate.Edges[7]])
			plate1=plate1.makeFillet(f,[plate1.Edges[1],plate1.Edges[5]])
			plate2=plate2.makeFillet(f-t/2,[plate2.Edges[1],plate2.Edges[3],plate2.Edges[5],plate2.Edges[7]])
			plate3=plate3.makeFillet(f-t/2,[plate3.Edges[1],plate3.Edges[5]])
			plate=plate.fuse(plate1)
			plate=plate.cut(plate2)
			plate=plate.cut(plate3)

			circle=Part.makeCylinder(D/2,H,Vector(0,0,2*h1))
			circle1=Part.makeCylinder(d/2,H+t,Vector(0,0,2*h1-t))
			circle2=Part.makeCylinder(d1/2,D,Vector(0,-D/2,2*h1+h2),Vector(0,1,0))
			plate=plate.fuse(circle)
			plate=plate.cut(circle1)
			plate=plate.cut(circle2)
			#Part.show(plate)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '112':
			doc=App.newDocument()

			D = 9.5
			l = 20
			d = 4.11
			d1 = 3.33
			i = 0
			n = 2

			cir = Part.makeCylinder(D/2,l,Vector(0,0,0))
			cir1 = Part.makeCylinder(d/2,l,Vector(0,0,0))
			cir = cir.cut(cir1)

			hole=[]
			for i in range(n):
				hole.append(Part.makeCylinder(d1/2,100,Vector(0,D,(D+d)*i+1.5+d/2),Vector(0,-1,0)))

			for i in hole:
				cir = cir.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=cir
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '127':
			doc=App.newDocument()
			v=12.7
			x=316.5
			t=1
			r=6.35
			n=25
			a=12.5
			f=(x-a*(n-1))/2 #6.5
			i=0
			d=4.1

			plate1=Part.makeBox(x,v,t,Vector(0,0,0))
			plate1=plate1.makeFillet(r-0.01,[plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir=[]
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(f+a*i,r,0)))
			for i in cir:
				plate1=plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '128':
			doc=App.newDocument()

			x = 315.8
			y = 50.8
			t = 0.68
			d = 4.11
			f = 6.35
			n = 25
			n1 = 3
			n2 = 2
			i = 0
			j = 0
			l = 42
			l1 = 46
			w = 25
			plate1 = Part.makeBox(x,y,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir = []
			cir1 = []
			for i in range(n):
				for j in range(n2):
					cir.append(Part.makeCylinder(d/2,t,Vector(((x-(d+4*2))/(n-1))*i+4+d/2,j*(y-(d+4*2))+4+d/2,0)))
			for i in range(n1):
				for j in range(n1):
					cir1.append(Part.makeCylinder(d/2,t,Vector(((x-(d+4*2))/(n-1))*(n-1)*j/2+4+d/2,((16.64-d)/(n1-1))*i+17.1+d/2,0)))
			for i in cir:
				plate1 = plate1.cut(i)
			for i in cir1:
				plate1 = plate1.cut(i)

			box = []
			box1 = []
			box2 = []
			for i in range(n2):
				box1.append(Part.makeBox(l1,w,t,Vector((y-w)/2+47+152*i,(y-w)/2,0)))
				for j in range(n2):
					box.append(Part.makeBox(l,w,t,Vector((y-w)/2+152*i+98*j,(y-w)/2,0)))
			for i in box:
				plate1 = plate1.cut(i)
			for i in box1:
				plate1 = plate1.cut(i)

			tri = Part.makePolygon([((y-w)/2,(y-w)/2+w,0),((y-w)/2+l-7,(y-w)/2,0),((y-w)/2+l,(y-w)/2,0),((y-w)/2+7,(y-w)/2+w,0),((y-w)/2,(y-w)/2+w,0)])
			fa = Part.Face(tri)
			p = fa.extrude(Vector(0,0,t))
			plate1 = plate1.fuse(p)
			tri1 = Part.makePolygon([((y-w)/2+98,(y-w)/2+w,0),((y-w)/2+l-7+98,(y-w)/2,0),((y-w)/2+l+98,(y-w)/2,0),((y-w)/2+7+98,(y-w)/2+w,0),((y-w)/2+98,(y-w)/2+w,0)])
			fa1 = Part.Face(tri1)
			p1 = fa1.extrude(Vector(0,0,t))
			plate1 = plate1.fuse(p1)
			tri2 = Part.makePolygon([((y-w)/2+199,(y-w)/2+w,0),((y-w)/2+l1-7+199,(y-w)/2,0),((y-w)/2+l1+199,(y-w)/2,0),((y-w)/2+7+199,(y-w)/2+w,0),((y-w)/2+199,(y-w)/2+w,0)])
			fa2 = Part.Face(tri2)
			p2 = fa2.extrude(Vector(0,0,t))
			plate1 = plate1.fuse(p2)

			tri3 = Part.makePolygon([((y-w)/2+47,(y-w)/2,0),((y-w)/2+47+7,(y-w)/2,0),((y-w)/2+47+l1,(y-w)/2+w,0),((y-w)/2+47+l1-7,(y-w)/2+w,0),((y-w)/2+47,(y-w)/2,0)])
			fa3 = Part.Face(tri3)
			p3 = fa3.extrude(Vector(0,0,t))
			plate1 = plate1.fuse(p3)
			tri4 = Part.makePolygon([((y-w)/2+47+105,(y-w)/2,0),((y-w)/2+47+7+105,(y-w)/2,0),((y-w)/2+47+l+105,(y-w)/2+w,0),((y-w)/2+47+l-7+105,(y-w)/2+w,0),((y-w)/2+47+105,(y-w)/2,0)])
			fa4 = Part.Face(tri4)
			p4 = fa4.extrude(Vector(0,0,t))
			plate1 = plate1.fuse(p4)
			tri5 = Part.makePolygon([((y-w)/2+47+203,(y-w)/2,0),((y-w)/2+47+7+203,(y-w)/2,0),((y-w)/2+47+l+203,(y-w)/2+w,0),((y-w)/2+47+l-7+203,(y-w)/2+w,0),((y-w)/2+47+203,(y-w)/2,0)])
			fa5 = Part.Face(tri5)
			p5 = fa5.extrude(Vector(0,0,t))
			plate1 = plate1.fuse(p5)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '129':
			doc=App.newDocument()

			x = 63.5
			y = 38.1
			t = 0.7
			d = 4.2
			n = 5
			m = 3
			f = 6
			i = 0
			j = 0
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			cir = []

			for j in range(m):
				for i in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-cc-a*j,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 1.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '130':
			doc=App.newDocument()

			x=85.5
			y=43.5
			t=0.7
			f=6.35
			d=4.2
			i=0
			j=1
			n=5
			n2=3

			cir = []
			cir2 = []
			tri = Part.makePolygon([(0,0,0),(x,0,0),(x,y,0),(0,0,0)])
			fa = Part.Face(tri)
			p = fa.extrude(Vector(0,0,t))
			p = p.makeFillet(f, [p.Edges[0],p.Edges[1],p.Edges[4]])

			for i in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(78.15-2*f*i,6.35,0)))

			for j in range(n2):
					cir2.append(Part.makeCylinder(d/2,t,Vector(78.15,6.35+2*f*j,0)))

			for i in cir:
			        p = p.cut(i)

			for j in cir2:
			        p = p.cut(j)

			cir3 = Part.makeCylinder(d/2,t,Vector(78.15-2*f*2,6.35+2*f,0))
			cir4 = Part.makeCylinder(d/2,t,Vector(27.35+16.3*0.8944,6.35+16.3*0.4472,0))
			cir5 = Part.makeCylinder(d/2,t,Vector(27.35+(16.3+4.1)*0.8944,6.35+(16.3+4.1)*0.4472,0))
			cir6 = Part.makeCylinder(d/2,t,Vector(78.15-2*f*2+8.15*0.8944,6.35+2*f+8.15*0.4472,0))
			cir7 = Part.makeCylinder(d/2,t,Vector(78.15-2*f*2+(8.15+12.6)*0.8944,6.35+2*f+(8.15+12.6)*0.4472,0))
			box = Part.makeBox(4.2,0.7,4.1, Vector(27.35+16.3*0.8944+2.1*0.4472,6.35+16.3*0.4472-2.1*0.8944,0), Vector(0.8944,0.4472,0))
			box1 = Part.makeBox(4.2,0.7,12.6, Vector(78.15-2*f*2+8.15*0.8944+2.1*0.4472,6.35+2*f+8.15*0.4472-2.1*0.8944,0), Vector(0.8944,0.4472,0))

			p=p.cut(cir3)
			p=p.cut(cir4)
			p=p.cut(cir5)
			p=p.cut(cir6)
			p=p.cut(cir7)
			p=p.cut(box)
			p=p.cut(box1)

			#Part.show(p)
			shape=doc.addObject("Part::Feature")
			shape.Shape=p
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '131':
			doc=App.newDocument()

			l=63.5
			t=0.85
			d=4.11
			R=6.35
			i=0
			j=0
			n=4
			n1=2
			n2=3

			v1=Vector(0,0,0)
			v2=Vector((l-13.5)/2,0,0)
			v3=Vector(l,(l+13.5)/2,0)
			v4=Vector(l,l,0)
			v5=Vector(0,l,0)


			Arc1=Part.makeCircle((l+13.5)/2,Vector(l,0,0),Vector(0,0,1),90,180)
			Line1=Part.makeLine(v1,v2)
			Line2=Part.makeLine(v3,v4)
			Line3=Part.makeLine(v4,v5)
			Line4=Part.makeLine(v5,v1)
			Sket=Arc1.fuse(Line1)
			Sket=Sket.fuse(Line2)
			Sket=Sket.fuse(Line3)
			Sket=Sket.fuse(Line4)
			W=Part.Wire(Sket.Edges)
			face=Part.Face(W)
			P=face.extrude(Vector(0,0,t))
			P = P.makeFillet(R, [P.Edges[0],P.Edges[1],P.Edges[4],P.Edges[7],P.Edges[10]])

			cir=[]
			cir1=[]
			cir2=[]
			cir3=[]
			for i in range(n):
				for j in range(n1):
					cir.append(Part.makeCylinder(d/2,t,Vector(R+(17-d)*i,l-R-(17-d)*j,0)))
					cir1.append(Part.makeCylinder(d/2,t,Vector(R+(17-d)*j,l-R-(17-d)*i,0)))
					cir2.append(Part.makeCylinder(d/2,t,Vector(R+(17-d)*j,R,0)))
					cir3.append(Part.makeCylinder(d/2,t,Vector(l-R,l-R-(17-d)*j,0)))
			cir4=Part.makeCylinder(d/2,t,Vector(25.5,l-25.5,0))


			for i in cir:
				P = P.cut(i)
			for i in cir1:
				P = P.cut(i)
			for i in cir2:
				P = P.cut(i)
			for i in cir3:
				P = P.cut(i)
			P=P.cut(cir4)

			shape=doc.addObject("Part::Feature")
			shape.Shape=P
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 1.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '132':
			doc=App.newDocument()

			l = 24.7
			w = 15.0
			h = 13.5
			t = 0.7
			d = 4.11
			n = 2
			b = n-1

			box = []
			cir = []
			mir = []
			hole = []
			plate1 = Part.makeBox(l,w,t,Vector(0,-w,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(w/2, [plate1.Edges[0],plate1.Edges[4]])
			box1 = Part.makeBox(d,5,t,Vector(6-d/2,-10,0))
			box2 = Part.makeBox(d,5,t,Vector(6+l-12.0-d/2,-10,0))
			cir1 = Part.makeCylinder(d/2,t,Vector(6,-10,0))
			mir1 = Part.makeCylinder(d/2,t,Vector(6,-5,0))
			cir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-10,0))
			mir2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-5,0))
			for i in range(1,b):
				box.append(Part.makeBox(d,5,t,Vector(6+(l-12.0)/b*i-d/2,-10,0)))
				cir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-10,0)))
				mir.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-5,0)))

			plate1 = plate1.cut(box1)
			plate1 = plate1.cut(box2)
			plate1 = plate1.cut(cir1)
			plate1 = plate1.cut(mir1)
			plate1 = plate1.cut(cir2)
			plate1 = plate1.cut(mir2)

			#print(len(box))
			#print(list(range(1,b)))
			#print(box[22])
			for i in box:
				plate1 = plate1.cut(i)
			for i in cir:
				plate1 = plate1.cut(i)
			for i in mir:
				plate1 = plate1.cut(i)

			plate2 = Part.makeBox(l,t,h-t,Vector(0,-t,t))
			plate2 = plate2.makeFillet(h/2, [plate2.Edges[1],plate2.Edges[5]])
			hole1 = Part.makeCylinder(d/2,t,Vector(6,-t,7),Vector(0,1,0))
			hole2 = Part.makeCylinder(d/2,t,Vector(6+l-12.0,-t,7),Vector(0,1,0))
			for i in range(1,b):
				hole.append(Part.makeCylinder(d/2,t,Vector(6+(l-12.0)/b*i,-t,7),Vector(0,1,0)))

			plate2 = plate2.cut(hole1)
			plate2 = plate2.cut(hole2)
			for i in hole:
				plate2 = plate2.cut(i)

			plate1 = plate1.fuse(plate2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '133':
			doc=App.newDocument()

			x = 36.5
			y = 12.8
			t = 1.20
			h = 17.9
			d = 4.2

			plate1 = Part.makeBox(x,y,t,Vector(0,0,0))
			plate1 = plate1.makeFillet(y/2-0.001, [plate1.Edges[0],plate1.Edges[2], plate1.Edges[4],plate1.Edges[6]])
			plate2 = Part.makeBox(y,y,t,Vector(11.85,12.8,0),Vector(0,0,1))
			plate2 = plate2.makeFillet(y/2-0.001, [plate2.Edges[2],plate2.Edges[6]])
			plate1 = plate1.fuse(plate2)
			plate3 = Part.makeBox(y,t,h,Vector (11.8,0,0),Vector(0,0,1))
			plate1 = plate1.fuse(plate3)
			plate4 = Part.makeBox(y,11.5,t,Vector(11.8,0,h-t),Vector(0,0,1))
			plate4 = plate4.makeFillet(y/2-0.001, [plate4.Edges[2],plate4.Edges[6]])
			plate1 = plate1.fuse(plate4)

			cir1 = Part.makeCylinder(d/2,t,Vector(5.6,y/2,0))
			cir2 = Part.makeCylinder(d/2,t,Vector(x/2,y/2,0))
			cir3 = Part.makeCylinder(d/2,t,Vector(36.5-5.6,y/2,0))
			cir4 = Part.makeCylinder(d/2,t,Vector(x/2,18.9,0))
			cir5 = Part.makeCylinder(d/2,t,Vector(x/2,y/2,h-t))
			cir6 = Part.makeCylinder(d/2,t,Vector(x/2,0,h/2), Vector(0,1,0))

			plate1 = plate1.cut(cir1)
			plate1 = plate1.cut(cir2)
			plate1 = plate1.cut(cir3)
			plate1 = plate1.cut(cir4)
			plate1 = plate1.cut(cir5)
			plate1 = plate1.cut(cir6)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '134':
			doc=App.newDocument()

			x = 63.6
			y = 63.6
			r = 6.4
			t = 0.41
			d = 4.2
			n = 5
			m = 5
			b = n-1
			p = m-1
			a=12.5
			bb=(x-a*(n-1))/2 #6.5
			cc=(y-a*(m-1))/2 #6.5
			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(r, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

			hole1 = Part.makeCylinder(d/2,t,Vector(x/2,-y/2,0))
			hole_up = []
			hole_down = []
			for i in range(n):
				hole_up.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,-25-y/2,0)))
				hole_down.append(Part.makeCylinder(d/2,t,Vector(bb+a*i,25-y/2,0)))
			plate1 = plate1.cut(hole1)
			for i in hole_up:
				plate1 = plate1.cut(i)
			for i in hole_down:
				plate1 = plate1.cut(i)

			left = []
			right = []
			box = []
			left2 = []
			right2 = []
			box2 = []
			for i in range(m):
				box.append(Part.makeBox(5,d,t,Vector(4.5,-cc-a*i-d/2,0)))
				left.append(Part.makeCylinder(d/2,t,Vector(bb-2.5,-cc-a*i,0)))
				right.append(Part.makeCylinder(d/2,t,Vector(bb+2.5,-cc-a*i,0)))
			for i in range(m):
				box2.append(Part.makeBox(5,d,t,Vector(x-bb-2.5,-cc-a*i-d/2,0)))
				left2.append(Part.makeCylinder(d/2,t,Vector(x-bb-2.5,-cc-a*i,0)))
				right2.append(Part.makeCylinder(d/2,t,Vector(x-bb+2.5,-cc-a*i,0)))
			for i in left:
				plate1 = plate1.cut(i)
			for i in right:
				plate1 = plate1.cut(i)
			for i in box:
				plate1 = plate1.cut(i)
			for i in left2:
				plate1 = plate1.cut(i)
			for i in right2:
				plate1 = plate1.cut(i)
			for i in box2:
				plate1 = plate1.cut(i)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '137':
			doc=App.newDocument()

			plate1 = Part.makeCylinder(1.98, 54, Vector(0,0,0))
			box1 = Part.makeBox(1.92,5.24,54,Vector(-0.96,-2.62,0))
			plate1 = plate1.fuse(box1)
			box2 = Part.makeBox(1.92,5.24,54,Vector(-0.96,-2.62,0))
			box2.rotate(Vector(0,0,0),Vector(0,0,1),90)
			plate1 = plate1.fuse(box2)

			#Part.show(plate1)
			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '138':
			doc=App.newDocument()

			R1 = 7.0
			H = 3.45
			H_f1 = 2.3
			H_f2 = 0.8
			D1 = 3.0

			base1 = Part.makeCylinder(R1,H*2,Vector(0,-H,0),Vector(0,1,0),360)

			tri = Part.makePolygon([(R1-(H_f1-H_f2)*sqrt(3),0,0),(R1,-H_f1+H_f2,0),(R1,H_f1-H_f2,0),(R1-(H_f1-H_f2)*sqrt(3),0,0)])
			face = Part.Face(tri)
			solid = face.revolve(Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.cut(solid)

			tri1 = Part.makePolygon([(R1-(H_f1-H_f2)*sqrt(3),3.45,0),(R1,3.45-H_f1+H_f2,0),(R1,3.45+H_f1-H_f2,0),(R1-(H_f1-H_f2)*sqrt(3),3.45,0)])
			face1 = Part.Face(tri1)
			solid1 = face1.revolve(Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.cut(solid1)

			tri2 = Part.makePolygon([(R1-(H_f1-H_f2)*sqrt(3),-3.45,0),(R1,-3.45-H_f1+H_f2,0),(R1,H_f1-H_f2-3.45,0),(R1-(H_f1-H_f2)*sqrt(3),-3.45,0)])
			face2 = Part.Face(tri2)
			solid2 = face2.revolve(Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.cut(solid2)

			base3 = Part.makeCylinder(5.0,H_f2+10,Vector(0,H_f1,0),Vector(0,1,0),360)
			base4 = Part.makeCylinder(3.9,H_f2+10,Vector(0,H_f1,0),Vector(0,1,0),360)
			base3 = base3.cut(base4)
			base1 = base1.cut(base3)

			base5 = Part.makeCylinder(5.0,H_f2+10,Vector(0,-H_f1,0),Vector(0,-1,0),360)
			base6 = Part.makeCylinder(3.9,H_f2+10,Vector(0,-H_f1,0),Vector(0,-1,0),360)
			base5 = base5.cut(base6)
			base1 = base1.cut(base5)

			base2 = Part.makeBox(3.0,3.0,50,Vector(-1.5,-25,-1.5),Vector(0,1,0))
			base1 = base1.cut(base2)

			#Part.show(base1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=base1
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '139':
			doc=App.newDocument()

			D = 8
			t = 6
			d = 4.48
			f = 0.5

			circle = Part.makeCylinder(D/2,t,Vector(0,0,0))
			circle = circle.makeFillet(f,[circle.Edges[0],circle.Edges[2]])
			circle1 = Part.makeCylinder(d/2,t,Vector(0,0,0))
			circle = circle.cut(circle1)

			#Part.show(circle)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '140':

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=0.68, z=58, alpha=20 * pi / 180., clearence=0, shift=0., beta=0., undercut=False, simple=False, height=5.25, backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                self.m_n = 0.73
			                self.z = 19
			                self.height = 6.6
			                self.m = self.m_n / cos(self.beta)
			                self.c = self.clearence * self.m_n
			                self.midpoint = [0., 0]
			                self.d = self.z * self.m
			                self.dw = self.m * self.z
			                self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			                self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			                self.dg = self.d * cos(self.alpha_t)
			                self.phipart = 2 * pi / self.z
			                self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			                self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			                self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			                self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			                self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot = self.involute_rot1 + self.involute_rot2
			                self.involute_start = 0.
			                if self.dg <= self.df:
			                    self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg

			                pts = self.points(self.numpoints)
			                if not self.simple:
			                    wi = []
			                    for i in pts:
			                        out = BSplineCurve()
			                        out.interpolate(map(fcvec, i))
			                        wi.append(out)
			                    s = Wire(Shape(wi).Edges)
			                    wi = []
			                    for i in range(self.z):
			                        rot = App.Matrix()
			                        rot.rotateZ(-i * self.phipart)
			                        tooth_rot = s.transformGeometry(rot)
			                        if i != 0:
			                            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                            pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                            wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                        wi.append(tooth_rot)
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                    wi = Wire(wi)
			                    self.Shapea = wi
			                    if self.beta == 0:
			                        sh = Face(wi)
			                        self.Shapea = sh.extrude(App.Vector(0, 0, self.height))
			                        self.Shapea.translate(Vector(0,0,5.7))
			                    self.Shape = self.Shape.fuse(self.Shapea)

			                cy1 = Part.makeCylinder(16.8,5,Vector(0,0,1.5))
			                cy2 = Part.makeCylinder(7.8,5,Vector(0,0,1.5))
			                cy1 = cy1.cut(cy2)
			                self.Shape = self.Shape.cut(cy1)
			                cy3 = Part.makeCylinder(7.5,0.75,Vector(0,0,5.25))
			                self.Shape = self.Shape.fuse(cy3)
			                cy4 = Part.makeCylinder(3.85,13.5,Vector(0,0,-1))
			                self.Shape = self.Shape.fuse(cy4)

			                cir1 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                self.Shape = self.Shape.cut(cir1)
			                cir2 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir2.rotate(Vector(0,0,0),Vector(0,0,1),45)
			                self.Shape = self.Shape.cut(cir2)
			                cir3 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir3.rotate(Vector(0,0,0),Vector(0,0,1),90)
			                self.Shape = self.Shape.cut(cir3)
			                cir4 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir4.rotate(Vector(0,0,0),Vector(0,0,1),135)
			                self.Shape = self.Shape.cut(cir4)
			                cir5 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir5.rotate(Vector(0,0,0),Vector(0,0,1),180)
			                self.Shape = self.Shape.cut(cir5)
			                cir6 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir6.rotate(Vector(0,0,0),Vector(0,0,1),225)
			                self.Shape = self.Shape.cut(cir6)
			                cir7 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir7.rotate(Vector(0,0,0),Vector(0,0,1),270)
			                self.Shape = self.Shape.cut(cir7)
			                cir8 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir8.rotate(Vector(0,0,0),Vector(0,0,1),315)
			                self.Shape = self.Shape.cut(cir8)

			                base1 = Part.makeCylinder(4.75,7.7,Vector(0,0,12.3),Vector(0,0,1))
			                self.Shape = self.Shape.fuse(base1)

			                base2 = Part.makeCylinder(2.0,50,Vector(0,0,-12.3),Vector(0,0,1))
			                self.Shape = self.Shape.cut(base2)

			                outC=Part.makeCylinder(3.29/2,50,Vector(-25,0,16.0),Vector(1,0,0))

			                self.Shape=self.Shape.cut(outC)

			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])


			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '141':

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=0.67, z=58, alpha=20 * pi / 180., clearence=0, shift=0., beta=0., undercut=False, simple=False, height=4.95, backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                self.m_n = 0.64
			                self.z = 19
			                self.height = 6.0
			                self.m = self.m_n / cos(self.beta)
			                self.c = self.clearence * self.m_n
			                self.midpoint = [0., 0]
			                self.d = self.z * self.m
			                self.dw = self.m * self.z
			                self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			                self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			                self.dg = self.d * cos(self.alpha_t)
			                self.phipart = 2 * pi / self.z
			                self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			                self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			                self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			                self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			                self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			                self.involute_rot = self.involute_rot1 + self.involute_rot2
			                self.involute_start = 0.
			                if self.dg <= self.df:
			                    self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg

			                pts = self.points(self.numpoints)
			                if not self.simple:
			                    wi = []
			                    for i in pts:
			                        out = BSplineCurve()
			                        out.interpolate(map(fcvec, i))
			                        wi.append(out)
			                    s = Wire(Shape(wi).Edges)
			                    wi = []
			                    for i in range(self.z):
			                        rot = App.Matrix()
			                        rot.rotateZ(-i * self.phipart)
			                        tooth_rot = s.transformGeometry(rot)
			                        if i != 0:
			                            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                            pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                            wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                        wi.append(tooth_rot)
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                    wi = Wire(wi)
			                    self.Shapea = wi
			                    if self.beta == 0:
			                        sh = Face(wi)
			                        self.Shapea = sh.extrude(App.Vector(0, 0, self.height))
			                        self.Shapea.translate(Vector(0,0,5.7))
			                    self.Shape = self.Shape.fuse(self.Shapea)


			                cy1 = Part.makeCylinder(16.8,5,Vector(0,0,1.5))
			                cy2 = Part.makeCylinder(7.8,5,Vector(0,0,1.5))
			                cy1 = cy1.cut(cy2)
			                self.Shape = self.Shape.cut(cy1)
			                cy3 = Part.makeCylinder(7.5,0.75,Vector(0,0,4.95))
			                self.Shape = self.Shape.fuse(cy3)
			                cy4 = Part.makeCylinder(3.85,13.5,Vector(0,0,-1))
			                self.Shape = self.Shape.fuse(cy4)
			                cy5 = Part.makeCylinder(4.5,13.5,Vector(0,0,9.5))
			                cy5 = cy5.cut(cy4)
			                self.Shape = self.Shape.cut(cy5)

			                plate1 = Part.makeCylinder(1.98, 54, Vector(0,0,-2))
			                box1 = Part.makeBox(1.92,5.24,54,Vector(-0.96,-2.62,-2))
			                plate1 = plate1.fuse(box1)
			                box2 = Part.makeBox(1.92,5.24,54,Vector(-0.96,-2.62,-2))
			                box2.rotate(Vector(0,0,0),Vector(0,0,1),90)
			                plate1 = plate1.fuse(box2)
			                self.Shape = self.Shape.cut(plate1)

			                cir1 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                self.Shape = self.Shape.cut(cir1)
			                cir2 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir2.rotate(Vector(0,0,0),Vector(0,0,1),45)
			                self.Shape = self.Shape.cut(cir2)
			                cir3 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir3.rotate(Vector(0,0,0),Vector(0,0,1),90)
			                self.Shape = self.Shape.cut(cir3)
			                cir4 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir4.rotate(Vector(0,0,0),Vector(0,0,1),135)
			                self.Shape = self.Shape.cut(cir4)
			                cir5 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir5.rotate(Vector(0,0,0),Vector(0,0,1),180)
			                self.Shape = self.Shape.cut(cir5)
			                cir6 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir6.rotate(Vector(0,0,0),Vector(0,0,1),225)
			                self.Shape = self.Shape.cut(cir6)
			                cir7 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir7.rotate(Vector(0,0,0),Vector(0,0,1),270)
			                self.Shape = self.Shape.cut(cir7)
			                cir8 = Part.makeCylinder(2.0,50,Vector(12,-2.0,0))
			                cir8.rotate(Vector(0,0,0),Vector(0,0,1),315)
			                self.Shape = self.Shape.cut(cir8)

			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])


			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '142':

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=0.637, z=19, alpha=20 * pi / 180., clearence=0, shift=0., beta=0., undercut=False, simple=False, height=5.88, backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정

			                x =5.47
			                y = 2
			                h = 7
			                h1 = 5.88
			                D = 8.77
			                D1 = 6.68
			                self.box = Part.makeBox(x,y,h,Vector(-x/2,-y/2,-(h-h1)/2))
			                self.box1 = Part.makeBox(y,x,h,Vector(-y/2,-x/2,-(h-h1)/2))
			                self.cir1 = Part.makeCylinder(D/2,(h-h1)/2,Vector(0,0,h1))
			                self.cir2 = Part.makeCylinder(D1/2,(h-h1)/2,Vector(0,0,h1))
			                self.cir3 = Part.makeCylinder(D/2,(h-h1)/2,Vector(0,0,-(h-h1)/2))
			                self.cir5 = Part.makeCylinder(D1/2,(h-h1)/2,Vector(0,0,-(h-h1)/2))

			                self.Shape = self.Shape.fuse(self.cir1)
			                self.Shape = self.Shape.fuse(self.cir3)
			                self.Shape = self.Shape.cut(self.box)
			                self.Shape = self.Shape.cut(self.box1)
			                self.Shape = self.Shape.cut(self.cir2)
			                self.Shape = self.Shape.cut(self.cir2)
			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(1.0, 0.89, 0.0)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])


			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '143':

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=2.05, z=12, alpha=20 * pi / 180., clearence=0., shift=0., beta=0., undercut=False, simple=False, height=5.8, backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                d = 4.11
			                d1 = 17.2
			                d2 = 7.96
			                l = 5.43
			                self.cir = Part.makeCylinder(d1/2,4.8,Vector(0,0,1))
			                self.cir2 = Part.makeCylinder(d2/2,11.7,Vector(0,0,-1))
			                self.box = Part.makeBox(l/2,l,11.7,Vector(-l/4,-l/2,-1))
			                self.box1 = Part.makeBox(l,l/2,11.7,Vector(-l/2,-l/4,-1))
			                self.Shape = self.Shape.cut(self.cir)
			                self.Shape = self.Shape.fuse(self.cir2)
			                self.Shape = self.Shape.cut(self.box)
			                self.Shape = self.Shape.cut(self.box1)

			                #Part.show(self.Shape) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])

			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()
		elif self.numericInput0.text() == '144':
			doc=App.newDocument()

			R1 = 28.4
			R3 = 2.0
			H_f1 = 3.0
			H_f2 = 1.0

			base1 = Part.makeCylinder(R1,H_f1*2,Vector(0,-H_f1,0),Vector(0,1,0),360)

			tri = Part.makePolygon([(R1-(H_f1-H_f2)*sqrt(3),0,0),(R1,-H_f1+H_f2,0),(R1,H_f1-H_f2,0),(R1-(H_f1-H_f2)*sqrt(3),0,0)])
			face = Part.Face(tri)
			angle = 360
			solid = face.revolve(Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.cut(solid)

			cir1 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			base1 = base1.cut(cir1)
			cir2 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir2.rotate(Vector(0,0,0),Vector(0,1,0),45)
			base1 = base1.cut(cir2)
			cir3 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir3.rotate(Vector(0,0,0),Vector(0,1,0),90)
			base1 = base1.cut(cir3)
			cir4 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir4.rotate(Vector(0,0,0),Vector(0,1,0),135)
			base1 = base1.cut(cir4)
			cir5 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir5.rotate(Vector(0,0,0),Vector(0,1,0),180)
			base1 = base1.cut(cir5)
			cir6 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir6.rotate(Vector(0,0,0),Vector(0,1,0),225)
			base1 = base1.cut(cir6)
			cir7 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir7.rotate(Vector(0,0,0),Vector(0,1,0),270)
			base1 = base1.cut(cir7)
			cir8 = Part.makeCylinder(2.1,50,Vector(12,-25.0,0),Vector(0,1,0))
			cir8.rotate(Vector(0,0,0),Vector(0,1,0),315)
			base1 = base1.cut(cir8)

			acir1 = Part.makeCylinder(2.1,50,Vector(18.0,-25.0,0),Vector(0,1,0))
			base1 = base1.cut(acir1)
			acir3 = Part.makeCylinder(2.1,50,Vector(18.0,-25.0,0),Vector(0,1,0))
			acir3.rotate(Vector(0,0,0),Vector(0,1,0),90)
			base1 = base1.cut(acir3)
			acir5 = Part.makeCylinder(2.1,50,Vector(18.0,-25.0,0),Vector(0,1,0))
			acir5.rotate(Vector(0,0,0),Vector(0,1,0),180)
			base1 = base1.cut(acir5)
			acir7 = Part.makeCylinder(2.1,50,Vector(18.0,-25.0,0),Vector(0,1,0))
			acir7.rotate(Vector(0,0,0),Vector(0,1,0),270)
			base1 = base1.cut(acir7)

			box1 = Part.makeBox(4.2,6.0,50,Vector(12.0,-25.0,-2.1),Vector(0,1,0))
			base1 = base1.cut(box1)
			box2 = Part.makeBox(4.2,6.0,50,Vector(12.0,-25.0,-2.1),Vector(0,1,0))
			box2.rotate(Vector(0,0,0),Vector(0,1,0),90)
			base1 = base1.cut(box2)
			box3 = Part.makeBox(4.2,6.0,50,Vector(12.0,-25.0,-2.1),Vector(0,1,0))
			box3.rotate(Vector(0,0,0),Vector(0,1,0),180)
			base1 = base1.cut(box3)
			box4 = Part.makeBox(4.2,6.0,50,Vector(12.0,-25.0,-2.1),Vector(0,1,0))
			box4.rotate(Vector(0,0,0),Vector(0,1,0),270)
			base1 = base1.cut(box4)

			base3 = Part.makeCylinder(4.75,19.4,Vector(0,0,0),Vector(0,1,0),360)
			base1 = base1.fuse(base3)
			outC=Part.makeCylinder(3.29/2,50,Vector(-25.0,15.0,0),Vector(1,0,0))
			base1=base1.cut(outC)

			R2 = 7.8
			base2 = Part.makeCylinder(R2,H_f1*2,Vector(0,4.7,0),Vector(0,1,0),360)

			tri = Part.makePolygon([(R2-(H_f1-H_f2)*sqrt(3),7.7,0),(R2,7.7-H_f1+H_f2,0),(R2,7.7+H_f1-H_f2,0),(R2-(H_f1-H_f2)*sqrt(3),7.7,0)])
			face = Part.Face(tri)
			angle = 360
			solid = face.revolve(Vector(0,0,0),Vector(0,1,0),360)
			base2 = base2.cut(solid)

			base1 = base1.fuse(base2)

			base2 = Part.makeCylinder(R3,50,Vector(0,-25,0),Vector(0,1,0),360)
			base1 = base1.cut(base2)

			#Part.show(base1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=base1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '145':

			doc=App.newDocument()

			class involute_tooth():
			    def __init__(self,numpoints=6, m=0.72, z=19, alpha=20 * pi / 180., clearence=0, shift=0., beta=0., undercut=False, simple=False, height=7., backlash=0.00):
			        self.alpha = alpha
			        self.beta = beta
			        self.m_n = m
			        self.z = z
			        self.undercut = undercut
			        self.shift = shift
			        self.simple = simple
			        self.height = height
			        self.numpoints = numpoints
			        self.clearence = clearence
			        self.backlash = backlash
			        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
			        self.m = self.m_n / cos(self.beta)
			        self.c = self.clearence * self.m_n
			        self.midpoint = [0., 0.]
			        self.d = self.z * self.m
			        self.dw = self.m * self.z
			        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
			        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
			        self.dg = self.d * cos(self.alpha_t)
			        self.phipart = 2 * pi / self.z
			        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
			        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
			        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
			        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
			        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
			        self.involute_rot = self.involute_rot1 + self.involute_rot2
			        self.involute_start = 0.
			        if self.dg <= self.df:
			            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
			        self.execute()

			    def execute(self):
			        pts = self.points(self.numpoints)
			        if not self.simple:
			            wi = []
			            for i in pts:
			                out = BSplineCurve()
			                out.interpolate(map(fcvec, i))
			                wi.append(out)
			            s = Wire(Shape(wi).Edges)
			            wi = []
			            for i in range(self.z):
			                rot = App.Matrix()
			                rot.rotateZ(-i * self.phipart)
			                tooth_rot = s.transformGeometry(rot)
			                if i != 0:
			                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
			                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
			                wi.append(tooth_rot)
			            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
			            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
			            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

			            wi = Wire(wi)
			            self.Shape = wi
			            if self.beta == 0:
			                sh = Face(wi)
			                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
			                #여기서부터 수정
			                cy1 = Part.makeCylinder(4.75,7.5,Vector(0,0,7),Vector(0,0,1),360)
			                self.Shape = self.Shape.fuse(cy1)
			                outC=Part.makeCylinder(3.29/2,50,Vector(-25.0,0,11.0),Vector(1,0,0))
			                self.Shape=self.Shape.cut(outC)

			                cy2 = Part.makeCylinder(19.0,5.6,Vector(0,0,0),Vector(0,0,-1),360)
			                self.Shape = self.Shape.fuse(cy2)
			                H_f1 = 5.6
			                H_f2 = 1.0
			                tri = Part.makePolygon([(19.0-(1.8)*sqrt(3),0,-2.8),(19.0,0,-H_f2),(19.0,0,-H_f1+H_f2),(19.0-(1.8)*sqrt(3),0,-2.8)])
			                face = Part.Face(tri)
			                solid = face.revolve(Vector(0,0,-2.8),Vector(0,0,1),360)
			                self.Shape = self.Shape.cut(solid)

			                cir1 = Part.makeCylinder(3.0,50,Vector(12,0,-4.6),Vector(0,0,1))
			                self.Shape = self.Shape.cut(cir1)
			                cir2 = Part.makeCylinder(3.0,50,Vector(12,0,-4.6),Vector(0,0,1))
			                cir2.rotate(Vector(0,0,0),Vector(0,0,1),45)
			                self.Shape = self.Shape.cut(cir2)
			                cir3 = Part.makeCylinder(3.0,50,Vector(12,0,-4.6),Vector(0,0,1))
			                cir3.rotate(Vector(0,0,0),Vector(0,0,1),90)
			                self.Shape = self.Shape.cut(cir3)
			                cir4 = Part.makeCylinder(3.0,50,Vector(12,0,-4.6),Vector(0,0,1))
			                cir4.rotate(Vector(0,0,0),Vector(0,0,1),135)
			                self.Shape = self.Shape.cut(cir4)
			                cir5 = Part.makeCylinder(3.0,50,Vector(12,0,-4.6),Vector(0,0,1))
			                cir5.rotate(Vector(0,0,0),Vector(0,0,1),180)
			                self.Shape = self.Shape.cut(cir5)
			                cir6 = Part.makeCylinder(3.0,50,Vector(12,0,-4.6),Vector(0,0,1))
			                cir6.rotate(Vector(0,0,0),Vector(0,0,1),225)
			                self.Shape = self.Shape.cut(cir6)
			                cir7 = Part.makeCylinder(3.0,50,Vector(12,0,-4.6),Vector(0,0,1))
			                cir7.rotate(Vector(0,0,0),Vector(0,0,1),270)
			                self.Shape = self.Shape.cut(cir7)
			                cir8 = Part.makeCylinder(3.0,50,Vector(12,0,-4.6),Vector(0,0,1))
			                cir8.rotate(Vector(0,0,0),Vector(0,0,1),315)
			                self.Shape = self.Shape.cut(cir8)

			                acir1 = Part.makeCylinder(2.1,50,Vector(12,0,-5.6),Vector(0,0,1))
			                self.Shape = self.Shape.cut(acir1)
			                acir2 = Part.makeCylinder(2.1,50,Vector(12,0,-5.6),Vector(0,0,1))
			                acir2.rotate(Vector(0,0,0),Vector(0,0,1),45)
			                self.Shape = self.Shape.cut(acir2)
			                acir3 = Part.makeCylinder(2.1,50,Vector(12,0,-5.6),Vector(0,0,1))
			                acir3.rotate(Vector(0,0,0),Vector(0,0,1),90)
			                self.Shape = self.Shape.cut(acir3)
			                acir4 = Part.makeCylinder(2.1,50,Vector(12,0,-5.6),Vector(0,0,1))
			                acir4.rotate(Vector(0,0,0),Vector(0,0,1),135)
			                self.Shape = self.Shape.cut(acir4)
			                acir5 = Part.makeCylinder(2.1,50,Vector(12,0,-5.6),Vector(0,0,1))
			                acir5.rotate(Vector(0,0,0),Vector(0,0,1),180)
			                self.Shape = self.Shape.cut(acir5)
			                acir6 = Part.makeCylinder(2.1,50,Vector(12,0,-5.6),Vector(0,0,1))
			                acir6.rotate(Vector(0,0,0),Vector(0,0,1),225)
			                self.Shape = self.Shape.cut(acir6)
			                acir7 = Part.makeCylinder(2.1,50,Vector(12,0,-5.6),Vector(0,0,1))
			                acir7.rotate(Vector(0,0,0),Vector(0,0,1),270)
			                self.Shape = self.Shape.cut(acir7)
			                acir8 = Part.makeCylinder(2.1,50,Vector(12,0,-5.6),Vector(0,0,1))
			                acir8.rotate(Vector(0,0,0),Vector(0,0,1),315)
			                self.Shape = self.Shape.cut(acir8)

			                cir1 = Part.makeCylinder(2.0,50,Vector(0,0,-25),Vector(0,0,1),360)
			                self.Shape = self.Shape.cut(cir1)
			                #Part.show(self.Shape) #보여주기
			                #Part.show(tri) #보여주기
			                shape=doc.addObject("Part::Feature")
			                shape.Shape=self.Shape
			                doc.recompute()
			                shape.ViewObject.ShapeColor=(1.0, 0.0, 0.0)
			                Gui.activeDocument().activeView().viewAxometric()
			                Gui.SendMsgToActiveView("ViewFit")
			            else:
			                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
			                Part.show(self.Shape)
			        else:
			            rw = self.dw / 2
			            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
			            wire = Part.Wire(circle.toShape())
			            face = Part.Face(wire)
			            self.Shape = face.extrude(App.Vector(0, 0, self.height))
			            Part.show(self.Shape)

			    def undercut_points(self, num):
			        pts = linspace(0, self.undercut_end, num)
			        fx = self.undercut_function_x()
			        x = array(map(fx, pts))
			        fy = self.undercut_function_y()
			        y = array(map(fy, pts))
			        xy = transpose([x, y])
			        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
			        xy = rotate(xy)
			        return(array(xy))

			    def involute_points(self, num):
			        pts = linspace(self.involute_start, self.involute_end, num)
			        fx = self.involute_function_x()
			        x = array(map(fx, pts))
			        fy = self.involute_function_y()
			        y = array(map(fy, pts))
			        rot = rotation(self.involute_rot - self.backlash / 4)
			        xy = rot(transpose(array([x, y])))
			        return(xy)

			    def points(self, num):
			        l1 = self.undercut_points(num)
			        l2 = self.involute_points(num)
			        s = trimfunc(l1, l2[::-1])
			        if self.undercut:
			            if isinstance(s, ndarray):
			                u1, e1 = s
			            else:
			                u1, e1 = nearestpts(l2, l1)
			        else:
			            u1 = False
			            if self.dg > self.df:
			                u1 = vstack(
			                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
			                e1 = l2
			            else:
			                e1 = l2

			        reflect = reflection(0)
			        e2 = reflect(e1)[::-1]
			        if isinstance(u1, bool):
			            u2 = False
			            one_tooth = [e1, [e1[-1], e2[0]], e2]
			        else:
			            u2 = reflect(u1)[::-1]
			            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
			        return(one_tooth)

			    def undercut_function_x(self):
			        def func(psi):
			            return(
			               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def undercut_function_y(self):
			        def func(psi):
			            return(
			                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
			        return(func)

			    def involute_function_x(self):
			        def func(phi):
			            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
			        return(func)

			    def involute_function_y(self):
			        def func(phi):
			            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
			        return(func)

			def fcvec(x):
			    if len(x) == 2:
			        return(App.Vector(x[0], x[1], 0))
			    else:
			        return(App.Vector(x[0], x[1], x[2]))

			def helicalextrusion(wire, height, angle):
			    face_a = Face(wire)
			    face_b = face_a.copy()
			    face_transform = App.Matrix()
			    face_transform.rotateZ(angle)
			    face_transform.move(App.Vector(0, 0, height))
			    face_b . transformShape(face_transform)
			    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
			    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
			    faces = [face_a, face_b]
			    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
			    pipeshell.setSpineSupport(spine)
			    pipeshell.add(wire)
			    pipeshell.setAuxiliarySpine(auxspine, True, False)
			    assert(pipeshell.isReady())
			    pipeshell.build()
			    faces.extend(pipeshell.shape().Faces)

			    fullshell = Shell(faces)
			    solid = Solid(fullshell)
			    if solid.Volume < 0:
			        solid.reverse()
			    assert(solid.Volume >= 0)
			    return(solid)

			def reflection(alpha):
			    mat = array(
			        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

			    def func(x):
			        return(dot(x, mat))
			    return(func)

			def rotation(alpha, midpoint=[0, 0]):
			    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
			    midpoint = array(midpoint)
			    vec = midpoint - dot(midpoint, mat)
			    trans = translation(vec)
			    def func(xx):
			        return(trans(dot(xx, mat)))
			    return(func)

			def translation(vec):
			    def trans(x):
			        return([x[0] + vec[0], x[1] + vec[1]])
			    def func(x):
			        return(array(map(trans, x)))
			    return(func)

			def trim(p1, p2, p3, p4):
			    a1 = array(p1)
			    a2 = array(p2)
			    a3 = array(p3)
			    a4 = array(p4)
			    if all(a1 == a2) or all(a3 == a4):
			        if all(a1 == a3):
			            return(a1)
			        else:
			            return(False)
			    elif all(a1 == a3):
			        if all(a2 == a4):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a1 == a4):
			        if all(a2 == a3):
			            return((a1 + a2) / 2)
			        else:
			            return(a1)
			    elif all(a2 == a3) or all(a2 == a4):
			        return(p2)
			    try:
			        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
			    except:
			        print(Exception)
			        return(False)
			    else:
			        if 0. < g < 1. and 0. < h < 1.:
			            return(a1 + g * (a2 - a1))
			        else:
			            return(False)
			    return(False)


			def trimfunc(l1, l2):
			    ik = 0
			    i0 = array(l1[0])
			    for i in array(l1[1:]):
			        jk = 0
			        j0 = array(l2[0])
			        for j in array(l2[1:]):
			            s = trim(j0, j, i0, i)
			            if isinstance(s, ndarray):
			                if ik == 0:
			                    l1 = [l1[0]]
			                else:
			                    l1 = l1[:ik]
			                if jk == 0:
			                    l2 == [l2[0]]
			                else:
			                    l2 = l2[jk::-1]
			                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
			            j0 = j
			            jk += 1
			        i0 = i
			        ik += 1
			    return(False)

			def norm(vec1, vec2):
			    vec = array(vec2) - array(vec1)
			    out = 0
			    for i in vec:
			        out += i ** 2
			    return(sqrt(out))

			def nearestpts(evolv, underc):
			    ik = 0
			    iout = 0
			    jout = 0
			    outmin = 1000.
			    for i in array(evolv[1:]):
			        jk = 0
			        for j in array(underc[1:]):
			            l = norm(i, j)
			            if l < outmin:
			                re = norm(i, [0, 0])
			                ru = norm(j, [0, 0])
			                if re > ru:
			                    outmin = l
			                    iout, jout = [ik, jk]
			            jk += 1
			        ik += 1
			    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])


			#class CreateInvoluteGear():
			#    """create an involute gear"""
			#    def __init__(self):
			#        pass
			#
			#    def GetResources(self):
			#        return {'Pixmap': 'involutegear.svg', 'MenuText': 'involute gear', 'ToolTip': 'involute gear'}
			#
			#    def IsActive(self):
			#        if ED.ActiveDocument is None:
			#            return False
			#        else:
			#            return True
			#
			#    def Activated(self):
			#        a = ED.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#        involute_gear(a)
			#        a.ViewObject.Proxy = 0.
			#        ED.ActiveDocument.recompute()
			#        Gui.SendMsgToActiveView("ViewFit")

			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#a = App.ActiveDocument.addObject("Part::FeaturePython", "involute_gear")
			#involute_gear(a)
			#a.ViewObject.Proxy = 0.
			#App.ActiveDocument.recompute()
			#Gui.SendMsgToActiveView("ViewFit")
			ex = involute_tooth()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '147':

			doc=App.newDocument()

			A = Part.makeSphere(33.0,Vector(0,0,0),Vector(0,0,1),0,90,90)
			B = Part.makeSphere(31.5,Vector(0,0,0),Vector(0,0,1),0,90,90)
			A = A.cut(B)

			cy4 = Part.makeCylinder(6.0 ,1.5,Vector(0,0,31.5),Vector(0,0,1),90)
			cy4.rotate(Vector(0,0,31.5),Vector(0,0,1),180)
			A = A.fuse(cy4)
			cy5 = Part.makeCylinder(6.0 ,1.5,Vector(0,31.5,0),Vector(0,1,0),90)
			cy5.rotate(Vector(0,31.5,0),Vector(0,1,0),180)
			A = A.fuse(cy5)
			cy6 = Part.makeCylinder(6.0 ,1.5,Vector(31.5,0,0),Vector(1,0,0),90)
			cy6.rotate(Vector(31.5,0,0),Vector(1,0,0),90)
			A = A.fuse(cy6)

			arc1=Part.makeCircle(33.0,Vector(0,0,0),Vector(0,0,1),0,90)
			Line1=Part.makeLine(Vector(0,33.0,0),Vector(0,31.5,0))
			arc2=Part.makeCircle(31.5,Vector(0,0,0),Vector(0,0,1),0,90)
			Line2=Part.makeLine(Vector(33.0,0,0),Vector(31.5,0,0))
			arc1=arc1.fuse(arc2)
			arc1=arc1.fuse(Line1)
			arc1=arc1.fuse(Line2)
			w1 = Part.Wire(arc1.Edges)
			face = Part.Face(w1)
			p = face.extrude(Vector(0,0,-6.0))
			A=A.fuse(p)

			aarc1=Part.makeCircle(33.0,Vector(0,0,0),Vector(1,0,0),0,90)
			aLine1=Part.makeLine(Vector(0,33.0,0),Vector(0,31.5,0))
			aarc2=Part.makeCircle(31.5,Vector(0,0,0),Vector(1,0,0),0,90)
			aLine2=Part.makeLine(Vector(0,0,33.0),Vector(0,0,31.5))
			aarc1=aarc1.fuse(aarc2)
			aarc1=aarc1.fuse(aLine1)
			aarc1=aarc1.fuse(aLine2)
			aw1 = Part.Wire(aarc1.Edges)
			aface = Part.Face(aw1)
			ap = aface.extrude(Vector(-6.0,0,0))
			A=A.fuse(ap)

			barc1=Part.makeCircle(33.0,Vector(0,0,0),Vector(0,-1,0),0,90)
			barc2=Part.makeCircle(31.5,Vector(0,0,0),Vector(0,-1,0),0,90)
			bLine1=Part.makeLine(Vector(33.0,0,0),Vector(31.5,0,0))
			bLine2=Part.makeLine(Vector(0,0,33.0),Vector(0,0,31.5))
			barc1=barc1.fuse(barc2)
			barc1=barc1.fuse(bLine1)
			barc1=barc1.fuse(bLine2)
			bw1 = Part.Wire(barc1.Edges)
			bface = Part.Face(bw1)
			bp = bface.extrude(Vector(0,-6.0,0))
			A=A.fuse(bp)

			cy1 = Part.makeCylinder(2.0 ,5,Vector(0,0,31),Vector(0,0,1))
			A = A.cut(cy1)
			cy2 = Part.makeCylinder(2.0 ,5,Vector(0,31,0),Vector(0,1,0))
			A = A.cut(cy2)
			cy3 = Part.makeCylinder(2.0 ,5,Vector(31,0,0),Vector(1,0,0))
			A = A.cut(cy3)

			#Part.show(A)

			shape=doc.addObject("Part::Feature")
			shape.Shape=A
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '148':
			doc=App.newDocument()

			t=1.95
			h=11.85
			l=139.50
			w= 29.70
			f=6.43
			D=11.10
			d1=5.45
			d2=4.05
			l1=15.10
			l2=45.70
			w1=26.70
			w2=10.20
			wt1=9.40
			wt2=10.60
			wt3=11.80
			h1=1.43
			h2=3.90
			l3=1
			t1=1.34
			i=0
			n=11
			cir4=[]

			plate1 = Part.makeBox(l,w,t,Vector(0,0,0),Vector(0,0,1))
			plate1 = plate1.makeFillet(f, [plate1.Edges[2],plate1.Edges[6]])
			plate2 = Part.makeBox(l,w,t,Vector(0,0,h-t),Vector(0,0,1))
			plate2 = plate2.makeFillet(f, [plate2.Edges[2],plate2.Edges[6]])
			cir1 = Part.makeCylinder(D/2,h,Vector(D/2,w-w1-D/2,0),Vector(0,0,1))
			cir2 = Part.makeCylinder(D/2,h,Vector(l/2,w-w1-D/2,0),Vector(0,0,1))
			cir3 = Part.makeCylinder(D/2,h,Vector(l-D/2,w-w1-D/2,0),Vector(0,0,1))
			plate1 = plate1.fuse(cir1)
			plate1 = plate1.fuse(cir2)
			plate1 = plate1.fuse(cir3)
			plate1 = plate1.fuse(plate2)
			box1= Part.makeBox(D,D/2,h,Vector(0,w-w1-D/2,0),Vector(0,0,1))
			box2= Part.makeBox(D,D/2,h,Vector(l/2-D/2,w-w1-D/2,0),Vector(0,0,1))
			box3= Part.makeBox(D,D/2,h,Vector(l-D,w-w1-D/2,0),Vector(0,0,1))
			plate1 = plate1.fuse(box1)
			plate1 = plate1.fuse(box2)
			plate1 = plate1.fuse(box3)
			box4= Part.makeBox(l1,w-w1,h-2*t,Vector(0,0,t),Vector(0,0,1))
			box5= Part.makeBox(l2,w-w1,h-2*t,Vector((l-l2)/2,0,t),Vector(0,0,1))
			box6= Part.makeBox(l1,w-w1,h-2*t,Vector(l-l1,0,t),Vector(0,0,1))
			plate1 = plate1.fuse(box4)
			plate1 = plate1.fuse(box5)
			plate1 = plate1.fuse(box6)

			for i in range(n):
					cir4.append(Part.makeCylinder(d2/2,h,Vector(6.525+12.7*i,w-(4.15+d2/2),0)))

			for i in cir4:
			        plate1 = plate1.cut(i)

			cir5 = Part.makeCylinder(d1/2,h,Vector(6.525+12.7,w-(4.15+d2/2),0))
			cir6 = Part.makeCylinder(d1/2,h,Vector(6.525+12.7*7,w-(4.15+d2/2),0))
			cir7 = Part.makeCylinder(d1/2,h,Vector(6.525+12.7*8,w-(4.15+d2/2),0))
			cir8 = Part.makeCylinder(d1/2,h,Vector(6.525+12.7*10,w-(4.15+d2/2),0))
			plate1 = plate1.cut(cir5)
			plate1 = plate1.cut(cir6)
			plate1 = plate1.cut(cir7)
			plate1 = plate1.cut(cir8)

			tri = Part.makePolygon([(0,11.80,0),(0,10.60,1.43),(0,9.40,0),(0,11.80,0)])
			fa = Part.Face(tri)
			p = fa.extrude(Vector(l,0,0))
			plate1 = plate1.cut(p)

			tri1 = Part.makePolygon([(0,11.80,h),(0,10.60,h-1.43),(0,9.40,h),(0,11.80,h)])
			fa1 = Part.Face(tri1)
			p1 = fa1.extrude(Vector(l,0,0))
			plate1 = plate1.cut(p1)

			extend1 = Part.makePolygon([(0,10.60+0.5+t1,t),(0,10.60+t1+0.5,3.9),(0,10.60+0.5,3.9),(0,10.6+0.5,3.9-h1),(0,10.6-0.5,3.9-h1),(0,10.6-0.5,3.9),(0,10.6-0.5-t1,3.9),(0,10.60-t1-0.5,t),(0,10.60+0.5+t1,t)])
			fa2 = Part.Face(extend1)
			p2 = fa2.extrude(Vector(l,0,0))
			plate1 = plate1.fuse(p2)

			extend2 = Part.makePolygon([(0,10.60+0.5+t1,h-t),(0,10.60+t1+0.5,h-3.9),(0,10.60+0.5,h-3.9),(0,10.6+0.5,h-3.9+h1),(0,10.6-0.5,h-3.9+h1),(0,10.6-0.5,h-3.9),(0,10.6-0.5-t1,h-3.9),(0,10.60-t1-0.5,h-t),(0,10.60+0.5+t1,h-t)])
			fa3 = Part.Face(extend2)
			p3 = fa3.extrude(Vector(l,0,0))
			plate1 = plate1.fuse(p3)

			#Part.show(plate1)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '151':
			doc=App.newDocument()

			d = 50
			t = 10
			d1 = 36.92
			d2 = 34.96
			h1 = 2.29
			n = 2
			i = 0

			circle = Part.makeCylinder(d/2,t,Vector(0,0,0))
			circle = circle.makeFillet((t-h1)/2,[circle.Edges[0],circle.Edges[2]])

			cir = []
			for i in range(n):
				cir.append(Part.makeCylinder(d1/2,(t-h1)/2,Vector(0,0,(t-(t-h1)/2)*i)))
			for i in cir:
				circle = circle.cut(i)

			circle1 = Part.makeCylinder(d2/2,h1,Vector(0,0,(t-h1)/2))
			circle = circle.cut(circle1)

			#Part.show(circle)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '152':
			doc=App.newDocument()

			d = 70
			t = 10
			d1 = 57.31
			d2 = 55.24
			h1 = 2.81
			n = 2
			i = 0

			circle = Part.makeCylinder(d/2,t,Vector(0,0,0))
			circle = circle.makeFillet((t-h1)/2,[circle.Edges[0],circle.Edges[2]])

			cir = []
			for i in range(n):
				cir.append(Part.makeCylinder(d1/2,(t-h1)/2,Vector(0,0,(t-(t-h1)/2)*i)))
			for i in cir:
				circle = circle.cut(i)

			circle1 = Part.makeCylinder(d2/2,h1,Vector(0,0,(t-h1)/2))
			circle = circle.cut(circle1)

			#Part.show(circle)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.0, 0.0, 0.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '161':
			doc=App.newDocument()

			D = 8
			h = 6
			d=2.8
			circle = Part.makeCylinder(D/2,h,Vector(0,0,0))
			box = Part.makeBox(d,d,h,Vector(-1.4,-1.4,0))
			circle = circle.cut(box)


			#Part.show(circle)

			shape=doc.addObject("Part::Feature")
			shape.Shape=circle
			doc.recompute()
			shape.ViewObject.ShapeColor=(0.8,0.8,0.8)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")
		elif self.numericInput0.text() == '168':
			doc=App.newDocument()

			x = 62.8
			y = 25.4
			z = 14.3
			t = 0.7
			d = 4.2
			n = 5
			m = 2
			f = 6.35
			i = 0
			j = 0

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate2 = Part.makeBox(t,y,z,Vector(0,-y,0),Vector(0,0,1))
			plate3 = Part.makeBox(t,y,z,Vector(x-t,-y,0),Vector(0,0,1))

			plate2 = plate2.makeFillet(f, [plate2.Edges[9],plate2.Edges[11]])
			plate3 = plate3.makeFillet(f, [plate3.Edges[9],plate3.Edges[11]])

			cir = []
			lt = []
			rt = []

			for j in range(m):
				for i in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(((x-11.0)/(n-1))*i+5.5,-((y-11.0)/(m-1))*j-5.5,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			for j in range(m):
				lt.append(Part.makeCylinder(d/2,t,Vector(0,-((y-11.0)/(m-1))*j-5.5,z/2),Vector(1,0,0)))
			for j in range(m):
				rt.append(Part.makeCylinder(d/2,t,Vector(x-t,-((y-11.0)/(m-1))*j-5.5,z/2),Vector(1,0,0)))
			for i in lt:
				plate2 = plate2.cut(i)
			for i in rt:
				plate3 = plate3.cut(i)

			plate1 = plate1.fuse(plate2)
			plate1 = plate1.fuse(plate3)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '169':
			doc=App.newDocument()

			x = 90.2
			y = 25.4
			z = 14.3
			t = 0.7
			d = 4.2
			n = 7
			m = 2
			f = 6.35
			i = 0
			j = 0

			plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
			plate2 = Part.makeBox(t,y,z,Vector(0,-y,0),Vector(0,0,1))
			plate3 = Part.makeBox(t,y,z,Vector(x-t,-y,0),Vector(0,0,1))

			plate2 = plate2.makeFillet(f, [plate2.Edges[9],plate2.Edges[11]])
			plate3 = plate3.makeFillet(f, [plate3.Edges[9],plate3.Edges[11]])

			cir = []
			lt = []
			rt = []

			for j in range(m):
				for i in range(n):
					cir.append(Part.makeCylinder(d/2,t,Vector(((x-11.0)/(n-1))*i+5.5,-((y-11.0)/(m-1))*j-5.5,0)))
			for i in cir:
				plate1 = plate1.cut(i)

			for j in range(m):
				lt.append(Part.makeCylinder(d/2,t,Vector(0,-((y-11.0)/(m-1))*j-5.5,z/2),Vector(1,0,0)))
			for j in range(m):
				rt.append(Part.makeCylinder(d/2,t,Vector(x-t,-((y-11.0)/(m-1))*j-5.5,z/2),Vector(1,0,0)))
			for i in lt:
				plate2 = plate2.cut(i)
			for i in rt:
				plate3 = plate3.cut(i)

			plate1 = plate1.fuse(plate2)
			plate1 = plate1.fuse(plate3)

			shape=doc.addObject("Part::Feature")
			shape.Shape=plate1
			doc.recompute()
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View
		elif self.numericInput0.text() == '177':
			doc=App.newDocument()

			# 기본형상 box
			cir_hex=4 #circle_diameter

			exHex = Part.makeBox(5.5,5.5,1.4,Vector(-5.5/2,-5.5/2,-1.4))

			d=8
			circ=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))
			exHex=exHex.fuse(circ)

			# 나사선 helix
			helix = Part.makeHelix(0.797,30,2)             #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((1.7,0,-0.125), (1.7,0,0.125))
			edge2 = Part.makeLine((1.7,0,0.125), (2.3,0,0.419))
			edge3 = Part.makeLine((2.3,0,0.419), (2.3,0,-0.419))
			edge4 = Part.makeLine((2.3,0,-0.419), (1.7,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)

	def onDesign1(self):
		doc=App.newDocument()

		r = float(self.numericInput1.text())
		l = float(self.numericInput2.text())

		v1=Base.Vector(0,r/2,0)
		v2=Base.Vector(-r/2,0,0)
		v3=Base.Vector(0,-r/2,0)
		v4=Base.Vector(r/2,0,0)

		C1=Part.Arc(v1,v2,v3)
		C2=Part.Arc(v3,v4,v1)

		S1=Part.Shape([C1,C2])

		W=Part.Wire(S1.Edges)
		face=Part.Face(W)
		P=face.extrude(Base.Vector(0,0,l))

		shape=doc.addObject("Part::Feature")
		shape.Shape=P
		doc.recompute()
		shape.ViewObject.ShapeColor=(0.6,0.6,0.6)
		Gui.activeDocument().activeView().viewAxometric()
		Gui.SendMsgToActiveView("ViewFit")
	def onDesign3(self):

		doc=App.newDocument()

		l = float(self.numericInput1.text())
		w = float(self.numericInput2.text())
		h = float(self.numericInput3.text())
		t = float(self.numericInput4.text())
		d = float(self.numericInput5.text())
		n = int(self.numericInput6.text())

		b = n-1

		box = []
		cir = []
		mir = []
		hole = []
		plate1 = Part.makeBox(l,w,t,Vector(0,-w,0),Vector(0,0,1))
		plate1 = plate1.makeFillet(w/2, [plate1.Edges[0],plate1.Edges[4]])
		box1 = Part.makeBox(d,5,t,Vector(5,-10,0))
		box2 = Part.makeBox(d,5,t,Vector(5+l-10.0-d,-10,0))
		cir1 = Part.makeCylinder(d/2,t,Vector(5+d/2,-10,0))
		mir1 = Part.makeCylinder(d/2,t,Vector(5+d/2,-5,0))
		cir2 = Part.makeCylinder(d/2,t,Vector(5+l-10.0-d/2,-10,0))
		mir2 = Part.makeCylinder(d/2,t,Vector(5+l-10.0-d/2,-5,0))
		for i in range(1,b):
			box.append(Part.makeBox(d,5,t,Vector(5+(l-10.0)/b*i-d/2,-10,0)))
			cir.append(Part.makeCylinder(d/2,t,Vector(5+(l-10.0)/b*i,-10,0)))
			mir.append(Part.makeCylinder(d/2,t,Vector(5+(l-10.0)/b*i,-5,0)))
			plate1 = plate1.cut(box1)
		plate1 = plate1.cut(box2)
		plate1 = plate1.cut(cir1)
		plate1 = plate1.cut(mir1)
		plate1 = plate1.cut(cir2)
		plate1 = plate1.cut(mir2)

		for i in box:
			plate1 = plate1.cut(i)
		for i in cir:
			plate1 = plate1.cut(i)
		for i in mir:
			plate1 = plate1.cut(i)

		plate2 = Part.makeBox(l,t,h-t,Vector(0,-t,t))
		plate2 = plate2.makeFillet(h/2, [plate2.Edges[1],plate2.Edges[5]])
		hole1 = Part.makeCylinder(d/2,t,Vector(5+d/2,-t,h/2),Vector(0,1,0))
		hole2 = Part.makeCylinder(d/2,t,Vector(5+l-10.0-d/2,-t,h/2),Vector(0,1,0))
		for i in range(1,b):
			hole.append(Part.makeCylinder(d/2,t,Vector(5+(l-10.0)/b*i,-t,h/2),Vector(0,1,0)))

		plate2 = plate2.cut(hole1)
		plate2 = plate2.cut(hole2)
		for i in hole:
			plate2 = plate2.cut(i)

		plate1 = plate1.fuse(plate2)

		#Part.show(plate1)
		shape=doc.addObject("Part::Feature")
		shape.Shape=plate1
		doc.recompute()
		shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
		Gui.activeDocument().activeView().viewAxometric()
		Gui.SendMsgToActiveView("ViewFit")

	def onDesign4(self):
		doc=App.newDocument()

		x = float(self.numericInput1.text())
		y = float(self.numericInput2.text())
		r = 6.35
		t = float(self.numericInput3.text())
		d = float(self.numericInput4.text())
		n = int(self.numericInput5.text())
		m = int(self.numericInput6.text())
		b = n-1
		p = m-1
		plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
		plate1 = plate1.makeFillet(r, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

		hole1 = Part.makeCylinder(d/2,t,Vector(x/2,-y/2,0))
		hole_up = []
		hole_down = []
		for i in range(1,b):
			hole_up.append(Part.makeCylinder(d/2,t,Vector(5+(x-10.0)/b*i,-5,0)))
			hole_down.append(Part.makeCylinder(d/2,t,Vector(5+(x-10.0)/b*i,5-y,0)))
		plate1 = plate1.cut(hole1)
		for i in hole_up:
			plate1 = plate1.cut(i)
		for i in hole_down:
			plate1 = plate1.cut(i)

		left = []
		right = []
		box = []
		left2 = []
		right2 = []
		box2 = []
		for i in range(0,m):
			box.append(Part.makeBox(5,d,t,Vector(5,-(y-10.0)/p*i-d/2-5,0)))
			left.append(Part.makeCylinder(d/2,t,Vector(5,-(y-10.0)/p*i-5,0)))
			right.append(Part.makeCylinder(d/2,t,Vector(5+5,-(y-10.0)/p*i-5,0)))
		for i in range(0,m):
			box2.append(Part.makeBox(5,d,t,Vector(x-10,-(y-10.0)/p*i-d/2-5,0)))
			left2.append(Part.makeCylinder(d/2,t,Vector(x-10,-(y-10.0)/p*i-5,0)))
			right2.append(Part.makeCylinder(d/2,t,Vector(x-10+5,-(y-10.0)/p*i-5,0)))
		for i in left:
			plate1 = plate1.cut(i)
		for i in right:
			plate1 = plate1.cut(i)
		for i in box:
			plate1 = plate1.cut(i)
		for i in left2:
			plate1 = plate1.cut(i)
		for i in right2:
			plate1 = plate1.cut(i)
		for i in box2:
			plate1 = plate1.cut(i)

		#Part.show(plate1)
		shape=doc.addObject("Part::Feature")
		shape.Shape=plate1
		doc.recompute()
		shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
		Gui.activeDocument().activeView().viewAxometric()
		Gui.SendMsgToActiveView("ViewFit")

	def onDesign5(self):
		doc=App.newDocument()

		x = float(self.numericInput1.text())
		y = float(self.numericInput2.text())
		r = (y-0.1)/2
		t = float(self.numericInput3.text())
		d = float(self.numericInput4.text())
		n = int(self.numericInput5.text())
		b = n-1
		plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
		plate1 = plate1.makeFillet(r, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

		hole_up = []
		for i in range(1,b):
			hole_up.append(Part.makeCylinder(d/2,t,Vector(5+(x-10.0)/b*i,-y/2,0)))
			hole_up.append(Part.makeCylinder(d/2,t,Vector(5,-y/2,0)))
			hole_up.append(Part.makeCylinder(d/2,t,Vector(x-5,-y/2,0)))
		for i in hole_up:
			plate1 = plate1.cut(i)

		#Part.show(plate1)
		shape=doc.addObject("Part::Feature")
		shape.Shape=plate1
		doc.recompute()
		shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
		Gui.activeDocument().activeView().viewAxometric()
		Gui.SendMsgToActiveView("ViewFit")

	def onDesign6(self):
		doc=App.newDocument()

		x = float(self.numericInput1.text())
		y = float(self.numericInput2.text())
		z = float(self.numericInput3.text())
		t = 2.0
		d = float(self.numericInput4.text())
		n = int(self.numericInput5.text())
		m = int(self.numericInput6.text())
		f = z/2-0.1
		i = 0
		j = 0

		plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
		plate2 = Part.makeBox(t,y,z,Vector(0,-y,0),Vector(0,0,1))
		plate3 = Part.makeBox(t,y,z,Vector(x-t,-y,0),Vector(0,0,1))

		plate2 = plate2.makeFillet(f, [plate2.Edges[9],plate2.Edges[11]])
		plate3 = plate3.makeFillet(f, [plate3.Edges[9],plate3.Edges[11]])

		cir = []
		lt = []
		rt = []

		for j in range(m):
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(((x-10.0)/(n-1))*i+5,-((y-10.0)/(m-1))*j-5,0)))
		for i in cir:
			plate1 = plate1.cut(i)

		for j in range(m):
			lt.append(Part.makeCylinder(d/2,t,Vector(0,-((y-10.0)/(m-1))*j-5,z/2),Vector(1,0,0)))
		for j in range(m):
			rt.append(Part.makeCylinder(d/2,t,Vector(x-t,-((y-10.0)/(m-1))*j-5,z/2),Vector(1,0,0)))
		for i in lt:
			plate2 = plate2.cut(i)
		for i in rt:
			plate3 = plate3.cut(i)

		plate1 = plate1.fuse(plate2)
		plate1 = plate1.fuse(plate3)

		#Part.show(plate1)
		shape=doc.addObject("Part::Feature")
		shape.Shape=plate1
		doc.recompute()
		shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
		Gui.activeDocument().activeView().viewAxometric()
		Gui.SendMsgToActiveView("ViewFit")
	def onDesign7(self):
		doc=App.newDocument()

		x = float(self.numericInput1.text())
		y = float(self.numericInput2.text())
		t = 2.0
		d = float(self.numericInput3.text())
		n = int(self.numericInput4.text())
		m = int(self.numericInput5.text())
		f = 6
		i = 0
		j = 0

		plate1 = Part.makeBox(x,y,t,Vector(0,-y,0),Vector(0,0,1))
		plate1 = plate1.makeFillet(f, [plate1.Edges[0],plate1.Edges[2],plate1.Edges[4],plate1.Edges[6]])

		cir = []

		for j in range(m):
			for i in range(n):
				cir.append(Part.makeCylinder(d/2,t,Vector(((x-10.0)/(n-1))*i+5,-((y-10.0)/(m-1))*j-5,0)))
		for i in cir:
			plate1 = plate1.cut(i)

		shape=doc.addObject("Part::Feature")                   #Color
		shape.Shape=plate1				                       #Color
		doc.recompute()                                        #Color
		shape.ViewObject.ShapeColor=(1.0,1.0,1.0)           #Color
		Gui.activeDocument().activeView().viewAxometric()      #View
		Gui.SendMsgToActiveView("ViewFit")                     #View
	def onDesign12(self):

		doc=App.newDocument()

		D = float(self.numericInput1.text())
		d = float(self.numericInput2.text())
		t = float(self.numericInput3.text())

		plate1 = Part.makeCylinder(D/2,t,Vector(0,0,0))
		plate2 = Part.makeCylinder(d/2,t,Vector(0,0,0))
		plate1 = plate1.cut(plate2)

		shape=doc.addObject("Part::Feature")                   #Color
		shape.Shape=plate1				                       #Color
		doc.recompute()                                        #Color
		shape.ViewObject.ShapeColor=(0.8, 0.8, 0.8)           #Color
		Gui.activeDocument().activeView().viewAxometric()      #View
		Gui.SendMsgToActiveView("ViewFit")                     #View

	def onDesign14(self):

		doc=App.newDocument()

		z = int(self.numericInput1.text())
		m = float(self.numericInput2.text())
		abb = float(self.numericInput3.text())

		class involute_tooth():
		    def __init__(self,numpoints=6,abb = float(self.numericInput3.text()), m=float(self.numericInput2.text()), z=int(self.numericInput1.text()), alpha=20 * pi / 180., clearence=0.75, shift=0., beta=0., undercut=False, simple=False, height=float(self.numericInput4.text()), backlash=0.00):
		        self.alpha = alpha
		        self.beta = beta
		        self.m_n = m
		        self.abb = abb
		        self.z = z
		        self.undercut = undercut
		        self.shift = shift
		        self.simple = simple
		        self.height = height
		        self.numpoints = numpoints
		        self.clearence = clearence
		        self.backlash = backlash
		        self.alpha_t = arctan(tan(self.alpha) / cos(self.beta))
		        self.m = self.m_n / cos(self.beta)
		        self.c = self.clearence * self.m_n
		        self.midpoint = [0., 0.]
		        self.d = self.z * self.m
		        self.dw = self.m * self.z
		        self.da = self.dw + 2. * self.m_n + 2. * self.shift * self.m_n
		        self.df = self.dw - 2. * self.m_n - 2 * self.c + 2. * self.shift * self.m_n
		        self.dg = self.d * cos(self.alpha_t)
		        self.phipart = 2 * pi / self.z
		        self.undercut_end = sqrt(-self.df ** 2 + self.da ** 2) / self.da
		        self.undercut_rot = (-self.df / self.dw * tan(arctan((2 * ((self.m * pi) / 4. - (self.c + self.m_n) * tan(self.alpha_t))) / self.df)))
		        self.involute_end = sqrt(self.da ** 2 - self.dg ** 2) / self.dg
		        self.involute_rot1 = sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg - arctan( sqrt(-self.dg ** 2 + (self.dw) ** 2) / self.dg)
		        self.involute_rot2 = self.m /(self.d) * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
		        self.involute_rot2 = 1 / self.z * (pi / 2 + 2 * self.shift * tan(self.alpha_t))
		        self.involute_rot = self.involute_rot1 + self.involute_rot2
		        self.involute_start = 0.
		        if self.dg <= self.df:
		            self.involute_start = sqrt(self.df ** 2 - self.dg ** 2) / self.dg
		        self.execute()

		    def execute(self):
		        pts = self.points(self.numpoints)
		        if not self.simple:
		            wi = []
		            for i in pts:
		                out = BSplineCurve()
		                out.interpolate(map(fcvec, i))
		                wi.append(out)
		            s = Wire(Shape(wi).Edges)
		            wi = []
		            for i in range(self.z):
		                rot = App.Matrix()
		                rot.rotateZ(-i * self.phipart)
		                tooth_rot = s.transformGeometry(rot)
		                if i != 0:
		                    pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
		                    pt_1 = tooth_rot.Edges[0].Vertexes[-1].Point
		                    wi.append(Wire([Line(pt_0, pt_1).toShape()]))
		                wi.append(tooth_rot)
		            pt_0 = wi[-1].Edges[-1].Vertexes[0].Point
		            pt_1 = wi[0].Edges[0].Vertexes[-1].Point
		            wi.append(Wire([Line(pt_0, pt_1).toShape()]))

		            wi = Wire(wi)
		            self.Shape = wi
		            if self.beta == 0:
		                sh = Face(wi)
		                self.Shape = sh.extrude(App.Vector(0, 0, self.height))
		                #여기서부터 수정
		                d = 4.11
		                self.cir = Part.makeCylinder(17,4,Vector(0,0,0))
		                self.cir2 = Part.makeCylinder(5.4,5,Vector(0,0,-1))
		                self.cir3 = Part.makeCylinder(4.7,7.6,Vector(0,0,-8.6))
		                self.cir4 = Part.makeCylinder(d/2,13.6,Vector(0,0,-8.6))
		                self.cir_1 = Part.makeCylinder(d/2,13.6,Vector(self.abb,0,0))
		                self.cir_2 = Part.makeCylinder(d/2,13.6,Vector(-self.abb,0,0))
		                self.cir_3 = Part.makeCylinder(d/2,13.6,Vector(0,self.abb,0))
		                self.cir_4 = Part.makeCylinder(d/2,13.6,Vector(0,-self.abb,0))
		                self.cir_5 = Part.makeCylinder(d/2,13.6,Vector(self.abb*cos(45 * pi / 180.),self.abb*sin(45 * pi / 180.),0))
		                self.cir_6 = Part.makeCylinder(d/2,13.6,Vector(-self.abb*cos(45 * pi / 180.),self.abb*sin(45 * pi / 180.),0))
		                self.cir_7 = Part.makeCylinder(d/2,13.6,Vector(self.abb*cos(45 * pi / 180.),-self.abb*sin(45 * pi / 180.),0))
		                self.cir_8 = Part.makeCylinder(d/2,13.6,Vector(-self.abb*cos(45 * pi / 180.),-self.abb*sin(45 * pi / 180.),0))
		                self.cir_0 = Part.makeCylinder(d/2,13.6,Vector(0,-6.8,-4.6),Vector(0,1,0))
		                self.Shape = self.Shape.cut(self.cir)
		                self.Shape = self.Shape.fuse(self.cir2)
		                self.Shape = self.Shape.fuse(self.cir3)
		                self.Shape = self.Shape.cut(self.cir4)
		                self.Shape = self.Shape.cut(self.cir_1)
		                self.Shape = self.Shape.cut(self.cir_2)
		                self.Shape = self.Shape.cut(self.cir_3)
		                self.Shape = self.Shape.cut(self.cir_4)
		                self.Shape = self.Shape.cut(self.cir_5)
		                self.Shape = self.Shape.cut(self.cir_6)
		                self.Shape = self.Shape.cut(self.cir_7)
		                self.Shape = self.Shape.cut(self.cir_8)
		                self.Shape = self.Shape.cut(self.cir_0)
		                #Part.show(self.Shape) #보여주기
		                shape=doc.addObject("Part::Feature")
		                shape.Shape=self.Shape
		                doc.recompute()
		                shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)
		                Gui.activeDocument().activeView().viewAxometric()
		                Gui.SendMsgToActiveView("ViewFit")
		            else:
		                self.Shape = helicalextrusion(wi, self.height, self.height*tan(self.beta)*2/self.d)
		                Part.show(self.Shape)
		        else:
		            rw = self.dw / 2
		            circle = Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), rw)
		            wire = Part.Wire(circle.toShape())
		            face = Part.Face(wire)
		            self.Shape = face.extrude(App.Vector(0, 0, self.height))
		            Part.show(self.Shape)

		    def undercut_points(self, num):
		        pts = linspace(0, self.undercut_end, num)
		        fx = self.undercut_function_x()
		        x = array(map(fx, pts))
		        fy = self.undercut_function_y()
		        y = array(map(fy, pts))
		        xy = transpose([x, y])
		        rotate = rotation(self.undercut_rot + self.phipart / 2 - self.backlash / 4)
		        xy = rotate(xy)
		        return(array(xy))

		    def involute_points(self, num):
		        pts = linspace(self.involute_start, self.involute_end, num)
		        fx = self.involute_function_x()
		        x = array(map(fx, pts))
		        fy = self.involute_function_y()
		        y = array(map(fy, pts))
		        rot = rotation(self.involute_rot - self.backlash / 4)
		        xy = rot(transpose(array([x, y])))
		        return(xy)

		    def points(self, num):
		        l1 = self.undercut_points(num)
		        l2 = self.involute_points(num)
		        s = trimfunc(l1, l2[::-1])
		        if self.undercut:
		            if isinstance(s, ndarray):
		                u1, e1 = s
		            else:
		                u1, e1 = nearestpts(l2, l1)
		        else:
		            u1 = False
		            if self.dg > self.df:
		                u1 = vstack(
		                    [[l2[0] * self.df / (norm(l2[0], [0, 0]) * 2)], [l2[0]]])
		                e1 = l2
		            else:
		                e1 = l2

		        reflect = reflection(0)
		        e2 = reflect(e1)[::-1]
		        if isinstance(u1, bool):
		            u2 = False
		            one_tooth = [e1, [e1[-1], e2[0]], e2]
		        else:
		            u2 = reflect(u1)[::-1]
		            one_tooth = [u1, e1, [e1[-1], e2[0]], e2, u2]
		        return(one_tooth)

		    def undercut_function_x(self):
		        def func(psi):
		            return(
		               cos(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
		        return(func)

		    def undercut_function_y(self):
		        def func(psi):
		            return(
		                sin(psi - (self.df * tan(psi)) / self.dw) * sqrt(self.df ** 2 / 4 + (self.df ** 2 * tan(psi) ** 2) / 4.))
		        return(func)

		    def involute_function_x(self):
		        def func(phi):
		            return(array(self.dg / 2 * cos(phi) + phi * self.dg / 2 * sin(phi)))
		        return(func)

		    def involute_function_y(self):
		        def func(phi):
		            return(self.dg / 2 * sin(phi) - phi * self.dg / 2 * cos(phi))
		        return(func)

		def fcvec(x):
		    if len(x) == 2:
		        return(App.Vector(x[0], x[1], 0))
		    else:
		        return(App.Vector(x[0], x[1], x[2]))

		def helicalextrusion(wire, height, angle):
		    face_a = Face(wire)
		    face_b = face_a.copy()
		    face_transform = App.Matrix()
		    face_transform.rotateZ(angle)
		    face_transform.move(App.Vector(0, 0, height))
		    face_b . transformShape(face_transform)
		    spine = Wire(Line(fcvec([0., 0, 0]), fcvec([0, 0, height])).toShape())
		    auxspine = makeHelix(height * 2 * pi / angle, height, 1.)
		    faces = [face_a, face_b]
		    pipeshell = BRepOffsetAPI.MakePipeShell(spine)
		    pipeshell.setSpineSupport(spine)
		    pipeshell.add(wire)
		    pipeshell.setAuxiliarySpine(auxspine, True, False)
		    assert(pipeshell.isReady())
		    pipeshell.build()
		    faces.extend(pipeshell.shape().Faces)

		    fullshell = Shell(faces)
		    solid = Solid(fullshell)
		    if solid.Volume < 0:
		        solid.reverse()
		    assert(solid.Volume >= 0)
		    return(solid)

		def reflection(alpha):
		    mat = array(
		        [[cos(2 * alpha), -sin(2 * alpha)], [-sin(2 * alpha), -cos(2 * alpha)]])

		    def func(x):
		        return(dot(x, mat))
		    return(func)

		def rotation(alpha, midpoint=[0, 0]):
		    mat = array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
		    midpoint = array(midpoint)
		    vec = midpoint - dot(midpoint, mat)
		    trans = translation(vec)
		    def func(xx):
		        return(trans(dot(xx, mat)))
		    return(func)

		def translation(vec):
		    def trans(x):
		        return([x[0] + vec[0], x[1] + vec[1]])
		    def func(x):
		        return(array(map(trans, x)))
		    return(func)

		def trim(p1, p2, p3, p4):
		    a1 = array(p1)
		    a2 = array(p2)
		    a3 = array(p3)
		    a4 = array(p4)
		    if all(a1 == a2) or all(a3 == a4):
		        if all(a1 == a3):
		            return(a1)
		        else:
		            return(False)
		    elif all(a1 == a3):
		        if all(a2 == a4):
		            return((a1 + a2) / 2)
		        else:
		            return(a1)
		    elif all(a1 == a4):
		        if all(a2 == a3):
		            return((a1 + a2) / 2)
		        else:
		            return(a1)
		    elif all(a2 == a3) or all(a2 == a4):
		        return(p2)
		    try:
		        g, h = solve(transpose([-a2 + a1, a4 - a3]), a1 - a3)
		    except:
		        print(Exception)
		        return(False)
		    else:
		        if 0. < g < 1. and 0. < h < 1.:
		            return(a1 + g * (a2 - a1))
		        else:
		            return(False)
		    return(False)


		def trimfunc(l1, l2):
		    ik = 0
		    i0 = array(l1[0])
		    for i in array(l1[1:]):
		        jk = 0
		        j0 = array(l2[0])
		        for j in array(l2[1:]):
		            s = trim(j0, j, i0, i)
		            if isinstance(s, ndarray):
		                if ik == 0:
		                    l1 = [l1[0]]
		                else:
		                    l1 = l1[:ik]
		                if jk == 0:
		                    l2 == [l2[0]]
		                else:
		                    l2 = l2[jk::-1]
		                return(array([vstack([l1, [s]]), vstack([[s], l2])]))
		            j0 = j
		            jk += 1
		        i0 = i
		        ik += 1
		    return(False)

		def norm(vec1, vec2):
		    vec = array(vec2) - array(vec1)
		    out = 0
		    for i in vec:
		        out += i ** 2
		    return(sqrt(out))

		def nearestpts(evolv, underc):
		    ik = 0
		    iout = 0
		    jout = 0
		    outmin = 1000.
		    for i in array(evolv[1:]):
		        jk = 0
		        for j in array(underc[1:]):
		            l = norm(i, j)
		            if l < outmin:
		                re = norm(i, [0, 0])
		                ru = norm(j, [0, 0])
		                if re > ru:
		                    outmin = l
		                    iout, jout = [ik, jk]
		            jk += 1
		        ik += 1
		    return([vstack([underc[:jout], evolv[iout]]), evolv[iout:]])

		ex = involute_tooth()

	def onDesign20(self):
			doc=App.newDocument()

			# 기본형상
			cir_hex=float(self.numericInput1.text()) #circle_diameter

			d=float(self.numericInput1.text()) #d 조절
			exHex=Part.makeCylinder(cir_hex/2.0,d,Vector(0,0,0))

			# 나사선 helix
			helix = Part.makeHelix(0.797,d,2) #75넣으면 메모리 문제로 실행 안될 수 있음. height 조절하기 #Part.makeHelix(pitch,height,radius,(angle))
			#사다리꼴 단면
			edge1 = Part.makeLine((1.7,0,-0.125), (1.7,0,0.125))
			edge2 = Part.makeLine((1.7,0,0.125), (2.3,0,0.419))
			edge3 = Part.makeLine((2.3,0,0.419), (2.3,0,-0.419))
			edge4 = Part.makeLine((2.3,0,-0.419), (1.7,0,-0.125))
			section = Part.Wire([edge1,edge2,edge3,edge4])
			makeSolid=bool(1)
			isFrenet=bool(1)
			pipe = Part.Wire(helix).makePipeShell([section],makeSolid,isFrenet)

			exHex=exHex.cut(pipe)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=exHex				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(0.5, 0.5, 0.5)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

			#Part.show(exHex)
	def onQuit(self):
		#self.quitButton.clicked.connect(self.close())
		self.close()

ex = Sci()
#ex.show()              #ED-PyCharm
#sys.exit(app.exec_())  #ED-PyCharm
