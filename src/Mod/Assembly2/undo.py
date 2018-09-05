import FreeCAD as ED
import FreeCADGui as EDGui
from assembly2lib import *
from lib3D import *
from pivy import coin
from PySide import QtGui
__dir2__ = os.path.dirname(__file__)
iconPath = os.path.join( __dir2__, 'Gui','Resources', 'icons' )
GuiPath = os.path.expanduser ("~") #GuiPath = os.path.join( __dir2__, 'Gui' )

s_nm = []
s_plc = []

#todo check redefining will update the undo

class UndoConstraint:
    def Activated(self):
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
        return

    def IsActive(self):
        constraintFile = os.path.join( GuiPath , 'constraintFile.txt')
        if not os.path.exists(constraintFile):
            return False
        return True

    def GetResources(self):
        return {
            'Pixmap' : os.path.join( iconPath , 'EditUndo.svg'),
            'MenuText': 'Undo last Constrain',
            'ToolTip': 'Undo last Constrain'
            }

EDGui.addCommand('a2_UndoConstraint', UndoConstraint())