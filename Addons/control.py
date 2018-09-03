
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
        self.treeWidget.setHeaderLabels([u"          운동조정용 기계부품"])  # headerlabel명
        self.treeWidget.setColumnCount(1)  # headerlabel 칼럼 갯수

        root1 = QtGui.QTreeWidgetItem(self.treeWidget)
        root1.setText(0, u'제동요소')
        child1 = QtGui.QTreeWidgetItem(root1)
        child1.setText(0, u'드럼 브레이크')
        self.treeWidget.addTopLevelItem(root1)

        root2 = QtGui.QTreeWidgetItem(self.treeWidget)
        root2.setText(0, u'완충요소')
        child1 = QtGui.QTreeWidgetItem(root2)
        child1.setText(0, u'압축 스프링')
        child2 = QtGui.QTreeWidgetItem(root2)
        child2.setText(0, u'토션바')
        child3 = QtGui.QTreeWidgetItem(root2)
        child3.setText(0, u'관성차')
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
        if self.treeWidget.currentItem().text(0) == u"드럼 브레이크":
            self.group2.hide()
            self.group3.hide()
            self.group4.hide()

            self.label1 = QtGui.QLabel(u"드럼 브레이크(Drum Brake)의 설계", self.group1)
            self.label1.setFont('Courier')
            self.label1.setStyleSheet("font: bold; font-size: 12pt;")
            self.label1.move(250, 10)
            self.label1.setAlignment(QtCore.Qt.AlignRight)

            # Varialbe group
            self.powergroup = QtGui.QGroupBox(self.group1)
            self.powergroup.setGeometry(QtCore.QRect(30,70,340,295))
            self.powergroup.setTitle(u"설계 변수")
            self.powergroup.setStyleSheet("font-size: 10pt;")
            self.powergroup.setFont('Courier')

            self.label1 = QtGui.QLabel(u"제어 동력", self.powergroup)
            self.label1.move(40,40)
            self.numericInput1 = QtGui.QLineEdit(self.powergroup)
            self.numericInput1.setFixedWidth(50)
            self.numericInput1.move(170, 35)
            self.popupItems1 = (u"(kW)", u"(HP)")
            self.popup1 = QtGui.QComboBox(self.powergroup)
            self.popup1.addItems(self.popupItems1)
            self.popup1.setCurrentIndex(self.popupItems1.index(u"(kW)"))
            self.popup1.move(230, 35)
            self.label2 = QtGui.QLabel(u"제어 회전속력", self.powergroup)
            self.label2.move(40,65)
            self.numericInput2 = QtGui.QLineEdit(self.powergroup)
            self.numericInput2.setFixedWidth(50)
            self.numericInput2.move(170, 60)
            self.popupItems2 = (u"(rpm)", u"(rad/s)")
            self.popup2 = QtGui.QComboBox(self.powergroup)
            self.popup2.addItems(self.popupItems2)
            self.popup2.setCurrentIndex(self.popupItems2.index(u"(rpm)"))
            self.popup2.move(230, 60)
            self.label3 = QtGui.QLabel(u"슈에 걸리는 힘", self.powergroup)
            self.label3.move(40,90)
            self.numericInput3 = QtGui.QLineEdit(self.powergroup)
            self.numericInput3.setFixedWidth(50)
            self.numericInput3.move(170, 85)
            self.popupItems3 = (u"(N)", u"(lbf)")
            self.popup3 = QtGui.QComboBox(self.powergroup)
            self.popup3.addItems(self.popupItems3)
            self.popup3.setCurrentIndex(self.popupItems3.index(u"(N)"))
            self.popup3.move(230, 85)
            self.label4 = QtGui.QLabel(u"유압실린더의 지름", self.powergroup)
            self.label4.move(40,115)
            self.label4.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.numericInput4 = QtGui.QLineEdit(self.powergroup)
            self.numericInput4.setFixedWidth(50)
            self.numericInput4.move(170, 110)
            self.popupItems4 = (u"(mm)", u"(inch)")
            self.popup4 = QtGui.QComboBox(self.powergroup)
            self.popup4.addItems(self.popupItems4)
            self.popup4.setCurrentIndex(self.popupItems4.index(u"(mm)"))
            self.popup4.move(230, 110)
            self.label5 = QtGui.QLabel(u"레버의 치수(b)", self.powergroup)
            self.label5.move(40,140)
            self.label5.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.numericInput5 = QtGui.QLineEdit(self.powergroup)
            self.numericInput5.setFixedWidth(50)
            self.numericInput5.move(170, 135)
            self.popupItems5 = (u"(mm)", u"(inch)")
            self.popup5 = QtGui.QComboBox(self.powergroup)
            self.popup5.addItems(self.popupItems5)
            self.popup5.setCurrentIndex(self.popupItems5.index(u"(mm)"))
            self.popup5.move(230, 135)
            self.label6 = QtGui.QLabel(u"레버의 치수(c)", self.powergroup)
            self.label6.move(40,165)
            self.label6.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.numericInput6 = QtGui.QLineEdit(self.powergroup)
            self.numericInput6.setFixedWidth(50)
            self.numericInput6.move(170, 160)
            self.popupItems6 = (u"(mm)", u"(inch)")
            self.popup6 = QtGui.QComboBox(self.powergroup)
            self.popup6.addItems(self.popupItems6)
            self.popup6.setCurrentIndex(self.popupItems6.index(u"(mm)"))
            self.popup6.move(230, 160)
            self.label7 = QtGui.QLabel(u"브레이크의 지름", self.powergroup)
            self.label7.move(40,190)
            self.label7.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.numericInput7 = QtGui.QLineEdit(self.powergroup)
            self.numericInput7.setFixedWidth(50)
            self.numericInput7.move(170, 185)
            self.popupItems7 = (u"(mm)", u"(inch)")
            self.popup7 = QtGui.QComboBox(self.powergroup)
            self.popup7.addItems(self.popupItems7)
            self.popup7.setCurrentIndex(self.popupItems7.index(u"(mm)"))
            self.popup7.move(230, 185)
            self.label8 = QtGui.QLabel(u"접촉면 마찰계수", self.powergroup)
            self.label8.move(40,215)
            self.numericInput8 = QtGui.QLineEdit(self.powergroup)
            self.numericInput8.setFixedWidth(50)
            self.numericInput8.move(170,210)
            self.tableButton = QtGui.QPushButton(u"재료의 기계적 성질", self.powergroup)
            self.tableButton.clicked.connect(self.onTable1_1)
            self.tableButton.setFixedWidth(180)
            self.tableButton.setAutoDefault(True)
            self.tableButton.move(90,235)
            self.designButton = QtGui.QPushButton("Design", self.powergroup)
            self.designButton.clicked.connect(self.onDesign1)
            self.designButton.setFixedWidth(180)
            self.designButton.setAutoDefault(True)
            self.designButton.move(90,265)

            # Result group
            self.resultgroup = QtGui.QGroupBox(self.group1)
            self.resultgroup.setGeometry(QtCore.QRect(30,375,340,165))
            self.resultgroup.setTitle(u"계산 결과")
            self.resultgroup.setStyleSheet("font-size: 10pt;")
            self.resultgroup.setFont('Courier')

            self.label9 = QtGui.QLabel(u"제동 토크", self.resultgroup)
            self.label9.move(40, 40)
            self.numericInput9 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput9.setFixedWidth(50)
            self.numericInput9.move(170, 35)
            self.popupItems9 = (u"(N*m)", u"(lbf*inch)")
            self.popup9 = QtGui.QComboBox(self.resultgroup)
            self.popup9.addItems(self.popupItems9)
            self.popup9.setCurrentIndex(self.popupItems9.index(u"(N*m)"))
            self.popup9.move(230, 35)
            self.label10 = QtGui.QLabel(u"제동력", self.resultgroup)
            self.label10.move(40, 65)
            self.numericInput10 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput10.setFixedWidth(50)
            self.numericInput10.move(170, 60)
            self.popupItems10 = (u"(N)", u"(lbf)")
            self.popup10 = QtGui.QComboBox(self.resultgroup)
            self.popup10.addItems(self.popupItems10)
            self.popup10.setCurrentIndex(self.popupItems10.index(u"(N)"))
            self.popup10.move(230, 60)
            self.label11 = QtGui.QLabel(u"필요 유압", self.resultgroup)
            self.label11.move(40, 90)
            self.numericInput11 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput11.setFixedWidth(50)
            self.numericInput11.move(170, 85)
            self.popupItems11 = (u"(MPa)", u"(ksi)")
            self.popup11 = QtGui.QComboBox(self.resultgroup)
            self.popup11.addItems(self.popupItems11)
            self.popup11.setCurrentIndex(self.popupItems11.index(u"(MPa)"))
            self.popup11.move(230, 85)
            self.label12 = QtGui.QLabel(u"레버의 치수(a)", self.resultgroup)
            self.label12.move(40, 115)
            self.label12.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.numericInput12 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput12.setFixedWidth(50)
            self.numericInput12.move(170, 110)
            self.popupItems12 = (u"(mm)", u"(inch)")
            self.popup12 = QtGui.QComboBox(self.resultgroup)
            self.popup12.addItems(self.popupItems12)
            self.popup12.setCurrentIndex(self.popupItems12.index(u"(mm)"))
            self.popup12.move(230, 110)
            self.label13 = QtGui.QLabel(u"슈의 두께", self.resultgroup)
            self.label13.move(40, 140)
            self.label13.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.numericInput13 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput13.setFixedWidth(50)
            self.numericInput13.move(170, 135)
            self.popupItems13 = (u"(mm)", u"(inch)")
            self.popup13 = QtGui.QComboBox(self.resultgroup)
            self.popup13.addItems(self.popupItems13)
            self.popup13.setCurrentIndex(self.popupItems13.index(u"(mm)"))
            self.popup13.move(230, 135)

            # Modling group
            self.modelinggroup = QtGui.QGroupBox(self.group1)
            self.modelinggroup.setGeometry(QtCore.QRect(30,550,340,115))
            self.modelinggroup.setTitle(u"모델링")
            self.modelinggroup.setStyleSheet("font-size: 10pt;")
            self.modelinggroup.setFont('Courier')

            self.label14 = QtGui.QLabel(u"브레이크의 높이", self.modelinggroup)
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
            self.generateButton.clicked.connect(self.onGenerate1)
            self.generateButton.setFixedWidth(180)
            self.generateButton.setAutoDefault(True)
            self.generateButton.move(90, 85)

            # Pictures 1
            self.refer_Img_GroupBox = QtGui.QGroupBox(self.group1)
            self.refer_Img_GroupBox.setGeometry(QtCore.QRect(380, 70, 370, 270))
            self.refer_Img_GroupBox.setTitle(u"드럼 브레이크 (Drum Brake)")
            self.refer_Img_GroupBox.setStyleSheet("font-size: 10pt;")
            self.refer_Img_GroupBox.setFont('Courier')

            self.side_View_Img = QtGui.QPixmap(os.path.join(addonPath, "control_module\Drum_Brake_Model.jpg"))
            self.side_View_label = QtGui.QLabel(self.refer_Img_GroupBox)
            self.side_View_label.setPixmap(self.side_View_Img)
            self.side_View_label.resize(self.side_View_Img.width(), self.side_View_Img.height())
            self.side_View_label.move(45, 30)

            self.refer_Img_GroupBox1 = QtGui.QGroupBox(self.group1)
            self.refer_Img_GroupBox1.setGeometry(QtCore.QRect(380, 350, 370, 400))
            self.refer_Img_GroupBox1.setTitle(u"계산 공식")
            self.refer_Img_GroupBox1.setStyleSheet("font-size: 10pt;")
            self.refer_Img_GroupBox1.setFont('Courier')

            self.side_View_Img1 = QtGui.QPixmap(os.path.join(addonPath, "control_module\Drum_Brake_Calculation.jpg"))
            self.side_View_label1 = QtGui.QLabel(self.refer_Img_GroupBox1)
            self.side_View_label1.setPixmap(self.side_View_Img1)
            self.side_View_label1.resize(self.side_View_Img1.width(), self.side_View_Img1.height())
            self.side_View_label1.move(10, 30)


            self.group1.show()

        elif self.treeWidget.currentItem().text(0) == u"압축 스프링":
            self.group1.hide()
            self.group3.hide()
            self.group4.hide()

            self.label1 = QtGui.QLabel(u"압축 스프링 (Compressive Spring)의 설계", self.group2)
            self.label1.setFont('Courier')
            self.label1.setStyleSheet("font: bold; font-size: 12pt;")
            self.label1.move(200, 10)
            self.label1.setAlignment(QtCore.Qt.AlignRight)

            self.power1group = QtGui.QGroupBox(self.group2)
            self.power1group.setGeometry(QtCore.QRect(30, 70, 340, 95))
            self.power1group.setTitle(u"재료 및 설계 제한 조건")
            self.power1group.setStyleSheet("font-size: 10pt;")
            self.power1group.setFont('Courier')
            self.label2 = QtGui.QLabel(u"피로하중을 고려하지 않은",self.power1group)
            self.label2.setStyleSheet("font: bold;")
            self.label2.move(40,40)
            self.label21 = QtGui.QLabel(u"Plain end, right hand 압축 스프링 설계",self.power1group)
            self.label21.setStyleSheet("font: bold;")
            self.label21.move(40,65)

            # Varialbe group
            self.powergroup = QtGui.QGroupBox(self.group2)
            self.powergroup.setGeometry(QtCore.QRect(30,175,340,200))
            self.powergroup.setTitle(u"설계 변수")
            self.powergroup.setStyleSheet("font-size: 10pt;")
            self.powergroup.setFont('Courier')
            self.label3 = QtGui.QLabel(u"Wire의 종류", self.powergroup)
            self.label3.move(40,40)
            self.popupItems3 = (u"(A227)", u"(A228)", u"(A232)", u"(A313)", u"(A401)", u"(B159)")
            self.popup3 = QtGui.QComboBox(self.powergroup)
            self.popup3.addItems(self.popupItems3)
            self.popup3.setCurrentIndex(self.popupItems3.index(u"(A227)"))
            self.popup3.move(230, 35)
            self.tableButton = QtGui.QPushButton(u"Spring Wire의 물성치", self.powergroup)
            self.tableButton.clicked.connect(self.onTable2_1)
            self.tableButton.setFixedWidth(180)
            self.tableButton.setAutoDefault(True)
            self.tableButton.move(90,60)
            self.label4 = QtGui.QLabel(u"Wire 지름", self.powergroup)
            self.label4.move(40,95)
            self.numericInput4 = QtGui.QLineEdit(self.powergroup)
            self.numericInput4.setFixedWidth(50)
            self.numericInput4.move(170, 90)
            self.popupItems4 = (u"(mm)", u"(inch)")
            self.popup4 = QtGui.QComboBox(self.powergroup)
            self.popup4.addItems(self.popupItems4)
            self.popup4.setCurrentIndex(self.popupItems4.index(u"(mm)"))
            self.popup4.move(230, 90)
            self.label5 = QtGui.QLabel(u"평균 스프링 지름", self.powergroup)
            self.label5.move(40,120)
            self.numericInput5 = QtGui.QLineEdit(self.powergroup)
            self.numericInput5.setFixedWidth(50)
            self.numericInput5.move(170, 115)
            self.popupItems5 = (u"(mm)", u"(inch)")
            self.popup5 = QtGui.QComboBox(self.powergroup)
            self.popup5.addItems(self.popupItems5)
            self.popup5.setCurrentIndex(self.popupItems5.index(u"(mm)"))
            self.popup5.move(230, 115)
            self.label6 = QtGui.QLabel(u"총 감김수", self.powergroup)
            self.label6.move(40,145)
            self.numericInput6 = QtGui.QLineEdit(self.powergroup)
            self.numericInput6.setFixedWidth(50)
            self.numericInput6.move(170, 140)
            self.designButton = QtGui.QPushButton("Design", self.powergroup)
            self.designButton.clicked.connect(self.onDesign2)
            self.designButton.setFixedWidth(180)
            self.designButton.setAutoDefault(True)
            self.designButton.move(90,165)

            # Result group
            self.resultgroup = QtGui.QGroupBox(self.group2)
            self.resultgroup.setGeometry(QtCore.QRect(30,385,340,190))
            self.resultgroup.setTitle(u"계산 결과")
            self.resultgroup.setStyleSheet("font-size: 10pt;")
            self.resultgroup.setFont('Courier')
            self.label9 = QtGui.QLabel(u"피치 길이", self.resultgroup)
            self.label9.move(40, 40)
            self.numericInput9 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput9.setFixedWidth(50)
            self.numericInput9.move(170, 35)
            self.popupItems9 = (u"(mm)", u"(inch)")
            self.popup9 = QtGui.QComboBox(self.resultgroup)
            self.popup9.addItems(self.popupItems9)
            self.popup9.setCurrentIndex(self.popupItems9.index(u"(mm)"))
            self.popup9.move(230, 35)
            self.label10 = QtGui.QLabel(u"최대 하중", self.resultgroup)
            self.label10.move(40, 65)
            self.numericInput10 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput10.setFixedWidth(50)
            self.numericInput10.move(170, 60)
            self.popupItems10 = (u"(N)", u"(lbf)")
            self.popup10 = QtGui.QComboBox(self.resultgroup)
            self.popup10.addItems(self.popupItems10)
            self.popup10.setCurrentIndex(self.popupItems10.index(u"(N)"))
            self.popup10.move(230, 60)
            self.label11 = QtGui.QLabel(u"자유 높이", self.resultgroup)
            self.label11.move(40, 90)
            self.numericInput11 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput11.setFixedWidth(50)
            self.numericInput11.move(170, 85)
            self.popupItems11 = (u"(mm)", u"(inch)")
            self.popup11 = QtGui.QComboBox(self.resultgroup)
            self.popup11.addItems(self.popupItems11)
            self.popup11.setCurrentIndex(self.popupItems11.index(u"(mm)"))
            self.popup11.move(230, 85)
            self.label12 = QtGui.QLabel(u"밀착 높이", self.resultgroup)
            self.label12.move(40, 115)
            self.numericInput12 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput12.setFixedWidth(50)
            self.numericInput12.move(170, 110)
            self.popupItems12 = (u"(mm)", u"(inch)")
            self.popup12 = QtGui.QComboBox(self.resultgroup)
            self.popup12.addItems(self.popupItems12)
            self.popup12.setCurrentIndex(self.popupItems12.index(u"(mm)"))
            self.popup12.move(230, 110)
            self.label13 = QtGui.QLabel(u"스프링 상수", self.resultgroup)
            self.label13.move(40, 140)
            self.numericInput13 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput13.setFixedWidth(50)
            self.numericInput13.move(170, 135)
            self.popupItems13 = (u"(N/mm)", u"(lbf/inch)")
            self.popup13 = QtGui.QComboBox(self.resultgroup)
            self.popup13.addItems(self.popupItems13)
            self.popup13.setCurrentIndex(self.popupItems13.index(u"(N/mm)"))
            self.popup13.move(230, 135)

            # Modling group
            self.modelinggroup = QtGui.QGroupBox(self.group2)
            self.modelinggroup.setGeometry(QtCore.QRect(30,560,340,165))
            self.modelinggroup.setTitle(u"모델링")
            self.modelinggroup.setStyleSheet("font-size: 10pt;")
            self.modelinggroup.setFont('Courier')
            self.label14 = QtGui.QLabel(u"스프링 지름", self.modelinggroup)
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
            self.label15 = QtGui.QLabel(u"평균 코일 지름", self.modelinggroup)
            self.label15.move(40, 65)
            self.label15.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.numericInput15 = QtGui.QLineEdit(self.modelinggroup)
            self.numericInput15.setFixedWidth(50)
            self.numericInput15.move(170, 60)
            self.popupItems15 = (u"(mm)", u"(inch)")
            self.popup15 = QtGui.QComboBox(self.modelinggroup)
            self.popup15.addItems(self.popupItems15)
            self.popup15.setCurrentIndex(self.popupItems15.index(u"(mm)"))
            self.popup15.move(230, 60)
            self.label16 = QtGui.QLabel(u"피치 길이", self.modelinggroup)
            self.label16.move(40, 90)
            self.label16.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.numericInput16 = QtGui.QLineEdit(self.modelinggroup)
            self.numericInput16.setFixedWidth(50)
            self.numericInput16.move(170, 85)
            self.popupItems16 = (u"(mm)", u"(inch)")
            self.popup16 = QtGui.QComboBox(self.modelinggroup)
            self.popup16.addItems(self.popupItems16)
            self.popup16.setCurrentIndex(self.popupItems16.index(u"(mm)"))
            self.popup16.move(230, 85)
            self.label17 = QtGui.QLabel(u"*붉은 색 파라미터를 이용하여 모델링함*", self.modelinggroup)
            self.label17.move(50, 115)
            self.label17.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.generateButton = QtGui.QPushButton("Generate", self.modelinggroup)
            self.generateButton.clicked.connect(self.onGenerate2)
            self.generateButton.setFixedWidth(180)
            self.generateButton.setAutoDefault(True)
            self.generateButton.move(90, 135)

            # Pictures 1
            self.refer_Img_GroupBox = QtGui.QGroupBox(self.group2)
            self.refer_Img_GroupBox.setGeometry(QtCore.QRect(380, 70, 370, 270))
            self.refer_Img_GroupBox.setTitle(u"드럼 브레이크 (Drum Brake)")
            self.refer_Img_GroupBox.setStyleSheet("font-size: 10pt;")
            self.refer_Img_GroupBox.setFont('Courier')

            self.side_View_Img = QtGui.QPixmap(os.path.join(addonPath, "control_module\Compressive_Spring_Model.jpg"))
            self.side_View_label = QtGui.QLabel(self.refer_Img_GroupBox)
            self.side_View_label.setPixmap(self.side_View_Img)
            self.side_View_label.resize(self.side_View_Img.width(), self.side_View_Img.height())
            self.side_View_label.move(10, 30)

            self.refer_Img_GroupBox1 = QtGui.QGroupBox(self.group2)
            self.refer_Img_GroupBox1.setGeometry(QtCore.QRect(380, 350, 370, 400))
            self.refer_Img_GroupBox1.setTitle(u"계산 공식")
            self.refer_Img_GroupBox1.setStyleSheet("font-size: 10pt;")
            self.refer_Img_GroupBox1.setFont('Courier')

            self.side_View_Img1 = QtGui.QPixmap(os.path.join(addonPath, "control_module\Compressive_Spring_Calculation.jpg"))
            self.side_View_label1 = QtGui.QLabel(self.refer_Img_GroupBox1)
            self.side_View_label1.setPixmap(self.side_View_Img1)
            self.side_View_label1.resize(self.side_View_Img1.width(), self.side_View_Img1.height())
            self.side_View_label1.move(10, 30)

            self.group2.show()

        elif self.treeWidget.currentItem().text(0) == u"토션바":
            self.group1.hide()
            self.group2.hide()
            self.group4.hide()

            self.label1 = QtGui.QLabel(u"토션바 (Torsion Bar)의 설계", self.group3)
            self.label1.setFont('Courier')
            self.label1.setStyleSheet("font: bold; font-size: 12pt;")
            self.label1.move(270, 10)
            self.label1.setAlignment(QtCore.Qt.AlignRight)

            # Varialbe group
            self.powergroup = QtGui.QGroupBox(self.group3)
            self.powergroup.setGeometry(QtCore.QRect(30,70,340,165))
            self.powergroup.setTitle(u"설계 변수")
            self.powergroup.setStyleSheet("font-size: 10pt;")
            self.powergroup.setFont('Courier')
            self.label3 = QtGui.QLabel(u"전단탄성계수", self.powergroup)
            self.label3.move(40,40)
            self.numericInput3 = QtGui.QLineEdit(self.powergroup)
            self.numericInput3.setFixedWidth(50)
            self.numericInput3.move(170, 35)
            self.popupItems3 = (u"(MPa)", u"(ksi)")
            self.popup3 = QtGui.QComboBox(self.powergroup)
            self.popup3.addItems(self.popupItems3)
            self.popup3.setCurrentIndex(self.popupItems3.index(u"(MPa)"))
            self.popup3.move(230, 35)
            self.label4 = QtGui.QLabel(u"허용전단응력", self.powergroup)
            self.label4.move(40,65)
            self.numericInput4 = QtGui.QLineEdit(self.powergroup)
            self.numericInput4.setFixedWidth(50)
            self.numericInput4.move(170, 60)
            self.popupItems4 = (u"(MPa)", u"(ksi)")
            self.popup4 = QtGui.QComboBox(self.powergroup)
            self.popup4.addItems(self.popupItems4)
            self.popup4.setCurrentIndex(self.popupItems4.index(u"(MPa)"))
            self.popup4.move(230, 60)
            self.label5 = QtGui.QLabel(u"비틀림모멘트", self.powergroup)
            self.label5.move(40,90)
            self.numericInput5 = QtGui.QLineEdit(self.powergroup)
            self.numericInput5.setFixedWidth(50)
            self.numericInput5.move(170, 85)
            self.popupItems5 = (u"(N*mm)", u"(lbf*inch)")
            self.popup5 = QtGui.QComboBox(self.powergroup)
            self.popup5.addItems(self.popupItems5)
            self.popup5.setCurrentIndex(self.popupItems5.index(u"(N*mm)"))
            self.popup5.move(230, 85)
            self.label6 = QtGui.QLabel(u"비틀림 각", self.powergroup)
            self.label6.move(40,115)
            self.numericInput6 = QtGui.QLineEdit(self.powergroup)
            self.numericInput6.setFixedWidth(50)
            self.numericInput6.move(170, 110)
            self.popupItems6 = (u"(degree)", u"(rad)")
            self.popup6 = QtGui.QComboBox(self.powergroup)
            self.popup6.addItems(self.popupItems6)
            self.popup6.setCurrentIndex(self.popupItems6.index(u"(rad)"))
            self.popup6.move(230, 110)
            self.designButton = QtGui.QPushButton("Design", self.powergroup)
            self.designButton.clicked.connect(self.onDesign3)
            self.designButton.setFixedWidth(180)
            self.designButton.setAutoDefault(True)
            self.designButton.move(90,135)

            # Result group
            self.resultgroup = QtGui.QGroupBox(self.group3)
            self.resultgroup.setGeometry(QtCore.QRect(30,245,340,115))
            self.resultgroup.setTitle(u"계산 결과")
            self.resultgroup.setStyleSheet("font-size: 10pt;")
            self.resultgroup.setFont('Courier')
            self.label9 = QtGui.QLabel(u"토션바 지름", self.resultgroup)
            self.label9.move(40, 40)
            self.numericInput9 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput9.setFixedWidth(50)
            self.numericInput9.move(170, 35)
            self.popupItems9 = (u"(mm)", u"(inch)")
            self.popup9 = QtGui.QComboBox(self.resultgroup)
            self.popup9.addItems(self.popupItems9)
            self.popup9.setCurrentIndex(self.popupItems9.index(u"(mm)"))
            self.popup9.move(230, 35)
            self.label10 = QtGui.QLabel(u"토션바 길이", self.resultgroup)
            self.label10.move(40, 65)
            self.numericInput10 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput10.setFixedWidth(50)
            self.numericInput10.move(170, 60)
            self.popupItems10 = (u"(mm)", u"(inch)")
            self.popup10 = QtGui.QComboBox(self.resultgroup)
            self.popup10.addItems(self.popupItems10)
            self.popup10.setCurrentIndex(self.popupItems10.index(u"(mm)"))
            self.popup10.move(230, 60)
            self.label11 = QtGui.QLabel(u"단위체적 탄성에너지", self.resultgroup)
            self.label11.move(40, 90)
            self.numericInput11 = QtGui.QLineEdit(self.resultgroup)
            self.numericInput11.setFixedWidth(50)
            self.numericInput11.move(170, 85)
            self.popupItems11 = (u"(N*mm/mm^3)", u"(1000*lbf*inch/inch^3)")
            self.popup11 = QtGui.QComboBox(self.resultgroup)
            self.popup11.addItems(self.popupItems11)
            self.popup11.setCurrentIndex(self.popupItems11.index(u"(N*mm/mm^3)"))
            self.popup11.move(230, 85)

            # Modling group
            self.modelinggroup = QtGui.QGroupBox(self.group3)
            self.modelinggroup.setGeometry(QtCore.QRect(30,370,340,140))
            self.modelinggroup.setTitle(u"모델링")
            self.modelinggroup.setStyleSheet("font-size: 10pt;")
            self.modelinggroup.setFont('Courier')
            self.label12 = QtGui.QLabel(u"토션바 지름", self.modelinggroup)
            self.label12.move(40, 40)
            self.label12.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.numericInput12 = QtGui.QLineEdit(self.modelinggroup)
            self.numericInput12.setFixedWidth(50)
            self.numericInput12.move(170, 35)
            self.popupItems12 = (u"(mm)", u"(inch)")
            self.popup12 = QtGui.QComboBox(self.modelinggroup)
            self.popup12.addItems(self.popupItems12)
            self.popup12.setCurrentIndex(self.popupItems12.index(u"(mm)"))
            self.popup12.move(230, 35)
            self.label13 = QtGui.QLabel(u"토션바 길이", self.modelinggroup)
            self.label13.move(40, 65)
            self.label13.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.numericInput13 = QtGui.QLineEdit(self.modelinggroup)
            self.numericInput13.setFixedWidth(50)
            self.numericInput13.move(170, 60)
            self.popupItems13 = (u"(mm)", u"(inch)")
            self.popup13 = QtGui.QComboBox(self.modelinggroup)
            self.popup13.addItems(self.popupItems13)
            self.popup13.setCurrentIndex(self.popupItems13.index(u"(mm)"))
            self.popup13.move(230, 60)
            self.label14 = QtGui.QLabel(u"*붉은 색 파라미터를 이용하여 모델링함*", self.modelinggroup)
            self.label14.move(50, 90)
            self.label14.setStyleSheet("color: rgb(255,0,0);")  # 텍스트 색 변환
            self.generateButton = QtGui.QPushButton("Generate", self.modelinggroup)
            self.generateButton.clicked.connect(self.onGenerate3)
            self.generateButton.setFixedWidth(180)
            self.generateButton.setAutoDefault(True)
            self.generateButton.move(90, 110)

            # Pictures 1
            self.refer_Img_GroupBox = QtGui.QGroupBox(self.group3)
            self.refer_Img_GroupBox.setGeometry(QtCore.QRect(380, 70, 370, 270))
            self.refer_Img_GroupBox.setTitle(u"드럼 브레이크 (Drum Brake)")
            self.refer_Img_GroupBox.setStyleSheet("font-size: 10pt;")
            self.refer_Img_GroupBox.setFont('Courier')

            self.side_View_Img = QtGui.QPixmap(os.path.join(addonPath, "control_module\Torsion_Bar_Model.jpg"))
            self.side_View_label = QtGui.QLabel(self.refer_Img_GroupBox)
            self.side_View_label.setPixmap(self.side_View_Img)
            self.side_View_label.resize(self.side_View_Img.width(), self.side_View_Img.height())
            self.side_View_label.move(45, 30)

            self.refer_Img_GroupBox1 = QtGui.QGroupBox(self.group3)
            self.refer_Img_GroupBox1.setGeometry(QtCore.QRect(380, 350, 370, 400))
            self.refer_Img_GroupBox1.setTitle(u"계산 공식")
            self.refer_Img_GroupBox1.setStyleSheet("font-size: 10pt;")
            self.refer_Img_GroupBox1.setFont('Courier')

            self.side_View_Img1 = QtGui.QPixmap(os.path.join(addonPath, "control_module\Torsion_Bar_Calculation.jpg"))
            self.side_View_label1 = QtGui.QLabel(self.refer_Img_GroupBox1)
            self.side_View_label1.setPixmap(self.side_View_Img1)
            self.side_View_label1.resize(self.side_View_Img1.width(), self.side_View_Img1.height())
            self.side_View_label1.move(10, 30)

            self.group3.show()

        elif self.treeWidget.currentItem().text(0) == u"관성차":
            self.group1.hide()
            self.group2.hide()
            self.group3.hide()

            self.label1 = QtGui.QLabel(u"관성차 ()의 설계", self.group4)
            self.label1.setFont('Courier')
            self.label1.setStyleSheet("font: bold; font-size: 12pt;")
            self.label1.move(270, 10)
            self.label1.setAlignment(QtCore.Qt.AlignRight)

            self.group4.show()

    def onTable1_1(self):
        ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러
        buf = QtGui.QPixmap(os.path.join(addonPath, "control_module\Drum_Brake_Table1.jpg"))  #C 드라이브에 넣었음
        Imageview1 = QtGui.QLabel(ks)
        Imageview1.setPixmap(buf)
        Imageview1.resize(buf.width(), buf.height())
        Imageview1.move(0, 0)
        Imageview1.show()
        ks.setGeometry(750, 100, buf.width(), buf.height())
        ks.setWindowTitle(u"재료에 따른 마찰계수 및 허용압력")
        ks.show()
        ks.exec_()

    def onTable2_1(self):
        ks = QtGui.QDialog()  # QtGui.QMessageBox(), QtGui.QLabel(), QtGui.QWidget() 에러
        buf = QtGui.QPixmap(os.path.join(addonPath, "control_module\Compressive_Spring_Properties.jpg"))  #C 드라이브에 넣었음
        Imageview1 = QtGui.QLabel(ks)
        Imageview1.setPixmap(buf)
        Imageview1.resize(buf.width(), buf.height())
        Imageview1.move(0, 0)
        Imageview1.show()
        ks.setGeometry(750, 100, buf.width(), buf.height())
        ks.setWindowTitle(u"기어 재료의 기계적 성질")
        ks.show()
        ks.exec_()

    def onDesign1(self):
        if self.popup1.currentText() == u"(kW)":			# 제어 동력 대입
            power_kW = float(self.numericInput1.text())
        elif self.popup1.currentText() == u"(HP)":
            power_kW = 735.49875/1000*float(self.numericInput1.text())
        if self.popup2.currentText() == u"(rpm)":			# 제어 회전속력 대입
            rotation_rpm = float(self.numericInput2.text())
        elif self.popup2.currentText() == u"(rad/s)":
            rotation_rpm = 9.849296*float(self.numericInput2.text())
        if self.popup3.currentText() == u"(N)":				# 제어 슈에 걸리는 힘 대입
            force_shoe_N = float(self.numericInput3.text())
        elif self.popup3.currentText() == u"(lbf)":
            force_shoe_N = 4.44822*float(self.numericInput3.text())
        if self.popup4.currentText() == u"(mm)":			# 유압실린더 지름 대입
            dia_cyl_mm = float(self.numericInput4.text())
        elif self.popup4.currentText() == u"(inch)":
            dia_cyl_mm = 25.4*float(self.numericInput4.text())
        if self.popup5.currentText() == u"(mm)":			# 제어 레버의 치수(b) 대입
            length_b_mm = float(self.numericInput5.text())
        elif self.popup5.currentText() == u"(inch)":
            length_b_mm = 25.4*float(self.numericInput5.text())
        if self.popup6.currentText() == u"(mm)":			# 제어 레버의 치수(c) 대입
            length_c_mm = float(self.numericInput6.text())
        elif self.popup6.currentText() == u"(inch)":
            length_c_mm = 25.4*float(self.numericInput6.text())
        if self.popup7.currentText() == u"(mm)":			# 브레이크의 지름 대입
            dia_brake_mm = float(self.numericInput7.text())
        elif self.popup7.currentText() == u"(inch)":
            dia_brake_mm = 25.4*float(self.numericInput7.text())
        friction_coef = float(self.numericInput8.text())	# 마찰 계수 대입

        Torque_Nm = 9.549297*1000*power_kW/rotation_rpm
        force_friction_N = 1000*2*Torque_Nm/dia_brake_mm
        length_a_mm = force_friction_N*(length_b_mm + friction_coef*length_c_mm)*(length_b_mm - friction_coef*length_c_mm)/(2*force_shoe_N*friction_coef*length_b_mm)
        area_cyl_mm2 = math.pi*dia_cyl_mm*dia_cyl_mm/4
        prssure_cyl_MPa = force_shoe_N/area_cyl_mm2
        thick_brake_mm = dia_brake_mm/8
        theta_2_rad = math.asin(length_b_mm/(dia_brake_mm/2 - thick_brake_mm/2))
        thick_shoe_mm = length_c_mm - dia_brake_mm/2 + (dia_brake_mm/2 - thick_brake_mm/2)*math.cos(theta_2_rad)

        if self.popup9.currentText() == u"(N*m)":			# 제동 토크 대입
            self.numericInput9.setText(str(round(Torque_Nm,3)))
        elif self.popup9.currentText() == u"(lbf*inch)":
            Torque_lbfft = 1/(4.44822*3.28084)*Torque_Nm
            self.numericInput9.setText(str(round(Torque_lbfft,3)))
        if self.popup10.currentText() == u"(N)":			# 제동력 대입
            self.numericInput10.setText(str(round(force_friction_N,3)))
        elif self.popup10.currentText() == u"(lbf)":
            force_friction_lbf = 1/(4.44822*3.28084)*force_friction_N
            self.numericInput10.setText(str(round(force_friction_lbf,3)))
        if self.popup11.currentText() == u"(MPa)":			# 필요 유압 대입
            self.numericInput11.setText(str(round(prssure_cyl_MPa,3)))
        elif self.popup11.currentText() == u"(lbf)":
            prssure_cyl_ksi = 0.1450377*prssure_cyl_MPa
            self.numericInput11.setText(str(round(prssure_cyl_ksi,3)))
        if self.popup12.currentText() == u"(mm)":			# 레버의 치수(a) 대입
            self.numericInput12.setText(str(round(length_a_mm,3)))
        elif self.popup12.currentText() == u"(inch)":
            length_a_inch = 1/25.4*length_a_mm
            self.numericInput12.setText(str(round(length_a_inch,3)))
        if self.popup13.currentText() == u"(mm)":			# 레버의 치수 대입
            self.numericInput13.setText(str(round(thick_shoe_mm,3)))
        elif self.popup13.currentText() == u"(inch)":
            thick_shoe_inch = 1/25.4*thick_shoe_mm
            self.numericInput13.setText(str(round(thick_shoe_inch,3)))

    def onDesign2(self):
        if self.popup4.currentText() == u"(mm)":			# 제어 회전속력 대입
            dia_mm = float(self.numericInput4.text())
        elif self.popup4.currentText() == u"(inch)":
            dia_mm = 25.4*float(self.numericInput4.text())
        if self.popup5.currentText() == u"(mm)":				# 제어 슈에 걸리는 힘 대입
            Dia_mm = float(self.numericInput5.text())
        elif self.popup5.currentText() == u"(inch)":
            Dia_mm = 25.4*float(self.numericInput5.text())
        Na = float(self.numericInput6.text())

        if self.popup3.currentText() == u"(A227)":			# 제어 동력 대입
            m = 0.190
            A = 1783
            if dia_mm < 0.8:
                E_GPa = 198.6
                G_GPa = 80.7
            elif dia_mm >= 0.8 and dia_mm < 1.6:
                E_GPa = 197.9
                G_GPa = 80.0
            elif dia_mm >= 1.6 and dia_mm < 3.0:
                E_GPa = 197.2
                G_GPa = 79.3
            elif dia_mm >= 3.0:
                E_GPa = 196.5
                G_GPa = 78.6
        elif self.popup3.currentText() == u"(A228)":
            m = 0.145
            A = 2211
            if dia_mm < 0.8:
                E_GPa = 203.4
                G_GPa = 82.7
            elif dia_mm >= 0.8 and dia_mm < 1.6:
                E_GPa = 200.0
                G_GPa = 81.7
            elif dia_mm >= 1.6 and dia_mm < 3.0:
                E_GPa = 196.5
                G_GPa = 81.0
            elif dia_mm >= 3.0:
                E_GPa = 193.0
                G_GPa = 80.0
        elif self.popup3.currentText() == u"(A232)":
            m = 0.168
            A = 2005
            E_GPa = 203.4
            G_GPa = 77.2
        elif self.popup3.currentText() == u"(A313)":
            m = 0.146
            A = 1867
            E_GPa = 193.0
            G_GPa = 69.0
        elif self.popup3.currentText() == u"(A401)":
            m = 0.108
            A = 1974
            E_GPa = 203.4
            G_GPa = 77.2
        elif self.popup3.currentText() == u"(B159)":
            m = 0
            A = 1000
            E_GPa = 103.4
            G_GPa = 41.4

        C = Dia_mm/dia_mm # 스프링 변수
        KB = (4*C+2)/(4*C-3) #
        k = ((dia_mm**4)*1000*G_GPa)/(8*(Dia_mm**3)*Na) # 스프링 상수 N/mm
        Ssys_MPa = 0.577*0.45*A/(dia_mm**m)
        Fmax_N = math.pi*(dia_mm**3)*Ssys_MPa/(8*KB*Dia_mm)
        Ls_mm = (Na+1)*dia_mm
        Lo_mm = Fmax_N/k + Ls_mm
        pitch_mm = (Lo_mm - dia_mm)/Na

        if self.popup9.currentText() == u"(mm)":			# 최대 하중 대입
            self.numericInput9.setText(str(round(pitch_mm,3)))
        elif self.popup9.currentText() == u"(inch)":
            pitch_inch = 1/25.4*pitch_mm
            self.numericInput10.setText(str(round(pitch_inch,3)))
        if self.popup10.currentText() == u"(N)":			# 최대 하중 대입
            self.numericInput10.setText(str(round(Fmax_N,3)))
        elif self.popup10.currentText() == u"(lbf)":
            Fmax_lbf = 0.224809*Fmax_N
            self.numericInput10.setText(str(round(Fmax_lbf,3)))
        if self.popup11.currentText() == u"(mm)":			# 자유높이 대입
            self.numericInput11.setText(str(round(Lo_mm,3)))
        elif self.popup11.currentText() == u"(inch)":
            Ls_inch = 1/25.4*Ls_mm
            self.numericInput11.setText(str(round(Lo_inch,3)))
        if self.popup12.currentText() == u"(mm)":			# 밀착높이 대입
            self.numericInput12.setText(str(round(Ls_mm,3)))
        elif self.popup12.currentText() == u"(inch)":
            Lo_inch = 1/25.4*Lo_mm
            self.numericInput12.setText(str(round(Ls_inch,3)))
        if self.popup13.currentText() == u"(N/mm)":			# 제동력 대입
            self.numericInput13.setText(str(round(k,3)))
        elif self.popup13.currentText() == u"(lbf/inch)":
            k_lbfinch = 0.224809/0.0393701*k
            self.numericInput13.setText(str(round(k_lbfinch,3)))

    def onDesign3(self):
        if self.popup3.currentText() == u"(MPa)":			# 전단탄성계수 입력
            G_MPa = float(self.numericInput3.text())
        elif self.popup3.currentText() == u"(ksi)":
            G_MPa = 6.8947572931*float(self.numericInput3.text())
        if self.popup4.currentText() == u"(MPa)":			# 허용전단응력 입력
            tau_MPa = float(self.numericInput4.text())
        elif self.popup4.currentText() == u"(ksi)":
            tau_MPa = 6.8947572931*float(self.numericInput4.text())
        if self.popup5.currentText() == u"(N*mm)":			# 비틈림 모멘트 입력
            moment_Nmm = float(self.numericInput5.text())
        elif self.popup5.currentText() == u"(lbf*inch)":
            moment_Nmm =4.44822*25.4*float(self.numericInput5.text())
        if self.popup6.currentText() == u"(rad)":			# 비틀림 각 입력
            angle_rad = float(self.numericInput6.text())
        elif self.popup6.currentText() == u"(degree)":
            angle_rad = math.pi/180*float(self.numericInput6.text())

        dia_mm = ((16*moment_Nmm)/(math.pi*tau_MPa))**(0.33333)
        length_mm = (math.pi*angle_rad*(dia_mm**4)*G_MPa)/(32*moment_Nmm)
        energy_MPa = (tau_MPa**2)/(4*G_MPa)

        if self.popup9.currentText() == u"(mm)":			# 토션바 지름 대입
            self.numericInput9.setText(str(round(dia_mm,3)))
        elif self.popup9.currentText() == u"(inch)":
            dia_inch = 1/25.4*dia_mm
            self.numericInput9.setText(str(round(dia_inch,3)))
        if self.popup10.currentText() == u"(mm)":			# 토션바 길이 대입
            self.numericInput10.setText(str(round(length_mm,3)))
        elif self.popup10.currentText() == u"(inch)":
            length_inch = 1/24*length_mm
            self.numericInput10.setText(str(round(length_inch,3)))
        if self.popup11.currentText() == u"(N*mm/mm^3)":			# 단위 체적당 탄성 에너지 대입
            self.numericInput11.setText(str(round(energy_MPa,3)))
        elif self.popup11.currentText() == u"(1000*lbf*inch/inch^3)":
            energy_ksi = 0.1450377*energy_MPa
            self.numericInput11.setText(str(round(energy_ksi,3)))

    def onGenerate1(self):
        doc = App.newDocument()

        if self.popup4.currentText() == u"(mm)":			# 유압실린더의 지름 대입
            d1_mm = float(self.numericInput4.text())
        elif self.popup4.currentText() == u"(inch)":
            d1_mm = 25.4 * float(self.numericInput4.text())
        if self.popup5.currentText() == u"(mm)":			# 레버의 치수(b) 대입
            b_mm = float(self.numericInput5.text())
        elif self.popup5.currentText() == u"(inch)":
            b_mm = 25.4 * float(self.numericInput5.text())
        if self.popup6.currentText() == u"(mm)":			# 레버의 치수(c) 대입
            c_mm = float(self.numericInput6.text())
        elif self.popup6.currentText() == u"(inch)":
            c_mm = 25.4 * float(self.numericInput6.text())
        if self.popup7.currentText() == u"(mm)":			# 브레이크의 지름 대입
            D_mm = float(self.numericInput7.text())
        elif self.popup7.currentText() == u"(inch)":
            D_mm = 25.4 * float(self.numericInput7.text())
        if self.popup12.currentText() == u"(mm)":			# 레버의 치수(a) 대입
            a_mm = float(self.numericInput12.text())
        elif self.popup12.currentText() == u"(inch)":
            a_mm = 25.4 * float(self.numericInput12.text())
        if self.popup13.currentText() == u"(mm)":			# 슈의 두께 대입
            t2_mm = float(self.numericInput13.text())
        elif self.popup13.currentText() == u"(inch)":
            t2_mm = 25.4 * float(self.numericInput13.text())
        if self.popup14.currentText() == u"(mm)":			# 슈의 두께 대입
            h_mm = float(self.numericInput14.text())
        elif self.popup13.currentText() == u"(inch)":
            h_mm = 25.4 * float(self.numericInput14.text())

        r_mm  = D_mm/2											# 반지름 계산
        t1_mm = r_mm/4											# 드럼 브레이크의 두께 계산
        d2_mm = t1_mm/2											# 드럼 브레이크를 고정하는 볼트의 지름 계산
        L_mm  = r_mm - t1_mm/2										#  계산
        theta1_rad = math.asin(b_mm/L_mm)						# 사이각 계산
        theta2_rad = math.asin(a_mm/L_mm - math.sin(theta1_rad))# 사이각 계산
        l_mm  = 2*L_mm*math.cos(theta1_rad)						# 유압 실린더의 길이 계산
        t2_mm = c_mm - r_mm + L_mm*math.cos(theta2_rad)			# 드럼 브레이크의 두께 계산

        p1  = Base.Vector(L_mm*math.cos(theta1_rad), L_mm*math.sin(theta1_rad), -h_mm/2)
        p2  = Base.Vector(L_mm*math.cos(theta2_rad), -L_mm*math.sin(theta2_rad), -h_mm/2)
        p3  = Base.Vector(L_mm*math.cos(theta1_rad), math.sqrt((r_mm - t1_mm)**2 - (L_mm*math.cos(theta1_rad))**2), -h_mm/2)
        p4  = Base.Vector(L_mm*math.cos(theta1_rad), math.sqrt((r_mm)**2 - (L_mm*math.cos(theta1_rad))**2), -h_mm/2)
        p5  = Base.Vector((L_mm - t1_mm/2)*math.cos(theta2_rad), -(L_mm - t1_mm/2)*math.sin(theta2_rad), -h_mm/2)
        p6  = Base.Vector((L_mm + t1_mm/2)*math.cos(theta2_rad), -(L_mm + t1_mm/2)*math.sin(theta2_rad), -h_mm/2)
        p7  = Base.Vector(r_mm, 0, -h_mm/2)
        p8  = Base.Vector(r_mm - t1_mm, 0, -h_mm/2)
        p9  = Base.Vector(L_mm*math.cos(theta2_rad) - t1_mm/2, -L_mm*math.sin(theta2_rad), -h_mm/2)
        p10 = Base.Vector(0, r_mm, -h_mm/2)
        p11 = Base.Vector((r_mm + t2_mm)*math.cos(theta1_rad - 0.1), (r_mm + t2_mm)*math.sin(theta1_rad - 0.1), -h_mm/2)
        p12 = Base.Vector(r_mm + t2_mm, 0, -h_mm/2)
        p13 = Base.Vector((r_mm + t2_mm)*math.cos(theta2_rad - 0.1), -(r_mm + t2_mm)*math.sin(theta2_rad - 0.1), -h_mm/2)
        p14 = Base.Vector((r_mm)*math.cos(theta1_rad - 0.1), (r_mm)*math.sin(theta2_rad - 0.1), -h_mm/2)
        p15 = Base.Vector(r_mm, 0, -h_mm/2)
        p16 = Base.Vector((r_mm)*math.cos(theta2_rad - 0.1), -(r_mm)*math.sin(theta2_rad - 0.1), -h_mm/2)

        C1 = Part.Arc(p3, p8, p5)
        C2 = Part.Arc(p4, p7, p6)
        C3 = Part.Arc(p5, p9, p6)
        L1 = Part.Line(p3, p4)
        S1 = Part.Shape([C1,C2,C3,L1])
        W1 = Part.Wire(S1.Edges)
        F1 = Part.Face(W1)
        P1 = F1.extrude(Base.Vector(0,0,h_mm))
        Cyl_hole = Part.makeCylinder(d2_mm/2, h_mm, p2, Base.Vector(0,0,1))
        P1 = P1.cut(Cyl_hole)

        CC1 = Part.Arc(p11, p12, p13)
        CC2 = Part.Arc(p14, p15, p16)
        LL1 = Part.Line(p11, p14)
        LL2 = Part.Line(p13, p16)
        SS1 = Part.Shape([CC1,CC2,LL1,LL2])
        WW1 = Part.Wire(SS1.Edges)
        FF1 = Part.Face(WW1)
        PP1 = FF1.extrude(Base.Vector(0,0,h_mm))
        P1 = P1.fuse(PP1)

        P2 = P1.copy()
        mhex = Base.Matrix()
        mhex.rotateY(math.radians(180.0))
        P1.transformShape(mhex)
        P1 = P1.fuse(P2)
        Cyl_pres = Part.makeCylinder(d1_mm/2, l_mm, Base.Vector(L_mm*math.cos(theta1_rad), L_mm*math.sin(theta1_rad), 0), Base.Vector(-1,0,0))
        P1 = P1.fuse(Cyl_pres)


        shape = doc.addObject("Part::Feature")  #Color
        shape.Shape = P1 #Color
        doc.recompute()  #Color
        shape.ViewObject.ShapeColor = (1.0, 1.0, 1.0)  #Color
        Gui.activeDocument().activeView().viewAxometric()  #View
        Gui.SendMsgToActiveView("ViewFit")  #View

    def onGenerate2(self):
        doc = App.newDocument()

        Na = float(self.numericInput6.text())
        if self.popup14.currentText() == u"(mm)":			# 유압실린더의 지름 대입
            dia_mm = float(self.numericInput14.text())
        elif self.popup14.currentText() == u"(inch)":
            dia_mm = 25.4 * float(self.numericInput14.text())
        if self.popup15.currentText() == u"(mm)":			# 레버의 치수(b) 대입
            Dia_mm = float(self.numericInput15.text())
        elif self.popup15.currentText() == u"(inch)":
            Dia_mm = 25.4 * float(self.numericInput15.text())
        if self.popup16.currentText() == u"(mm)":			# 레버의 치수(b) 대입
            pitch_mm = float(self.numericInput16.text())
        elif self.popup16.currentText() == u"(inch)":
            pitch_mm = 25.4 * float(self.numericInput16.text())

        C = Part.makeBox(20,20,20)
        Lo_mm = pitch_mm*Na + dia_mm
        edge1 = Part.Arc(Base.Vector(Dia_mm/2-dia_mm/2,0,0), Base.Vector(Dia_mm/2,0,dia_mm/2), Base.Vector(Dia_mm/2+dia_mm/2,0,0))
        edge2 = Part.Arc(Base.Vector(Dia_mm/2+dia_mm/2,0,0), Base.Vector(Dia_mm/2,0,-dia_mm/2), Base.Vector(Dia_mm/2-dia_mm/2,0,0))
        S = Part.Shape([edge1, edge2])
        section = Part.Wire(S.Edges)
        #circle = Part.makeCircle(dia_mm, Base.Vector(Dia_mm/2,0,0), Base.Vector(0,0,1))
        helix = Part.makeHelix(pitch_mm, Lo_mm, Dia_mm/2)  #Part.makeHelix(pitch,height,radius,(angle))
        makeSolid = bool(1)  #change to 1 to make a solid, but it will take a while
        isFrenet = bool(1)
        pipe = Part.Wire(helix).makePipeShell([section], makeSolid, isFrenet)

        shape = doc.addObject("Part::Feature")  #Color
        shape.Shape = pipe #Color
        doc.recompute()  #Color
        shape.ViewObject.ShapeColor = (1.0, 1.0, 1.0)  #Color
        Gui.activeDocument().activeView().viewAxometric()  #View
        Gui.SendMsgToActiveView("ViewFit")  #View

    def onGenerate3(self):
        doc = App.newDocument()

        if self.popup12.currentText() == u"(mm)":			# 유압실린더의 지름 대입
            dia_mm = float(self.numericInput12.text())
        elif self.popup4.currentText() == u"(inch)":
            dia_mm = 25.4 * float(self.numericInput12.text())
        if self.popup13.currentText() == u"(mm)":			# 레버의 치수(b) 대입
            length_mm = float(self.numericInput13.text())
        elif self.popup13.currentText() == u"(inch)":
            length_mm = 25.4 * float(self.numericInput13.text())

        Cylinder = Part.makeCylinder(dia_mm, length_mm)

        shape = doc.addObject("Part::Feature")  #Color
        shape.Shape = Cylinder #Color
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
