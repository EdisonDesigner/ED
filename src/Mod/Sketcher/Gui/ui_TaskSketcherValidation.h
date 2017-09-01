/********************************************************************************
** Form generated from reading UI file 'TaskSketcherValidation.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TASKSKETCHERVALIDATION_H
#define UI_TASKSKETCHERVALIDATION_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QComboBox>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>
#include <QtGui/QWidget>

namespace SketcherGui {

class Ui_TaskSketcherValidation
{
public:
    QGridLayout *gridLayout_3;
    QGroupBox *groupBox_2;
    QGridLayout *gridLayout_2;
    QPushButton *fixConstraint;
    QPushButton *findConstraint;
    QPushButton *delConstrExtr;
    QGroupBox *groupBox;
    QGridLayout *gridLayout;
    QLabel *label;
    QComboBox *comboBoxTolerance;
    QPushButton *findButton;
    QPushButton *fixButton;
    QGroupBox *groupBox_3;
    QGridLayout *gridLayout_4;
    QPushButton *findReversed;
    QPushButton *swapReversed;
    QGroupBox *groupBox_4;
    QGridLayout *gridLayout_5;
    QPushButton *orientLockEnable;
    QPushButton *orientLockDisable;

    void setupUi(QWidget *SketcherGui__TaskSketcherValidation)
    {
        if (SketcherGui__TaskSketcherValidation->objectName().isEmpty())
            SketcherGui__TaskSketcherValidation->setObjectName(QString::fromUtf8("SketcherGui__TaskSketcherValidation"));
        SketcherGui__TaskSketcherValidation->resize(242, 423);
        gridLayout_3 = new QGridLayout(SketcherGui__TaskSketcherValidation);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        groupBox_2 = new QGroupBox(SketcherGui__TaskSketcherValidation);
        groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
        gridLayout_2 = new QGridLayout(groupBox_2);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        fixConstraint = new QPushButton(groupBox_2);
        fixConstraint->setObjectName(QString::fromUtf8("fixConstraint"));

        gridLayout_2->addWidget(fixConstraint, 0, 1, 1, 1);

        findConstraint = new QPushButton(groupBox_2);
        findConstraint->setObjectName(QString::fromUtf8("findConstraint"));

        gridLayout_2->addWidget(findConstraint, 0, 0, 1, 1);

        delConstrExtr = new QPushButton(groupBox_2);
        delConstrExtr->setObjectName(QString::fromUtf8("delConstrExtr"));

        gridLayout_2->addWidget(delConstrExtr, 1, 0, 1, 2);


        gridLayout_3->addWidget(groupBox_2, 2, 0, 1, 1);

        groupBox = new QGroupBox(SketcherGui__TaskSketcherValidation);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        gridLayout = new QGridLayout(groupBox);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label = new QLabel(groupBox);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout->addWidget(label, 0, 0, 1, 1);

        comboBoxTolerance = new QComboBox(groupBox);
        comboBoxTolerance->setObjectName(QString::fromUtf8("comboBoxTolerance"));

        gridLayout->addWidget(comboBoxTolerance, 0, 1, 1, 1);

        findButton = new QPushButton(groupBox);
        findButton->setObjectName(QString::fromUtf8("findButton"));

        gridLayout->addWidget(findButton, 1, 0, 1, 1);

        fixButton = new QPushButton(groupBox);
        fixButton->setObjectName(QString::fromUtf8("fixButton"));

        gridLayout->addWidget(fixButton, 1, 1, 1, 1);


        gridLayout_3->addWidget(groupBox, 0, 0, 1, 1);

        groupBox_3 = new QGroupBox(SketcherGui__TaskSketcherValidation);
        groupBox_3->setObjectName(QString::fromUtf8("groupBox_3"));
        gridLayout_4 = new QGridLayout(groupBox_3);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        findReversed = new QPushButton(groupBox_3);
        findReversed->setObjectName(QString::fromUtf8("findReversed"));

        gridLayout_4->addWidget(findReversed, 0, 0, 1, 1);

        swapReversed = new QPushButton(groupBox_3);
        swapReversed->setObjectName(QString::fromUtf8("swapReversed"));

        gridLayout_4->addWidget(swapReversed, 1, 0, 1, 1);


        gridLayout_3->addWidget(groupBox_3, 4, 0, 1, 1);

        groupBox_4 = new QGroupBox(SketcherGui__TaskSketcherValidation);
        groupBox_4->setObjectName(QString::fromUtf8("groupBox_4"));
        gridLayout_5 = new QGridLayout(groupBox_4);
        gridLayout_5->setObjectName(QString::fromUtf8("gridLayout_5"));
        orientLockEnable = new QPushButton(groupBox_4);
        orientLockEnable->setObjectName(QString::fromUtf8("orientLockEnable"));

        gridLayout_5->addWidget(orientLockEnable, 0, 0, 1, 1);

        orientLockDisable = new QPushButton(groupBox_4);
        orientLockDisable->setObjectName(QString::fromUtf8("orientLockDisable"));

        gridLayout_5->addWidget(orientLockDisable, 1, 0, 1, 1);


        gridLayout_3->addWidget(groupBox_4, 5, 0, 1, 1);


        retranslateUi(SketcherGui__TaskSketcherValidation);

        QMetaObject::connectSlotsByName(SketcherGui__TaskSketcherValidation);
    } // setupUi

    void retranslateUi(QWidget *SketcherGui__TaskSketcherValidation)
    {
        SketcherGui__TaskSketcherValidation->setWindowTitle(QApplication::translate("SketcherGui::TaskSketcherValidation", "Sketcher validation", 0, QApplication::UnicodeUTF8));
        groupBox_2->setTitle(QApplication::translate("SketcherGui::TaskSketcherValidation", "Invalid constraints", 0, QApplication::UnicodeUTF8));
        fixConstraint->setText(QApplication::translate("SketcherGui::TaskSketcherValidation", "Fix", 0, QApplication::UnicodeUTF8));
        findConstraint->setText(QApplication::translate("SketcherGui::TaskSketcherValidation", "Find", 0, QApplication::UnicodeUTF8));
        delConstrExtr->setText(QApplication::translate("SketcherGui::TaskSketcherValidation", "Delete constraints to external geom.", 0, QApplication::UnicodeUTF8));
        groupBox->setTitle(QApplication::translate("SketcherGui::TaskSketcherValidation", "Missing coincidences", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("SketcherGui::TaskSketcherValidation", "Tolerance:", 0, QApplication::UnicodeUTF8));
        findButton->setText(QApplication::translate("SketcherGui::TaskSketcherValidation", "Find", 0, QApplication::UnicodeUTF8));
        fixButton->setText(QApplication::translate("SketcherGui::TaskSketcherValidation", "Fix", 0, QApplication::UnicodeUTF8));
        groupBox_3->setTitle(QApplication::translate("SketcherGui::TaskSketcherValidation", "Reversed external geometry", 0, QApplication::UnicodeUTF8));
        findReversed->setText(QApplication::translate("SketcherGui::TaskSketcherValidation", "Find", 0, QApplication::UnicodeUTF8));
        swapReversed->setText(QApplication::translate("SketcherGui::TaskSketcherValidation", "Swap endpoints in constraints", 0, QApplication::UnicodeUTF8));
        groupBox_4->setTitle(QApplication::translate("SketcherGui::TaskSketcherValidation", "Constraint orientation locking", 0, QApplication::UnicodeUTF8));
        orientLockEnable->setText(QApplication::translate("SketcherGui::TaskSketcherValidation", "Enable/Update", 0, QApplication::UnicodeUTF8));
        orientLockDisable->setText(QApplication::translate("SketcherGui::TaskSketcherValidation", "Disable", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace SketcherGui

namespace SketcherGui {
namespace Ui {
    class TaskSketcherValidation: public Ui_TaskSketcherValidation {};
} // namespace Ui
} // namespace SketcherGui

#endif // UI_TASKSKETCHERVALIDATION_H
