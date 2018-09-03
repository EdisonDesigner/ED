__author__ = 'Youngki'

# import statement
import sys
from PySide import QtGui, QtCore

#-- For EdisonDesigner macro --#
import FreeCAD as ED
import Sketcher, PartDesign, Part
import Part, PartGui
from FreeCAD import Base
#------------------------------#

import time
import datetime as dttm

import os
addonPath = os.path.dirname(os.path.abspath(__file__))

class L_type_model(QtGui.QWidget):
	def __init__(self):
		super(L_type_model, self).__init__()
		self.initUI()

	def initUI(self):

		# Set main window
		#self.resize(830, 450)		# initialize size
		self.setMinimumWidth(1000)
		self.setMinimumHeight(720)	# limit window size
		#self.setFixedWidth(830)
		#self.setFixedHeight(510)
		self.setWindowIcon(QtGui.QIcon(os.path.join(addonPath, "L-shape bracket modeler\EdisonDesigner_icon.png")))	# icon setting
		self.setWindowTitle('EdisonDesigner L-shape bracket modeler v 0.3.2')

		# Set a background image
		Background = QtGui.QPalette()
		Background.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap(os.path.join(addonPath, "L-shape bracket modeler\Background image.png"))))



# --------------- Objects in model selection group box --------------- #

		model_sel_GroupBox = QtGui.QGroupBox(self)
		model_sel_GroupBox.setGeometry(QtCore.QRect(30, 30, 260, 60))
		model_sel_GroupBox.setTitle('Model selection')

		# Locate widget for radio button, Surface model
		surfaceModel = QtGui.QRadioButton(model_sel_GroupBox)
		surfaceModel.setGeometry(QtCore.QRect(20, 25, 110, 20))
		surfaceModel.setText('Surface model')

		# Locate widget for radio button, Solid model
		solidModel = QtGui.QRadioButton(model_sel_GroupBox)
		solidModel.setGeometry(QtCore.QRect(150, 25, 90, 20))
		solidModel.setText('Solid model')

# --------------- Design parameters groupbox ------------------#

		# Set group box for Design parameter group box
		DesignParaGroupBox = QtGui.QGroupBox(self)
		DesignParaGroupBox.setGeometry(QtCore.QRect(30, model_sel_GroupBox.height() + 60, 220, 350))
		DesignParaGroupBox.setTitle('Design parameters')

		# Set grid widget in a groupbox of design parameters
		gridParaWidget = QtGui.QWidget(DesignParaGroupBox)
		gridParaWidget.setGeometry(QtCore.QRect(20, 30, 180, 190))

		# Set grid layout in a groupbox of design parameters
		gridLayout = QtGui.QGridLayout(gridParaWidget)
		gridLayout.setSpacing(10)
		gridLayout.setContentsMargins(5, 5, 5, -1)

# --------------- Document name group box --------------- #

		# 2016. 5. 5 modified
		docName_Group = QtGui.QGroupBox(self)
		docName_Group.setGeometry(QtCore.QRect(330, 30, 350, 60))
		docName_Group.setTitle('Document name')

		docName_Label = QtGui.QLabel('Write a file name :', docName_Group)
		docName_Label.setGeometry(QtCore.QRect(20, 20, 120, 25))

		self.docName_LineEdit = QtGui.QLineEdit(docName_Group)
		self.docName_LineEdit.setGeometry(QtCore.QRect((docName_Label.width() + 10), 20, 200, 25))

