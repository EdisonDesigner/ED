
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
        self.treeWidget.setHeaderLabels([u"            전동용 기계부품"])  # headerlabel명
        self.treeWidget.setColumnCount(1)  # headerlabel 칼럼 갯수

        root1 = QtGui.QTreeWidgetItem(self.treeWidget)
        root1.setText(0, u'직전전동')
        child1 = QtGui.QTreeWidgetItem(root1)
        child1.setText(0, u'마찰자')
        child2 = QtGui.QTreeWidgetItem(root1)
        child2.setText(0, u'스퍼기어')
        child3 = QtGui.QTreeWidgetItem(root1)
        child3.setText(0, u'캠')
        self.treeWidget.addTopLevelItem(root1)

        root2 = QtGui.QTreeWidgetItem(self.treeWidget)
        root2.setText(0, u'간접전동')
        child1 = QtGui.QTreeWidgetItem(root2)
        child1.setText(0, u'평벨트')
        child2 = QtGui.QTreeWidgetItem(root2)
        child2.setText(0, u'체인')
        child3 = QtGui.QTreeWidgetItem(root2)
        child3.setText(0, u'로프')
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
        self.group7 = QtGui.QGroupBox(self)
        self.group7.setGeometry(220, 10, 770, 780)
        self.group7.hide()

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
        self.setWindowTitle(u"전동용 기계부품 설계 SW")
        self.show()

    def clickedItem(self, parent):
        if self.treeWidget.currentItem().text(0) == u"마찰자":
            self.group2.hide()
            self.group3.hide()
            self.group4.hide()
            self.group5.hide()
            self.group6.hide()
            self.group7.hide()

            self.label1 = QtGui.QLabel(u"마찰자 ()의 설계", self.group1)
            self.label1.setFont('Courier')
            self.label1.setStyleSheet("font: bold; font-size: 12pt;")
            self.label1.move(270, 10)
            self.label1.setAlignment(QtCore.Qt.AlignRight)

            self.group1.show()

        elif self.treeWidget.currentItem().text(0) == u"스퍼기어":
            self.group1.hide()
            self.group3.hide()
            self.group4.hide()
            self.group5.hide()
            self.group6.hide()
            self.group7.hide()

            self.label1 = QtGui.QLabel(u"스퍼기어 (Spur Gear)의 설계", self.group2)
            self.label1.setFont('Courier')
            self.label1.setStyleSheet("font: bold; font-size: 12pt;")
            self.label1.move(270, 10)
            self.label1.setAlignment(QtCore.Qt.AlignRight)

            # Power group
            self.powergroup = QtGui.QGroupBox(self.group2)
            self.powergroup.setGeometry(QtCore.QRect(30,70,340,145))
            self.powergroup.setTitle(u"재질 설정")
            self.powergroup.setStyleSheet("font-size: 10pt;")
            self.powergroup.setFont('Courier')

            self.label1 = QtGui.QLabel(u"기어 경도", self.powergroup)
            self.label1.move(40,40)
            self.numericInput1 = QtGui.QLineEdit(self.powergroup)
            self.numericInput1.setFixedWidth(50)
            self.numericInput1.move(170, 35)
            self.popupItems1 = (u"(브리넬 경도)", u"( )")
            self.popup1 = QtGui.QComboBox(self.powergroup)
            self.popup1.addItems(self.popupItems1)
            self.popup1.setCurrentIndex(self.popupItems1.index(u"(브리넬 경도)"))
            self.popup1.move(230, 35)
            self.label2 = QtGui.QLabel(u"피니언 경도", self.powergroup)
            self.label2.move(40,65)
            self.numericInput2 = QtGui.QLineEdit(self.powergroup)
            self.numericInput2.setFixedWidth(50)
            self.numericInput2.move(170, 60)
            self.popupItems2 = (u"(브리넬 경도)", u"( )")
            self.popup2 = QtGui.QComboBox(self.powergroup)
            self.popup2.addItems(self.popupItems2)
            self.popup2.setCurrentIndex(self.popupItems2.index(u"(브리넬 경도)"))
            self.popup2.move(230, 60)
            self.tableButton = QtGui.QPushButton(u"기어 재료의 기계적 성질", self.powergroup)
            self.tableButton.clicked.connect(self.onTable2_1)
            self.tableButton.setFixedWidth(180)
            self.tableButton.setAutoDefault(True)
            self.tableButton.move(90,90)
            self.label3 = QtGui.QLabel(u"*면압 강도를 이용한 기어 설계, 압력각 20 degree*", self.powergroup)
            self.label3.move(20, 120)
            self.label3.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환

            # Variable group
            self.varigroup = QtGui.QGroupBox(self.group2)
            self.varigroup.setGeometry(QtCore.QRect(30,225,340,255))
            self.varigroup.setTitle(u"설계 변수")
            self.varigroup.setStyleSheet("font-size: 10pt;")
            self.varigroup.setFont('Courier')

            self.label4 = QtGui.QLabel(u"모듈", self.varigroup)
            self.label4.move(40, 40)
            self.label4.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.numericInput4 = QtGui.QLineEdit(self.varigroup)
            self.numericInput4.setFixedWidth(50)
            self.numericInput4.move(170, 35)
            self.tableButton = QtGui.QPushButton(u"모듈의 표준 값", self.varigroup)
            self.tableButton.clicked.connect(self.onTable2_2)
            self.tableButton.setFixedWidth(180)
            self.tableButton.setAutoDefault(True)
            self.tableButton.move(90,60)
            self.label5 = QtGui.QLabel(u"기어의 잇수", self.varigroup)
            self.label5.move(40, 95)
            self.label5.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.numericInput5 = QtGui.QLineEdit(self.varigroup)
            self.numericInput5.setFixedWidth(50)
            self.numericInput5.move(170, 90)
            self.label6 = QtGui.QLabel(u"피니언의 잇수", self.varigroup)
            self.label6.move(40, 120)
            self.label6.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.numericInput6 = QtGui.QLineEdit(self.varigroup)
            self.numericInput6.setFixedWidth(50)
            self.numericInput6.move(170, 115)
            self.tableButton = QtGui.QPushButton(u"기어 잇수와 치형계수", self.varigroup)
            self.tableButton.clicked.connect(self.onTable2_3)
            self.tableButton.setFixedWidth(180)
            self.tableButton.setAutoDefault(True)
            self.tableButton.move(90,140)
            self.label7 = QtGui.QLabel(u"기어의 회전 속력", self.varigroup)
            self.label7.move(40, 175)
            self.numericInput7 = QtGui.QLineEdit(self.varigroup)
            self.numericInput7.setFixedWidth(50)
            self.numericInput7.move(170, 170)
            self.popupItems7 = (u"(rpm)", u"(rad/s)")
            self.popup7 = QtGui.QComboBox(self.varigroup)
            self.popup7.addItems(self.popupItems7)
            self.popup7.setCurrentIndex(self.popupItems7.index(u"(rpm)"))
            self.popup7.move(230, 170)
            self.label8 = QtGui.QLabel(u"전달 동력", self.varigroup)
            self.label8.move(40, 200)
            self.numericInput8 = QtGui.QLineEdit(self.varigroup)
            self.numericInput8.setFixedWidth(50)
            self.numericInput8.move(170, 195)
            self.popupItems8 = (u"(kW)", u"(HP)")
            self.popup8 = QtGui.QComboBox(self.varigroup)
            self.popup8.addItems(self.popupItems8)
            self.popup8.setCurrentIndex(self.popupItems8.index(u"(kW)"))
            self.popup8.move(230, 195)
            self.designButton = QtGui.QPushButton("Design", self.varigroup)
            self.designButton.clicked.connect(self.onDesign2)
            self.designButton.setFixedWidth(180)
            self.designButton.setAutoDefault(True)
            self.designButton.move(90, 220)

            # Result group
            self.resultgroup = QtGui.QGroupBox(self.group2)
            self.resultgroup.setGeometry(QtCore.QRect(30,490,340,140))
            self.resultgroup.setTitle(u"계산 결과")
            self.resultgroup.setStyleSheet("font-size: 10pt;")
            self.resultgroup.setFont('Courier')

            self.label9 = QtGui.QLabel(u"이에 작용하는 힘", self.resultgroup)
            self.label9.move(40, 40)
            self.numericInput9 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput9.setFixedWidth(50)
            self.numericInput9.move(170, 35)
            self.popupItems9 = (u"(N)", u"(lbf)")
            self.popup9 = QtGui.QComboBox(self.resultgroup)
            self.popup9.addItems(self.popupItems9)
            self.popup9.setCurrentIndex(self.popupItems9.index(u"(N)"))
            self.popup9.move(230, 35)
            self.label10 = QtGui.QLabel(u"허용 압축 응력", self.resultgroup)
            self.label10.move(40, 65)
            self.numericInput10 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput10.setFixedWidth(50)
            self.numericInput10.move(170, 60)
            self.popupItems10 = (u"(MPa)", u"(ksi)")
            self.popup10 = QtGui.QComboBox(self.resultgroup)
            self.popup10.addItems(self.popupItems10)
            self.popup10.setCurrentIndex(self.popupItems10.index(u"(MPa)"))
            self.popup10.move(230, 60)
            self.label11 = QtGui.QLabel(u"기어 중심 사이 거리", self.resultgroup)
            self.label11.move(40, 90)
            self.numericInput11 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput11.setFixedWidth(50)
            self.numericInput11.move(170, 85)
            self.popupItems11 = (u"(mm)", u"(inch)")
            self.popup11 = QtGui.QComboBox(self.resultgroup)
            self.popup11.addItems(self.popupItems11)
            self.popup11.setCurrentIndex(self.popupItems11.index(u"(mm)"))
            self.popup11.move(230, 85)
            self.label12 = QtGui.QLabel(u"최소 필요 기어 두께", self.resultgroup)
            self.label12.move(40, 115)
            self.numericInput12 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput12.setFixedWidth(50)
            self.numericInput12.move(170, 110)
            self.popupItems12 = (u"(mm)", u"(inch)")
            self.popup12 = QtGui.QComboBox(self.resultgroup)
            self.popup12.addItems(self.popupItems12)
            self.popup12.setCurrentIndex(self.popupItems12.index(u"(mm)"))
            self.popup12.move(230, 110)


            # Modling group
            self.modelinggroup = QtGui.QGroupBox(self.group2)
            self.modelinggroup.setGeometry(QtCore.QRect(30,640,340,135))
            self.modelinggroup.setTitle(u"모델링")
            self.modelinggroup.setStyleSheet("font-size: 10pt;")
            self.modelinggroup.setFont('Courier')

            self.label13 = QtGui.QLabel(u"기어 두께", self.modelinggroup)
            self.label13.move(40, 40)
            self.label13.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.numericInput13 = QtGui.QLineEdit(self.modelinggroup)
            self.numericInput13.setFixedWidth(50)
            self.numericInput13.move(170, 35)
            self.popupItems13 = (u"(mm)", u"(inch)")
            self.popup13 = QtGui.QComboBox(self.modelinggroup)
            self.popup13.addItems(self.popupItems13)
            self.popup13.setCurrentIndex(self.popupItems13.index(u"(mm)"))
            self.popup13.move(230, 35)
            self.label14 = QtGui.QLabel(u"축 지름", self.modelinggroup)
            self.label14.move(40, 65)
            self.label14.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.numericInput14 = QtGui.QLineEdit(self.modelinggroup)
            self.numericInput14.setFixedWidth(50)
            self.numericInput14.move(170, 60)
            self.popupItems14 = (u"(mm)", u"(inch)")
            self.popup14 = QtGui.QComboBox(self.modelinggroup)
            self.popup14.addItems(self.popupItems14)
            self.popup14.setCurrentIndex(self.popupItems14.index(u"(mm)"))
            self.popup14.move(230, 60)
            self.label15 = QtGui.QLabel(u"*붉은 색 파라미터를 이용하여 모델링함*", self.modelinggroup)
            self.label15.move(50, 90)
            self.label15.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.generateButton = QtGui.QPushButton("Generate", self.modelinggroup)
            self.generateButton.clicked.connect(self.onGenerate2)
            self.generateButton.setFixedWidth(180)
            self.generateButton.setAutoDefault(True)
            self.generateButton.move(90, 110)

            # Pictures 1
            self.refer_Img_GroupBox = QtGui.QGroupBox(self.group2)
            self.refer_Img_GroupBox.setGeometry(QtCore.QRect(380, 70, 370, 270))
            self.refer_Img_GroupBox.setTitle(u"스퍼기어(Spur Gear)")
            self.refer_Img_GroupBox.setStyleSheet("font-size: 10pt;")
            self.refer_Img_GroupBox.setFont('Courier')

            self.side_View_Img = QtGui.QPixmap(os.path.join(addonPath, "transmission_module/Spur_Gear_Model.jpg"))
            self.side_View_label = QtGui.QLabel(self.refer_Img_GroupBox)
            self.side_View_label.setPixmap(self.side_View_Img)
            self.side_View_label.resize(self.side_View_Img.width(), self.side_View_Img.height())
            self.side_View_label.move(45, 30)

            self.refer_Img_GroupBox1 = QtGui.QGroupBox(self.group2)
            self.refer_Img_GroupBox1.setGeometry(QtCore.QRect(380, 350, 370, 400))
            self.refer_Img_GroupBox1.setTitle(u"계산 공식")
            self.refer_Img_GroupBox1.setStyleSheet("font-size: 10pt;")
            self.refer_Img_GroupBox1.setFont('Courier')

            self.side_View_Img1 = QtGui.QPixmap(os.path.join(addonPath, "transmission_module/Spur_Gear_Calculation.jpg"))
            self.side_View_label1 = QtGui.QLabel(self.refer_Img_GroupBox1)
            self.side_View_label1.setPixmap(self.side_View_Img1)
            self.side_View_label1.resize(self.side_View_Img1.width(), self.side_View_Img1.height())
            self.side_View_label1.move(10, 30)

            self.group2.show()

        elif self.treeWidget.currentItem().text(0) == u"캠":
            self.group1.hide()
            self.group2.hide()
            self.group3.hide()
            self.group5.hide()
            self.group6.hide()
            self.group7.hide()

            self.label1 = QtGui.QLabel(u"캠 ()의 설계", self.group4)
            self.label1.setFont('Courier')
            self.label1.setStyleSheet("font: bold; font-size: 12pt;")
            self.label1.move(270, 10)
            self.label1.setAlignment(QtCore.Qt.AlignRight)

            self.group4.show()

        elif self.treeWidget.currentItem().text(0) == u"평벨트":
            self.group1.hide()
            self.group2.hide()
            self.group3.hide()
            self.group4.hide()
            self.group6.hide()
            self.group7.hide()

            self.label1 = QtGui.QLabel(u"평벨트(Flat Belt)의 설계", self.group5)
            self.label1.setFont('Courier')
            self.label1.setStyleSheet("font: bold; font-size: 12pt;")
            self.label1.move(270, 10)
            self.label1.setAlignment(QtCore.Qt.AlignRight)

            # Power group
            self.powergroup = QtGui.QGroupBox(self.group5)
            self.powergroup.setGeometry(QtCore.QRect(30,70,340,90))
            self.powergroup.setTitle(u"재질 설정")
            self.powergroup.setStyleSheet("font-size: 10pt;")
            self.powergroup.setFont('Courier')

            self.label1 = QtGui.QLabel(u"벨트의 재료", self.powergroup)
            self.label1.move(40,40)
            self.popupItems1 = (u"(가죽)", u"(고무)")
            self.popup1 = QtGui.QComboBox(self.powergroup)
            self.popup1.addItems(self.popupItems1)
            self.popup1.setCurrentIndex(self.popupItems1.index(u"(가죽)"))
            self.popup1.move(230, 35)
            self.label2 = QtGui.QLabel(u"풀리의 재료", self.powergroup)
            self.label2.move(40,65)
            self.popupItems2 = (u"(철제)", u"( ) ")
            self.popup2 = QtGui.QComboBox(self.powergroup)
            self.popup2.addItems(self.popupItems2)
            self.popup2.setCurrentIndex(self.popupItems2.index(u"(철제)"))
            self.popup2.move(230, 60)

            # Power group
            self.varigroup = QtGui.QGroupBox(self.group5)
            self.varigroup.setGeometry(QtCore.QRect(30,170,340,285))
            self.varigroup.setTitle(u"설계 변수")
            self.varigroup.setStyleSheet("font-size: 10pt;")
            self.varigroup.setFont('Courier')

            self.label3 = QtGui.QLabel(u"벨트 폭", self.varigroup)
            self.label3.move(40, 40)
            self.label3.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.numericInput3 = QtGui.QLineEdit(self.varigroup)
            self.numericInput3.setFixedWidth(50)
            self.numericInput3.move(170, 35)
            self.popupItems3 = (u"(mm)", u"(inch)")
            self.popup3 = QtGui.QComboBox(self.varigroup)
            self.popup3.addItems(self.popupItems3)
            self.popup3.setCurrentIndex(self.popupItems3.index(u"(mm)"))
            self.popup3.move(230, 35)
            self.label4 = QtGui.QLabel(u"벨트 높이", self.varigroup)
            self.label4.move(40, 65)
            self.label4.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.numericInput4 = QtGui.QLineEdit(self.varigroup)
            self.numericInput4.setFixedWidth(50)
            self.numericInput4.move(170, 60)
            self.popupItems4 = (u"(mm)", u"(inch)")
            self.popup4 = QtGui.QComboBox(self.varigroup)
            self.popup4.addItems(self.popupItems4)
            self.popup4.setCurrentIndex(self.popupItems4.index(u"(mm)"))
            self.popup4.move(230, 60)
            self.tableButton = QtGui.QPushButton(u"벨트의 규격 Table", self.varigroup)
            self.tableButton.clicked.connect(self.onTable5_1)
            self.tableButton.setFixedWidth(180)
            self.tableButton.setAutoDefault(True)
            self.tableButton.move(90,90)
            self.label5 = QtGui.QLabel(u"큰 풀리 지름", self.varigroup)
            self.label5.move(40, 125)
            self.label5.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.numericInput5 = QtGui.QLineEdit(self.varigroup)
            self.numericInput5.setFixedWidth(50)
            self.numericInput5.move(170, 120)
            self.popupItems5 = (u"(mm)", u"(inch)")
            self.popup5 = QtGui.QComboBox(self.varigroup)
            self.popup5.addItems(self.popupItems5)
            self.popup5.setCurrentIndex(self.popupItems5.index(u"(mm)"))
            self.popup5.move(230, 120)
            self.label16 = QtGui.QLabel(u"두 풀리 사이 거리", self.varigroup)
            self.label16.move(40, 150)
            self.label16.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.numericInput16 = QtGui.QLineEdit(self.varigroup)
            self.numericInput16.setFixedWidth(50)
            self.numericInput16.move(170, 145)
            self.popupItems16 = (u"(mm)", u"(inch)")
            self.popup16 = QtGui.QComboBox(self.varigroup)
            self.popup16.addItems(self.popupItems16)
            self.popup16.setCurrentIndex(self.popupItems16.index(u"(mm)"))
            self.popup16.move(230, 145)
            self.label6 = QtGui.QLabel(u"전달 동력", self.varigroup)
            self.label6.move(40, 175)
            self.numericInput6 = QtGui.QLineEdit(self.varigroup)
            self.numericInput6.setFixedWidth(50)
            self.numericInput6.move(170, 170)
            self.popupItems6 = (u"(kW)", u"(HP)")
            self.popup6 = QtGui.QComboBox(self.varigroup)
            self.popup6.addItems(self.popupItems6)
            self.popup6.setCurrentIndex(self.popupItems6.index(u"(kW)"))
            self.popup6.move(230, 170)
            self.label7 = QtGui.QLabel(u"회전 속력", self.varigroup)
            self.label7.move(40, 200)
            self.numericInput7 = QtGui.QLineEdit(self.varigroup)
            self.numericInput7.setFixedWidth(50)
            self.numericInput7.move(170, 195)
            self.popupItems7 = (u"(rpm)", u"(rad/s)")
            self.popup7 = QtGui.QComboBox(self.varigroup)
            self.popup7.addItems(self.popupItems7)
            self.popup7.setCurrentIndex(self.popupItems7.index(u"(rpm)"))
            self.popup7.move(230, 195)
            self.label8 = QtGui.QLabel(u"감속비", self.varigroup)
            self.label8.move(40, 225)
            self.numericInput8 = QtGui.QLineEdit(self.varigroup)
            self.numericInput8.setFixedWidth(50)
            self.numericInput8.move(170, 220)
            self.designButton = QtGui.QPushButton("Design", self.varigroup)
            self.designButton.clicked.connect(self.onDesign5)
            self.designButton.setFixedWidth(180)
            self.designButton.setAutoDefault(True)
            self.designButton.move(90, 255)

            # Result group
            self.resultgroup = QtGui.QGroupBox(self.group5)
            self.resultgroup.setGeometry(QtCore.QRect(30,465,340,165))
            self.resultgroup.setTitle(u"계산 결과")
            self.resultgroup.setStyleSheet("font-size: 10pt;")
            self.resultgroup.setFont('Courier')

            self.label9 = QtGui.QLabel(u"작은 풀리 최소 지름", self.resultgroup)
            self.label9.move(40, 40)
            self.label9.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.numericInput9 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput9.setFixedWidth(50)
            self.numericInput9.move(170, 35)
            self.popupItems9 = (u"(mm)", u"(inch)")
            self.popup9 = QtGui.QComboBox(self.resultgroup)
            self.popup9.addItems(self.popupItems9)
            self.popup9.setCurrentIndex(self.popupItems9.index(u"(mm)"))
            self.popup9.move(230, 35)
            self.label10 = QtGui.QLabel(u"벨트의 길이", self.resultgroup)
            self.label10.move(40, 65)
            self.numericInput10 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput10.setFixedWidth(50)
            self.numericInput10.move(170, 60)
            self.popupItems10 = (u"(mm)", u"(inch)")
            self.popup10 = QtGui.QComboBox(self.resultgroup)
            self.popup10.addItems(self.popupItems10)
            self.popup10.setCurrentIndex(self.popupItems10.index(u"(mm)"))
            self.popup10.move(230, 60)
            self.label11 = QtGui.QLabel(u"벨트의 속력", self.resultgroup)
            self.label11.move(40, 90)
            self.numericInput11 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput11.setFixedWidth(50)
            self.numericInput11.move(170, 85)
            self.popupItems11 = (u"(m/s)", u"(fps)")
            self.popup11 = QtGui.QComboBox(self.resultgroup)
            self.popup11.addItems(self.popupItems11)
            self.popup11.setCurrentIndex(self.popupItems11.index(u"(m/s)"))
            self.popup11.move(230, 85)
            self.label12 = QtGui.QLabel(u"벨트의 최소 유효장력", self.resultgroup)
            self.label12.move(40, 115)
            self.numericInput12 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput12.setFixedWidth(50)
            self.numericInput12.move(170, 110)
            self.popupItems12 = (u"(Newton)", u"(lbf)")
            self.popup12 = QtGui.QComboBox(self.resultgroup)
            self.popup12.addItems(self.popupItems12)
            self.popup12.setCurrentIndex(self.popupItems12.index(u"(Newton)"))
            self.popup12.move(230, 110)
            self.label13 = QtGui.QLabel(u"벨트의 인장강도", self.resultgroup)
            self.label13.move(40, 140)
            self.numericInput13 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput13.setFixedWidth(50)
            self.numericInput13.move(170, 135)
            self.popupItems13 = (u"(MPa)", u"(ksi)")
            self.popup13 = QtGui.QComboBox(self.resultgroup)
            self.popup13.addItems(self.popupItems13)
            self.popup13.setCurrentIndex(self.popupItems13.index(u"(MPa)"))
            self.popup13.move(230, 135)

            # Modling group
            self.modelinggroup = QtGui.QGroupBox(self.group5)
            self.modelinggroup.setGeometry(QtCore.QRect(30,640,340,130))
            self.modelinggroup.setTitle(u"모델링")
            self.modelinggroup.setStyleSheet("font-size: 10pt;")
            self.modelinggroup.setFont('Courier')

            self.label14 = QtGui.QLabel(u"축의 지름", self.modelinggroup)
            self.label14.move(40, 40)
            self.label14.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.numericInput14 = QtGui.QLineEdit(self.modelinggroup)
            self.numericInput14.setFixedWidth(50)
            self.numericInput14.move(170, 35)
            self.popupItems14 = (u"(mm)", u"(inch)")
            self.popup14 = QtGui.QComboBox(self.modelinggroup)
            self.popup14.addItems(self.popupItems14)
            self.popup14.setCurrentIndex(self.popupItems14.index(u"(mm)"))
            self.popup14.move(230, 35)
            self.label15 = QtGui.QLabel(u"*붉은 색 파라미터를 이용하여 모델링함*", self.modelinggroup)
            self.label15.move(50, 65)
            self.label15.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.generateButton = QtGui.QPushButton("Generate", self.modelinggroup)
            self.generateButton.clicked.connect(self.onGenerate5)
            self.generateButton.setFixedWidth(180)
            self.generateButton.setAutoDefault(True)
            self.generateButton.move(90, 95)

            # Pictures 1
            self.refer_Img_GroupBox = QtGui.QGroupBox(self.group5)
            self.refer_Img_GroupBox.setGeometry(QtCore.QRect(380, 70, 370, 270))
            self.refer_Img_GroupBox.setTitle(u"평밸트(Flat Belt)")
            self.refer_Img_GroupBox.setStyleSheet("font-size: 10pt;")
            self.refer_Img_GroupBox.setFont('Courier')

            self.side_View_Img = QtGui.QPixmap(os.path.join(addonPath, "transmission_module/Flat_Belt_Model.jpg"))
            self.side_View_label = QtGui.QLabel(self.refer_Img_GroupBox)
            self.side_View_label.setPixmap(self.side_View_Img)
            self.side_View_label.resize(self.side_View_Img.width(), self.side_View_Img.height())
            self.side_View_label.move(45, 30)

            self.refer_Img_GroupBox1 = QtGui.QGroupBox(self.group5)
            self.refer_Img_GroupBox1.setGeometry(QtCore.QRect(380, 350, 370, 300))
            self.refer_Img_GroupBox1.setTitle(u"계산 공식")
            self.refer_Img_GroupBox1.setStyleSheet("font-size: 10pt;")
            self.refer_Img_GroupBox1.setFont('Courier')

            self.side_View_Img1 = QtGui.QPixmap(os.path.join(addonPath, "transmission_module/Flat_Belt_Calculation.jpg"))
            self.side_View_label1 = QtGui.QLabel(self.refer_Img_GroupBox1)
            self.side_View_label1.setPixmap(self.side_View_Img1)
            self.side_View_label1.resize(self.side_View_Img1.width(), self.side_View_Img1.height())
            self.side_View_label1.move(10, 30)

            self.group5.show()

        elif self.treeWidget.currentItem().text(0) == u"체인":
            self.group1.hide()
            self.group2.hide()
            self.group3.hide()
            self.group4.hide()
            self.group5.hide()
            self.group7.hide()

            self.label1 = QtGui.QLabel(u"체인 ()의 설계", self.group6)
            self.label1.setFont('Courier')
            self.label1.setStyleSheet("font: bold; font-size: 12pt;")
            self.label1.move(270, 10)
            self.label1.setAlignment(QtCore.Qt.AlignRight)

            self.group6.show()

        elif self.treeWidget.currentItem().text(0) == u"로프":
            self.group1.hide()
            self.group2.hide()
            self.group3.hide()
            self.group4.hide()
            self.group5.hide()
            self.group6.hide()

            self.label1 = QtGui.QLabel(u"로프 ()의 설계", self.group7)
            self.label1.setFont('Courier')
            self.label1.setStyleSheet("font: bold; font-size: 12pt;")
            self.label1.move(270, 10)
            self.label1.setAlignment(QtCore.Qt.AlignRight)

            self.group7.show()


    def onTable2_1(self):
        ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러
        buf = QtGui.QPixmap(os.path.join(addonPath, "transmission_module/Spur_Gear_Mechanical_Properties.jpg"))  #C 드라이브에 넣었음
        Imageview1 = QtGui.QLabel(ks)
        Imageview1.setPixmap(buf)
        Imageview1.resize(buf.width(), buf.height())
        Imageview1.move(0, 0)
        Imageview1.show()
        ks.setGeometry(750, 100, buf.width(), buf.height())
        ks.setWindowTitle(u"기어 재료의 기계적 성질")
        ks.show()
        ks.exec_()

    def onTable2_2(self):
        ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러
        buf = QtGui.QPixmap(os.path.join(addonPath, "transmission_module/Spur_Gear_Module.jpg"))  #C 드라이브에 넣었음
        Imageview1 = QtGui.QLabel(ks)
        Imageview1.setPixmap(buf)
        Imageview1.resize(buf.width(), buf.height())
        Imageview1.move(0, 0)
        Imageview1.show()
        ks.setGeometry(750, 100, buf.width(), buf.height())
        ks.setWindowTitle(u"모듈의 표준값")
        ks.show()
        ks.exec_()

    def onTable2_3(self):
        ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러
        buf = QtGui.QPixmap(os.path.join(addonPath, "transmission_module/Spur_Gear_Tooth.png"))  #C 드라이브에 넣었음
        Imageview1 = QtGui.QLabel(ks)
        Imageview1.setPixmap(buf)
        Imageview1.resize(buf.width(), buf.height())
        Imageview1.move(0, 0)
        Imageview1.show()
        ks.setGeometry(750, 100, buf.width(), buf.height())
        ks.setWindowTitle(u"평기어의 피치기준 치형계수 값")
        ks.show()
        ks.exec_()

    def onTable5_1(self):
        ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러
        buf = QtGui.QPixmap(os.path.join(addonPath, "transmission_module/Flat_Belt_Calculation.jpg"))  #C 드라이브에 넣었음
        Imageview1 = QtGui.QLabel(ks)
        Imageview1.setPixmap(buf)
        Imageview1.resize(buf.width(), buf.height())
        Imageview1.move(0, 0)
        Imageview1.show()
        ks.setGeometry(750, 100, buf.width(), buf.height())
        ks.setWindowTitle(u"허용 면 압력 Table")
        ks.show()
        ks.exec_()

    def onDesign2(self):
        hardness_gear = float(self.numericInput1.text())	# 기어 경도 대입
        hardness_pinion = float(self.numericInput2.text())	# 피니언 경도 대입
        module = float(self.numericInput4.text())			# 모듈 대입
        Z_gear = float(self.numericInput5.text())			# 기어 잇수 대입
        Z_pinion = float(self.numericInput6.text())			# 피니언 잇수 대입
        if self.popup7.currentText() == u"(rpm)":			# 기어의 회전 속력 대입
            rot_gear_rpm = float(self.numericInput7.text())
        elif self.popup7.currentText() == u"(rad/s)":
            rot_gear_rpm = 9.549296596425 * float(self.numericInput7.text())
        if self.popup8.currentText() == u"(kW)":			# 전달 동력 대입
            power_kW = float(self.numericInput8.text())
        elif self.popup8.currentText() == u"(HP)":
            power_kW = 0.745699872 * float(self.numericInput8.text())

        ratio = Z_gear/Z_pinion								# 회전비 계산
        dia_gear_mm = module*Z_gear							# 기어 피치원 지름 계산
        vel_pitch_mps = math.pi*dia_gear_mm*rot_gear_rpm/60000	# 피치원 속력 계산 (Z1, Z2 공통)
        contact_force_N = 1000*power_kW/vel_pitch_mps		# 이에 작용하는 컨택 포스 계산 (Z1, Z2 공통)
        dist_mm = module*(Z_gear + Z_pinion)/2+module/2				# 중심 사이 거리
        thick_tooth_mm = math.pi*module/2					# 이의 두께

        if vel_pitch_mps <= 5:								# 속도 계수 계산 (Z1, Z2 공통)
            fv = 3.05/(3.05 + vel_pitch_mps)
        elif vel_pitch_mps > 5 and vel_pitch_mps <= 10:
            fv = 6.1/(6.1 + vel_pitch_mps)
        elif vel_pitch_mps > 10 and vel_pitch_mps <= 20:
            fv = 15/(15 + vel_pitch_mps)
        else:
            fv = 5.55/(5.55 + math.sqrt(vel_pitch_mps))

        if hardness_gear >= 150 and hardness_gear < 200:
            if hardness_pinion >= 150 and hardness_pinion < 200:
                k_number = 0.262
                allow_comp_MPa = 340
            elif hardness_pinion >= 200 and hardness_pinion < 250:
                 k_number = 0.387
                 allow_comp_MPa = 410
            elif hardness_pinion > 250:
                 k_number = 0.514
                 allow_comp_MPa = 480
        elif hardness_gear >= 200 and hardness_gear < 250:
            if hardness_pinion >= 200 and hardness_pinion < 250:
                 k_number = 0.514
                 allow_comp_MPa = 480
            elif hardness_pinion >= 250 and hardness_pinion < 300:
                 k_number = 0.672
                 allow_comp_MPa = 550
            elif hardness_pinion > 300:
                 k_number = 0.848
                 allow_comp_MPa = 610
        elif hardness_gear >= 250 and hardness_gear < 300:
            if hardness_pinion >= 250 and hardness_pinion < 300:
                 k_number = 0.848
                 allow_comp_MPa = 610
            elif hardness_pinion >= 300 and hardness_pinion < 350:
                 k_number = 1.05
                 allow_comp_MPa = 680
            elif hardness_pinion > 350:
                 k_number = 1.27
                 allow_comp_MPa = 750
        elif hardness_gear >= 300 and hardness_gear < 350:
            if hardness_pinion >= 300 and hardness_pinion < 350:
                 k_number = 1.27
                 allow_comp_MPa = 750
            elif hardness_pinion >= 350 and hardness_pinion < 400:
                 k_number = 1.51
                 allow_comp_MPa = 820
            elif hardness_pinion > 400:
                 k_number = 1.66
                 allow_comp_MPa = 860
        elif hardness_gear >= 350 and hardness_gear < 400:
            if hardness_pinion >= 350 and hardness_pinion < 400:
                 k_number = 1.77
                 allow_comp_MPa = 890
            elif hardness_pinion >= 400 and hardness_pinion < 500:
                 k_number = 2.10
                 allow_comp_MPa = 970
            elif hardness_pinion > 500:
                 k_number = 2.23
                 allow_comp_MPa = 1000
        elif hardness_gear >= 400 and hardness_gear < 500:
            if hardness_pinion > 400 and hardness_pinion < 500:
                 k_number = 3.08
                 allow_comp_MPa = 1170
            elif hardness_pinion >= 500 and hardness_pinion < 600:
                 k_number = 3.24
                 allow_comp_MPa = 1200
            elif hardness_pinion > 600:
                 k_number = 3.45
                 allow_comp_MPa = 1240

        width_mm = contact_force_N*(Z_gear + Z_pinion)/(2*fv*k_number*dia_gear_mm*Z_pinion)

        if self.popup9.currentText() == u"(N)":				# 이에 작용하는 힘 대입
           self.numericInput9.setText(str(round(contact_force_N, 0)))
        elif self.popup9.currentText() == u"(lbf)":
           contact_force_lbf = 0.224809 * contact_force_N
           self.numericInput9.setText(str(round(contact_force_lbf, 0)))
        if self.popup10.currentText() == u"(MPa)":			# 허용 압축 응력 대입
           self.numericInput10.setText(str(round(allow_comp_MPa, 2)))
        elif self.popup10.currentText() == u"(ksi)":
           allow_comp_ksi = 0.1450377 * allow_comp_MPa
           self.numericInput10.setText(str(round(allow_comp_ksi, 2)))
        if self.popup11.currentText() == u"(mm)":			# 중심 사이 거리 대입
           self.numericInput11.setText(str(round(dist_mm, 2)))
        elif self.popup11.currentText() == u"(inch)":
           dist_inch = 1/24 * dist_mm
           self.numericInput11.setText(str(round(dist_inch, 2)))
        if self.popup12.currentText() == u"(mm)":			# 필요 두께 대입
           self.numericInput12.setText(str(round(width_mm, 2)))
        elif self.popup12.currentText() == u"(inch)":
           width_inch = 1/24 * width_mm
           self.numericInput12.setText(str(round(width_inch, 2)))

    def onDesign5(self):
        if self.popup1.currentText() == u"(가죽)":		# 인장강도 및 마찰계수 결정
            if self.popup2.currentText() == u"(철제)":
                si_MPa = 30.0
                frac = 0.25
                density_kgm = 860
        elif self.popup1.currentText() == u"(고무)":
            if self.popup2.currentText() == u"(철제)":
                si_MPa = 42.5
                frac = 0.225
                density_kgm = 1200
        if self.popup3.currentText() == u"(mm)":		# 벨트 두께 대입
            thick_mm = float(self.numericInput3.text())
        elif self.popup3.currentText() == u"(inch)":
            thick_mm = 25.4 * float(self.numericInput3.text())
        if self.popup4.currentText() == u"(mm)":		# 벨트 폭 대입
            height_mm = float(self.numericInput4.text())
        elif self.popup4.currentText() == u"(inch)":
            height_mm = 25.4 * float(self.numericInput4.text())
        if self.popup5.currentText() == u"(mm)":		# 큰 풀리 지름 대입
            dia1_mm = float(self.numericInput5.text())
        elif self.popup5.currentText() == u"(inch)":
            dia1_mm = 25.4 * float(self.numericInput5.text())
        if self.popup16.currentText() == u"(mm)":		# 두 풀리 사이 거리 대입
            dist_mm = float(self.numericInput16.text())
        elif self.popup16.currentText() == u"(inch)":
            dist_mm = 25.4 * float(self.numericInput16.text())
        if self.popup6.currentText() == u"(kW)":		# 전달 동력 대입
            power_kW = float(self.numericInput6.text())
        elif self.popup6.currentText() == u"(HP)":
            power_kW = 0.745699872 * float(self.numericInput6.text())
        if self.popup7.currentText() == u"(rpm)":		# 회전 속력 대입
            rot1_rpm = float(self.numericInput7.text())
        elif self.popup7.currentText() == u"(rad/s)":
            rot1_rpm = 9.549296596425 * float(self.numericInput7.text())
        ratio = float(self.numericInput8.text())        # 감속비 대입

        rot2_rpm = ratio*rot1_rpm									# 작은 풀리 회전 속력 계산
        dia2_mm = (dia1_mm + thick_mm)/ratio - thick_mm				# 작은 풀리 지름 계산
        vel_mps = (math.pi*dia1_mm*rot1_rpm)/(60000)			    # 벨트 속력 계산
        tension1_N = 1000*power_kW/vel_mps							# 유효 장력 계산
        theta1_rad = math.pi + 2*math.asin((dia1_mm - dia2_mm)/(2*dist_mm)) # 큰 풀리와 벨트 사이의 접촉 각
        theta2_rad = math.pi - 2*math.asin((dia1_mm - dia2_mm)/(2*dist_mm)) # 작은 풀리와 벨트 사이의 접촉 각
        length_mm = math.pi/2*(dia1_mm + dia2_mm) + (dia1_mm - dia2_mm)*(dia1_mm - dia2_mm)/(2*dist_mm) + 2*dist_mm*(1 - (dia1_mm - dia2_mm)*(dia1_mm - dia2_mm)/(8*dist_mm*dist_mm))
        tension_avail_N = math.exp(frac*theta2_rad)/( math.exp(frac*theta2_rad) - 1)*tension1_N + vel_mps*vel_mps*(density_kgm*height_mm*thick_mm/1000000)

        if self.popup9.currentText() == u"(mm)":					# 작은 풀리 지름 대입
           self.numericInput9.setText(str(round(dia2_mm, 1)))
        elif self.popup9.currentText() == u"(inch)":
           dia2_inch = 1/25.4 * dia2_mm
           self.numericInput9.setText(str(round(dia2_inch, 1)))
        if self.popup10.currentText() == u"(mm)":					# 벨트 길이 대입
           self.numericInput10.setText(str(round(length_mm, 0)))
        elif self.popup10.currentText() == u"(inch)":
           length_inch = 1/25.4 * length_mm
           self.numericInput10.setText(str(round(length_inch, 0)))
        if self.popup11.currentText() == u"(m/s)":					# 벨트 속력 대입
           self.numericInput11.setText(str(round(vel_mps, 3)))
        elif self.popup11.currentText() == u"(fps)":
           vel_fps = 3.28084 * vel_mps
           self.numericInput11.setText(str(round(vel_fps, 3)))
        if self.popup12.currentText() == u"(Newton)":				# 유효 장력 대입
           self.numericInput12.setText(str(round(tension_avail_N, 0)))
        elif self.popup12.currentText() == u"(lbf)":
           tension_avail_lbf = 0.224809 * tension_avail_N
           self.numericInput12.setText(str(round(tension_avail_lbf, 0)))
        if self.popup13.currentText() == u"(MPa)":					# 인장 강도 대입
           self.numericInput13.setText(str(round(si_MPa, 3)))
        elif self.popup13.currentText() == u"(ksi)":
           si_ksi = 0.1450377 * si_MPa
           self.numericInput13.setText(str(round(si_ksi, 3)))

    def onGenerate2(self):
        doc = App.newDocument()

        module = float(self.numericInput4.text())			# 모듈 대입
        Z_gear = float(self.numericInput5.text())			# 기어 잇수 대입
        Z_pinion = float(self.numericInput6.text())			# 피니언 잇수 대입
        if self.popup13.currentText() == u"(mm)":			# 기어 두께 대입
            width_mm = float(self.numericInput13.text())
        elif self.popup13.currentText() == u"(inch)":
            width_mm = 1/24 * float(self.numericInput13.text())
        if self.popup14.currentText() == u"(mm)":			# 축의 지름 대입
            axis_mm = float(self.numericInput14.text())
        elif self.popup14.currentText() == u"(inch)":
            axis_mm = 1/24 * float(self.numericInput14.text())

        dia_gear_mm = module*Z_gear							# 기어 피치원 지름 계산
        dia_pinion_mm = module*Z_pinion						# 피니온 피치원 지름 계산
        dist_mm = module*(Z_gear + Z_pinion)/2 + module/2				# 중심 사이 거리
        gear_rad = math.radians(90.0/Z_gear)
        pinion_rad = math.radians(90.0/Z_pinion)
        alpha_rad = 20.0*math.pi/180

        rot_initial = Base.Matrix()
        rot_initial.rotateZ(math.radians(180/Z_gear))
        rot_gear = Base.Matrix()
        rot_gear.rotateZ(math.radians(360.0/Z_gear))
        rot_pinion = Base.Matrix()
        rot_pinion.rotateZ(math.radians(360.0/Z_pinion))
        g1 = Base.Vector(-dia_gear_mm/2*math.sin(gear_rad) - 1.5708*module*tan(alpha_rad), dia_gear_mm/2*math.cos(gear_rad) - 1.15708*module, -width_mm/2)
        g2 = Base.Vector(-dia_gear_mm/2*math.sin(gear_rad) +		module*tan(alpha_rad), dia_gear_mm/2*math.cos(gear_rad) + 		  module,	-width_mm/2)
        g3 = Base.Vector( dia_gear_mm/2*math.sin(gear_rad) -		module*tan(alpha_rad), dia_gear_mm/2*math.cos(gear_rad) + 		  module, -width_mm/2)
        g4 = Base.Vector( dia_gear_mm/2*math.sin(gear_rad) + 1.5708*module*tan(alpha_rad), dia_gear_mm/2*math.cos(gear_rad) - 1.15708*module, -width_mm/2)
        p1 = Base.Vector(-dia_pinion_mm/2*math.sin(pinion_rad) - 1.5708*module*tan(alpha_rad), dia_pinion_mm/2*math.cos(pinion_rad) - 1.15708*module, -width_mm/2)
        p2 = Base.Vector(-dia_pinion_mm/2*math.sin(pinion_rad) + 	    module*tan(alpha_rad), dia_pinion_mm/2*math.cos(pinion_rad) + module		  ,	-width_mm/2)
        p3 = Base.Vector( dia_pinion_mm/2*math.sin(pinion_rad) - 	    module*tan(alpha_rad), dia_pinion_mm/2*math.cos(pinion_rad) + module		  , -width_mm/2)
        p4 = Base.Vector( dia_pinion_mm/2*math.sin(pinion_rad) + 1.5708*module*tan(alpha_rad), dia_pinion_mm/2*math.cos(pinion_rad) - 1.15708*module, -width_mm/2)
        polygon_gear = []
        polygon_pinion = []
        g1 = rot_initial.multiply(g1)
        g2 = rot_initial.multiply(g2)
        g3 = rot_initial.multiply(g3)
        g4 = rot_initial.multiply(g4)
        for i in range(int(Z_gear)):
            p14 = p4.add(Base.Vector(0, dist_mm, 0))
            p13 = p3.add(Base.Vector(0, dist_mm, 0))
            p12 = p2.add(Base.Vector(0, dist_mm, 0))
            p11 = p1.add(Base.Vector(0, dist_mm, 0))
            polygon_pinion.append(p14)
            polygon_pinion.append(p13)
            polygon_pinion.append(p12)
            polygon_pinion.append(p11)
            polygon_gear.append(g4)
            polygon_gear.append(g3)
            polygon_gear.append(g2)
            polygon_gear.append(g1)
            g1 = rot_gear.multiply(g1)
            g2 = rot_gear.multiply(g2)
            g3 = rot_gear.multiply(g3)
            g4 = rot_gear.multiply(g4)
            p1 = rot_pinion.multiply(p1)
            p2 = rot_pinion.multiply(p2)
            p3 = rot_pinion.multiply(p3)
            p4 = rot_pinion.multiply(p4)

        polygon_gear.append(g4)
        hexagon_gear = Part.makePolygon(polygon_gear)
        face_gear = Part.Face(hexagon_gear)
        exhex_gear = face_gear.extrude(Base.Vector(0.0,0.0, width_mm))
        #circle_gear = Part.makeCylinder((dia_gear_mm-2.31416*module)/2.0, width_mm, Vector(0.0, 0.0, -width_mm/2), Vector(0.0, 0.0, 1.0))
        #exhex_gear = exhex_gear.fuse(circle_gear)
        axis_gear = Part.makeCylinder(axis_mm/2.0, 1.1*width_mm, Vector(0.0, 0.0, -width_mm/2), Vector(0.0, 0.0, 1.0))
        exhex_gear = exhex_gear.cut(axis_gear)

        p14 = p4.add(Base.Vector(0, dist_mm, 0))
        polygon_pinion.append(p14)
        hexagon_pinion = Part.makePolygon(polygon_pinion)
        face_pinion = Part.Face(hexagon_pinion)
        exhex_pinion = face_pinion.extrude(Base.Vector(0.0,0.0, width_mm))
        #circle_pinion = Part.makeCylinder((dia_pinion_mm-2.31416*module)/2.0, width_mm, Vector(0.0, dist_mm, -width_mm/2), Vector(0.0, 0.0, 1.0))
        #exhex_pinion = exhex_pinion.fuse(circle_pinion)
        #circle = Part.makeCircle(axis_mm/2, Base.Vector(0.0, dist_mm, -width_mm/2), Base.Vector(0, 0, 1))
        #face_circle = Part.Face(circle)
        #axis_pinion = face_circle.extrude(Base.Vector(0.0,0.0, width_mm))
        axis_pinion = Part.makeCylinder(axis_mm/2.0, 1.5*width_mm, Vector(0.0, dist_mm, -width_mm/1.5), Vector(0.0, 0.0, 1.0))
        exhex_pinion = exhex_pinion.cut(axis_pinion)

        exhex = exhex_gear.fuse(exhex_pinion)

        shape = doc.addObject("Part::Feature")  #Color

        shape.Shape = exhex #Color
        doc.recompute()  #Color
        shape.ViewObject.ShapeColor = (1.0, 1.0, 1.0)  #Color
        Gui.activeDocument().activeView().viewAxometric()  #View
        Gui.SendMsgToActiveView("ViewFit")  #View


    def onGenerate5(self):
        doc = App.newDocument()

        # input parameters
        if self.popup3.currentText() == u"(mm)":		# 벨트 두께 대입
            thick_mm = float(self.numericInput3.text())
        elif self.popup3.currentText() == u"(inch)":
            thick_mm = 25.4 * float(self.numericInput3.text())
        if self.popup4.currentText() == u"(mm)":		# 벨트 폭 대입
            height_mm = float(self.numericInput4.text())
        elif self.popup4.currentText() == u"(inch)":
            height_mm = 25.4 * float(self.numericInput4.text())
        if self.popup5.currentText() == u"(mm)":		# 큰 풀리 지름 대입
            dia1_mm = float(self.numericInput5.text())
        elif self.popup5.currentText() == u"(inch)":
            dia1_mm = 25.4 * float(self.numericInput5.text())
        if self.popup9.currentText() == u"(mm)":		# 큰 풀리 지름 대입
            dia2_mm = float(self.numericInput9.text())
        elif self.popup9.currentText() == u"(inch)":
            dia2_mm = 25.4 * float(self.numericInput9.text())
        if self.popup16.currentText() == u"(mm)":		# 두 풀리 사이 거리 대입
            dist_mm = float(self.numericInput16.text())
        elif self.popup16.currentText() == u"(inch)":
            dist_mm = 25.4 * float(self.numericInput16.text())
        if self.popup14.currentText() == u"(mm)":		# 축의 지름 대입
            axis_dia_mm = float(self.numericInput14.text())
        elif self.popup14.currentText() == u"(inch)":
            aixs_dia_mm = 25.4 * float(self.numericInput14.text())
        pulley_thick_mm = 1.1*thick_mm + 10
        theta_rad = math.asin((dia1_mm - dia2_mm)/(2*dist_mm)) # 큰 풀리와 벨트 사이의 접촉 각

        # holes
        pulley1 = Part.makeCylinder(dia1_mm / 2.0, pulley_thick_mm, Vector(0.0, 0.0, -pulley_thick_mm/2), Vector(0.0, 0.0, 1.0))
        hole1 = Part.makeCylinder(axis_dia_mm / 2.0, pulley_thick_mm, Vector(0.0, 0.0, -pulley_thick_mm/2), Vector(0.0, 0.0, 1.0))
        #pulley1 = pulley1.cut(hole1)
        # Smaller pulley part
        pulley2 = Part.makeCylinder(dia2_mm / 2.0, pulley_thick_mm, Vector(dist_mm, 0.0, -pulley_thick_mm/2.0), Vector(0.0, 0.0, 1.0))
        hole2 = Part.makeCylinder(axis_dia_mm / 2.0, pulley_thick_mm, Vector(dist_mm, 0.0, -pulley_thick_mm/2.0), Vector(0.0, 0.0, 1.0))
        #pulley2 = pulley2.cut(hole2)
        # Combine two pulleys into one
        pulley1 = pulley1.fuse(pulley2)
        # Belt inner part
        inner_pulley1 = Part.makeCylinder(dia1_mm / 2.0, thick_mm, Vector(0.0, 0.0, -thick_mm/2), Vector(0.0, 0.0, 1.0))
        inner_pulley2 = Part.makeCylinder(dia2_mm / 2.0, thick_mm, Vector(dist_mm, 0.0, -thick_mm/2.0), Vector(0.0, 0.0, 1.0))
        inner_pulley1 = inner_pulley1.fuse(inner_pulley2)
        inner_p1 = Base.Vector( dia1_mm/2.0*math.sin(theta_rad), (dia1_mm/2.0)*math.cos(theta_rad), -thick_mm/2.0)
        inner_p2 = Base.Vector(-dia1_mm/2.0                    ,                               0.0, -thick_mm/2.0)
        inner_p3 = Base.Vector( dia1_mm/2.0*math.sin(theta_rad),-(dia1_mm/2.0)*math.cos(theta_rad), -thick_mm/2.0)
        inner_p4 = Base.Vector( dist_mm + dia2_mm/2.0*math.sin(theta_rad), (dia2_mm/2.0)*math.cos(theta_rad), -thick_mm/2.0)
        inner_p5 = Base.Vector( dist_mm + dia2_mm/2.0*math.sin(theta_rad),                               0.0, -thick_mm/2.0)
        inner_p6 = Base.Vector( dist_mm + dia2_mm/2.0*math.sin(theta_rad),-(dia2_mm/2.0)*math.cos(theta_rad), -thick_mm/2.0)
        inner_polygon = Part.makePolygon([inner_p1, inner_p4, inner_p6, inner_p3, inner_p1])
        inner_face = Part.Face(inner_polygon)
        inner_part = inner_face.extrude(Base.Vector(0.0, 0.0, thick_mm))
        inner_part = inner_pulley1.fuse(inner_part)
        # Belt outer part
        outer_pulley1 = Part.makeCylinder((dia1_mm + height_mm)/2.0, thick_mm, Vector(0.0, 0.0, -thick_mm/2), Vector(0.0, 0.0, 1.0))
        outer_pulley2 = Part.makeCylinder((dia2_mm + height_mm)/2.0, thick_mm, Vector(dist_mm, 0.0, -thick_mm/2.0), Vector(0.0, 0.0, 1.0))
        outer_pulley1 = outer_pulley1.fuse(outer_pulley2)
        outer_p1 = Base.Vector( (dia1_mm + height_mm)/2.0*math.sin(theta_rad), (dia1_mm + height_mm)/2.0*math.cos(theta_rad), -thick_mm/2.0)
        outer_p2 = Base.Vector(-(dia1_mm + height_mm)/2.0                ,                                           0.0, -thick_mm/2.0)
        outer_p3 = Base.Vector( (dia1_mm + height_mm)/2.0*math.sin(theta_rad),-(dia1_mm + height_mm)/2.0*math.cos(theta_rad), -thick_mm/2.0)
        outer_p4 = Base.Vector( dist_mm + (dia2_mm + height_mm)/2.0*math.sin(theta_rad), (dia2_mm + height_mm)/2.0*math.cos(theta_rad), -thick_mm/2.0)
        outer_p5 = Base.Vector( dist_mm + (dia2_mm + height_mm)/2.0*math.sin(theta_rad),                                           0.0, -thick_mm/2.0)
        outer_p6 = Base.Vector( dist_mm + (dia2_mm + height_mm)/2.0*math.sin(theta_rad),-(dia2_mm + height_mm)/2.0*math.cos(theta_rad), -thick_mm/2.0)
        outer_polygon = Part.makePolygon([outer_p1, outer_p4, outer_p6, outer_p3, outer_p1])
        outer_face = Part.Face(outer_polygon)
        outer_part = outer_face.extrude(Base.Vector(0.0, 0.0, thick_mm))
        outer_part = outer_pulley1.fuse(outer_part)
        # Belt part
        Belt = outer_part.cut(inner_part)
        # Combine pulleys and belts
        model = pulley1.fuse(Belt)
        model = model.cut(hole1)
        model = model.cut(hole2)


        shape = doc.addObject("Part::Feature")  #Color
        shape.Shape = model #Color
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
