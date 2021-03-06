import FreeCAD as ED
import FreeCADGui as EDGui
from assembly2lib import *
from PySide import QtGui, QtCore
import traceback
import degreesOfFreedom
import sys

moduleVars = {}

class AnimateCommand:
    def Activated(self):
        from assembly2solver import solveConstraints
        constraintSystem = solveConstraints(ED.ActiveDocument)
        self.taskPanel = AnimateDegreesOfFreedomTaskPanel( constraintSystem )
        EDGui.Control.showDialog( self.taskPanel )
    def GetResources(self):
        msg = 'Animate degrees of freedom'
        return {
            'Pixmap' : ':/assembly2/icons/degreesOfFreedomAnimation.svg',
            'MenuText': msg,
            'ToolTip':  msg
            }
animateCommand = AnimateCommand()
EDGui.addCommand('degreesOfFreedomAnimation', animateCommand)


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class AnimateDegreesOfFreedomTaskPanel:
    def __init__(self, constraintSystem):
        self.constraintSystem = constraintSystem
        self.form = EDGui.PySideUic.loadUi( ':/assembly2/ui/degreesOfFreedomAnimation.ui' )
        self.form.setWindowIcon(QtGui.QIcon( ':/assembly2/icons/degreesOfFreedomAnimation.svg' ) )
        self.form.groupBox_DOF.setTitle('%i Degrees-of-freedom:' % len(constraintSystem.degreesOfFreedom))
        for i, d in enumerate(constraintSystem.degreesOfFreedom):
            item = QtGui.QListWidgetItem('%i. %s' % (i+1, str(d)[1:-1].replace('DegreeOfFreedom ','')), self.form.listWidget_DOF)
            if i == 0: item.setSelected(True)
        self.form.pushButton_animateSelected.clicked.connect(self.animateSelected)
        self.form.pushButton_animateAll.clicked.connect(self.animateAll)
        self.form.pushButton_set_as_default.clicked.connect(self.test)#setDefaults
        self.setIntialValues()

    def test(self):
	ex = Example()
	QtGui.QMessageBox.information(  QtGui.qApp.activeWindow(), "Value Error", "So H W" )
	ED.Console.PrintMessage('hellow')
	#ED.Console.PrintError('Aborting Animation! Constraint system has no degrees of freedom.')
	#print('Hellow')

    def _startAnimation(self, degreesOfFreedomToAnimate):
        frames_per_DOF =  self.form.spinBox_frames_per_DOF.value()
        ms_per_frame = self.form.spinBox_ms_per_frame.value()
        rotationAmplification = self.form.doubleSpinBox_rotMag.value()
        linearDispAmplification = self.form.doubleSpinBox_linMag.value()
        if len(self.constraintSystem.degreesOfFreedom) > 0:
            moduleVars['animation'] = AnimateDOF(self.constraintSystem, degreesOfFreedomToAnimate, ms_per_frame, frames_per_DOF, rotationAmplification, linearDispAmplification)
            #moduleVars['animation'] assignment required to protect the QTimer from the garbage collector
        else:
            ED.Console.PrintError('Aborting Animation! Constraint system has no degrees of freedom.')
            EDGui.Control.closeDialog()

    def setIntialValues(self):
        parms = ED.ParamGet("User parameter:BaseApp/Preferences/Mod/Assembly2/degreeOfFreedomAnimation")
        form = self.form
        form.spinBox_frames_per_DOF.setValue(    parms.GetFloat('frames_per_DOF', 42) )
        form.spinBox_ms_per_frame.setValue(      parms.GetFloat('ms_per_frame', 50) )
        form.doubleSpinBox_rotMag.setValue(      parms.GetFloat('rotation_magnitude', 1.0) )
        form.doubleSpinBox_linMag.setValue(      parms.GetFloat('linear_magnitude', 1.0) )
    def setDefaults(self):
        parms = ED.ParamGet("User parameter:BaseApp/Preferences/Mod/Assembly2/degreeOfFreedomAnimation")
        form = self.form
        parms.SetFloat('frames_per_DOF',       form.spinBox_frames_per_DOF.value()       )
        parms.SetFloat('ms_per_frame',         form.spinBox_ms_per_frame.value()       )
        parms.SetFloat('rotation_magnitude',   form.doubleSpinBox_rotMag.value()       )
        parms.SetFloat('linear_magnitude',     form.doubleSpinBox_linMag.value()       )

    def animateSelected(self):
        debugPrint(4,'pushButton_animateSelected has been clicked')
        D_to_animate = []
        for index, d in enumerate( self.constraintSystem.degreesOfFreedom ):
            #debugPrint(4,'getting item at index %i' % index)
            item = self.form.listWidget_DOF.item(index)
            #debugPrint(4,'checking if %s is selected' % d.str())
            if item.isSelected():
                D_to_animate.append( d )
        if len(D_to_animate) > 0:
            self._startAnimation( D_to_animate )
    def animateAll(self):
         self._startAnimation( [d for d in self.constraintSystem.degreesOfFreedom] )

    def reject(self): #or more correctly close, given the button settings
        if  'animation' in moduleVars:
            moduleVars['animation'].timer.stop()
            self.constraintSystem.variableManager.updateEDValues(moduleVars['animation'].X_before_animation)
            del moduleVars['animation']
        EDGui.Control.closeDialog()

    def getStandardButtons(self): #http://forum.FreeCADweb.org/viewtopic.php?f=10&t=11801
        return 0x00200000




