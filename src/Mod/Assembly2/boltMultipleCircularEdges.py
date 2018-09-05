import FreeCAD as ED
import FreeCADGui as EDGui
from assembly2lib import *
from assembly2solver import solveConstraints

class CircularEdgeSelectionGate:
    def allow(self, doc, obj, sub):
        return CircularEdgeSelected( SelectionExObject(doc, obj, sub) )

class boltMultipleCircularEdgesCommand:
    def Activated(self):
        selection = EDGui.Selection.getSelectionEx()
        if len(selection) < 2:
            EDGui.Selection.clearSelection()
            self.taskDialog = RapidBoltingTaskDialog()
            EDGui.Control.showDialog( self.taskDialog )
            EDGui.Selection.removeSelectionGate()
            EDGui.Selection.addSelectionGate( CircularEdgeSelectionGate() )
        else:
            valid = True
            for s in selection:
                for se_name in s.SubElementNames:
                    if not CircularEdgeSelected( SelectionExObject(ED.ActiveDocument, s.Object, se_name) ):
                        valid = False
                        break
            if valid:
                boltSelection()
            else:
                QtGui.QMessageBox.information(  QtGui.qApp.activeWindow(), "Incorrect Usage", 'Select only circular edges')
    def GetResources(self):
        msg = 'Bolt multiple circular edges'
        return {
            'Pixmap' : ':/assembly2/icons/boltMultipleCircularEdges.svg',
            'MenuText': msg,
            'ToolTip': msg
            }

EDGui.addCommand('boltMultipleCircularEdges', boltMultipleCircularEdgesCommand())

class RapidBoltingTaskDialog:
    def __init__(self):
        self.form = RapidBoltingForm('''Instructions:

1) select mating edge on Bolt
2) add to the Selection the edges
to which the bolt is to be mated
3) press Ok ''' )
        self.form.setWindowTitle( 'Bolt multiple circular edges' )
        self.form.setWindowIcon( QtGui.QIcon( ':/assembly2/icons/boltMultipleCircularEdges.svg' ) )
    def reject(self):
        EDGui.Selection.removeSelectionGate()
        EDGui.Control.closeDialog()
    def accept(self):
        EDGui.Selection.removeSelectionGate()
        EDGui.Control.closeDialog()
        boltSelection()
class RapidBoltingForm(QtGui.QWidget):
    def __init__(self, textLines ):
        super(RapidBoltingForm, self).__init__()
        self.textLines = textLines
        self.initUI()
    def initUI(self):
        vbox = QtGui.QVBoxLayout()
        for line in self.textLines.split('\n'):
            vbox.addWidget( QtGui.QLabel(line) )
        self.setLayout(vbox)


from circularEdgeConstraint import parseSelection
from importPart import duplicateImportedPart

def boltSelection():
    doc = ED.ActiveDocument
    doc.openTransaction('Bolt Multiple Circular Edges')
    selection = EDGui.Selection.getSelectionEx()
    bolt = selection[0].Object
    bolt_se_name = selection[0].SubElementNames[0]
    S = [] #edgesToConstrainTo
    for s in selection[1:]:
        for se_name in s.SubElementNames:
            S.append( SelectionExObject(doc, s.Object, se_name) )
    for s2 in S:
        newBolt = duplicateImportedPart(bolt)
        s1 = SelectionExObject(doc, newBolt, bolt_se_name)
        debugPrint(3,'s1 %s' % [s1, s2])
        parseSelection(
            [s1, s2 ],
            callSolveConstraints= False, lockRotation = True
            )
    solveConstraints( doc )
    ED.ActiveDocument.commitTransaction()
    repair_tree_view()
