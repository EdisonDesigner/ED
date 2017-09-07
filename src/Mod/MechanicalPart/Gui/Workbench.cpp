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
# include <qobject.h>
#endif

#include "Workbench.h"
#include <Gui/Application.h>
#include <Gui/Command.h>
#include <Gui/MenuManager.h>
#include <Gui/ToolBarManager.h>

using namespace MechanicalPartGui;

/// @namespace AssemblyGui @class Workbench
TYPESYSTEM_SOURCE(MechanicalPartGui::Workbench, Gui::StdWorkbench)

Workbench::Workbench()
{
}

Workbench::~Workbench()
{
}

// EdisonDesigner 상단 메뉴에 항목 추가
Gui::MenuItem* Workbench::setupMenuBar() const
{
	Gui::MenuItem* root = StdWorkbench::setupMenuBar();
	Gui::MenuItem* item = root->findItem("&Windows");

	Gui::MenuItem* part = new Gui::MenuItem;
	root->insertItem(item, part);

	// 추가될 메뉴의 이름
	part->setCommand("&Mechanical Part");

	// 추가될 항목 - Command.cpp에서 정의한 것과 동일해야 함.
	*part << "MechanicalPart_Test";

	return root;
}

// EdisonDesigner 툴바에 항목 추가
Gui::ToolBarItem* Workbench::setupToolBars() const
{
    Gui::ToolBarItem* root = StdWorkbench::setupToolBars();
    Gui::ToolBarItem* part = new Gui::ToolBarItem(root);
    part->setCommand(QT_TR_NOOP("MechanicalPart"));
    *part << "MechanicalPart_Test";
     return root;
}

Gui::ToolBarItem* Workbench::setupCommandBars() const
{
    // Part tools
    Gui::ToolBarItem* root = new Gui::ToolBarItem;
    return root;
}

