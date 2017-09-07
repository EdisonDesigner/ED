# Mechanical Part gui init module  
# (c) 2017 Youngki Kim
#
# Gathering all the information to start EdisonDesigner
# This is the second one of three init scripts, the third one
# runs when the gui is up

#***************************************************************************
#*   (c) Youngki Kim (kyk5415@gmail.com) 2017                              *
#*                                                                         *
#*   This file is part of the EdisonDesigner CAx development system.       *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   EdisonDesigner is distributed in the hope that it will be useful,     *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        * 
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Lesser General Public License for more details.                   *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with EdisonDesigner; if not, write to the Free Software * 
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#*   Youngki Kim 2017                                                      *
#***************************************************************************/



class MechanicalPartWorkbench ( Workbench ):
	"Mechanical Part workbench object"
	Icon = """
			/* XPM */
			static const char *Assembly_Box[]={
			"16 16 3 1",
			". c None",
			"# c #000000",
			"a c #c6c642",
			"................",
			".......#######..",
			"......#aaaaa##..",
			".....#aaaaa###..",
			"....#aaaaa##a#..",
			"...#aaaaa##aa#..",
			"..#aaaaa##aaa#..",
			".########aaaa#..",
			".#aaaaa#aaaaa#..",
			".#aaaaa#aaaa##..",
			".#aaaaa#aaa##...",
			".#aaaaa#aa##....",
			".#aaaaa#a##... .",
			".#aaaaa###......",
			".########.......",
			"................"};
			"""
	MenuText = "Mechanical Part"
	ToolTip = "Mechanical Part workbench"

	def Initialize(self):
		# load the module
		import MechanicalPartGui
		import MechanicalPart
	def GetClassName(self):
		return "MechanicalPartGui::Workbench"

Gui.addWorkbench(MechanicalPartWorkbench())
