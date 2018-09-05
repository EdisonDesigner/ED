import FreeCAD as ED
import FreeCADGui as EDGui
from assembly2lib import *
from lib3D import *
from pivy import coin
from PySide import QtGui
from undo import *

from PySide.QtGui import *
from PySide.QtCore import *

__dir2__ = os.path.dirname(__file__)
GuiPath = os.path.join( __dir2__, 'Gui' )

class PlaneSelectionGate:
    def allow(self, doc, obj, sub):
        return planeSelected( SelectionExObject(doc, obj, sub) )

class PlaneSelectionGate2:
    def allow(self, doc, obj, sub):
        s2 = SelectionExObject(doc, obj, sub)
        return planeSelected(s2) or vertexSelected(s2)

def promt_user_for_axis_for_constraint_label():
    preferences = ED.ParamGet("User parameter:BaseApp/Preferences/Mod/Assembly2")
    return preferences.GetBool('promtUserForAxisConstraintLabel', False)

def parseSelection(selection, objectToUpdate=None, val_offset=0,direction = 'opposed'):

    validSelection = False
    if len(selection) == 2:
        s1, s2 = selection
        if s1.ObjectName != s2.ObjectName:
            if not planeSelected(s1):
                s2, s1 = s1, s2
            if planeSelected(s1) and (planeSelected(s2) or vertexSelected(s2)):
                validSelection = True
                cParms = [ [s1.ObjectName, s1.SubElementNames[0], s1.Object.Label ],
                               [s2.ObjectName, s2.SubElementNames[0], s2.Object.Label ] ]
    if not validSelection:
        msg = '''Plane constraint requires a selection of either
- 2 planes, or
- 1 plane and 1 vertex

Selection made:
%s'''  % printSelection(selection)
        QtGui.QMessageBox.information(  QtGui.qApp.activeWindow(), "Incorrect Usage", msg)
        return

    if objectToUpdate is None:
        if promt_user_for_axis_for_constraint_label():
            extraText, extraOk = QtGui.QInputDialog.getText(QtGui.qApp.activeWindow(), "Axis", "Axis for constraint Label", QtGui.QLineEdit.Normal, "0")
            if not extraOk:
                return
        else:
            extraText = ''
        cName = findUnusedObjectName('planeConstraint')
        debugPrint(2, "creating %s" % cName )
        c = ED.ActiveDocument.addObject("App::FeaturePython", cName)
        c.addProperty("App::PropertyString","Type","ConstraintInfo").Type = 'plane'
        c.addProperty("App::PropertyString","Object1","ConstraintInfo").Object1 = cParms[0][0]
        c.addProperty("App::PropertyString","SubElement1","ConstraintInfo").SubElement1 = cParms[0][1]
        c.addProperty("App::PropertyString","Object2","ConstraintInfo").Object2 = cParms[1][0]
        c.addProperty("App::PropertyString","SubElement2","ConstraintInfo").SubElement2 = cParms[1][1]
        c.addProperty('App::PropertyDistance','offset',"ConstraintInfo").offset=val_offset;

        c.addProperty("App::PropertyEnumeration","directionConstraint", "ConstraintInfo")
        c.directionConstraint = ["none","aligned","opposed"]

        c.setEditorMode('Type',1)
        for prop in ["Object1","Object2","SubElement1","SubElement2"]:
            c.setEditorMode(prop, 1)
        c.Proxy = ConstraintObjectProxy()
        c.ViewObject.Proxy = ConstraintViewProviderProxy( c, ':/assembly2/icons/planeConstraint.svg', True, cParms[1][2], cParms[0][2], extraText)
    else:
        debugPrint(2, "redefining %s" % objectToUpdate.Name )
        c = objectToUpdate
        c.Object1 = cParms[0][0]
        c.SubElement1 = cParms[0][1]
        c.Object2 = cParms[1][0]
        c.SubElement2 = cParms[1][1]
        if direction=='opposed':
            c.offset=val_offset
        else:
            c.offset=-val_offset
        c.directionConstraint = direction

        updateObjectProperties(c)
    constraintFile = os.path.join( GuiPath , 'constraintFile.txt')
    with open(constraintFile, 'w') as outfile:
        outfile.write(make_string(s1.ObjectName)+'\n'+str(s1.Object.Placement.Base)+'\n'+str(s1.Object.Placement.Rotation)+'\n')
        outfile.write(make_string(s2.ObjectName)+'\n'+str(s2.Object.Placement.Base)+'\n'+str(s2.Object.Placement.Rotation)+'\n')
    constraints = [ obj for obj in ED.ActiveDocument.Objects if 'ConstraintInfo' in obj.Content ]
    #print constraints
    if len(constraints) > 0:
        constraintFile = os.path.join( GuiPath , 'constraintFile.txt')
        if os.path.exists(constraintFile):
            with open(constraintFile, 'a') as outfile:
                lastConstraintAdded = constraints[-1]
                outfile.write(make_string(lastConstraintAdded.Name)+'\n')

    c.purgeTouched()
    c.Proxy.callSolveConstraints()
    repair_tree_view()
    return c

