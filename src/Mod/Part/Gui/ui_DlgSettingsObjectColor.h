/********************************************************************************
** Form generated from reading UI file 'DlgSettingsObjectColor.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DLGSETTINGSOBJECTCOLOR_H
#define UI_DLGSETTINGSOBJECTCOLOR_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QSpacerItem>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>
#include "Gui/PrefWidgets.h"
#include "Gui/Widgets.h"

namespace PartGui {

class Ui_DlgSettingsObjectColor
{
public:
    QVBoxLayout *verticalLayout;
    QGroupBox *groupBoxDefaultColors;
    QHBoxLayout *horizontalLayout;
    QGridLayout *gridLayout;
    QLabel *label_6;
    Gui::PrefColorButton *DefaultShapeColor;
    QLabel *label_7;
    Gui::PrefColorButton *DefaultShapeLineColor;
    QLabel *label_9;
    Gui::PrefSpinBox *DefaultShapeLineWidth;
    QLabel *label_10;
    Gui::PrefColorButton *DefaultShapeVertexColor;
    QLabel *label_11;
    Gui::PrefSpinBox *DefaultShapeVertexWidth;
    QLabel *label_8;
    Gui::PrefColorButton *BoundingBoxColor;
    QSpacerItem *horizontalSpacer;
    QGroupBox *groupBox;
    QHBoxLayout *horizontalLayout_2;
    QGridLayout *gridLayout_2;
    QLabel *label;
    Gui::PrefColorButton *AnnotationTextColor;
    QSpacerItem *horizontalSpacer_2;
    QSpacerItem *verticalSpacer;

    void setupUi(QWidget *PartGui__DlgSettingsObjectColor)
    {
        if (PartGui__DlgSettingsObjectColor->objectName().isEmpty())
            PartGui__DlgSettingsObjectColor->setObjectName(QString::fromUtf8("PartGui__DlgSettingsObjectColor"));
        PartGui__DlgSettingsObjectColor->resize(332, 331);
        verticalLayout = new QVBoxLayout(PartGui__DlgSettingsObjectColor);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        groupBoxDefaultColors = new QGroupBox(PartGui__DlgSettingsObjectColor);
        groupBoxDefaultColors->setObjectName(QString::fromUtf8("groupBoxDefaultColors"));
        horizontalLayout = new QHBoxLayout(groupBoxDefaultColors);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        gridLayout = new QGridLayout();
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label_6 = new QLabel(groupBoxDefaultColors);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setMinimumSize(QSize(182, 0));

        gridLayout->addWidget(label_6, 0, 0, 1, 1);

        DefaultShapeColor = new Gui::PrefColorButton(groupBoxDefaultColors);
        DefaultShapeColor->setObjectName(QString::fromUtf8("DefaultShapeColor"));
        DefaultShapeColor->setColor(QColor(204, 204, 204));
        DefaultShapeColor->setProperty("prefEntry", QVariant(QByteArray("DefaultShapeColor")));
        DefaultShapeColor->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout->addWidget(DefaultShapeColor, 0, 1, 1, 1);

        label_7 = new QLabel(groupBoxDefaultColors);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setMinimumSize(QSize(182, 0));

        gridLayout->addWidget(label_7, 1, 0, 1, 1);

        DefaultShapeLineColor = new Gui::PrefColorButton(groupBoxDefaultColors);
        DefaultShapeLineColor->setObjectName(QString::fromUtf8("DefaultShapeLineColor"));
        DefaultShapeLineColor->setColor(QColor(25, 25, 25));
        DefaultShapeLineColor->setProperty("prefEntry", QVariant(QByteArray("DefaultShapeLineColor")));
        DefaultShapeLineColor->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout->addWidget(DefaultShapeLineColor, 1, 1, 1, 1);

        label_9 = new QLabel(groupBoxDefaultColors);
        label_9->setObjectName(QString::fromUtf8("label_9"));
        label_9->setMinimumSize(QSize(182, 0));

        gridLayout->addWidget(label_9, 2, 0, 1, 1);

        DefaultShapeLineWidth = new Gui::PrefSpinBox(groupBoxDefaultColors);
        DefaultShapeLineWidth->setObjectName(QString::fromUtf8("DefaultShapeLineWidth"));
        DefaultShapeLineWidth->setMaximum(9);
        DefaultShapeLineWidth->setValue(2);
        DefaultShapeLineWidth->setProperty("prefEntry", QVariant(QByteArray("DefaultShapeLineWidth")));
        DefaultShapeLineWidth->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout->addWidget(DefaultShapeLineWidth, 2, 1, 1, 1);

        label_10 = new QLabel(groupBoxDefaultColors);
        label_10->setObjectName(QString::fromUtf8("label_10"));
        label_10->setMinimumSize(QSize(182, 0));

        gridLayout->addWidget(label_10, 3, 0, 1, 1);

        DefaultShapeVertexColor = new Gui::PrefColorButton(groupBoxDefaultColors);
        DefaultShapeVertexColor->setObjectName(QString::fromUtf8("DefaultShapeVertexColor"));
        DefaultShapeVertexColor->setColor(QColor(25, 25, 25));
        DefaultShapeVertexColor->setProperty("prefEntry", QVariant(QByteArray("DefaultShapeVertexColor")));
        DefaultShapeVertexColor->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout->addWidget(DefaultShapeVertexColor, 3, 1, 1, 1);

        label_11 = new QLabel(groupBoxDefaultColors);
        label_11->setObjectName(QString::fromUtf8("label_11"));
        label_11->setMinimumSize(QSize(182, 0));

        gridLayout->addWidget(label_11, 4, 0, 1, 1);

        DefaultShapeVertexWidth = new Gui::PrefSpinBox(groupBoxDefaultColors);
        DefaultShapeVertexWidth->setObjectName(QString::fromUtf8("DefaultShapeVertexWidth"));
        DefaultShapeVertexWidth->setMaximum(9);
        DefaultShapeVertexWidth->setValue(2);
        DefaultShapeVertexWidth->setProperty("prefEntry", QVariant(QByteArray("DefaultShapeVertexWidth")));
        DefaultShapeVertexWidth->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout->addWidget(DefaultShapeVertexWidth, 4, 1, 1, 1);

        label_8 = new QLabel(groupBoxDefaultColors);
        label_8->setObjectName(QString::fromUtf8("label_8"));
        label_8->setMinimumSize(QSize(182, 0));

        gridLayout->addWidget(label_8, 5, 0, 1, 1);

        BoundingBoxColor = new Gui::PrefColorButton(groupBoxDefaultColors);
        BoundingBoxColor->setObjectName(QString::fromUtf8("BoundingBoxColor"));
        BoundingBoxColor->setColor(QColor(255, 255, 255));
        BoundingBoxColor->setProperty("prefEntry", QVariant(QByteArray("BoundingBoxColor")));
        BoundingBoxColor->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout->addWidget(BoundingBoxColor, 5, 1, 1, 1);


        horizontalLayout->addLayout(gridLayout);

        horizontalSpacer = new QSpacerItem(28, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);


        verticalLayout->addWidget(groupBoxDefaultColors);

        groupBox = new QGroupBox(PartGui__DlgSettingsObjectColor);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        horizontalLayout_2 = new QHBoxLayout(groupBox);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        gridLayout_2 = new QGridLayout();
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        label = new QLabel(groupBox);
        label->setObjectName(QString::fromUtf8("label"));
        label->setMinimumSize(QSize(182, 0));

        gridLayout_2->addWidget(label, 0, 0, 1, 1);

        AnnotationTextColor = new Gui::PrefColorButton(groupBox);
        AnnotationTextColor->setObjectName(QString::fromUtf8("AnnotationTextColor"));
        AnnotationTextColor->setProperty("prefEntry", QVariant(QByteArray("AnnotationTextColor")));
        AnnotationTextColor->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout_2->addWidget(AnnotationTextColor, 0, 1, 1, 1);


        horizontalLayout_2->addLayout(gridLayout_2);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer_2);


        verticalLayout->addWidget(groupBox);

        verticalSpacer = new QSpacerItem(20, 217, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer);

        QWidget::setTabOrder(DefaultShapeColor, DefaultShapeLineWidth);
        QWidget::setTabOrder(DefaultShapeLineWidth, DefaultShapeLineColor);
        QWidget::setTabOrder(DefaultShapeLineColor, BoundingBoxColor);

        retranslateUi(PartGui__DlgSettingsObjectColor);

        QMetaObject::connectSlotsByName(PartGui__DlgSettingsObjectColor);
    } // setupUi

    void retranslateUi(QWidget *PartGui__DlgSettingsObjectColor)
    {
        PartGui__DlgSettingsObjectColor->setWindowTitle(QApplication::translate("PartGui::DlgSettingsObjectColor", "Part colors", 0, QApplication::UnicodeUTF8));
        groupBoxDefaultColors->setTitle(QApplication::translate("PartGui::DlgSettingsObjectColor", "Default Part colors", 0, QApplication::UnicodeUTF8));
        label_6->setText(QApplication::translate("PartGui::DlgSettingsObjectColor", "Default shape color", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        DefaultShapeColor->setToolTip(QApplication::translate("PartGui::DlgSettingsObjectColor", "The default color for new shapes", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        label_7->setText(QApplication::translate("PartGui::DlgSettingsObjectColor", "Default line color", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        DefaultShapeLineColor->setToolTip(QApplication::translate("PartGui::DlgSettingsObjectColor", "The default line color for new shapes", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        label_9->setText(QApplication::translate("PartGui::DlgSettingsObjectColor", "Default line width", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        DefaultShapeLineWidth->setToolTip(QApplication::translate("PartGui::DlgSettingsObjectColor", "The default line thickness for new shapes", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        DefaultShapeLineWidth->setSuffix(QApplication::translate("PartGui::DlgSettingsObjectColor", "px", 0, QApplication::UnicodeUTF8));
        label_10->setText(QApplication::translate("PartGui::DlgSettingsObjectColor", "Default vertex color", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        DefaultShapeVertexColor->setToolTip(QApplication::translate("PartGui::DlgSettingsObjectColor", "The default line color for new shapes", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        label_11->setText(QApplication::translate("PartGui::DlgSettingsObjectColor", "Default vertex size", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        DefaultShapeVertexWidth->setToolTip(QApplication::translate("PartGui::DlgSettingsObjectColor", "The default line thickness for new shapes", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        DefaultShapeVertexWidth->setSuffix(QApplication::translate("PartGui::DlgSettingsObjectColor", "px", 0, QApplication::UnicodeUTF8));
        label_8->setText(QApplication::translate("PartGui::DlgSettingsObjectColor", "Bounding box color", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        BoundingBoxColor->setToolTip(QApplication::translate("PartGui::DlgSettingsObjectColor", "The color of bounding boxes in the 3D view", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        groupBox->setTitle(QApplication::translate("PartGui::DlgSettingsObjectColor", "Annotations", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("PartGui::DlgSettingsObjectColor", "Default text color", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace PartGui

namespace PartGui {
namespace Ui {
    class DlgSettingsObjectColor: public Ui_DlgSettingsObjectColor {};
} // namespace Ui
} // namespace PartGui

#endif // UI_DLGSETTINGSOBJECTCOLOR_H
