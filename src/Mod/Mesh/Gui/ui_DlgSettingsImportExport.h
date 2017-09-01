/********************************************************************************
** Form generated from reading UI file 'DlgSettingsImportExport.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DLGSETTINGSIMPORTEXPORT_H
#define UI_DLGSETTINGSIMPORTEXPORT_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QSpacerItem>
#include <QtGui/QWidget>
#include "Gui/PrefWidgets.h"

namespace MeshGui {

class Ui_DlgSettingsImportExport
{
public:
    QGridLayout *gridLayout;
    QSpacerItem *spacerItem;
    QGroupBox *GroupBox12;
    QGridLayout *gridLayout1;
    QGridLayout *gridLayout2;
    QLabel *textLabel1;
    Gui::QuantitySpinBox *maxDeviationExport;

    void setupUi(QWidget *MeshGui__DlgSettingsImportExport)
    {
        if (MeshGui__DlgSettingsImportExport->objectName().isEmpty())
            MeshGui__DlgSettingsImportExport->setObjectName(QString::fromUtf8("MeshGui__DlgSettingsImportExport"));
        MeshGui__DlgSettingsImportExport->resize(539, 339);
        gridLayout = new QGridLayout(MeshGui__DlgSettingsImportExport);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        spacerItem = new QSpacerItem(20, 61, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(spacerItem, 1, 0, 1, 1);

        GroupBox12 = new QGroupBox(MeshGui__DlgSettingsImportExport);
        GroupBox12->setObjectName(QString::fromUtf8("GroupBox12"));
        gridLayout1 = new QGridLayout(GroupBox12);
        gridLayout1->setSpacing(6);
        gridLayout1->setContentsMargins(11, 11, 11, 11);
        gridLayout1->setObjectName(QString::fromUtf8("gridLayout1"));
        gridLayout2 = new QGridLayout();
        gridLayout2->setSpacing(6);
        gridLayout2->setObjectName(QString::fromUtf8("gridLayout2"));
        textLabel1 = new QLabel(GroupBox12);
        textLabel1->setObjectName(QString::fromUtf8("textLabel1"));

        gridLayout2->addWidget(textLabel1, 0, 0, 1, 1);

        maxDeviationExport = new Gui::QuantitySpinBox(GroupBox12);
        maxDeviationExport->setObjectName(QString::fromUtf8("maxDeviationExport"));
        maxDeviationExport->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        maxDeviationExport->setMinimum(0);
        maxDeviationExport->setMaximum(1e+08);
        maxDeviationExport->setSingleStep(0.01);
        maxDeviationExport->setValue(0.1);

        gridLayout2->addWidget(maxDeviationExport, 0, 1, 1, 1);


        gridLayout1->addLayout(gridLayout2, 0, 0, 1, 1);


        gridLayout->addWidget(GroupBox12, 0, 0, 1, 1);


        retranslateUi(MeshGui__DlgSettingsImportExport);

        QMetaObject::connectSlotsByName(MeshGui__DlgSettingsImportExport);
    } // setupUi

    void retranslateUi(QWidget *MeshGui__DlgSettingsImportExport)
    {
        MeshGui__DlgSettingsImportExport->setWindowTitle(QApplication::translate("MeshGui::DlgSettingsImportExport", "Mesh Formats", 0, QApplication::UnicodeUTF8));
        GroupBox12->setTitle(QApplication::translate("MeshGui::DlgSettingsImportExport", "Export", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        textLabel1->setToolTip(QApplication::translate("MeshGui::DlgSettingsImportExport", "Defines the deviation of tessellation to the actual surface", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_WHATSTHIS
        textLabel1->setWhatsThis(QApplication::translate("MeshGui::DlgSettingsImportExport", "<html><head><meta name=\"qrichtext\" content=\"1\" /></head><body style=\" white-space: pre-wrap; font-family:MS Shell Dlg 2; font-size:7.8pt; font-weight:400; font-style:normal; text-decoration:none;\"><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Tessellation</span></p><p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"></p><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><span style=\" font-weight:400;\">Defines the maximum deviation of the tessellated mesh to the surface. The smaller the value is the slower the render speed and the nicer the appearance are.</span></p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS
        textLabel1->setText(QApplication::translate("MeshGui::DlgSettingsImportExport", "Maximum mesh deviation", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace MeshGui

namespace MeshGui {
namespace Ui {
    class DlgSettingsImportExport: public Ui_DlgSettingsImportExport {};
} // namespace Ui
} // namespace MeshGui

#endif // UI_DLGSETTINGSIMPORTEXPORT_H