selection_text = '''Selection 1 options:
  - plane
Selection 2 options:
  - plane
  - vertex '''




#dlg = ExampleEX(selection)
#retval = dlg.exec_()
'''
class ExampleEX(QtGui.QDialog):

    def __init__(self,selection):
        super(ExampleEX, self).__init__()
        self.selection = selection
        self.initUI()

    def initUI(self):

        self.l  = QLabel("Offset Value:")


        self.le = QLineEdit("10",self)
        self.le.setValidator(QtGui.QIntValidator(0,65535,self))
        self.le.textChanged.connect(self.Update)
        self.hl = QHBoxLayout()
        self.hl.addWidget(self.l)
        self.hl.addWidget(self.le)

        self.bb = QDialogButtonBox(self)
        self.bb.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.bb.accepted.connect(self.accept)
        self.bb.rejected.connect(self.reject)

        self.button = QtGui.QPushButton("up")
        self.button.clicked.connect(lambda:self.buttonClick('up'))

        self.button2 = QtGui.QPushButton("down")
        self.button2.clicked.connect(lambda:self.buttonClick('down'))

        self.vl = QVBoxLayout(self)
        self.vl.addLayout(self.hl)
        self.vl.addWidget(self.bb)
        self.vl.addWidget(self.button)
        self.vl.addWidget(self.button2)

        offset = int(self.le.text())
        self.obj = parseSelection(self.selection, val_offset=offset)

    def Update(self):
        offset = int(self.le.text())
        #RedefineConstraintCommand()
        self.obj = parseSelection( self.selection, self.obj,val_offset=offset)
        ED.Console.PrintMessage('%s:,%d\n'%(self.obj.Name,offset))
        #parseSelection(selection, val_offset=offset)

    def buttonClick(self,txt):

        if txt == 'up':
            temp = str(int(self.le.text())+5)

        else:
            temp = str(int(self.le.text())-5)
        self.le.setText(temp)
'''

