/********************************************************************************
** Form generated from reading UI file 'DlgChooseIcon.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DLGCHOOSEICON_H
#define UI_DLGCHOOSEICON_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDialog>
#include <QtGui/QDialogButtonBox>
#include <QtGui/QGridLayout>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QListWidget>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>

namespace Gui {
namespace Dialog {

class Ui_DlgChooseIcon
{
public:
    QGridLayout *gridLayout;
    QListWidget *listWidget;
    QHBoxLayout *horizontalLayout;
    QPushButton *addButton;
    QSpacerItem *spacerItem;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *Gui__Dialog__DlgChooseIcon)
    {
        if (Gui__Dialog__DlgChooseIcon->objectName().isEmpty())
            Gui__Dialog__DlgChooseIcon->setObjectName(QString::fromUtf8("Gui__Dialog__DlgChooseIcon"));
        Gui__Dialog__DlgChooseIcon->resize(430, 370);
        gridLayout = new QGridLayout(Gui__Dialog__DlgChooseIcon);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        listWidget = new QListWidget(Gui__Dialog__DlgChooseIcon);
        listWidget->setObjectName(QString::fromUtf8("listWidget"));
        listWidget->setGridSize(QSize(50, 50));
        listWidget->setViewMode(QListView::IconMode);
        listWidget->setUniformItemSizes(false);

        gridLayout->addWidget(listWidget, 0, 0, 1, 1);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        addButton = new QPushButton(Gui__Dialog__DlgChooseIcon);
        addButton->setObjectName(QString::fromUtf8("addButton"));

        horizontalLayout->addWidget(addButton);

        spacerItem = new QSpacerItem(38, 31, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(spacerItem);

        buttonBox = new QDialogButtonBox(Gui__Dialog__DlgChooseIcon);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        horizontalLayout->addWidget(buttonBox);


        gridLayout->addLayout(horizontalLayout, 1, 0, 1, 1);


        retranslateUi(Gui__Dialog__DlgChooseIcon);
        QObject::connect(buttonBox, SIGNAL(accepted()), Gui__Dialog__DlgChooseIcon, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), Gui__Dialog__DlgChooseIcon, SLOT(reject()));

        QMetaObject::connectSlotsByName(Gui__Dialog__DlgChooseIcon);
    } // setupUi

    void retranslateUi(QDialog *Gui__Dialog__DlgChooseIcon)
    {
        Gui__Dialog__DlgChooseIcon->setWindowTitle(QApplication::translate("Gui::Dialog::DlgChooseIcon", "Choose Icon", 0, QApplication::UnicodeUTF8));
        addButton->setText(QApplication::translate("Gui::Dialog::DlgChooseIcon", "Icon folders...", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace Dialog
} // namespace Gui

namespace Gui {
namespace Dialog {
namespace Ui {
    class DlgChooseIcon: public Ui_DlgChooseIcon {};
} // namespace Ui
} // namespace Dialog
} // namespace Gui

#endif // UI_DLGCHOOSEICON_H
