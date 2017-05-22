/********************************************************************************
** Form generated from reading UI file 'DlgMaterialProperties.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DLGMATERIALPROPERTIES_H
#define UI_DLGMATERIALPROPERTIES_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDialog>
#include <QtGui/QDialogButtonBox>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QSpacerItem>
#include <QtGui/QSpinBox>
#include "Widgets.h"

namespace Gui {
namespace Dialog {

class Ui_DlgMaterialProperties
{
public:
    QGridLayout *gridLayout;
    QGroupBox *groupBox4;
    QGridLayout *gridLayout1;
    QLabel *label;
    QLabel *textLabel3;
    QLabel *textLabel2;
    QLabel *textLabel1;
    Gui::ColorButton *emissiveColor;
    Gui::ColorButton *specularColor;
    QHBoxLayout *hboxLayout;
    QLabel *textLabel4;
    QSpacerItem *spacerItem;
    QSpinBox *shininess;
    Gui::ColorButton *diffuseColor;
    Gui::ColorButton *ambientColor;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *Gui__Dialog__DlgMaterialProperties)
    {
        if (Gui__Dialog__DlgMaterialProperties->objectName().isEmpty())
            Gui__Dialog__DlgMaterialProperties->setObjectName(QString::fromUtf8("Gui__Dialog__DlgMaterialProperties"));
        Gui__Dialog__DlgMaterialProperties->resize(292, 247);
        Gui__Dialog__DlgMaterialProperties->setSizeGripEnabled(true);
        Gui__Dialog__DlgMaterialProperties->setModal(true);
        gridLayout = new QGridLayout(Gui__Dialog__DlgMaterialProperties);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        groupBox4 = new QGroupBox(Gui__Dialog__DlgMaterialProperties);
        groupBox4->setObjectName(QString::fromUtf8("groupBox4"));
        gridLayout1 = new QGridLayout(groupBox4);
        gridLayout1->setSpacing(6);
        gridLayout1->setContentsMargins(9, 9, 9, 9);
        gridLayout1->setObjectName(QString::fromUtf8("gridLayout1"));
        label = new QLabel(groupBox4);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout1->addWidget(label, 2, 0, 1, 1);

        textLabel3 = new QLabel(groupBox4);
        textLabel3->setObjectName(QString::fromUtf8("textLabel3"));

        gridLayout1->addWidget(textLabel3, 3, 0, 1, 1);

        textLabel2 = new QLabel(groupBox4);
        textLabel2->setObjectName(QString::fromUtf8("textLabel2"));

        gridLayout1->addWidget(textLabel2, 0, 0, 1, 1);

        textLabel1 = new QLabel(groupBox4);
        textLabel1->setObjectName(QString::fromUtf8("textLabel1"));

        gridLayout1->addWidget(textLabel1, 1, 0, 1, 1);

        emissiveColor = new Gui::ColorButton(groupBox4);
        emissiveColor->setObjectName(QString::fromUtf8("emissiveColor"));

        gridLayout1->addWidget(emissiveColor, 2, 1, 1, 1);

        specularColor = new Gui::ColorButton(groupBox4);
        specularColor->setObjectName(QString::fromUtf8("specularColor"));

        gridLayout1->addWidget(specularColor, 3, 1, 1, 1);

        hboxLayout = new QHBoxLayout();
        hboxLayout->setSpacing(6);
        hboxLayout->setContentsMargins(0, 0, 0, 0);
        hboxLayout->setObjectName(QString::fromUtf8("hboxLayout"));
        textLabel4 = new QLabel(groupBox4);
        textLabel4->setObjectName(QString::fromUtf8("textLabel4"));

        hboxLayout->addWidget(textLabel4);

        spacerItem = new QSpacerItem(81, 31, QSizePolicy::Expanding, QSizePolicy::Minimum);

        hboxLayout->addItem(spacerItem);

        shininess = new QSpinBox(groupBox4);
        shininess->setObjectName(QString::fromUtf8("shininess"));

        hboxLayout->addWidget(shininess);


        gridLayout1->addLayout(hboxLayout, 4, 0, 1, 2);

        diffuseColor = new Gui::ColorButton(groupBox4);
        diffuseColor->setObjectName(QString::fromUtf8("diffuseColor"));

        gridLayout1->addWidget(diffuseColor, 1, 1, 1, 1);

        ambientColor = new Gui::ColorButton(groupBox4);
        ambientColor->setObjectName(QString::fromUtf8("ambientColor"));

        gridLayout1->addWidget(ambientColor, 0, 1, 1, 1);


        gridLayout->addWidget(groupBox4, 0, 0, 1, 1);

        buttonBox = new QDialogButtonBox(Gui__Dialog__DlgMaterialProperties);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setStandardButtons(QDialogButtonBox::Close);

        gridLayout->addWidget(buttonBox, 1, 0, 1, 1);

        QWidget::setTabOrder(ambientColor, diffuseColor);
        QWidget::setTabOrder(diffuseColor, emissiveColor);
        QWidget::setTabOrder(emissiveColor, specularColor);
        QWidget::setTabOrder(specularColor, shininess);

        retranslateUi(Gui__Dialog__DlgMaterialProperties);
        QObject::connect(buttonBox, SIGNAL(rejected()), Gui__Dialog__DlgMaterialProperties, SLOT(reject()));

        QMetaObject::connectSlotsByName(Gui__Dialog__DlgMaterialProperties);
    } // setupUi

    void retranslateUi(QDialog *Gui__Dialog__DlgMaterialProperties)
    {
        Gui__Dialog__DlgMaterialProperties->setWindowTitle(QApplication::translate("Gui::Dialog::DlgMaterialProperties", "Material properties", 0, QApplication::UnicodeUTF8));
        groupBox4->setTitle(QApplication::translate("Gui::Dialog::DlgMaterialProperties", "Material", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("Gui::Dialog::DlgMaterialProperties", "Emissive color:", 0, QApplication::UnicodeUTF8));
        textLabel3->setText(QApplication::translate("Gui::Dialog::DlgMaterialProperties", "Specular color:", 0, QApplication::UnicodeUTF8));
        textLabel2->setText(QApplication::translate("Gui::Dialog::DlgMaterialProperties", "Ambient color:", 0, QApplication::UnicodeUTF8));
        textLabel1->setText(QApplication::translate("Gui::Dialog::DlgMaterialProperties", "Diffuse color:", 0, QApplication::UnicodeUTF8));
        emissiveColor->setText(QString());
        specularColor->setText(QString());
        textLabel4->setText(QApplication::translate("Gui::Dialog::DlgMaterialProperties", "Shininess:", 0, QApplication::UnicodeUTF8));
        shininess->setSuffix(QApplication::translate("Gui::Dialog::DlgMaterialProperties", "%", 0, QApplication::UnicodeUTF8));
        diffuseColor->setText(QString());
        ambientColor->setText(QString());
    } // retranslateUi

};

} // namespace Dialog
} // namespace Gui

namespace Gui {
namespace Dialog {
namespace Ui {
    class DlgMaterialProperties: public Ui_DlgMaterialProperties {};
} // namespace Ui
} // namespace Dialog
} // namespace Gui

#endif // UI_DLGMATERIALPROPERTIES_H
