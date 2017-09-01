/********************************************************************************
** Form generated from reading UI file 'DlgSettings3DViewPart.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DLGSETTINGS3DVIEWPART_H
#define UI_DLGSETTINGS3DVIEWPART_H

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

namespace PartGui {

class Ui_DlgSettings3DViewPart
{
public:
    QGridLayout *gridLayout;
    QSpacerItem *spacerItem;
    QGroupBox *GroupBox12;
    QGridLayout *gridLayout1;
    QGridLayout *gridLayout2;
    Gui::PrefDoubleSpinBox *maxDeviation;
    QLabel *textLabel1;
    QLabel *label;
    Gui::PrefDoubleSpinBox *maxAngularDeflection;

    void setupUi(QWidget *PartGui__DlgSettings3DViewPart)
    {
        if (PartGui__DlgSettings3DViewPart->objectName().isEmpty())
            PartGui__DlgSettings3DViewPart->setObjectName(QString::fromUtf8("PartGui__DlgSettings3DViewPart"));
        PartGui__DlgSettings3DViewPart->resize(539, 339);
        gridLayout = new QGridLayout(PartGui__DlgSettings3DViewPart);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(9, 9, 9, 9);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        spacerItem = new QSpacerItem(20, 61, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(spacerItem, 1, 0, 1, 1);

        GroupBox12 = new QGroupBox(PartGui__DlgSettings3DViewPart);
        GroupBox12->setObjectName(QString::fromUtf8("GroupBox12"));
        gridLayout1 = new QGridLayout(GroupBox12);
        gridLayout1->setSpacing(6);
        gridLayout1->setContentsMargins(9, 9, 9, 9);
        gridLayout1->setObjectName(QString::fromUtf8("gridLayout1"));
        gridLayout2 = new QGridLayout();
        gridLayout2->setSpacing(6);
        gridLayout2->setContentsMargins(0, 0, 0, 0);
        gridLayout2->setObjectName(QString::fromUtf8("gridLayout2"));
        maxDeviation = new Gui::PrefDoubleSpinBox(GroupBox12);
        maxDeviation->setObjectName(QString::fromUtf8("maxDeviation"));
        maxDeviation->setDecimals(4);
        maxDeviation->setMinimum(0.0001);
        maxDeviation->setMaximum(100);
        maxDeviation->setSingleStep(0.01);
        maxDeviation->setValue(0.5);
        maxDeviation->setProperty("prefEntry", QVariant(QByteArray("MeshDeviation")));
        maxDeviation->setProperty("prefPath", QVariant(QByteArray("Mod/Part")));

        gridLayout2->addWidget(maxDeviation, 0, 1, 1, 1);

        textLabel1 = new QLabel(GroupBox12);
        textLabel1->setObjectName(QString::fromUtf8("textLabel1"));

        gridLayout2->addWidget(textLabel1, 0, 0, 1, 1);

        label = new QLabel(GroupBox12);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout2->addWidget(label, 1, 0, 1, 1);

        maxAngularDeflection = new Gui::PrefDoubleSpinBox(GroupBox12);
        maxAngularDeflection->setObjectName(QString::fromUtf8("maxAngularDeflection"));
        maxAngularDeflection->setDecimals(2);
        maxAngularDeflection->setMinimum(0);
        maxAngularDeflection->setMaximum(180);
        maxAngularDeflection->setSingleStep(0.5);
        maxAngularDeflection->setValue(28.5);
        maxAngularDeflection->setProperty("prefEntry", QVariant(QByteArray("MeshAngularDeflection")));
        maxAngularDeflection->setProperty("prefPath", QVariant(QByteArray("Mod/Part")));

        gridLayout2->addWidget(maxAngularDeflection, 1, 1, 1, 1);


        gridLayout1->addLayout(gridLayout2, 0, 0, 1, 1);


        gridLayout->addWidget(GroupBox12, 0, 0, 1, 1);


        retranslateUi(PartGui__DlgSettings3DViewPart);

        QMetaObject::connectSlotsByName(PartGui__DlgSettings3DViewPart);
    } // setupUi

    void retranslateUi(QWidget *PartGui__DlgSettings3DViewPart)
    {
        PartGui__DlgSettings3DViewPart->setWindowTitle(QApplication::translate("PartGui::DlgSettings3DViewPart", "Shape view", 0, QApplication::UnicodeUTF8));
        GroupBox12->setTitle(QApplication::translate("PartGui::DlgSettings3DViewPart", "Tessellation", 0, QApplication::UnicodeUTF8));
        maxDeviation->setSuffix(QApplication::translate("PartGui::DlgSettings3DViewPart", " %", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        textLabel1->setToolTip(QApplication::translate("PartGui::DlgSettings3DViewPart", "Defines the deviation of tessellation to the actual surface", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_WHATSTHIS
        textLabel1->setWhatsThis(QApplication::translate("PartGui::DlgSettings3DViewPart", "<html><head><meta name=\"qrichtext\" content=\"1\" /></head><body style=\" white-space: pre-wrap; font-family:MS Shell Dlg 2; font-size:7.8pt; font-weight:400; font-style:normal; text-decoration:none;\"><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Tessellation</span></p><p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"></p><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><span style=\" font-weight:400;\">Defines the maximum deviation of the tessellated mesh to the surface. The smaller the value is the slower the render speed and the nicer the appearance are.</span></p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS
        textLabel1->setText(QApplication::translate("PartGui::DlgSettings3DViewPart", "Maximum deviation depending on the model bounding box", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("PartGui::DlgSettings3DViewPart", "Maximum angular deflection", 0, QApplication::UnicodeUTF8));
        maxAngularDeflection->setSuffix(QApplication::translate("PartGui::DlgSettings3DViewPart", " \302\260", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace PartGui

namespace PartGui {
namespace Ui {
    class DlgSettings3DViewPart: public Ui_DlgSettings3DViewPart {};
} // namespace Ui
} // namespace PartGui

#endif // UI_DLGSETTINGS3DVIEWPART_H
