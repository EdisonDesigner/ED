/***************************************************************************
*   Copyright (c) 2017 Youngki Kim (kyk5415@gmail.com)                    *
*                                                                         *
*   This file is part of the EdisonDesigner CAx development system.       *
*                                                                         *
*   This library is free software; you can redistribute it and/or         *
*   modify it under the terms of the GNU Library General Public           *
*   License as published by the Free Software Foundation; either          *
*   version 2 of the License, or (at your option) any later version.      *
*                                                                         *
*   This library  is distributed in the hope that it will be useful,      *
*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
*   GNU Library General Public License for more details.                  *
*                                                                         *
*   You should have received a copy of the GNU Library General Public     *
*   License along with this library; see the file COPYING.LIB. If not,    *
*   write to the Free Software Foundation, Inc., 59 Temple Place,         *
*   Suite 330, Boston, MA  02111-1307, USA                                *
*                                                                         *
***************************************************************************/


#include "PreCompiled.h"
#ifndef _PreComp_
# include <Python.h>
#endif

#include <Base/Console.h>
#include <Gui/Application.h>
#include <Gui/Language/Translator.h>
#include "Workbench.h"

// use a different name to CreateCommand()
void CreateMechanicalPartCommands(void);

void loadMechanicalPartResource()
{
    // add resources and reloads the translators
    Q_INIT_RESOURCE(MechanicalPart);
    Gui::Translator::instance()->refresh();
}

/* registration table  */
extern struct PyMethodDef MechanicalPartGui_Import_methods[];


/* Python entry */
extern "C" {
void MechanicalPartGuiExport initMechanicalPartGui()
{
    if (!Gui::Application::Instance) {
        PyErr_SetString(PyExc_ImportError, "Cannot load Gui module in console application.");
        return;
    }

    (void) Py_InitModule("MechanicalPartGui", MechanicalPartGui_Import_methods);   /* mod name, table ptr */
    Base::Console().Log("Loading GUI of MechanicalPart module... done\n");

    // instanciating the commands
    CreateMechanicalPartCommands();
    MechanicalPartGui::Workbench::init();

     // add resources and reloads the translators
    loadMechanicalPartResource();
}

} // extern "C" {