# --------------- Objects in Design parameters group box --------------- #

		# Locate widget for parameter, length 1
		# Length 1 object - label
		length_1_label = QtGui.QLabel('L1 :', gridParaWidget)
		gridLayout.addWidget(length_1_label, 0, 0, 1, 1)

		# Length 1 object - Line edit
		self.length_1_LineEdit = QtGui.QLineEdit(gridParaWidget)
		gridLayout.addWidget(self.length_1_LineEdit, 0, 1, 1, 1)
		self.length_1_LineEdit.setText('100')						# set default value
		self.length_1_LineEdit.setAlignment(QtCore.Qt.AlignRight)


		L1_mm_label = QtGui.QLabel('mm', gridParaWidget)
		gridLayout.addWidget(L1_mm_label, 0, 2, 1, 1)

		# ------------------------------------------------------- #

		# Locate widget for parameter, length 2
		# Length 2 object - label
		length_2_label = QtGui.QLabel('L2 :', gridParaWidget)
		gridLayout.addWidget(length_2_label, 1, 0, 1, 1)

		# Length 1 object - Line edit
		self.length_2_LineEdit = QtGui.QLineEdit(gridParaWidget)
		gridLayout.addWidget(self.length_2_LineEdit, 1, 1, 1, 1)
		self.length_2_LineEdit.setText('100')						# set default value
		self.length_2_LineEdit.setAlignment(QtCore.Qt.AlignRight)

		L2_mm_label = QtGui.QLabel('mm', gridParaWidget)
		gridLayout.addWidget(L2_mm_label, 1, 2, 1, 1)

		# ------------------------------------------------------- #

		# Locate widget for parameter, d of support structure
		# d of support structure object - label
		support_d_label = QtGui.QLabel('d  :', gridParaWidget)
		gridLayout.addWidget(support_d_label, 2, 0, 1, 1)

		# d of support structure object - Line edit
		self.support_d_LineEdit = QtGui.QLineEdit(gridParaWidget)
		gridLayout.addWidget(self.support_d_LineEdit, 2, 1, 1, 1)
		self.support_d_LineEdit.setText('35')						# set default value
		self.support_d_LineEdit.setAlignment(QtCore.Qt.AlignRight)

		support_d_mm_label = QtGui.QLabel('mm', gridParaWidget)
		gridLayout.addWidget(support_d_mm_label, 2, 2, 1, 1)

		# ------------------------------------------------------- #

		# Locate widget for parameter, h of support structure
		# h of support structure object - label
		support_h_label = QtGui.QLabel('h  :', gridParaWidget)
		gridLayout.addWidget(support_h_label, 3, 0, 1, 1)

		# d of support structure object - Line edit
		self.support_h_LineEdit = QtGui.QLineEdit(gridParaWidget)
		gridLayout.addWidget(self.support_h_LineEdit, 3, 1, 1, 1)
		self.support_h_LineEdit.setText('35')						# set default value
		self.support_h_LineEdit.setAlignment(QtCore.Qt.AlignRight)

		support_h_mm_label = QtGui.QLabel('mm', gridParaWidget)
		gridLayout.addWidget(support_h_mm_label, 3, 2, 1, 1)

		# ------------------------------------------------------- #

		# Locate widget for parameter, Radius 1
		# Radius 1 object - label
		radius_1_label = QtGui.QLabel('r1 :', gridParaWidget)
		gridLayout.addWidget(radius_1_label, 4, 0, 1, 1)

		# Radius 1 object - Line edit
		self.radius_1_LineEdit = QtGui.QLineEdit(gridParaWidget)
		gridLayout.addWidget(self.radius_1_LineEdit, 4, 1, 1, 1)
		self.radius_1_LineEdit.setText('10')						# set default value
		self.radius_1_LineEdit.setAlignment(QtCore.Qt.AlignRight)

		radius_1_mm_label = QtGui.QLabel('mm', gridParaWidget)
		gridLayout.addWidget(radius_1_mm_label, 4, 2, 1, 1)

		# ------------------------------------------------------- #

		# Locate widget for parameter, Radius 2
		# Radius 1 object - label
		radius_2_label = QtGui.QLabel('r2 :', gridParaWidget)
		gridLayout.addWidget(radius_2_label, 5, 0, 1, 1)

		# Radius 1 object - Line edit
		self.radius_2_LineEdit = QtGui.QLineEdit(gridParaWidget)
		gridLayout.addWidget(self.radius_2_LineEdit, 5, 1, 1, 1)
		self.radius_2_LineEdit.setText('10')						# set default value
		self.radius_2_LineEdit.setAlignment(QtCore.Qt.AlignRight)

		radius_2_mm_label = QtGui.QLabel('mm', gridParaWidget)
		gridLayout.addWidget(radius_2_mm_label, 5, 2, 1, 1)

		# ---------- For solid model group box ---------- #

		Solid_model_groupbox = QtGui.QGroupBox(DesignParaGroupBox)
		Solid_model_groupbox.setGeometry(QtCore.QRect(20, 240, 180, 100))
		Solid_model_groupbox.setTitle('For Solid model')

		Solid_model_para_Widget = QtGui.QWidget(Solid_model_groupbox)
		Solid_model_para_Widget.setGeometry(QtCore.QRect(10, 30, 160, 60))

		Solid_model_para_grid = QtGui.QGridLayout(Solid_model_para_Widget)
		Solid_model_para_grid.setContentsMargins(5, 5, 5, 5)
		Solid_model_para_grid.setSpacing(10)

		# Locate widget for parameter, thickness 1 for solid model
		# thickness 1 for solid model object - label
		thk_1_label = QtGui.QLabel('t1 :', gridParaWidget)
		Solid_model_para_grid.addWidget(thk_1_label, 0, 0, 1, 1)

		self.thk_1_LineEdit = QtGui.QLineEdit(Solid_model_para_Widget)
		Solid_model_para_grid.addWidget(self.thk_1_LineEdit, 0, 1, 1, 1)
		self.thk_1_LineEdit.setAlignment(QtCore.Qt.AlignRight)

		thk_1_label = QtGui.QLabel('mm', Solid_model_para_Widget)
		Solid_model_para_grid.addWidget(thk_1_label, 0, 2, 1, 1)

		# Locate widget for parameter, thickness 2 for solid model
		# thickness 2 for solid model object - label
		thk_2_label = QtGui.QLabel('t2 :', gridParaWidget)
		Solid_model_para_grid.addWidget(thk_2_label, 1, 0, 1, 1)

		self.thk_2_LineEdit = QtGui.QLineEdit(Solid_model_para_Widget)
		Solid_model_para_grid.addWidget(self.thk_2_LineEdit, 1, 1, 1, 1)
		self.thk_2_LineEdit.setAlignment(QtCore.Qt.AlignRight)

		thk_2_label = QtGui.QLabel('mm', Solid_model_para_Widget)
		Solid_model_para_grid.addWidget(thk_2_label, 1, 2, 1, 1)

