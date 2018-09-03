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
		self.treeWidget.setHeaderLabels([u"            축계용 기계부품"]) # headerlabel명
		self.treeWidget.setColumnCount(1) # headerlabel 칼럼 갯수

		root1 = QtGui.QTreeWidgetItem(self.treeWidget)
		root1.setText(0,u'축')
		child1 = QtGui.QTreeWidgetItem(root1)
		child1.setText(0,u'중실축의 강도 설계')
		#child1.setText(1,'name1')
		child2 = QtGui.QTreeWidgetItem(root1)
		child2.setText(0,u'중공축의 강도 설계')
		child3 = QtGui.QTreeWidgetItem(root1)
		child3.setText(0,u'중실축의 강성 설계')
		self.treeWidget.addTopLevelItem(root1)

		root2 = QtGui.QTreeWidgetItem(self.treeWidget)
		root2.setText(0,u'축이음')
		child1 = QtGui.QTreeWidgetItem(root2)
		child1.setText(0,u'유니버셜 조인트')

		root3 = QtGui.QTreeWidgetItem(self.treeWidget)
		root3.setText(0,u'축과 보스의 결합')
		child1 = QtGui.QTreeWidgetItem(root3)
		child1.setText(0,u'평행키')
		child2 = QtGui.QTreeWidgetItem(root3)
		child2.setText(0,u'너클핀')

		root4 = QtGui.QTreeWidgetItem(self.treeWidget)
		root4.setText(0,u'베어링')
		child1 = QtGui.QTreeWidgetItem(root4)
		child1.setText(0,u'엔드 저널 베어링')
		child2 = QtGui.QTreeWidgetItem(root4)
		child2.setText(0,u'칼라 베어링')
		child3 = QtGui.QTreeWidgetItem(root4)
		child3.setText(0,u'볼 베어링')
		self.treeWidget.addTopLevelItem(root4)

		self.treeWidget.setGeometry(10, 10, 200, 780)
		self.treeWidget.expandAll()      # 트리 리스트 보여주기
		self.treeWidget.itemClicked.connect(self.clickedItem)

		self.group1 = QtGui.QGroupBox(self)
		self.group1.setGeometry(220, 10, 770, 780)
		self.group1.hide()
		self.group2 = QtGui.QGroupBox(self)
		self.group2.setGeometry(220, 10, 770, 780)
		self.group2.hide()
		self.group3 = QtGui.QGroupBox(self)
		self.group3.setGeometry(220, 10, 770, 780)
		self.group3.hide()
		self.group4 = QtGui.QGroupBox(self)
		self.group4.setGeometry(220, 10, 770, 780)
		self.group4.hide()
		self.group5 = QtGui.QGroupBox(self)
		self.group5.setGeometry(220, 10, 770, 780)
		self.group5.hide()
		self.group6 = QtGui.QGroupBox(self)
		self.group6.setGeometry(220, 10, 770, 780)
		self.group6.hide()
		self.group7 = QtGui.QGroupBox(self)
		self.group7.setGeometry(220, 10, 770, 780)
		self.group7.hide()
		self.group8 = QtGui.QGroupBox(self)
		self.group8.setGeometry(220, 10, 770, 780)
		self.group8.hide()
		self.group9 = QtGui.QGroupBox(self)
		self.group9.setGeometry(220, 10, 770, 780)
		self.group9.hide()

		#mainLayout = QtGui.QHBoxLayout()
		#mainLayout.addWidget(self.treeWidget)

		self.quitButton = QtGui.QPushButton("Quit", self)
		self.quitButton.setFixedWidth(100)
		self.quitButton.move(860,760)
		self.quitButton.setAutoDefault(True)
		self.quitButton.clicked.connect(self.onQuit)

		#self.resize(580,800)
		self.setGeometry(100, 100, 1000,800)
		self.setFixedWidth(1000)
		self.setFixedHeight(800)
		self.setWindowTitle(u"축용 기계부품 설계 SW")
		self.show()

	def clickedItem(self, parent):
		if self.treeWidget.currentItem().text(0) == u"중실축의 강도 설계":
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()

			self.label1 = QtGui.QLabel(u"중실축 (Solid Shaft)의 강도 설계",self.group1)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold; font-size: 12pt;")
			self.label1.move(230,10)
			self.label1.setAlignment(QtCore.Qt.AlignRight)

			self.powergroup = QtGui.QGroupBox(self.group1)
			self.powergroup.setGeometry(QtCore.QRect(30, 70, 340, 115))
			self.powergroup.setTitle(u"작용하는 힘의 종류")
			self.powergroup.setStyleSheet("font-size: 10pt;")
			self.powergroup.setFont('Courier')

			self.r3 = QtGui.QRadioButton(u"굽힘만 작용하는 축",self.powergroup)
			self.r3.move(40,40)
			self.r3.clicked.connect(self.onSelect1)
			self.r4 = QtGui.QRadioButton(u"비틀림만을 받는 축",self.powergroup)
			self.r4.move(40,65)
			self.r4.clicked.connect(self.onSelect2)
			self.r5 = QtGui.QRadioButton(u"굽힘과 비틀림을 동시에 받는 축",self.powergroup)
			self.r5.move(40,90)
			self.r5.clicked.connect(self.onSelect3)
			#self.r3.setChecked(True)

			self.varigroup = QtGui.QGroupBox(self.group1)
			self.varigroup.setGeometry(QtCore.QRect(30, 195, 340, 165))
			self.varigroup.setTitle(u"설계 변수(빨강 : 입력해야 할 변수)")
			self.varigroup.setStyleSheet("font-size: 10pt;")
			self.varigroup.setFont('Courier')
			self.label2 = QtGui.QLabel(u"작용 굽힘 모멘트",self.varigroup)
			self.label2.move(40,40)
			self.numericInput1 = QtGui.QLineEdit(self.varigroup)
			self.numericInput1.setFixedWidth(50)
			self.numericInput1.move(170,35)
			self.popupItems1 = (u"(kN*m)", u"(lbf*ft)")
			self.popup1 = QtGui.QComboBox(self.varigroup)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(u"(kN*m)"))
			self.popup1.move(230, 35)
			self.label3 = QtGui.QLabel(u"작용 비틀림 모멘트",self.varigroup)
			self.label3.move(40,65)
			self.numericInput2 = QtGui.QLineEdit(self.varigroup)
			self.numericInput2.setFixedWidth(50)
			self.numericInput2.move(170,60)
			self.popupItems2 = (u"(kN*m)", u"(lbf*ft)")
			self.popup2 = QtGui.QComboBox(self.varigroup)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(u"(kN*m)"))
			self.popup2.move(230, 60)
			self.label4 = QtGui.QLabel(u"허용굽힘응력",self.varigroup)
			self.label4.move(40,90)
			self.numericInput3 = QtGui.QLineEdit(self.varigroup)
			self.numericInput3.setFixedWidth(50)
			self.numericInput3.move(170,85)
			self.popupItems3 = (u"(MPa)", u"(ksi)")
			self.popup3 = QtGui.QComboBox(self.varigroup)
			self.popup3.addItems(self.popupItems3)
			self.popup3.setCurrentIndex(self.popupItems3.index(u"(MPa)"))
			self.popup3.move(230, 85)
			self.label5 = QtGui.QLabel(u"허용전단응력",self.varigroup)
			self.label5.move(40,115)
			self.numericInput4 = QtGui.QLineEdit(self.varigroup)
			self.numericInput4.setFixedWidth(50)
			self.numericInput4.move(170,110)
			self.popupItems4 = (u"(MPa)", u"(ksi)")
			self.popup4 = QtGui.QComboBox(self.varigroup)
			self.popup4.addItems(self.popupItems4)
			self.popup4.setCurrentIndex(self.popupItems4.index(u"(MPa)"))
			self.popup4.move(230, 110)
			self.designButton = QtGui.QPushButton("Design",self.varigroup)
			self.designButton.clicked.connect(self.onDesign1)
			self.designButton.setFixedWidth(180)
			self.designButton.setAutoDefault(True)
			self.designButton.move(90,135)

			self.resugroup = QtGui.QGroupBox(self.group1)
			self.resugroup.setGeometry(QtCore.QRect(30, 370, 340, 115))
			self.resugroup.setTitle(u"계산 결과값(축의 지름)")
			self.resugroup.setStyleSheet("font-size: 10pt;")
			self.resugroup.setFont('Courier')
			self.label6 = QtGui.QLabel(u"굽힘을 받을 때",self.resugroup)
			self.label6.move(40,40)
			self.numericInput5 = QtGui.QLineEdit(self.resugroup)
			self.numericInput5.setFixedWidth(50)
			self.numericInput5.move(170,35)
			self.popupItems5 = (u"(mm)", u"(inch)")
			self.popup5 = QtGui.QComboBox(self.resugroup)
			self.popup5.addItems(self.popupItems5)
			self.popup5.setCurrentIndex(self.popupItems5.index(u"(mm)"))
			self.popup5.move(230, 35)
			self.label7 = QtGui.QLabel(u"비틀림을 받을 때",self.resugroup)
			self.label7.move(40,65)
			self.numericInput6 = QtGui.QLineEdit(self.resugroup)
			self.numericInput6.setFixedWidth(50)
			self.numericInput6.move(170,60)
			self.popupItems6 = (u"(mm)", u"(inch)")
			self.popup6 = QtGui.QComboBox(self.resugroup)
			self.popup6.addItems(self.popupItems6)
			self.popup6.setCurrentIndex(self.popupItems6.index(u"(mm)"))
			self.popup6.move(230, 60)
			self.label7 = QtGui.QLabel(u"*안전한 큰 쪽의 지름을 선택*",self.resugroup)
			self.label7.setStyleSheet("font-size: 9pt;")
			self.label7.setStyleSheet("color: rgb(255,0,0);")    # 텍스트 색 변환
			self.label7.move(85,95)

			self.modelgroup = QtGui.QGroupBox(self.group1)
			self.modelgroup.setGeometry(QtCore.QRect(30, 505, 340, 135))
			self.modelgroup.setTitle(u"모델링(변수 입력)")
			self.modelgroup.setStyleSheet("font-size: 10pt;")
			self.modelgroup.setFont('Courier')
			self.label8 = QtGui.QLabel(u"축의 길이",self.modelgroup)
			self.label8.setStyleSheet("color: rgb(255,0,0);")
			self.label8.move(40,40)
			self.numericInput7 = QtGui.QLineEdit(self.modelgroup)
			self.numericInput7.setFixedWidth(50)
			self.numericInput7.move(170,35)
			self.popupItems7 = (u"(mm)", u"(inch)")
			self.popup7 = QtGui.QComboBox(self.modelgroup)
			self.popup7.addItems(self.popupItems7)
			self.popup7.setCurrentIndex(self.popupItems7.index(u"(mm)"))
			self.popup7.move(230, 35)
			self.label9 = QtGui.QLabel(u"축의 지름",self.modelgroup)
			self.label9.setStyleSheet("color: rgb(255,0,0);")
			self.label9.move(40,65)
			self.numericInput8 = QtGui.QLineEdit(self.modelgroup)
			self.numericInput8.setFixedWidth(50)
			self.numericInput8.move(170,60)
			self.popupItems8 = (u"(mm)", u"(inch)")
			self.popup8 = QtGui.QComboBox(self.modelgroup)
			self.popup8.addItems(self.popupItems8)
			self.popup8.setCurrentIndex(self.popupItems8.index(u"(mm)"))
			self.popup8.move(230, 60)
			self.generateButton = QtGui.QPushButton("Generate",self.modelgroup)
			self.generateButton.clicked.connect(self.onGenerate1)
			self.generateButton.setFixedWidth(180)
			self.generateButton.setAutoDefault(True)
			self.generateButton.move(90,85)
			self.label10 = QtGui.QLabel(u"*붉은색 변수를 이용하여 모델링함*",self.modelgroup)
			self.label10.setStyleSheet("color: rgb(255,0,0);")
			self.label10.move(70,115)

			self.refer_Img_GroupBox = QtGui.QGroupBox(self.group1)
			self.refer_Img_GroupBox.setGeometry(QtCore.QRect(380, 70, 370, 270))
			self.refer_Img_GroupBox.setTitle(u"중실축")
			self.refer_Img_GroupBox.setStyleSheet("font-size: 10pt;")
			self.refer_Img_GroupBox.setFont('Courier')

			self.side_View_Img = QtGui.QPixmap(os.path.join(addonPath, "shaft_module\Shaft_Model.jpg"))
			self.side_View_label = QtGui.QLabel(self.refer_Img_GroupBox)
			self.side_View_label.setPixmap(self.side_View_Img)
			self.side_View_label.resize(self.side_View_Img.width(), self.side_View_Img.height())
			self.side_View_label.move(95, 15)

			self.refer_Img_GroupBox1 = QtGui.QGroupBox(self.group1)
			self.refer_Img_GroupBox1.setGeometry(QtCore.QRect(380, 350, 370, 300))
			self.refer_Img_GroupBox1.setTitle(u"중실축의 지름 계산 공식")
			self.refer_Img_GroupBox1.setStyleSheet("font-size: 10pt;")
			self.refer_Img_GroupBox1.setFont('Courier')

			self.side_View_Img1 = QtGui.QPixmap(os.path.join(addonPath, "shaft_module\Shaft_Calculation.jpg"))
			self.side_View_label1 = QtGui.QLabel(self.refer_Img_GroupBox1)
			self.side_View_label1.setPixmap(self.side_View_Img1)
			self.side_View_label1.resize(self.side_View_Img1.width(), self.side_View_Img1.height())
			self.side_View_label1.move(10, 30)

			self.group1.show()

		elif self.treeWidget.currentItem().text(0) == u"중공축의 강도 설계":
			self.group1.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()

			self.label1 = QtGui.QLabel(u"중공축 (Hollow Shaft)의 강도 설계",self.group2)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold; font-size: 12pt;")
			self.label1.move(230,10)
			self.label1.setAlignment(QtCore.Qt.AlignRight)

			self.powergroup = QtGui.QGroupBox(self.group2)
			self.powergroup.setGeometry(QtCore.QRect(30, 70, 340, 115))
			self.powergroup.setTitle(u"작용하는 힘의 종류")
			self.powergroup.setStyleSheet("font-size: 10pt;")
			self.powergroup.setFont('Courier')

			self.r3 = QtGui.QRadioButton(u"굽힘만 작용하는 축",self.powergroup)
			self.r3.move(40,40)
			self.r3.clicked.connect(self.onSelect4)
			self.r4 = QtGui.QRadioButton(u"비틀림만을 받는 축",self.powergroup)
			self.r4.move(40,65)
			self.r4.clicked.connect(self.onSelect5)
			self.r5 = QtGui.QRadioButton(u"굽힘과 비틀림을 동시에 받는 축",self.powergroup)
			self.r5.move(40,90)
			self.r5.clicked.connect(self.onSelect6)
			#self.r3.setChecked(True)

			self.varigroup = QtGui.QGroupBox(self.group2)
			self.varigroup.setGeometry(QtCore.QRect(30, 195, 340, 190))
			self.varigroup.setTitle(u"설계 변수(빨강 : 입력해야 할 변수)")
			self.varigroup.setStyleSheet("font-size: 10pt;")
			self.varigroup.setFont('Courier')

			self.label2 = QtGui.QLabel(u"작용 굽힘 모멘트",self.varigroup)
			self.label2.move(40,40)
			self.numericInput1 = QtGui.QLineEdit(self.varigroup)
			self.numericInput1.setFixedWidth(50)
			self.numericInput1.move(170,35)
			self.popupItems1 = (u"(kN*m)", u"(lbf*ft)")
			self.popup1 = QtGui.QComboBox(self.varigroup)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(u"(kN*m)"))
			self.popup1.move(230, 35)
			self.label3 = QtGui.QLabel(u"작용 비틀림 모멘트",self.varigroup)
			self.label3.move(40,65)
			self.numericInput2 = QtGui.QLineEdit(self.varigroup)
			self.numericInput2.setFixedWidth(50)
			self.numericInput2.move(170,60)
			self.popupItems2 = (u"(kN*m)", u"(lbf*ft)")
			self.popup2 = QtGui.QComboBox(self.varigroup)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(u"(kN*m)"))
			self.popup2.move(230, 60)
			self.label4 = QtGui.QLabel(u"허용굽힘응력",self.varigroup)
			self.label4.move(40,90)
			self.numericInput3 = QtGui.QLineEdit(self.varigroup)
			self.numericInput3.setFixedWidth(50)
			self.numericInput3.move(170,85)
			self.popupItems3 = (u"(MPa)", u"(ksi)")
			self.popup3 = QtGui.QComboBox(self.varigroup)
			self.popup3.addItems(self.popupItems3)
			self.popup3.setCurrentIndex(self.popupItems3.index(u"(MPa)"))
			self.popup3.move(230, 85)
			self.label5 = QtGui.QLabel(u"허용전단응력",self.varigroup)
			self.label5.move(40,115)
			self.numericInput4 = QtGui.QLineEdit(self.varigroup)
			self.numericInput4.setFixedWidth(50)
			self.numericInput4.move(170,110)
			self.popupItems4 = (u"(MPa)", u"(ksi)")
			self.popup4 = QtGui.QComboBox(self.varigroup)
			self.popup4.addItems(self.popupItems4)
			self.popup4.setCurrentIndex(self.popupItems4.index(u"(MPa)"))
			self.popup4.move(230, 110)
			self.label6 = QtGui.QLabel(u"지름의 비",self.varigroup)
			self.label6.move(40,140)
			self.numericInput5 = QtGui.QLineEdit(self.varigroup)
			self.numericInput5.setFixedWidth(50)
			self.numericInput5.move(170,135)
			self.designButton = QtGui.QPushButton("Design",self.varigroup)
			self.designButton.clicked.connect(self.onDesign2)
			self.designButton.setFixedWidth(180)
			self.designButton.setAutoDefault(True)
			self.designButton.move(90,160)

			self.resugroup = QtGui.QGroupBox(self.group2)
			self.resugroup.setGeometry(QtCore.QRect(30, 395, 340, 165))
			self.resugroup.setTitle(u"계산 결과값(축의 지름)")
			self.resugroup.setStyleSheet("font-size: 10pt;")
			self.resugroup.setFont('Courier')
			self.label15 = QtGui.QLabel(u"굽힘 적용     바깥지름",self.resugroup)
			self.label15.move(40,40)
			self.numericInput6 = QtGui.QLineEdit(self.resugroup)
			self.numericInput6.setFixedWidth(50)
			self.numericInput6.move(170,35)
			self.popupItems6 = (u"(mm)", u"(inch)")
			self.popup6 = QtGui.QComboBox(self.resugroup)
			self.popup6.addItems(self.popupItems6)
			self.popup6.setCurrentIndex(self.popupItems6.index(u"(mm)"))
			self.popup6.move(230, 35)
			self.label9 = QtGui.QLabel(u"                   안지름",self.resugroup)
			self.label9.move(40,65)
			self.numericInput7 = QtGui.QLineEdit(self.resugroup)
			self.numericInput7.setFixedWidth(50)
			self.numericInput7.move(170,60)
			self.popupItems7 = (u"(mm)", u"(inch)")
			self.popup7 = QtGui.QComboBox(self.resugroup)
			self.popup7.addItems(self.popupItems7)
			self.popup7.setCurrentIndex(self.popupItems7.index(u"(mm)"))
			self.popup7.move(230, 60)
			self.label16 = QtGui.QLabel(u"비틀림 적용 바깥지름",self.resugroup)
			self.label16.move(40,90)
			self.numericInput8 = QtGui.QLineEdit(self.resugroup)
			self.numericInput8.setFixedWidth(50)
			self.numericInput8.move(170,85)
			self.popupItems8 = (u"(mm)", u"(inch)")
			self.popup8 = QtGui.QComboBox(self.resugroup)
			self.popup8.addItems(self.popupItems8)
			self.popup8.setCurrentIndex(self.popupItems8.index(u"(mm)"))
			self.popup8.move(230, 85)
			self.label10 = QtGui.QLabel(u"               안지름",self.resugroup)
			self.label10.move(55,115)
			self.numericInput9 = QtGui.QLineEdit(self.resugroup)
			self.numericInput9.setFixedWidth(50)
			self.numericInput9.move(170,110)
			self.popupItems9 = (u"(mm)", u"(inch)")
			self.popup9 = QtGui.QComboBox(self.resugroup)
			self.popup9.addItems(self.popupItems9)
			self.popup9.setCurrentIndex(self.popupItems9.index(u"(mm)"))
			self.popup9.move(230, 110)
			self.label7 = QtGui.QLabel(u"*안전한 큰 쪽의 지름을 선택*",self.resugroup)
			self.label7.setStyleSheet("font-size: 9pt;")
			self.label7.setStyleSheet("color: rgb(255,0,0);")    # 텍스트 색 변환
			self.label7.move(65,145)

			self.modelgroup = QtGui.QGroupBox(self.group2)
			self.modelgroup.setGeometry(QtCore.QRect(30, 570, 340, 160))
			self.modelgroup.setTitle(u"모델링(변수 입력)")
			self.modelgroup.setStyleSheet("font-size: 10pt;")
			self.modelgroup.setFont('Courier')
			self.label11 = QtGui.QLabel(u"축의 길이",self.modelgroup)
			self.label11.setStyleSheet("color: rgb(255,0,0);")
			self.label11.move(40,40)
			self.numericInput10 = QtGui.QLineEdit(self.modelgroup)
			self.numericInput10.setFixedWidth(50)
			self.numericInput10.move(170,35)
			self.popupItems10 = (u"(mm)", u"(inch)")
			self.popup10 = QtGui.QComboBox(self.modelgroup)
			self.popup10.addItems(self.popupItems10)
			self.popup10.setCurrentIndex(self.popupItems10.index(u"(mm)"))
			self.popup10.move(230, 35)
			self.label12 = QtGui.QLabel(u"축의 바깥지름",self.modelgroup)
			self.label12.setStyleSheet("color: rgb(255,0,0);")
			self.label12.move(40,65)
			self.numericInput11 = QtGui.QLineEdit(self.modelgroup)
			self.numericInput11.setFixedWidth(50)
			self.numericInput11.move(170,60)
			self.popupItems11 = (u"(mm)", u"(inch)")
			self.popup11 = QtGui.QComboBox(self.modelgroup)
			self.popup11.addItems(self.popupItems11)
			self.popup11.setCurrentIndex(self.popupItems11.index(u"(mm)"))
			self.popup11.move(230, 60)
			self.label13 = QtGui.QLabel(u"축의 안지름",self.modelgroup)
			self.label13.setStyleSheet("color: rgb(255,0,0);")
			self.label13.move(40,90)
			self.numericInput12 = QtGui.QLineEdit(self.modelgroup)
			self.numericInput12.setFixedWidth(50)
			self.numericInput12.move(170,85)
			self.popupItems12 = (u"(mm)", u"(inch)")
			self.popup12 = QtGui.QComboBox(self.modelgroup)
			self.popup12.addItems(self.popupItems12)
			self.popup12.setCurrentIndex(self.popupItems12.index(u"(mm)"))
			self.popup12.move(230, 85)
			self.generateButton = QtGui.QPushButton("Generate",self.modelgroup)
			self.generateButton.clicked.connect(self.onGenerate2)
			self.generateButton.setFixedWidth(180)
			self.generateButton.setAutoDefault(True)
			self.generateButton.move(90,110)
			self.label14 = QtGui.QLabel(u"*붉은색 변수를 이용하여 모델링함*",self.modelgroup)
			self.label14.setStyleSheet("color: rgb(255,0,0);")
			self.label14.move(70,140)

			self.refer_Img_GroupBox = QtGui.QGroupBox(self.group2)
			self.refer_Img_GroupBox.setGeometry(QtCore.QRect(380, 70, 370, 270))
			self.refer_Img_GroupBox.setTitle(u"중공축")
			self.refer_Img_GroupBox.setStyleSheet("font-size: 10pt;")
			self.refer_Img_GroupBox.setFont('Courier')

			self.side_View_Img = QtGui.QPixmap(os.path.join(addonPath, "shaft_module\Hollow_Shaft_Model.jpg"))
			self.side_View_label = QtGui.QLabel(self.refer_Img_GroupBox)
			self.side_View_label.setPixmap(self.side_View_Img)
			self.side_View_label.resize(self.side_View_Img.width(), self.side_View_Img.height())
			self.side_View_label.move(110, 20)

			self.refer_Img_GroupBox1 = QtGui.QGroupBox(self.group2)
			self.refer_Img_GroupBox1.setGeometry(QtCore.QRect(380, 350, 370, 300))
			self.refer_Img_GroupBox1.setTitle(u"중공축의 지름 계산 공식")
			self.refer_Img_GroupBox1.setStyleSheet("font-size: 10pt;")
			self.refer_Img_GroupBox1.setFont('Courier')

			self.side_View_Img1 = QtGui.QPixmap(os.path.join(addonPath, "shaft_module\Hollow_Shaft_Calculation.jpg"))
			self.side_View_label1 = QtGui.QLabel(self.refer_Img_GroupBox1)
			self.side_View_label1.setPixmap(self.side_View_Img1)
			self.side_View_label1.resize(self.side_View_Img1.width(), self.side_View_Img1.height())
			self.side_View_label1.move(10, 30)

			self.group2.show()

		elif self.treeWidget.currentItem().text(0) == u"중실축의 강성 설계":
			self.group1.hide()
			self.group2.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()

			self.label1 = QtGui.QLabel(u"중실축(Solid Shaft)의 강성 설계",self.group3)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold; font-size: 12pt;")
			self.label1.move(230,10)
			self.label1.setAlignment(QtCore.Qt.AlignRight)

			self.powergroup = QtGui.QGroupBox(self.group3)
			self.powergroup.setGeometry(QtCore.QRect(30, 70, 340, 100))
			self.powergroup.setTitle(u"재료 및 설계 제한 조건")
			self.powergroup.setStyleSheet("font-size: 10pt;")
			self.powergroup.setFont('Courier')
			self.label2 = QtGui.QLabel(u"Bach의 축공식에 따라",self.powergroup)
			self.label2.setStyleSheet("font: bold;")
			self.label2.move(40,40)
			self.label3 = QtGui.QLabel(u"연강, 허용비틀림각은 1m당 0.25도로 제한",self.powergroup)
			self.label3.setStyleSheet("font: bold;")
			self.label3.move(40,65)

			self.varigroup = QtGui.QGroupBox(self.group3)
			self.varigroup.setGeometry(QtCore.QRect(30, 185, 340, 160))
			self.varigroup.setTitle(u"설계 변수")
			self.varigroup.setStyleSheet("font-size: 10pt;")
			self.varigroup.setFont('Courier')
			self.label4 = QtGui.QLabel(u"회전수",self.varigroup)
			self.label4.move(40,40)
			self.numericInput1 = QtGui.QLineEdit(self.varigroup)
			self.numericInput1.setFixedWidth(50)
			self.numericInput1.move(170,35)
			self.popupItems1 = (u"(rpm)", u"(rad/s)")
			self.popup1 = QtGui.QComboBox(self.varigroup)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(u"(rpm)"))
			self.popup1.move(230, 35)
			self.label5 = QtGui.QLabel(u"동력",self.varigroup)
			self.label5.move(40,65)
			self.numericInput2 = QtGui.QLineEdit(self.varigroup)
			self.numericInput2.setFixedWidth(50)
			self.numericInput2.move(170,60)
			self.popupItems2 = (u"(kW)", u"(HP)")
			self.popup2 = QtGui.QComboBox(self.varigroup)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(u"(kW)"))
			self.popup2.move(230, 60)
			self.label6 = QtGui.QLabel(u"허용전단응력",self.varigroup)
			self.label6.move(40,90)
			self.numericInput3 = QtGui.QLineEdit(self.varigroup)
			self.numericInput3.setFixedWidth(50)
			self.numericInput3.move(170,85)
			self.popupItems3 = (u"(MPa)", u"(ksi)")
			self.popup3 = QtGui.QComboBox(self.varigroup)
			self.popup3.addItems(self.popupItems3)
			self.popup3.setCurrentIndex(self.popupItems3.index(u"(MPa)"))
			self.popup3.move(230, 85)
			self.designButton = QtGui.QPushButton("Design",self.varigroup)
			self.designButton.clicked.connect(self.onDesign3)
			self.designButton.setFixedWidth(180)
			self.designButton.setAutoDefault(True)
			self.designButton.move(90,120)

			self.resugroup = QtGui.QGroupBox(self.group3)
			self.resugroup.setGeometry(QtCore.QRect(30, 360, 340, 125))
			self.resugroup.setTitle(u"계산 결과값(축의 지름)")
			self.resugroup.setStyleSheet("font-size: 10pt;")
			self.resugroup.setFont('Courier')
			self.label7 = QtGui.QLabel(u"비틀림강도로 계산",self.resugroup)
			self.label7.move(40,40)
			self.numericInput4 = QtGui.QLineEdit(self.resugroup)
			self.numericInput4.setFixedWidth(50)
			self.numericInput4.move(170,35)
			self.popupItems4 = (u"(mm)", u"(inch)")
			self.popup4 = QtGui.QComboBox(self.resugroup)
			self.popup4.addItems(self.popupItems4)
			self.popup4.setCurrentIndex(self.popupItems4.index(u"(mm)"))
			self.popup4.move(230, 35)
			self.label8 = QtGui.QLabel(u"비틀림강성로 계산",self.resugroup)
			self.label8.move(40,65)
			self.numericInput5 = QtGui.QLineEdit(self.resugroup)
			self.numericInput5.setFixedWidth(50)
			self.numericInput5.move(170,60)
			self.popupItems5 = (u"(mm)", u"(inch)")
			self.popup5 = QtGui.QComboBox(self.resugroup)
			self.popup5.addItems(self.popupItems5)
			self.popup5.setCurrentIndex(self.popupItems5.index(u"(mm)"))
			self.popup5.move(230, 60)
			self.label9 = QtGui.QLabel(u"*안전한 큰 쪽의 지름을 선택*",self.resugroup)
			self.label9.setStyleSheet("font-size: 9pt;")
			self.label9.setStyleSheet("color: rgb(255,0,0);")    # 텍스트 색 변환
			self.label9.move(85,95)

			self.modelgroup = QtGui.QGroupBox(self.group3)
			self.modelgroup.setGeometry(QtCore.QRect(30, 500, 340, 140))
			self.modelgroup.setTitle(u"모델링(변수 입력)")
			self.modelgroup.setStyleSheet("font-size: 10pt;")
			self.modelgroup.setFont('Courier')
			self.label10 = QtGui.QLabel(u"축의 길이",self.modelgroup)
			self.label10.setStyleSheet("color: rgb(255,0,0);")
			self.label10.move(40,40)
			self.numericInput6 = QtGui.QLineEdit(self.modelgroup)
			self.numericInput6.setFixedWidth(50)
			self.numericInput6.move(170,35)
			self.popupItems6 = (u"(mm)", u"(inch)")
			self.popup6 = QtGui.QComboBox(self.modelgroup)
			self.popup6.addItems(self.popupItems6)
			self.popup6.setCurrentIndex(self.popupItems6.index(u"(mm)"))
			self.popup6.move(230, 35)
			self.label11 = QtGui.QLabel(u"축의 지름",self.modelgroup)
			self.label11.setStyleSheet("color: rgb(255,0,0);")
			self.label11.move(40,65)
			self.numericInput7 = QtGui.QLineEdit(self.modelgroup)
			self.numericInput7.setFixedWidth(50)
			self.numericInput7.move(170,60)
			self.popupItems7 = (u"(mm)", u"(inch)")
			self.popup7 = QtGui.QComboBox(self.modelgroup)
			self.popup7.addItems(self.popupItems7)
			self.popup7.setCurrentIndex(self.popupItems6.index(u"(mm)"))
			self.popup7.move(230, 60)
			self.designButton = QtGui.QPushButton("Generate",self.modelgroup)
			self.designButton.clicked.connect(self.onGenerate3)
			self.designButton.setFixedWidth(180)
			self.designButton.setAutoDefault(True)
			self.designButton.move(90,90)
			self.label12 = QtGui.QLabel(u"*붉은색 변수를 이용하여 모델링함*",self.modelgroup)
			self.label12.setStyleSheet("font-size: 9pt;")
			self.label12.setStyleSheet("color: rgb(255,0,0);")    # 텍스트 색 변환
			self.label12.move(70,120)

			self.refer_Img_GroupBox = QtGui.QGroupBox(self.group3)
			self.refer_Img_GroupBox.setGeometry(QtCore.QRect(380, 70, 370, 270))
			self.refer_Img_GroupBox.setTitle(u"중실축")
			self.refer_Img_GroupBox.setStyleSheet("font-size: 10pt;")
			self.refer_Img_GroupBox.setFont('Courier')

			self.side_View_Img = QtGui.QPixmap(os.path.join(addonPath, "shaft_module\Solid_Shaft_Model.jpg"))
			self.side_View_label = QtGui.QLabel(self.refer_Img_GroupBox)
			self.side_View_label.setPixmap(self.side_View_Img)
			self.side_View_label.resize(self.side_View_Img.width(), self.side_View_Img.height())
			self.side_View_label.move(95, 15)

			self.refer_Img_GroupBox1 = QtGui.QGroupBox(self.group3)
			self.refer_Img_GroupBox1.setGeometry(QtCore.QRect(380, 350, 370, 260))
			self.refer_Img_GroupBox1.setTitle(u"중실축의 지름 계산 공식")
			self.refer_Img_GroupBox1.setStyleSheet("font-size: 10pt;")
			self.refer_Img_GroupBox1.setFont('Courier')

			self.side_View_Img1 = QtGui.QPixmap(os.path.join(addonPath, "shaft_module\Solid_Shaft_Calculation.jpg"))
			self.side_View_label1 = QtGui.QLabel(self.refer_Img_GroupBox1)
			self.side_View_label1.setPixmap(self.side_View_Img1)
			self.side_View_label1.resize(self.side_View_Img1.width(), self.side_View_Img1.height())
			self.side_View_label1.move(10, 30)

			self.group3.show()

		elif self.treeWidget.currentItem().text(0) == u"유니버셜 조인트":
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()

			self.label1 = QtGui.QLabel(u"유니버셜 조인트(Universal Joint) 설계",self.group4)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold; font-size: 12pt;")
			self.label1.move(200,10)
			self.label1.setAlignment(QtCore.Qt.AlignRight)

			self.varigroup = QtGui.QGroupBox(self.group4)
			self.varigroup.setGeometry(QtCore.QRect(30, 70, 340, 150))
			self.varigroup.setTitle(u"기준축의 회전 정보 입력")
			self.varigroup.setStyleSheet("font-size: 10pt;")
			self.varigroup.setFont('Courier')
			self.label2 = QtGui.QLabel(u"조인트 꺽임각", self.varigroup)
			self.label2.setStyleSheet("color: rgb(255,0,0);")
			self.label2.move(40,40)
			self.numericInput2 = QtGui.QLineEdit(self.varigroup)
			self.numericInput2.setFixedWidth(50)
			self.numericInput2.move(170,35)
			self.popupItems2 = (u"(rad)", u"(degree)")
			self.popup2 = QtGui.QComboBox(self.varigroup)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(u"(rad)"))
			self.popup2.move(230, 35)
			self.label3 = QtGui.QLabel(u"기준축 회전각", self.varigroup)

			self.label3.move(40,65)
			self.numericInput3 = QtGui.QLineEdit(self.varigroup)
			self.numericInput3.setFixedWidth(50)
			self.numericInput3.move(170,60)
			self.popupItems3 = (u"(rad)", u"(degree)")
			self.popup3 = QtGui.QComboBox(self.varigroup)
			self.popup3.addItems(self.popupItems3)
			self.popup3.setCurrentIndex(self.popupItems3.index(u"(rad)"))
			self.popup3.move(230, 60)
			self.label4 = QtGui.QLabel(u"기준축 회전속도", self.varigroup)
			self.label4.move(40,90)
			self.numericInput4 = QtGui.QLineEdit(self.varigroup)
			self.numericInput4.setFixedWidth(50)
			self.numericInput4.move(170,85)
			self.popupItems4 = (u"(rpm)", u"(rad/s)")
			self.popup4 = QtGui.QComboBox(self.varigroup)
			self.popup4.addItems(self.popupItems4)
			self.popup4.setCurrentIndex(self.popupItems4.index(u"(rpm)"))
			self.popup4.move(230, 85)
			self.designButton = QtGui.QPushButton("Design", self.varigroup)
			self.designButton.clicked.connect(self.onDesign4)
			self.designButton.setFixedWidth(180)
			self.designButton.setAutoDefault(True)
			self.designButton.move(90,115)

			self.resugroup = QtGui.QGroupBox(self.group4)
			self.resugroup.setGeometry(QtCore.QRect(30, 230, 340, 120))
			self.resugroup.setTitle(u"계산 결과값")
			self.resugroup.setStyleSheet("font-size: 10pt;")
			self.resugroup.setFont('Courier')
			self.label7 = QtGui.QLabel(u"전달축 회전속도",self.resugroup)
			self.label7.move(40,40)
			self.numericInput7 = QtGui.QLineEdit(self.resugroup)
			self.numericInput7.setFixedWidth(50)
			self.numericInput7.move(170,35)
			self.popupItems7 = (u"(rpm)", u"(rad/s)")
			self.popup7 = QtGui.QComboBox(self.resugroup)
			self.popup7.addItems(self.popupItems7)
			self.popup7.setCurrentIndex(self.popupItems7.index(u"(rpm)"))
			self.popup7.move(230, 35)
			self.label8 = QtGui.QLabel(u"전달축 최대회전속도",self.resugroup)
			self.label8.move(40,65)
			self.numericInput8 = QtGui.QLineEdit(self.resugroup)
			self.numericInput8.setFixedWidth(50)
			self.numericInput8.move(170,60)
			self.popupItems8 = (u"(rpm)", u"(rad/s)")
			self.popup8 = QtGui.QComboBox(self.resugroup)
			self.popup8.addItems(self.popupItems8)
			self.popup8.setCurrentIndex(self.popupItems8.index(u"(rpm)"))
			self.popup8.move(230, 60)
			self.label9 = QtGui.QLabel(u"전달축 최소회전속도",self.resugroup)
			self.label9.move(40,90)
			self.numericInput9 = QtGui.QLineEdit(self.resugroup)
			self.numericInput9.setFixedWidth(50)
			self.numericInput9.move(170,85)
			self.popupItems9 = (u"(rpm)", u"(rad/s)")
			self.popup9 = QtGui.QComboBox(self.resugroup)
			self.popup9.addItems(self.popupItems9)
			self.popup9.setCurrentIndex(self.popupItems9.index(u"(rpm)"))
			self.popup9.move(230, 85)

			self.modelgroup = QtGui.QGroupBox(self.group4)
			self.modelgroup.setGeometry(QtCore.QRect(30, 360, 340, 165))
			self.modelgroup.setTitle(u"모델링")
			self.modelgroup.setStyleSheet("font-size: 10pt;")
			self.modelgroup.setFont('Courier')
			self.label10 = QtGui.QLabel(u"기준축 지름",self.modelgroup)
			self.label10.setStyleSheet("color: rgb(255,0,0);")    # 텍스트 색 변환
			self.label10.move(40,40)
			self.numericInput10 = QtGui.QLineEdit(self.modelgroup)
			self.numericInput10.setFixedWidth(50)
			self.numericInput10.move(170,35)
			self.popupItems10 = (u"(mm)", u"(inch)")
			self.popup10 = QtGui.QComboBox(self.modelgroup)
			self.popup10.addItems(self.popupItems10)
			self.popup10.setCurrentIndex(self.popupItems10.index(u"(mm)"))
			self.popup10.move(230, 35)
			self.label11 = QtGui.QLabel(u"기준축 길이",self.modelgroup)
			self.label11.setStyleSheet("color: rgb(255,0,0);")
			self.label11.move(40,65)
			self.numericInput11 = QtGui.QLineEdit(self.modelgroup)
			self.numericInput11.setFixedWidth(50)
			self.numericInput11.move(170,60)
			self.popupItems11 = (u"(mm)", u"(inch)")
			self.popup11 = QtGui.QComboBox(self.modelgroup)
			self.popup11.addItems(self.popupItems11)
			self.popup11.setCurrentIndex(self.popupItems11.index(u"(mm)"))
			self.popup11.move(230, 60)
			self.label12 = QtGui.QLabel(u"전달축 길이",self.modelgroup)
			self.label12.setStyleSheet("color: rgb(255,0,0);")
			self.label12.move(40,90)
			self.numericInput12 = QtGui.QLineEdit(self.modelgroup)
			self.numericInput12.setFixedWidth(50)
			self.numericInput12.move(170,85)
			self.popupItems12 = (u"(mm)", u"(inch)")
			self.popup12 = QtGui.QComboBox(self.modelgroup)
			self.popup12.addItems(self.popupItems12)
			self.popup12.setCurrentIndex(self.popupItems12.index(u"(mm)"))
			self.popup12.move(230, 85)
			self.designButton = QtGui.QPushButton("Generate",self.modelgroup)
			self.designButton.clicked.connect(self.onGenerate4)
			self.designButton.setFixedWidth(180)
			self.designButton.setAutoDefault(True)
			self.designButton.move(90,115)
			self.label13 = QtGui.QLabel(u"*붉은색 변수를 이용하여 모델링함*",self.modelgroup)
			self.label13.setStyleSheet("color: rgb(255,0,0);")    # 텍스트 색 변환
			self.label13.move(70,145)

			self.refer_Img_GroupBox = QtGui.QGroupBox(self.group4)
			self.refer_Img_GroupBox.setGeometry(QtCore.QRect(380, 70, 370, 270))
			self.refer_Img_GroupBox.setTitle(u"유니버셜 조인트")
			self.refer_Img_GroupBox.setStyleSheet("font-size: 10pt;")
			self.refer_Img_GroupBox.setFont('Courier')

			self.side_View_Img = QtGui.QPixmap(os.path.join(addonPath, "shaft_module/Universal_Joint_Model.png"))
			self.side_View_label = QtGui.QLabel(self.refer_Img_GroupBox)
			self.side_View_label.setPixmap(self.side_View_Img)
			self.side_View_label.resize(self.side_View_Img.width(), self.side_View_Img.height())
			self.side_View_label.move(50, 25)

			self.refer_Img_GroupBox1 = QtGui.QGroupBox(self.group4)
			self.refer_Img_GroupBox1.setGeometry(QtCore.QRect(380, 350, 370, 280))
			self.refer_Img_GroupBox1.setTitle(u"유니버셜 조인트 계산 공식")
			self.refer_Img_GroupBox1.setStyleSheet("font-size: 10pt;")
			self.refer_Img_GroupBox1.setFont('Courier')

			self.side_View_Img1 = QtGui.QPixmap(os.path.join(addonPath, "shaft_module/Universal_Joint_Calculation.png"))
			self.side_View_label1 = QtGui.QLabel(self.refer_Img_GroupBox1)
			self.side_View_label1.setPixmap(self.side_View_Img1)
			self.side_View_label1.resize(self.side_View_Img1.width(), self.side_View_Img1.height())
			self.side_View_label1.move(10, 30)

			self.group4.show()

		elif self.treeWidget.currentItem().text(0) == u"평행키":
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()

			self.label1 = QtGui.QLabel(u"평행키(Parallel Key)의 길이 설계", self.group5)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold; font-size: 12pt;")
			self.label1.move(210,10)
			self.label1.setAlignment(QtCore.Qt.AlignRight)

			self.varigroup = QtGui.QGroupBox(self.group5)
			self.varigroup.setGeometry(QtCore.QRect(30, 70, 340, 340))
			self.varigroup.setTitle(u"설계 변수")
			self.varigroup.setStyleSheet("font-size: 10pt;")
			self.varigroup.setFont('Courier')
			self.label2 = QtGui.QLabel(u"축 지름", self.varigroup)
			self.label2.move(40,40)
			self.numericInput2 = QtGui.QLineEdit(self.varigroup)
			self.numericInput2.setFixedWidth(50)
			self.numericInput2.move(170,35)
			self.popupItems2 = (u"(mm)", u"(inch)")
			self.popup2 = QtGui.QComboBox(self.varigroup)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(u"(mm)"))
			self.popup2.move(230, 35)
			self.tableButton = QtGui.QPushButton(u"평행키 table", self.varigroup)
			self.tableButton.clicked.connect(self.onTable5_1)
			self.tableButton.setFixedWidth(180)
			self.tableButton.setAutoDefault(True)
			self.tableButton.move(90,60)
			self.label3 = QtGui.QLabel(u"키의 폭", self.varigroup)
			self.label3.setStyleSheet("color: rgb(255,0,0);")
			self.label3.move(40,95)
			self.numericInput3 = QtGui.QLineEdit(self.varigroup)
			self.numericInput3.setFixedWidth(50)
			self.numericInput3.move(170,90)
			self.popupItems3 = (u"(mm)", u"(inch)")
			self.popup3 = QtGui.QComboBox(self.varigroup)
			self.popup3.addItems(self.popupItems3)
			self.popup3.setCurrentIndex(self.popupItems3.index(u"(mm)"))
			self.popup3.move(230, 90)
			self.label4 = QtGui.QLabel(u"키의 높이", self.varigroup)
			self.label4.setStyleSheet("color: rgb(255,0,0);")
			self.label4.move(40,120)
			self.numericInput4 = QtGui.QLineEdit(self.varigroup)
			self.numericInput4.setFixedWidth(50)
			self.numericInput4.move(170,115)
			self.popupItems4 = (u"(mm)", u"(inch)")
			self.popup4 = QtGui.QComboBox(self.varigroup)
			self.popup4.addItems(self.popupItems4)
			self.popup4.setCurrentIndex(self.popupItems4.index(u"(mm)"))
			self.popup4.move(230, 115)
			self.label5 = QtGui.QLabel(u"t1", self.varigroup)
			self.label5.move(40,145)
			self.numericInput5 = QtGui.QLineEdit(self.varigroup)
			self.numericInput5.setFixedWidth(50)
			self.numericInput5.move(170,140)
			self.popupItems5 = (u"(mm)", u"(inch)")
			self.popup5 = QtGui.QComboBox(self.varigroup)
			self.popup5.addItems(self.popupItems5)
			self.popup5.setCurrentIndex(self.popupItems5.index(u"(mm)"))
			self.popup5.move(230, 140)
			self.label6 = QtGui.QLabel(u"회전속력", self.varigroup)
			self.label6.move(40,170)
			self.numericInput6 = QtGui.QLineEdit(self.varigroup)
			self.numericInput6.setFixedWidth(50)
			self.numericInput6.move(170,165)
			self.popupItems6 = (u"(rpm)", u"(rad/s)")
			self.popup6 = QtGui.QComboBox(self.varigroup)
			self.popup6.addItems(self.popupItems6)
			self.popup6.setCurrentIndex(self.popupItems6.index(u"(rpm)"))
			self.popup6.move(230, 165)
			self.label7 = QtGui.QLabel(u"전달 동력", self.varigroup)
			self.label7.move(40,195)
			self.numericInput7 = QtGui.QLineEdit(self.varigroup)
			self.numericInput7.setFixedWidth(50)
			self.numericInput7.move(170,190)
			self.popupItems1 = (u"(kW)", u"(HP)")
			self.popup1 = QtGui.QComboBox(self.varigroup)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(u"(kW)"))
			self.popup1.move(230, 190)
			self.label8 = QtGui.QLabel(u"허용전단응력", self.varigroup)
			self.label8.move(40,220)
			self.numericInput8 = QtGui.QLineEdit(self.varigroup)
			self.numericInput8.setFixedWidth(50)
			self.numericInput8.move(170,215)
			self.popupItems8 = (u"(MPa)", u"(ksi)")
			self.popup8 = QtGui.QComboBox(self.varigroup)
			self.popup8.addItems(self.popupItems8)
			self.popup8.setCurrentIndex(self.popupItems8.index(u"(MPa)"))
			self.popup8.move(230, 215)
			self.label9 = QtGui.QLabel(u"허용압축응력", self.varigroup)
			self.label9.move(40,245)
			self.numericInput9 = QtGui.QLineEdit(self.varigroup)
			self.numericInput9.setFixedWidth(50)
			self.numericInput9.move(170,240)
			self.popupItems9 = (u"(MPa)", u"(ksi)")
			self.popup9 = QtGui.QComboBox(self.varigroup)
			self.popup9.addItems(self.popupItems9)
			self.popup9.setCurrentIndex(self.popupItems9.index(u"(MPa)"))
			self.popup9.move(230, 240)
			self.tableButton = QtGui.QPushButton(u"허용 응력 table", self.varigroup)
			self.tableButton.clicked.connect(self.onTable5_2)
			self.tableButton.setFixedWidth(180)
			self.tableButton.setAutoDefault(True)
			self.tableButton.move(90,270)
			self.designButton = QtGui.QPushButton("Design", self.varigroup)
			self.designButton.clicked.connect(self.onDesign5)
			self.designButton.setFixedWidth(180)
			self.designButton.setAutoDefault(True)
			self.designButton.move(90,300)

			# Result group
			self.resultgroup = QtGui.QGroupBox(self.group5)
			self.resultgroup.setGeometry(QtCore.QRect(30, 420, 340, 105))
			self.resultgroup.setTitle(u"계산 결과값 (받는 힘에 따른 최소 키의 길이)")
			self.resultgroup.setStyleSheet("font-size: 10pt;")
			self.resultgroup.setFont('Courier')
			self.r1 = QtGui.QRadioButton(u" 전단력 적용", self.resultgroup)
			self.r1.move(40,40)
			self.r1.setChecked(True)
			self.numericInput10 = QtGui.QLineEdit(self.resultgroup)
			self.numericInput10.setFixedWidth(50)
			self.numericInput10.move(170,35)
			self.popupItems10 = (u"(mm)", u"(inch)")
			self.popup10 = QtGui.QComboBox(self.resultgroup)
			self.popup10.addItems(self.popupItems10)
			self.popup10.setCurrentIndex(self.popupItems10.index(u"(mm)"))
			self.popup10.move(230, 35)
			self.r2 = QtGui.QRadioButton(u" 압축력 적용", self.resultgroup)
			self.r2.move(40,65)
			self.numericInput11 = QtGui.QLineEdit(self.resultgroup)
			self.numericInput11.setFixedWidth(50)
			self.numericInput11.move(170,60)
			self.popupItems11 = (u"(mm)", u"(inch)")
			self.popup11 = QtGui.QComboBox(self.resultgroup)
			self.popup11.addItems(self.popupItems11)
			self.popup11.setCurrentIndex(self.popupItems11.index(u"(mm)"))
			self.popup11.move(230, 60)

			# Modeling group
			self.modelinggroup = QtGui.QGroupBox(self.group5)
			self.modelinggroup.setGeometry(QtCore.QRect(30, 530, 340, 125))
			self.modelinggroup.setTitle(u"모델링")
			self.modelinggroup.setStyleSheet("font-size: 10pt;")
			self.modelinggroup.setFont('Courier')
			self.label12 = QtGui.QLabel(u"키 길이", self.modelinggroup)
			self.label12.setStyleSheet("color: rgb(255,0,0);")
			self.label12.move(40,40)
			self.numericInput12 = QtGui.QLineEdit(self.modelinggroup)
			self.numericInput12.setFixedWidth(50)
			self.numericInput12.move(170,35)
			self.popupItems12 = (u"(mm)", u"(inch)")
			self.popup12 = QtGui.QComboBox(self.modelinggroup)
			self.popup12.addItems(self.popupItems12)
			self.popup12.setCurrentIndex(self.popupItems12.index(u"(mm)"))
			self.popup12.move(230, 35)
			self.generateButton = QtGui.QPushButton("Generate", self.modelinggroup)
			self.generateButton.clicked.connect(self.onGenerate5)
			self.generateButton.setFixedWidth(180)
			self.generateButton.setAutoDefault(True)
			self.generateButton.move(90,65)
			self.label13 = QtGui.QLabel(u"*붉은색 변수를 이용하여 모델링함*",self.modelinggroup)
			self.label13.setStyleSheet("color: rgb(255,0,0);")
			self.label13.move(70,95)

			self.refer_Img_GroupBox1 = QtGui.QGroupBox(self.group5)
			self.refer_Img_GroupBox1.setGeometry(QtCore.QRect(380, 70, 370, 270))
			self.refer_Img_GroupBox1.setTitle(u"평행키")
			self.refer_Img_GroupBox1.setStyleSheet("font-size: 10pt;")
			self.refer_Img_GroupBox1.setFont('Courier')

			self.side_View_Img1 = QtGui.QPixmap(os.path.join(addonPath, "shaft_module\Key_Model.jpg"))
			self.side_View_label1 = QtGui.QLabel(self.refer_Img_GroupBox1)
			self.side_View_label1.setPixmap(self.side_View_Img1)
			self.side_View_label1.resize(self.side_View_Img1.width(), self.side_View_Img1.height())
			self.side_View_label1.move(95, 30)

			self.refer_Img_GroupBox2 = QtGui.QGroupBox(self.group5)
			self.refer_Img_GroupBox2.setGeometry(QtCore.QRect(380, 360, 370, 250))
			self.refer_Img_GroupBox2.setTitle(u"계산 공식")
			self.refer_Img_GroupBox2.setStyleSheet("font-size: 10pt;")
			self.refer_Img_GroupBox2.setFont('Courier')

			self.side_View_Img2 = QtGui.QPixmap(os.path.join(addonPath, "shaft_module\Key_Calculation.jpg"))
			self.side_View_label2 = QtGui.QLabel(self.refer_Img_GroupBox2)
			self.side_View_label2.setPixmap(self.side_View_Img2)
			self.side_View_label2.resize(self.side_View_Img2.width(), self.side_View_Img2.height())
			self.side_View_label2.move(10, 30)

			self.group5.show()

		elif self.treeWidget.currentItem().text(0) == u"너클핀":
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group7.hide()
			self.group8.hide()
			self.group9.hide()

			self.label1 = QtGui.QLabel(u"너클핀의 길이 설계", self.group6)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold; font-size: 12pt;")
			self.label1.move(310,10)
			self.label1.setAlignment(QtCore.Qt.AlignRight)

			# Variable Group
			self.varigroup = QtGui.QGroupBox(self.group6)
			self.varigroup.setGeometry(QtCore.QRect(30, 70, 340, 195))
			self.varigroup.setTitle(u"설계 변수")
			self.varigroup.setStyleSheet("font-size: 10pt;")
			self.varigroup.setFont('Courier')
			self.label2 = QtGui.QLabel(u"인장 하중", self.varigroup)
			self.label2.move(40,40)
			self.numericInput2 = QtGui.QLineEdit(self.varigroup)
			self.numericInput2.setFixedWidth(50)
			self.numericInput2.move(170,35)
			self.popupItems2 = (u"(kN)", u"(lbf)")
			self.popup2 = QtGui.QComboBox(self.varigroup)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(u"(kN)"))
			self.popup2.move(230, 35)
			self.label3 = QtGui.QLabel(u"허용전단응력", self.varigroup)
			self.label3.move(40,65)
			self.numericInput3 = QtGui.QLineEdit(self.varigroup)
			self.numericInput3.setFixedWidth(50)
			self.numericInput3.move(170,60)
			self.popupItems3 = (u"(MPa)", u"(ksi)")
			self.popup3 = QtGui.QComboBox(self.varigroup)
			self.popup3.addItems(self.popupItems3)
			self.popup3.setCurrentIndex(self.popupItems3.index(u"(MPa)"))
			self.popup3.move(230, 60)
			self.label4 = QtGui.QLabel(u"허용면압", self.varigroup)
			self.label4.move(40,90)
			self.numericInput4 = QtGui.QLineEdit(self.varigroup)
			self.numericInput4.setFixedWidth(50)
			self.numericInput4.move(170,85)
			self.popupItems4 = (u"(MPa)", u"(ksi)")
			self.popup4 = QtGui.QComboBox(self.varigroup)
			self.popup4.addItems(self.popupItems4)
			self.popup4.setCurrentIndex(self.popupItems4.index(u"(MPa)"))
			self.popup4.move(230, 85)
			self.label5 = QtGui.QLabel(u"아이 길이", self.varigroup)
			self.label5.setStyleSheet("color: rgb(255,0,0);")
			self.label5.move(40,115)
			self.numericInput5 = QtGui.QLineEdit(self.varigroup)
			self.numericInput5.setFixedWidth(50)
			self.numericInput5.move(170,110)
			self.popupItems5 = (u"(mm)", u"(inch)")
			self.popup5 = QtGui.QComboBox(self.varigroup)
			self.popup5.addItems(self.popupItems5)
			self.popup5.setCurrentIndex(self.popupItems5.index(u"(mm)"))
			self.popup5.move(230, 110)
			self.label6 = QtGui.QLabel(u"포크 길이", self.varigroup)
			self.label6.setStyleSheet("color: rgb(255,0,0);")
			self.label6.move(40,140)
			self.numericInput6 = QtGui.QLineEdit(self.varigroup)
			self.numericInput6.setFixedWidth(50)
			self.numericInput6.move(170,135)
			self.popupItems6 = (u"(mm)", u"(inch)")
			self.popup6 = QtGui.QComboBox(self.varigroup)
			self.popup6.addItems(self.popupItems6)
			self.popup6.setCurrentIndex(self.popupItems6.index(u"(mm)"))
			self.popup6.move(230, 135)
			self.designButton = QtGui.QPushButton("Design", self.varigroup)
			self.designButton.clicked.connect(self.onDesign6)
			self.designButton.setFixedWidth(180)
			self.designButton.setAutoDefault(True)
			self.designButton.move(90,165)

			# Result group
			self.resultgroup = QtGui.QGroupBox(self.group6)
			self.resultgroup.setGeometry(QtCore.QRect(30, 275, 340, 130))
			self.resultgroup.setTitle(u"계산 결과값 (포크의 필요 지름)")
			self.resultgroup.setStyleSheet("font-size: 10pt;")
			self.resultgroup.setFont('Courier')
			self.r1 = QtGui.QRadioButton(u" 허용전단 기준", self.resultgroup)
			self.r1.move(40,40)
			self.r1.setChecked(True)
			self.numericInput7 = QtGui.QLineEdit(self.resultgroup)
			self.numericInput7.setFixedWidth(50)
			self.numericInput7.move(170,35)
			self.popupItems7 = (u"(mm)", u"(inch)")
			self.popup7 = QtGui.QComboBox(self.resultgroup)
			self.popup7.addItems(self.popupItems7)
			self.popup7.setCurrentIndex(self.popupItems7.index(u"(mm)"))
			self.popup7.move(230, 35)
			self.r2 = QtGui.QRadioButton(u" 아이의 면압 기준", self.resultgroup)
			self.r2.move(40,65)
			self.numericInput8 = QtGui.QLineEdit(self.resultgroup)
			self.numericInput8.setFixedWidth(50)
			self.numericInput8.move(170,60)
			self.popupItems8 = (u"(mm)", u"(inch)")
			self.popup8 = QtGui.QComboBox(self.resultgroup)
			self.popup8.addItems(self.popupItems8)
			self.popup8.setCurrentIndex(self.popupItems8.index(u"(mm)"))
			self.popup8.move(230, 60)
			self.r3 = QtGui.QRadioButton(u" 포크의 면압 기준", self.resultgroup)
			self.r3.move(40,90)
			self.numericInput9 = QtGui.QLineEdit(self.resultgroup)
			self.numericInput9.setFixedWidth(50)
			self.numericInput9.move(170,85)
			self.popupItems9 = (u"(mm)", u"(inch)")
			self.popup9 = QtGui.QComboBox(self.resultgroup)
			self.popup9.addItems(self.popupItems9)
			self.popup9.setCurrentIndex(self.popupItems9.index(u"(mm)"))
			self.popup9.move(230, 85)

			# Modeling group
			self.modelinggroup = QtGui.QGroupBox(self.group6)
			self.modelinggroup.setGeometry(QtCore.QRect(30, 415, 340, 115))
			self.modelinggroup.setTitle(u"모델링")
			self.modelinggroup.setStyleSheet("font-size: 10pt;")
			self.modelinggroup.setFont('Courier')
			self.label10 = QtGui.QLabel(u"포크 지름", self.modelinggroup)
			self.label10.setStyleSheet("color: rgb(255,0,0);")
			self.label10.move(40,40)
			self.numericInput10 = QtGui.QLineEdit(self.modelinggroup)
			self.numericInput10.setFixedWidth(50)
			self.numericInput10.move(170,35)
			self.popupItems10 = (u"(mm)", u"(inch)")
			self.popup10 = QtGui.QComboBox(self.modelinggroup)
			self.popup10.addItems(self.popupItems10)
			self.popup10.setCurrentIndex(self.popupItems10.index(u"(mm)"))
			self.popup10.move(230, 35)
			self.generateButton = QtGui.QPushButton("Generate", self.modelinggroup)
			self.generateButton.clicked.connect(self.onGenerate6)
			self.generateButton.setFixedWidth(180)
			self.generateButton.setAutoDefault(True)
			self.generateButton.move(90,65)
			self.label11 = QtGui.QLabel(u"*붉은색 변수를 이용하여 모델링함*",self.modelinggroup)
			self.label11.setStyleSheet("color: rgb(255,0,0);")
			self.label11.move(70,95)

			# A Sample Picture
			self.refer_Img_GroupBox1 = QtGui.QGroupBox(self.group6)
			self.refer_Img_GroupBox1.setGeometry(QtCore.QRect(380, 70, 370, 270))
			self.refer_Img_GroupBox1.setTitle(u"평행키")
			self.refer_Img_GroupBox1.setStyleSheet("font-size: 10pt;")
			self.refer_Img_GroupBox1.setFont('Courier')

			self.side_View_Img1 = QtGui.QPixmap(os.path.join(addonPath, "shaft_module\Pin_model.jpg"))
			self.side_View_label1 = QtGui.QLabel(self.refer_Img_GroupBox1)
			self.side_View_label1.setPixmap(self.side_View_Img1)
			self.side_View_label1.resize(self.side_View_Img1.width(), self.side_View_Img1.height())
			self.side_View_label1.move(95, 30)

			# Calcultation method
			self.refer_Img_GroupBox2 = QtGui.QGroupBox(self.group6)
			self.refer_Img_GroupBox2.setGeometry(QtCore.QRect(380, 360, 370, 330))
			self.refer_Img_GroupBox2.setTitle(u"계산 공식")
			self.refer_Img_GroupBox2.setStyleSheet("font-size: 10pt;")
			self.refer_Img_GroupBox2.setFont('Courier')

			self.side_View_Img2 = QtGui.QPixmap(os.path.join(addonPath, "shaft_module\Pin_Calculation.jpg"))
			self.side_View_label2 = QtGui.QLabel(self.refer_Img_GroupBox2)
			self.side_View_label2.setPixmap(self.side_View_Img2)
			self.side_View_label2.resize(self.side_View_Img2.width(), self.side_View_Img2.height())
			self.side_View_label2.move(10, 30)

			self.group6.show()

		elif self.treeWidget.currentItem().text(0) == u"엔드 저널 베어링":
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group8.hide()
			self.group9.hide()

			self.label1 = QtGui.QLabel(u"엔드 저널 베어링 설계",self.group7)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold; font-size: 12pt;")
			self.label1.move(290,10)
			self.label1.setAlignment(QtCore.Qt.AlignRight)

			self.varigroup = QtGui.QGroupBox(self.group7)
			self.varigroup.setGeometry(QtCore.QRect(30, 70, 340, 175))
			self.varigroup.setTitle(u"설계 변수")
			self.varigroup.setStyleSheet("font-size: 10pt;")
			self.varigroup.setFont('Courier')
			self.label2 = QtGui.QLabel(u"회전수",self.varigroup)
			self.label2.move(40,40)
			self.numericInput1 = QtGui.QLineEdit(self.varigroup)
			self.numericInput1.setFixedWidth(50)
			self.numericInput1.move(170,35)
			self.popupItems1 = (u"(rpm)", u"(rad/s)")
			self.popup1 = QtGui.QComboBox(self.varigroup)
			self.popup1.addItems(self.popupItems1)
			self.popup1.setCurrentIndex(self.popupItems1.index(u"(rpm)"))
			self.popup1.move(230, 35)
			self.label3 = QtGui.QLabel(u"하중",self.varigroup)
			self.label3.move(40,65)
			self.numericInput2 = QtGui.QLineEdit(self.varigroup)
			self.numericInput2.setFixedWidth(50)
			self.numericInput2.move(170,60)
			self.popupItems2 = (u"(kN)", u"(lbf)")
			self.popup2 = QtGui.QComboBox(self.varigroup)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(u"(kN)"))
			self.popup2.move(230, 60)
			self.label4 = QtGui.QLabel(u"압력속도계수",self.varigroup)
			self.label4.move(40,90)
			self.numericInput3 = QtGui.QLineEdit(self.varigroup)
			self.numericInput3.setFixedWidth(50)
			self.numericInput3.move(170,85)
			self.popupItems3 = (u"(MPa*m/s)", u"( )")
			self.popup3 = QtGui.QComboBox(self.varigroup)
			self.popup3.addItems(self.popupItems3)
			self.popup3.setCurrentIndex(self.popupItems3.index(u"(MPa*m/s)"))
			self.popup3.move(230, 85)
			self.label5 = QtGui.QLabel(u"허용굽힘응력",self.varigroup)
			self.label5.move(40,115)
			self.numericInput4 = QtGui.QLineEdit(self.varigroup)
			self.numericInput4.setFixedWidth(50)
			self.numericInput4.move(170,110)
			self.popupItems4 = (u"(MPa)", u"(ksi)")
			self.popup4 = QtGui.QComboBox(self.varigroup)
			self.popup4.addItems(self.popupItems4)
			self.popup4.setCurrentIndex(self.popupItems4.index(u"(MPa)"))
			self.popup4.move(230, 110)
			self.designButton = QtGui.QPushButton("Design",self.varigroup)
			self.designButton.clicked.connect(self.onDesign7)
			self.designButton.setFixedWidth(180)
			self.designButton.setAutoDefault(True)
			self.designButton.move(90,145)


			self.resugroup = QtGui.QGroupBox(self.group7)
			self.resugroup.setGeometry(QtCore.QRect(30, 255, 340, 140))
			self.resugroup.setTitle(u"계산 결과값")
			self.resugroup.setStyleSheet("font-size: 10pt;")
			self.resugroup.setFont('Courier')
			self.label6 = QtGui.QLabel(u"저널의 길이",self.resugroup)
			self.label6.move(40,40)
			self.numericInput5 = QtGui.QLineEdit(self.resugroup)
			self.numericInput5.setFixedWidth(50)
			self.numericInput5.move(170,35)
			self.popupItems5 = (u"(mm)", u"(inch)")
			self.popup5 = QtGui.QComboBox(self.resugroup)
			self.popup5.addItems(self.popupItems5)
			self.popup5.setCurrentIndex(self.popupItems5.index(u"(mm)"))
			self.popup5.move(230, 35)
			self.label7 = QtGui.QLabel(u"저널의 지름",self.resugroup)
			self.label7.move(40,65)
			self.numericInput6 = QtGui.QLineEdit(self.resugroup)
			self.numericInput6.setFixedWidth(50)
			self.numericInput6.move(170,60)
			self.popupItems6 = (u"(mm)", u"(inch)")
			self.popup6 = QtGui.QComboBox(self.resugroup)
			self.popup6.addItems(self.popupItems6)
			self.popup6.setCurrentIndex(self.popupItems6.index(u"(mm)"))
			self.popup6.move(230, 60)
			self.label8 = QtGui.QLabel(u"평균압력",self.resugroup)
			self.label8.move(40,90)
			self.numericInput7 = QtGui.QLineEdit(self.resugroup)
			self.numericInput7.setFixedWidth(50)
			self.numericInput7.move(170,85)
			self.popupItems7 = (u"(MPa)", u"(ksi)")
			self.popup7 = QtGui.QComboBox(self.resugroup)
			self.popup7.addItems(self.popupItems7)
			self.popup7.setCurrentIndex(self.popupItems7.index(u"(MPa)"))
			self.popup7.move(230, 85)

			self.modelgroup = QtGui.QGroupBox(self.group7)
			self.modelgroup.setGeometry(QtCore.QRect(30, 415, 340, 150))
			self.modelgroup.setTitle(u"모델링")
			self.modelgroup.setStyleSheet("font-size: 10pt;")
			self.modelgroup.setFont('Courier')

			self.label9 = QtGui.QLabel(u"저널의 길이",self.modelgroup)
			self.label9.move(40,40)
			self.numericInput8 = QtGui.QLineEdit(self.modelgroup)
			self.numericInput8.setFixedWidth(50)
			self.numericInput8.move(170,35)
			self.popupItems8 = (u"(mm)", u"(inch)")
			self.popup8 = QtGui.QComboBox(self.modelgroup)
			self.popup8.addItems(self.popupItems8)
			self.popup8.setCurrentIndex(self.popupItems8.index(u"(mm)"))
			self.popup8.move(230, 35)
			self.label10 = QtGui.QLabel(u"저널의 지름",self.modelgroup)
			self.label10.move(40,65)
			self.numericInput9 = QtGui.QLineEdit(self.modelgroup)
			self.numericInput9.setFixedWidth(50)
			self.numericInput9.move(170,60)
			self.popupItems9 = (u"(mm)", u"(inch)")
			self.popup9 = QtGui.QComboBox(self.modelgroup)
			self.popup9.addItems(self.popupItems9)
			self.popup9.setCurrentIndex(self.popupItems9.index(u"(mm)"))
			self.popup9.move(230, 60)

			self.generateButton = QtGui.QPushButton("Generate",self.modelgroup)
			self.generateButton.clicked.connect(self.onGenerate7)
			self.generateButton.setFixedWidth(180)
			self.generateButton.setAutoDefault(True)
			self.generateButton.move(90,100)
			self.label8 = QtGui.QLabel(u"*붉은색 변수를 이용하여 모델링함*",self.modelgroup)
			self.label8.setStyleSheet("color: rgb(255,0,0);")
			self.label8.move(70,130)


			self.refer_Img_GroupBox = QtGui.QGroupBox(self.group7)
			self.refer_Img_GroupBox.setGeometry(QtCore.QRect(380, 70, 370, 270))
			self.refer_Img_GroupBox.setTitle(u"엔드 저널 베어링")
			self.refer_Img_GroupBox.setStyleSheet("font-size: 10pt;")
			self.refer_Img_GroupBox.setFont('Courier')

			self.side_View_Img = QtGui.QPixmap(os.path.join(addonPath, "shaft_module\end.jpg"))
			self.side_View_label = QtGui.QLabel(self.refer_Img_GroupBox)
			self.side_View_label.setPixmap(self.side_View_Img)
			self.side_View_label.resize(self.side_View_Img.width(), self.side_View_Img.height())
			self.side_View_label.move(105, 30)

			self.refer_Img_GroupBox1 = QtGui.QGroupBox(self.group7)
			self.refer_Img_GroupBox1.setGeometry(QtCore.QRect(380, 350, 370, 300))
			self.refer_Img_GroupBox1.setTitle(u"중실축의 지름 계산 공식")
			self.refer_Img_GroupBox1.setStyleSheet("font-size: 10pt;")
			self.refer_Img_GroupBox1.setFont('Courier')

			self.side_View_Img1 = QtGui.QPixmap(os.path.join(addonPath, "shaft_module\endfor.jpg"))
			self.side_View_label1 = QtGui.QLabel(self.refer_Img_GroupBox1)
			self.side_View_label1.setPixmap(self.side_View_Img1)
			self.side_View_label1.resize(self.side_View_Img1.width(), self.side_View_Img1.height())
			self.side_View_label1.move(30, 30)
			self.group7.show()

		elif self.treeWidget.currentItem().text(0) == u"칼라 베어링":
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group9.hide()

			self.label1 = QtGui.QLabel(u"칼라 베어링",self.group8)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold; font-size: 12pt;")
			self.label1.move(330,10)
			self.label1.setAlignment(QtCore.Qt.AlignRight)

			self.varigroup = QtGui.QGroupBox(self.group8)
			self.varigroup.setGeometry(QtCore.QRect(30, 70, 340, 175))
			self.varigroup.setTitle(u"설계 변수")
			self.varigroup.setStyleSheet("font-size: 10pt;")
			self.varigroup.setFont('Courier')

			self.label3 = QtGui.QLabel(u"축방향하중",self.varigroup)
			self.label3.move(40,40)
			self.numericInput2 = QtGui.QLineEdit(self.varigroup)
			self.numericInput2.setFixedWidth(50)
			self.numericInput2.move(170,35)
			self.popupItems2 = (u"(N)", u"(lbf)")
			self.popup2 = QtGui.QComboBox(self.varigroup)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(u"(N)"))
			self.popup2.move(230, 35)
			self.label4 = QtGui.QLabel(u"베어링의 안지름",self.varigroup)
			self.label4.setStyleSheet("color: rgb(255,0,0);")
			self.label4.move(40,65)
			self.numericInput3 = QtGui.QLineEdit(self.varigroup)
			self.numericInput3.setFixedWidth(50)
			self.numericInput3.move(170,60)
			self.popupItems3 = (u"(mm)", u"(inch)")
			self.popup3 = QtGui.QComboBox(self.varigroup)
			self.popup3.addItems(self.popupItems3)
			self.popup3.setCurrentIndex(self.popupItems3.index(u"(mm)"))
			self.popup3.move(230, 60)
			self.label5 = QtGui.QLabel(u"칼라의 수",self.varigroup)
			self.label5.setStyleSheet("color: rgb(255,0,0);")
			self.label5.move(40,90)
			self.numericInput4 = QtGui.QLineEdit(self.varigroup)
			self.numericInput4.setFixedWidth(50)
			self.numericInput4.move(170,85)
			self.label6 = QtGui.QLabel(u"허용베어링압력",self.varigroup)
			self.label6.move(40,115)
			self.numericInput5 = QtGui.QLineEdit(self.varigroup)
			self.numericInput5.setFixedWidth(50)
			self.numericInput5.move(170,110)
			self.popupItems5 = (u"(MPa)", u"(ksi)")
			self.popup5 = QtGui.QComboBox(self.varigroup)
			self.popup5.addItems(self.popupItems5)
			self.popup5.setCurrentIndex(self.popupItems5.index(u"(MPa)"))
			self.popup5.move(230, 110)
			self.designButton = QtGui.QPushButton("Design",self.varigroup)
			self.designButton.clicked.connect(self.onDesign8)
			self.designButton.setFixedWidth(180)
			self.designButton.setAutoDefault(True)
			self.designButton.move(80,145)

			self.resugroup = QtGui.QGroupBox(self.group8)
			self.resugroup.setGeometry(QtCore.QRect(30, 255, 340, 65))
			self.resugroup.setTitle(u"계산 결과값")
			self.resugroup.setStyleSheet("font-size: 10pt;")
			self.resugroup.setFont('Courier')
			self.label7 = QtGui.QLabel(u"칼라의 바깥지름",self.resugroup)
			self.label7.setStyleSheet("color: rgb(255,0,0);")
			self.label7.move(40,40)
			self.numericInput6 = QtGui.QLineEdit(self.resugroup)
			self.numericInput6.setFixedWidth(50)
			self.numericInput6.move(170,35)
			self.popupItems6 = (u"(mm)", u"(inch)")
			self.popup6 = QtGui.QComboBox(self.resugroup)
			self.popup6.addItems(self.popupItems6)
			self.popup6.setCurrentIndex(self.popupItems6.index(u"(mm)"))
			self.popup6.move(230, 35)

			self.modelgroup = QtGui.QGroupBox(self.group8)
			self.modelgroup.setGeometry(QtCore.QRect(30, 375, 340, 150))
			self.modelgroup.setTitle(u"모델링(변수 입력)")
			self.modelgroup.setStyleSheet("font-size: 10pt;")
			self.modelgroup.setFont('Courier')

			self.label8 = QtGui.QLabel(u"베어링의 높이",self.modelgroup)
			self.label8.move(40,40)
			self.numericInput7 = QtGui.QLineEdit(self.modelgroup)
			self.numericInput7.setFixedWidth(50)
			self.numericInput7.move(170,40)
			self.popupItems7 = (u"(mm)", u"(inch)")
			self.popup7 = QtGui.QComboBox(self.modelgroup)
			self.popup7.addItems(self.popupItems7)
			self.popup7.setCurrentIndex(self.popupItems7.index(u"(mm)"))
			self.popup7.move(230, 35)


			self.label10 = QtGui.QLabel(u"칼라의 바깥지름",self.modelgroup)
			self.label10.setStyleSheet("color: rgb(255,0,0);")
			self.label10.move(40,70)
			self.numericInput8 = QtGui.QLineEdit(self.modelgroup)
			self.numericInput8.setFixedWidth(50)
			self.numericInput8.move(170,70)
			self.popupItems8 = (u"(mm)", u"(inch)")
			self.popup8 = QtGui.QComboBox(self.modelgroup)
			self.popup8.addItems(self.popupItems8)
			self.popup8.setCurrentIndex(self.popupItems8.index(u"(mm)"))
			self.popup8.move(230, 70)
			self.generateButton = QtGui.QPushButton("Generate",self.modelgroup)
			self.generateButton.clicked.connect(self.onGenerate8)
			self.generateButton.setFixedWidth(180)
			self.generateButton.setAutoDefault(True)
			self.generateButton.move(80,100)
			self.label9= QtGui.QLabel(u"*붉은색 변수를 이용하여 모델링함*",self.modelgroup)
			self.label9.setStyleSheet("color: rgb(255,0,0);")
			self.label9.move(70,130)

			self.refer_Img_GroupBox = QtGui.QGroupBox(self.group8)
			self.refer_Img_GroupBox.setGeometry(QtCore.QRect(380, 70, 370, 200))
			self.refer_Img_GroupBox.setTitle(u"칼라 베어링")
			self.refer_Img_GroupBox.setStyleSheet("font-size: 10pt;")
			self.refer_Img_GroupBox.setFont('Courier')

			self.side_View_Img = QtGui.QPixmap(os.path.join(addonPath, "shaft_module\cal.jpg"))
			self.side_View_label = QtGui.QLabel(self.refer_Img_GroupBox)
			self.side_View_label.setPixmap(self.side_View_Img)
			self.side_View_label.resize(self.side_View_Img.width(), self.side_View_Img.height())
			self.side_View_label.move(105, 30)

			self.refer_Img_GroupBox1 = QtGui.QGroupBox(self.group8)
			self.refer_Img_GroupBox1.setGeometry(QtCore.QRect(380, 280, 370, 160))
			self.refer_Img_GroupBox1.setTitle(u"칼라 베어링의 지름 계산 공식")
			self.refer_Img_GroupBox1.setStyleSheet("font-size: 10pt;")
			self.refer_Img_GroupBox1.setFont('Courier')

			self.side_View_Img1 = QtGui.QPixmap(os.path.join(addonPath, "shaft_module\calfor.jpg"))
			self.side_View_label1 = QtGui.QLabel(self.refer_Img_GroupBox1)
			self.side_View_label1.setPixmap(self.side_View_Img1)
			self.side_View_label1.resize(self.side_View_Img1.width(), self.side_View_Img1.height())
			self.side_View_label1.move(30, 30)

			self.group8.show()

		elif self.treeWidget.currentItem().text(0) == u"볼 베어링":
			self.group1.hide()
			self.group2.hide()
			self.group3.hide()
			self.group4.hide()
			self.group5.hide()
			self.group6.hide()
			self.group7.hide()
			self.group8.hide()

			self.label1 = QtGui.QLabel(u"볼 베어링의 설계",self.group9)
			self.label1.setFont('Courier')
			self.label1.setStyleSheet("font: bold; font-size: 12pt;")
			self.label1.move(310,10)
			self.label1.setAlignment(QtCore.Qt.AlignRight)


			self.powergroup = QtGui.QGroupBox(self.group9)
			self.powergroup.setGeometry(QtCore.QRect(30, 70, 340, 90))
			self.powergroup.setTitle(u"작용하는 힘의 종류")
			self.powergroup.setStyleSheet("font-size: 10pt;")
			self.powergroup.setFont('Courier')
			self.label2 = QtGui.QLabel(u"축 방향 하중",self.powergroup)
			self.label2.move(40,40)
			self.numericInput2 = QtGui.QLineEdit(self.powergroup)
			self.numericInput2.setFixedWidth(50)
			self.numericInput2.move(170,35)
			self.popupItems2 = (u"(kN)", u"(lbf)")
			self.popup2 = QtGui.QComboBox(self.powergroup)
			self.popup2.addItems(self.popupItems2)
			self.popup2.setCurrentIndex(self.popupItems2.index(u"(kN)"))
			self.popup2.move(230, 35)
			self.label3 = QtGui.QLabel(u"반경 방향 하중",self.powergroup)
			self.label3.move(40,65)
			self.numericInput3 = QtGui.QLineEdit(self.powergroup)
			self.numericInput3.setFixedWidth(50)
			self.numericInput3.move(170,60)
			self.popupItems3 = (u"(kN)", u"(lbf)")
			self.popup3 = QtGui.QComboBox(self.powergroup)
			self.popup3.addItems(self.popupItems3)
			self.popup3.setCurrentIndex(self.popupItems3.index(u"(kN)"))
			self.popup3.move(230, 60)

			self.varigroup = QtGui.QGroupBox(self.group9)
			self.varigroup.setGeometry(QtCore.QRect(30, 170, 340, 315))
			self.varigroup.setTitle(u"설계 변수")
			self.varigroup.setStyleSheet("font-size: 10pt;")
			self.varigroup.setFont('Courier')
			self.label4 = QtGui.QLabel(u"베어링의 종류", self.varigroup)
			self.label4.move(40,40)
			self.label4.setFont('Courier')
			self.label4.setStyleSheet("font-size: 10pt;")
			self.popupItems9_1 = (u"(레이디얼)",u"(앵귤러)")
			self.popup9_1 = QtGui.QComboBox(self.varigroup)
			self.popup9_1.addItems(self.popupItems9_1)
			self.popup9_1.setCurrentIndex(self.popupItems9_1.index(u"(레이디얼)"))
			self.popup9_1.move(230, 35)
			self.label5 = QtGui.QLabel(u"기본 수명(rev)", self.varigroup)
			self.label5.move(40,65)
			self.label5.setFont('Courier')
			self.label5.setStyleSheet("font-size: 10pt;")
			self.popupItems9_2 = (u"(million)",u"(90 million)")
			self.popup9_2 = QtGui.QComboBox(self.varigroup)
			self.popup9_2.addItems(self.popupItems9_2)
			self.popup9_2.setCurrentIndex(self.popupItems9_2.index(u"(million)"))
			self.popup9_2.move(230, 60)
			self.label6 = QtGui.QLabel(u"회전속력",self.varigroup)
			self.label6.move(40,90)
			self.numericInput6 = QtGui.QLineEdit(self.varigroup)
			self.numericInput6.setFixedWidth(50)
			self.numericInput6.move(170,85)
			self.popupItems6 = (u"(rpm)", u"(rad/s)")
			self.popup6 = QtGui.QComboBox(self.varigroup)
			self.popup6.addItems(self.popupItems6)
			self.popup6.setCurrentIndex(self.popupItems6.index(u"(rpm)"))
			self.popup6.move(230, 85)
			self.label7 = QtGui.QLabel(u"적용 계수",self.varigroup)
			self.label7.move(40,115)
			self.numericInput7 = QtGui.QLineEdit("1.0",self.varigroup)
			self.numericInput7.setFixedWidth(50)
			self.numericInput7.move(170,110)
			self.tableButton = QtGui.QPushButton(u"적용 계수 예시", self.varigroup)
			self.tableButton.clicked.connect(self.onTable9_1)
			self.tableButton.setFixedWidth(180)
			self.tableButton.setAutoDefault(True)
			self.tableButton.move(90, 140)
			self.label8 = QtGui.QLabel(u"신뢰도 계수",self.varigroup)
			self.label8.move(40,170)
			self.numericInput8 = QtGui.QLineEdit("1.0",self.varigroup)
			self.numericInput8.setFixedWidth(50)
			self.numericInput8.move(170,165)
			self.tableButton = QtGui.QPushButton(u"신뢰도 계수 예시", self.varigroup)
			self.tableButton.clicked.connect(self.onTable9_2)
			self.tableButton.setFixedWidth(180)
			self.tableButton.setAutoDefault(True)
			self.tableButton.move(90, 195)
			self.label9 = QtGui.QLabel(u"기대 수명(hours)",self.varigroup)
			self.label9.move(40,225)
			self.numericInput9 = QtGui.QLineEdit(self.varigroup)
			self.numericInput9.setFixedWidth(50)
			self.numericInput9.move(170,220)
			self.tableButton = QtGui.QPushButton(u"기대 수명 예시", self.varigroup)
			self.tableButton.clicked.connect(self.onTable9_3)
			self.tableButton.setFixedWidth(180)
			self.tableButton.setAutoDefault(True)
			self.tableButton.move(90, 250)
			self.designButton = QtGui.QPushButton("Design",self.varigroup)
			self.designButton.clicked.connect(self.onDesign9)
			self.designButton.setFixedWidth(180)
			self.designButton.setAutoDefault(True)
			self.designButton.move(90,280)


			self.thirdgroup = QtGui.QGroupBox(self.group9)
			self.thirdgroup.setGeometry(QtCore.QRect(30, 495, 340, 65))
			self.thirdgroup.setTitle(u"계산 결과값 (요구되는 부하)")
			self.thirdgroup.setStyleSheet("font-size: 10pt;")
			self.thirdgroup.setFont('Courier')
			self.label10 = QtGui.QLabel(u"정적 부하",self.thirdgroup)
			self.label10.move(40,40)
			self.numericInput10 = QtGui.QLineEdit(self.thirdgroup)
			self.numericInput10.setFixedWidth(50)
			self.numericInput10.move(170,35)
			self.popupItems10 = (u"(kN)", u"(lbf)")
			self.popup10 = QtGui.QComboBox(self.thirdgroup)
			self.popup10.addItems(self.popupItems10)
			self.popup10.setCurrentIndex(self.popupItems10.index(u"(kN)"))
			self.popup10.move(230, 35)

			self.forthgroup = QtGui.QGroupBox(self.group9)
			self.forthgroup.setGeometry(QtCore.QRect(30, 570, 340, 160))
			self.forthgroup.setTitle(u"모델링(베어링 종류 : 300 med[kN])")
			self.forthgroup.setStyleSheet("font-size: 10pt;")
			self.forthgroup.setFont('Courier')

			self.tableButton = QtGui.QPushButton(u"Bore의 지름", self.forthgroup)
			self.tableButton.clicked.connect(self.onTable9_4)
			self.tableButton.setFixedWidth(180)
			self.tableButton.setAutoDefault(True)
			self.tableButton.move(90, 35)
			self.label12 = QtGui.QLabel(u"Bearing Basic Number",self.forthgroup)
			self.label12.move(40,70)
			self.numericInput12 = QtGui.QLineEdit(self.forthgroup)
			self.numericInput12.setFixedWidth(50)
			self.numericInput12.move(230,70)
			self.tableButton = QtGui.QPushButton(u"Bearing Basic Number", self.forthgroup)
			self.tableButton.clicked.connect(self.onTable9_5)
			self.tableButton.setFixedWidth(180)
			self.tableButton.setAutoDefault(True)
			self.tableButton.move(90, 100)
			self.designButton = QtGui.QPushButton("Generate",self.forthgroup)
			self.designButton.clicked.connect(self.onGenerate9)
			self.designButton.setFixedWidth(180)
			self.designButton.setAutoDefault(True)
			self.designButton.move(90,130)

			self.refer_Img_GroupBox = QtGui.QGroupBox(self.group9)
			self.refer_Img_GroupBox.setGeometry(QtCore.QRect(380, 70, 370, 270))
			self.refer_Img_GroupBox.setTitle(u"볼 베어링")
			self.refer_Img_GroupBox.setStyleSheet("font-size: 10pt;")
			self.refer_Img_GroupBox.setFont('Courier')

			self.side_View_Img = QtGui.QPixmap(os.path.join(addonPath, "shaft_module/bearing.jpg"))
			self.side_View_label = QtGui.QLabel(self.refer_Img_GroupBox)
			self.side_View_label.setPixmap(self.side_View_Img)
			self.side_View_label.resize(self.side_View_Img.width(), self.side_View_Img.height())
			self.side_View_label.move(80, 20)

			self.refer_Img_GroupBox1 = QtGui.QGroupBox(self.group9)
			self.refer_Img_GroupBox1.setGeometry(QtCore.QRect(380, 350, 370, 380))
			self.refer_Img_GroupBox1.setTitle(u"볼 베어링의 계산 공식")
			self.refer_Img_GroupBox1.setStyleSheet("font-size: 10pt;")
			self.refer_Img_GroupBox1.setFont('Courier')
			self.side_View_Img1 = QtGui.QPixmap(os.path.join(addonPath, "shaft_module/6_6_1.png"))

			self.side_View_label1 = QtGui.QLabel(self.refer_Img_GroupBox1)
			self.side_View_label1.setPixmap(self.side_View_Img1)
			self.side_View_label1.resize(self.side_View_Img1.width(), self.side_View_Img1.height())
			self.side_View_label1.move(10, 30)
			self.group9.show()



	def onTable(self):
		ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

		buf = QtGui.QPixmap(os.path.join(addonPath, "shaft_module/Iron Key_table.jpg"))  #C 드라이브에 넣었음

		Imageview1 = QtGui.QLabel(ks)
		Imageview1.setPixmap(buf)
		Imageview1.resize(buf.width(), buf.height())
		Imageview1.move(0,0)
		Imageview1.show()

		ks.setGeometry(750,100,buf.width(),buf.height())
		ks.setWindowTitle("KS Table")
		ks.show()
		ks.exec_()

	def onTable5_1(self):
		ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

		buf = QtGui.QPixmap(os.path.join(addonPath, "shaft_module/Key_table.jpg"))  #C 드라이브에 넣었음

		Imageview1 = QtGui.QLabel(ks)
		Imageview1.setPixmap(buf)
		Imageview1.resize(buf.width(), buf.height())
		Imageview1.move(0,0)
		Imageview1.show()

		ks.setGeometry(750,100,buf.width(),buf.height())
		ks.setWindowTitle(u"KS Table")
		ks.show()
		ks.exec_()

	def onTable5_2(self):
		ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

		buf = QtGui.QPixmap(os.path.join(addonPath, "shaft_module/Iron_Properties.jpg"))  #C 드라이브에 넣었음

		Imageview1 = QtGui.QLabel(ks)
		Imageview1.setPixmap(buf)
		Imageview1.resize(buf.width(), buf.height())
		Imageview1.move(0,0)
		Imageview1.show()

		ks.setGeometry(750,100,buf.width(),buf.height())
		ks.setWindowTitle(u"다양한 철의 물성치")
		ks.show()
		ks.exec_()


	def onTable9_1(self):
		ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

		buf = QtGui.QPixmap(os.path.join(addonPath, "shaft_module/6_1.png"))  #C 드라이브에 넣었음

		Imageview1 = QtGui.QLabel(ks)
		Imageview1.setPixmap(buf)
		Imageview1.resize(buf.width(), buf.height())
		Imageview1.move(0,0)
		Imageview1.show()

		ks.setGeometry(750,100,buf.width(),buf.height())
		ks.setWindowTitle(u"적용계수 Table")
		ks.show()
		ks.exec_()

	def onTable9_2(self):
		ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

		buf = QtGui.QPixmap(os.path.join(addonPath, "shaft_module/6_2.png"))  #C 드라이브에 넣었음

		Imageview1 = QtGui.QLabel(ks)
		Imageview1.setPixmap(buf)
		Imageview1.resize(buf.width(), buf.height())
		Imageview1.move(0,0)
		Imageview1.show()

		ks.setGeometry(750,100,buf.width(),buf.height())
		ks.setWindowTitle(u"수명 조정 신뢰도 계수")
		ks.show()
		ks.exec_()

	def onTable9_3(self):
		ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

		buf = QtGui.QPixmap(os.path.join(addonPath, "shaft_module/6_3.png"))

		Imageview1 = QtGui.QLabel(ks)
		Imageview1.setPixmap(buf)
		Imageview1.resize(buf.width(), buf.height())
		Imageview1.move(0,0)
		Imageview1.show()

		ks.setGeometry(750,100,buf.width(),buf.height())
		ks.setWindowTitle(u"사용 용도에서 요구되는 수명")
		ks.show()
		ks.exec_()

	def onTable9_4(self):
		ks = QtGui.QDialog()
		buf = QtGui.QPixmap(os.path.join(addonPath, "shaft_module/6_4.png"))

		Imageview1 = QtGui.QLabel(ks)
		Imageview1.setPixmap(buf)
		Imageview1.resize(buf.width(), buf.height())
		Imageview1.move(0,0)
		Imageview1.show()

		ks.setGeometry(750,100,buf.width(),buf.height())
		ks.setWindowTitle(u"Bore의 지름")
		ks.show()
		ks.exec_()

	def onTable9_5(self):
		ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

		buf = QtGui.QPixmap(os.path.join(addonPath, "shaft_module/6_5.png"))  #C 드라이브에 넣었음

		Imageview1 = QtGui.QLabel(ks)
		Imageview1.setPixmap(buf)
		Imageview1.resize(buf.width(), buf.height())
		Imageview1.move(0,0)
		Imageview1.show()

		ks.setGeometry(750,100,buf.width(),buf.height())
		ks.setWindowTitle(u"Bearing Basic Number")
		ks.show()
		#ks.exec_()

		kss = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

		buff = QtGui.QPixmap(os.path.join(addonPath, "shaft_module/6_5_1.png"))  #C 드라이브에 넣었음

		Imageview1 = QtGui.QLabel(kss)
		Imageview1.setPixmap(buff)
		Imageview1.resize(buff.width(), buff.height())
		Imageview1.move(0,0)
		Imageview1.show()

		kss.setGeometry(1300,100,buff.width(),buff.height())
		kss.setWindowTitle(u"Bearing Basic Number")
		kss.show()
		#kss.exec_()
		ks.exec_()

	def onSelect1(self):
		if self.r3.isChecked() == True:
			self.label2.setStyleSheet(("color: rgb(255,0,0)"))
			self.label3.setStyleSheet(("color: rgb(0,0,0)"))
			self.label4.setStyleSheet(("color: rgb(255,0,0)"))
			self.label5.setStyleSheet(("color: rgb(0,0,0)"))

	def onSelect2(self):
		if self.r4.isChecked() == True:
			self.label2.setStyleSheet(("color: rgb(0,0,0)"))
			self.label3.setStyleSheet(("color: rgb(255,0,0)"))
			self.label4.setStyleSheet(("color: rgb(0,0,0)"))
			self.label5.setStyleSheet(("color: rgb(255,0,0)"))

	def onSelect3(self):
		if self.r5.isChecked() == True:
			self.label2.setStyleSheet(("color: rgb(255,0,0)"))
			self.label3.setStyleSheet(("color: rgb(255,0,0)"))
			self.label4.setStyleSheet(("color: rgb(255,0,0)"))
			self.label5.setStyleSheet(("color: rgb(255,0,0)"))

	def onSelect4(self):
		if self.r3.isChecked() == True:
			self.label2.setStyleSheet(("color: rgb(255,0,0)"))
			self.label3.setStyleSheet(("color: rgb(0,0,0)"))
			self.label4.setStyleSheet(("color: rgb(255,0,0)"))
			self.label5.setStyleSheet(("color: rgb(0,0,0)"))
			self.label6.setStyleSheet(("color: rgb(255,0,0)"))

	def onSelect5(self):
		if self.r4.isChecked() == True:
			self.label2.setStyleSheet(("color: rgb(0,0,0)"))
			self.label3.setStyleSheet(("color: rgb(255,0,0)"))
			self.label4.setStyleSheet(("color: rgb(0,0,0)"))
			self.label5.setStyleSheet(("color: rgb(255,0,0)"))
			self.label6.setStyleSheet(("color: rgb(255,0,0)"))

	def onSelect6(self):
		if self.r5.isChecked() == True:
			self.label2.setStyleSheet(("color: rgb(255,0,0)"))
			self.label3.setStyleSheet(("color: rgb(255,0,0)"))
			self.label4.setStyleSheet(("color: rgb(255,0,0)"))
			self.label5.setStyleSheet(("color: rgb(255,0,0)"))
			self.label6.setStyleSheet(("color: rgb(255,0,0)"))

	def onDesign1(self):
		if self.r3.isChecked() == True:
			if self.popup1.currentText() == u"(kN*m)":
				bending_Nmm = float(self.numericInput1.text())*1000000
			elif self.popup1.currentText() == u"(lbf*ft)":
				bending_lbfft = float(self.numericInput1.text())
				bending_Nmm = 1000*1/0.737562*bending_lbfft
			if self.popup3.currentText() == u"(MPa)":
				bending_MPa = float(self.numericInput3.text())
			elif self.popup3.currentText() == u"(ksi)":
				bending_ksi = float(self.numericInput3.text())
				bending_MPa = 6.894759086*bending_ksi
			d1 = ((32*bending_Nmm)/(math.pi*bending_MPa))**(1/3)
			if self.popup5.currentText() == u"(mm)":
				self.numericInput5.setText(str(round(d1,3)))
			elif self.popup5.currentText() == u"(inch)":
				d1 = 1/25.4*d1
				self.numericInput5.setText(str(round(d1,3)))
			self.numericInput6.setText(str(round(0,1)))
		elif self.r4.isChecked() == True:
			if self.popup2.currentText() == u"(kN*m)":
				twist_Nmm = float(self.numericInput2.text())*1000000
			elif self.popup2.currentText() == u"(lbf*ft)":
				twist_lbfft = float(self.numericInput2.text())
				twist_Nmm = 1000*1/0.737562*bending_lbfft
			if self.popup4.currentText() == u"(MPa)":
				shear_MPa = float(self.numericInput4.text())
			elif self.popup4.currentText() == u"(ksi)":
				shear_ksi = float(self.numericInput4.text())
				shear_MPa = 6.894759086*bending_ksi
			d2 = ((16*twist_Nmm)/(math.pi*shear_MPa))**(1/3)
			self.numericInput5.setText(str(round(0,1)))
			if self.popup6.currentText() == u"(mm)":
				self.numericInput6.setText(str(round(d2,3)))
			elif self.popup6.currentText() == u"(inch)":
				d2 = 1/25.4*d2
				self.numericInput6.setText(str(round(d2,3)))
		elif self.r5.isChecked() == True:
			if self.popup1.currentText() == u"(kN*m)":
				bending_Nmm = float(self.numericInput1.text())*1000000
			elif self.popup1.currentText() == u"(lbf*ft)":
				bending_lbfft = float(self.numericInput1.text())
				bending_Nmm = 1000*1/0.737562*bending_lbfft
			if self.popup2.currentText() == u"(kN*m)":
				twist_Nmm = float(self.numericInput2.text())*1000000
			elif self.popup2.currentText() == u"(lbf*ft)":
				twist_lbfft = float(self.numericInput2.text())
				twist_Nmm = 1000*1/0.737562*bending_lbfft
			if self.popup3.currentText() == u"(MPa)":
				bending_MPa = float(self.numericInput3.text())
			elif self.popup3.currentText() == u"(ksi)":
				bending_ksi = float(self.numericInput3.text())
				bending_MPa = 6.894759086*bending_ksi
			if self.popup4.currentText() == u"(MPa)":
				shear_MPa = float(self.numericInput4.text())
			elif self.popup4.currentText() == u"(ksi)":
				shear_ksi = float(self.numericInput4.text())
				shear_MPa = 6.894759086*bending_ksi
			me = 1/2*(bending_Nmm+((bending_Nmm**2+twist_Nmm**2)**(1/2)))
			te = ((bending_Nmm**2+twist_Nmm**2)**(1/2))
			d1 = ((32*me)/(math.pi*bending_MPa))**(1/3)
			if self.popup5.currentText() == u"(mm)":
				self.numericInput5.setText(str(round(d1,3)))
			elif self.popup5.currentText() == u"(inch)":
				d1 = 1/25.4*d1
				self.numericInput5.setText(str(round(d1,3)))
			d2 = ((16*te)/(math.pi*shear_MPa))**(1/3)
			if self.popup6.currentText() == u"(mm)":
				self.numericInput6.setText(str(round(d2,3)))
			elif self.popup6.currentText() == u"(inch)":
				d2 = 1/25.4*d2
				self.numericInput6.setText(str(round(d2,3)))

	def onDesign2(self):

		if self.r3.isChecked() == True:
			if self.popup1.currentText() == u"(kN*m)":
				bending_Nmm = float(self.numericInput1.text())*1000000
			elif self.popup1.currentText() == u"(lbf*ft)":
				bending_lbfft = float(self.numericInput1.text())
				bending_Nmm = 1000*1/0.737562*bending_lbfft
			if self.popup3.currentText() == u"(MPa)":
				bending_MPa = float(self.numericInput3.text())
			elif self.popup3.currentText() == u"(ksi)":
				bending_ksi = float(self.numericInput3.text())
				bending_MPa = 6.894759086*bending_ksi
			x = float(self.numericInput5.text())
			d1 = ((32*bending_Nmm)/(math.pi*(1-(x)**(4))*bending_MPa))**(1/3)
			d11 = x*d1
			d2 = 1/25.4*d1
			d21 = 1/25.4*d11
			if self.popup6.currentText() == u"(mm)":
				self.numericInput6.setText(str(round(d1,3)))
			elif self.popup6.currentText() == u"(inch)":
				self.numericInput6.setText(str(round(d2,3)))
			if self.popup7.currentText() == u"(mm)":
				self.numericInput7.setText(str(round(d11,3)))
			elif self.popup7.currentText() == u"(inch)":
				self.numericInput7.setText(str(round(d21,3)))
			self.numericInput8.setText(str(0))
			self.numericInput9.setText(str(0))
		elif self.r4.isChecked() == True:
			if self.popup2.currentText() == u"(kN*m)":
				twist_Nmm = float(self.numericInput2.text())*1000000
			elif self.popup2.currentText() == u"(lbf*ft)":
				twist_lbfft = float(self.numericInput2.text())
				twist_Nmm = 1000*1/0.737562*bending_lbfft
			if self.popup4.currentText() == u"(MPa)":
				shear_MPa = float(self.numericInput4.text())
			elif self.popup4.currentText() == u"(ksi)":
				shear_ksi = float(self.numericInput4.text())
				shear_MPa = 6.894759086*bending_ksi
			x = float(self.numericInput5.text())
			d1 = ((16*twist_Nmm)/(math.pi*(1-(x)**(4))*shear_MPa))**(1/3)
			d2 = 1/25.4*d1
			d11 = x*d1
			d21 = 1/25.4*d11
			if self.popup8.currentText() == u"(mm)":
				self.numericInput8.setText(str(round(d1,3)))
			elif self.popup8.currentText() == u"(inch)":
				self.numericInput8.setText(str(round(d2,3)))
			if self.popup9.currentText() == u"(mm)":
				self.numericInput9.setText(str(round(d11,3)))
			elif self.popup9.currentText() == u"(inch)":
				self.numericInput9.setText(str(round(d21,3)))
			self.numericInput6.setText(str(0))
			self.numericInput7.setText(str(0))

		elif self.r5.isChecked() == True:
			if self.popup1.currentText() == u"(kN*m)":
				bending_Nmm = float(self.numericInput1.text())*1000000
			elif self.popup1.currentText() == u"(lbf*ft)":
				bending_lbfft = float(self.numericInput1.text())
				bending_Nmm = 1000*1/0.737562*bending_lbfft
			if self.popup2.currentText() == u"(kN*m)":
				twist_Nmm = float(self.numericInput2.text())*1000000
			elif self.popup2.currentText() == u"(lbf*ft)":
				twist_lbfft = float(self.numericInput2.text())
				twist_Nmm = 1000*1/0.737562*bending_lbfft
			if self.popup3.currentText() == u"(MPa)":
				bending_MPa = float(self.numericInput3.text())
			elif self.popup3.currentText() == u"(ksi)":
				bending_ksi = float(self.numericInput3.text())
				bending_MPa = 6.894759086*bending_ksi
			if self.popup4.currentText() == u"(MPa)":
				shear_MPa = float(self.numericInput4.text())
			elif self.popup4.currentText() == u"(ksi)":
				shear_ksi = float(self.numericInput4.text())
				shear_MPa = 6.894759086*bending_ksi
			x = float(self.numericInput5.text())
			me = 1/2*(bending_Nmm+((bending_Nmm**2+twist_Nmm**2)**(1/2)))
			te = ((bending_Nmm**2+twist_Nmm**2)**(1/2))
			d1 = ((32*me)/(math.pi*(1-(x)**(4))*bending_MPa))**(1/3)
			d11 = x*d1
			if self.popup6.currentText() == u"(mm)":
				self.numericInput6.setText(str(round(d1,3)))
			elif self.popup6.currentText() == u"(inch)":
				d12 = 1/25.4*d1
				self.numericInput6.setText(str(round(d12,3)))
			if self.popup7.currentText() == u"(mm)":
				self.numericInput7.setText(str(round(d11,3)))
			elif self.popup7.currentText() == u"(inch)":
				d112 = 1/25.4*d11
				self.numericInput7.setText(str(round(d112,3)))

			d2 = ((16*te)/(math.pi*(1-(x)**(4))*shear_MPa))**(1/3)
			d21 = x*d2
			if self.popup8.currentText() == u"(mm)":
				self.numericInput8.setText(str(round(d2,3)))
			elif self.popup8.currentText() == u"(inch)":
				d22 = 1/25.4*d2
				self.numericInput8.setText(str(round(d22,3)))
			if self.popup9.currentText() == u"(mm)":
				self.numericInput9.setText(str(round(d21,3)))
			elif self.popup9.currentText() == u"(inch)":
				d212 = 1/25.4*d21
				self.numericInput9.setText(str(round(d212,3)))



	def onDesign3(self):
		if self.popup1.currentText() == u"(rpm)":
			n = float(self.numericInput1.text())
		elif self.popup1.currentText() == u"(rad/s)":
			n_rad = float(self.numericInput1.text())
			n = n_rad*2*math.pi/60
		if self.popup3.currentText() == u"(MPa)":
			tau = float(self.numericInput3.text())
		elif self.popup3.currentText() == u"(ksi)":
			tau_ksi = float(self.numericInput3.text())
			tau = tau_ksi*6.894759086
		if self.popup2.currentText() == u"(kW)":
			p = float(self.numericInput2.text())
			if self.popup4.currentText() == u"(mm)":
				l1 = (9549000*16/(math.pi*tau)*p/n)**(1/3)
			elif self.popup4.currentText() == u"(inch)":
				l1_inch = (9549000*16/(math.pi*tau)*p/n)**(1/3)
				l1 = l1_inch*0.03937
			self.numericInput4.setText(str(round(l1,2)))
			if self.popup5.currentText() == u"(mm)":
				l2 = 130*((p/n)**(1/4))
			elif self.popup5.currentText() == u"(inch)":
				l2_inch = 130*((p/n)**(1/4))
				l2 = l2_inch*0.03937
			self.numericInput5.setText(str(round(l2,2)))
		elif self.popup2.currentText() == u"(HP)":
			p = float(self.numericInput2.text())
			if self.popup4.currentText() == u"(mm)":
				l1 = (7023500*16/(math.pi*tau)*p/n)**(1/3)
			elif self.popup4.currentText() == u"(inch)":
				l1_inch = (7023500*16/(math.pi*tau)*p/n)**(1/3)
				l1 = l1_inch*0.03937
			self.numericInput4.setText(str(round(l1,2)))
			if self.popup5.currentText() == u"(mm)":
				l2 = 120*((p/n)**(1/4))
			elif self.popup5.currentText() == u"(inch)":
				l2_inch = 120*((p/n)**(1/4))
				l2 = l2_inch*0.03937
			self.numericInput5.setText(str(round(l2,2)))





	def onDesign4(self):
		if self.popup2.currentText() == u"(rad)":
			a_rad = float(self.numericInput2.text())
			a = a_rad*180/math.pi	   # 조인트 꺽임각(degree)
		elif self.popup2.currentText() == u"(degree)":
			a = float(self.numericInput2.text())
		if self.popup3.currentText() == u"(rad)":
			th_rad = float(self.numericInput3.text())	   # 기준축 회전각 (degree)
			th = th_rad*180/math.pi
		elif self.popup3.currentText() == u"(degree)":
			th = float(self.numericInput3.text())
		if self.popup4.currentText() == u"(rpm)":
			r = float(self.numericInput4.text())	   # 기준축 각속도 (rpm)
		elif self.popup4.currentText() == u"(rad/s)":
			r_rad = float(self.numericInput4.text())
			r = r_rad*2*math.pi/60
		if self.popup7.currentText() == u"(rpm)":
			d1 = (math.cos(math.radians(a))*r)/(1-pow(math.cos(math.radians(th))*math.sin(math.radians(a)),2))
		elif self.popup7.currentText() == u"(rad/s)":
			d1_rpm = (math.cos(math.radians(a))*r)/(1-pow(math.cos(math.radians(th))*math.sin(math.radians(a)),2))
			d1 = d1_rpm*60/(math.pi*2)
		if self.popup8.currentText() == u"(rpm)":
			d2 = r/math.cos(math.radians(a))
		elif self.popup8.currentText() == u"(rad/s)":
			d2_rpm = r/math.cos(math.radians(a))
			d2 = d2_rpm*60/(2*math.pi)
		if self.popup9.currentText() == u"(rpm)":
			d3 = r*math.cos(math.radians(a))
		elif self.popup9.currentText() == u"(rad/s)":
			d3_rpm = r*math.cos(math.radians(a))
			d3 = d3_rpm*60/(2*math.pi)
		self.numericInput7.setText(str(round(d1,3)))
		self.numericInput8.setText(str(round(d2,3)))
		self.numericInput9.setText(str(round(d3,3)))

	def onDesign5(self):


		if self.popup2.currentText() == u"(mm)":
			d = float(self.numericInput2.text())		# 축 지름
		elif self.popup2.currentText() == u"(inch)":
			d_inch = float(self.numericInput2.text())
			d = d_inch*25.4
		if self.popup3.currentText() == u"(mm)":
			b = float(self.numericInput3.text())		# 키의 폭
		elif self.popup3.currentText() == u"(inch)":
			b_inch = float(self.numericInput3.text())
			b = b_inch*25.4
		if self.popup4.currentText() == u"(mm)":
			h = float(self.numericInput4.text())		# 키의 높이
		elif self.popup4.currentText() == u"(inch)":
			h_inch = float(self.numericInput4.text())
			h = h_inch*25.4
		if self.popup5.currentText() == u"(mm)":
			t = float(self.numericInput5.text())		# t1
		elif self.popup5.currentText() == u"(inch)":
			t_inch = float(self.numericInput5.text())
			t = t_inch*25.4
		if self.popup6.currentText() == u"(rpm)":
			n = float(self.numericInput6.text())		# rpm
		elif self.popup6.currentText() == u"(rad/s)":
			n_rad = float(self.numericInput6.text())
			n = n_rad*60/(2*math.pi)
		if self.popup8.currentText() == u"(MPa)":
			tau = float(self.numericInput8.text())		# 허용 전단 응력 (MPa)
		elif self.popup8.currentText() == u"(ksi)":
			tau_ksi = float(self.numericInput8.text())
			tau = tau_ksi*6.894759086
		if self.popup9.currentText() == u"(MPa)":
			s = float(self.numericInput9.text())		# 허용 전단 응력 (MPa)
		elif self.popup9.currentText() == u"(ksi)":
			s_ksi = float(self.numericInput9.text())		# 허용 압축 응력 (MPa)
			s = s_ksi*6.894759086
		if self.popup1.currentText() == u"(HP)":
			p_hp = float(self.numericInput7.text())
			p = p_hp*745700
		elif self.popup1.currentText() == u"(kW)":
			p_kw = float(self.numericInput7.text())
			p = p_kw*1000000
		if self.popup10.currentText() == u"(mm)":
			l1 = 2 * p / (n * b * d * tau)
		elif self.popup10.currentText() == u"(inch)":
			l1_inch =  2 * p / (n * b * d * tau)
			l1 = l1_inch*0.03937
		if self.popup11.currentText() == u"(mm)":
			l2 = 2 * p / (n * b * d * t)
		elif self.popup11.currentText() == u"(inch)":
			l2_inch = 2 * p / (n * b * d * t)
			l2 = l2_inch*0.03937


		self.numericInput10.setText(str(round(l1,2)))
		self.numericInput11.setText(str(round(l2,2)))







	def onDesign6(self):
		if self.popup2.currentText() == u"(kN)":
			p = float(self.numericInput2.text())	   # 인장하중 (kN)
		elif self.popup2.currentText() == u"(lbf)":
			p_lbf = float(self.numericInput2.text())
			p = p_lbf*0.2248*1000
		if self.popup3.currentText() == u"(MPa)":
			tau = float(self.numericInput3.text())	   # 허용전단응력 (MPa)
		elif self.popup3.currentText() == u"(ksi)":
			tau_ksi = float(self.numericInput3.text())
			tau = tau_ksi*6.894759086
		if self.popup4.currentText() == u"(MPa)":
			q = float(self.numericInput4.text())	   # 허용면압 (MPa)
		elif self.popup4.currentText() == u"(ksi)":
			q_ksi = float(self.numericInput4.text())
			q = q_ksi*6.894759086
		if self.popup5.currentText() == u"(mm)":
			a = float(self.numericInput5.text())	   # 아이 두께 (mm)
		elif self.popup5.currentText() == u"(inch)":
			a_inch = float(self.numericInput5.text())
			a = a_inch*25.4
		if self.popup6.currentText() == u"(mm)":
			b = float(self.numericInput6.text())	   # 포크의 부께 (mm)
		elif self.popup6.currentText() == u"(inch)":
			b_inch = float(self.numericInput6.text())
			b = b_inch*25.4
		if self.popup7.currentText() == u"(mm)":
			d1 = math.sqrt((2 * p *1000) / (math.pi * tau))
		elif self.popup7.currentText() == u"(inch)":
			d1_inch = math.sqrt((2 * p *1000) / (math.pi * tau))
			d1 = d1_inch/25.4
		if self.popup8.currentText() == u"(mm)":
			d2 = p * 1000 / (a * q)
		elif self.popup8.currentText() == u"(inch)":
			d2_inch = p * 1000 / (a * q)
			d2 = d2_inch/25.4
		if self.popup9.currentText() == u"(mm)":
			d3 = p * 1000 / (2 * b * q)
		elif self.popup9.currentText() == u"(inch)":
			d3_inch = p * 1000 / (2 * b * q)
			d3 = d3_inch/25.4
		self.numericInput7.setText(str(round(d1,3)))
		self.numericInput8.setText(str(round(d2,3)))
		self.numericInput9.setText(str(round(d3,3)))

	def onDesign7(self):
		if self.popup1.currentText() == u"(rpm)":
			n = float(self.numericInput1.text())
		elif self.popup1.currentText() == u"(rad/s)":
			n_rad = float(self.numericInput1.text())
			n = n_rad*2*math.pi/60
	   	if self.popup2.currentText() == u"(kN)":
			p = float(self.numericInput2.text())
		elif self.popup2.currentText() == u"(lbf)":
			p_lbf = float(self.numericInput2.text())
			p = p_lbf*0.2248*1000
		if self.popup3.currentText() == u"(MPa*m/s)":
			q = float(self.numericInput3.text())
		elif self.popup3.currentText() == u"(())":
			q = float(self.numericInput3.text())
		if self.popup4.currentText() == u"(MPa)":
			si = float(self.numericInput4.text())
		elif self.popup4.currentText() == u"(ksi)":
			si_ksi = float(self.numericInput4.text())
			si = si_ksi*6.894759086

		if self.popup5.currentText() == u"(mm)":
			l = math.pi*p*1000*n/(60000*q)
		elif self.popup5.currentText() == u"(inch)":
			l_inch = math.pi*p*1000*n/(60000*q)
			l = l_inch/25.4
		if self.popup6.currentText() == u"(mm)":
			d = (16*p*1000*math.pi*p*1000*n/(60000*q)/(math.pi*si))**(1/3)
		elif self.popup6.currentText() == u"(inch)":
			d_inch = (16*p*1000*math.pi*p*1000*n/(60000*q)/(math.pi*si))**(1/3)
			d = d_inch/25.4

		if self.popup7.currentText() == u"(MPa)":
			pp = p*1000/((16*p*1000*math.pi*p*1000*n/(60000*q)/(math.pi*si))**(1/3)*math.pi*p*1000*n/(60000*q))
		elif self.popup7.currentText() == u"(ksi)":
			pp_ksi = p*1000/((16*p*1000*math.pi*p*1000*n/(60000*q)/(math.pi*si))**(1/3)*math.pi*p*1000*n/(60000*q))
			pp = pp_ksi/6.894759086
		self.numericInput5.setText(str(round(l,2)))
		self.numericInput6.setText(str(round(d,2)))
		self.numericInput7.setText(str(round(pp,2)))

	def onDesign8(self):
		if self.popup2.currentText() == u"(N)":
			P = float(self.numericInput2.text())
		elif self.popup2.currentText() == u"(lbf)":
			P_lbf = float(self.numericInput2.text())
			p = p_lbf*0.2248
		if self.popup3.currentText() == u"(mm)":
			d1 = float(self.numericInput3.text())
		elif self.popup3.currentText() == u"(inch)":
			d1_inch = float(self.numericInput3.text())
			d1 = d1_inch*25.4
		z = float(self.numericInput4.text())
		if self.popup5.currentText() == u"(MPa)":
			p = float(self.numericInput5.text())
		elif self.popup5.currentText() == u"(ksi)":
			p_ksi = float(self.numericInput5.text())
			p = p_ksi*6.894759086
		if self.popup6.currentText() == u"(mm)":
			d2 = (d1**(2)+(4*P)/(math.pi*p*z))**(1/2)
		elif self.popup6.currentText() == u"(inch)":
			d2_inch = (d1**(2)+(4*P)/(math.pi*p*z))**(1/2)
			d2 = d2_inch/25.4
		self.numericInput6.setText(str(round(d2,2)))

	def onDesign9(self):
		if self.popup2.currentText() == u"(kN)":
			Ft = float(self.numericInput2.text())
		elif self.popup2.currentText() == u"(lbf)":
			Ft_lbf = float(self.numericInput2.text())
			Ft = Ft_lbf*0.2248*1000
		if self.popup3.currentText() == u"(kN)":
			Fr = float(self.numericInput3.text())
		elif self.popup3.currentText() == u"(lbf)":
			Fr_lbf = float(self.numericInput3.text())
			Fr = Fr_lbf*0.2248*1000
		if self.popup6.currentText() == u"(rpm)":
			rpm = float(self.numericInput6.text())
		elif self.popup6.currentText() == u"(rad/s)":
			rad = float(self.numericInput6.text())
			rpm = rad*2*math.pi/60
		Ka = float(self.numericInput7.text())
		Kr = float(self.numericInput8.text())
		Hours = float(self.numericInput9.text())


		if self.popup9_1.currentText() == u"(레이디얼)":
			if Ft/Fr < 0.35:
				Fe = Fr
			elif Ft/Fr < 10:
				Fe = Fr*(1+1.115*(Ft/Fr-0.35))
			else:
				Fe = Fe = 1.176*Ft
		if self.popup9_1.currentText() == u"(앵귤러)":
			if Ft/Fr < 0.68:
				Fe = Fr
			elif Ft/Fr < 10:
				Fe = Fr*(1+0.870*(Ft/Fr-0.68))
			else:
				Fe = Fe = 0.911*Ft

		if self.popup9_2.currentText() == u"(million)":
			Lr = 1000000
		elif self.popup9_2.currentText() == u"(90 million)":
			Lr = 90000000

		L = rpm*Hours*60
		if self.popup10.currentText() == u"(kN)":
			Creq = Fe*Ka*(L/(Kr*Lr))**(0.3)
		elif self.popup10.currentText() == u"(lbf)":
			Creq_lbf = Fe*Ka*(L/(Kr*Lr))**(0.3)
			Creq = Creq_lbf*4.448*1000

		self.numericInput10.setText(str(round(Creq,3)))

	def onGenerate1(self):
		doc=App.newDocument()
		if self.popup7.currentText() == u"(mm)":
			length_mm = float(self.numericInput7.text())
		elif self.popup7.currentText() == u"(inch)":
			length_inch = float(self.numericInput7.text())
			length_mm = 25.4*length_inch
		if self.popup8.currentText() == u"(mm)":
			dia_mm = float(self.numericInput8.text())
		elif self.popup8.currentText() == u"(inch)":
			dia_inch = float(self.numericInput8.text())
			dia_mm = 25.4*dia_inch

		circ=Part.makeCylinder(dia_mm/2.0,length_mm,Vector(0,0,0))

		shape=doc.addObject("Part::Feature")                   #Color
		shape.Shape=circ				                       #Color
		doc.recompute()                                        #Color
		shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
		Gui.activeDocument().activeView().viewAxometric()      #View
		Gui.SendMsgToActiveView("ViewFit")                     #View

	def onGenerate2(self):
		doc=App.newDocument()
		if self.popup11.currentText() == u"(mm)":
			dia_out_mm = float(self.numericInput11.text())
		elif self.popup11.currentText() == u"(inch)":
			dia_out_inch = float(self.numericInput11.text())
			dia_out_mm =25.4*dia_out_inch
		if self.popup12.currentText() == u"(mm)":
			dia_inner_mm = float(self.numericInput12.text())
		elif self.popup12.currentText() == u"(inch)":
			dia_inner_inch = float(self.numericInput12.text())
			dia_inner_mm =25.4*dia_inner_inch
		if self.popup10.currentText() == u"(mm)":
			length_mm = float(self.numericInput10.text())
		elif self.popup10.currentText() == u"(inch)":
			length_inch = float(self.numericInput10.text())
			length_mm =25.4*length_inch


		circ  = Part.makeCylinder(dia_out_mm/2.0,length_mm,Vector(0,0,0))
		circ2 = Part.makeCylinder(dia_inner_mm/2.0,length_mm,Vector(0,0,0))
		circ  = circ.cut(circ2)

		shape=doc.addObject("Part::Feature")                   #Color
		shape.Shape=circ				                       #Color
		doc.recompute()                                        #Color
		shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
		Gui.activeDocument().activeView().viewAxometric()      #View
		Gui.SendMsgToActiveView("ViewFit")                     #View

	def onGenerate3(self):


			doc=App.newDocument()
			if self.popup7.currentText() == u"(mm)":
				d = float(self.numericInput7.text())
			elif self.popup7.currentText() == u"(inch)":
				d_inch = float(self.numericInput7.text())
				d = d_inch*25.4
			if self.popup6.currentText() == u"(mm)":
				l = float(self.numericInput6.text())
			elif self.popup6.currentText() == u"(inch)":
				l_inch = float(self.numericInput6.text())
				l = l_inch*25.4

			circ=Part.makeCylinder(d/2.0,l,Vector(0,0,0))

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=circ				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


	def onGenerate4(self):

			doc = App.newDocument()
			if self.popup10.currentText() == u"(mm)":
				d = float(self.numericInput10.text())
			elif self.popup10.currentText() == u"(inch)":
				d_inch = float(self.numericInput10.text())
				d = d_inch*25.4
			if self.popup11.currentText() == u"(mm)":
				l1 = float(self.numericInput11.text()) #길이
			elif self.popup11.currentText() == u"(inch)":
				l1_inch = float(self.numericInput11.text())
				l1 = l1_inch*25.4
			if self.popup12.currentText() == u"(mm)":
				l2 = float(self.numericInput12.text()) #길이
			elif self.popup12.currentText() == u"(inch)":
				l2_inch = float(self.numericInput12.text())
				l2 = l2_inch*25.4
			if self.popup2.currentText() == u"(rad)":
				deg_rad = float(self.numericInput2.text())#각도
				deg = deg_rad*math.pi/180
			elif self.popup2.currentText() == u"(degree)":
				deg = float(self.numericInput2.text())

			cyl = Part.makeCylinder(d/2, l1, Vector(0, 0, d/5))
			bo1 = Part.makeBox(d, d, d/5, Vector( d/2, -d/2, d/5), Vector( 0, 0, -1))
			bo2 = Part.makeBox(d, d/5, d+d/5, Vector( d/2, -d/2-d/5, d/5), Vector( 0, 0, -1))
			bo3 = Part.makeBox(d, d/5, d+d/5, Vector( d/2, d/2, d/5), Vector( 0, 0, -1))
			cy2 = Part.makeCylinder(d/2,d/5,Vector(0,d/2+d/5,-d),Vector(0,-1,0))
			cy3 = Part.makeCylinder(d/2,d/5,Vector(0,-d/2-d/5,-d),Vector(0,1,0))
			ch1 = Part.makeCylinder(7*d/20,d+2*d/5,Vector(0,-d/2-d/5,-d),Vector(0,1,0))
			ch2 = Part.makeCylinder(7*d/20,d+2*d/5,Vector(-d/2-d/5,0,-d),Vector(1,0,0))
			cy4 = Part.makeCylinder(d/2,d/5,Vector(d/2+d/5,0,-d),Vector(-1,0,0))
			cy5 = Part.makeCylinder(d/2,d/5,Vector(-d/2-d/5,0,-d),Vector(1,0,0))
			bo5 = Part.makeBox(d, d/5, d, Vector(-d/2-d/5,d/2,-d), Vector( 0, -1, 0))
			bo6 = Part.makeBox(d, d/5, d, Vector(d/2,d/2,-d), Vector( 0, -1, 0))
			bo5.rotate(Vector(-d/2-d/5,0,-d),(1,0,0),deg)
			bo6.rotate(Vector(d/2,0,-d),(1,0,0),deg)
			bo7 = Part.makeBox(d, d, d/5, Vector( d/2, -d/2, d/5-2*d), Vector( 0, 0, -1))
			cy6 = Part.makeCylinder(d/2, l1, Vector(0, 0, -2*d-l2))
			bo7.rotate(Vector(0,0,-d),(1,0,0),deg)
			cy6.rotate(Vector(0,0,-d),(1,0,0),deg)
			fuse = cyl.fuse(bo1)
			fuse2 = bo1.fuse(fuse)
			fuse3 = bo2.fuse(fuse2)
			fuse4 = bo3.fuse(fuse3)
			fuse5 = cy2.fuse(fuse4)
			fuse6 = cy3.fuse(fuse5)
			fuse7 = ch1.fuse(fuse6)
			fuse8 = ch2.fuse(fuse7)
			fuse9 = cy4.fuse(fuse8)
			fuse10 = cy5.fuse(fuse9)
			fuse11 = bo5.fuse(fuse10)
			fuse12 = bo6.fuse(fuse11)
			fuse13 = bo7.fuse(fuse12)
			fuse14 = cy6.fuse(fuse13)



			shape = doc.addObject("Part::Feature")

			shape.Shape = fuse14
			doc.recompute()
			shape.ViewObject.ShapeColor = (1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")                     #View





	def onGenerate5(self):

			self.r2.setStyleSheet("color: rgb(0,0,0);")
			doc = App.newDocument()
			if self.popup3.currentText() == u"(mm)":
				b = float(self.numericInput3.text())		# 키의 폭
			elif self.popup3.currentText() == u"(inch)":
				b_inch = float(self.numericInput3.text())
				b = b_inch*25.4
			if self.popup4.currentText() == u"(mm)":
				h = float(self.numericInput4.text())		# 키의 높이
			elif self.popup4.currentText() == u"(inch)":
				h_inch = float(self.numericInput4.text())
				h = h_inch*25.4
			if self.popup12.currentText() == u"(mm)":
				l = float(self.numericInput12.text())		# 키의 높이
			elif self.popup12.currentText() == u"(inch)":
				l_inch = float(self.numericInput12.text())
				l = l_inch*25.4

			exHex = Part.makeBox(b, h, l,
								Vector(-b / 2, -h / 2, -l / 2))
			shape = doc.addObject("Part::Feature")
			shape.Shape = exHex
			doc.recompute()
			shape.ViewObject.ShapeColor = (1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

			self.numericInput12.setText('%.1f x %.1f x %.1f' % (
				round(b, 3), round(h, 3), round(l, 3)))



	def onGenerate6(self):

			doc = App.newDocument()
			if self.popup5.currentText() == u"(mm)":
				a = float(self.numericInput5.text())	   # 아이 두께 (mm)
			elif self.popup5.currentText() == u"(inch)":
				a_inch = float(self.numericInput5.text())
				a = a_inch*25.4
			if self.popup6.currentText() == u"(mm)":
				b = float(self.numericInput6.text())	   # 포크의 부께 (mm)
			elif self.popup6.currentText() == u"(inch)":
				b_inch = float(self.numericInput6.text())
				b = b_inch*25.4
			if self.popup10.currentText() == u"(mm)":
				r = float(self.numericInput10.text())	   # 포크의 부께 (mm)
			elif self.popup10.currentText() == u"(inch)":
				r_inch = float(self.numericInput10.text())
				r = r_inch*25.4
			cyl = Part.makeCylinder(r / 2, 2 * b + a, Vector(0, 0, 0))
			cyl2 = Part.makeCylinder(r / 2 * 1.4, (2 * b + a) * 0.2, Vector(0, 0, 0), Vector(0, 0, -1))
			cyl = cyl.fuse(cyl2)

			shape = doc.addObject("Part::Feature")
			shape.Shape = cyl
			doc.recompute()
			shape.ViewObject.ShapeColor = (1.0, 1.0, 1.0)
			Gui.activeDocument().activeView().viewAxometric()
			Gui.SendMsgToActiveView("ViewFit")

			#self.numericInput10.setText('%.1f x %.1f x %.1f' % (
			#	round(float(self.numericInput4.text()), 3), round(float(self.numericInput5.text()), 3), round(float(self.numericInput7.text()), 3)))



	def onGenerate7(self):
		doc=App.newDocument()
		if self.popup9.currentText() == u"(mm)":
			d = float(self.numericInput9.text())
		elif self.popup9.currentText() == u"(inch)":
			d_inch = float(self.numericInput9.text())
			d = d_inch*25.4
		if self.popup8.currentText() == u"(mm)":
			l = float(self.numericInput8.text()) #길이
		elif self.popup8.currentText() == u"(inch)":
			l_inch = float(self.numericInput8.text()) #길이
			l = l_inch*25.4

		circ=Part.makeCylinder(d*1.5/2.0,l,Vector(0,0,0))
		circ2=Part.makeCylinder(d/2.0,l,Vector(0,0,0))

		circ = circ.cut(circ2)
		shape=doc.addObject("Part::Feature")                   #Color
		shape.Shape=circ				                       #Color
		doc.recompute()                                        #Color
		shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
		Gui.activeDocument().activeView().viewAxometric()      #View
		Gui.SendMsgToActiveView("ViewFit")                     #View

	def onGenerate8(self):
		doc=App.newDocument()
		if self.popup8.currentText() == u"(mm)":
			d = float(self.numericInput8.text())
		elif self.popup8.currentText() == u"(inch)":
			d_inch = float(self.numericInput8.text())
			d = d_inch*25.4
		if self.popup3.currentText() == u"(mm)":
			d1 = float(self.numericInput3.text())
		elif self.popup3.currentText() == u"(inch)":
			d1_inch = float(self.numericInput3.text())
			d1 = d1_inch*25.4
		if self.popup7.currentText() == u"(mm)":
			l = float(self.numericInput7.text()) #길이
		elif self.popup7.currentText() == u"(inch)":
			l_inch = float(self.numericInput7.text()) #길이
			l = l_inch*25.4

		circ=Part.makeCylinder(d/2.0,l,Vector(0,0,0))
		circ2=Part.makeCylinder(d1/2.0,l,Vector(0,0,0))

		circ = circ.cut(circ2)
		shape=doc.addObject("Part::Feature")                   #Color
		shape.Shape=circ				                       #Color
		doc.recompute()                                        #Color
		shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
		Gui.activeDocument().activeView().viewAxometric()      #View
		Gui.SendMsgToActiveView("ViewFit")                     #View

	def onGenerate9(self):

		if float(self.numericInput12.text())==300:
			doc=App.newDocument()
			bore=10.0/2 #
			ds=12.7/2 #
			dh=23.4/2
			od=26.0/2
			w=8
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

		elif float(self.numericInput12.text())==301:
			doc=App.newDocument()
			bore=12.0/2 #
			ds=17.7/2 #
			dh=32.0/2
			od=37.0/2
			w=12
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==302:
			doc=App.newDocument()
			bore=15.0/2 #
			ds=21.2/2 #
			dh=36.6/2
			od=42.0/2
			w=13
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==303:
			doc=App.newDocument()
			bore=17.0/2 #
			ds=23.6/2 #
			dh=41.1/2
			od=47.0/2
			w=14
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==304:
			doc=App.newDocument()
			bore=20.0/2 #
			ds=27.7/2 #
			dh=45.2/2
			od=52.0/2
			w=15
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==305:
			doc=App.newDocument()
			bore=25.0/2 #
			ds=33.0/2 #
			dh=54.9/2
			od=62.0/2
			w=17
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==306:
			doc=App.newDocument()
			bore=30.0/2 #
			ds=38.4/2 #
			dh=64.8/2
			od=72.0/2
			w=19
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==307:
			doc=App.newDocument()
			bore=35.0/2 #
			ds=45.2/2 #
			dh=70.4/2
			od=80.0/2
			w=21
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==308:
			doc=App.newDocument()
			bore=40.0/2 #
			ds=50.8/2 #
			dh=80.0/2
			od=90.0/2
			w=23
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==309:
			doc=App.newDocument()
			bore=45.0/2 #
			ds=57.2/2 #
			dh=88.9/2
			od=100.0/2
			w=25
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==310:
			doc=App.newDocument()
			bore=50.0/2 #
			ds=64.3/2 #
			dh=96.5/2
			od=110.0/2
			w=27
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==311:
			doc=App.newDocument()
			bore=55.0/2 #
			ds=69.8/2 #
			dh=106.2/2
			od=120.0/2
			w=29
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==312:
			doc=App.newDocument()
			bore=60.0/2 #
			ds=75.4/2 #
			dh=115.6/2
			od=130.0/2
			w=31
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==313:
			doc=App.newDocument()
			bore=65.0/2 #
			ds=81.3/2 #
			dh=125.0/2
			od=140.0/2
			w=33
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==314:
			doc=App.newDocument()
			bore=70.0/2 #
			ds=86.9/2 #
			dh=134.4/2
			od=150.0/2
			w=35
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==315:
			doc=App.newDocument()
			bore=75.0/2 #
			ds=92.7/2 #
			dh=143.8/2
			od=160.0/2
			w=37
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==316:
			doc=App.newDocument()
			bore=80.0/2 #
			ds=98.6/2 #
			dh=152.9/2
			od=170.0/2
			w=39
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==317:
			doc=App.newDocument()
			bore=85.0/2 #
			ds=105.7/2 #
			dh=160.8/2
			od=180.0/2
			w=41
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==318:
			doc=App.newDocument()
			bore=90.0/2 #
			ds=111.3/2 #
			dh=170.2/2
			od=190.0/2
			w=43
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==319:
			doc=App.newDocument()
			bore=95.0/2 #
			ds=117.3/2 #
			dh=179.3/2
			od=200.0/2
			w=45
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==320:
			doc=App.newDocument()
			bore=100.0/2 #
			ds=122.9/2 #
			dh=194.1/2
			od=215.0/2
			w=47
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==321:
			doc=App.newDocument()
			bore=105.0/2 #
			ds=128.8/2 #
			dh=203.5/2
			od=225.0/2
			w=49
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==322:
			doc=App.newDocument()
			bore=110.0/2 #
			ds=134.4/2 #
			dh=218.2/2
			od=240.0/2
			w=50
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View


		elif float(self.numericInput12.text())==326:
			doc=App.newDocument()
			bore=130.0/2 #
			ds=160.0/2 #
			dh=253.0/2
			od=280.0/2
			w=58
			NBall=6
			RBall=((od+dh)/2-(bore+ds)/2)/2

			#Program#

			B1=Part.makeCylinder(bore,w)
			B2=Part.makeCylinder(ds,w)
			IR=B2.cut(B1)

			B3=Part.makeCylinder(dh,w)
			B4=Part.makeCylinder(od,w)
			OR=B4.cut(B3)

			IR=IR.fuse(OR)

			CBall=((dh-ds)/2)+ds
			PBall=w/2

			for i in range(NBall):
				Ball=Part.makeSphere(RBall)
				Alpha=(i*2*math.pi)/NBall
				BV=(CBall*math.cos(Alpha),CBall*math.sin(Alpha),w/2)
				Ball.translate(BV)
				IR=IR.fuse(Ball)

			shape=doc.addObject("Part::Feature")                   #Color
			shape.Shape=IR				                       #Color
			doc.recompute()                                        #Color
			shape.ViewObject.ShapeColor=(1.0, 1.0, 1.0)           #Color
			Gui.activeDocument().activeView().viewAxometric()      #View
			Gui.SendMsgToActiveView("ViewFit")                     #View

	def onQuit(self):
		#self.quitButton.clicked.connect(self.close())
		self.close()

ex = Sci()
#ex.show()              #ED-PyCharm
#sys.exit(app.exec_())  #ED-PyCharm
