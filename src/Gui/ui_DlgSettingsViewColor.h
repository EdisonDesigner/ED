/********************************************************************************
** Form generated from reading UI file 'DlgSettingsViewColor.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DLGSETTINGSVIEWCOLOR_H
#define UI_DLGSETTINGSVIEWCOLOR_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHeaderView>
#include <QtGui/QSpacerItem>
#include <QtGui/QWidget>
#include "PrefWidgets.h"
#include "Widgets.h"

namespace Gui {
namespace Dialog {

class Ui_DlgSettingsViewColor
{
public:
    QGridLayout *gridLayout;
    QGroupBox *groupBoxSelection;
    QGridLayout *gridLayout1;
    QSpacerItem *spacer_4;
    QGridLayout *_3;
    Gui::PrefColorButton *SelectionColor;
    Gui::PrefCheckBox *checkBoxSelection;
    Gui::PrefCheckBox *checkBoxPreselection;
    Gui::PrefColorButton *HighlightColor;
    QGroupBox *groupBoxColor;
    QGridLayout *gridLayout2;
    QSpacerItem *spacer;
    QGridLayout *_4;
    QSpacerItem *spacer_2;
    Gui::PrefColorButton *SelectionColor_Background;
    Gui::PrefCheckBox *checkMidColor;
    Gui::PrefColorButton *backgroundColorTo;
    Gui::PrefColorButton *backgroundColorMid;
    Gui::PrefRadioButton *radioButtonGradient;
    Gui::PrefColorButton *backgroundColorFrom;
    Gui::PrefRadioButton *radioButtonSimple;
    QSpacerItem *spacer_3;

    void setupUi(QWidget *Gui__Dialog__DlgSettingsViewColor)
    {
        if (Gui__Dialog__DlgSettingsViewColor->objectName().isEmpty())
            Gui__Dialog__DlgSettingsViewColor->setObjectName(QString::fromUtf8("Gui__Dialog__DlgSettingsViewColor"));
        Gui__Dialog__DlgSettingsViewColor->resize(601, 598);
        gridLayout = new QGridLayout(Gui__Dialog__DlgSettingsViewColor);
#ifndef Q_OS_MAC
        gridLayout->setSpacing(6);
#endif
#ifndef Q_OS_MAC
        gridLayout->setContentsMargins(9, 9, 9, 9);
#endif
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        groupBoxSelection = new QGroupBox(Gui__Dialog__DlgSettingsViewColor);
        groupBoxSelection->setObjectName(QString::fromUtf8("groupBoxSelection"));
        gridLayout1 = new QGridLayout(groupBoxSelection);
#ifndef Q_OS_MAC
        gridLayout1->setSpacing(6);
#endif
#ifndef Q_OS_MAC
        gridLayout1->setContentsMargins(9, 9, 9, 9);
#endif
        gridLayout1->setObjectName(QString::fromUtf8("gridLayout1"));
        spacer_4 = new QSpacerItem(183, 23, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout1->addItem(spacer_4, 0, 1, 1, 1);

        _3 = new QGridLayout();
#ifndef Q_OS_MAC
        _3->setSpacing(6);
#endif
#ifndef Q_OS_MAC
        _3->setContentsMargins(0, 0, 0, 0);
#endif
        _3->setObjectName(QString::fromUtf8("_3"));
        SelectionColor = new Gui::PrefColorButton(groupBoxSelection);
        SelectionColor->setObjectName(QString::fromUtf8("SelectionColor"));
        SelectionColor->setEnabled(false);
        SelectionColor->setColor(QColor(28, 173, 28));
        SelectionColor->setProperty("prefEntry", QVariant(QByteArray("SelectionColor")));
        SelectionColor->setProperty("prefPath", QVariant(QByteArray("View")));

        _3->addWidget(SelectionColor, 1, 1, 1, 1);

        checkBoxSelection = new Gui::PrefCheckBox(groupBoxSelection);
        checkBoxSelection->setObjectName(QString::fromUtf8("checkBoxSelection"));
        checkBoxSelection->setChecked(true);
        checkBoxSelection->setProperty("prefEntry", QVariant(QByteArray("EnableSelection")));
        checkBoxSelection->setProperty("prefPath", QVariant(QByteArray("View")));

        _3->addWidget(checkBoxSelection, 1, 0, 1, 1);

        checkBoxPreselection = new Gui::PrefCheckBox(groupBoxSelection);
        checkBoxPreselection->setObjectName(QString::fromUtf8("checkBoxPreselection"));
        checkBoxPreselection->setMinimumSize(QSize(240, 0));
        checkBoxPreselection->setChecked(true);
        checkBoxPreselection->setProperty("prefEntry", QVariant(QByteArray("EnablePreselection")));
        checkBoxPreselection->setProperty("prefPath", QVariant(QByteArray("View")));

        _3->addWidget(checkBoxPreselection, 0, 0, 1, 1);

        HighlightColor = new Gui::PrefColorButton(groupBoxSelection);
        HighlightColor->setObjectName(QString::fromUtf8("HighlightColor"));
        HighlightColor->setEnabled(false);
        QSizePolicy sizePolicy(QSizePolicy::MinimumExpanding, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(HighlightColor->sizePolicy().hasHeightForWidth());
        HighlightColor->setSizePolicy(sizePolicy);
        HighlightColor->setColor(QColor(225, 225, 20));
        HighlightColor->setProperty("prefEntry", QVariant(QByteArray("HighlightColor")));
        HighlightColor->setProperty("prefPath", QVariant(QByteArray("View")));

        _3->addWidget(HighlightColor, 0, 1, 1, 1);


        gridLayout1->addLayout(_3, 0, 0, 1, 1);


        gridLayout->addWidget(groupBoxSelection, 0, 0, 1, 1);

        groupBoxColor = new QGroupBox(Gui__Dialog__DlgSettingsViewColor);
        groupBoxColor->setObjectName(QString::fromUtf8("groupBoxColor"));
        gridLayout2 = new QGridLayout(groupBoxColor);
#ifndef Q_OS_MAC
        gridLayout2->setSpacing(6);
#endif
#ifndef Q_OS_MAC
        gridLayout2->setContentsMargins(9, 9, 9, 9);
#endif
        gridLayout2->setObjectName(QString::fromUtf8("gridLayout2"));
        spacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout2->addItem(spacer, 0, 1, 1, 1);

        _4 = new QGridLayout();
#ifndef Q_OS_MAC
        _4->setSpacing(6);
#endif
#ifndef Q_OS_MAC
        _4->setContentsMargins(0, 0, 0, 0);
#endif
        _4->setObjectName(QString::fromUtf8("_4"));
        spacer_2 = new QSpacerItem(171, 20, QSizePolicy::Minimum, QSizePolicy::Minimum);

        _4->addItem(spacer_2, 2, 0, 1, 1);

        SelectionColor_Background = new Gui::PrefColorButton(groupBoxColor);
        SelectionColor_Background->setObjectName(QString::fromUtf8("SelectionColor_Background"));
        SelectionColor_Background->setEnabled(false);
        sizePolicy.setHeightForWidth(SelectionColor_Background->sizePolicy().hasHeightForWidth());
        SelectionColor_Background->setSizePolicy(sizePolicy);
        SelectionColor_Background->setColor(QColor(20, 20, 163));
        SelectionColor_Background->setProperty("prefEntry", QVariant(QByteArray("BackgroundColor")));
        SelectionColor_Background->setProperty("prefPath", QVariant(QByteArray("View")));

        _4->addWidget(SelectionColor_Background, 0, 1, 1, 1);

        checkMidColor = new Gui::PrefCheckBox(groupBoxColor);
        checkMidColor->setObjectName(QString::fromUtf8("checkMidColor"));
        checkMidColor->setProperty("prefEntry", QVariant(QByteArray("UseBackgroundColorMid")));
        checkMidColor->setProperty("prefPath", QVariant(QByteArray("View")));

        _4->addWidget(checkMidColor, 3, 0, 1, 1);

        backgroundColorTo = new Gui::PrefColorButton(groupBoxColor);
        backgroundColorTo->setObjectName(QString::fromUtf8("backgroundColorTo"));
        backgroundColorTo->setColor(QColor(151, 151, 170));
        backgroundColorTo->setProperty("prefEntry", QVariant(QByteArray("BackgroundColor3")));
        backgroundColorTo->setProperty("prefPath", QVariant(QByteArray("View")));

        _4->addWidget(backgroundColorTo, 2, 1, 1, 1);

        backgroundColorMid = new Gui::PrefColorButton(groupBoxColor);
        backgroundColorMid->setObjectName(QString::fromUtf8("backgroundColorMid"));
        backgroundColorMid->setEnabled(false);
        backgroundColorMid->setColor(QColor(111, 111, 147));
        backgroundColorMid->setProperty("prefEntry", QVariant(QByteArray("BackgroundColor4")));
        backgroundColorMid->setProperty("prefPath", QVariant(QByteArray("View")));

        _4->addWidget(backgroundColorMid, 3, 1, 1, 1);

        radioButtonGradient = new Gui::PrefRadioButton(groupBoxColor);
        radioButtonGradient->setObjectName(QString::fromUtf8("radioButtonGradient"));
        radioButtonGradient->setChecked(true);
        radioButtonGradient->setProperty("prefEntry", QVariant(QByteArray("Gradient")));
        radioButtonGradient->setProperty("prefPath", QVariant(QByteArray("View")));

        _4->addWidget(radioButtonGradient, 1, 0, 1, 1);

        backgroundColorFrom = new Gui::PrefColorButton(groupBoxColor);
        backgroundColorFrom->setObjectName(QString::fromUtf8("backgroundColorFrom"));
        backgroundColorFrom->setColor(QColor(51, 51, 101));
        backgroundColorFrom->setProperty("prefEntry", QVariant(QByteArray("BackgroundColor2")));
        backgroundColorFrom->setProperty("prefPath", QVariant(QByteArray("View")));

        _4->addWidget(backgroundColorFrom, 1, 1, 1, 1);

        radioButtonSimple = new Gui::PrefRadioButton(groupBoxColor);
        radioButtonSimple->setObjectName(QString::fromUtf8("radioButtonSimple"));
        radioButtonSimple->setMinimumSize(QSize(240, 0));
        radioButtonSimple->setProperty("prefEntry", QVariant(QByteArray("Simple")));
        radioButtonSimple->setProperty("prefPath", QVariant(QByteArray("View")));

        _4->addWidget(radioButtonSimple, 0, 0, 1, 1);


        gridLayout2->addLayout(_4, 0, 0, 1, 1);


        gridLayout->addWidget(groupBoxColor, 1, 0, 1, 1);

        spacer_3 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(spacer_3, 2, 0, 1, 1);

        QWidget::setTabOrder(checkBoxPreselection, checkBoxSelection);
        QWidget::setTabOrder(checkBoxSelection, HighlightColor);
        QWidget::setTabOrder(HighlightColor, SelectionColor);
        QWidget::setTabOrder(SelectionColor, radioButtonSimple);
        QWidget::setTabOrder(radioButtonSimple, SelectionColor_Background);
        QWidget::setTabOrder(SelectionColor_Background, radioButtonGradient);
        QWidget::setTabOrder(radioButtonGradient, backgroundColorFrom);
        QWidget::setTabOrder(backgroundColorFrom, backgroundColorTo);
        QWidget::setTabOrder(backgroundColorTo, checkMidColor);
        QWidget::setTabOrder(checkMidColor, backgroundColorMid);

        retranslateUi(Gui__Dialog__DlgSettingsViewColor);
        QObject::connect(checkBoxPreselection, SIGNAL(toggled(bool)), HighlightColor, SLOT(setEnabled(bool)));
        QObject::connect(checkBoxSelection, SIGNAL(toggled(bool)), SelectionColor, SLOT(setEnabled(bool)));
        QObject::connect(checkMidColor, SIGNAL(toggled(bool)), backgroundColorMid, SLOT(setEnabled(bool)));
        QObject::connect(radioButtonSimple, SIGNAL(toggled(bool)), SelectionColor_Background, SLOT(setEnabled(bool)));
        QObject::connect(radioButtonGradient, SIGNAL(toggled(bool)), backgroundColorFrom, SLOT(setEnabled(bool)));
        QObject::connect(radioButtonGradient, SIGNAL(toggled(bool)), backgroundColorTo, SLOT(setEnabled(bool)));
        QObject::connect(radioButtonSimple, SIGNAL(toggled(bool)), checkMidColor, SLOT(setDisabled(bool)));

        QMetaObject::connectSlotsByName(Gui__Dialog__DlgSettingsViewColor);
    } // setupUi

    void retranslateUi(QWidget *Gui__Dialog__DlgSettingsViewColor)
    {
        Gui__Dialog__DlgSettingsViewColor->setWindowTitle(QApplication::translate("Gui::Dialog::DlgSettingsViewColor", "Colors", 0, QApplication::UnicodeUTF8));
        groupBoxSelection->setTitle(QApplication::translate("Gui::Dialog::DlgSettingsViewColor", "Selection", 0, QApplication::UnicodeUTF8));
        SelectionColor->setText(QString());
        checkBoxSelection->setText(QApplication::translate("Gui::Dialog::DlgSettingsViewColor", "Enable selection highlighting", 0, QApplication::UnicodeUTF8));
        checkBoxPreselection->setText(QApplication::translate("Gui::Dialog::DlgSettingsViewColor", "Enable preselection highlighting", 0, QApplication::UnicodeUTF8));
        HighlightColor->setText(QString());
        groupBoxColor->setTitle(QApplication::translate("Gui::Dialog::DlgSettingsViewColor", "Background color", 0, QApplication::UnicodeUTF8));
        SelectionColor_Background->setText(QString());
        checkMidColor->setText(QApplication::translate("Gui::Dialog::DlgSettingsViewColor", "Middle color", 0, QApplication::UnicodeUTF8));
        backgroundColorTo->setText(QString());
        backgroundColorMid->setText(QString());
        radioButtonGradient->setText(QApplication::translate("Gui::Dialog::DlgSettingsViewColor", "Color gradient", 0, QApplication::UnicodeUTF8));
        backgroundColorFrom->setText(QString());
        radioButtonSimple->setText(QApplication::translate("Gui::Dialog::DlgSettingsViewColor", "Simple color", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace Dialog
} // namespace Gui

namespace Gui {
namespace Dialog {
namespace Ui {
    class DlgSettingsViewColor: public Ui_DlgSettingsViewColor {};
} // namespace Ui
} // namespace Dialog
} // namespace Gui

#endif // UI_DLGSETTINGSVIEWCOLOR_H
