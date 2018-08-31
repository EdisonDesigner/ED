#add_defintions(-D_FC_GUI_ENABLED_)
#add_defintions(-DFREECADMAINPY)

if(BUILD_GUI)
    include_directories(
        ${Boost_INCLUDE_DIRS}
        ${COIN3D_INCLUDE_DIRS}
        ${ZLIB_INCLUDE_DIR}
        ${QT_INCLUDE_DIR}
        ${PYTHON_INCLUDE_DIRS}
        ${XercesC_INCLUDE_DIRS}
    )
else(BUILD_GUI)
    include_directories(
        ${Boost_INCLUDE_DIRS}
        ${ZLIB_INCLUDE_DIR}
        ${QT_INCLUDE_DIR}
        ${PYTHON_INCLUDE_DIRS}
        ${XercesC_INCLUDE_DIRS}
    )
endif(BUILD_GUI)

######################## EdisonDesignerMain ########################
if(BUILD_GUI)

    SET(EdisonDesigner_SRCS
        edisondesigner.rc
        ED.ico
        MainGui.cpp
    )

    SET(EdisonDesigner_LIBS
        EdisonDesignerGui
    )

    if (MSVC AND NOT BUILD_QT5)
        list(APPEND EdisonDesigner_LIBS
            ${QT_QTMAIN_LIBRARY}
        )
    endif()

    add_executable(EdisonDesignerMain WIN32 ${EdisonDesigner_SRCS})
    target_link_libraries(EdisonDesignerMain ${EdisonDesigner_LIBS})

    SET_BIN_DIR(EdisonDesignerMain EdisonDesigner)

    if(WIN32)
        INSTALL(TARGETS EdisonDesignerMain
            RUNTIME DESTINATION bin
            LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        )
    elseif(APPLE)
        INSTALL(TARGETS EdisonDesignerMain
	    RUNTIME DESTINATION MacOS
            LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        )
    else()
        INSTALL(TARGETS EdisonDesignerMain 
            RUNTIME DESTINATION bin
        )
    endif()
endif(BUILD_GUI)
######################## EdisonDesignerMainCmd ########################

SET(EdisonDesignerMainCmd_SRCS
    MainCmd.cpp
)
add_executable(EdisonDesignerMainCmd ${EdisonDesignerMainCmd_SRCS})

SET(EdisonDesignerMainCmd_LIBS
    EdisonDesignerApp
)

if (BUILD_QT5)
    list(APPEND EdisonDesignerMainCmd_LIBS
        ${Qt5Core_LIBRARIES}
        ${Qt5Xml_LIBRARIES}
    )
else()
    list(APPEND EdisonDesignerMainCmd_LIBS
        ${QT_QTCORE_LIBRARY}
        ${QT_QTXML_LIBRARY}
    )
endif()

target_link_libraries(EdisonDesignerMainCmd 
    ${EdisonDesignerMainCmd_LIBS}
)

SET_BIN_DIR(EdisonDesignerMainCmd EdisonDesignerCmd)

if(WIN32)
    INSTALL(TARGETS EdisonDesignerMainCmd
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    )
elseif(APPLE)
    INSTALL(TARGETS EdisonDesignerMainCmd
        RUNTIME DESTINATION MacOS
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    )
else()
    INSTALL(TARGETS EdisonDesignerMainCmd 
        RUNTIME DESTINATION bin
    )
endif()

######################## EdisonDesignerMainPy ########################

SET(EdisonDesignerMainPy_SRCS
    MainPy.cpp
)

add_library(EdisonDesignerMainPy SHARED ${EdisonDesignerMainPy_SRCS})

target_link_libraries(EdisonDesignerMainPy EdisonDesignerApp)

SET_BIN_DIR(EdisonDesignerMainPy EdisonDesigner)
SET_PYTHON_PREFIX_SUFFIX(EdisonDesignerMainPy)

if(WIN32)
    INSTALL(TARGETS EdisonDesignerMainPy
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    )
else(WIN32)
    INSTALL(TARGETS EdisonDesignerMainPy
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    )
endif(WIN32)

######################## EdisonDesignerGuiPy ########################
if(BUILD_GUI)

    SET(EdisonDesignerGuiPy_SRCS
        EdisonDesignerGuiPy.cpp
    )

    add_library(EdisonDesignerGuiPy SHARED ${EdisonDesignerGuiPy_SRCS})

    target_link_libraries(EdisonDesignerGuiPy EdisonDesignerGui)

    SET_BIN_DIR(EdisonDesignerGuiPy EdisonDesignerGui)
    SET_PYTHON_PREFIX_SUFFIX(EdisonDesignerGuiPy)
    if(WIN32)
        # Name clash with target "EdisonDesignerGui"
        # Must be called "EdisonDesignerGuiPy_d" and "EdisonDesignerGuiPy" to work so override default
        set_target_properties(EdisonDesignerGuiPy PROPERTIES PDB_NAME_DEBUG "EdisonDesignerGuiPy_d")
        set_target_properties(EdisonDesignerGuiPy PROPERTIES PDB_NAME_RELEASE "EdisonDesignerGuiPy")
    endif(WIN32)
    
    if(WIN32)
        INSTALL(TARGETS EdisonDesignerGuiPy
            RUNTIME DESTINATION bin
            LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        )
    else(WIN32)
        INSTALL(TARGETS EdisonDesignerGuiPy
            LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        )
    endif(WIN32)
endif(BUILD_GUI)
