/********************************************************************************
** Form generated from reading UI file 'DlgPartBox.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DLGPARTBOX_H
#define UI_DLGPARTBOX_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QComboBox>
#include <QtGui/QDialog>
#include <QtGui/QDialogButtonBox>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include "Gui/QuantitySpinBox.h"

namespace PartGui {

class Ui_DlgPartBox
{
public:
    QGridLayout *gridLayout;
    QGroupBox *GroupBox5;
    QGridLayout *gridLayout1;
    Gui::QuantitySpinBox *xPos;
    QComboBox *direction;
    Gui::QuantitySpinBox *yPos;
    Gui::QuantitySpinBox *zPos;
    QLabel *TextLabel1_3;
    QLabel *TextLabel1;
    QLabel *TextLabel2;
    QLabel *TextLabel3;
    QGroupBox *GroupBox5_2;
    QGridLayout *gridLayout2;
    Gui::QuantitySpinBox *wLength;
    Gui::QuantitySpinBox *vLength;
    Gui::QuantitySpinBox *uLength;
    QLabel *TextLabel3_2;
    QLabel *TextLabel2_2;
    QLabel *TextLabel1_2;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *PartGui__DlgPartBox)
    {
        if (PartGui__DlgPartBox->objectName().isEmpty())
            PartGui__DlgPartBox->setObjectName(QString::fromUtf8("PartGui__DlgPartBox"));
        PartGui__DlgPartBox->resize(257, 305);
        gridLayout = new QGridLayout(PartGui__DlgPartBox);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        GroupBox5 = new QGroupBox(PartGui__DlgPartBox);
        GroupBox5->setObjectName(QString::fromUtf8("GroupBox5"));
        gridLayout1 = new QGridLayout(GroupBox5);
        gridLayout1->setSpacing(6);
        gridLayout1->setContentsMargins(9, 9, 9, 9);
        gridLayout1->setObjectName(QString::fromUtf8("gridLayout1"));
        xPos = new Gui::QuantitySpinBox(GroupBox5);
        xPos->setObjectName(QString::fromUtf8("xPos"));
        xPos->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        xPos->setMinimum(-2.14748e+09);
        xPos->setMaximum(2.14748e+09);

        gridLayout1->addWidget(xPos, 0, 1, 1, 1);

        direction = new QComboBox(GroupBox5);
        direction->setObjectName(QString::fromUtf8("direction"));

        gridLayout1->addWidget(direction, 3, 1, 1, 1);

        yPos = new Gui::QuantitySpinBox(GroupBox5);
        yPos->setObjectName(QString::fromUtf8("yPos"));
        yPos->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        yPos->setMinimum(-2.14748e+09);
        yPos->setMaximum(2.14748e+09);

        gridLayout1->addWidget(yPos, 1, 1, 1, 1);

        zPos = new Gui::QuantitySpinBox(GroupBox5);
        zPos->setObjectName(QString::fromUtf8("zPos"));
        zPos->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        zPos->setMinimum(-2.14748e+09);
        zPos->setMaximum(2.14748e+09);

        gridLayout1->addWidget(zPos, 2, 1, 1, 1);

        TextLabel1_3 = new QLabel(GroupBox5);
        TextLabel1_3->setObjectName(QString::fromUtf8("TextLabel1_3"));

        gridLayout1->addWidget(TextLabel1_3, 3, 0, 1, 1);

        TextLabel1 = new QLabel(GroupBox5);
        TextLabel1->setObjectName(QString::fromUtf8("TextLabel1"));

        gridLayout1->addWidget(TextLabel1, 0, 0, 1, 1);

        TextLabel2 = new QLabel(GroupBox5);
        TextLabel2->setObjectName(QString::fromUtf8("TextLabel2"));

        gridLayout1->addWidget(TextLabel2, 1, 0, 1, 1);

        TextLabel3 = new QLabel(GroupBox5);
        TextLabel3->setObjectName(QString::fromUtf8("TextLabel3"));

        gridLayout1->addWidget(TextLabel3, 2, 0, 1, 1);


        gridLayout->addWidget(GroupBox5, 0, 0, 1, 1);

        GroupBox5_2 = new QGroupBox(PartGui__DlgPartBox);
        GroupBox5_2->setObjectName(QString::fromUtf8("GroupBox5_2"));
        gridLayout2 = new QGridLayout(GroupBox5_2);
        gridLayout2->setSpacing(6);
        gridLayout2->setContentsMargins(9, 9, 9, 9);
        gridLayout2->setObjectName(QString::fromUtf8("gridLayout2"));
        wLength = new Gui::QuantitySpinBox(GroupBox5_2);
        wLength->setObjectName(QString::fromUtf8("wLength"));
        wLength->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        wLength->setMaximum(2.14748e+09);
        wLength->setValue(100);

        gridLayout2->addWidget(wLength, 2, 1, 1, 1);

        vLength = new Gui::QuantitySpinBox(GroupBox5_2);
        vLength->setObjectName(QString::fromUtf8("vLength"));
        vLength->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        vLength->setMaximum(2.14748e+09);
        vLength->setValue(100);

        gridLayout2->addWidget(vLength, 1, 1, 1, 1);

        uLength = new Gui::QuantitySpinBox(GroupBox5_2);
        uLength->setObjectName(QString::fromUtf8("uLength"));
        uLength->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        uLength->setMaximum(2.14748e+09);
        uLength->setValue(100);

        gridLayout2->addWidget(uLength, 0, 1, 1, 1);

        TextLabel3_2 = new QLabel(GroupBox5_2);
        TextLabel3_2->setObjectName(QString::fromUtf8("TextLabel3_2"));

        gridLayout2->addWidget(TextLabel3_2, 2, 0, 1, 1);

        TextLabel2_2 = new QLabel(GroupBox5_2);
        TextLabel2_2->setObjectName(QString::fromUtf8("TextLabel2_2"));

        gridLayout2->addWidget(TextLabel2_2, 1, 0, 1, 1);

        TextLabel1_2 = new QLabel(GroupBox5_2);
        TextLabel1_2->setObjectName(QString::fromUtf8("TextLabel1_2"));

        gridLayout2->addWidget(TextLabel1_2, 0, 0, 1, 1);


        gridLayout->addWidget(GroupBox5_2, 1, 0, 1, 1);

        buttonBox = new QDialogButtonBox(PartGui__DlgPartBox);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        gridLayout->addWidget(buttonBox, 2, 0, 1, 1);

        QWidget::setTabOrder(xPos, yPos);
        QWidget::setTabOrder(yPos, zPos);
        QWidget::setTabOrder(zPos, direction);
        QWidget::setTabOrder(direction, uLength);
        QWidget::setTabOrder(uLength, vLength);
        QWidget::setTabOrder(vLength, wLength);

        retranslateUi(PartGui__DlgPartBox);
        QObject::connect(buttonBox, SIGNAL(accepted()), PartGui__DlgPartBox, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), PartGui__DlgPartBox, SLOT(reject()));

        direction->setCurrentIndex(-1);


        QMetaObject::connectSlotsByName(PartGui__DlgPartBox);
    } // setupUi

    void retranslateUi(QDialog *PartGui__DlgPartBox)
    {
        PartGui__DlgPartBox->setWindowTitle(QApplication::translate("PartGui::DlgPartBox", "Box definition", 0, QApplication::UnicodeUTF8));
        GroupBox5->setTitle(QApplication::translate("PartGui::DlgPartBox", "Position:", 0, QApplication::UnicodeUTF8));
        TextLabel1_3->setText(QApplication::translate("PartGui::DlgPartBox", "Direction:", 0, QApplication::UnicodeUTF8));
        TextLabel1->setText(QApplication::translate("PartGui::DlgPartBox", "X:", 0, QApplication::UnicodeUTF8));
        TextLabel2->setText(QApplication::translate("PartGui::DlgPartBox", "Y:", 0, QApplication::UnicodeUTF8));
        TextLabel3->setText(QApplication::translate("PartGui::DlgPartBox", "Z:", 0, QApplication::UnicodeUTF8));
        GroupBox5_2->setTitle(QApplication::translate("PartGui::DlgPartBox", "Size:", 0, QApplication::UnicodeUTF8));
        TextLabel3_2->setText(QApplication::translate("PartGui::DlgPartBox", "Height:", 0, QApplication::UnicodeUTF8));
        TextLabel2_2->setText(QApplication::translate("PartGui::DlgPartBox", "Width:", 0, QApplication::UnicodeUTF8));
        TextLabel1_2->setText(QApplication::translate("PartGui::DlgPartBox", "Length:", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace PartGui

namespace PartGui {
namespace Ui {
    class DlgPartBox: public Ui_DlgPartBox {};
} // namespace Ui
} // namespace PartGui

#endif // UI_DLGPARTBOX_H
