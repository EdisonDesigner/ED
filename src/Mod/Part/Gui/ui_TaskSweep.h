/********************************************************************************
** Form generated from reading UI file 'TaskSweep.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TASKSWEEP_H
#define UI_TASKSWEEP_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QCheckBox>
#include <QtGui/QGridLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QWidget>
#include "Gui/Widgets.h"

namespace PartGui {

class Ui_TaskSweep
{
public:
    QGridLayout *gridLayout;
    Gui::ActionSelector *selector;
    QPushButton *buttonPath;
    QSpacerItem *horizontalSpacer_2;
    QLabel *labelPath;
    QCheckBox *checkSolid;
    QCheckBox *checkFrenet;
    QSpacerItem *horizontalSpacer;

    void setupUi(QWidget *PartGui__TaskSweep)
    {
        if (PartGui__TaskSweep->objectName().isEmpty())
            PartGui__TaskSweep->setObjectName(QString::fromUtf8("PartGui__TaskSweep"));
        PartGui__TaskSweep->resize(333, 434);
        gridLayout = new QGridLayout(PartGui__TaskSweep);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        selector = new Gui::ActionSelector(PartGui__TaskSweep);
        selector->setObjectName(QString::fromUtf8("selector"));

        gridLayout->addWidget(selector, 0, 0, 1, 3);

        buttonPath = new QPushButton(PartGui__TaskSweep);
        buttonPath->setObjectName(QString::fromUtf8("buttonPath"));

        gridLayout->addWidget(buttonPath, 1, 0, 1, 1);

        horizontalSpacer_2 = new QSpacerItem(224, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_2, 1, 1, 1, 2);

        labelPath = new QLabel(PartGui__TaskSweep);
        labelPath->setObjectName(QString::fromUtf8("labelPath"));
        labelPath->setText(QString::fromUtf8("TextLabel"));

        gridLayout->addWidget(labelPath, 2, 0, 1, 3);

        checkSolid = new QCheckBox(PartGui__TaskSweep);
        checkSolid->setObjectName(QString::fromUtf8("checkSolid"));

        gridLayout->addWidget(checkSolid, 3, 0, 1, 1);

        checkFrenet = new QCheckBox(PartGui__TaskSweep);
        checkFrenet->setObjectName(QString::fromUtf8("checkFrenet"));

        gridLayout->addWidget(checkFrenet, 3, 1, 1, 1);

        horizontalSpacer = new QSpacerItem(130, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer, 3, 2, 1, 1);


        retranslateUi(PartGui__TaskSweep);

        QMetaObject::connectSlotsByName(PartGui__TaskSweep);
    } // setupUi

    void retranslateUi(QWidget *PartGui__TaskSweep)
    {
        PartGui__TaskSweep->setWindowTitle(QApplication::translate("PartGui::TaskSweep", "Sweep", 0, QApplication::UnicodeUTF8));
        buttonPath->setText(QApplication::translate("PartGui::TaskSweep", "Sweep Path", 0, QApplication::UnicodeUTF8));
        checkSolid->setText(QApplication::translate("PartGui::TaskSweep", "Create solid", 0, QApplication::UnicodeUTF8));
        checkFrenet->setText(QApplication::translate("PartGui::TaskSweep", "Frenet", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace PartGui

namespace PartGui {
namespace Ui {
    class TaskSweep: public Ui_TaskSweep {};
} // namespace Ui
} // namespace PartGui

#endif // UI_TASKSWEEP_H
