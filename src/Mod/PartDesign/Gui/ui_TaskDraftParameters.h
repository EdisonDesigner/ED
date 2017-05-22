/********************************************************************************
** Form generated from reading UI file 'TaskDraftParameters.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TASKDRAFTPARAMETERS_H
#define UI_TASKDRAFTPARAMETERS_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QCheckBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QListWidget>
#include <QtGui/QToolButton>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>
#include "Gui/QuantitySpinBox.h"

namespace PartDesignGui {

class Ui_TaskDraftParameters
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QToolButton *buttonFaceAdd;
    QToolButton *buttonFaceRemove;
    QListWidget *listWidgetFaces;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label;
    Gui::QuantitySpinBox *draftAngle;
    QHBoxLayout *horizontalLayout_3;
    QToolButton *buttonPlane;
    QLineEdit *linePlane;
    QHBoxLayout *horizontalLayout_4;
    QToolButton *buttonLine;
    QLineEdit *lineLine;
    QCheckBox *checkReverse;

    void setupUi(QWidget *PartDesignGui__TaskDraftParameters)
    {
        if (PartDesignGui__TaskDraftParameters->objectName().isEmpty())
            PartDesignGui__TaskDraftParameters->setObjectName(QString::fromUtf8("PartDesignGui__TaskDraftParameters"));
        PartDesignGui__TaskDraftParameters->resize(257, 285);
        verticalLayout = new QVBoxLayout(PartDesignGui__TaskDraftParameters);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        buttonFaceAdd = new QToolButton(PartDesignGui__TaskDraftParameters);
        buttonFaceAdd->setObjectName(QString::fromUtf8("buttonFaceAdd"));
        buttonFaceAdd->setCheckable(true);

        horizontalLayout->addWidget(buttonFaceAdd);

        buttonFaceRemove = new QToolButton(PartDesignGui__TaskDraftParameters);
        buttonFaceRemove->setObjectName(QString::fromUtf8("buttonFaceRemove"));
        buttonFaceRemove->setCheckable(true);

        horizontalLayout->addWidget(buttonFaceRemove);


        verticalLayout->addLayout(horizontalLayout);

        listWidgetFaces = new QListWidget(PartDesignGui__TaskDraftParameters);
        listWidgetFaces->setObjectName(QString::fromUtf8("listWidgetFaces"));

        verticalLayout->addWidget(listWidgetFaces);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label = new QLabel(PartDesignGui__TaskDraftParameters);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout_2->addWidget(label);

        draftAngle = new Gui::QuantitySpinBox(PartDesignGui__TaskDraftParameters);
        draftAngle->setObjectName(QString::fromUtf8("draftAngle"));
        draftAngle->setProperty("unit", QVariant(QString::fromUtf8("deg")));
        draftAngle->setMinimum(0);
        draftAngle->setMaximum(90);
        draftAngle->setSingleStep(0.1);
        draftAngle->setValue(1.5);

        horizontalLayout_2->addWidget(draftAngle);


        verticalLayout->addLayout(horizontalLayout_2);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        buttonPlane = new QToolButton(PartDesignGui__TaskDraftParameters);
        buttonPlane->setObjectName(QString::fromUtf8("buttonPlane"));
        buttonPlane->setCheckable(true);

        horizontalLayout_3->addWidget(buttonPlane);

        linePlane = new QLineEdit(PartDesignGui__TaskDraftParameters);
        linePlane->setObjectName(QString::fromUtf8("linePlane"));

        horizontalLayout_3->addWidget(linePlane);


        verticalLayout->addLayout(horizontalLayout_3);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        buttonLine = new QToolButton(PartDesignGui__TaskDraftParameters);
        buttonLine->setObjectName(QString::fromUtf8("buttonLine"));
        buttonLine->setCheckable(true);

        horizontalLayout_4->addWidget(buttonLine);

        lineLine = new QLineEdit(PartDesignGui__TaskDraftParameters);
        lineLine->setObjectName(QString::fromUtf8("lineLine"));

        horizontalLayout_4->addWidget(lineLine);


        verticalLayout->addLayout(horizontalLayout_4);

        checkReverse = new QCheckBox(PartDesignGui__TaskDraftParameters);
        checkReverse->setObjectName(QString::fromUtf8("checkReverse"));

        verticalLayout->addWidget(checkReverse);

        checkReverse->raise();
        listWidgetFaces->raise();

        retranslateUi(PartDesignGui__TaskDraftParameters);

        QMetaObject::connectSlotsByName(PartDesignGui__TaskDraftParameters);
    } // setupUi

    void retranslateUi(QWidget *PartDesignGui__TaskDraftParameters)
    {
        PartDesignGui__TaskDraftParameters->setWindowTitle(QApplication::translate("PartDesignGui::TaskDraftParameters", "Form", 0, QApplication::UnicodeUTF8));
        buttonFaceAdd->setText(QApplication::translate("PartDesignGui::TaskDraftParameters", "Add face", 0, QApplication::UnicodeUTF8));
        buttonFaceRemove->setText(QApplication::translate("PartDesignGui::TaskDraftParameters", "Remove face", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("PartDesignGui::TaskDraftParameters", "Draft angle", 0, QApplication::UnicodeUTF8));
        buttonPlane->setText(QApplication::translate("PartDesignGui::TaskDraftParameters", "Neutral plane", 0, QApplication::UnicodeUTF8));
        buttonLine->setText(QApplication::translate("PartDesignGui::TaskDraftParameters", "Pull direction", 0, QApplication::UnicodeUTF8));
        checkReverse->setText(QApplication::translate("PartDesignGui::TaskDraftParameters", "Reverse pull direction", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace PartDesignGui

namespace PartDesignGui {
namespace Ui {
    class TaskDraftParameters: public Ui_TaskDraftParameters {};
} // namespace Ui
} // namespace PartDesignGui

#endif // UI_TASKDRAFTPARAMETERS_H
