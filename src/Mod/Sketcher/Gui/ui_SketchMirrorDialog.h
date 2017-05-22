/********************************************************************************
** Form generated from reading UI file 'SketchMirrorDialog.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SKETCHMIRRORDIALOG_H
#define UI_SKETCHMIRRORDIALOG_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDialog>
#include <QtGui/QDialogButtonBox>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHeaderView>
#include <QtGui/QRadioButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QVBoxLayout>

namespace SketcherGui {

class Ui_SketchMirrorDialog
{
public:
    QGridLayout *gridLayout;
    QGroupBox *groupBox;
    QVBoxLayout *verticalLayout;
    QRadioButton *XAxisRadioButton;
    QRadioButton *YAxisRadioButton;
    QRadioButton *OriginRadioButton;
    QDialogButtonBox *buttonBox;
    QSpacerItem *verticalSpacer;

    void setupUi(QDialog *SketcherGui__SketchMirrorDialog)
    {
        if (SketcherGui__SketchMirrorDialog->objectName().isEmpty())
            SketcherGui__SketchMirrorDialog->setObjectName(QString::fromUtf8("SketcherGui__SketchMirrorDialog"));
        SketcherGui__SketchMirrorDialog->resize(220, 171);
        gridLayout = new QGridLayout(SketcherGui__SketchMirrorDialog);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        groupBox = new QGroupBox(SketcherGui__SketchMirrorDialog);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        verticalLayout = new QVBoxLayout(groupBox);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        XAxisRadioButton = new QRadioButton(groupBox);
        XAxisRadioButton->setObjectName(QString::fromUtf8("XAxisRadioButton"));
        XAxisRadioButton->setChecked(true);

        verticalLayout->addWidget(XAxisRadioButton);

        YAxisRadioButton = new QRadioButton(groupBox);
        YAxisRadioButton->setObjectName(QString::fromUtf8("YAxisRadioButton"));

        verticalLayout->addWidget(YAxisRadioButton);

        OriginRadioButton = new QRadioButton(groupBox);
        OriginRadioButton->setObjectName(QString::fromUtf8("OriginRadioButton"));

        verticalLayout->addWidget(OriginRadioButton);


        gridLayout->addWidget(groupBox, 0, 0, 1, 1);

        buttonBox = new QDialogButtonBox(SketcherGui__SketchMirrorDialog);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        gridLayout->addWidget(buttonBox, 2, 0, 1, 2);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer, 1, 0, 1, 1);


        retranslateUi(SketcherGui__SketchMirrorDialog);
        QObject::connect(buttonBox, SIGNAL(accepted()), SketcherGui__SketchMirrorDialog, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), SketcherGui__SketchMirrorDialog, SLOT(reject()));

        QMetaObject::connectSlotsByName(SketcherGui__SketchMirrorDialog);
    } // setupUi

    void retranslateUi(QDialog *SketcherGui__SketchMirrorDialog)
    {
        SketcherGui__SketchMirrorDialog->setWindowTitle(QApplication::translate("SketcherGui::SketchMirrorDialog", "Select Mirror Axis/Point", 0, QApplication::UnicodeUTF8));
        groupBox->setTitle(QApplication::translate("SketcherGui::SketchMirrorDialog", "Select Mirror Axis/Point", 0, QApplication::UnicodeUTF8));
        XAxisRadioButton->setText(QApplication::translate("SketcherGui::SketchMirrorDialog", "X-Axis", 0, QApplication::UnicodeUTF8));
        YAxisRadioButton->setText(QApplication::translate("SketcherGui::SketchMirrorDialog", "Y-Axis", 0, QApplication::UnicodeUTF8));
        OriginRadioButton->setText(QApplication::translate("SketcherGui::SketchMirrorDialog", "Origin", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace SketcherGui

namespace SketcherGui {
namespace Ui {
    class SketchMirrorDialog: public Ui_SketchMirrorDialog {};
} // namespace Ui
} // namespace SketcherGui

#endif // UI_SKETCHMIRRORDIALOG_H
