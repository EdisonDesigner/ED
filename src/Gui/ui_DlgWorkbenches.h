/********************************************************************************
** Form generated from reading UI file 'DlgWorkbenches.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DLGWORKBENCHES_H
#define UI_DLGWORKBENCHES_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QGridLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>
#include "QListWidgetCustom.h"

namespace Gui {
namespace Dialog {

class Ui_DlgWorkbenches
{
public:
    QGridLayout *gridLayout;
    QVBoxLayout *vboxLayout;
    QLabel *lb_enabled;
    QListWidgetCustom *lw_enabled_workbenches;
    QSpacerItem *sp_right;
    QVBoxLayout *vboxLayout1;
    QLabel *lb_disabled;
    QListWidgetCustom *lw_disabled_workbenches;
    QSpacerItem *sp_left;
    QPushButton *shift_workbench_down_btn;
    QPushButton *remove_from_enabled_workbenches_btn;
    QPushButton *add_to_enabled_workbenches_btn;
    QPushButton *sort_enabled_workbenches_btn;
    QPushButton *shift_workbench_up_btn;
    QLabel *label;
    QPushButton *add_all_to_enabled_workbenches_btn;

    void setupUi(QWidget *Gui__Dialog__DlgWorkbenches)
    {
        if (Gui__Dialog__DlgWorkbenches->objectName().isEmpty())
            Gui__Dialog__DlgWorkbenches->setObjectName(QString::fromUtf8("Gui__Dialog__DlgWorkbenches"));
        Gui__Dialog__DlgWorkbenches->resize(421, 354);
        gridLayout = new QGridLayout(Gui__Dialog__DlgWorkbenches);
#ifndef Q_OS_MAC
        gridLayout->setSpacing(6);
#endif
#ifndef Q_OS_MAC
        gridLayout->setContentsMargins(9, 9, 9, 9);
#endif
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        vboxLayout = new QVBoxLayout();
#ifndef Q_OS_MAC
        vboxLayout->setSpacing(6);
#endif
#ifndef Q_OS_MAC
        vboxLayout->setContentsMargins(0, 0, 0, 0);
#endif
        vboxLayout->setObjectName(QString::fromUtf8("vboxLayout"));
        lb_enabled = new QLabel(Gui__Dialog__DlgWorkbenches);
        lb_enabled->setObjectName(QString::fromUtf8("lb_enabled"));

        vboxLayout->addWidget(lb_enabled);

        lw_enabled_workbenches = new QListWidgetCustom(Gui__Dialog__DlgWorkbenches);
        lw_enabled_workbenches->setObjectName(QString::fromUtf8("lw_enabled_workbenches"));

        vboxLayout->addWidget(lw_enabled_workbenches);


        gridLayout->addLayout(vboxLayout, 2, 2, 8, 1);

        sp_right = new QSpacerItem(33, 57, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(sp_right, 6, 3, 4, 1);

        vboxLayout1 = new QVBoxLayout();
#ifndef Q_OS_MAC
        vboxLayout1->setSpacing(6);
#endif
        vboxLayout1->setContentsMargins(0, 0, 0, 0);
        vboxLayout1->setObjectName(QString::fromUtf8("vboxLayout1"));
        lb_disabled = new QLabel(Gui__Dialog__DlgWorkbenches);
        lb_disabled->setObjectName(QString::fromUtf8("lb_disabled"));

        vboxLayout1->addWidget(lb_disabled);

        lw_disabled_workbenches = new QListWidgetCustom(Gui__Dialog__DlgWorkbenches);
        lw_disabled_workbenches->setObjectName(QString::fromUtf8("lw_disabled_workbenches"));

        vboxLayout1->addWidget(lw_disabled_workbenches);


        gridLayout->addLayout(vboxLayout1, 2, 0, 8, 1);

        sp_left = new QSpacerItem(33, 57, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(sp_left, 6, 1, 4, 1);

        shift_workbench_down_btn = new QPushButton(Gui__Dialog__DlgWorkbenches);
        shift_workbench_down_btn->setObjectName(QString::fromUtf8("shift_workbench_down_btn"));
        shift_workbench_down_btn->setEnabled(true);
        shift_workbench_down_btn->setMinimumSize(QSize(30, 30));
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/icons/button_down.svg"), QSize(), QIcon::Normal, QIcon::Off);
        shift_workbench_down_btn->setIcon(icon);
        shift_workbench_down_btn->setAutoDefault(true);

        gridLayout->addWidget(shift_workbench_down_btn, 5, 3, 1, 1);

        remove_from_enabled_workbenches_btn = new QPushButton(Gui__Dialog__DlgWorkbenches);
        remove_from_enabled_workbenches_btn->setObjectName(QString::fromUtf8("remove_from_enabled_workbenches_btn"));
        remove_from_enabled_workbenches_btn->setEnabled(true);
        remove_from_enabled_workbenches_btn->setMinimumSize(QSize(30, 30));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/icons/button_left.svg"), QSize(), QIcon::Normal, QIcon::Off);
        remove_from_enabled_workbenches_btn->setIcon(icon1);
        remove_from_enabled_workbenches_btn->setAutoDefault(true);
        remove_from_enabled_workbenches_btn->setDefault(false);

        gridLayout->addWidget(remove_from_enabled_workbenches_btn, 5, 1, 1, 1);

        add_to_enabled_workbenches_btn = new QPushButton(Gui__Dialog__DlgWorkbenches);
        add_to_enabled_workbenches_btn->setObjectName(QString::fromUtf8("add_to_enabled_workbenches_btn"));
        add_to_enabled_workbenches_btn->setEnabled(true);
        add_to_enabled_workbenches_btn->setMinimumSize(QSize(30, 30));
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/icons/button_right.svg"), QSize(), QIcon::Normal, QIcon::Off);
        add_to_enabled_workbenches_btn->setIcon(icon2);

        gridLayout->addWidget(add_to_enabled_workbenches_btn, 3, 1, 1, 1);

        sort_enabled_workbenches_btn = new QPushButton(Gui__Dialog__DlgWorkbenches);
        sort_enabled_workbenches_btn->setObjectName(QString::fromUtf8("sort_enabled_workbenches_btn"));
        sort_enabled_workbenches_btn->setEnabled(true);
        sort_enabled_workbenches_btn->setMinimumSize(QSize(30, 30));
        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/icons/button_sort.svg"), QSize(), QIcon::Normal, QIcon::Off);
        sort_enabled_workbenches_btn->setIcon(icon3);
        sort_enabled_workbenches_btn->setAutoDefault(true);

        gridLayout->addWidget(sort_enabled_workbenches_btn, 4, 3, 1, 1);

        shift_workbench_up_btn = new QPushButton(Gui__Dialog__DlgWorkbenches);
        shift_workbench_up_btn->setObjectName(QString::fromUtf8("shift_workbench_up_btn"));
        shift_workbench_up_btn->setEnabled(true);
        shift_workbench_up_btn->setMinimumSize(QSize(30, 30));
        QIcon icon4;
        icon4.addFile(QString::fromUtf8(":/icons/button_up.svg"), QSize(), QIcon::Normal, QIcon::Off);
        shift_workbench_up_btn->setIcon(icon4);

        gridLayout->addWidget(shift_workbench_up_btn, 3, 3, 1, 1);

        label = new QLabel(Gui__Dialog__DlgWorkbenches);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout->addWidget(label, 10, 0, 1, 4);

        add_all_to_enabled_workbenches_btn = new QPushButton(Gui__Dialog__DlgWorkbenches);
        add_all_to_enabled_workbenches_btn->setObjectName(QString::fromUtf8("add_all_to_enabled_workbenches_btn"));
        add_all_to_enabled_workbenches_btn->setEnabled(true);
        add_all_to_enabled_workbenches_btn->setMinimumSize(QSize(30, 30));
        QIcon icon5;
        icon5.addFile(QString::fromUtf8(":/icons/button_add_all.svg"), QSize(), QIcon::Normal, QIcon::Off);
        add_all_to_enabled_workbenches_btn->setIcon(icon5);
        add_all_to_enabled_workbenches_btn->setAutoDefault(true);
        add_all_to_enabled_workbenches_btn->setDefault(false);

        gridLayout->addWidget(add_all_to_enabled_workbenches_btn, 4, 1, 1, 1);


        retranslateUi(Gui__Dialog__DlgWorkbenches);

        QMetaObject::connectSlotsByName(Gui__Dialog__DlgWorkbenches);
    } // setupUi

    void retranslateUi(QWidget *Gui__Dialog__DlgWorkbenches)
    {
        Gui__Dialog__DlgWorkbenches->setWindowTitle(QApplication::translate("Gui::Dialog::DlgWorkbenches", "Workbenches", 0, QApplication::UnicodeUTF8));
        lb_enabled->setText(QApplication::translate("Gui::Dialog::DlgWorkbenches", "Enabled workbenches", 0, QApplication::UnicodeUTF8));
        lb_disabled->setText(QApplication::translate("Gui::Dialog::DlgWorkbenches", "Disabled workbenches", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        shift_workbench_down_btn->setToolTip(QApplication::translate("Gui::Dialog::DlgWorkbenches", "Move down", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_WHATSTHIS
        shift_workbench_down_btn->setWhatsThis(QApplication::translate("Gui::Dialog::DlgWorkbenches", "<html><head/><body><p><span style=\" font-weight:600;\">Move the selected item down.</span></p><p>The item will be moved down</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS
        shift_workbench_down_btn->setText(QString());
#ifndef QT_NO_TOOLTIP
        remove_from_enabled_workbenches_btn->setToolTip(QApplication::translate("Gui::Dialog::DlgWorkbenches", "Move left", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_WHATSTHIS
        remove_from_enabled_workbenches_btn->setWhatsThis(QApplication::translate("Gui::Dialog::DlgWorkbenches", "<html><head/><body><p><span style=\" font-weight:600;\">Remove the selected workbench from enabled workbenches</span></p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS
        remove_from_enabled_workbenches_btn->setText(QString());
#ifndef QT_NO_TOOLTIP
        add_to_enabled_workbenches_btn->setToolTip(QApplication::translate("Gui::Dialog::DlgWorkbenches", "Move right", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_WHATSTHIS
        add_to_enabled_workbenches_btn->setWhatsThis(QApplication::translate("Gui::Dialog::DlgWorkbenches", "<html><head/><body><p><span style=\" font-weight:600;\">Move the selected workbench to enabled workbenches.</span></p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS
        add_to_enabled_workbenches_btn->setText(QString());
#ifndef QT_NO_TOOLTIP
        sort_enabled_workbenches_btn->setToolTip(QApplication::translate("Gui::Dialog::DlgWorkbenches", "Sort enabled workbenches", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_WHATSTHIS
        sort_enabled_workbenches_btn->setWhatsThis(QApplication::translate("Gui::Dialog::DlgWorkbenches", "<b>Sort enabled workbenches</p>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS
        sort_enabled_workbenches_btn->setText(QString());
#ifndef QT_NO_TOOLTIP
        shift_workbench_up_btn->setToolTip(QApplication::translate("Gui::Dialog::DlgWorkbenches", "Move up", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_WHATSTHIS
        shift_workbench_up_btn->setWhatsThis(QApplication::translate("Gui::Dialog::DlgWorkbenches", "<html><head/><body><p><span style=\" font-weight:600;\">Move the selected item up.</span></p><p>The item will be moved up.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS
        shift_workbench_up_btn->setText(QString());
        label->setText(QApplication::translate("Gui::Dialog::DlgWorkbenches", "<html><head/><body><p><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:600;\">Note:</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\"> The changes become active the next time you start ED</span></p></body></html>", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        add_all_to_enabled_workbenches_btn->setToolTip(QApplication::translate("Gui::Dialog::DlgWorkbenches", "Add all to enabled workbenches", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_WHATSTHIS
        add_all_to_enabled_workbenches_btn->setWhatsThis(QApplication::translate("Gui::Dialog::DlgWorkbenches", "<html><head/><body><p><span style=\" font-weight:600;\">Remove the selected workbench from enabled workbenches</span></p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS
        add_all_to_enabled_workbenches_btn->setText(QString());
    } // retranslateUi

};

} // namespace Dialog
} // namespace Gui

namespace Gui {
namespace Dialog {
namespace Ui {
    class DlgWorkbenches: public Ui_DlgWorkbenches {};
} // namespace Ui
} // namespace Dialog
} // namespace Gui

#endif // UI_DLGWORKBENCHES_H
