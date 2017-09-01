/********************************************************************************
** Form generated from reading UI file 'DlgSettingsGeneral.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DLGSETTINGSGENERAL_H
#define UI_DLGSETTINGSGENERAL_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHeaderView>
#include <QtGui/QSpacerItem>
#include <QtGui/QWidget>
#include "Gui/PrefWidgets.h"

namespace PartGui {

class Ui_DlgSettingsGeneral
{
public:
    QGridLayout *gridLayout_3;
    QGroupBox *groupBox_2;
    QGridLayout *gridLayout;
    Gui::PrefCheckBox *checkBooleanCheck;
    Gui::PrefCheckBox *checkBooleanRefine;
    Gui::PrefCheckBox *checkSketchBaseRefine;
    QGroupBox *groupBox_3;
    QGridLayout *gridLayout_2;
    Gui::PrefCheckBox *checkObjectNaming;
    QSpacerItem *spacerItem;

    void setupUi(QWidget *PartGui__DlgSettingsGeneral)
    {
        if (PartGui__DlgSettingsGeneral->objectName().isEmpty())
            PartGui__DlgSettingsGeneral->setObjectName(QString::fromUtf8("PartGui__DlgSettingsGeneral"));
        PartGui__DlgSettingsGeneral->resize(550, 333);
        gridLayout_3 = new QGridLayout(PartGui__DlgSettingsGeneral);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        groupBox_2 = new QGroupBox(PartGui__DlgSettingsGeneral);
        groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
        gridLayout = new QGridLayout(groupBox_2);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        checkBooleanCheck = new Gui::PrefCheckBox(groupBox_2);
        checkBooleanCheck->setObjectName(QString::fromUtf8("checkBooleanCheck"));
        checkBooleanCheck->setProperty("prefEntry", QVariant(QByteArray("CheckModel")));
        checkBooleanCheck->setProperty("prefPath", QVariant(QByteArray("Mod/Part/Boolean")));

        gridLayout->addWidget(checkBooleanCheck, 0, 0, 1, 1);

        checkBooleanRefine = new Gui::PrefCheckBox(groupBox_2);
        checkBooleanRefine->setObjectName(QString::fromUtf8("checkBooleanRefine"));
        checkBooleanRefine->setProperty("prefEntry", QVariant(QByteArray("RefineModel")));
        checkBooleanRefine->setProperty("prefPath", QVariant(QByteArray("Mod/Part/Boolean")));

        gridLayout->addWidget(checkBooleanRefine, 1, 0, 1, 1);

        checkSketchBaseRefine = new Gui::PrefCheckBox(groupBox_2);
        checkSketchBaseRefine->setObjectName(QString::fromUtf8("checkSketchBaseRefine"));
        checkSketchBaseRefine->setProperty("prefEntry", QVariant(QByteArray("RefineModel")));
        checkSketchBaseRefine->setProperty("prefPath", QVariant(QByteArray("Mod/PartDesign")));

        gridLayout->addWidget(checkSketchBaseRefine, 2, 0, 1, 1);


        gridLayout_3->addWidget(groupBox_2, 0, 0, 1, 1);

        groupBox_3 = new QGroupBox(PartGui__DlgSettingsGeneral);
        groupBox_3->setObjectName(QString::fromUtf8("groupBox_3"));
        gridLayout_2 = new QGridLayout(groupBox_3);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        checkObjectNaming = new Gui::PrefCheckBox(groupBox_3);
        checkObjectNaming->setObjectName(QString::fromUtf8("checkObjectNaming"));
        checkObjectNaming->setProperty("prefEntry", QVariant(QByteArray("AddBaseObjectName")));
        checkObjectNaming->setProperty("prefPath", QVariant(QByteArray("Mod/Part")));

        gridLayout_2->addWidget(checkObjectNaming, 0, 0, 1, 1);


        gridLayout_3->addWidget(groupBox_3, 1, 0, 1, 1);

        spacerItem = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_3->addItem(spacerItem, 2, 0, 1, 1);


        retranslateUi(PartGui__DlgSettingsGeneral);

        QMetaObject::connectSlotsByName(PartGui__DlgSettingsGeneral);
    } // setupUi

    void retranslateUi(QWidget *PartGui__DlgSettingsGeneral)
    {
        PartGui__DlgSettingsGeneral->setWindowTitle(QApplication::translate("PartGui::DlgSettingsGeneral", "General", 0, QApplication::UnicodeUTF8));
        groupBox_2->setTitle(QApplication::translate("PartGui::DlgSettingsGeneral", "Model settings", 0, QApplication::UnicodeUTF8));
        checkBooleanCheck->setText(QApplication::translate("PartGui::DlgSettingsGeneral", "Automatically check model after boolean operation", 0, QApplication::UnicodeUTF8));
        checkBooleanRefine->setText(QApplication::translate("PartGui::DlgSettingsGeneral", "Automatically refine model after boolean operation", 0, QApplication::UnicodeUTF8));
        checkSketchBaseRefine->setText(QApplication::translate("PartGui::DlgSettingsGeneral", "Automatically refine model after sketch-based operation", 0, QApplication::UnicodeUTF8));
        groupBox_3->setTitle(QApplication::translate("PartGui::DlgSettingsGeneral", "Object naming", 0, QApplication::UnicodeUTF8));
        checkObjectNaming->setText(QApplication::translate("PartGui::DlgSettingsGeneral", "Add name of base object", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace PartGui

namespace PartGui {
namespace Ui {
    class DlgSettingsGeneral: public Ui_DlgSettingsGeneral {};
} // namespace Ui
} // namespace PartGui

#endif // UI_DLGSETTINGSGENERAL_H
