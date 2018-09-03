# -*- coding: utf-8 -*-

import ED, EDGui
import Part
import Part,PartGui
from ED import Base

def make_35_bar(App):
    App.newDocument("Truss_35_bar")

    App.ActiveDocument.addObject("Part::Vertex","vertex_01")
    App.ActiveDocument.vertex_01.X=0.00
    App.ActiveDocument.vertex_01.Y=0.00
    App.ActiveDocument.vertex_01.Z=0.00
    App.ActiveDocument.vertex_01.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))
    App.ActiveDocument.vertex_01.Label='vertex_01'

    App.ActiveDocument.addObject("Part::Vertex","vertex_02")
    App.ActiveDocument.vertex_02.X=1000.00
    App.ActiveDocument.vertex_02.Y=0.00
    App.ActiveDocument.vertex_02.Z=0.00
    App.ActiveDocument.vertex_02.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))
    App.ActiveDocument.vertex_02.Label='vertex_02'

    App.ActiveDocument.addObject("Part::Vertex","vertex_03")
    App.ActiveDocument.vertex_03.X=0.00
    App.ActiveDocument.vertex_03.Y=1000.00
    App.ActiveDocument.vertex_03.Z=0.00
    App.ActiveDocument.vertex_03.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))
    App.ActiveDocument.vertex_03.Label='vertex_03'

    App.ActiveDocument.addObject("Part::Vertex","vertex_04")
    App.ActiveDocument.vertex_04.X=1000.00
    App.ActiveDocument.vertex_04.Y=1000.00
    App.ActiveDocument.vertex_04.Z=0.00
    App.ActiveDocument.vertex_04.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))
    App.ActiveDocument.vertex_04.Label='vertex_04'

    App.ActiveDocument.addObject("Part::Vertex","vertex_05")
    App.ActiveDocument.vertex_05.X=0.00
    App.ActiveDocument.vertex_05.Y=2000.00
    App.ActiveDocument.vertex_05.Z=0.00
    App.ActiveDocument.vertex_05.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))
    App.ActiveDocument.vertex_05.Label='vertex_05'

    App.ActiveDocument.addObject("Part::Vertex","vertex_06")
    App.ActiveDocument.vertex_06.X=1000.00
    App.ActiveDocument.vertex_06.Y=2000.00
    App.ActiveDocument.vertex_06.Z=0.00
    App.ActiveDocument.vertex_06.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))
    App.ActiveDocument.vertex_06.Label='vertex_06'

    App.ActiveDocument.addObject("Part::Vertex","vertex_07")
    App.ActiveDocument.vertex_07.X=-2000.00
    App.ActiveDocument.vertex_07.Y=2000.00
    App.ActiveDocument.vertex_07.Z=0.00
    App.ActiveDocument.vertex_07.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))
    App.ActiveDocument.vertex_07.Label='vertex_07'

    App.ActiveDocument.addObject("Part::Vertex","vertex_08")
    App.ActiveDocument.vertex_08.X=-1000.00
    App.ActiveDocument.vertex_08.Y=2000.00
    App.ActiveDocument.vertex_08.Z=0.00
    App.ActiveDocument.vertex_08.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))
    App.ActiveDocument.vertex_08.Label='vertex_08'

    App.ActiveDocument.addObject("Part::Vertex","vertex_09")
    App.ActiveDocument.vertex_09.X=2000.00
    App.ActiveDocument.vertex_09.Y=2000.00
    App.ActiveDocument.vertex_09.Z=0.00
    App.ActiveDocument.vertex_09.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))
    App.ActiveDocument.vertex_09.Label='vertex_09'

    App.ActiveDocument.addObject("Part::Vertex","vertex_10")
    App.ActiveDocument.vertex_10.X=3000.00
    App.ActiveDocument.vertex_10.Y=2000.00
    App.ActiveDocument.vertex_10.Z=0.00
    App.ActiveDocument.vertex_10.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))
    App.ActiveDocument.vertex_10.Label='vertex_10'

    App.ActiveDocument.addObject("Part::Vertex","vertex_11")
    App.ActiveDocument.vertex_11.X=-1000.00
    App.ActiveDocument.vertex_11.Y=3000.00
    App.ActiveDocument.vertex_11.Z=0.00
    App.ActiveDocument.vertex_11.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))
    App.ActiveDocument.vertex_11.Label='vertex_11'

    App.ActiveDocument.addObject("Part::Vertex","vertex_12")
    App.ActiveDocument.vertex_12.X=0.00
    App.ActiveDocument.vertex_12.Y=3000.00
    App.ActiveDocument.vertex_12.Z=0.00
    App.ActiveDocument.vertex_12.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))
    App.ActiveDocument.vertex_12.Label='vertex_12'

    App.ActiveDocument.addObject("Part::Vertex","vertex_13")
    App.ActiveDocument.vertex_13.X=1000.00
    App.ActiveDocument.vertex_13.Y=3000.00
    App.ActiveDocument.vertex_13.Z=0.00
    App.ActiveDocument.vertex_13.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))
    App.ActiveDocument.vertex_13.Label='vertex_13'

    App.ActiveDocument.addObject("Part::Vertex","vertex_14")
    App.ActiveDocument.vertex_14.X=2000.00
    App.ActiveDocument.vertex_14.Y=3000.00
    App.ActiveDocument.vertex_14.Z=0.00
    App.ActiveDocument.vertex_14.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))
    App.ActiveDocument.vertex_14.Label='vertex_14'

    App.ActiveDocument.recompute()

    _=Part.makeLine(App.ActiveDocument.vertex_01.Shape.Vertex1.Point, App.ActiveDocument.vertex_03.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_01.Shape.Vertex1.Point, App.ActiveDocument.vertex_06.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_01.Shape.Vertex1.Point, App.ActiveDocument.vertex_04.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_02.Shape.Vertex1.Point, App.ActiveDocument.vertex_04.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_02.Shape.Vertex1.Point, App.ActiveDocument.vertex_03.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_02.Shape.Vertex1.Point, App.ActiveDocument.vertex_05.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_03.Shape.Vertex1.Point, App.ActiveDocument.vertex_04.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_03.Shape.Vertex1.Point, App.ActiveDocument.vertex_05.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_03.Shape.Vertex1.Point, App.ActiveDocument.vertex_13.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_03.Shape.Vertex1.Point, App.ActiveDocument.vertex_06.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_04.Shape.Vertex1.Point, App.ActiveDocument.vertex_05.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_04.Shape.Vertex1.Point, App.ActiveDocument.vertex_12.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_04.Shape.Vertex1.Point, App.ActiveDocument.vertex_06.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_07.Shape.Vertex1.Point, App.ActiveDocument.vertex_08.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_07.Shape.Vertex1.Point, App.ActiveDocument.vertex_11.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_07.Shape.Vertex1.Point, App.ActiveDocument.vertex_12.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_08.Shape.Vertex1.Point, App.ActiveDocument.vertex_05.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_08.Shape.Vertex1.Point, App.ActiveDocument.vertex_11.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_08.Shape.Vertex1.Point, App.ActiveDocument.vertex_12.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_05.Shape.Vertex1.Point, App.ActiveDocument.vertex_11.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_05.Shape.Vertex1.Point, App.ActiveDocument.vertex_12.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_05.Shape.Vertex1.Point, App.ActiveDocument.vertex_13.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_05.Shape.Vertex1.Point, App.ActiveDocument.vertex_06.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_06.Shape.Vertex1.Point, App.ActiveDocument.vertex_12.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_06.Shape.Vertex1.Point, App.ActiveDocument.vertex_13.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_06.Shape.Vertex1.Point, App.ActiveDocument.vertex_14.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_06.Shape.Vertex1.Point, App.ActiveDocument.vertex_09.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_09.Shape.Vertex1.Point, App.ActiveDocument.vertex_13.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_09.Shape.Vertex1.Point, App.ActiveDocument.vertex_14.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_09.Shape.Vertex1.Point, App.ActiveDocument.vertex_10.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_10.Shape.Vertex1.Point, App.ActiveDocument.vertex_13.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_10.Shape.Vertex1.Point, App.ActiveDocument.vertex_14.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_11.Shape.Vertex1.Point, App.ActiveDocument.vertex_12.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_12.Shape.Vertex1.Point, App.ActiveDocument.vertex_13.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    _=Part.makeLine(App.ActiveDocument.vertex_13.Shape.Vertex1.Point, App.ActiveDocument.vertex_14.Shape.Vertex1.Point)
    if _.isNull(): raise RuntimeError('Failed to create edge')
    App.ActiveDocument.addObject('Part::Feature','Edge').Shape=_
    del _

    # increase vertex size to improve visibility
    for i in range(1, 15):
        if i < 10:
            name = "vertex_0" + str(i)
        elif i < 100:
            name = "vertex_" + str(i)

        v = EDGui.getDocument("Truss_35_bar").getObject(name)
        v.PointSize = 10


    # rename
    for i in range(35):
        if i == 0:
            obj = "Edge"
        elif i < 10:
            obj = "Edge" + "00" + str(i)
        elif i < 100:
            obj = "Edge" + "0" + str(i)

        ED.getDocument("Truss_35_bar").getObject(obj).Label = "line_" + str(i + 1)

    EDGui.SendMsgToActiveView("ViewFit")