class AnimateDOF(object):
    'based on http://FreeCAD-tutorial.blogspot.com/2014/06/piston-conrod-animation.html'
    def __init__(self, constraintSystem, degreesOfFreedomToAnimate, tick=50, framesPerDOF=40, rotationAmplification=1.0, linearDispAmplification=1.0):
        self.constraintSystem = constraintSystem
        self.degreesOfFreedomToAnimate = degreesOfFreedomToAnimate
        self.Y0 = numpy.array([ d.getValue() for d in degreesOfFreedomToAnimate] )
        self.X_before_animation = constraintSystem.variableManager.X.copy()
        self.framesPerDOF = framesPerDOF
        self.rotationAmplification = rotationAmplification
        self.linearDispAmplification = linearDispAmplification
        debugPrint(2,'beginning degrees of freedom animation')
        self.count = 0
        self.dof_count = 0
        self.updateAmplitude()
        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.renderFrame)
        self.timer.start( tick )

    def updateAmplitude( self) :
        D = self.degreesOfFreedomToAnimate
        if D[self.dof_count].rotational():
            self.amplitude = 1.0 * self.rotationAmplification
        else:
            obj = ED.ActiveDocument.getObject( D[self.dof_count].objName )
            self.amplitude = obj.Shape.BoundBox.DiagonalLength / 2 * self.linearDispAmplification

    def renderFrame(self):
        try:
            debugPrint(5,'timer loop running')
            self.count = self.count + 1
            D = self.degreesOfFreedomToAnimate
            if self.count > self.framesPerDOF: #placed here so that if is error timer still exits
                self.count = 0
                self.dof_count = self.dof_count + 1
                if base_rotation_dof( D[self.dof_count-1] ):
                    self.dof_count = self.dof_count + 2
                if self.dof_count + 1 > len( D ):
                    self.timer.stop()
                    self.constraintSystem.variableManager.updateEDValues(self.X_before_animation)
                    return
                self.updateAmplitude()

            if self.count == 1: debugPrint(3,'animating %s' % D[self.dof_count])
            debugPrint(4,'dof %i, dof frame %i' % (self.dof_count, self.count))
            Y = self.Y0.copy()
            r = 2*numpy.pi*( 1.0*self.count/self.framesPerDOF)
            Y[self.dof_count] = self.Y0[self.dof_count] + self.amplitude * numpy.sin(r)
            if self.dof_count + 2 < len(D):
                if base_rotation_dof( D[self.dof_count] ) and base_rotation_dof( D[self.dof_count+1] ) and base_rotation_dof( D[self.dof_count+2] ): #then also adjust other base rotation degrees of freedom so that rotation is always visible
                    Y[self.dof_count+1] = self.Y0[self.dof_count+1] +self.amplitude*numpy.sin(r)
                    Y[self.dof_count+2] = self.Y0[self.dof_count+2] +self.amplitude*numpy.sin(r)
            debugPrint(5,'Y frame %s, sin(r) %1.2f' % (Y,numpy.sin(r)))
        except:
            self.timer.stop()
            App.Console.PrintError(traceback.format_exc())
            App.Console.PrintError('Aborting animation')
        try:
            for d,y in zip( D, Y):
                d.setValue(y)
                self.constraintSystem.update()
            self.constraintSystem.variableManager.updateEDValues( self.constraintSystem.variableManager.X )
            debugPrint(5,'updated assembly')
        except:
            ED.Console.PrintError('AnimateDegreeOfFreedom (dof %i, dof frame %i) unable to update constraint system\n'  % (self.dof_count, self.count))
            ED.Console.PrintError(traceback.format_exc())
        debugPrint(5,'finished timer loop')

def base_rotation_dof(d):
    if isinstance(d,degreesOfFreedom.PlacementDegreeOfFreedom) and  hasattr(d, 'ind'):
        return d.ind % 6 > 2
    return False
