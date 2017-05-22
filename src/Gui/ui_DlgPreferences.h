/********************************************************************************
** Form generated from reading UI file 'DlgPreferences.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DLGPREFERENCES_H
#define UI_DLGPREFERENCES_H

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
#include <QtGui/QStackedWidget>

namespace Gui {
namespace Dialog {

class Ui_DlgPreferences
{
public:
    QGridLayout *gridLayout;
    QHBoxLayout *hboxLayout;
    QListWidget *listBox;
    QStackedWidget *tabWidgetStack;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *Gui__Dialog__DlgPreferences)
    {
        if (Gui__Dialog__DlgPreferences->objectName().isEmpty())
            Gui__Dialog__DlgPreferences->setObjectName(QString::fromUtf8("Gui__Dialog__DlgPreferences"));
        Gui__Dialog__DlgPreferences->resize(570, 454);
        Gui__Dialog__DlgPreferences->setSizeGripEnabled(true);
        Gui__Dialog__DlgPreferences->setModal(true);
        gridLayout = new QGridLayout(Gui__Dialog__DlgPreferences);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(9, 9, 9, 9);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        hboxLayout = new QHBoxLayout();
        hboxLayout->setSpacing(6);
        hboxLayout->setContentsMargins(0, 0, 0, 0);
        hboxLayout->setObjectName(QString::fromUtf8("hboxLayout"));
        listBox = new QListWidget(Gui__Dialog__DlgPreferences);
        listBox->setObjectName(QString::fromUtf8("listBox"));
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(listBox->sizePolicy().hasHeightForWidth());
        listBox->setSizePolicy(sizePolicy);
        listBox->setMinimumSize(QSize(120, 0));
        listBox->setMaximumSize(QSize(128, 16777215));
        listBox->setFrameShape(QFrame::StyledPanel);
        listBox->setFrameShadow(QFrame::Sunken);
        listBox->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        listBox->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        listBox->setIconSize(QSize(96, 96));
        listBox->setSpacing(12);
        listBox->setViewMode(QListView::IconMode);

        hboxLayout->addWidget(listBox);

        tabWidgetStack = new QStackedWidget(Gui__Dialog__DlgPreferences);
        tabWidgetStack->setObjectName(QString::fromUtf8("tabWidgetStack"));

        hboxLayout->addWidget(tabWidgetStack);


        gridLayout->addLayout(hboxLayout, 0, 0, 1, 1);

        buttonBox = new QDialogButtonBox(Gui__Dialog__DlgPreferences);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setStandardButtons(QDialogButtonBox::Apply|QDialogButtonBox::Cancel|QDialogButtonBox::Help|QDialogButtonBox::Ok|QDialogButtonBox::Reset);

        gridLayout->addWidget(buttonBox, 1, 0, 1, 1);


        retranslateUi(Gui__Dialog__DlgPreferences);
        QObject::connect(buttonBox, SIGNAL(accepted()), Gui__Dialog__DlgPreferences, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), Gui__Dialog__DlgPreferences, SLOT(reject()));

        QMetaObject::connectSlotsByName(Gui__Dialog__DlgPreferences);
    } // setupUi

    void retranslateUi(QDialog *Gui__Dialog__DlgPreferences)
    {
        Gui__Dialog__DlgPreferences->setWindowTitle(QApplication::translate("Gui::Dialog::DlgPreferences", "Preferences", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace Dialog
} // namespace Gui

namespace Gui {
namespace Dialog {
namespace Ui {
    class DlgPreferences: public Ui_DlgPreferences {};
} // namespace Ui
} // namespace Dialog
} // namespace Gui

#endif // UI_DLGPREFERENCES_H
