/********************************************************************************
** Form generated from reading UI file 'TaskFilletParameters.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TASKFILLETPARAMETERS_H
#define UI_TASKFILLETPARAMETERS_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>
#include "Gui/QuantitySpinBox.h"

namespace PartDesignGui {

class Ui_TaskFilletParameters
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label;
    Gui::QuantitySpinBox *filletRadius;

    void setupUi(QWidget *PartDesignGui__TaskFilletParameters)
    {
        if (PartDesignGui__TaskFilletParameters->objectName().isEmpty())
            PartDesignGui__TaskFilletParameters->setObjectName(QString::fromUtf8("PartDesignGui__TaskFilletParameters"));
        PartDesignGui__TaskFilletParameters->resize(135, 40);
        verticalLayout = new QVBoxLayout(PartDesignGui__TaskFilletParameters);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label = new QLabel(PartDesignGui__TaskFilletParameters);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout_2->addWidget(label);

        filletRadius = new Gui::QuantitySpinBox(PartDesignGui__TaskFilletParameters);
        filletRadius->setObjectName(QString::fromUtf8("filletRadius"));

        horizontalLayout_2->addWidget(filletRadius);


        verticalLayout->addLayout(horizontalLayout_2);


        retranslateUi(PartDesignGui__TaskFilletParameters);

        QMetaObject::connectSlotsByName(PartDesignGui__TaskFilletParameters);
    } // setupUi

    void retranslateUi(QWidget *PartDesignGui__TaskFilletParameters)
    {
        PartDesignGui__TaskFilletParameters->setWindowTitle(QApplication::translate("PartDesignGui::TaskFilletParameters", "Form", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("PartDesignGui::TaskFilletParameters", "Radius:", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace PartDesignGui

namespace PartDesignGui {
namespace Ui {
    class TaskFilletParameters: public Ui_TaskFilletParameters {};
} // namespace Ui
} // namespace PartDesignGui

#endif // UI_TASKFILLETPARAMETERS_H
