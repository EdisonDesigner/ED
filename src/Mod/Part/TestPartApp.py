#   (c) Juergen Riegel (FreeCAD@juergen-riegel.net) 2011      LGPL        *
#                                                                         *
#   This file is part of the FreeCAD CAx development system.              *
#                                                                         *
#   This program is free software; you can redistribute it and/or modify  *
#   it under the terms of the GNU Lesser General Public License (LGPL)    *
#   as published by the Free Software Foundation; either version 2 of     *
#   the License, or (at your option) any later version.                   *
#   for detail see the LICENCE text file.                                 *
#                                                                         *
#   FreeCAD is distributed in the hope that it will be useful,            *
#   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#   GNU Library General Public License for more details.                  *
#                                                                         *
#   You should have received a copy of the GNU Library General Public     *
#   License along with FreeCAD; if not, write to the Free Software        *
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#   USA                                                                   *
#**************************************************************************

import ED, os, sys, unittest, Part
App = ED

#---------------------------------------------------------------------------
# define the test cases to test the ED Part module
#---------------------------------------------------------------------------


class PartTestCases(unittest.TestCase):
	def setUp(self):
		self.Doc = ED.newDocument("PartTest")

	def testBoxCase(self):
		self.Box = App.ActiveDocument.addObject("Part::Box","Box")
		self.Doc.recompute()
		self.failUnless(len(self.Box.Shape.Faces)==6)
		
	def tearDown(self):
		#closing doc
		ED.closeDocument("PartTest")
		#print ("omit clos document for debuging")
