# -*- coding: utf-8 -*-
__author__ = 'Youngki'

import sys, os
from PySide import QtGui, QtCore

import trussCreatorGui
import Examples.examples

# EdisonDesigner
import ED, EDGui, Part, PartGui
from ED import Base


class TrussCreator(QtGui.QMainWindow, trussCreatorGui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(TrussCreator, self).__init__(parent)
        self.setupUi(self)
        self.move(100, 100)
        self.show()

        self.select_2d.toggled.connect(self.check2D)
        self.select_3d.toggled.connect(self.check3D)

        self.makePoints.clicked.connect(self.createPoints)

        self.exampleList.itemDoubleClicked.connect(self.onPopupImg)

        self.makeExample.clicked.connect(self.createExample)

    def check2D(self):
        self.coordTable.setColumnCount(0)
        self.coordTable.setColumnCount(3)
        self.coordTable.setHorizontalHeaderLabels(['X', 'Y', 'Select points'])
        for i in range(2):
            self.coordTable.setColumnWidth(i, 70)

        header = self.coordTable.horizontalHeader()
        header.setResizeMode(2, QtGui.QHeaderView.ResizeToContents)

        self.initTable()

    def check3D(self):
        self.coordTable.setColumnCount(0)
        self.coordTable.setColumnCount(4)
        self.coordTable.setHorizontalHeaderLabels(['X', 'Y', 'Z', 'Select points'])
        for i in range(3):
            self.coordTable.setColumnWidth(i, 70)

        header = self.coordTable.horizontalHeader()
        header.setResizeMode(3, QtGui.QHeaderView.ResizeToContents)

        self.initTable()

    def initTable(self):
        num = int(self.numOfPoints.text())
        self.coordTable.setRowCount(num)

        # set checkbox
        for itr in range(num):
            cell_widget = QtGui.QWidget()
            chk_bx = QtGui.QCheckBox()
            chk_bx.setCheckState(QtCore.Qt.Unchecked)
            lay_out = QtGui.QHBoxLayout(cell_widget)
            lay_out.addWidget(chk_bx)
            lay_out.setAlignment(QtCore.Qt.AlignCenter)
            lay_out.setContentsMargins(0, 0, 0, 0)
            cell_widget.setLayout(lay_out)

            if self.select_2d.isChecked():
                self.coordTable.setCellWidget(itr, 2, cell_widget)
            elif self.select_3d.isChecked():
                self.coordTable.setCellWidget(itr, 3, cell_widget)

    def createPoints(self):
        num = int(self.numOfPoints.text())

        for i in range(num):
            if self.select_2d.isChecked():
                vertex = "vertex_" + str(i)
                App.ActiveDocument.addObject("Part::Vertex", vertex)
                self.createPoint("2d", i, vertex)

            elif self.select_3d.isChecked():
                vertex = "vertex_" + str(i)
                App.ActiveDocument.addObject("Part::Vertex", vertex)
                self.createPoint("3d", i, vertex)

    def createPoint(self, flag, row, vertexName):
        if flag == "2d":
            obj = App.ActiveDocument.getObject(vertexName)
            obj.X = self.coordTable.item(row, 0).text()
            obj.Y = self.coordTable.item(row, 1).text()
            obj.Z = 0.0

        if flag == "3d":
            obj = App.ActiveDocument.getObject(vertexName)
            obj.X = self.coordTable.item(row, 0).text()
            obj.Y = self.coordTable.item(row, 1).text()
            obj.Z = self.coordTable.item(row, 2).text()

        obj.Placement = Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))

        docName = App.ActiveDocument.Name
        obj = EDGui.getDocument(docName).getObject(vertexName)
        obj.PointSize = 10

        App.ActiveDocument.recompute()
        Gui.SendMsgToActiveView("ViewFit")

    def onPopupImg(self):
        dlg = QtGui.QDialog()
        dlg.setWindowTitle(self.exampleList.currentItem().text())

        progDir = os.getcwd()
        imgDir = progDir + "/Addons/Examples/"

        if self.exampleList.currentItem().text() == "35 bar truss":
            pixmap = QtGui.QPixmap(imgDir + "35_Bar_Truss.png")
        elif self.exampleList.currentItem().text() == "Test":
            pixmap = QtGui.QPixmap(imgDir + "Test.jpg")

        image = QtGui.QLabel(dlg)
        image.setPixmap(pixmap)
        image.resize(pixmap.width(), pixmap.height())
        dlg.move(750, 100)
        dlg.show()
        dlg.exec_()

    def createExample(self):
        if self.exampleList.currentItem().text() == "35 bar truss":
            Examples.examples.make_35_bar(App)


app = TrussCreator()
'''
def main():
    app = QtGui.QApplication(sys.argv)
    form = TrussCreator()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
'''
