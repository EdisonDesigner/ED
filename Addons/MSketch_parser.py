# -*- coding:utf-8 -*-
#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2018 - Youngki Kim <kimyg5415@kaist.ac.kr>              *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************

import FreeCAD as ED
import FreeCADGui as EDGui
import Part, Sketcher, PartDesign
import json, math
from pprint import pprint
from PySide import QtCore, QtGui

# Define constant
PI = math.pi

def MakeSketch(sketchName, translation, rotation):
    obj = App.activeDocument().addObject('Sketcher::SketchObject', sketchName)
    obj.Placement = App.Placement(App.Vector(float(translation['x']), float(translation['y']), float(translation['z'])),
                                  App.Rotation(float(rotation['x']), float(rotation['y']), float(rotation['z'])))
    ActiveSketch = App.ActiveDocument.getObject(sketchName)

def MakeCircle(sketchName, radius, index):
    obj = App.ActiveDocument.getObject(sketchName)
    """ temp circle on the origin """
    obj.addGeometry(Part.Circle(App.Vector(0.0, 0.0, 0.0), App.Vector(0.0, 0.0, 1.0), radius), False)
    obj.addConstraint(Sketcher.Constraint('Coincident', index + 4, 3, index, 3))

def MakeSlot(sketchName, linkWidth, index1, index2):
    obj = App.ActiveDocument.getObject(sketchName)
    geoList = []
    geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(0.0, 0.0, 0), App.Vector(0, 0, 1), linkWidth / 2), PI/2, -PI/2))
    geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(10.0, 0.0, 0),App.Vector(0,0,1), linkWidth / 2), -PI/2, PI/2))

    if (App.Version()[0] == "4"):
        geoList.append(Part.LineSegment(App.Vector(0.0, -linkWidth / 2, 0), App.Vector(10.0, -linkWidth / 2, 0)))
        geoList.append(Part.LineSegment(App.Vector(0.0, linkWidth / 2, 0), App.Vector(10.0, linkWidth / 2, 0)))
    elif(App.Version()[0] == "3"):
        geoList.append(Part.Line(App.Vector(0.0, -linkWidth / 2, 0), App.Vector(10.0, -linkWidth / 2, 0)))
        geoList.append(Part.Line(App.Vector(0.0, linkWidth / 2, 0), App.Vector(10.0, linkWidth / 2, 0)))
        obj.addGeometry(geoList,False)

    conList = []
    conList.append(Sketcher.Constraint('Tangent', index1, 1, index1 + 3, 1))
    conList.append(Sketcher.Constraint('Tangent', index1, 2, index1 + 2, 1))
    conList.append(Sketcher.Constraint('Tangent', index1 + 2, 2, index2, 1))
    conList.append(Sketcher.Constraint('Tangent', index1 + 3, 2, index2, 2))
    conList.append(Sketcher.Constraint('Equal', index1, index2))
    obj.addConstraint(conList)

    obj.addConstraint(Sketcher.Constraint('Radius', index1, linkWidth / 2))

def ConstrainSlot(sketchName, position, index):
    # For debug
    App.Console.PrintMessage("Index [ " + str(index) + " ]" + "\n")
    App.Console.PrintMessage("Position: [" + position['x'] + ", " + position['y'] + ", " + position['z'] + "] " + "\n")

    obj = App.ActiveDocument.getObject(sketchName)
    #obj.movePoint(index, 3, App.Vector(float(position['x']), float(position['y']), 0), 0)
    obj.addConstraint(Sketcher.Constraint('DistanceX', index, 3, float(position['x'])))
    obj.addConstraint(Sketcher.Constraint('DistanceY', index, 3, float(position['y'])))

    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView("ViewFit")

def MakePad(sketchName, depth):
    padName = "Pad_" + sketchName

    obj = App.ActiveDocument.addObject('PartDesign::Pad', padName)
    sketch = App.activeDocument().getObject(sketchName)
    obj.Sketch = sketch
    obj.Length = float(depth)

    sketch.ViewObject.hide()
    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView("ViewFit")





## File load ##
#Tkinter.Tk().withdraw() # Close the root window
#mSketchFile = tkFileDialog.askopenfilename()

#mSketchFile = 'E:\\ED_Integration\\MSketch_parser\\MSketch_parser\\Test_two_link.json'
fName = QtGui.QFileDialog.getOpenFileName()
mSketchFile = fName[0]

with open(mSketchFile) as input_data:
    data = json.load(input_data)

#print json.dumps(data, indent = 4)

# Initial parameters
thickness = data['thickness']
holeSize = data['holeSize']
linkWidth = data['linkWidth']
# Show initial data to console
App.Console.PrintMessage("Thickness(Pad depth): " + str(thickness) + "\n")
App.Console.PrintMessage("Hole size: " + str(holeSize) + "\n")
App.Console.PrintMessage("Link width: " + str(linkWidth) + "\n")

sketches = data['sketches']

# When there is no document currently, create new document
if App.activeDocument() == None:
    App.newDocument("Unnamed")

for i in range(len(sketches)):
    first_index = 0
    second_index = 1

    sketch = 'sketch' + str(i)
    translation = sketches[i]['plane']['translation']
    rotation = sketches[i]['plane']['rotation']

    """ Make Sketch """
    MakeSketch(sketch, translation, rotation)

    links = sketches[i]['links']

    for link in range(len(links)):
        """ Make slot """
        MakeSlot(sketch, linkWidth, first_index, second_index)

        """ Move sequence """
        first_pos = links[link]['points'][0]
        second_pos = links[link]['points'][1]
        # For debug
        #App.Console.PrintMessage("First Position: [" + first_pos['x'] + ", " + first_pos['y'] + ", " + first_pos['z'] + "] " + "\n")
        #App.Console.PrintMessage("Second Position: [" + second_pos['x'] + ", " + second_pos['y'] + ", " + second_pos['z'] + "] " + "\n")
        ConstrainSlot(sketch, first_pos, first_index)
        ConstrainSlot(sketch, second_pos, second_index)

        MakeCircle(sketch, holeSize, first_index)
        MakeCircle(sketch, holeSize, second_index)

        first_index = first_index + 6
        second_index = second_index + 6


    """ Make Pad """
    MakePad(sketch, thickness)