# --------------- Reference images group box --------------- #

		# Set group box for reference image section
		refer_Img_GroupBox = QtGui.QGroupBox(self)
		refer_Img_GroupBox.setGeometry(QtCore.QRect(270, 110, 630, 350))
		refer_Img_GroupBox.setTitle('Reference images')

		# Set reference image in reference image section
		side_View_Img = QtGui.QPixmap(os.path.join(addonPath, "L-shape bracket modeler\L-shape bracket_3D_model_view.png"))
		side_View_label = QtGui.QLabel(refer_Img_GroupBox)
		side_View_label.setPixmap(side_View_Img)
		side_View_label.resize(side_View_Img.width(), side_View_Img.height())
		side_View_label.move(10, 20)

		model_3D_View_Img = QtGui.QPixmap(os.path.join(addonPath, "L-shape bracket modeler\L-shape bracket_side_view.png"))
		model_3D_View_label = QtGui.QLabel(refer_Img_GroupBox)
		model_3D_View_label.setPixmap(model_3D_View_Img)
		model_3D_View_label.resize(model_3D_View_Img.width(), model_3D_View_Img.height())
		model_3D_View_label.move(side_View_Img.width() + 30, 20)


# --------------- Push buttons --------------- #

		# Generation buttons, Generate surface model
		Gen_surf_model = QtGui.QPushButton(self)
		Gen_surf_model.setGeometry(QtCore.QRect(30, 480, 220, 40))
		Gen_surf_model.setText('Generate surface model')
		Gen_surf_model.clicked.connect(self.make_surface_model)

		# Generation buttons, Generate solid model
		Gen_solid_model = QtGui.QPushButton( self)
		Gen_solid_model.setGeometry(QtCore.QRect(30, 530, 220, 40))
		Gen_solid_model.setText('Generate solid model')
		Gen_solid_model.clicked.connect(self.make_solid_model)

# --------------- Save path and Export a model --------------- #

		# Save a model
		Save_dir_path = QtGui.QLabel('Save directory path', self)
		Save_dir_path.setGeometry(QtCore.QRect(30, 600, 120, 25))

		self.dir_path_LineEdit = QtGui.QLineEdit(self)
		self.dir_path_LineEdit.setGeometry(QtCore.QRect(160, 600, 550, 25))

		dir_path_sel = QtGui.QPushButton(self)
		dir_path_sel.setGeometry(QtCore.QRect(720, 605, 41, 20))
		dir_path_sel.setText('...')
		dir_path_sel.clicked.connect(self.getDir)

		# ---------- Export a model to IGES and STEP ---------- #

		Export_IGES = QtGui.QPushButton(self)
		Export_IGES.setGeometry(QtCore.QRect(30, 640, 110, 30))
		Export_IGES.setText('Export to IGES')
		Export_IGES.clicked.connect(self.export2IGES)

		Export_STEP = QtGui.QPushButton(self)
		Export_STEP.setGeometry(QtCore.QRect(150, 640, 110, 30))
		Export_STEP.setText('Export to STEP')
		Export_STEP.clicked.connect(self.export2STEP)

