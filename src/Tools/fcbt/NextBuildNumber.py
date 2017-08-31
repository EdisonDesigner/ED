# FreeCAD MakeNewBuildNbr script
# (c) 2002 Juergen Riegel
#
# Increase the Build Number in Version.h

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

import time

# reading the last Version information
[EDVersionMajor,EDVersionMinor,EDVersionBuild,EDVersionDisDa] = open("../Version.h",'r').readlines()

# increasing build number
BuildNumber = int(EDVersionBuild[23:-1]) +1

print "New Buildnumber is:"
print BuildNumber
print "\n"

# writing new Version.h File
open("../Version.h",'w').writelines([EDVersionMajor,
                                     EDVersionMinor,
                                     EDVersionBuild[:23]+`BuildNumber`+'\n',
                                     EDVersionDisDa[:23]+ '"'+time.asctime()+'" \n\n'])

# writing the ChangeLog.txt
open("../ChangeLog.txt",'a').write("\nVersion: V"+EDVersionMajor[23:-1]+"."+EDVersionMinor[23:-1]+"B"+`BuildNumber`+" Date: "+time.asctime()+' +++++++++++++++++++++++++++++++\n')

# writing new Version.wxi File
open("../Version.wxi",'w').writelines(["<Include>\n",
                                     "   <?define EDVersionMajor ="+EDVersionMajor[23:-1] + " ?>\n",
                                     "   <?define EDVersionMinor ="+EDVersionMinor[23:-1] + " ?>\n",
                                     "   <?define EDVersionBuild ="+ `BuildNumber`        + " ?>\n",
                                     "</Include> \n"])

