import FreeCAD as ED
import FreeCADGui as EDGui
from assembly2lib import *
from lib3D import *
from pivy import coin
from PySide import QtGui
from PySide.QtGui import *
from PySide.QtCore import *

class MoveConstraintCommand:
    def Activated(self):
        from assembly2solver import solveConstraints

        EDGui.Selection.addObserver(self)

        self.constraintSystem = solveConstraints(ED.ActiveDocument)
        dof = self.ParSelecDOF(self.constraintSystem)

        self.taskPanel = EDTaskDialog('T',None,'S', dof )
        EDGui.Control.showDialog( self.taskPanel )


    def ParSelecDOF(self,solvedconstraint):

        constraintSystem = solvedconstraint

        selection = [s for s in EDGui.Selection.getSelectionEx() if s.Document == ED.ActiveDocument ]
        self.target = selection[0].ObjectName
        self.targetobj = selection[0].Object
        ED.Console.PrintMessage('%s is selected\n' % (self.target))


        dof = [False,False,False,False,False,False] #TRANS X TRANS Y TRANS Z ROT X ROT Y ROT Z - basis norm
        self.dofc = [None,None,None,None,None,None]
        for d in constraintSystem.degreesOfFreedom: #Get freedom direction or axis from constraintSystem
            if str(d).find(self.target)!=-1:
                temp = str(d)
                for si in ['[',']',':','<','>','  ','  ','  ']:
                    temp = temp.replace(si,' ')
                tempinfo = temp.split(' ')          #LinearMotion, DegreeOfFreedom, part2, direction, 6.12323400e-17, 1.00000000e+00, 0.00000000e+00,  value, -0.212375
                                                    #AxisRotation, DegreeOfFreedom, part2, axis,      1.33650194e-16, 2.22044605e-16, -1.00000000e+00, value, -0.000000
                for i in range(0,len(tempinfo)):
                    ED.Console.PrintMessage('%s\n' % (tempinfo[i]))

                freeDirection = tempinfo[5:8]       #object's free direction [X,Y,Z] values - faxis

                #temporary calculatation just max it will be changed
                #'%s<LinearMotion DegreeOfFreedom %s direction:%s value:%f>' % (indent, self.objName, self.directionVector, self.getValue())
                #'%s<AxisRotation DegreeOfFreedom %s axis:%s value:%f>' % (indent, self.objName, self.axis, self.getValue())
                for i in range(3):
                    freeDirection[i]=abs(float(freeDirection[i]))
                index = freeDirection.index(max(freeDirection))

                if tempinfo[4]=='direction':
                    dof[index]=True
                    self.dofc[index]=d
                elif tempinfo[4]=='axis':
                    dof[index+3]=True
                    self.dofc[index+3]=d

        return dof


    def GetResources(self):
        return {
            'Pixmap' : ':/assembly2/icons/moveConstraint.svg',
            'MenuText': 'Check DOF',
            'ToolTip': 'Check DOF for selected part'
        }

    def addSelection( self, docName, objName, sub, pnt ):
        #debugPrint(4,'addSelection: docName,objName,sub = %s,%s,%s' % (docName, objName, sub))
        #EDGui.Selection.removeObserver(self)
        obj = ED.ActiveDocument.getObject(objName)
        ED.Console.PrintMessage('%s is selected\n' % (objName))


        if self.target != objName:
            dof = self.ParSelecDOF(self.constraintSystem)
            self.taskPanel.form.updateDialog(dof)

        if self.taskPanel.form.sel > -1 and self.target == objName:
            view = EDGui.activeDocument().activeView()
            ED.Console.PrintMessage('movemove\n')
            PartMover( view, obj, self.constraintSystem,[self.dofc[self.taskPanel.form.sel]])
            #PartMover( view, obj, self.constraintSystem,[self.constraintSystem.degreesOfFreedom[1]])


EDGui.addCommand('addMoveConstraint', MoveConstraintCommand())

class EDTaskDialog:
    def __init__(self, title, iconPath, textLines, argu):
        self.form = MoveDegreeofFreedomTaskPanel( argu )
        self.form.setWindowTitle( title )
        if iconPath != None:
            self.form.setWindowIcon( QtGui.QIcon( iconPath ) )
    def reject(self):
        EDGui.Control.closeDialog()

    def getStandardButtons(self): #http://forum.FreeCADweb.org/viewtopic.php?f=10&t=11801
        return 0x00400000 #cancel button


