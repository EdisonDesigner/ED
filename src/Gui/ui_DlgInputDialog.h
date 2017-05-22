/********************************************************************************
** Form generated from reading UI file 'DlgInputDialog.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DLGINPUTDIALOG_H
#define UI_DLGINPUTDIALOG_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QComboBox>
#include <QtGui/QDialog>
#include <QtGui/QDialogButtonBox>
#include <QtGui/QDoubleSpinBox>
#include <QtGui/QGridLayout>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QSpinBox>
#include <QtGui/QStackedWidget>
#include <QtGui/QWidget>
#include "SpinBox.h"

namespace Gui {
namespace Dialog {

class Ui_DlgInputDialog
{
public:
    QGridLayout *gridLayout;
    QLabel *label;
    QStackedWidget *stack;
    QWidget *WStackPage1;
    QGridLayout *gridLayout1;
    QLineEdit *lineEdit;
    QWidget *WStackPage2;
    QGridLayout *gridLayout2;
    QSpinBox *spinBox;
    QWidget *WStackPage3;
    QGridLayout *gridLayout3;
    QDoubleSpinBox *floatSpinBox;
    QWidget *WStackPage4;
    QGridLayout *gridLayout4;
    QComboBox *comboBox;
    QWidget *WStackPage5;
    QHBoxLayout *hboxLayout;
    Gui::UIntSpinBox *uIntSpinBox;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *Gui__Dialog__DlgInputDialog)
    {
        if (Gui__Dialog__DlgInputDialog->objectName().isEmpty())
            Gui__Dialog__DlgInputDialog->setObjectName(QString::fromUtf8("Gui__Dialog__DlgInputDialog"));
        Gui__Dialog__DlgInputDialog->resize(399, 99);
        Gui__Dialog__DlgInputDialog->setSizeGripEnabled(false);
        gridLayout = new QGridLayout(Gui__Dialog__DlgInputDialog);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label = new QLabel(Gui__Dialog__DlgInputDialog);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout->addWidget(label, 0, 0, 1, 1);

        stack = new QStackedWidget(Gui__Dialog__DlgInputDialog);
        stack->setObjectName(QString::fromUtf8("stack"));
        WStackPage1 = new QWidget();
        WStackPage1->setObjectName(QString::fromUtf8("WStackPage1"));
        gridLayout1 = new QGridLayout(WStackPage1);
        gridLayout1->setSpacing(6);
        gridLayout1->setContentsMargins(1, 1, 1, 1);
        gridLayout1->setObjectName(QString::fromUtf8("gridLayout1"));
        lineEdit = new QLineEdit(WStackPage1);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));

        gridLayout1->addWidget(lineEdit, 0, 0, 1, 1);

        stack->addWidget(WStackPage1);
        WStackPage2 = new QWidget();
        WStackPage2->setObjectName(QString::fromUtf8("WStackPage2"));
        gridLayout2 = new QGridLayout(WStackPage2);
        gridLayout2->setSpacing(6);
        gridLayout2->setContentsMargins(1, 1, 1, 1);
        gridLayout2->setObjectName(QString::fromUtf8("gridLayout2"));
        spinBox = new QSpinBox(WStackPage2);
        spinBox->setObjectName(QString::fromUtf8("spinBox"));

        gridLayout2->addWidget(spinBox, 0, 0, 1, 1);

        stack->addWidget(WStackPage2);
        WStackPage3 = new QWidget();
        WStackPage3->setObjectName(QString::fromUtf8("WStackPage3"));
        gridLayout3 = new QGridLayout(WStackPage3);
        gridLayout3->setSpacing(6);
        gridLayout3->setContentsMargins(1, 1, 1, 1);
        gridLayout3->setObjectName(QString::fromUtf8("gridLayout3"));
        floatSpinBox = new QDoubleSpinBox(WStackPage3);
        floatSpinBox->setObjectName(QString::fromUtf8("floatSpinBox"));

        gridLayout3->addWidget(floatSpinBox, 0, 0, 1, 1);

        stack->addWidget(WStackPage3);
        WStackPage4 = new QWidget();
        WStackPage4->setObjectName(QString::fromUtf8("WStackPage4"));
        gridLayout4 = new QGridLayout(WStackPage4);
        gridLayout4->setSpacing(6);
        gridLayout4->setContentsMargins(1, 1, 1, 1);
        gridLayout4->setObjectName(QString::fromUtf8("gridLayout4"));
        comboBox = new QComboBox(WStackPage4);
        comboBox->setObjectName(QString::fromUtf8("comboBox"));

        gridLayout4->addWidget(comboBox, 0, 0, 1, 1);

        stack->addWidget(WStackPage4);
        WStackPage5 = new QWidget();
        WStackPage5->setObjectName(QString::fromUtf8("WStackPage5"));
        hboxLayout = new QHBoxLayout(WStackPage5);
        hboxLayout->setSpacing(6);
        hboxLayout->setContentsMargins(1, 1, 1, 1);
        hboxLayout->setObjectName(QString::fromUtf8("hboxLayout"));
        uIntSpinBox = new Gui::UIntSpinBox(WStackPage5);
        uIntSpinBox->setObjectName(QString::fromUtf8("uIntSpinBox"));

        hboxLayout->addWidget(uIntSpinBox);

        stack->addWidget(WStackPage5);

        gridLayout->addWidget(stack, 1, 0, 1, 1);

        buttonBox = new QDialogButtonBox(Gui__Dialog__DlgInputDialog);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        gridLayout->addWidget(buttonBox, 2, 0, 1, 1);


        retranslateUi(Gui__Dialog__DlgInputDialog);
        QObject::connect(buttonBox, SIGNAL(accepted()), Gui__Dialog__DlgInputDialog, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), Gui__Dialog__DlgInputDialog, SLOT(reject()));

        QMetaObject::connectSlotsByName(Gui__Dialog__DlgInputDialog);
    } // setupUi

    void retranslateUi(QDialog *Gui__Dialog__DlgInputDialog)
    {
        Gui__Dialog__DlgInputDialog->setWindowTitle(QApplication::translate("Gui::Dialog::DlgInputDialog", "Input", 0, QApplication::UnicodeUTF8));
        label->setText(QString());
    } // retranslateUi

};

} // namespace Dialog
} // namespace Gui

namespace Gui {
namespace Dialog {
namespace Ui {
    class DlgInputDialog: public Ui_DlgInputDialog {};
} // namespace Ui
} // namespace Dialog
} // namespace Gui

#endif // UI_DLGINPUTDIALOG_H
