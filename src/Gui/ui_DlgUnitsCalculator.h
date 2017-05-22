/********************************************************************************
** Form generated from reading UI file 'DlgUnitsCalculator.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DLGUNITSCALCULATOR_H
#define UI_DLGUNITSCALCULATOR_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QTextEdit>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>
#include "InputField.h"

QT_BEGIN_NAMESPACE

class Ui_DlgUnitCalculator
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout_2;
    Gui::InputField *ValueInput;
    QLabel *label;
    Gui::InputField *UnitInput;
    QLabel *label_2;
    QLineEdit *ValueOutput;
    QTextEdit *textEdit;
    QHBoxLayout *horizontalLayout;
    QPushButton *pushButton_Help;
    QSpacerItem *horizontalSpacer;
    QPushButton *pushButton_Copy;
    QPushButton *pushButton_Close;

    void setupUi(QWidget *DlgUnitCalculator)
    {
        if (DlgUnitCalculator->objectName().isEmpty())
            DlgUnitCalculator->setObjectName(QString::fromUtf8("DlgUnitCalculator"));
        DlgUnitCalculator->resize(375, 139);
        verticalLayout = new QVBoxLayout(DlgUnitCalculator);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        ValueInput = new Gui::InputField(DlgUnitCalculator);
        ValueInput->setObjectName(QString::fromUtf8("ValueInput"));
        ValueInput->setMinimumSize(QSize(100, 0));

        horizontalLayout_2->addWidget(ValueInput);

        label = new QLabel(DlgUnitCalculator);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout_2->addWidget(label);

        UnitInput = new Gui::InputField(DlgUnitCalculator);
        UnitInput->setObjectName(QString::fromUtf8("UnitInput"));
        UnitInput->setMinimumSize(QSize(100, 0));

        horizontalLayout_2->addWidget(UnitInput);

        label_2 = new QLabel(DlgUnitCalculator);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout_2->addWidget(label_2);

        ValueOutput = new QLineEdit(DlgUnitCalculator);
        ValueOutput->setObjectName(QString::fromUtf8("ValueOutput"));
        ValueOutput->setMinimumSize(QSize(150, 0));
        ValueOutput->setReadOnly(true);

        horizontalLayout_2->addWidget(ValueOutput);


        verticalLayout->addLayout(horizontalLayout_2);

        textEdit = new QTextEdit(DlgUnitCalculator);
        textEdit->setObjectName(QString::fromUtf8("textEdit"));
        textEdit->setReadOnly(true);

        verticalLayout->addWidget(textEdit);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        pushButton_Help = new QPushButton(DlgUnitCalculator);
        pushButton_Help->setObjectName(QString::fromUtf8("pushButton_Help"));

        horizontalLayout->addWidget(pushButton_Help);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        pushButton_Copy = new QPushButton(DlgUnitCalculator);
        pushButton_Copy->setObjectName(QString::fromUtf8("pushButton_Copy"));

        horizontalLayout->addWidget(pushButton_Copy);

        pushButton_Close = new QPushButton(DlgUnitCalculator);
        pushButton_Close->setObjectName(QString::fromUtf8("pushButton_Close"));

        horizontalLayout->addWidget(pushButton_Close);


        verticalLayout->addLayout(horizontalLayout);


        retranslateUi(DlgUnitCalculator);

        QMetaObject::connectSlotsByName(DlgUnitCalculator);
    } // setupUi

    void retranslateUi(QWidget *DlgUnitCalculator)
    {
        DlgUnitCalculator->setWindowTitle(QApplication::translate("DlgUnitCalculator", "Units calculator", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("DlgUnitCalculator", "as:", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("DlgUnitCalculator", "=>", 0, QApplication::UnicodeUTF8));
        pushButton_Help->setText(QApplication::translate("DlgUnitCalculator", "Help", 0, QApplication::UnicodeUTF8));
        pushButton_Copy->setText(QApplication::translate("DlgUnitCalculator", "Copy", 0, QApplication::UnicodeUTF8));
        pushButton_Close->setText(QApplication::translate("DlgUnitCalculator", "Close", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class DlgUnitCalculator: public Ui_DlgUnitCalculator {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DLGUNITSCALCULATOR_H