class MoveDegreeofFreedomTaskPanel(QtGui.QWidget):
    def __init__(self,DegreeOfFreedom):
        super(MoveDegreeofFreedomTaskPanel, self).__init__()
        #self.constraintSystem = constraintSystem
        self.dof = DegreeOfFreedom
        self.sel = -1
        self.mover = None
        self.initUI()

    def initUI(self):
        lay = QGridLayout()
        self.status = QLabel('Move DOF')

        #set tool
        self.buttontxt=["Trans X","Trans Y","Trans Z","Rot X","Rot Y","Rot Z"]
        self.buttons=[QtGui.QPushButton(self.buttontxt[i]) for i in range(6)]

        for i in range(6):
            self.buttons[i].setCheckable(True)
            self.buttons[i].clicked[bool].connect(self.btnToggle)

        #set layout
        layout_b = QHBoxLayout()
        layout_c = QHBoxLayout()

        for i in range(3):
            layout_b.addWidget(self.buttons[i])
            layout_c.addWidget(self.buttons[i+3])

        lay.addWidget(self.status,0,0)
        lay.addLayout(layout_c, 1, 0)
        lay.addLayout(layout_b, 2, 0)

        self.setLayout(lay)
        self.setWindowTitle("Move DOF")

        self.updateDialog(self.dof)

    def updateDialog(self,DegreeOfFreedom):
        self.dof = DegreeOfFreedom
        self.sel = -1                       #checked button index reset
        self.mover = None
        for i in range(6):
            self.buttons[i].setEnabled(self.dof[i])
            if self.buttons[i].isChecked(): # all the buttons uncheck
                self.buttons[i].toggle()

    def btnToggle(self,pressed):
        c = self.sender()
        ED.Console.PrintMessage('%s is clicked\n' % (c.text()))
        for i in range(6):
            if self.buttontxt[i]==c.text():
                self.sel = i
            else:
                if self.buttons[i].isChecked():
                    self.buttons[i].toggle()
        ED.Console.PrintMessage('%s is selected\n' % (self.buttons[self.sel].text()))


