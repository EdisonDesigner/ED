/********************************************************************************
** Form generated from reading UI file 'DlgSettingsUnits.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DLGSETTINGSUNITS_H
#define UI_DLGSETTINGSUNITS_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QComboBox>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QSpacerItem>
#include <QtGui/QSpinBox>
#include <QtGui/QTableWidget>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>

namespace Gui {
namespace Dialog {

class Ui_DlgSettingsUnits
{
public:
    QVBoxLayout *verticalLayout_2;
    QGroupBox *GroupBox6;
    QGridLayout *gridLayout;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QComboBox *comboBox_ViewSystem;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label_2;
    QSpinBox *spinBoxDecimals;
    QTableWidget *tableWidget;
    QSpacerItem *verticalSpacer;

    void setupUi(QWidget *Gui__Dialog__DlgSettingsUnits)
    {
        if (Gui__Dialog__DlgSettingsUnits->objectName().isEmpty())
            Gui__Dialog__DlgSettingsUnits->setObjectName(QString::fromUtf8("Gui__Dialog__DlgSettingsUnits"));
        Gui__Dialog__DlgSettingsUnits->resize(380, 388);
        verticalLayout_2 = new QVBoxLayout(Gui__Dialog__DlgSettingsUnits);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        GroupBox6 = new QGroupBox(Gui__Dialog__DlgSettingsUnits);
        GroupBox6->setObjectName(QString::fromUtf8("GroupBox6"));
        gridLayout = new QGridLayout(GroupBox6);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label = new QLabel(GroupBox6);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout->addWidget(label);

        comboBox_ViewSystem = new QComboBox(GroupBox6);
        comboBox_ViewSystem->setObjectName(QString::fromUtf8("comboBox_ViewSystem"));

        horizontalLayout->addWidget(comboBox_ViewSystem);


        gridLayout->addLayout(horizontalLayout, 0, 0, 1, 1);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label_2 = new QLabel(GroupBox6);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout_2->addWidget(label_2);

        spinBoxDecimals = new QSpinBox(GroupBox6);
        spinBoxDecimals->setObjectName(QString::fromUtf8("spinBoxDecimals"));
        spinBoxDecimals->setMinimum(1);
        spinBoxDecimals->setMaximum(12);

        horizontalLayout_2->addWidget(spinBoxDecimals);


        gridLayout->addLayout(horizontalLayout_2, 1, 0, 1, 1);

        tableWidget = new QTableWidget(GroupBox6);
        if (tableWidget->columnCount() < 2)
            tableWidget->setColumnCount(2);
        QTableWidgetItem *__qtablewidgetitem = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(0, __qtablewidgetitem);
        QTableWidgetItem *__qtablewidgetitem1 = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(1, __qtablewidgetitem1);
        tableWidget->setObjectName(QString::fromUtf8("tableWidget"));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::MinimumExpanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(tableWidget->sizePolicy().hasHeightForWidth());
        tableWidget->setSizePolicy(sizePolicy);
        tableWidget->setEditTriggers(QAbstractItemView::NoEditTriggers);

        gridLayout->addWidget(tableWidget, 2, 0, 1, 1);

        verticalSpacer = new QSpacerItem(20, 79, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer, 3, 0, 1, 1);


        verticalLayout_2->addWidget(GroupBox6);


        retranslateUi(Gui__Dialog__DlgSettingsUnits);

        QMetaObject::connectSlotsByName(Gui__Dialog__DlgSettingsUnits);
    } // setupUi

    void retranslateUi(QWidget *Gui__Dialog__DlgSettingsUnits)
    {
        Gui__Dialog__DlgSettingsUnits->setWindowTitle(QApplication::translate("Gui::Dialog::DlgSettingsUnits", "Units", 0, QApplication::UnicodeUTF8));
        GroupBox6->setTitle(QApplication::translate("Gui::Dialog::DlgSettingsUnits", "Units settings", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("Gui::Dialog::DlgSettingsUnits", "User system:", 0, QApplication::UnicodeUTF8));
        comboBox_ViewSystem->clear();
        comboBox_ViewSystem->insertItems(0, QStringList()
         << QApplication::translate("Gui::Dialog::DlgSettingsUnits", "Standard (mm/kg/s/degree)", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("Gui::Dialog::DlgSettingsUnits", "MKS (m/kg/s/degree)", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("Gui::Dialog::DlgSettingsUnits", "US customary (in/lb)", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("Gui::Dialog::DlgSettingsUnits", "Imperial decimal (in/lb)", 0, QApplication::UnicodeUTF8)
        );
        label_2->setText(QApplication::translate("Gui::Dialog::DlgSettingsUnits", "Number of decimals:", 0, QApplication::UnicodeUTF8));
        QTableWidgetItem *___qtablewidgetitem = tableWidget->horizontalHeaderItem(0);
        ___qtablewidgetitem->setText(QApplication::translate("Gui::Dialog::DlgSettingsUnits", "Magnitude", 0, QApplication::UnicodeUTF8));
        QTableWidgetItem *___qtablewidgetitem1 = tableWidget->horizontalHeaderItem(1);
        ___qtablewidgetitem1->setText(QApplication::translate("Gui::Dialog::DlgSettingsUnits", "Unit", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace Dialog
} // namespace Gui

namespace Gui {
namespace Dialog {
namespace Ui {
    class DlgSettingsUnits: public Ui_DlgSettingsUnits {};
} // namespace Ui
} // namespace Dialog
} // namespace Gui

#endif // UI_DLGSETTINGSUNITS_H
