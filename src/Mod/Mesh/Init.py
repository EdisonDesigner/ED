# ED init script of the Mesh module
# (c) 2004 Werner Mayer LGPL

# Append the open handler
ED.addImportType("STL Mesh (*.stl *.ast)", "Mesh")
ED.addImportType("Binary Mesh (*.bms)","Mesh")
ED.addImportType("Alias Mesh (*.obj)","Mesh")
ED.addImportType("Object File Format Mesh (*.off)","Mesh")
ED.addImportType("Stanford Triangle Mesh (*.ply)","Mesh")

ED.addExportType("STL Mesh (*.stl *.ast)", "Mesh")
ED.addExportType("Binary Mesh (*.bms)","Mesh")
ED.addExportType("Alias Mesh (*.obj)","Mesh")
ED.addExportType("Object File Format Mesh (*.off)","Mesh")
ED.addExportType("Stanford Triangle Mesh (*.ply)","Mesh")
