# EdisonDesigner
EdisonDesigner is a free CAD system for education purpose.
It is based on FreeCAD that is also open-source CAD system.
Currently, we used some workbenches such as sketcher, part design, part, start, and web with GUI.

For EdisonDesgienr source code, 3rd party libraries is needed.

Go to this link, you can download 3rd party libraries that are also provided by the FreeCAD team.

https://www.dropbox.com/s/raqvnj6lt16vf6u/EdisonDesigner_3rdParty.7z?dl=0


# How to set up the EdisonDesigner source code

1. Download or clone source code
2. Download a 3rd party library through dropbox
3. Unzip the 3rd party library to source code folder
   then source code directory consist of
   - Bin
   - Data
   - Doc
   - Mod
   - src
   - ExtLibs
   - ReleaseBin
   - EdisonDesigner.sln

4. Open the EdisonDesigner.sln
5. Solution build
   * If you want to build by release mode, you should change the folder from Bin to DebugBin and from ReleaseBin to Bin

6. Run the EdisonDesigner_d.exe(debug mode) or EdisonDesigner.exe(Release mode) in the bin folder
   
