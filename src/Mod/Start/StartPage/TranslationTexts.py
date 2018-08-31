#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2012                                                    *
#*   Yorik van Havre <yorik@uncreated.net>                                 *
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

import sys
from PySide import QtGui

def translate(context,text):
    "convenience function for the Qt translator"
    # return str(QtGui.QApplication.translate(context, text, None, QtGui.QApplication.UnicodeUTF8).toUtf8())
    try:
        _encoding = QtGui.QApplication.UnicodeUTF8
        u = QtGui.QApplication.translate(context, text, None, _encoding)
    except AttributeError:
        u = QtGui.QApplication.translate(context, text, None)

    if sys.version_info.major < 3:
        u = u.encode("utf8")

    # s = cStringIO.StringIO()
    # for i in u:
    #     if sys.version_info.major > 2: #below only works correctly in python3
    #         if i == 39:
    #             s.write("\\'")
    #         else:
    #             s.write(chr(i))
    #     else:
    #         if ord(i) == 39:
    #             s.write(unicode("\\'"))
    #         else:
    #             s.write(unicode(i))
    # t = s.getvalue()
    # s.close()
    # return t

    return u.replace(chr(39), "\\'")


text01 = translate("StartPage", "EdisonDesigner Start Center")
text02 = translate("StartPage", "Start a new project")
text03 = translate("StartPage", "Recent Files")
text04 = translate("StartPage", "Latest videos")
text05 = translate("StartPage", "Latest commits")
text06 = translate("StartPage", "On the web")
text09 = translate("StartPage", "Example projects")


# Start a new project section ======================================== #
text49 = translate("StartPage", "Getting started")
text50 = translate("StartPage", "The EdisonDesigner interface is divided in workbenches, which are sets of tools suited for a specific task. You can start with one of the workbenches in this list, or with the complete workbench, which presents you with some of the most used tools gathered from other workbenches. Click to read more about workbenches on the EdisonDesigner manual website.")
text51 = translate("StartPage", "http://http://kiya.kr/ED/manual/edisondesigner.html")

text19 = translate("StartPage", "Designing parts")
text20 = translate("StartPage", "The <b>Part Design</b> workbench is designed to create complex pieces based on constrained 2D sketches. Use it to draw 2D shapes, constrain some of their elements and extrude them to form 3D pieces.")
text21 = translate("StartPage", "Example workflow")
text22 = translate("StartPage", "Part Design")

text26 = translate("StartPage", "Working with Meshes")
text27 = translate("StartPage", "The <b>Mesh Workbench</b> is used to work with Mesh objects. Meshes are simpler 3D objects than Part objects, but they are often easier to import and export to/from other applications.")
text28 = translate("StartPage", "EdisonDesigner offers you several tools to convert between Mesh and Part objects.")
text29 = translate("StartPage", "Work with Meshes")
# ======================================== Start a new project section #


# Example projects section ======================================== #
text10 = translate("StartPage", "Connecting rod example")
text11 = translate("StartPage", "Assembly - A1")
text12 = translate("StartPage", "Assembly - A2")
# ======================================== Example projects section #


# On the Web section ======================================== #
text08 = translate("StartPage", "EDISON project Homepage")
text07 = translate("StartPage", "This is the EDISON project Homepage. Here you will be able to find a lot of information about EDISON project, other software, and so on.")

text37 = translate("StartPage", "User manual")
text45 = translate("StartPage", "This is the official user manual of EdisonDesigner, built, maintained and translated by the iCAD Laboratory.")
text38 = translate("StartPage", "http://www.kiya.kr/ED/manual")

text39 = translate("StartPage", "Tutorials")
text46 = translate("StartPage", "The tutorials section on the EdisonDesigner manual website")
text56 = translate("StartPage", "https://www.youtube.com/channel/UCCU13XDKLu__84QwQYFu97g")

text40 = translate("StartPage", "Python resources")
text47 = translate("StartPage", "The section of the FreeCAD website dedicated to python scripting, with examples, explanations, and API commands.")
text57 = translate("StartPage", "http://www.freecadweb.org/wiki/Power_users_hub")

text43 = translate("StartPage", "The FreeCAD-tutorial blog")
text48 = translate("StartPage", "A blog dedicated to teaching FreeCAD, maintained by members of the FreeCAD community")

text61 = translate("StartPage", "Obtain a development version")
text62 = translate("StartPage", "<b>Development versions</b> are made available by community members from time to time and usually contain the latest changes, but are more likely to contain bugs.")
# ======================================== On the Web section #

# Recent Files section ======================================== #
text33 = translate("StartPage", "file size:")
text34 = translate("StartPage", "creation time:")
text35 = translate("StartPage", "last modified:")
text36 = translate("StartPage", "location:")
text41 = translate("StartPage", "File not found")
# ======================================== Recent Files section #


text58 = translate("StartPage", "Your version of FreeCAD is up to date.")
text59 = translate("StartPage", "There is a new release of FreeCAD available.")


text63 = translate("StartPage", "See all commits")
text71 = translate("StartPage", "to allow FreeCAD to access the internet")


text65 = translate("StartPage", "FreeCAD Standard File")
text66 = translate("StartPage", "Author")
text67 = translate("StartPage", "Company")
text68 = translate("StartPage", "License")
text70 = translate("StartPage", "Click here")
