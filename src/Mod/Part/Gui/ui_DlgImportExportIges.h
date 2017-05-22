/********************************************************************************
** Form generated from reading UI file 'DlgImportExportIges.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DLGIMPORTEXPORTIGES_H
#define UI_DLGIMPORTEXPORTIGES_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QCheckBox>
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

class Ui_DlgImportExportIges
{
public:
    QGridLayout *gridLayout_5;
    QGroupBox *groupBox;
    QGridLayout *gridLayout_4;
    QLabel *label;
    QSpacerItem *spacerItem;
    QComboBox *comboBoxUnits;
    QGroupBox *groupBox_3;
    QGridLayout *gridLayout;
    QRadioButton *radioButtonBRepOff;
    QRadioButton *radioButtonBRepOn;
    QGroupBox *groupBox_2;
    QGridLayout *gridLayout_3;
    QCheckBox *checkSkipBlank;
    QGroupBox *groupBoxHeader;
    QGridLayout *gridLayout_2;
    QLabel *label_2;
    QLineEdit *lineEditCompany;
    QLabel *label_3;
    QLineEdit *lineEditProduct;
    QLineEdit *lineEditAuthor;
    QLabel *label_4;
    QSpacerItem *verticalSpacer;

    void setupUi(QWidget *PartGui__DlgImportExportIges)
    {
        if (PartGui__DlgImportExportIges->objectName().isEmpty())
            PartGui__DlgImportExportIges->setObjectName(QString::fromUtf8("PartGui__DlgImportExportIges"));
        PartGui__DlgImportExportIges->resize(515, 446);
        gridLayout_5 = new QGridLayout(PartGui__DlgImportExportIges);
        gridLayout_5->setObjectName(QString::fromUtf8("gridLayout_5"));
        groupBox = new QGroupBox(PartGui__DlgImportExportIges);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        gridLayout_4 = new QGridLayout(groupBox);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        label = new QLabel(groupBox);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout_4->addWidget(label, 0, 0, 1, 1);

        spacerItem = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_4->addItem(spacerItem, 0, 1, 1, 1);

        comboBoxUnits = new QComboBox(groupBox);
        comboBoxUnits->setObjectName(QString::fromUtf8("comboBoxUnits"));

        gridLayout_4->addWidget(comboBoxUnits, 0, 2, 1, 1);

        groupBox_3 = new QGroupBox(groupBox);
        groupBox_3->setObjectName(QString::fromUtf8("groupBox_3"));
        gridLayout = new QGridLayout(groupBox_3);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        radioButtonBRepOff = new QRadioButton(groupBox_3);
        radioButtonBRepOff->setObjectName(QString::fromUtf8("radioButtonBRepOff"));
        radioButtonBRepOff->setChecked(true);

        gridLayout->addWidget(radioButtonBRepOff, 0, 0, 1, 1);

        radioButtonBRepOn = new QRadioButton(groupBox_3);
        radioButtonBRepOn->setObjectName(QString::fromUtf8("radioButtonBRepOn"));

        gridLayout->addWidget(radioButtonBRepOn, 1, 0, 1, 1);


        gridLayout_4->addWidget(groupBox_3, 1, 0, 1, 3);


        gridLayout_5->addWidget(groupBox, 0, 0, 1, 1);

        groupBox_2 = new QGroupBox(PartGui__DlgImportExportIges);
        groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
        gridLayout_3 = new QGridLayout(groupBox_2);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        checkSkipBlank = new QCheckBox(groupBox_2);
        checkSkipBlank->setObjectName(QString::fromUtf8("checkSkipBlank"));

        gridLayout_3->addWidget(checkSkipBlank, 0, 0, 1, 1);


        gridLayout_5->addWidget(groupBox_2, 1, 0, 1, 1);

        groupBoxHeader = new QGroupBox(PartGui__DlgImportExportIges);
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

        gridLayout_2->addWidget(label_3, 2, 0, 1, 1);

        lineEditProduct = new QLineEdit(groupBoxHeader);
        lineEditProduct->setObjectName(QString::fromUtf8("lineEditProduct"));

        gridLayout_2->addWidget(lineEditProduct, 2, 1, 1, 1);

        lineEditAuthor = new QLineEdit(groupBoxHeader);
        lineEditAuthor->setObjectName(QString::fromUtf8("lineEditAuthor"));

        gridLayout_2->addWidget(lineEditAuthor, 1, 1, 1, 1);

        label_4 = new QLabel(groupBoxHeader);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout_2->addWidget(label_4, 1, 0, 1, 1);


        gridLayout_5->addWidget(groupBoxHeader, 2, 0, 1, 1);

        verticalSpacer = new QSpacerItem(20, 82, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_5->addItem(verticalSpacer, 3, 0, 1, 1);

        QWidget::setTabOrder(comboBoxUnits, radioButtonBRepOff);
        QWidget::setTabOrder(radioButtonBRepOff, radioButtonBRepOn);
        QWidget::setTabOrder(radioButtonBRepOn, checkSkipBlank);
        QWidget::setTabOrder(checkSkipBlank, lineEditCompany);
        QWidget::setTabOrder(lineEditCompany, lineEditAuthor);
        QWidget::setTabOrder(lineEditAuthor, lineEditProduct);

        retranslateUi(PartGui__DlgImportExportIges);

        QMetaObject::connectSlotsByName(PartGui__DlgImportExportIges);
    } // setupUi

    void retranslateUi(QWidget *PartGui__DlgImportExportIges)
    {
        PartGui__DlgImportExportIges->setWindowTitle(QApplication::translate("PartGui::DlgImportExportIges", "IGES", 0, QApplication::UnicodeUTF8));
        groupBox->setTitle(QApplication::translate("PartGui::DlgImportExportIges", "Export", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("PartGui::DlgImportExportIges", "Units for export of IGES", 0, QApplication::UnicodeUTF8));
        comboBoxUnits->clear();
        comboBoxUnits->insertItems(0, QStringList()
         << QApplication::translate("PartGui::DlgImportExportIges", "Millimeter", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("PartGui::DlgImportExportIges", "Meter", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("PartGui::DlgImportExportIges", "Inch", 0, QApplication::UnicodeUTF8)
        );
        groupBox_3->setTitle(QApplication::translate("PartGui::DlgImportExportIges", "Write solids and shells as", 0, QApplication::UnicodeUTF8));
        radioButtonBRepOff->setText(QApplication::translate("PartGui::DlgImportExportIges", "Groups of Trimmed Surfaces (type 144)", 0, QApplication::UnicodeUTF8));
        radioButtonBRepOn->setText(QApplication::translate("PartGui::DlgImportExportIges", "Solids (type 186) and Shells (type 514) / B-REP mode", 0, QApplication::UnicodeUTF8));
        groupBox_2->setTitle(QApplication::translate("PartGui::DlgImportExportIges", "Import", 0, QApplication::UnicodeUTF8));
        checkSkipBlank->setText(QApplication::translate("PartGui::DlgImportExportIges", "Skip blank entities", 0, QApplication::UnicodeUTF8));
        groupBoxHeader->setTitle(QApplication::translate("PartGui::DlgImportExportIges", "Header", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("PartGui::DlgImportExportIges", "Company", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("PartGui::DlgImportExportIges", "Product", 0, QApplication::UnicodeUTF8));
        label_4->setText(QApplication::translate("PartGui::DlgImportExportIges", "Author", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace PartGui

namespace PartGui {
namespace Ui {
    class DlgImportExportIges: public Ui_DlgImportExportIges {};
} // namespace Ui
} // namespace PartGui

#endif // UI_DLGIMPORTEXPORTIGES_H
