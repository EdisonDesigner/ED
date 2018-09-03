from __future__ import division
# -*- coding: utf-8 -*- # 반드시 코드 2번째나 3번째 줄에 있어야함.
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
    def __init__(self):  # 생성자 소멸자 : def __del__(self)
        super(Sci, self).__init__()
        self.initUI()

    def initUI(self):
        self.treeWidget = QtGui.QTreeWidget(self)  # treeview
        self.treeWidget.setHeaderLabels([u"            체결용 기계부품"])  # headerlabel명
        self.treeWidget.setColumnCount(1)  # headerlabel 칼럼 갯수

        root1 = QtGui.QTreeWidgetItem(self.treeWidget)
        root1.setText(0, u'나사')
        child1 = QtGui.QTreeWidgetItem(root1)
        child1.setText(0, u'육각볼트')
        #child1.setText(1,'name1')
        child2 = QtGui.QTreeWidgetItem(root1)
        child2.setText(0, u'육각너트')
        child3 = QtGui.QTreeWidgetItem(root1)
        child3.setText(0, u'사각볼트')
        child4 = QtGui.QTreeWidgetItem(root1)
        child4.setText(0, u'사각너트')
        child5 = QtGui.QTreeWidgetItem(root1)
        child5.setText(0, u'와셔')
        self.treeWidget.addTopLevelItem(root1)

        root2 = QtGui.QTreeWidgetItem(self.treeWidget)
        root2.setText(0, u'리벳')
        child1 = QtGui.QTreeWidgetItem(root2)
        child1.setText(0, u'리벳')
        self.treeWidget.addTopLevelItem(root2)

        self.treeWidget.setGeometry(10, 10, 200, 780)
        self.treeWidget.expandAll()  # 트리 리스트 보여주기
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

        #mainLayout = QtGui.QHBoxLayout()
        #mainLayout.addWidget(self.treeWidget)

        self.quitButton = QtGui.QPushButton("Quit", self)
        self.quitButton.setFixedWidth(100)
        self.quitButton.move(860, 760)
        self.quitButton.setAutoDefault(True)
        self.quitButton.clicked.connect(self.onQuit)

        #self.resize(580,800)
        self.setGeometry(100, 100, 1000, 800)
        self.setFixedWidth(1000)
        self.setFixedHeight(800)
        self.setWindowTitle(u"체결용 기계부품 설계 SW")
        self.show()

    def clickedItem(self, parent):
        if self.treeWidget.currentItem().text(0) == u"육각볼트":
            self.group2.hide()
            self.group3.hide()
            self.group4.hide()
            self.group5.hide()
            self.group6.hide()

            self.label1 = QtGui.QLabel(u"육각볼트(Hex Bolt)의 설계", self.group1)
            self.label1.setFont('Courier')
            self.label1.setStyleSheet("font: bold; font-size: 12pt;")
            self.label1.move(270, 10)
            self.label1.setAlignment(QtCore.Qt.AlignRight)

            # Power group
            self.powergroup = QtGui.QGroupBox(self.group1)
            self.powergroup.setGeometry(QtCore.QRect(30,70,340,100))
            self.powergroup.setTitle(u"작용하는 힘의 종류")
            self.powergroup.setStyleSheet("font-size: 10pt;")
            self.powergroup.setFont('Courier')

            self.r1 = QtGui.QRadioButton(u"축하중만 작용하는 경우", self.powergroup)
            self.r1.move(40,40)
            self.r2 = QtGui.QRadioButton(u"축하중과 비틀림 모멘트가 동시에 작용하는 경우", self.powergroup)
            self.r2.move(40,65)
            self.r1.setChecked(True)

            # Variable group
            self.varigroup = QtGui.QGroupBox(self.group1)
            self.varigroup.setGeometry(QtCore.QRect(30,180,340,190))
            self.varigroup.setTitle(u"설계 변수")
            self.varigroup.setStyleSheet("font-size: 10pt;")
            self.varigroup.setFont('Courier')

            self.label2 = QtGui.QLabel(u"인장강도", self.varigroup)
            self.label2.move(40, 40)
            self.numericInput2 = QtGui.QLineEdit(self.varigroup)
            self.numericInput2.setFixedWidth(50)
            self.numericInput2.move(170, 35)
            self.popupItems2 = (u"(MPa)", u"(ksi)")
            self.popup2 = QtGui.QComboBox(self.varigroup)
            self.popup2.addItems(self.popupItems2)
            self.popup2.setCurrentIndex(self.popupItems2.index(u"(MPa)"))
            self.popup2.move(230, 35)
            self.tableButton = QtGui.QPushButton(u"철의 인장강도 Table", self.varigroup)
            self.tableButton.clicked.connect(self.onTable1_1)
            self.tableButton.setFixedWidth(180)
            self.tableButton.setAutoDefault(True)
            self.tableButton.move(90,65)
            self.label3 = QtGui.QLabel(u"안전계수", self.varigroup)
            self.label3.move(40, 100)
            self.numericInput3 = QtGui.QLineEdit(self.varigroup)
            self.numericInput3.setFixedWidth(50)
            self.numericInput3.move(170, 95)
            self.label4 = QtGui.QLabel(u"축하중", self.varigroup)
            self.label4.move(40, 125)
            self.numericInput4 = QtGui.QLineEdit(self.varigroup)
            self.numericInput4.setFixedWidth(50)
            self.numericInput4.move(170, 120)
            self.popupItems4 = (u"(N)", u"(lbf)")
            self.popup4 = QtGui.QComboBox(self.varigroup)
            self.popup4.addItems(self.popupItems4)
            self.popup4.setCurrentIndex(self.popupItems4.index(u"(N)"))
            self.popup4.move(230, 120)
            self.designButton = QtGui.QPushButton("Design", self.varigroup)
            self.designButton.clicked.connect(self.onDesign1)
            self.designButton.setFixedWidth(180)
            self.designButton.setAutoDefault(True)
            self.designButton.move(90, 150)

            # Result group
            self.resultgroup = QtGui.QGroupBox(self.group1)
            self.resultgroup.setGeometry(QtCore.QRect(30,380,340,100))
            self.resultgroup.setTitle(u"계산 결과값")
            self.resultgroup.setStyleSheet("font-size: 10pt;")
            self.resultgroup.setFont('Courier')

            self.label5 = QtGui.QLabel(u"허용인장응력", self.resultgroup)
            self.label5.move(40, 40)
            self.numericInput5 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput5.setFixedWidth(50)
            self.numericInput5.move(170, 35)
            self.popupItems5 = (u"(MPa)", u"(ksi)")
            self.popup5 = QtGui.QComboBox(self.resultgroup)
            self.popup5.addItems(self.popupItems5)
            self.popup5.setCurrentIndex(self.popupItems5.index(u"(MPa)"))
            self.popup5.move(230, 35)
            self.label6 = QtGui.QLabel(u"바깥지름", self.resultgroup)
            self.label6.move(40, 65)
            self.numericInput6 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput6.setFixedWidth(50)
            self.numericInput6.move(170, 60)
            self.popupItems6 = (u"(mm)", u"(inch)")
            self.popup6 = QtGui.QComboBox(self.resultgroup)
            self.popup6.addItems(self.popupItems6)
            self.popup6.setCurrentIndex(self.popupItems6.index(u"(mm)"))
            self.popup6.move(230, 60)

            # Modling group
            self.modelinggroup = QtGui.QGroupBox(self.group1)
            self.modelinggroup.setGeometry(QtCore.QRect(30,490,340,120))
            self.modelinggroup.setTitle(u"모델링")
            self.modelinggroup.setStyleSheet("font-size: 10pt;")
            self.modelinggroup.setFont('Courier')

            self.label7 = QtGui.QLabel(u"볼트의 길이", self.modelinggroup)
            self.label7.move(40, 40)
            self.numericInput7 = QtGui.QLineEdit(self.modelinggroup)
            self.numericInput7.setFixedWidth(50)
            self.numericInput7.move(170, 35)
            self.popupItems7 = (u"(mm)", u"(inch)")
            self.popup7 = QtGui.QComboBox(self.modelinggroup)
            self.popup7.addItems(self.popupItems7)
            self.popup7.setCurrentIndex(self.popupItems7.index(u"(mm)"))
            self.popup7.move(230, 35)
            self.generateButton = QtGui.QPushButton("Generate", self.modelinggroup)
            self.generateButton.clicked.connect(self.onGenerate1)
            self.generateButton.setFixedWidth(180)
            self.generateButton.setAutoDefault(True)
            self.generateButton.move(90, 65)
            self.label8 = QtGui.QLabel(u"*볼트의 길이에 따라 피치가 형성되지 않을 수 있음*", self.modelinggroup)
            self.label8.move(20, 95)
            self.label8.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환

            # Pictures 1
            self.refer_Img_GroupBox = QtGui.QGroupBox(self.group1)
            self.refer_Img_GroupBox.setGeometry(QtCore.QRect(380, 70, 370, 270))
            self.refer_Img_GroupBox.setTitle(u"육각볼트(Hex Bolt)")
            self.refer_Img_GroupBox.setStyleSheet("font-size: 10pt;")
            self.refer_Img_GroupBox.setFont('Courier')

            self.side_View_Img = QtGui.QPixmap(os.path.join(addonPath, "clamping_module\Hex_Bolt_Model.jpg"))
            self.side_View_label = QtGui.QLabel(self.refer_Img_GroupBox)
            self.side_View_label.setPixmap(self.side_View_Img)
            self.side_View_label.resize(self.side_View_Img.width(), self.side_View_Img.height())
            self.side_View_label.move(95, 30)

            self.refer_Img_GroupBox1 = QtGui.QGroupBox(self.group1)
            self.refer_Img_GroupBox1.setGeometry(QtCore.QRect(380, 350, 370, 260))
            self.refer_Img_GroupBox1.setTitle(u"계산 공식")
            self.refer_Img_GroupBox1.setStyleSheet("font-size: 10pt;")
            self.refer_Img_GroupBox1.setFont('Courier')

            self.side_View_Img1 = QtGui.QPixmap(os.path.join(addonPath, "clamping_module\Hex_Bolt_Calculation.jpg"))
            self.side_View_label1 = QtGui.QLabel(self.refer_Img_GroupBox1)
            self.side_View_label1.setPixmap(self.side_View_Img1)
            self.side_View_label1.resize(self.side_View_Img1.width(), self.side_View_Img1.height())
            self.side_View_label1.move(10, 30)

            self.group1.show()

        elif self.treeWidget.currentItem().text(0) == u"사각볼트":
            self.group1.hide()
            self.group3.hide()
            self.group4.hide()
            self.group5.hide()
            self.group6.hide()

            self.label1 = QtGui.QLabel(u"사각볼트(Square Bolt)의 설계", self.group2)
            self.label1.setFont('Courier')
            self.label1.setStyleSheet("font: bold; font-size: 12pt;")
            self.label1.move(270, 10)
            self.label1.setAlignment(QtCore.Qt.AlignRight)

            # Power group
            self.powergroup = QtGui.QGroupBox(self.group2)
            self.powergroup.setGeometry(QtCore.QRect(30,70,340,100))
            self.powergroup.setTitle(u"작용하는 힘의 종류")
            self.powergroup.setStyleSheet("font-size: 10pt;")
            self.powergroup.setFont('Courier')

            self.r1 = QtGui.QRadioButton(u"축하중만 작용하는 경우", self.powergroup)
            self.r1.move(40,40)
            self.r2 = QtGui.QRadioButton(u"축하중과 비틀림 모멘트가 동시에 작용하는 경우", self.powergroup)
            self.r2.move(40,65)
            self.r1.setChecked(True)

            # Variable group
            self.varigroup = QtGui.QGroupBox(self.group2)
            self.varigroup.setGeometry(QtCore.QRect(30,180,340,190))
            self.varigroup.setTitle(u"설계 변수")
            self.varigroup.setStyleSheet("font-size: 10pt;")
            self.varigroup.setFont('Courier')

            self.label2 = QtGui.QLabel(u"인장강도", self.varigroup)
            self.label2.move(40, 40)
            self.numericInput2 = QtGui.QLineEdit(self.varigroup)
            self.numericInput2.setFixedWidth(50)
            self.numericInput2.move(170, 35)
            self.popupItems2 = (u"(MPa)", u"(ksi)")
            self.popup2 = QtGui.QComboBox(self.varigroup)
            self.popup2.addItems(self.popupItems2)
            self.popup2.setCurrentIndex(self.popupItems2.index(u"(MPa)"))
            self.popup2.move(230, 35)
            self.tableButton = QtGui.QPushButton(u"철의 인장강도 Table", self.varigroup)
            self.tableButton.clicked.connect(self.onTable2_1)
            self.tableButton.setFixedWidth(180)
            self.tableButton.setAutoDefault(True)
            self.tableButton.move(90,65)
            self.label3 = QtGui.QLabel(u"안전계수", self.varigroup)
            self.label3.move(40, 100)
            self.numericInput3 = QtGui.QLineEdit(self.varigroup)
            self.numericInput3.setFixedWidth(50)
            self.numericInput3.move(170, 95)
            self.label4 = QtGui.QLabel(u"축하중", self.varigroup)
            self.label4.move(40, 125)
            self.numericInput4 = QtGui.QLineEdit(self.varigroup)
            self.numericInput4.setFixedWidth(50)
            self.numericInput4.move(170, 120)
            self.popupItems4 = (u"(N)", u"(lbf)")
            self.popup4 = QtGui.QComboBox(self.varigroup)
            self.popup4.addItems(self.popupItems4)
            self.popup4.setCurrentIndex(self.popupItems4.index(u"(N)"))
            self.popup4.move(230, 120)
            self.designButton = QtGui.QPushButton("Design", self.varigroup)
            self.designButton.clicked.connect(self.onDesign2)
            self.designButton.setFixedWidth(180)
            self.designButton.setAutoDefault(True)
            self.designButton.move(90, 150)

            # Result group
            self.resultgroup = QtGui.QGroupBox(self.group2)
            self.resultgroup.setGeometry(QtCore.QRect(30,380,340,100))
            self.resultgroup.setTitle(u"계산 결과값")
            self.resultgroup.setStyleSheet("font-size: 10pt;")
            self.resultgroup.setFont('Courier')

            self.label5 = QtGui.QLabel(u"허용인장응력", self.resultgroup)
            self.label5.move(40, 40)
            self.numericInput5 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput5.setFixedWidth(50)
            self.numericInput5.move(170, 35)
            self.popupItems5 = (u"(MPa)", u"(ksi)")
            self.popup5 = QtGui.QComboBox(self.resultgroup)
            self.popup5.addItems(self.popupItems5)
            self.popup5.setCurrentIndex(self.popupItems5.index(u"(MPa)"))
            self.popup5.move(230, 35)
            self.label6 = QtGui.QLabel(u"바깥지름", self.resultgroup)
            self.label6.move(40, 65)
            self.numericInput6 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput6.setFixedWidth(50)
            self.numericInput6.move(170, 60)
            self.popupItems6 = (u"(mm)", u"(inch)")
            self.popup6 = QtGui.QComboBox(self.resultgroup)
            self.popup6.addItems(self.popupItems6)
            self.popup6.setCurrentIndex(self.popupItems6.index(u"(mm)"))
            self.popup6.move(230, 60)

            # Modling group
            self.modelinggroup = QtGui.QGroupBox(self.group2)
            self.modelinggroup.setGeometry(QtCore.QRect(30,490,340,120))
            self.modelinggroup.setTitle(u"모델링")
            self.modelinggroup.setStyleSheet("font-size: 10pt;")
            self.modelinggroup.setFont('Courier')

            self.label7 = QtGui.QLabel(u"볼트의 길이", self.modelinggroup)
            self.label7.move(40, 40)
            self.numericInput7 = QtGui.QLineEdit(self.modelinggroup)
            self.numericInput7.setFixedWidth(50)
            self.numericInput7.move(170, 35)
            self.popupItems7 = (u"(mm)", u"(inch)")
            self.popup7 = QtGui.QComboBox(self.modelinggroup)
            self.popup7.addItems(self.popupItems7)
            self.popup7.setCurrentIndex(self.popupItems7.index(u"(mm)"))
            self.popup7.move(230, 35)
            self.generateButton = QtGui.QPushButton("Generate", self.modelinggroup)
            self.generateButton.clicked.connect(self.onGenerate2)
            self.generateButton.setFixedWidth(180)
            self.generateButton.setAutoDefault(True)
            self.generateButton.move(90, 65)
            self.label8 = QtGui.QLabel(u"*볼트의 길이에 따라 피치가 형성되지 않을 수 있음*", self.modelinggroup)
            self.label8.move(20, 95)
            self.label8.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환

            # Pictures 1
            self.refer_Img_GroupBox = QtGui.QGroupBox(self.group2)
            self.refer_Img_GroupBox.setGeometry(QtCore.QRect(380, 70, 370, 270))
            self.refer_Img_GroupBox.setTitle(u"사각볼트(Square Bolt)")
            self.refer_Img_GroupBox.setStyleSheet("font-size: 10pt;")
            self.refer_Img_GroupBox.setFont('Courier')

            self.side_View_Img = QtGui.QPixmap(os.path.join(addonPath, "clamping_module\Square_Bolt_Model.jpg"))
            self.side_View_label = QtGui.QLabel(self.refer_Img_GroupBox)
            self.side_View_label.setPixmap(self.side_View_Img)
            self.side_View_label.resize(self.side_View_Img.width(), self.side_View_Img.height())
            self.side_View_label.move(95, 30)

            self.refer_Img_GroupBox1 = QtGui.QGroupBox(self.group2)
            self.refer_Img_GroupBox1.setGeometry(QtCore.QRect(380, 350, 370, 260))
            self.refer_Img_GroupBox1.setTitle(u"계산 공식")
            self.refer_Img_GroupBox1.setStyleSheet("font-size: 10pt;")
            self.refer_Img_GroupBox1.setFont('Courier')

            self.side_View_Img1 = QtGui.QPixmap(os.path.join(addonPath, "clamping_module\Square_Bolt_Calculation.jpg"))
            self.side_View_label1 = QtGui.QLabel(self.refer_Img_GroupBox1)
            self.side_View_label1.setPixmap(self.side_View_Img1)
            self.side_View_label1.resize(self.side_View_Img1.width(), self.side_View_Img1.height())
            self.side_View_label1.move(10, 30)

            self.group2.show()


        elif self.treeWidget.currentItem().text(0) == u"육각너트":
            self.group1.hide()
            self.group2.hide()
            self.group4.hide()
            self.group5.hide()
            self.group6.hide()

            self.label1 = QtGui.QLabel(u"육각너트(Square Nut)의 설계", self.group3)
            self.label1.setFont('Courier')
            self.label1.setStyleSheet("font: bold; font-size: 12pt;")
            self.label1.move(270, 10)
            self.label1.setAlignment(QtCore.Qt.AlignRight)

            # Power group
            self.powergroup = QtGui.QGroupBox(self.group3)
            self.powergroup.setGeometry(QtCore.QRect(30,70,340,165))
            self.powergroup.setTitle(u"재료 설정")
            self.powergroup.setStyleSheet("font-size: 10pt;")
            self.powergroup.setFont('Courier')

            self.label2 = QtGui.QLabel(u"사용처", self.powergroup)
            self.label2.setFont('Courier')
            self.label2.move(40, 40)
            self.popupItems2 = (u"(결합용)", u"(전동용)")
            self.popup2 = QtGui.QComboBox(self.powergroup)
            self.popup2.addItems(self.popupItems2)
            self.popup2.setCurrentIndex(self.popupItems2.index(u"(결합용)"))
            self.popup2.move(230, 35)
            self.label3 = QtGui.QLabel(u"볼트의 재료", self.powergroup)
            self.label3.setFont('Courier')
            self.label3.move(40, 65)
            self.popupItems3 = (u"(연강)",u"(경강)", u"(강)")
            self.popup3 = QtGui.QComboBox(self.powergroup)
            self.popup3.addItems(self.popupItems3)
            self.popup3.setCurrentIndex(self.popupItems3.index(u"(연강)"))
            self.popup3.move(230, 60)
            self.label4 = QtGui.QLabel(u"너트의 재료", self.powergroup)
            self.label4.setFont('Courier')
            self.label4.move(40, 90)
            self.popupItems4 = (u"(연강)",u"(경강)", u"(청동)", u"(주철)")
            self.popup4 = QtGui.QComboBox(self.powergroup)
            self.popup4.addItems(self.popupItems4)
            self.popup4.setCurrentIndex(self.popupItems4.index(u"(연강)"))
            self.popup4.move(230, 85)
            self.tableButton = QtGui.QPushButton(u"허용 면 압력 table", self.powergroup)
            self.tableButton.clicked.connect(self.onTable3_1)
            self.tableButton.setFixedWidth(180)
            self.tableButton.setAutoDefault(True)
            self.tableButton.move(90, 115)
            self.label15 = QtGui.QLabel(u"*너트의 재료는 볼트의 재료보다 무른 재료여야함*", self.powergroup)
            self.label15.move(20, 145)
            self.label15.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환

            # Variable group
            self.varigroup = QtGui.QGroupBox(self.group3)
            self.varigroup.setGeometry(QtCore.QRect(30,245,340,200))
            self.varigroup.setTitle(u"설계 변수")
            self.varigroup.setFont('Courier')

            self.label6 = QtGui.QLabel(u"피치", self.varigroup)
            self.label6.move(40, 40)
            self.numericInput6 = QtGui.QLineEdit(self.varigroup)
            self.numericInput6.setFixedWidth(50)
            self.numericInput6.move(170, 35)
            self.popupItems6 = (u"(mm)", u"(inch)")
            self.popup6 = QtGui.QComboBox(self.varigroup)
            self.popup6.addItems(self.popupItems6)
            self.popup6.setCurrentIndex(self.popupItems6.index(u"(mm)"))
            self.popup6.move(230, 35)
            self.label7 = QtGui.QLabel(u"바깥지름", self.varigroup)
            self.label7.move(40, 65)
            self.numericInput7 = QtGui.QLineEdit(self.varigroup)
            self.numericInput7.setFixedWidth(50)
            self.numericInput7.move(170, 60)
            self.popupItems7 = (u"(mm)", u"(inch)")
            self.popup7 = QtGui.QComboBox(self.varigroup)
            self.popup7.addItems(self.popupItems7)
            self.popup7.setCurrentIndex(self.popupItems7.index(u"(mm)"))
            self.popup7.move(230, 60)
            self.label8 = QtGui.QLabel(u"안지름", self.varigroup)
            self.label8.move(40, 90)
            self.numericInput8 = QtGui.QLineEdit(self.varigroup)
            self.numericInput8.setFixedWidth(50)
            self.numericInput8.move(170, 85)
            self.popupItems8 = (u"(mm)", u"(inch)")
            self.popup8 = QtGui.QComboBox(self.varigroup)
            self.popup8.addItems(self.popupItems8)
            self.popup8.setCurrentIndex(self.popupItems8.index(u"(mm)"))
            self.popup8.move(230, 85)
            self.label9 = QtGui.QLabel(u"축하중", self.varigroup)
            self.label9.move(40, 115)
            self.numericInput9 = QtGui.QLineEdit(self.varigroup)
            self.numericInput9.setFixedWidth(50)
            self.numericInput9.move(170, 110)
            self.popupItems9 = (u"(N)", u"(lbf)")
            self.popup9 = QtGui.QComboBox(self.varigroup)
            self.popup9.addItems(self.popupItems9)
            self.popup9.setCurrentIndex(self.popupItems9.index(u"(N)"))
            self.popup9.move(230, 110)
            self.label10 = QtGui.QLabel(u"안전계수", self.varigroup)
            self.label10.move(40, 140)
            self.numericInput10 = QtGui.QLineEdit("1", self.varigroup)
            self.numericInput10.setFixedWidth(50)
            self.numericInput10.move(170, 135)
            self.designButton = QtGui.QPushButton("Design", self.varigroup)
            self.designButton.clicked.connect(self.onDesign3)
            self.designButton.setFixedWidth(180)
            self.designButton.setAutoDefault(True)
            self.designButton.move(90, 165)

            # Result group
            self.resultgroup = QtGui.QGroupBox(self.group3)
            self.resultgroup.setGeometry(QtCore.QRect(30,455,340,115))
            self.resultgroup.setTitle(u"계산 결과값")
            self.resultgroup.setFont('Courier')

            self.label11 = QtGui.QLabel(u"최소 너트 높이", self.resultgroup)
            self.label11.move(40, 40)
            self.numericInput11 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput11.setFixedWidth(50)
            self.numericInput11.move(170, 35)
            self.popupItems11 = (u"(mm)", u"(inch)")
            self.popup11 = QtGui.QComboBox(self.resultgroup)
            self.popup11.addItems(self.popupItems11)
            self.popup11.setCurrentIndex(self.popupItems11.index(u"(mm)"))
            self.popup11.move(230, 35)
            self.label12 = QtGui.QLabel(u"나사산의 개수", self.resultgroup)
            self.label12.move(40, 65)
            self.numericInput12 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput12.setFixedWidth(50)
            self.numericInput12.move(170, 60)
            self.label13 = QtGui.QLabel(u"허용면 압력", self.resultgroup)
            self.label13.move(40, 90)
            self.numericInput13 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput13.setFixedWidth(50)
            self.numericInput13.move(170, 85)
            self.popupItems13 = (u"(MPa)", u"(ksi)")
            self.popup13 = QtGui.QComboBox(self.resultgroup)
            self.popup13.addItems(self.popupItems13)
            self.popup13.setCurrentIndex(self.popupItems13.index(u"(MPa)"))
            self.popup13.move(230, 85)

            # Modeling group
            self.modelinggroup = QtGui.QGroupBox(self.group3)
            self.modelinggroup.setGeometry(QtCore.QRect(30,580,340,115))
            self.modelinggroup.setTitle(u"모델링")
            self.modelinggroup.setFont('Courier')

            self.label14 = QtGui.QLabel(u"너트 높이", self.modelinggroup)
            self.label14.move(40, 40)
            self.numericInput14 = QtGui.QLineEdit(self.modelinggroup)
            self.numericInput14.setFixedWidth(50)
            self.numericInput14.move(170, 35)
            self.popupItems14 = (u"(mm)", u"(inch)")
            self.popup14 = QtGui.QComboBox(self.modelinggroup)
            self.popup14.addItems(self.popupItems14)
            self.popup14.setCurrentIndex(self.popupItems14.index(u"(mm)"))
            self.popup14.move(230, 35)
            self.generateButton = QtGui.QPushButton("Generate", self.modelinggroup)
            self.generateButton.clicked.connect(self.onGenerate3)
            self.generateButton.setFixedWidth(180)
            self.generateButton.setAutoDefault(True)
            self.generateButton.move(90, 65)
            self.label15 = QtGui.QLabel(u"*너트의 길이에 따라 피치가 형성되지 않을 수 있음*", self.modelinggroup)
            self.label15.move(20, 95)
            self.label15.setStyleSheet("color: rgb(255,0,0);")

            # Pictures 1
            self.refer_Img_GroupBox = QtGui.QGroupBox(self.group3)
            self.refer_Img_GroupBox.setGeometry(QtCore.QRect(380, 70, 370, 270))
            self.refer_Img_GroupBox.setTitle(u"육각너트(Hex Nut)")
            self.refer_Img_GroupBox.setStyleSheet("font-size: 10pt;")
            self.refer_Img_GroupBox.setFont('Courier')

            self.side_View_Img = QtGui.QPixmap(os.path.join(addonPath, "clamping_module\Hex_Nut_Model.jpg"))
            self.side_View_label = QtGui.QLabel(self.refer_Img_GroupBox)
            self.side_View_label.setPixmap(self.side_View_Img)
            self.side_View_label.resize(self.side_View_Img.width(), self.side_View_Img.height())
            self.side_View_label.move(95, 30)

            self.refer_Img_GroupBox1 = QtGui.QGroupBox(self.group3)
            self.refer_Img_GroupBox1.setGeometry(QtCore.QRect(380, 350, 370, 260))
            self.refer_Img_GroupBox1.setTitle(u"계산 공식")
            self.refer_Img_GroupBox1.setStyleSheet("font-size: 10pt;")
            self.refer_Img_GroupBox1.setFont('Courier')

            self.side_View_Img1 = QtGui.QPixmap(os.path.join(addonPath, "clamping_module\Hex_Nut_Calculation.PNG"))
            self.side_View_label1 = QtGui.QLabel(self.refer_Img_GroupBox1)
            self.side_View_label1.setPixmap(self.side_View_Img1)
            self.side_View_label1.resize(self.side_View_Img1.width(), self.side_View_Img1.height())
            self.side_View_label1.move(10, 30)

            self.group3.show()

        elif self.treeWidget.currentItem().text(0) == u"사각너트":
            self.group1.hide()
            self.group2.hide()
            self.group3.hide()
            self.group5.hide()
            self.group6.hide()

            self.label1 = QtGui.QLabel(u"사각너트(Square Nut)의 설계", self.group4)
            self.label1.setFont('Courier')
            self.label1.setStyleSheet("font: bold; font-size: 12pt;")
            self.label1.move(270, 10)
            self.label1.setAlignment(QtCore.Qt.AlignRight)

            # Power group
            self.powergroup = QtGui.QGroupBox(self.group4)
            self.powergroup.setGeometry(QtCore.QRect(30,70,340,165))
            self.powergroup.setTitle(u"재료 설정")
            self.powergroup.setStyleSheet("font-size: 10pt;")
            self.powergroup.setFont('Courier')

            self.label2 = QtGui.QLabel(u"사용처", self.powergroup)
            self.label2.setFont('Courier')
            self.label2.move(40, 40)
            self.popupItems2 = (u"(결합용)", u"(전동용)")
            self.popup2 = QtGui.QComboBox(self.powergroup)
            self.popup2.addItems(self.popupItems2)
            self.popup2.setCurrentIndex(self.popupItems2.index(u"(결합용)"))
            self.popup2.move(230, 35)
            self.label3 = QtGui.QLabel(u"볼트의 재료", self.powergroup)
            self.label3.setFont('Courier')
            self.label3.move(40, 65)
            self.popupItems3 = (u"(연강)",u"(경강)", u"(강)")
            self.popup3 = QtGui.QComboBox(self.powergroup)
            self.popup3.addItems(self.popupItems3)
            self.popup3.setCurrentIndex(self.popupItems3.index(u"(연강)"))
            self.popup3.move(230, 60)
            self.label4 = QtGui.QLabel(u"너트의 재료", self.powergroup)
            self.label4.setFont('Courier')
            self.label4.move(40, 90)
            self.popupItems4 = (u"(연강)",u"(경강)", u"(청동)", u"(주철)")
            self.popup4 = QtGui.QComboBox(self.powergroup)
            self.popup4.addItems(self.popupItems4)
            self.popup4.setCurrentIndex(self.popupItems4.index(u"(연강)"))
            self.popup4.move(230, 85)
            self.tableButton = QtGui.QPushButton(u"허용 면 압력 table", self.powergroup)
            self.tableButton.clicked.connect(self.onTable4_1)
            self.tableButton.setFixedWidth(180)
            self.tableButton.setAutoDefault(True)
            self.tableButton.move(90, 115)
            self.label15 = QtGui.QLabel(u"*너트의 재료는 볼트의 재료보다 무른 재료여야함*", self.powergroup)
            self.label15.move(20, 145)
            self.label15.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환

            # Variable group
            self.varigroup = QtGui.QGroupBox(self.group4)
            self.varigroup.setGeometry(QtCore.QRect(30,245,340,200))
            self.varigroup.setTitle(u"설계 변수")
            self.varigroup.setFont('Courier')

            self.label6 = QtGui.QLabel(u"피치", self.varigroup)
            self.label6.move(40, 40)
            self.numericInput6 = QtGui.QLineEdit(self.varigroup)
            self.numericInput6.setFixedWidth(50)
            self.numericInput6.move(170, 35)
            self.popupItems6 = (u"(mm)", u"(inch)")
            self.popup6 = QtGui.QComboBox(self.varigroup)
            self.popup6.addItems(self.popupItems6)
            self.popup6.setCurrentIndex(self.popupItems6.index(u"(mm)"))
            self.popup6.move(230, 35)
            self.label7 = QtGui.QLabel(u"바깥지름", self.varigroup)
            self.label7.move(40, 65)
            self.numericInput7 = QtGui.QLineEdit(self.varigroup)
            self.numericInput7.setFixedWidth(50)
            self.numericInput7.move(170, 60)
            self.popupItems7 = (u"(mm)", u"(inch)")
            self.popup7 = QtGui.QComboBox(self.varigroup)
            self.popup7.addItems(self.popupItems7)
            self.popup7.setCurrentIndex(self.popupItems7.index(u"(mm)"))
            self.popup7.move(230, 60)
            self.label8 = QtGui.QLabel(u"안지름", self.varigroup)
            self.label8.move(40, 90)
            self.numericInput8 = QtGui.QLineEdit(self.varigroup)
            self.numericInput8.setFixedWidth(50)
            self.numericInput8.move(170, 85)
            self.popupItems8 = (u"(mm)", u"(inch)")
            self.popup8 = QtGui.QComboBox(self.varigroup)
            self.popup8.addItems(self.popupItems8)
            self.popup8.setCurrentIndex(self.popupItems8.index(u"(mm)"))
            self.popup8.move(230, 85)
            self.label9 = QtGui.QLabel(u"축하중", self.varigroup)
            self.label9.move(40, 115)
            self.numericInput9 = QtGui.QLineEdit(self.varigroup)
            self.numericInput9.setFixedWidth(50)
            self.numericInput9.move(170, 110)
            self.popupItems9 = (u"(N)", u"(lbf)")
            self.popup9 = QtGui.QComboBox(self.varigroup)
            self.popup9.addItems(self.popupItems9)
            self.popup9.setCurrentIndex(self.popupItems9.index(u"(N)"))
            self.popup9.move(230, 110)
            self.label10 = QtGui.QLabel(u"안전계수", self.varigroup)
            self.label10.move(40, 140)
            self.numericInput10 = QtGui.QLineEdit("1", self.varigroup)
            self.numericInput10.setFixedWidth(50)
            self.numericInput10.move(170, 135)
            self.designButton = QtGui.QPushButton("Design", self.varigroup)
            self.designButton.clicked.connect(self.onDesign4)
            self.designButton.setFixedWidth(180)
            self.designButton.setAutoDefault(True)
            self.designButton.move(90, 165)

            # Result group
            self.resultgroup = QtGui.QGroupBox(self.group4)
            self.resultgroup.setGeometry(QtCore.QRect(30,455,340,115))
            self.resultgroup.setTitle(u"계산 결과값")
            self.resultgroup.setFont('Courier')

            self.label11 = QtGui.QLabel(u"최소 너트 높이", self.resultgroup)
            self.label11.move(40, 40)
            self.numericInput11 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput11.setFixedWidth(50)
            self.numericInput11.move(170, 35)
            self.popupItems11 = (u"(mm)", u"(inch)")
            self.popup11 = QtGui.QComboBox(self.resultgroup)
            self.popup11.addItems(self.popupItems11)
            self.popup11.setCurrentIndex(self.popupItems11.index(u"(mm)"))
            self.popup11.move(230, 35)
            self.label12 = QtGui.QLabel(u"나사산의 개수", self.resultgroup)
            self.label12.move(40, 65)
            self.numericInput12 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput12.setFixedWidth(50)
            self.numericInput12.move(170, 60)
            self.label13 = QtGui.QLabel(u"허용면 압력", self.resultgroup)
            self.label13.move(40, 90)
            self.numericInput13 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput13.setFixedWidth(50)
            self.numericInput13.move(170, 85)
            self.popupItems13 = (u"(MPa)", u"(ksi)")
            self.popup13 = QtGui.QComboBox(self.resultgroup)
            self.popup13.addItems(self.popupItems13)
            self.popup13.setCurrentIndex(self.popupItems13.index(u"(MPa)"))
            self.popup13.move(230, 85)

            # Modeling group
            self.modelinggroup = QtGui.QGroupBox(self.group4)
            self.modelinggroup.setGeometry(QtCore.QRect(30,580,340,115))
            self.modelinggroup.setTitle(u"모델링")
            self.modelinggroup.setFont('Courier')

            self.label14 = QtGui.QLabel(u"너트 높이", self.modelinggroup)
            self.label14.move(40, 40)
            self.numericInput14 = QtGui.QLineEdit(self.modelinggroup)
            self.numericInput14.setFixedWidth(50)
            self.numericInput14.move(170, 35)
            self.popupItems14 = (u"(mm)", u"(inch)")
            self.popup14 = QtGui.QComboBox(self.modelinggroup)
            self.popup14.addItems(self.popupItems14)
            self.popup14.setCurrentIndex(self.popupItems14.index(u"(mm)"))
            self.popup14.move(230, 35)
            self.generateButton = QtGui.QPushButton("Generate", self.modelinggroup)
            self.generateButton.clicked.connect(self.onGenerate4)
            self.generateButton.setFixedWidth(180)
            self.generateButton.setAutoDefault(True)
            self.generateButton.move(90, 65)
            self.label15 = QtGui.QLabel(u"*너트의 길이에 따라 피치가 형성되지 않을 수 있음*", self.modelinggroup)
            self.label15.move(20, 95)
            self.label15.setStyleSheet("color: rgb(255,0,0);")

            # Pictures 1
            self.refer_Img_GroupBox = QtGui.QGroupBox(self.group4)
            self.refer_Img_GroupBox.setGeometry(QtCore.QRect(380, 70, 370, 270))
            self.refer_Img_GroupBox.setTitle(u"사각너트(Square Nut)")
            self.refer_Img_GroupBox.setStyleSheet("font-size: 10pt;")
            self.refer_Img_GroupBox.setFont('Courier')

            self.side_View_Img = QtGui.QPixmap(os.path.join(addonPath, "clamping_module\Square_Nut_Model.jpg"))
            self.side_View_label = QtGui.QLabel(self.refer_Img_GroupBox)
            self.side_View_label.setPixmap(self.side_View_Img)
            self.side_View_label.resize(self.side_View_Img.width(), self.side_View_Img.height())
            self.side_View_label.move(95, 30)

            self.refer_Img_GroupBox1 = QtGui.QGroupBox(self.group4)
            self.refer_Img_GroupBox1.setGeometry(QtCore.QRect(380, 350, 370, 260))
            self.refer_Img_GroupBox1.setTitle(u"계산 공식")
            self.refer_Img_GroupBox1.setStyleSheet("font-size: 10pt;")
            self.refer_Img_GroupBox1.setFont('Courier')

            self.side_View_Img1 = QtGui.QPixmap(os.path.join(addonPath, "clamping_module\Square_Nut_Calculation.PNG"))
            self.side_View_label1 = QtGui.QLabel(self.refer_Img_GroupBox1)
            self.side_View_label1.setPixmap(self.side_View_Img1)
            self.side_View_label1.resize(self.side_View_Img1.width(), self.side_View_Img1.height())
            self.side_View_label1.move(10, 30)

            self.group4.show()

        elif self.treeWidget.currentItem().text(0) == u"와셔":
            self.group1.hide()
            self.group2.hide()
            self.group3.hide()
            self.group4.hide()
            self.group6.hide()



            self.group5.show()

        elif self.treeWidget.currentItem().text(0) == u"리벳":
            self.group1.hide()
            self.group2.hide()
            self.group3.hide()
            self.group4.hide()
            self.group5.hide()

            self.group6.show()

    def onTable1_1(self):
        ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

        buf = QtGui.QPixmap(os.path.join(addonPath, "clamping_module\Hex_Bolt_Table_1.jpg"))  #C 드라이브에 넣었음

        Imageview1 = QtGui.QLabel(ks)
        Imageview1.setPixmap(buf)
        Imageview1.resize(buf.width(), buf.height())
        Imageview1.move(0, 0)
        Imageview1.show()

        ks.setGeometry(750, 100, buf.width(), buf.height())
        ks.setWindowTitle("철의 인장강도 Table")
        ks.show()
        ks.exec_()

    def onTable2_1(self):
        ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

        buf = QtGui.QPixmap(os.path.join(addonPath, "clamping_module\Square_Bolt_Table_1.jpg"))  #C 드라이브에 넣었음

        Imageview1 = QtGui.QLabel(ks)
        Imageview1.setPixmap(buf)
        Imageview1.resize(buf.width(), buf.height())
        Imageview1.move(0, 0)
        Imageview1.show()

        ks.setGeometry(750, 100, buf.width(), buf.height())
        ks.setWindowTitle("철의 인장강도 Table")
        ks.show()
        ks.exec_()

    def onTable3_1(self):
        ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

        buf = QtGui.QPixmap(os.path.join(addonPath, "clamping_module\Hex_Nut_Table_1.PNG"))  #C 드라이브에 넣었음

        Imageview1 = QtGui.QLabel(ks)
        Imageview1.setPixmap(buf)
        Imageview1.resize(buf.width(), buf.height())
        Imageview1.move(0, 0)
        Imageview1.show()

        ks.setGeometry(750, 100, buf.width(), buf.height())
        ks.setWindowTitle(u"허용 면 압력 Table")
        ks.show()
        ks.exec_()

    def onTable4_1(self):
        ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러

        buf = QtGui.QPixmap(os.path.join(addonPath, "clamping_module\Square_Nut_Table_1.PNG"))  #C 드라이브에 넣었음

        Imageview1 = QtGui.QLabel(ks)
        Imageview1.setPixmap(buf)
        Imageview1.resize(buf.width(), buf.height())
        Imageview1.move(0, 0)
        Imageview1.show()

        ks.setGeometry(750, 100, buf.width(), buf.height())
        ks.setWindowTitle(u"허용 면 압력 Table")
        ks.show()
        ks.exec_()

    def onDesign1(self):
        if self.popup2.currentText() == u"(MPa)":
            m_MPa = float(self.numericInput2.text())
        elif self.popup2.currentText() == u"(ksi)":
            m_MPa = 6.89475908677537 * float(self.numericInput2.text())
        if self.popup4.currentText() == u"(N)":
            q_Newton = float(self.numericInput4.text())
        elif self.popup2.currentText() == u"(lbf)":
            q_Newton = 4.44822 * float(self.numericInput4.text())

        n = float(self.numericInput3.text())                # 안전계수
        si_MPa = m_MPa / n                                      # 허용인장응력 계산

        if self.popup5.currentText() == u"(MPa)":
            self.numericInput5.setText(str(round(si_MPa, 3)))   # 허용인장응력 대입
        elif self.popup5.currentText() == u"(ksi)":
            si_ksi = si_MPa / 6.89475908677537
            self.numericInput5.setText(str(round(si_ksi, 3)))

        if self.r1.isChecked() == True:   # 축하중만 작용하는 경우
            d_mm = math.sqrt((2 * q_Newton) / (si_MPa))      # 바깥지름 계산
            if self.popup6.currentText() == u"(mm)":
                self.numericInput6.setText(str(round(d_mm, 3)))   # 바깥지름 대입
            elif self.popup6.currentText() == u"(inch)":
                d_inch = d_mm / 25.4
                self.numericInput6.setText(str(round(d_inch, 3)))   # 바깥지름 대입
        elif self.r2.isChecked() == True:
            d_mm = math.sqrt((8 * q_Newton) / (3 * si_MPa))      # 바깥지름 계산
            if self.popup6.currentText() == u"(mm)":
                self.numericInput6.setText(str(round(d_mm, 3)))     # 바깥지름 대입
            elif self.popup6.currentText() == u"(inch)":
                d_inch = d_mm / 25.4
                self.numericInput6.setText(str(round(d_inch, 3)))   # 바깥지름 대입


    def onDesign2(self):
        if self.popup2.currentText() == u"(MPa)":
            m_MPa = float(self.numericInput2.text())
        elif self.popup2.currentText() == u"(ksi)":
            m_MPa = 6.89475908677537 * float(self.numericInput2.text())
        if self.popup4.currentText() == u"(N)":
            q_Newton = float(self.numericInput4.text())
        elif self.popup2.currentText() == u"(lbf)":
            q_Newton = 4.44822 * float(self.numericInput4.text())

        n = float(self.numericInput3.text())                # 안전계수
        si_MPa = m_MPa / n                                      # 허용인장응력 계산

        if self.popup5.currentText() == u"(MPa)":
            self.numericInput5.setText(str(round(si_MPa, 3)))   # 허용인장응력 대입
        elif self.popup5.currentText() == u"(ksi)":
            si_ksi = si_MPa / 6.89475908677537
            self.numericInput5.setText(str(round(si_ksi, 3)))

        if self.r1.isChecked() == True:   # 축하중만 작용하는 경우
            d_mm = math.sqrt((2 * q_Newton) / (si_MPa))      # 바깥지름 계산
            if self.popup6.currentText() == u"(mm)":
                self.numericInput6.setText(str(round(d_mm, 3)))   # 바깥지름 대입
            elif self.popup6.currentText() == u"(inch)":
                d_inch = d_mm / 25.4
                self.numericInput6.setText(str(round(d_inch, 3)))   # 바깥지름 대입
        elif self.r2.isChecked() == True:
            d_mm = math.sqrt((8 * q_Newton) / (3 * si_MPa))      # 바깥지름 계산
            if self.popup6.currentText() == u"(mm)":
                self.numericInput6.setText(str(round(d_mm, 3)))     # 바깥지름 대입
            elif self.popup6.currentText() == u"(inch)":
                d_inch = d_mm / 25.4
                self.numericInput6.setText(str(round(d_inch, 3)))   # 바깥지름 대입


    def onDesign3(self):
        if self.popup6.currentText() == u"(mm)":  # 피치 (mm로 변환)
            p_mm = float(self.numericInput6.text())
        elif self.popup6.currentText() == u"(inch)":
            p_mm = 25.4 * float(self.numericInput6.text())
        if self.popup7.currentText() == u"(mm)":  # 바깥 지름 (mm로 변환)
            do_mm = float(self.numericInput7.text())
        elif self.popup7.currentText() == u"(inch)":
            do_mm = 25.4 * float(self.numericInput7.text())
        if self.popup8.currentText() == u"(mm)":  # 안 지름 (mm로 변환)
            di_mm = float(self.numericInput8.text())
        elif self.popup8.currentText() == u"(inch)":
            di_mm = 25.4 * float(self.numericInput8.text())
        if self.popup9.currentText() == u"(N)":  # 안 지름 (mm로 변환)
            Q_Newton = float(self.numericInput9.text())
        elif self.popup9.currentText() == u"(lbf)":
            Q_Newton = 4.44822 * float(self.numericInput9.text())
        SF = float(self.numericInput10.text())  # 안전 계수

        if self.popup2.currentText() == u"(결합용)":
            if self.popup3.currentText() == u"(연강)":
                if self.popup4.currentText() == u"(연강)":
                    q_MPa = 3.0*9.81

                elif self.popup4.currentText() == u"(청동)":
                    q_MPa = 3.0*9.81

                else:
                    q_MPa = 0

            elif self.popup3.currentText() == u"(경강)":
                if self.popup4.currentText() == u"(경강)":
                    q_MPa = 4.0*9.81

                elif self.popup4.currentText() == u"(청동)":
                    q_MPa = 3.0*9.81

                else:
                    q_MPa = 0

            elif self.popup3.currentText() == u"(강)":
                if self.popup4.currentText() == u"(주철)":
                    q_MPa = 1.5*9.81

                else:
                    q_MPa = 0

        else:
            if self.popup3.currentText() == u"(연강)":
                if self.popup4.currentText() == u"(연강)":
                    q_MPa = 1.0*9.81

                elif self.popup4.currentText() == u"(청동)":
                    q_MPa = 1.0*9.81

                else:
                    q_MPa = 0

            elif self.popup3.currentText() == u"(경강)":
                if self.popup4.currentText() == u"(경강)":
                    q_MPa = 1.3*9.81

                elif self.popup4.currentText() == u"(청동)":
                    q_MPa = 1.3*9.81

                else:
                    q_MPa = 0

            elif self.popup3.currentText() == u"(강)":
                if self.popup4.currentText() == u"(주철)":
                    q_MPa = 0.5*9.81
                else:
                    q_MPa = 0

        Z = Q_Newton * 4 / (math.pi * q_MPa * ( do_mm * do_mm - di_mm * di_mm))
        H_mm = Z * SF * p_mm

        if self.popup11.currentText() == u"(mm)":            # 최소 너트 높이
            self.numericInput11.setText(str(round(H_mm,3)))
        elif self.popup11.currentText() == u"(inch)":
            H_inch = 1 / 25.4 * H_mm
            self.numericInput11.setText(str(round(H_inch,3)))
        self.numericInput12.setText(str(round(Z,3)))         # 나사산의 개수
        if self.popup13.currentText() == u"(MPa)":           # 허용면압력
            self.numericInput13.setText(str(round(q_MPa,3)))
        elif self.popup13.currentText() == u"(ksi)":
            q_ksi = 1 / 6.89475908677537 * q_MPa
            self.numericInput13.setText(str(round(q_ksi,3)))

    def onDesign4(self):
        if self.popup6.currentText() == u"(mm)":  # 피치 (mm로 변환)
            p_mm = float(self.numericInput6.text())
        elif self.popup6.currentText() == u"(inch)":
            p_mm = 25.4 * float(self.numericInput6.text())
        if self.popup7.currentText() == u"(mm)":  # 바깥 지름 (mm로 변환)
            do_mm = float(self.numericInput7.text())
        elif self.popup7.currentText() == u"(inch)":
            do_mm = 25.4 * float(self.numericInput7.text())
        if self.popup8.currentText() == u"(mm)":  # 안 지름 (mm로 변환)
            di_mm = float(self.numericInput8.text())
        elif self.popup8.currentText() == u"(inch)":
            di_mm = 25.4 * float(self.numericInput8.text())
        if self.popup9.currentText() == u"(N)":  # 안 지름 (mm로 변환)
            Q_Newton = float(self.numericInput9.text())
        elif self.popup9.currentText() == u"(lbf)":
            Q_Newton = 4.44822 * float(self.numericInput9.text())
        SF = float(self.numericInput10.text())  # 안전 계수

        if self.popup2.currentText() == u"(결합용)":
            if self.popup3.currentText() == u"(연강)":
                if self.popup4.currentText() == u"(연강)":
                    q_MPa = 3.0*9.81

                elif self.popup4.currentText() == u"(청동)":
                    q_MPa = 3.0*9.81

                else:
                    q_MPa = 0

            elif self.popup3.currentText() == u"(경강)":
                if self.popup4.currentText() == u"(경강)":
                    q_MPa = 4.0*9.81

                elif self.popup4.currentText() == u"(청동)":
                    q_MPa = 3.0*9.81

                else:
                    q_MPa = 0

            elif self.popup3.currentText() == u"(강)":
                if self.popup4.currentText() == u"(주철)":
                    q_MPa = 1.5*9.81

                else:
                    q_MPa = 0

        else:
            if self.popup3.currentText() == u"(연강)":
                if self.popup4.currentText() == u"(연강)":
                    q_MPa = 1.0*9.81

                elif self.popup4.currentText() == u"(청동)":
                    q_MPa = 1.0*9.81

                else:
                    q_MPa = 0

            elif self.popup3.currentText() == u"(경강)":
                if self.popup4.currentText() == u"(경강)":
                    q_MPa = 1.3*9.81

                elif self.popup4.currentText() == u"(청동)":
                    q_MPa = 1.3*9.81

                else:
                    q_MPa = 0

            elif self.popup3.currentText() == u"(강)":
                if self.popup4.currentText() == u"(주철)":
                    q_MPa = 0.5*9.81
                else:
                    q_MPa = 0

        Z = Q_Newton * 4 / (math.pi * q_MPa * ( do_mm * do_mm - di_mm * di_mm))
        H_mm = Z * SF * p_mm

        if self.popup11.currentText() == u"(mm)":            # 최소 너트 높이
            self.numericInput11.setText(str(round(H_mm,3)))
        elif self.popup11.currentText() == u"(inch)":
            H_inch = 1 / 25.4 * H_mm
            self.numericInput11.setText(str(round(H_inch,3)))
        self.numericInput12.setText(str(round(Z,3)))         # 나사산의 개수
        if self.popup13.currentText() == u"(MPa)":           # 허용면압력
            self.numericInput13.setText(str(round(q_MPa,3)))
        elif self.popup13.currentText() == u"(ksi)":
            q_ksi = 1 / 6.89475908677537 * q_MPa
            self.numericInput13.setText(str(round(q_ksi,3)))


    def onGenerate1(self):
        if self.popup6.currentText() == u"(mm)":       # 바깥 지름 단위 설정 (inch -> mm)
            d_mm = float(self.numericInput6.text())
        elif self.popup6.currentText() == u"(inch)":
            d_inch = float(self.numericInput6.text())
            d_mm = d_inch * 25.4
        if self.popup7.currentText() == u"(mm)":       # 볼트 길이 단위 설정 (inch -> mm)
            D_mm = float(self.numericInput7.text())
        elif self.popup7.currentText() == u"(inch)":
            D_inch = float(self.numericInput7.text())
            D_mm = D_inch * 25.4

        doc = App.newDocument()
        # 기본형상 hexagon, circle
        s_hex = d_mm * 1.7  #hexagon_diameter
        cir_hex = d_mm      #circle_diameter
        k_hex = D_mm / 5    #height

        mhex = Base.Matrix()
        mhex.rotateZ(math.radians(60.0))
        polygon = []
        vhex = Base.Vector(s_hex / math.sqrt(3.0), 0.0, -k_hex)
        for i in range(6):
            polygon.append(vhex)
            vhex = mhex.multiply(vhex)
        polygon.append(vhex)
        hexagon = Part.makePolygon(polygon)
        face = Part.Face(hexagon)
        exHex = face.extrude(Base.Vector(0.0, 0.0, k_hex))  #높이
        circ = Part.makeCylinder(cir_hex / 2.0, D_mm, Vector(0, 0, 0))
        exHex = exHex.fuse(circ)

        # 나사선 helix
        helix = Part.makeHelix(d_mm / 5, D_mm, d_mm)  #Part.makeHelix(pitch,height,radius,(angle))
        #사다리꼴 단면
        edge1 = Part.makeLine(
            (d_mm * 6 / 5 / 2, 0, -d_mm * 4 / 5 / 2 / 16), (d_mm * 6 / 5 / 2, 0, d_mm * 4 / 5 / 2 / 16))
        edge2 = Part.makeLine(
            (d_mm * 6 / 5 / 2, 0, d_mm * 4 / 5 / 2 / 16), (d_mm * 4 / 5 / 2, 0, d_mm * 4 / 5 / 2 / 5))
        edge3 = Part.makeLine(
            (d_mm * 4 / 5 / 2, 0, d_mm * 4 / 5 / 2 / 5), (d_mm * 4 / 5 / 2, 0, -d_mm * 4 / 5 / 2 / 5))
        edge4 = Part.makeLine(
            (d_mm * 4 / 5 / 2, 0, -d_mm * 4 / 5 / 2 / 5), (d_mm * 6 / 5 / 2, 0, -d_mm * 4 / 5 / 2 / 16))
        section = Part.Wire([edge4, edge1, edge2, edge3])
        makeSolid = bool(1)  #change to 1 to make a solid, but it will take a while
        isFrenet = bool(1)
        pipe = Part.Wire(helix).makePipeShell([section], makeSolid, isFrenet)
        exHex = exHex.fuse(pipe)
        shape = doc.addObject("Part::Feature")  #Color
        shape.Shape = exHex  #Color
        doc.recompute()  #Color
        shape.ViewObject.ShapeColor = (1.0, 1.0, 1.0)  #Color
        Gui.activeDocument().activeView().viewAxometric()  #View
        Gui.SendMsgToActiveView("ViewFit")  #View


    def onGenerate2(self):
        if self.popup6.currentText() == u"(mm)":       # 바깥 지름 단위 설정 (inch -> mm)
            d_mm = float(self.numericInput6.text())
        elif self.popup6.currentText() == u"(inch)":
            d_inch = float(self.numericInput6.text())
            d_mm = d_inch * 25.4
        if self.popup7.currentText() == u"(mm)":       # 볼트 길이 단위 설정 (inch -> mm)
            D_mm = float(self.numericInput7.text())
        elif self.popup7.currentText() == u"(inch)":
            D_inch = float(self.numericInput7.text())
            D_mm = D_inch * 25.4

        doc = App.newDocument()
        # 기본형상 hexagon, circle
        s_hex = d_mm * 1.7  #hexagon_diameter
        cir_hex = d_mm      #circle_diameter
        k_hex = D_mm / 5    #height

        exHex = Part.makeBox(d_mm * 1.7, d_mm * 1.7, D_mm / 7, Vector(-d_mm * 1.7 / 2, -d_mm * 1.7 / 2, -D_mm / 7))
        circ = Part.makeCylinder(cir_hex / 2.0, D_mm, Vector(0, 0, 0))
        exHex = exHex.fuse(circ)

        # 나사선 helix
        helix = Part.makeHelix(d_mm / 5, D_mm, d_mm)  #Part.makeHelix(pitch,height,radius,(angle))
        #사다리꼴 단면
        edge1 = Part.makeLine((d_mm * 6 / 5 / 2, 0, -d_mm * 4 / 5 / 2 / 16), (d_mm * 6 / 5 / 2, 0, d_mm * 4 / 5 / 2 / 16))
        edge2 = Part.makeLine((d_mm * 6 / 5 / 2, 0, d_mm * 4 / 5 / 2 / 16), (d_mm * 4 / 5 / 2, 0, d_mm * 4 / 5 / 2 / 5))
        edge3 = Part.makeLine((d_mm * 4 / 5 / 2, 0, d_mm * 4 / 5 / 2 / 5), (d_mm * 4 / 5 / 2, 0, -d_mm * 4 / 5 / 2 / 5))
        edge4 = Part.makeLine((d_mm * 4 / 5 / 2, 0, -d_mm * 4 / 5 / 2 / 5), (d_mm * 6 / 5 / 2, 0, -d_mm * 4 / 5 / 2 / 16))
        section = Part.Wire([edge1, edge2, edge3, edge4])
        makeSolid = bool(1)
        isFrenet = bool(1)
        pipe = Part.Wire(helix).makePipeShell([section], makeSolid, isFrenet)

        exHex = exHex.fuse(pipe)

        shape = doc.addObject("Part::Feature")  #Color
        shape.Shape = exHex  #Color
        doc.recompute()  #Color
        shape.ViewObject.ShapeColor = (1.0, 1.0, 1.0)  #Color
        Gui.activeDocument().activeView().viewAxometric()  #View
        Gui.SendMsgToActiveView("ViewFit")  #View

    def onGenerate3(self):
        doc = App.newDocument()
        if self.popup7.currentText() == u"(mm)":          # 바깥 지름 * 1.7 (mm로 변환)
            s_hex = 1.7 * float(self.numericInput7.text())
            do_mm = float(self.numericInput7.text())
        elif self.popup7.currentText() == u"(inch)":
            s_hex = 2.54 * 1.7 * float(self.numericInput7.text())
            do_mm = 2.54 * float(self.numericInput7.text())
        if self.popup8.currentText() == u"(mm)":          # 안 지름 (mm로 변환)
            cir_hex = float(self.numericInput8.text())
        elif self.popup8.currentText() == u"(inch)":
            cir_hex = 2.54 * float(self.numericInput8.text())
        if self.popup14.currentText() == u"(mm)":          # 너트 높이 (mm로 변환)
            h_mm = float(self.numericInput14.text())
        elif self.popup14.currentText() == u"(inch)":
            h_mm = 2.54 * float(self.numericInput14.text())

        mhex = Base.Matrix()
        mhex.rotateZ(math.radians(60.0))
        polygon = []
        vhex = Base.Vector(s_hex/math.sqrt(3.0),0.0,0.0)
        for i in range(6):
           polygon.append(vhex)
           vhex = mhex.multiply(vhex)
        polygon.append(vhex)
        hexagon = Part.makePolygon(polygon)
        circ = Part.makeCircle(cir_hex/2.0)
        face = Part.Face([hexagon, Part.Wire(circ)])
        exhex = face.extrude(Base.Vector(0.0,0.0,h_mm))

        # 나사선 helix
        helix = Part.makeHelix(cir_hex / 5, h_mm, cir_hex)  #Part.makeHelix(pitch,height,radius,(angle))
        #사다리꼴 단면
        edge1 = Part.makeLine((cir_hex * 6 / 5 / 2, 0, -cir_hex * 4 / 5 / 2 / 16), (cir_hex * 6 / 5 / 2, 0, cir_hex * 4 / 5 / 2 / 16))
        edge2 = Part.makeLine((cir_hex * 6 / 5 / 2, 0, cir_hex * 4 / 5 / 2 / 16), (cir_hex * 4 / 5 / 2, 0, cir_hex * 4 / 5 / 2 / 5))
        edge3 = Part.makeLine((cir_hex * 4 / 5 / 2, 0, cir_hex * 4 / 5 / 2 / 5), (cir_hex * 4 / 5 / 2, 0, -cir_hex * 4 / 5 / 2 / 5))
        edge4 = Part.makeLine((cir_hex * 4 / 5 / 2, 0, -cir_hex * 4 / 5 / 2 / 5), (cir_hex * 6 / 5 / 2, 0, -cir_hex * 4 / 5 / 2 / 16))
        section = Part.Wire([edge1, edge2, edge3, edge4])
        makeSolid = bool(1)
        isFrenet = bool(1)
        pipe = Part.Wire(helix).makePipeShell([section], makeSolid, isFrenet)

        exhex = exhex.cut(pipe)

        shape = doc.addObject("Part::Feature")  #Color
        shape.Shape = exhex  #Color
        doc.recompute()  #Color
        shape.ViewObject.ShapeColor = (1.0, 1.0, 1.0)  #Color
        Gui.activeDocument().activeView().viewAxometric()  #View
        Gui.SendMsgToActiveView("ViewFit")  #View

    def onGenerate4(self):
        doc = App.newDocument()
        if self.popup7.currentText() == u"(mm)":          # 바깥 지름 (mm로 변환)
            do_mm = float(self.numericInput7.text())
        elif self.popup7.currentText() == u"(inch)":
            do_mm = 2.54 * float(self.numericInput7.text())
        if self.popup8.currentText() == u"(mm)":          # 안 지름 (mm로 변환)
            di_mm = float(self.numericInput8.text())
        elif self.popup8.currentText() == u"(inch)":
            di_mm = 2.54 * float(self.numericInput8.text())
        if self.popup14.currentText() == u"(mm)":         # 너트 높이 (mm로 변환)
            h_mm = float(self.numericInput14.text())
        elif self.popup14.currentText() == u"(inch)":
            h_mm = 2.54 * float(self.numericInput14.text())

        exhex = Part.makeBox(do_mm * 1.7, do_mm * 1.7, h_mm, Vector(-do_mm * 1.7 / 2, -do_mm * 1.7 / 2, 0))
        ccc = Part.makeCylinder(di_mm/2, h_mm, Vector(0,0,0))
        exhex = exhex.cut(ccc)

        # 나사선 helix
        helix = Part.makeHelix(di_mm / 5, h_mm, di_mm)  #Part.makeHelix(pitch,height,radius,(angle))
        #사다리꼴 단면
        edge1 = Part.makeLine((di_mm * 6 / 5 / 2, 0, -di_mm * 4 / 5 / 2 / 16), (di_mm * 6 / 5 / 2, 0, di_mm * 4 / 5 / 2 / 16))
        edge2 = Part.makeLine((di_mm * 6 / 5 / 2, 0, di_mm * 4 / 5 / 2 / 16), (di_mm * 4 / 5 / 2, 0, di_mm * 4 / 5 / 2 / 5))
        edge3 = Part.makeLine((di_mm * 4 / 5 / 2, 0, di_mm * 4 / 5 / 2 / 5), (di_mm * 4 / 5 / 2, 0, -di_mm * 4 / 5 / 2 / 5))
        edge4 = Part.makeLine((di_mm * 4 / 5 / 2, 0, -di_mm * 4 / 5 / 2 / 5), (di_mm * 6 / 5 / 2, 0, -di_mm * 4 / 5 / 2 / 16))
        section = Part.Wire([edge1, edge2, edge3, edge4])
        makeSolid = bool(1)
        isFrenet = bool(1)
        pipe = Part.Wire(helix).makePipeShell([section], makeSolid, isFrenet)

        exhex = exhex.cut(pipe)

        shape = doc.addObject("Part::Feature")  #Color
        shape.Shape = exhex  #Color
        doc.recompute()  #Color
        shape.ViewObject.ShapeColor = (1.0, 1.0, 1.0)  #Color
        Gui.activeDocument().activeView().viewAxometric()  #View
        Gui.SendMsgToActiveView("ViewFit")  #View


    def onQuit(self):
        #self.quitButton.clicked.connect(self.close())
        self.close()


ex = Sci()
#ex.show()  #ED-PyCharm
#sys.exit(app.exec_())  #ED-PyCharm