class DistanceTaskpanel(QtGui.QWidget):

    def __init__(self,selection,enable=False):
        super(DistanceTaskpanel, self).__init__()
        self.selection = selection
        self.enable = enable
        self.opposite = 'opposed'
        self.initUI()

    def initUI(self):
        lay = QGridLayout()
        self.status = QLabel(selection_text)


        layout = QHBoxLayout()
        layout_b = QHBoxLayout()
        layout_c = QHBoxLayout()
        #layout_v = QVBoxLayout()

        self.l  = QLabel("Offset Value:")
        layout.addWidget(self.l)

        self.sp = QSpinBox()
        self.sp.setMinimum(-100000)
        self.sp.setMaximum(100000)
        self.sp.valueChanged.connect(self.Update)
        layout.addWidget(self.sp)

        self.applyButton = QtGui.QPushButton("Apply")
        self.applyButton.clicked.connect(self.OK)
        self.undoButton = QtGui.QPushButton("Cancel")
        self.undoButton.clicked.connect(self.Undo)
        layout_b.addWidget(self.applyButton)
        layout_b.addWidget(self.undoButton)

        self.checkBox1 = QCheckBox("Opposite")
        self.checkBox1.move(0, 20)
        #self.checkBox1.resize(150, 30)
        self.checkBox1.setCheckState(Qt.Checked)
        self.checkBox1.stateChanged.connect(self.checkBoxState)

        self.checkBox2 = QCheckBox("View Update")
        self.checkBox2.move(10, 20)
        #self.checkBox1.resize(150, 30)
        self.checkBox2.setCheckState(Qt.Checked)
        self.checkBox2.stateChanged.connect(self.checkBoxState)
        layout_c.addWidget(self.checkBox1)
        layout_c.addWidget(self.checkBox2)


        lay.addWidget(self.status,0,0)
        lay.addLayout(layout, 1, 0)
        lay.addLayout(layout_c, 2, 0, Qt.AlignRight)
        lay.addLayout(layout_b, 3, 0, Qt.AlignRight)


        self.setLayout(lay)
        self.setWindowTitle("Distance Constraint")

        self.sp.setValue(int(10))
        offset = int(self.sp.value())
        #self.obj = parseSelection(self.selection, val_offset=offset,direction=self.opposite)

        self.sp.setEnabled(self.enable)
        self.applyButton.setEnabled(self.enable)
        self.undoButton.setEnabled(self.enable)
        self.checkBox1.setEnabled(self.enable)

        if self.enable==True:
            self.obj = parseSelection(self.selection, val_offset=offset,direction=self.opposite)


    def checkBoxState(self):
        if self.checkBox1.isChecked() == True:
            self.opposite='opposed';
            self.Update()
        else:
            self.opposite='aligned';
            self.Update()

    def Update(self):
        if self.checkBox2.isChecked()==True:
            offset = int(self.sp.value())
            self.obj = parseSelection( self.selection, self.obj,val_offset=offset,direction=self.opposite)
            ED.Console.PrintMessage('%s:,%d\n'%(self.obj.Name,offset))

    def OK(self):
        EDGui.Control.closeDialog()


    def Undo(self):
        constraints = [ obj for obj in ED.ActiveDocument.Objects if 'ConstraintInfo' in obj.Content ]
        if len(constraints) == 0:
            QtGui.QMessageBox.information(  QtGui.qApp.activeWindow(), "Command Aborted", 'Undo aborted since no assembly2 constraints in active document.')
            return
        lastConstraintAdded = constraints[-1]
        #print lastConstraintAdded.Name
        constraintFile = os.path.join( GuiPath , 'constraintFile.txt')
        if os.path.exists(constraintFile):
            s_nm = []
            s_plcB = []
            s_plcR = []
            undo_constraint=''
            lines = [line.rstrip('\n') for line in open(constraintFile)]
            #with open(constraintFile, 'r') as inpfile:
            #for line in inpfile:
            #    print line
            s_nm.append(lines[0])
            if len (lines) > 6:
                s_nm.append(lines[3])
                undo_constraint=lines[6]
            elif len (lines) > 3:
                undo_constraint=lines[3] #not redefining
            plc0B=lines[1].strip('Vector (').strip(')').split(',')
            plc0R=lines[2].strip('Rotation (').strip(')').split(',')
            s_plcB.append([float(plc0B[0]),float(plc0B[1]),float(plc0B[2])])
            #s_plcB.append(ED.Vector (plc0B[0],plc0B[1],plc0B[2]))
            s_plcR.append([float(plc0R[0]),float(plc0R[1]),float(plc0R[2]),float(plc0R[3])])
            if len (lines) > 6:
                plc0B=lines[4].strip('Vector (').strip(')').split(',')
                plc0R=lines[5].strip('Rotation (').strip(')').split(',')
                s_plcB.append([float(plc0B[0]),float(plc0B[1]),float(plc0B[2])])
                #s_plcB.append(ED.Vector (plc0B[0],plc0B[1],plc0B[2]))
                s_plcR.append([float(plc0R[0]),float(plc0R[1]),float(plc0R[2]),float(plc0R[3])])
                #print s_nm,s_plcB, s_plcR
            ED.ActiveDocument.getObject(s_nm[0]).Placement.Base = ED.Vector (s_plcB[0][0],s_plcB[0][1],s_plcB[0][2],)  #App.Vector (5.000000000000001, 5.000000000000003, 5.00)
            ED.ActiveDocument.getObject(s_nm[0]).Placement.Rotation = ED.Rotation (s_plcR[0][0],s_plcR[0][1],s_plcR[0][2],s_plcR[0][3])  #App.Vector (5.000000000000001, 5.000000000000003, 5.00)
            if len (lines) > 6:
                ED.ActiveDocument.getObject(s_nm[1]).Placement.Base = ED.Vector (s_plcB[1][0],s_plcB[1][1],s_plcB[1][2],)  #App.Vector (5.000000000000001, 5.000000000000003, 5.00)
                ED.ActiveDocument.getObject(s_nm[1]).Placement.Rotation = ED.Rotation (s_plcR[1][0],s_plcR[1][1],s_plcR[1][2],s_plcR[1][3])  #App.Vector (5.000000000000001, 5.000000000000003, 5.00)
            constraints = [ obj for obj in ED.ActiveDocument.Objects if 'ConstraintInfo' in obj.Content ]
            if len(constraints) == 0:
                QtGui.QMessageBox.information(  QtGui.qApp.activeWindow(), "Command Aborted", 'Flip aborted since no assembly2 constraints in active document.')
                return
            lastConstraintAdded = constraints[-1]
            if undo_constraint == lastConstraintAdded.Name:
                #print lastConstraintAdded.Name
                ED.ActiveDocument.removeObject(lastConstraintAdded.Name)
                ED.ActiveDocument.recompute()
            ED.ActiveDocument.recompute()
            os.remove(constraintFile)
        EDGui.Control.closeDialog()
        return

