/********************************************************************************
** Form generated from reading UI file 'DlgActivateWindow.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DLGACTIVATEWINDOW_H
#define UI_DLGACTIVATEWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDialog>
#include <QtGui/QDialogButtonBox>
#include <QtGui/QGridLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QTreeWidget>

namespace Gui {
namespace Dialog {

class Ui_DlgActivateWindow
{
public:
    QGridLayout *gridLayout;
    QTreeWidget *treeWidget;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *Gui__Dialog__DlgActivateWindow)
    {
        if (Gui__Dialog__DlgActivateWindow->objectName().isEmpty())
            Gui__Dialog__DlgActivateWindow->setObjectName(QString::fromUtf8("Gui__Dialog__DlgActivateWindow"));
        Gui__Dialog__DlgActivateWindow->resize(341, 267);
        Gui__Dialog__DlgActivateWindow->setSizeGripEnabled(true);
        Gui__Dialog__DlgActivateWindow->setModal(true);
        gridLayout = new QGridLayout(Gui__Dialog__DlgActivateWindow);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        treeWidget = new QTreeWidget(Gui__Dialog__DlgActivateWindow);
        QTreeWidgetItem *__qtreewidgetitem = new QTreeWidgetItem();
        __qtreewidgetitem->setText(0, QString::fromUtf8("1"));
        treeWidget->setHeaderItem(__qtreewidgetitem);
        treeWidget->setObjectName(QString::fromUtf8("treeWidget"));
        treeWidget->setRootIsDecorated(false);

        gridLayout->addWidget(treeWidget, 0, 0, 1, 1);

        buttonBox = new QDialogButtonBox(Gui__Dialog__DlgActivateWindow);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        gridLayout->addWidget(buttonBox, 1, 0, 1, 1);


        retranslateUi(Gui__Dialog__DlgActivateWindow);
        QObject::connect(treeWidget, SIGNAL(activated(QModelIndex)), Gui__Dialog__DlgActivateWindow, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(accepted()), Gui__Dialog__DlgActivateWindow, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), Gui__Dialog__DlgActivateWindow, SLOT(reject()));

        QMetaObject::connectSlotsByName(Gui__Dialog__DlgActivateWindow);
    } // setupUi

    void retranslateUi(QDialog *Gui__Dialog__DlgActivateWindow)
    {
        Gui__Dialog__DlgActivateWindow->setWindowTitle(QApplication::translate("Gui::Dialog::DlgActivateWindow", "Choose Window", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace Dialog
} // namespace Gui

namespace Gui {
namespace Dialog {
namespace Ui {
    class DlgActivateWindow: public Ui_DlgActivateWindow {};
} // namespace Ui
} // namespace Dialog
} // namespace Gui

#endif // UI_DLGACTIVATEWINDOW_H
