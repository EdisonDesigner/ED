/********************************************************************************
** Form generated from reading UI file 'DlgImportExportStep.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DLGIMPORTEXPORTSTEP_H
#define UI_DLGIMPORTEXPORTSTEP_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QComboBox>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QRadioButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QWidget>

namespace PartGui {

class Ui_DlgImportExportStep
{
public:
    QGridLayout *gridLayout_4;
    QGroupBox *groupBox;
    QGridLayout *gridLayout_3;
    QLabel *label;
    QSpacerItem *spacerItem;
    QComboBox *comboBoxUnits;
    QGroupBox *groupBox_2;
    QGridLayout *gridLayout;
    QRadioButton *radioButtonAP203;
    QRadioButton *radioButtonAP214;
    QGroupBox *groupBoxHeader;
    QGridLayout *gridLayout_2;
    QLabel *label_2;
    QLineEdit *lineEditCompany;
    QLabel *label_3;
    QLineEdit *lineEditAuthor;
    QLabel *label_4;
    QLineEdit *lineEditProduct;
    QSpacerItem *verticalSpacer;

    void setupUi(QWidget *PartGui__DlgImportExportStep)
    {
        if (PartGui__DlgImportExportStep->objectName().isEmpty())
            PartGui__DlgImportExportStep->setObjectName(QString::fromUtf8("PartGui__DlgImportExportStep"));
        PartGui__DlgImportExportStep->resize(445, 270);
        gridLayout_4 = new QGridLayout(PartGui__DlgImportExportStep);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        groupBox = new QGroupBox(PartGui__DlgImportExportStep);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        gridLayout_3 = new QGridLayout(groupBox);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        label = new QLabel(groupBox);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout_3->addWidget(label, 0, 0, 1, 1);

        spacerItem = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_3->addItem(spacerItem, 0, 1, 1, 1);

        comboBoxUnits = new QComboBox(groupBox);
        comboBoxUnits->setObjectName(QString::fromUtf8("comboBoxUnits"));

        gridLayout_3->addWidget(comboBoxUnits, 0, 2, 1, 1);

        groupBox_2 = new QGroupBox(groupBox);
        groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
        gridLayout = new QGridLayout(groupBox_2);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        radioButtonAP203 = new QRadioButton(groupBox_2);
        radioButtonAP203->setObjectName(QString::fromUtf8("radioButtonAP203"));
        radioButtonAP203->setText(QString::fromUtf8("AP 203"));
        radioButtonAP203->setChecked(true);

        gridLayout->addWidget(radioButtonAP203, 0, 0, 1, 1);

        radioButtonAP214 = new QRadioButton(groupBox_2);
        radioButtonAP214->setObjectName(QString::fromUtf8("radioButtonAP214"));
        radioButtonAP214->setText(QString::fromUtf8("AP 214"));

        gridLayout->addWidget(radioButtonAP214, 0, 1, 1, 1);


        gridLayout_3->addWidget(groupBox_2, 1, 0, 1, 3);


        gridLayout_4->addWidget(groupBox, 0, 0, 1, 1);

        groupBoxHeader = new QGroupBox(PartGui__DlgImportExportStep);
        groupBoxHeader->setObjectName(QString::fromUtf8("groupBoxHeader"));
        gridLayout_2 = new QGridLayout(groupBoxHeader);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        label_2 = new QLabel(groupBoxHeader);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout_2->addWidget(label_2, 0, 0, 1, 1);

        lineEditCompany = new QLineEdit(groupBoxHeader);
        lineEditCompany->setObjectName(QString::fromUtf8("lineEditCompany"));

        gridLayout_2->addWidget(lineEditCompany, 0, 1, 1, 1);

        label_3 = new QLabel(groupBoxHeader);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout_2->addWidget(label_3, 1, 0, 1, 1);

        lineEditAuthor = new QLineEdit(groupBoxHeader);
        lineEditAuthor->setObjectName(QString::fromUtf8("lineEditAuthor"));

        gridLayout_2->addWidget(lineEditAuthor, 1, 1, 1, 1);

        label_4 = new QLabel(groupBoxHeader);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout_2->addWidget(label_4, 2, 0, 1, 1);

        lineEditProduct = new QLineEdit(groupBoxHeader);
        lineEditProduct->setObjectName(QString::fromUtf8("lineEditProduct"));

        gridLayout_2->addWidget(lineEditProduct, 2, 1, 1, 1);


        gridLayout_4->addWidget(groupBoxHeader, 1, 0, 1, 1);

        verticalSpacer = new QSpacerItem(20, 82, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_4->addItem(verticalSpacer, 2, 0, 1, 1);

        QWidget::setTabOrder(comboBoxUnits, radioButtonAP203);
        QWidget::setTabOrder(radioButtonAP203, radioButtonAP214);
        QWidget::setTabOrder(radioButtonAP214, lineEditCompany);
        QWidget::setTabOrder(lineEditCompany, lineEditAuthor);
        QWidget::setTabOrder(lineEditAuthor, lineEditProduct);

        retranslateUi(PartGui__DlgImportExportStep);

        QMetaObject::connectSlotsByName(PartGui__DlgImportExportStep);
    } // setupUi

    void retranslateUi(QWidget *PartGui__DlgImportExportStep)
    {
        PartGui__DlgImportExportStep->setWindowTitle(QApplication::translate("PartGui::DlgImportExportStep", "STEP", 0, QApplication::UnicodeUTF8));
        groupBox->setTitle(QApplication::translate("PartGui::DlgImportExportStep", "Export", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("PartGui::DlgImportExportStep", "Units for export of STEP", 0, QApplication::UnicodeUTF8));
        comboBoxUnits->clear();
        comboBoxUnits->insertItems(0, QStringList()
         << QApplication::translate("PartGui::DlgImportExportStep", "Millimeter", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("PartGui::DlgImportExportStep", "Meter", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("PartGui::DlgImportExportStep", "Inch", 0, QApplication::UnicodeUTF8)
        );
        groupBox_2->setTitle(QApplication::translate("PartGui::DlgImportExportStep", "Scheme", 0, QApplication::UnicodeUTF8));
        groupBoxHeader->setTitle(QApplication::translate("PartGui::DlgImportExportStep", "Header", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("PartGui::DlgImportExportStep", "Company", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("PartGui::DlgImportExportStep", "Author", 0, QApplication::UnicodeUTF8));
        label_4->setText(QApplication::translate("PartGui::DlgImportExportStep", "Product", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace PartGui

namespace PartGui {
namespace Ui {
    class DlgImportExportStep: public Ui_DlgImportExportStep {};
} // namespace Ui
} // namespace PartGui

#endif // UI_DLGIMPORTEXPORTSTEP_H
