SET(Assembly2_Files
    angleConstraint.py
    animate_constraint.py
    assembly2lib.py
    assembly2solver.py
    axialConstraint.py
    boltMultipleCircularEdges.py
    cache_assembly2.py
    checkAssembly.py
    circularEdgeConstraint.py
    CMakeLists.txt
    constraintSystems.py
    degreesOfFreedom.py
    degreesOfFreedomAnimation.py
    distanceConstraint.py
    importPart.py
    Init.py
    InitGui.py
    lib3D.py
    LICENSE
    lineSearches.py
    moveConstraint.py
    muxAssembly.py
    partsList.py
    planeConstraint.py
    solverLib.py
    sphericalSurfaceConstraint.py
    undo.py
    variableManager.py
    viewProviderProxies.py
    Gui/Resources/resources.qrc
    Gui/Resources/resources.rcc
)

SET(Assembly2_test_models
  tests/degreesOfFreedomAnimation.py
  tests/testAssembly01.fcstd
  tests/testAssembly02.fcstd
  tests/testAssembly03.fcstd
  tests/testAssembly04.fcstd
  tests/testAssembly05.fcstd
  tests/testAssembly06.fcstd
  tests/testAssembly07.fcstd
  tests/testAssembly08.fcstd
  tests/testAssembly09.fcstd
  tests/testAssembly10-block_iregular_constraint_order.fcstd
  tests/testAssembly10.fcstd
  tests/testAssembly11-Pipe_assembly.fcstd
  tests/testAssembly11.fcstd
  tests/testAssembly11b-Pipe_assembly.fcstd
  tests/testAssembly12-angles_clock_face.fcstd
  tests/testAssembly13-spherical_surfaces_cube_vertices.fcstd
  tests/testAssembly13-spherical_surfaces_hip.fcstd
  tests/testAssembly14-lock_relative_axial_rotation.fcstd
  tests/testAssembly15-triangular-link-assembly.fcstd
  tests/testAssembly16-revolved_surface_objs.fcstd
  tests/testAssembly17-bspline_objects.fcstd
  tests/testAssembly18-AddFreeObjects.fcstd
)

SET(Assembly2_icons
  Gui/Resources/icons/angleConstraint.svg
  Gui/Resources/icons/assembly2SolveConstraints.svg
  Gui/Resources/icons/axialConstraint.svg
  Gui/Resources/icons/boltMultipleCircularEdges.svg
  Gui/Resources/icons/checkAssembly.svg
  Gui/Resources/icons/circularEdgeConstraint.svg
  Gui/Resources/icons/degreesOfFreedomAnimation.svg
  Gui/Resources/icons/distanceConstraint.svg
  Gui/Resources/icons/Draft_Move.svg
  Gui/Resources/icons/EditUndo.svg
  Gui/Resources/icons/flipConstraint.svg
  Gui/Resources/icons/help.svg
  Gui/Resources/icons/importPart.svg
  Gui/Resources/icons/importPart_update.svg
  Gui/Resources/icons/lockRotation.svg
  Gui/Resources/icons/moveConstraint.svg
  Gui/Resources/icons/muxAssembly.svg
  Gui/Resources/icons/muxAssemblyRefresh.svg
  Gui/Resources/icons/partsList.svg
  Gui/Resources/icons/pause.svg
  Gui/Resources/icons/planeConstraint.svg
  Gui/Resources/icons/play.svg
  Gui/Resources/icons/preferences-assembly2.svg
  Gui/Resources/icons/sphericalSurfaceConstraint.svg
  Gui/Resources/icons/stop.svg
  Gui/Resources/icons/workBenchIcon.svg
)

SET(Assembly2_uis
  Gui/Resources/ui/assembly2_prefs.ui
  Gui/Resources/ui/degreesOfFreedomAnimation.ui
  Gui/Resources/ui/partsList.ui
)

SET(Assembly2_docs
  docs/assembly2_docs.pdf
)

ADD_CUSTOM_TARGET(Assembly2 ALL
    SOURCES ${Assembly2_Files}
            ${Assembly2_test_models}
            ${Assembly2_icons}
            ${Assembly2_uis}
            ${Assembly2_docs}
)

fc_copy_sources(Assembly2 "${CMAKE_BINARY_DIR}/Mod/Assembly2" ${Assembly2_Files}
                                                              ${Assembly2_test_models}
                                                              ${Assembly2_icons}
                                                              ${Assembly2_uis}
                                                              ${Assembly2_docs})

# Visual Studio filters
SOURCE_GROUP("Test models"  FILES ${Assembly2_test_models})
SOURCE_GROUP("Icons"        FILES ${Assembly2_icons})
SOURCE_GROUP("UIs"          FILES ${Assembly2_uis})
SOURCE_GROUP("Docs"         FILES ${Assembly2_docs})
