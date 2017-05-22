/***************************************************************************
 *   (c) Juergen Riegel (juergen.riegel@web.de) 2008                       *
 *                                                                         *
 *   This file is part of the FreeCAD CAx development system.              *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU Library General Public License (LGPL)   *
 *   as published by the Free Software Foundation; either version 2 of     *
 *   the License, or (at your option) any later version.                   *
 *   for detail see the LICENCE text file.                                 *
 *                                                                         *
 *   FreeCAD is distributed in the hope that it will be useful,            *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU Library General Public License for more details.                  *
 *                                                                         *
 *   You should have received a copy of the GNU Library General Public     *
 *   License along with FreeCAD; if not, write to the Free Software        *
 *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
 *   USA                                                                   *
 *                                                                         *
 *   Juergen Riegel 2002                                                   *
 ***************************************************************************/
#include <EDConfig.h>

#ifdef _PreComp_
# undef _PreComp_
#endif



#if HAVE_CONFIG_H
#	include <config.h>
#endif // HAVE_CONFIG_H

#include <stdio.h>
#include <sstream>


// ED Base header
#include <Base/Exception.h>
#include <App/Application.h>


#if defined(ED_OS_WIN32)
# include <windows.h>
#endif

/** DllMain is called when DLL is loaded
 */
BOOL APIENTRY DllMain(HANDLE hModule, DWORD  ul_reason_for_call, LPVOID lpReserved)
{
    switch (ul_reason_for_call) {
    case DLL_PROCESS_ATTACH: {
        // This name is preliminary, we pass it to Application::init() in initED()
        // which does the rest.
        char  szFileName [MAX_PATH];
        GetModuleFileName((HMODULE)hModule, szFileName, MAX_PATH-1);
        App::Application::Config()["AppHomePath"] = szFileName;
    }
    break;
    default:
        break;
    }

    return true;
}

#ifdef ED_OS_WIN32
#	define MainExport __declspec(dllexport)
#else
#	define MainExport
#endif

extern "C"
{
    void MainExport initED() {

        // Init phase ===========================================================
		App::Application::Config()["ExeName"] = "ED";
		App::Application::Config()["ExeVendor"] = "KAIST iCAD Lab.";
		App::Application::Config()["AppDataSkipVendor"] = "true";
		

        int    argc=1;
        char** argv;
        argv = (char**)malloc(sizeof(char*)* (argc+1));

#if defined(ED_OS_WIN32)
        argv[0] = (char*)malloc(MAX_PATH);
        strncpy(argv[0],App::Application::Config()["AppHomePath"].c_str(),MAX_PATH);
        argv[0][MAX_PATH-1] = '\0'; // ensure null termination
#else
# error "Implement: Retrieve the path of the module for your platform."
#endif
        argv[argc] = 0;

        try {
            // Inits the Application
            App::Application::init(argc,argv);
        }
        catch (const Base::Exception& e) {
            std::string appName = App::Application::Config()["ExeName"];
            std::stringstream msg;
            msg << "While initializing " << appName << " the  following exception occurred: '"
                << e.what() << "'\n\n";
            msg << "\nPlease contact the application's support team for more information.\n\n";
            printf("Initialization of %s failed:\n%s", appName.c_str(), msg.str().c_str());
        }

        free(argv[0]);
        free(argv);

        return;
    } //InitED....
} // extern "C"
