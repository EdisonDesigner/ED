﻿# ED gui init module
# (c) 2003 Juergen Riegel
#
# Gathering all the information to start ED
# This is the second one of three init scripts, the third one
# runs when the gui is up

#***************************************************************************
#*   (c) Juergen Riegel (juergen.riegel@web.de) 2002                       *
#*                                                                         *
#*   This file is part of the FreeCAD CAx development system.              *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   FreeCAD is distributed in the hope that it will be useful,            *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Lesser General Public License for more details.                   *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with FreeCAD; if not, write to the Free Software        *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#*   Juergen Riegel 2002                                                   *
#***************************************************************************/


# imports the one and only
import ED, EDGui

# shortcuts
Gui = EDGui

# Important definitions
class Workbench:
	"""The workbench base class."""
	MenuText = ""
	ToolTip = ""
	
	def Initialize(self):
		"""Initializes this workbench."""
		App.PrintWarning(str(self) + ": Workbench.Initialize() not implemented in subclass!")
	def ContextMenu(self, recipient):
		pass
	def appendToolbar(self,name,cmds):
		self.__Workbench__.appendToolbar(name, cmds)
	def removeToolbar(self,name):
		self.__Workbench__.removeToolbar(name)
	def appendCommandbar(self,name,cmds):
		self.__Workbench__.appendCommandbar(name, cmds)
	def removeCommandbar(self,name):
		self.__Workbench__.removeCommandbar(name)
	def appendMenu(self,name,cmds):
		self.__Workbench__.appendMenu(name, cmds)
	def removeMenu(self,name):
		self.__Workbench__.removeMenu(name)
	def listMenus(self):
		return self.__Workbench__.listMenus()
	def appendContextMenu(self,name,cmds):
		self.__Workbench__.appendContextMenu(name, cmds)
	def removeContextMenu(self,name):
		self.__Workbench__.removeContextMenu(name)
	def name(self):
		return self.__Workbench__.name()
	def GetClassName(self):
		"""Return the name of the associated C++ class."""
		# as default use this to simplify writing workbenches in Python 
		return "Gui::PythonWorkbench"


class StandardWorkbench ( Workbench ):
	"""A workbench defines the tool bars, command bars, menus, 
context menu and dockable windows of the main window.
	"""
	def Initialize(self):
		"""Initialize this workbench."""
		# load the module
		Log ('Init: Loading ED GUI\n')
	def GetClassName(self):
		"""Return the name of the associated C++ class."""
		return "Gui::StdWorkbench"

class NoneWorkbench ( Workbench ):
	"""An empty workbench."""
	MenuText = "<none>"
	ToolTip = "The default empty workbench"
	def Initialize(self):
		"""Initialize this workbench."""
		# load the module
		Log ('Init: Loading ED GUI\n')
	def GetClassName(self):
		"""Return the name of the associated C++ class."""
		return "Gui::NoneWorkbench"

def InitApplications():
	import sys,os,traceback,cStringIO
	# Searching modules dirs +++++++++++++++++++++++++++++++++++++++++++++++++++
	# (additional module paths are already cached)
	ModDirs = ED.__path__
	#print ModDirs
	Log('Init:   Searching modules...\n')
	for Dir in ModDirs:
		if ((Dir != '') & (Dir != 'CVS') & (Dir != '__init__.py')):
			InstallFile = os.path.join(Dir,"InitGui.py")
			if (os.path.exists(InstallFile)):
				try:
					#execfile(InstallFile)
					exec open(InstallFile).read()
				except Exception, inst:
					Log('Init:      Initializing ' + Dir + '... failed\n')
					Log('-'*100+'\n')
					output=cStringIO.StringIO()
					traceback.print_exc(file=output)
					Log(output.getvalue())
					Log('-'*100+'\n')
					Err('During initialization the error ' + str(inst).decode('ascii','replace') + ' occurred in ' + InstallFile + '\n')
				else:
					Log('Init:      Initializing ' + Dir + '... done\n')
			else:
				Log('Init:      Initializing ' + Dir + '(InitGui.py not found)... ignore\n')


Log ('Init: Running EDGuiInit.py start script...\n')

# init the gui

# signal that the gui is up
App.GuiUp = 1
App.Gui = EDGui
EDGui.Workbench = Workbench

Gui.addWorkbench(NoneWorkbench())

# init modules
InitApplications()

# set standard workbench (needed as fallback)
Gui.activateWorkbench("NoneWorkbench")

# Register .py, .FCScript and .FCMacro
ED.addImportType("Inventor V2.1 (*.iv)","EDGui")
ED.addImportType("VRML V2.0 (*.wrl *.vrml *.wrz *.wrl.gz)","EDGui")
ED.addImportType("Python (*.py *.FCMacro *.FCScript)","EDGui")
ED.addExportType("Inventor V2.1 (*.iv)","EDGui")
ED.addExportType("VRML V2.0 (*.wrl *.vrml *.wrz *.wrl.gz)","EDGui")
#ED.addExportType("IDTF (for 3D PDF) (*.idtf)","EDGui")
#ED.addExportType("3D View (*.svg)","EDGui")
ED.addExportType("Portable Document Format (*.pdf)","EDGui")

del(InitApplications)
del(NoneWorkbench)
del(StandardWorkbench)


Log ('Init: Running EDGuiInit.py start script... done\n')