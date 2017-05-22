/********************************************************************************
** Form generated from reading UI file 'TaskSketcherGeneral.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TASKSKETCHERGENERAL_H
#define UI_TASKSKETCHERGENERAL_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QCheckBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>
#include "Gui/PrefWidgets.h"

namespace SketcherGui {

class Ui_TaskSketcherGeneral
{
public:
    QVBoxLayout *verticalLayout;
    QCheckBox *checkBoxShowGrid;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    Gui::PrefQuantitySpinBox *gridSize;
    QCheckBox *checkBoxGridSnap;
    QCheckBox *checkBoxAutoconstraints;

    void setupUi(QWidget *SketcherGui__TaskSketcherGeneral)
    {
        if (SketcherGui__TaskSketcherGeneral->objectName().isEmpty())
            SketcherGui__TaskSketcherGeneral->setObjectName(QString::fromUtf8("SketcherGui__TaskSketcherGeneral"));
        SketcherGui__TaskSketcherGeneral->resize(153, 115);
        verticalLayout = new QVBoxLayout(SketcherGui__TaskSketcherGeneral);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        checkBoxShowGrid = new QCheckBox(SketcherGui__TaskSketcherGeneral);
        checkBoxShowGrid->setObjectName(QString::fromUtf8("checkBoxShowGrid"));
        checkBoxShowGrid->setChecked(true);

        verticalLayout->addWidget(checkBoxShowGrid);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label = new QLabel(SketcherGui__TaskSketcherGeneral);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout->addWidget(label);

        gridSize = new Gui::PrefQuantitySpinBox(SketcherGui__TaskSketcherGeneral);
        gridSize->setObjectName(QString::fromUtf8("gridSize"));
        gridSize->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        gridSize->setProperty("decimals", QVariant(3));
        gridSize->setProperty("maximum", QVariant(1e+08));
        gridSize->setProperty("minimum", QVariant(0.001));
        gridSize->setProperty("singleStep", QVariant(1));
        gridSize->setProperty("value", QVariant(1e-07));

        horizontalLayout->addWidget(gridSize);


        verticalLayout->addLayout(horizontalLayout);

        checkBoxGridSnap = new QCheckBox(SketcherGui__TaskSketcherGeneral);
        checkBoxGridSnap->setObjectName(QString::fromUtf8("checkBoxGridSnap"));
        checkBoxGridSnap->setEnabled(true);

        verticalLayout->addWidget(checkBoxGridSnap);

        checkBoxAutoconstraints = new QCheckBox(SketcherGui__TaskSketcherGeneral);
        checkBoxAutoconstraints->setObjectName(QString::fromUtf8("checkBoxAutoconstraints"));
        checkBoxAutoconstraints->setEnabled(true);
        checkBoxAutoconstraints->setChecked(true);

        verticalLayout->addWidget(checkBoxAutoconstraints);


        retranslateUi(SketcherGui__TaskSketcherGeneral);

        QMetaObject::connectSlotsByName(SketcherGui__TaskSketcherGeneral);
    } // setupUi

    void retranslateUi(QWidget *SketcherGui__TaskSketcherGeneral)
    {
        SketcherGui__TaskSketcherGeneral->setWindowTitle(QApplication::translate("SketcherGui::TaskSketcherGeneral", "Form", 0, QApplication::UnicodeUTF8));
        checkBoxShowGrid->setText(QApplication::translate("SketcherGui::TaskSketcherGeneral", "Show grid", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("SketcherGui::TaskSketcherGeneral", "Grid size:", 0, QApplication::UnicodeUTF8));
        checkBoxGridSnap->setText(QApplication::translate("SketcherGui::TaskSketcherGeneral", "Grid snap", 0, QApplication::UnicodeUTF8));
        checkBoxAutoconstraints->setText(QApplication::translate("SketcherGui::TaskSketcherGeneral", "Auto constraints", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace SketcherGui

namespace SketcherGui {
namespace Ui {
    class TaskSketcherGeneral: public Ui_TaskSketcherGeneral {};
} // namespace Ui
} // namespace SketcherGui

#endif // UI_TASKSKETCHERGENERAL_H
