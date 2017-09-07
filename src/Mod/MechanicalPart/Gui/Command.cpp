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
#endif

#include <Gui/Application.h>
#include <Gui/Command.h>
#include <Gui/MainWindow.h>
#include <Gui/FileDialog.h>


using namespace std;

DEF_STD_CMD(CmdMechanicalPartTest);

CmdMechanicalPartTest::CmdMechanicalPartTest()
	:Command("MechanicalPart_Test")
{
    sAppModule      = "MechanicalPart";
    sGroup          = QT_TR_NOOP("MechanicalPart");
    sMenuText       = QT_TR_NOOP("Test...");
    sToolTipText    = QT_TR_NOOP("This is a test function");
    sWhatsThis      = "MechanicalPart_Test";
    sStatusTip      = sToolTipText;
    sPixmap         = "TestIcon";
}


void CmdMechanicalPartTest::activated(int iMsg)
{
    // load the file with the module
    //Command::doCommand(Command::Gui, "import Assembly, AssemblyGui");
      
}



void CreateMechanicalPartCommands(void)
{
    Gui::CommandManager &rcCmdMgr = Gui::Application::Instance->commandManager();

	rcCmdMgr.addCommand(new CmdMechanicalPartTest());
 }
