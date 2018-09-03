# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ED_Truss\trussCreatorGui.ui'
#
# Created: Sun Oct 29 13:03:54 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 420)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.coordTable = QtGui.QTableWidget(self.centralwidget)
        self.coordTable.setGeometry(QtCore.QRect(30, 110, 350, 211))
        self.coordTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.coordTable.setObjectName("coordTable")
        self.coordTable.setColumnCount(0)
        self.coordTable.setRowCount(0)
        self.select_2d = QtGui.QRadioButton(self.centralwidget)
        self.select_2d.setGeometry(QtCore.QRect(140, 56, 37, 16))
        self.select_2d.setObjectName("select_2d")
        self.select_3d = QtGui.QRadioButton(self.centralwidget)
        self.select_3d.setGeometry(QtCore.QRect(185, 56, 37, 16))
        self.select_3d.setObjectName("select_3d")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 67, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 72, 12))
        self.label_4.setObjectName("label_4")
        self.makePoints = QtGui.QPushButton(self.centralwidget)
        self.makePoints.setGeometry(QtCore.QRect(30, 340, 90, 25))
        self.makePoints.setObjectName("makePoints")
        self.numOfPoints = QtGui.QLineEdit(self.centralwidget)
        self.numOfPoints.setGeometry(QtCore.QRect(140, 25, 51, 20))
        self.numOfPoints.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.numOfPoints.setObjectName("numOfPoints")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 80, 12))
        self.label.setObjectName("label")
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(400, 30, 20, 370))
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 30, 61, 12))
        self.label_2.setObjectName("label_2")
        self.exampleList = QtGui.QListWidget(self.centralwidget)
        self.exampleList.setGeometry(QtCore.QRect(430, 50, 180, 150))
        self.exampleList.setObjectName("exampleList")
        QtGui.QListWidgetItem(self.exampleList)
        QtGui.QListWidgetItem(self.exampleList)
        self.makeExample = QtGui.QPushButton(self.centralwidget)
        self.makeExample.setGeometry(QtCore.QRect(430, 210, 100, 25))
        self.makeExample.setObjectName("makeExample")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "EdisonDesigner - 2D/3D Truss creator", None, QtGui.QApplication.UnicodeUTF8))
        self.select_2d.setText(QtGui.QApplication.translate("MainWindow", "2D", None, QtGui.QApplication.UnicodeUTF8))
        self.select_3d.setText(QtGui.QApplication.translate("MainWindow", "3D", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Select type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Coordinates:", None, QtGui.QApplication.UnicodeUTF8))
        self.makePoints.setText(QtGui.QApplication.translate("MainWindow", "Create points", None, QtGui.QApplication.UnicodeUTF8))
        self.numOfPoints.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Num. of point:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Examples:", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.exampleList.isSortingEnabled()
        self.exampleList.setSortingEnabled(False)
        self.exampleList.item(0).setText(QtGui.QApplication.translate("MainWindow", "35 bar truss", None, QtGui.QApplication.UnicodeUTF8))
        self.exampleList.item(1).setText(QtGui.QApplication.translate("MainWindow", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.exampleList.setSortingEnabled(__sortingEnabled)
        self.makeExample.setText(QtGui.QApplication.translate("MainWindow", "Create example", None, QtGui.QApplication.UnicodeUTF8))
