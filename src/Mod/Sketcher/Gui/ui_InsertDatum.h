/********************************************************************************
** Form generated from reading UI file 'InsertDatum.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_INSERTDATUM_H
#define UI_INSERTDATUM_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDialog>
#include <QtGui/QDialogButtonBox>
#include <QtGui/QGridLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QVBoxLayout>
#include "Gui/PrefWidgets.h"

namespace SketcherGui {

class Ui_InsertDatum
{
public:
    QVBoxLayout *verticalLayout;
    QGridLayout *gridLayout;
    QLabel *label;
    Gui::PrefQuantitySpinBox *labelEdit;
    QLabel *label_2;
    QLineEdit *name;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *SketcherGui__InsertDatum)
    {
        if (SketcherGui__InsertDatum->objectName().isEmpty())
            SketcherGui__InsertDatum->setObjectName(QString::fromUtf8("SketcherGui__InsertDatum"));
        SketcherGui__InsertDatum->setWindowModality(Qt::ApplicationModal);
        SketcherGui__InsertDatum->resize(344, 122);
        verticalLayout = new QVBoxLayout(SketcherGui__InsertDatum);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        gridLayout = new QGridLayout();
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label = new QLabel(SketcherGui__InsertDatum);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout->addWidget(label, 0, 0, 1, 1);

        labelEdit = new Gui::PrefQuantitySpinBox(SketcherGui__InsertDatum);
        labelEdit->setObjectName(QString::fromUtf8("labelEdit"));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(labelEdit->sizePolicy().hasHeightForWidth());
        labelEdit->setSizePolicy(sizePolicy);

        gridLayout->addWidget(labelEdit, 0, 1, 1, 1);

        label_2 = new QLabel(SketcherGui__InsertDatum);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout->addWidget(label_2, 1, 0, 1, 1);

        name = new QLineEdit(SketcherGui__InsertDatum);
        name->setObjectName(QString::fromUtf8("name"));

        gridLayout->addWidget(name, 1, 1, 1, 1);


        verticalLayout->addLayout(gridLayout);

        buttonBox = new QDialogButtonBox(SketcherGui__InsertDatum);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        verticalLayout->addWidget(buttonBox);


        retranslateUi(SketcherGui__InsertDatum);
        QObject::connect(buttonBox, SIGNAL(accepted()), SketcherGui__InsertDatum, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), SketcherGui__InsertDatum, SLOT(reject()));

        QMetaObject::connectSlotsByName(SketcherGui__InsertDatum);
    } // setupUi

    void retranslateUi(QDialog *SketcherGui__InsertDatum)
    {
        SketcherGui__InsertDatum->setWindowTitle(QApplication::translate("SketcherGui::InsertDatum", "Insert datum", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("SketcherGui::InsertDatum", "datum:", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("SketcherGui::InsertDatum", "Name (optional)", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace SketcherGui

namespace SketcherGui {
namespace Ui {
    class InsertDatum: public Ui_InsertDatum {};
} // namespace Ui
} // namespace SketcherGui

#endif // UI_INSERTDATUM_H
