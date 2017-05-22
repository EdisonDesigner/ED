/********************************************************************************
** Form generated from reading UI file 'DlgPartImportIges.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DLGPARTIMPORTIGES_H
#define UI_DLGPARTIMPORTIGES_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDialog>
#include <QtGui/QDialogButtonBox>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHeaderView>
#include <QtGui/QLineEdit>
#include <QtGui/QPushButton>

namespace PartGui {

class Ui_DlgPartImportIges
{
public:
    QGridLayout *gridLayout_2;
    QGroupBox *GroupBox5;
    QGridLayout *gridLayout;
    QLineEdit *FileName;
    QPushButton *SearchFile;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *PartGui__DlgPartImportIges)
    {
        if (PartGui__DlgPartImportIges->objectName().isEmpty())
            PartGui__DlgPartImportIges->setObjectName(QString::fromUtf8("PartGui__DlgPartImportIges"));
        PartGui__DlgPartImportIges->resize(342, 112);
        gridLayout_2 = new QGridLayout(PartGui__DlgPartImportIges);
        gridLayout_2->setSpacing(6);
        gridLayout_2->setContentsMargins(11, 11, 11, 11);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        GroupBox5 = new QGroupBox(PartGui__DlgPartImportIges);
        GroupBox5->setObjectName(QString::fromUtf8("GroupBox5"));
        gridLayout = new QGridLayout(GroupBox5);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        FileName = new QLineEdit(GroupBox5);
        FileName->setObjectName(QString::fromUtf8("FileName"));

        gridLayout->addWidget(FileName, 0, 0, 1, 1);

        SearchFile = new QPushButton(GroupBox5);
        SearchFile->setObjectName(QString::fromUtf8("SearchFile"));
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(SearchFile->sizePolicy().hasHeightForWidth());
        SearchFile->setSizePolicy(sizePolicy);
        SearchFile->setMinimumSize(QSize(30, 0));
        SearchFile->setMaximumSize(QSize(30, 32767));

        gridLayout->addWidget(SearchFile, 0, 1, 1, 1);


        gridLayout_2->addWidget(GroupBox5, 0, 0, 1, 1);

        buttonBox = new QDialogButtonBox(PartGui__DlgPartImportIges);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        gridLayout_2->addWidget(buttonBox, 1, 0, 1, 1);

        QWidget::setTabOrder(FileName, SearchFile);

        retranslateUi(PartGui__DlgPartImportIges);

        QMetaObject::connectSlotsByName(PartGui__DlgPartImportIges);
    } // setupUi

    void retranslateUi(QDialog *PartGui__DlgPartImportIges)
    {
        PartGui__DlgPartImportIges->setWindowTitle(QApplication::translate("PartGui::DlgPartImportIges", "IGES input file", 0, QApplication::UnicodeUTF8));
        GroupBox5->setTitle(QApplication::translate("PartGui::DlgPartImportIges", "File Name", 0, QApplication::UnicodeUTF8));
        FileName->setText(QString());
        SearchFile->setText(QApplication::translate("PartGui::DlgPartImportIges", "...", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace PartGui

namespace PartGui {
namespace Ui {
    class DlgPartImportIges: public Ui_DlgPartImportIges {};
} // namespace Ui
} // namespace PartGui

#endif // UI_DLGPARTIMPORTIGES_H
