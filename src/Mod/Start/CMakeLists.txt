
add_subdirectory(App)
if(BUILD_GUI)
    SET(StartPage_Scripts
        StartPage.py
        TranslationTexts.py
        __init__.py
    )

    SET(StartPage_Resources  
        LoadConnectingRod.py      
        DefaultWorkbench.py        
        LoadMRU0.py
        LoadMRU1.py
        LoadMRU2.py
        LoadMRU3.py        
        PartDesign.py
        StartPage.css
        StartPage.js
        StartPage.html
        EnableDownload.py
        images/Background.jpg
        images/EdisonDesigner.png
        images/PartDesign.png        
        images/Mesh.png
        images/PartDesignExample.png
        images/web.png
        images/blank.png
        images/EdisonDesigner-doc.png
    )

    add_subdirectory(Gui)
    add_subdirectory(StartPage)
endif(BUILD_GUI)

INSTALL(
    FILES
        Init.py
        InitGui.py
    DESTINATION
        Mod/Start
)