# --------------- Exit a program --------------- #

		Exit_button = QtGui.QPushButton(self)
		Exit_button.setGeometry(QtCore.QRect(850, 640, 110, 30))
		Exit_button.setText('Close')
		Exit_button.clicked.connect(self.close_program)

		self.setPalette(Background)
		self.show()

	def make_solid_model(self):

		# 2016. 5. 5 modified

		# Create a new document
		docName = self.docName_LineEdit.text()
		ED.newDocument(docName)

		# Set input parameters
		t1 = float(self.thk_1_LineEdit.text())
		t2 = float(self.thk_2_LineEdit.text())
		l1 = float(self.length_1_LineEdit.text())
		l2 = float(self.length_2_LineEdit.text())
		r1 = float(self.radius_1_LineEdit.text())
		r2 = float(self.radius_2_LineEdit.text())
		h  = float(self.support_h_LineEdit.text())
		d  = float(self.support_d_LineEdit.text())


		# Create a new sketch for a main frame
		ED.activeDocument().addObject('Sketcher::SketchObject','Main_frame_sketch')
		ED.activeDocument().Main_frame_sketch.Placement = ED.Placement(ED.Vector(0.000000,0.000000,0.000000),ED.Rotation(0.000000,0.000000,0.000000,1.000000))

		# Draw lines
		ED.ActiveDocument.Main_frame_sketch.addGeometry(Part.Line(ED.Vector(0.0, 0.0, 0), ED.Vector(100.0, 0.0, 0)))
		ED.ActiveDocument.Main_frame_sketch.addGeometry(Part.Line(ED.Vector(100.0, 0.0, 0), ED.Vector(100.0, t1, 0)))
		ED.ActiveDocument.Main_frame_sketch.addGeometry(Part.Line(ED.Vector(100.0, t1, 0), ED.Vector(t2, t1, 0)))
		ED.ActiveDocument.Main_frame_sketch.addGeometry(Part.Line(ED.Vector(t2, t1, 0), ED.Vector(t2, 100.0, 0)))
		ED.ActiveDocument.Main_frame_sketch.addGeometry(Part.Line(ED.Vector(t2, 100.0, 0), ED.Vector(0.0, 100.0, 0)))
		ED.ActiveDocument.Main_frame_sketch.addGeometry(Part.Line(ED.Vector(0.0, 100.0, 0), ED.Vector(0.0, 0.0, 0)))

		# Create a Pad feature using above sketch(Main_frame_sketch)
		ED.activeDocument().addObject("PartDesign::Pad", "Main_frame")
		ED.activeDocument().Main_frame.Sketch = ED.activeDocument().Main_frame_sketch
		ED.activeDocument().Main_frame.Length = 40.0
		ED.activeDocument().Main_frame.Midplane = 1		# Midplane = 1 : use a symmetric pad feature

		Gui.getDocument(docName).getObject("Main_frame_sketch").Visibility=False		# Hide a sketch
		ED.activeDocument().recompute()

		# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

		# Create a new sketch for a cut(pocket)
		ED.activeDocument().addObject('Sketcher::SketchObject','cut_sketch_1')
		ED.activeDocument().cut_sketch_1.Placement = ED.Placement(ED.Vector(0.000000,0.000000,0.000000),ED.Rotation(0.500000,0.500000,0.500000,0.500000))
		ED.ActiveDocument.cut_sketch_1.addGeometry(Part.Circle(ED.Vector(70.0, 0.0, 0.0), ED.Vector(0.0, 0.0, 1.0), r1))		# A third parameter is a r1 value from input value
		#0.500000,0.500000,0.500000,0.500000
		# Create a Pad feature using above sketch(cut_sketch_1)
		ED.activeDocument().addObject("PartDesign::Pad", "Pad_for_cut_1")
		ED.activeDocument().Pad_for_cut_1.Sketch = ED.activeDocument().cut_sketch_1
		ED.activeDocument().Pad_for_cut_1.Length = t2	# This parameter is a t1 value from input value
		#ED.activeDocument().Pad_for_cut_1.Reversed = 1

		Gui.getDocument(docName).getObject("cut_sketch_1").Visibility=False		# Hide a sketch
		ED.activeDocument().recompute()

		# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

		# Create a new sketch for a cut(pocket)
		ED.activeDocument().addObject('Sketcher::SketchObject','cut_sketch_2')
		ED.activeDocument().cut_sketch_2.Placement = ED.Placement(ED.Vector(0.000000,0.000000,0.000000),ED.Rotation(-0.707107,0.000000,0.000000,-0.707107))
		ED.ActiveDocument.cut_sketch_2.addGeometry(Part.Circle(ED.Vector(70.0, 0.0, 0.0), ED.Vector(0.0, 0.0, 1.0), r2))		# A third parameter is a r2 value from input value

		# Create a Pad feature using above sketch(cut_sketch_2)
		ED.activeDocument().addObject("PartDesign::Pad", "Pad_for_cut_2")
		ED.activeDocument().Pad_for_cut_2.Sketch = ED.activeDocument().cut_sketch_2
		ED.activeDocument().Pad_for_cut_2.Length = t1		# This parameter is a t1 value from input value
		ED.activeDocument().Pad_for_cut_2.Reversed = 1

		Gui.getDocument(docName).getObject("cut_sketch_2").Visibility=False		# Hide a sketch
		ED.activeDocument().recompute()

		# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

		# Create a new sketch for a support structure
		ED.activeDocument().addObject('Sketcher::SketchObject','Support_sketch')
		ED.activeDocument().Support_sketch.Placement = ED.Placement(ED.Vector(0.000000,0.000000,0.000000),ED.Rotation(0.000000,0.000000,0.000000,1.000000))

		# Draw lines
		ED.ActiveDocument.Support_sketch.addGeometry(Part.Line(ED.Vector(t1, t1, 0), ED.Vector(t1 + d, t1, 0)))		# First parameter(t1, t1, 0), second parameter(t1+d, t1, 0)
		ED.ActiveDocument.Support_sketch.addGeometry(Part.Line(ED.Vector(t1 + d, t1, 0), ED.Vector(t1, t1 + h, 0)))		# First parameter(t1+d, t1, 0), second parameter(t1, t1+h, 0)
		ED.ActiveDocument.Support_sketch.addGeometry(Part.Line(ED.Vector(t1, t1 + h, 0), ED.Vector(t1, t1, 0)))		# First parameter(t1, t1+h, 0), second parameter(t1, t1, 0)

		# Create a Pad feature using above sketch(Support_sketch)
		ED.activeDocument().addObject("PartDesign::Pad", "Support_structure")
		ED.activeDocument().Support_structure.Sketch = ED.activeDocument().Support_sketch
		ED.activeDocument().Support_structure.Length = t2		# This value is a t2/2 value
		ED.activeDocument().Support_structure.Midplane = 1		# Midplane = 1 : use a symmetric pad feature

		Gui.getDocument(docName).getObject("Support_sketch").Visibility=False		# Hide a sketch
		ED.activeDocument().recompute()

		# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

		# Conduct boolean operation
		ED.activeDocument().addObject("Part::Cut", "Main_frame_with_Pad_for_cut_1")
		ED.activeDocument().Main_frame_with_Pad_for_cut_1.Base = ED.activeDocument().Main_frame
		ED.activeDocument().Main_frame_with_Pad_for_cut_1.Tool = ED.activeDocument().Pad_for_cut_1

		ED.activeDocument().addObject("Part::Cut", "Main_frame_with_Pad_for_cut_2")
		ED.activeDocument().Main_frame_with_Pad_for_cut_2.Base = ED.activeDocument().Main_frame_with_Pad_for_cut_1
		ED.activeDocument().Main_frame_with_Pad_for_cut_2.Tool = ED.activeDocument().Pad_for_cut_2

		ED.activeDocument().addObject("Part::MultiFuse", "L_type_model")
		ED.activeDocument().L_type_model.Shapes = [ED.activeDocument().Main_frame_with_Pad_for_cut_2, ED.activeDocument().Support_structure,]

		ED.ActiveDocument.recompute()

		self.doc = ED.getDocument(docName)

	def make_surface_model(self):
		# Create a new document
		docName = self.docName_LineEdit.text()
		ED.newDocument(docName)
		#ED.newDocument("L_type_model")

		# Set input parameters
		l1 = float(self.length_1_LineEdit.text())
		l2 = float(self.length_2_LineEdit.text())
		r1 = float(self.radius_1_LineEdit.text())
		r2 = float(self.radius_2_LineEdit.text())
		h  = float(self.support_h_LineEdit.text())
		d  = float(self.support_d_LineEdit.text())

		# Draw lines
		ED.ActiveDocument.addObject("Part::Line", "Bottom_Line1")
		ED.ActiveDocument.Bottom_Line1.X1 = 0.0
		ED.ActiveDocument.Bottom_Line1.Y1 = 0.0
		ED.ActiveDocument.Bottom_Line1.Z1 = 0.0
		ED.ActiveDocument.Bottom_Line1.X2 = l1
		ED.ActiveDocument.Bottom_Line1.Y2 = 0.0
		ED.ActiveDocument.Bottom_Line1.Z2 = 0.0

		ED.ActiveDocument.addObject("Part::Line", "Bottom_Line2")
		ED.ActiveDocument.Bottom_Line2.X1 = ED.ActiveDocument.Bottom_Line1.X2
		ED.ActiveDocument.Bottom_Line2.Y1 = ED.ActiveDocument.Bottom_Line1.Y2
		ED.ActiveDocument.Bottom_Line2.Z1 = ED.ActiveDocument.Bottom_Line1.Z2
		ED.ActiveDocument.Bottom_Line2.X2 = l1
		ED.ActiveDocument.Bottom_Line2.Y2 = 0.0
		ED.ActiveDocument.Bottom_Line2.Z2 = 20.0

		ED.ActiveDocument.addObject("Part::Line", "Bottom_Line3")
		ED.ActiveDocument.Bottom_Line3.X1 = ED.ActiveDocument.Bottom_Line2.X2
		ED.ActiveDocument.Bottom_Line3.Y1 = ED.ActiveDocument.Bottom_Line2.Y2
		ED.ActiveDocument.Bottom_Line3.Z1 = ED.ActiveDocument.Bottom_Line2.Z2
		ED.ActiveDocument.Bottom_Line3.X2 = d
		ED.ActiveDocument.Bottom_Line3.Y2 = 0.0
		ED.ActiveDocument.Bottom_Line3.Z2 = 20.0

		ED.ActiveDocument.addObject("Part::Line", "Bottom_Line4")
		ED.ActiveDocument.Bottom_Line4.X1 = ED.ActiveDocument.Bottom_Line3.X2
		ED.ActiveDocument.Bottom_Line4.Y1 = ED.ActiveDocument.Bottom_Line3.Y2
		ED.ActiveDocument.Bottom_Line4.Z1 = ED.ActiveDocument.Bottom_Line3.Z2
		ED.ActiveDocument.Bottom_Line4.X2 = 0.0
		ED.ActiveDocument.Bottom_Line4.Y2 = 0.0
		ED.ActiveDocument.Bottom_Line4.Z2 = 20.0

		ED.ActiveDocument.addObject("Part::Line", "Bottom_Line5")
		ED.ActiveDocument.Bottom_Line5.X1 = ED.ActiveDocument.Bottom_Line4.X2
		ED.ActiveDocument.Bottom_Line5.Y1 = ED.ActiveDocument.Bottom_Line4.Y2
		ED.ActiveDocument.Bottom_Line5.Z1 = ED.ActiveDocument.Bottom_Line4.Z2
		ED.ActiveDocument.Bottom_Line5.X2 = 0.0
		ED.ActiveDocument.Bottom_Line5.Y2 = 0.0
		ED.ActiveDocument.Bottom_Line5.Z2 = 0.0

		# Make a surface
		_=Part.makeFilledFace(Part.__sortEdges__(
			[ED.ActiveDocument.Bottom_Line1.Shape.Edge1,
			 ED.ActiveDocument.Bottom_Line2.Shape.Edge1,
			 ED.ActiveDocument.Bottom_Line3.Shape.Edge1,
			 ED.ActiveDocument.Bottom_Line4.Shape.Edge1,
			 ED.ActiveDocument.Bottom_Line5.Shape.Edge1, ]))

		ED.ActiveDocument.addObject('Part::Feature','BottomFace1').Shape=_

		ED.ActiveDocument.recompute()

		# Hide lines
		Gui.getDocument(docName).getObject("Bottom_Line1").Visibility=False
		Gui.getDocument(docName).getObject("Bottom_Line2").Visibility=False
		Gui.getDocument(docName).getObject("Bottom_Line3").Visibility=False
		Gui.getDocument(docName).getObject("Bottom_Line4").Visibility=False
		Gui.getDocument(docName).getObject("Bottom_Line5").Visibility=False

		# ------------------------------------------------------------------------------------------ #

		# Draw lines
		ED.ActiveDocument.addObject("Part::Line", "Bottom_Line6")
		ED.ActiveDocument.Bottom_Line6.X1 = 0.0
		ED.ActiveDocument.Bottom_Line6.Y1 = 0.0
		ED.ActiveDocument.Bottom_Line6.Z1 = 20.0
		ED.ActiveDocument.Bottom_Line6.X2 = 0.0
		ED.ActiveDocument.Bottom_Line6.Y2 = 0.0
		ED.ActiveDocument.Bottom_Line6.Z2 = 40.0

		ED.ActiveDocument.addObject("Part::Line", "Bottom_Line7")
		ED.ActiveDocument.Bottom_Line7.X1 = ED.ActiveDocument.Bottom_Line6.X2
		ED.ActiveDocument.Bottom_Line7.Y1 = ED.ActiveDocument.Bottom_Line6.Y2
		ED.ActiveDocument.Bottom_Line7.Z1 = ED.ActiveDocument.Bottom_Line6.Z2
		ED.ActiveDocument.Bottom_Line7.X2 = l1
		ED.ActiveDocument.Bottom_Line7.Y2 = 0.0
		ED.ActiveDocument.Bottom_Line7.Z2 = 40.0

		ED.ActiveDocument.addObject("Part::Line", "Bottom_Line8")
		ED.ActiveDocument.Bottom_Line8.X1 = ED.ActiveDocument.Bottom_Line7.X2
		ED.ActiveDocument.Bottom_Line8.Y1 = ED.ActiveDocument.Bottom_Line7.Y2
		ED.ActiveDocument.Bottom_Line8.Z1 = ED.ActiveDocument.Bottom_Line7.Z2
		ED.ActiveDocument.Bottom_Line8.X2 = l1
		ED.ActiveDocument.Bottom_Line8.Y2 = 0.0
		ED.ActiveDocument.Bottom_Line8.Z2 = 20.0

		# Make a surface
		_=Part.makeFilledFace(Part.__sortEdges__(
			[ED.ActiveDocument.Bottom_Line3.Shape.Edge1,
			 ED.ActiveDocument.Bottom_Line4.Shape.Edge1,
			 ED.ActiveDocument.Bottom_Line6.Shape.Edge1,
			 ED.ActiveDocument.Bottom_Line7.Shape.Edge1,
			 ED.ActiveDocument.Bottom_Line8.Shape.Edge1, ]))

		ED.ActiveDocument.addObject('Part::Feature','BottomFace2').Shape=_

		ED.ActiveDocument.recompute()

		# Union operation to merge two surfaces for botton surface
		ED.activeDocument().addObject("Part::MultiFuse","Bottom_surf")
		ED.activeDocument().Bottom_surf.Shapes = [ED.activeDocument().BottomFace1,ED.activeDocument().BottomFace2,]

		ED.ActiveDocument.recompute()

		# Hide lines
		Gui.getDocument(docName).getObject("Bottom_Line6").Visibility=False
		Gui.getDocument(docName).getObject("Bottom_Line7").Visibility=False
		Gui.getDocument(docName).getObject("Bottom_Line8").Visibility=False

		# ------------------------------------------------------------------------------------------ #

		# Draw lines for side surface
		ED.ActiveDocument.addObject("Part::Line", "Side_Line1")	# = line no. 9
		ED.ActiveDocument.Side_Line1.X1 = 0.0
		ED.ActiveDocument.Side_Line1.Y1 = 0.0
		ED.ActiveDocument.Side_Line1.Z1 = 0.0
		ED.ActiveDocument.Side_Line1.X2 = 0.0
		ED.ActiveDocument.Side_Line1.Y2 = l2
		ED.ActiveDocument.Side_Line1.Z2 = 0.0

		ED.ActiveDocument.addObject("Part::Line", "Side_Line2")	# = line no. 10
		ED.ActiveDocument.Side_Line2.X1 = ED.ActiveDocument.Side_Line1.X2
		ED.ActiveDocument.Side_Line2.Y1 = ED.ActiveDocument.Side_Line1.Y2
		ED.ActiveDocument.Side_Line2.Z1 = ED.ActiveDocument.Side_Line1.Z2
		ED.ActiveDocument.Side_Line2.X2 = 0.0
		ED.ActiveDocument.Side_Line2.Y2 = l2
		ED.ActiveDocument.Side_Line2.Z2 = 20.0

		ED.ActiveDocument.addObject("Part::Line", "Side_Line3")	# = line no. 11
		ED.ActiveDocument.Side_Line3.X1 = ED.ActiveDocument.Side_Line2.X2
		ED.ActiveDocument.Side_Line3.Y1 = ED.ActiveDocument.Side_Line2.Y2
		ED.ActiveDocument.Side_Line3.Z1 = ED.ActiveDocument.Side_Line2.Z2
		ED.ActiveDocument.Side_Line3.X2 = 0.0
		ED.ActiveDocument.Side_Line3.Y2 = h
		ED.ActiveDocument.Side_Line3.Z2 = 20.0

		ED.ActiveDocument.addObject("Part::Line", "Side_Line4")	# = line no. 12
		ED.ActiveDocument.Side_Line4.X1 = ED.ActiveDocument.Side_Line3.X2
		ED.ActiveDocument.Side_Line4.Y1 = ED.ActiveDocument.Side_Line3.Y2
		ED.ActiveDocument.Side_Line4.Z1 = ED.ActiveDocument.Side_Line3.Z2
		ED.ActiveDocument.Side_Line4.X2 = 0.0
		ED.ActiveDocument.Side_Line4.Y2 = 0.0
		ED.ActiveDocument.Side_Line4.Z2 = 20.0

		# Make a surface
		_=Part.makeFilledFace(Part.__sortEdges__(
			[ED.ActiveDocument.Side_Line1.Shape.Edge1,
			 ED.ActiveDocument.Side_Line2.Shape.Edge1,
			 ED.ActiveDocument.Side_Line3.Shape.Edge1,
			 ED.ActiveDocument.Side_Line4.Shape.Edge1,
			 ED.ActiveDocument.Bottom_Line5.Shape.Edge1, ]))

		ED.ActiveDocument.addObject('Part::Feature','SideFace1').Shape=_

		ED.ActiveDocument.recompute()

		Gui.getDocument(docName).getObject("Side_Line1").Visibility=False
		Gui.getDocument(docName).getObject("Side_Line2").Visibility=False
		Gui.getDocument(docName).getObject("Side_Line3").Visibility=False
		Gui.getDocument(docName).getObject("Side_Line4").Visibility=False

		# ------------------------------------------------------------------------------------------ #

		# Draw lines
		ED.ActiveDocument.addObject("Part::Line", "Side_Line5")	# = line no. 13
		ED.ActiveDocument.Side_Line5.X1 = 0.0
		ED.ActiveDocument.Side_Line5.Y1 = 0.0
		ED.ActiveDocument.Side_Line5.Z1 = 40.0
		ED.ActiveDocument.Side_Line5.X2 = 0.0
		ED.ActiveDocument.Side_Line5.Y2 = l2
		ED.ActiveDocument.Side_Line5.Z2 = 40.0

		ED.ActiveDocument.addObject("Part::Line", "Side_Line6")	# = line no. 14
		ED.ActiveDocument.Side_Line6.X1 = ED.ActiveDocument.Side_Line5.X2
		ED.ActiveDocument.Side_Line6.Y1 = ED.ActiveDocument.Side_Line5.Y2
		ED.ActiveDocument.Side_Line6.Z1 = ED.ActiveDocument.Side_Line5.Z2
		ED.ActiveDocument.Side_Line6.X2 = 0.0
		ED.ActiveDocument.Side_Line6.Y2 = l2
		ED.ActiveDocument.Side_Line6.Z2 = 20.0

		# Make a surface
		_=Part.makeFilledFace(Part.__sortEdges__(
			[ED.ActiveDocument.Side_Line5.Shape.Edge1,
			 ED.ActiveDocument.Side_Line6.Shape.Edge1,
			 ED.ActiveDocument.Side_Line3.Shape.Edge1,
			 ED.ActiveDocument.Side_Line4.Shape.Edge1,
			 ED.ActiveDocument.Bottom_Line6.Shape.Edge1, ]))

		ED.ActiveDocument.addObject('Part::Feature','SideFace2').Shape=_

		ED.ActiveDocument.recompute()

		# Union operation to merge two surfaces for side surface
		ED.activeDocument().addObject("Part::MultiFuse","Side_surf")
		ED.activeDocument().Side_surf.Shapes = [ED.activeDocument().SideFace1,ED.activeDocument().SideFace2,]

		ED.ActiveDocument.recompute()

		# Hide lines
		Gui.getDocument(docName).getObject("Side_Line5").Visibility=False
		Gui.getDocument(docName).getObject("Side_Line6").Visibility=False

		# ------------------------------------------------------------------------------------------ #

		# Union operation to merge two surfaces
		ED.activeDocument().addObject("Part::MultiFuse","L_shape")
		ED.activeDocument().L_shape.Shapes = [ED.activeDocument().Bottom_surf, ED.activeDocument().Side_surf,]

		ED.ActiveDocument.recompute()

		# ------------------------------------------------------------------------------------------ #

		ED.ActiveDocument.addObject("Part::Line", "Support_line")	# = line no. 15
		ED.ActiveDocument.Support_line.X1 = d
		ED.ActiveDocument.Support_line.Y1 = 0.0
		ED.ActiveDocument.Support_line.Z1 = 20.0
		ED.ActiveDocument.Support_line.X2 = 0.0
		ED.ActiveDocument.Support_line.Y2 = h
		ED.ActiveDocument.Support_line.Z2 = 20

		# Make a surface of support structure
		_=Part.makeFilledFace(Part.__sortEdges__(
			[ED.ActiveDocument.Bottom_Line4.Shape.Edge1,
			 ED.ActiveDocument.Side_Line4.Shape.Edge1,
			 ED.ActiveDocument.Support_line.Shape.Edge1, ]))

		ED.ActiveDocument.addObject('Part::Feature','SupportFace').Shape=_

		ED.ActiveDocument.recompute()

		# Union operation to merge two surfaces
		ED.activeDocument().addObject("Part::MultiFuse","L_shape_with_support")
		ED.activeDocument().L_shape_with_support.Shapes = [ED.activeDocument().L_shape, ED.activeDocument().SupportFace,]

		ED.ActiveDocument.recompute()

		# ------------------------------------------------------------------------------------------ #


		ED.ActiveDocument.addObject("Part::Circle","R1_Circle")
		ED.ActiveDocument.R1_Circle.Radius= r1
		ED.ActiveDocument.R1_Circle.Angle0= 0.00
		ED.ActiveDocument.R1_Circle.Angle1= 360.00
		ED.ActiveDocument.R1_Circle.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))

		ED.getDocument(docName).R1_Circle.Placement=ED.Placement(ED.Vector(70,0,20), ED.Rotation(ED.Vector(0,0,1),0), ED.Vector(0,0,0))
		ED.getDocument(docName).R1_Circle.Placement=ED.Placement(ED.Vector(70,0,20), ED.Rotation(0,0,90), ED.Vector(0,0,0))

		_=Part.makeFilledFace(Part.__sortEdges__([ED.ActiveDocument.R1_Circle.Shape.Edge1, ]))
		ED.ActiveDocument.addObject('Part::Feature','R1_Circle_Face').Shape=_

		ED.ActiveDocument.addObject("Part::Circle","R2_Circle")
		ED.ActiveDocument.R2_Circle.Radius= r2
		ED.ActiveDocument.R2_Circle.Angle0= 0.00
		ED.ActiveDocument.R2_Circle.Angle1= 360.00
		ED.ActiveDocument.R2_Circle.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))

		ED.getDocument(docName).R2_Circle.Placement=ED.Placement(ED.Vector(0,70,20), ED.Rotation(ED.Vector(1,0,0),0), ED.Vector(0,0,0))
		ED.getDocument(docName).R2_Circle.Placement=ED.Placement(ED.Vector(0,70,20), ED.Rotation(0,90,0), ED.Vector(0,0,0))

		_=Part.makeFilledFace(Part.__sortEdges__([ED.ActiveDocument.R2_Circle.Shape.Edge1, ]))
		ED.ActiveDocument.addObject('Part::Feature','R2_Circle_Face').Shape=_

		ED.activeDocument().addObject("Part::MultiFuse","Circles")
		ED.activeDocument().Circles.Shapes = [ED.activeDocument().R1_Circle_Face, ED.activeDocument().R2_Circle_Face,]

		ED.ActiveDocument.recompute()

		ED.activeDocument().addObject("Part::Cut","Final_model")
		ED.activeDocument().Final_model.Base = ED.activeDocument().L_shape_with_support
		ED.activeDocument().Final_model.Tool = ED.activeDocument().Circles

		ED.ActiveDocument.recompute()

		Gui.getDocument(docName).getObject("R1_Circle").Visibility=False
		Gui.getDocument(docName).getObject("R2_Circle").Visibility=False

		self.doc = ED.getDocument(docName)


	def export2IGES(self):
		atnow = dttm.datetime.now()
		now = atnow.strftime("%m-%d_%H-%M-%S")

		__objs__ = []
		__objs__.append(self.doc.getObject("Final_model"))

		fileName = now + "_L-type_model.iges"
		filePath = self.str_selectedDir

		#aa = QtGui.QFileDialog.getSaveFileName(self, 'Save file', 'c:/')


		Part.export(__objs__, filePath + fileName)

		del __objs__


	def export2STEP(self):
		atnow = dttm.datetime.now()
		now = atnow.strftime("%m-%d_%H-%M-%S")
		print now

		__objs__ = []
		__objs__.append(self.doc.getObject("Final_model"))

		fileName = now + "_L-type_model.step"
		filePath = self.str_selectedDir
		Part.export(__objs__, filePath + fileName)

		del __objs__

	def getDir(self):
		selectedDir = QtGui.QFileDialog.getExistingDirectory(self, 'Open Folder', 'c:/')

		self.str_selectedDir = str(selectedDir + '\\')
		self.dir_path_LineEdit.setText(self.str_selectedDir)

	def close_program(self):
		self.close()

# For EdisonDesigner macro
app = L_type_model()

# For visual studio
#def main():
#	L_type_modeler = QtGui.QEDlication(sys.argv)
#	modeler = L_type_model()
#	sys.exit(L_type_modeler.exec_())

#main()
