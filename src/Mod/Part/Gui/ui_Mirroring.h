/********************************************************************************
** Form generated from reading UI file 'Mirroring.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MIRRORING_H
#define UI_MIRRORING_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QComboBox>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QTreeWidget>
#include <QtGui/QWidget>
#include "Gui/QuantitySpinBox.h"

namespace PartGui {

class Ui_Mirroring
{
public:
    QGridLayout *gridLayout_2;
    QTreeWidget *shapes;
    QLabel *label;
    QComboBox *comboBox;
    QGroupBox *groupBox;
    QGridLayout *gridLayout;
    QLabel *label_3;
    Gui::QuantitySpinBox *baseX;
    QLabel *label_4;
    Gui::QuantitySpinBox *baseY;
    QLabel *label_5;
    Gui::QuantitySpinBox *baseZ;

    void setupUi(QWidget *PartGui__Mirroring)
    {
        if (PartGui__Mirroring->objectName().isEmpty())
            PartGui__Mirroring->setObjectName(QString::fromUtf8("PartGui__Mirroring"));
        PartGui__Mirroring->resize(279, 543);
        gridLayout_2 = new QGridLayout(PartGui__Mirroring);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        shapes = new QTreeWidget(PartGui__Mirroring);
        shapes->setObjectName(QString::fromUtf8("shapes"));
        shapes->setEditTriggers(QAbstractItemView::CurrentChanged|QAbstractItemView::EditKeyPressed);
        shapes->setSelectionMode(QAbstractItemView::ExtendedSelection);
        shapes->setRootIsDecorated(false);
        shapes->setExpandsOnDoubleClick(false);

        gridLayout_2->addWidget(shapes, 0, 0, 1, 2);

        label = new QLabel(PartGui__Mirroring);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout_2->addWidget(label, 1, 0, 1, 1);

        comboBox = new QComboBox(PartGui__Mirroring);
        comboBox->setObjectName(QString::fromUtf8("comboBox"));

        gridLayout_2->addWidget(comboBox, 1, 1, 1, 1);

        groupBox = new QGroupBox(PartGui__Mirroring);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        gridLayout = new QGridLayout(groupBox);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label_3 = new QLabel(groupBox);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        gridLayout->addWidget(label_3, 0, 0, 1, 1);

        baseX = new Gui::QuantitySpinBox(groupBox);
        baseX->setObjectName(QString::fromUtf8("baseX"));
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(baseX->sizePolicy().hasHeightForWidth());
        baseX->setSizePolicy(sizePolicy);
        baseX->setProperty("unit", QVariant(QString::fromUtf8("mm")));

        gridLayout->addWidget(baseX, 0, 1, 1, 1);

        label_4 = new QLabel(groupBox);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        gridLayout->addWidget(label_4, 1, 0, 1, 1);

        baseY = new Gui::QuantitySpinBox(groupBox);
        baseY->setObjectName(QString::fromUtf8("baseY"));
        sizePolicy.setHeightForWidth(baseY->sizePolicy().hasHeightForWidth());
        baseY->setSizePolicy(sizePolicy);
        baseY->setProperty("unit", QVariant(QString::fromUtf8("mm")));

        gridLayout->addWidget(baseY, 1, 1, 1, 1);

        label_5 = new QLabel(groupBox);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        gridLayout->addWidget(label_5, 2, 0, 1, 1);

        baseZ = new Gui::QuantitySpinBox(groupBox);
        baseZ->setObjectName(QString::fromUtf8("baseZ"));
        sizePolicy.setHeightForWidth(baseZ->sizePolicy().hasHeightForWidth());
        baseZ->setSizePolicy(sizePolicy);
        baseZ->setProperty("unit", QVariant(QString::fromUtf8("mm")));

        gridLayout->addWidget(baseZ, 2, 1, 1, 1);


        gridLayout_2->addWidget(groupBox, 2, 0, 1, 2);


        retranslateUi(PartGui__Mirroring);

        QMetaObject::connectSlotsByName(PartGui__Mirroring);
    } // setupUi

    void retranslateUi(QWidget *PartGui__Mirroring)
    {
        PartGui__Mirroring->setWindowTitle(QApplication::translate("PartGui::Mirroring", "Mirroring", 0, QApplication::UnicodeUTF8));
        QTreeWidgetItem *___qtreewidgetitem = shapes->headerItem();
        ___qtreewidgetitem->setText(0, QApplication::translate("PartGui::Mirroring", "Shapes", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("PartGui::Mirroring", "Mirror plane:", 0, QApplication::UnicodeUTF8));
        comboBox->clear();
        comboBox->insertItems(0, QStringList()
         << QApplication::translate("PartGui::Mirroring", "XY plane", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("PartGui::Mirroring", "XZ plane", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("PartGui::Mirroring", "YZ plane", 0, QApplication::UnicodeUTF8)
        );
        groupBox->setTitle(QApplication::translate("PartGui::Mirroring", "Base point", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("PartGui::Mirroring", "x", 0, QApplication::UnicodeUTF8));
        label_4->setText(QApplication::translate("PartGui::Mirroring", "y", 0, QApplication::UnicodeUTF8));
        label_5->setText(QApplication::translate("PartGui::Mirroring", "z", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace PartGui

namespace PartGui {
namespace Ui {
    class Mirroring: public Ui_Mirroring {};
} // namespace Ui
} // namespace PartGui

#endif // UI_MIRRORING_H
