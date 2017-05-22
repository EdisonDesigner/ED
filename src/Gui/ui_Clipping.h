/********************************************************************************
** Form generated from reading UI file 'Clipping.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CLIPPING_H
#define UI_CLIPPING_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QCheckBox>
#include <QtGui/QDoubleSpinBox>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QWidget>

namespace Gui {
namespace Dialog {

class Ui_Clipping
{
public:
    QGridLayout *gridLayout_5;
    QGroupBox *groupBoxX;
    QGridLayout *gridLayout;
    QDoubleSpinBox *clipX;
    QPushButton *flipClipX;
    QSpacerItem *horizontalSpacer_2;
    QLabel *label;
    QGroupBox *groupBoxY;
    QGridLayout *gridLayout_2;
    QDoubleSpinBox *clipY;
    QPushButton *flipClipY;
    QSpacerItem *horizontalSpacer_3;
    QLabel *label_2;
    QGroupBox *groupBoxZ;
    QGridLayout *gridLayout_3;
    QDoubleSpinBox *clipZ;
    QPushButton *flipClipZ;
    QSpacerItem *horizontalSpacer_4;
    QLabel *label_3;
    QGroupBox *groupBoxView;
    QGridLayout *gridLayout_6;
    QSpacerItem *horizontalSpacer;
    QPushButton *fromView;
    QCheckBox *adjustViewdirection;
    QGroupBox *groupBox;
    QGridLayout *gridLayout_4;
    QDoubleSpinBox *dirX;
    QDoubleSpinBox *dirY;
    QDoubleSpinBox *dirZ;
    QLabel *label_4;
    QDoubleSpinBox *clipView;

    void setupUi(QWidget *Gui__Dialog__Clipping)
    {
        if (Gui__Dialog__Clipping->objectName().isEmpty())
            Gui__Dialog__Clipping->setObjectName(QString::fromUtf8("Gui__Dialog__Clipping"));
        Gui__Dialog__Clipping->resize(304, 430);
        gridLayout_5 = new QGridLayout(Gui__Dialog__Clipping);
        gridLayout_5->setObjectName(QString::fromUtf8("gridLayout_5"));
        groupBoxX = new QGroupBox(Gui__Dialog__Clipping);
        groupBoxX->setObjectName(QString::fromUtf8("groupBoxX"));
        groupBoxX->setCheckable(true);
        groupBoxX->setChecked(false);
        gridLayout = new QGridLayout(groupBoxX);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        clipX = new QDoubleSpinBox(groupBoxX);
        clipX->setObjectName(QString::fromUtf8("clipX"));

        gridLayout->addWidget(clipX, 0, 1, 1, 1);

        flipClipX = new QPushButton(groupBoxX);
        flipClipX->setObjectName(QString::fromUtf8("flipClipX"));

        gridLayout->addWidget(flipClipX, 0, 3, 1, 1);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_2, 0, 2, 1, 1);

        label = new QLabel(groupBoxX);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout->addWidget(label, 0, 0, 1, 1);


        gridLayout_5->addWidget(groupBoxX, 0, 0, 1, 1);

        groupBoxY = new QGroupBox(Gui__Dialog__Clipping);
        groupBoxY->setObjectName(QString::fromUtf8("groupBoxY"));
        groupBoxY->setCheckable(true);
        groupBoxY->setChecked(false);
        gridLayout_2 = new QGridLayout(groupBoxY);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        clipY = new QDoubleSpinBox(groupBoxY);
        clipY->setObjectName(QString::fromUtf8("clipY"));

        gridLayout_2->addWidget(clipY, 0, 1, 1, 1);

        flipClipY = new QPushButton(groupBoxY);
        flipClipY->setObjectName(QString::fromUtf8("flipClipY"));

        gridLayout_2->addWidget(flipClipY, 0, 3, 1, 1);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer_3, 0, 2, 1, 1);

        label_2 = new QLabel(groupBoxY);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout_2->addWidget(label_2, 0, 0, 1, 1);


        gridLayout_5->addWidget(groupBoxY, 1, 0, 1, 1);

        groupBoxZ = new QGroupBox(Gui__Dialog__Clipping);
        groupBoxZ->setObjectName(QString::fromUtf8("groupBoxZ"));
        groupBoxZ->setCheckable(true);
        groupBoxZ->setChecked(false);
        gridLayout_3 = new QGridLayout(groupBoxZ);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        clipZ = new QDoubleSpinBox(groupBoxZ);
        clipZ->setObjectName(QString::fromUtf8("clipZ"));

        gridLayout_3->addWidget(clipZ, 0, 1, 1, 1);

        flipClipZ = new QPushButton(groupBoxZ);
        flipClipZ->setObjectName(QString::fromUtf8("flipClipZ"));

        gridLayout_3->addWidget(flipClipZ, 0, 3, 1, 1);

        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_3->addItem(horizontalSpacer_4, 0, 2, 1, 1);

        label_3 = new QLabel(groupBoxZ);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout_3->addWidget(label_3, 0, 0, 1, 1);


        gridLayout_5->addWidget(groupBoxZ, 2, 0, 1, 1);

        groupBoxView = new QGroupBox(Gui__Dialog__Clipping);
        groupBoxView->setObjectName(QString::fromUtf8("groupBoxView"));
        groupBoxView->setCheckable(true);
        groupBoxView->setChecked(false);
        gridLayout_6 = new QGridLayout(groupBoxView);
        gridLayout_6->setObjectName(QString::fromUtf8("gridLayout_6"));
        horizontalSpacer = new QSpacerItem(84, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_6->addItem(horizontalSpacer, 0, 3, 1, 1);

        fromView = new QPushButton(groupBoxView);
        fromView->setObjectName(QString::fromUtf8("fromView"));

        gridLayout_6->addWidget(fromView, 0, 4, 1, 1);

        adjustViewdirection = new QCheckBox(groupBoxView);
        adjustViewdirection->setObjectName(QString::fromUtf8("adjustViewdirection"));

        gridLayout_6->addWidget(adjustViewdirection, 1, 0, 1, 5);

        groupBox = new QGroupBox(groupBoxView);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        gridLayout_4 = new QGridLayout(groupBox);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        dirX = new QDoubleSpinBox(groupBox);
        dirX->setObjectName(QString::fromUtf8("dirX"));

        gridLayout_4->addWidget(dirX, 0, 0, 1, 1);

        dirY = new QDoubleSpinBox(groupBox);
        dirY->setObjectName(QString::fromUtf8("dirY"));

        gridLayout_4->addWidget(dirY, 0, 1, 1, 1);

        dirZ = new QDoubleSpinBox(groupBox);
        dirZ->setObjectName(QString::fromUtf8("dirZ"));

        gridLayout_4->addWidget(dirZ, 0, 2, 1, 1);


        gridLayout_6->addWidget(groupBox, 2, 0, 1, 5);

        label_4 = new QLabel(groupBoxView);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout_6->addWidget(label_4, 0, 1, 1, 1);

        clipView = new QDoubleSpinBox(groupBoxView);
        clipView->setObjectName(QString::fromUtf8("clipView"));

        gridLayout_6->addWidget(clipView, 0, 2, 1, 1);


        gridLayout_5->addWidget(groupBoxView, 3, 0, 1, 1);

        QWidget::setTabOrder(groupBoxX, clipX);
        QWidget::setTabOrder(clipX, flipClipX);
        QWidget::setTabOrder(flipClipX, groupBoxY);
        QWidget::setTabOrder(groupBoxY, clipY);
        QWidget::setTabOrder(clipY, flipClipY);
        QWidget::setTabOrder(flipClipY, groupBoxZ);
        QWidget::setTabOrder(groupBoxZ, clipZ);
        QWidget::setTabOrder(clipZ, flipClipZ);
        QWidget::setTabOrder(flipClipZ, groupBoxView);
        QWidget::setTabOrder(groupBoxView, clipView);
        QWidget::setTabOrder(clipView, fromView);
        QWidget::setTabOrder(fromView, adjustViewdirection);
        QWidget::setTabOrder(adjustViewdirection, dirX);
        QWidget::setTabOrder(dirX, dirY);
        QWidget::setTabOrder(dirY, dirZ);

        retranslateUi(Gui__Dialog__Clipping);

        QMetaObject::connectSlotsByName(Gui__Dialog__Clipping);
    } // setupUi

    void retranslateUi(QWidget *Gui__Dialog__Clipping)
    {
        Gui__Dialog__Clipping->setWindowTitle(QApplication::translate("Gui::Dialog::Clipping", "Clipping", 0, QApplication::UnicodeUTF8));
        groupBoxX->setTitle(QApplication::translate("Gui::Dialog::Clipping", "Clipping X", 0, QApplication::UnicodeUTF8));
        flipClipX->setText(QApplication::translate("Gui::Dialog::Clipping", "Flip", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("Gui::Dialog::Clipping", "Offset", 0, QApplication::UnicodeUTF8));
        groupBoxY->setTitle(QApplication::translate("Gui::Dialog::Clipping", "Clipping Y", 0, QApplication::UnicodeUTF8));
        flipClipY->setText(QApplication::translate("Gui::Dialog::Clipping", "Flip", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("Gui::Dialog::Clipping", "Offset", 0, QApplication::UnicodeUTF8));
        groupBoxZ->setTitle(QApplication::translate("Gui::Dialog::Clipping", "Clipping Z", 0, QApplication::UnicodeUTF8));
        flipClipZ->setText(QApplication::translate("Gui::Dialog::Clipping", "Flip", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("Gui::Dialog::Clipping", "Offset", 0, QApplication::UnicodeUTF8));
        groupBoxView->setTitle(QApplication::translate("Gui::Dialog::Clipping", "Clipping custom direction", 0, QApplication::UnicodeUTF8));
        fromView->setText(QApplication::translate("Gui::Dialog::Clipping", "View", 0, QApplication::UnicodeUTF8));
        adjustViewdirection->setText(QApplication::translate("Gui::Dialog::Clipping", "Adjust to view direction", 0, QApplication::UnicodeUTF8));
        groupBox->setTitle(QApplication::translate("Gui::Dialog::Clipping", "Direction", 0, QApplication::UnicodeUTF8));
        label_4->setText(QApplication::translate("Gui::Dialog::Clipping", "Offset", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace Dialog
} // namespace Gui

namespace Gui {
namespace Dialog {
namespace Ui {
    class Clipping: public Ui_Clipping {};
} // namespace Ui
} // namespace Dialog
} // namespace Gui

#endif // UI_CLIPPING_H