class DistanceConstraintCommand:
    def Activated(self):
        selection = EDGui.Selection.getSelectionEx()
        sel = EDGui.Selection.getSelection()
        if len(selection) == 2:
            self.parseSelection_EX( selection ,True)
        else:
            #related selection
            EDGui.Selection.clearSelection()

            self.selections = []
            self.secondSelectionGate = PlaneSelectionGate2()
            EDGui.Selection.addObserver(self)
            EDGui.Selection.removeSelectionGate()
            EDGui.Selection.addSelectionGate( PlaneSelectionGate() )
            wb_globals['selectionObserver'] = self

            #taskpannel
            self.parseSelection_EX( selection, False )

            '''self.taskDialog = ConstraintSelectionObserver(
		    PlaneSelectionGate(),
		    self.parseSelection_EX,
		    taskDialog_title ='add Distance constraint',
		    taskDialog_iconPath = self.GetResources()['Pixmap'],
		    taskDialog_text = selection_text,
		    secondSelectionGate = PlaneSelectionGate2() )'''


    def parseSelection_EX(self, selection,enable=False):
        EDGui.Control.closeDialog()

        self.taskDialog = SelectionTaskDialog('add Distance constraint', self.GetResources()['Pixmap'], selection_text)
        self.taskDialog.form = DistanceTaskpanel(selection,enable)
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        EDGui.Control.showDialog( self.taskDialog )

    def GetResources(self):
        return {
              'Pixmap' : ':/assembly2/icons/distanceConstraint.svg',
               'MenuText': 'Add distance constraint',
               'ToolTip': 'Add a distance constraint between two objects'
          }

    def addSelection( self, docName, objName, sub, pnt ):
        debugPrint(4,'addSelection: docName,objName,sub = %s,%s,%s' % (docName, objName, sub))
        obj = ED.ActiveDocument.getObject(objName)
        debugPrint(1,'addSelection: docName,obj.Label,sub = %s,%s,%s' % (docName, obj.Label, sub)) # to print selection name
        self.selections.append( SelectionRecord( docName, objName, sub ))
        if len(self.selections) == 2:
            s1, s2 = self.selections
            if s1.ObjectName != s2.ObjectName:
                self.stopSelectionObservation()
                self.taskDialog.form.sp.setEnabled(True)
                self.taskDialog.form.applyButton.setEnabled(True)
                self.taskDialog.form.undoButton.setEnabled(True)
                self.taskDialog.form.checkBox1.setEnabled(True)
                self.taskDialog.form.selection=self.selections
                self.taskDialog.form.obj = parseSelection(self.selections)
            else:
                QtGui.QMessageBox.information(QtGui.qApp.activeWindow(), "Warning", "Please select another object")
                ED.Console.PrintMessage('reset selection list')
                self.selections = []
                EDGui.Selection.removeSelectionGate()
                EDGui.Selection.addSelectionGate( PlaneSelectionGate() )

            #self.parseSelection_EX( self.selections, True )
        elif self.secondSelectionGate is not None and len(self.selections) == 1:
            EDGui.Selection.removeSelectionGate()
            EDGui.Selection.addSelectionGate( self.secondSelectionGate )

    def stopSelectionObservation(self):
        EDGui.Selection.removeObserver(self)
        del wb_globals['selectionObserver']
        EDGui.Selection.removeSelectionGate()
        #EDGui.Control.closeDialog()


EDGui.addCommand('addDistnaceConstraint', DistanceConstraintCommand())