class PartMover:
    def __init__(self, view, obj,constraintSystem,degreesOfFreedomToAnimate,tick=50, framesPerDOF=40, rotationAmplification=1.0, linearDispAmplification=1.0):
        self.obj = obj
        self.initialPostion = self.obj.Placement.Base
        self.copiedObject = False
        self.view = view
        self.prePos = None
        self.callbackMove = self.view.addEventCallback("SoLocation2Event",self.moveMouse)
        self.callbackClick = self.view.addEventCallback("SoMouseButtonEvent",self.clickMouse)
        self.callbackKey = self.view.addEventCallback("SoKeyboardEvent",self.KeyboardEvent)

        self.constraintSystem = constraintSystem
        self.dof_count = 0
        self.count = 0
        self.degreesOfFreedomToAnimate = degreesOfFreedomToAnimate
        self.Y0 = numpy.array([degreesOfFreedomToAnimate[0].getValue()])
        self.X_before_animation = constraintSystem.variableManager.X.copy()
        self.rotationAmplification = rotationAmplification
        self.framesPerDOF = framesPerDOF
        self.linearDispAmplification = linearDispAmplification
        self.updateAmplitude()
    def updateAmplitude( self) :
        D = self.degreesOfFreedomToAnimate
        if D[self.dof_count].rotational():
            self.amplitude = 1.0 * self.rotationAmplification
        else:
            obj = ED.ActiveDocument.getObject( D[self.dof_count].objName )
            #self.amplitude = obj.Shape.BoundBox.DiagonalLength / 2 * self.linearDispAmplification
            self.amplitude = 1

    def moveMouse(self, info):
        newPos = self.view.getPoint( *info['Position'] )
        debugPrint(5, 'new position %s' % str(newPos))


        self.count = self.count + 1
        D = self.degreesOfFreedomToAnimate

        Y = self.Y0.copy()

        if self.prePos == None:
            r = 0
            self.prePos = newPos
        else:
            if D[self.dof_count].rotational():
                v1 = numpy.array(self.prePos - self.initialPostion)
                v2 = numpy.array(newPos - self.initialPostion)

                v1_u = v1 / numpy.linalg.norm(v1)
                v2_u = v2 / numpy.linalg.norm(v2)
                r = numpy.arccos(numpy.clip(numpy.dot(v1_u, v2_u), -1.0, 1.0)) * -1
                #r = math.acos(dotproduct(v1, v2) / (math.sqrt(dotproduct(v1, v1)) * math.sqrt(dotproduct(v2, v2))))
                ED.Console.PrintMessage('%s /////\n' %(str(r)))

            else:
                #r = dot((newPos - self.prePos), D[self.dof_count].directionVector)
                v1 = D[self.dof_count].directionVector
                v1_u = v1 / numpy.linalg.norm(v1)
                r = dot((newPos - self.initialPostion), v1_u)
                ED.Console.PrintMessage('%e \n' % (r))

        Y[self.dof_count] = self.Y0[self.dof_count] + self.amplitude * r #numpy.sin(r)
        ED.Console.PrintMessage('%e %e is selected\n' % (self.Y0[0],Y[0]))

        '''
        if self.dof_count + 2 < len(D):
            if base_rotation_dof( D[self.dof_count] ) and base_rotation_dof( D[self.dof_count+1] ) and base_rotation_dof( D[self.dof_count+2] ): #then also adjust other base rotation degrees of freedom so that rotation is always visible
                Y[self.dof_count+1] = self.Y0[self.dof_count+1] +self.amplitude*numpy.sin(r)
                Y[self.dof_count+2] = self.Y0[self.dof_count+2] +self.amplitude*numpy.sin(r)
        debugPrint(5,'Y frame %s, sin(r) %1.2f' % (Y,numpy.sin(r)))
        '''

        try:
            for d,y in zip( D, Y):
                d.setValue(y)
                self.constraintSystem.update()
            self.constraintSystem.variableManager.updateEDValues( self.constraintSystem.variableManager.X )
            debugPrint(5,'updated assembly')
        except:
            ED.Console.PrintError('AnimateDegreeOfFreedom (dof %i, dof frame %i) unable to update constraint system\n'  % (self.dof_count, self.count))
            ED.Console.PrintError(traceback.format_exc())



        '''
        newPos = self.view.getPoint( *info['Position'] )
        debugPrint(5, 'new position %s' % str(newPos))
        self.obj.Placement.Base = newPos
        '''
    def removeCallbacks(self):
        self.view.removeEventCallback("SoLocation2Event",self.callbackMove)
        self.view.removeEventCallback("SoMouseButtonEvent",self.callbackClick)
        self.view.removeEventCallback("SoKeyboardEvent",self.callbackKey)
    def clickMouse(self, info):
        debugPrint(4, 'clickMouse info %s' % str(info))
        self.removeCallbacks()
        '''
        debugPrint(4, 'clickMouse info %s' % str(info))
        if info['Button'] == 'BUTTON1' and info['State'] == 'DOWN':
            if not info['ShiftDown'] and not info['CtrlDown']:
                self.removeCallbacks()
            elif info['ShiftDown']: #copy object
                self.obj = duplicateImportedPart( self.obj )
                self.copiedObject = True
            elif info['CtrlDown']:
                azi   =  ( numpy.random.rand() - 0.5 )*numpy.pi*2
                ela   =  ( numpy.random.rand() - 0.5 )*numpy.pi
                theta =  ( numpy.random.rand() - 0.5 )*numpy.pi
                axis = azimuth_and_elevation_angles_to_axis( azi, ela )
                self.obj.Placement.Rotation.Q = quaternion( theta, *axis )
        '''

    def KeyboardEvent(self, info):
        debugPrint(4, 'KeyboardEvent info %s' % str(info))
        '''
        debugPrint(4, 'KeyboardEvent info %s' % str(info))
        if info['State'] == 'UP' and info['Key'] == 'ESCAPE':
            if not self.copiedObject:
                self.obj.Placement.Base = self.initialPostion
            else:
                ED.ActiveDocument.removeObject(self.obj.Name)
            self.removeCallbacks()
        '''
