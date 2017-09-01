#! python
# -*- coding: utf-8 -*-
# (c) 2011 Adrian Przekwas LGPL

from __future__ import division # allows floating point division from integers
import ED, Part
from ED import Base

class MySpring:
   def __init__(self, obj):
      ''' Add the properties: Pitch, Diameter, Height, BarDiameter '''
      obj.addProperty("App::PropertyLength","Pitch","MySpring","Pitch of the helix").Pitch=5.0
      obj.addProperty("App::PropertyLength","Diameter","MySpring","Diameter of the helix").Diameter=6.0
      obj.addProperty("App::PropertyLength","Height","MySpring","Height of the helix").Height=30.0
      obj.addProperty("App::PropertyLength","BarDiameter","MySpring","Diameter of the bar").BarDiameter=3.0
      obj.Proxy = self

   def onChanged(self, fp, prop):
      if prop == "Pitch" or prop == "Diameter" or prop == "Height" or prop == "BarDiameter":
         self.execute(fp)

   def execute(self, fp):
      pitch = fp.Pitch
      radius = fp.Diameter/2
      height = fp.Height
      barradius = fp.BarDiameter/2
      myhelix=Part.makeHelix(pitch,height,radius)
      g=myhelix.Edges[0].Curve
      c=Part.Circle()
      c.Center=g.value(0) # start point of the helix
      c.Axis=(0,1,0)
      c.Radius=barradius
      p=c.toShape()
      section = Part.Wire([p])
      makeSolid=1 #change to 1 to make a solid
      isFrenet=1
      myspring=Part.Wire(myhelix).makePipeShell([section],makeSolid,isFrenet)
      fp.Shape = myspring

def makeMySpring():
   doc = ED.activeDocument()
   if doc == None:
      doc = ED.newDocument()
   spring=doc.addObject("Part::FeaturePython","My_Spring")
   spring.Label = "My Spring"
   MySpring(spring)
   spring.ViewObject.Proxy=0
   doc.recompute()

if __name__ == "__main__":
   makeMySpring()
