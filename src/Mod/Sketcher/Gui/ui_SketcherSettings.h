/********************************************************************************
** Form generated from reading UI file 'SketcherSettings.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SKETCHERSETTINGS_H
#define UI_SKETCHERSETTINGS_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QComboBox>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QSpacerItem>
#include <QtGui/QWidget>
#include "Gui/PrefWidgets.h"
#include "Gui/Widgets.h"

namespace SketcherGui {

class Ui_SketcherSettings
{
public:
    QGridLayout *gridLayout_3;
    QGroupBox *groupBoxSketcherColor;
    QHBoxLayout *horizontalLayout_2;
    QGridLayout *gridLayout_2;
    QLabel *label_17;
    Gui::PrefColorButton *SketchEdgeColor;
    QLabel *label_18;
    Gui::PrefColorButton *SketchVertexColor;
    QLabel *label;
    Gui::PrefColorButton *EditedEdgeColor;
    QLabel *label_2;
    Gui::PrefColorButton *EditedVertexColor;
    QLabel *label_3;
    Gui::PrefColorButton *DatumColor;
    Gui::PrefColorButton *ConstructionColor;
    QLabel *label_20;
    Gui::PrefColorButton *ExternalColor;
    QLabel *label_4;
    QLabel *label_14;
    Gui::PrefColorButton *FullyConstrainedColor;
    QLabel *label_15;
    QLabel *label_16;
    QLabel *label_12;
    Gui::PrefSpinBox *SketcherDatumWidth;
    QLabel *label_13;
    Gui::PrefSpinBox *DefaultSketcherVertexWidth;
    QLabel *label_5;
    Gui::PrefColorButton *CursorTextColor;
    Gui::PrefSpinBox *DefaultSketcherLineWidth;
    QLabel *label_8;
    Gui::PrefColorButton *ConstrainedColor;
    Gui::PrefColorButton *NonDrivingConstraintColor;
    QGroupBox *groupBox;
    QGridLayout *gridLayout;
    QLabel *label_6;
    Gui::PrefSpinBox *EditSketcherFontSize;
    QLabel *label_marker;
    QComboBox *EditSketcherMarkerSize;
    QLabel *label_7;
    QComboBox *comboBox;
    Gui::PrefCheckBox *dialogOnDistanceConstraint;
    Gui::PrefCheckBox *continueMode;
    QGroupBox *groupBox_2;
    QGridLayout *gridLayout_4;
    Gui::PrefCheckBox *checkBoxAdvancedSolverTaskBox;
    QSpacerItem *verticalSpacer;

    void setupUi(QWidget *SketcherGui__SketcherSettings)
    {
        if (SketcherGui__SketcherSettings->objectName().isEmpty())
            SketcherGui__SketcherSettings->setObjectName(QString::fromUtf8("SketcherGui__SketcherSettings"));
        SketcherGui__SketcherSettings->resize(404, 744);
        gridLayout_3 = new QGridLayout(SketcherGui__SketcherSettings);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        groupBoxSketcherColor = new QGroupBox(SketcherGui__SketcherSettings);
        groupBoxSketcherColor->setObjectName(QString::fromUtf8("groupBoxSketcherColor"));
        horizontalLayout_2 = new QHBoxLayout(groupBoxSketcherColor);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        gridLayout_2 = new QGridLayout();
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        label_17 = new QLabel(groupBoxSketcherColor);
        label_17->setObjectName(QString::fromUtf8("label_17"));
        label_17->setMinimumSize(QSize(182, 0));

        gridLayout_2->addWidget(label_17, 0, 0, 1, 1);

        SketchEdgeColor = new Gui::PrefColorButton(groupBoxSketcherColor);
        SketchEdgeColor->setObjectName(QString::fromUtf8("SketchEdgeColor"));
        SketchEdgeColor->setColor(QColor(255, 255, 255));
        SketchEdgeColor->setProperty("prefEntry", QVariant(QByteArray("SketchEdgeColor")));
        SketchEdgeColor->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout_2->addWidget(SketchEdgeColor, 0, 1, 1, 1);

        label_18 = new QLabel(groupBoxSketcherColor);
        label_18->setObjectName(QString::fromUtf8("label_18"));
        label_18->setMinimumSize(QSize(182, 0));

        gridLayout_2->addWidget(label_18, 1, 0, 1, 1);

        SketchVertexColor = new Gui::PrefColorButton(groupBoxSketcherColor);
        SketchVertexColor->setObjectName(QString::fromUtf8("SketchVertexColor"));
        SketchVertexColor->setColor(QColor(255, 255, 255));
        SketchVertexColor->setProperty("prefEntry", QVariant(QByteArray("SketchVertexColor")));
        SketchVertexColor->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout_2->addWidget(SketchVertexColor, 1, 1, 1, 1);

        label = new QLabel(groupBoxSketcherColor);
        label->setObjectName(QString::fromUtf8("label"));
        label->setMinimumSize(QSize(182, 0));

        gridLayout_2->addWidget(label, 2, 0, 1, 1);

        EditedEdgeColor = new Gui::PrefColorButton(groupBoxSketcherColor);
        EditedEdgeColor->setObjectName(QString::fromUtf8("EditedEdgeColor"));
        EditedEdgeColor->setColor(QColor(255, 255, 255));
        EditedEdgeColor->setProperty("prefEntry", QVariant(QByteArray("EditedEdgeColor")));
        EditedEdgeColor->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout_2->addWidget(EditedEdgeColor, 2, 1, 1, 1);

        label_2 = new QLabel(groupBoxSketcherColor);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setMinimumSize(QSize(182, 0));

        gridLayout_2->addWidget(label_2, 3, 0, 1, 1);

        EditedVertexColor = new Gui::PrefColorButton(groupBoxSketcherColor);
        EditedVertexColor->setObjectName(QString::fromUtf8("EditedVertexColor"));
        EditedVertexColor->setColor(QColor(255, 38, 0));
        EditedVertexColor->setProperty("prefEntry", QVariant(QByteArray("EditedVertexColor")));
        EditedVertexColor->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout_2->addWidget(EditedVertexColor, 3, 1, 1, 1);

        label_3 = new QLabel(groupBoxSketcherColor);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setMinimumSize(QSize(182, 0));

        gridLayout_2->addWidget(label_3, 4, 0, 1, 1);

        DatumColor = new Gui::PrefColorButton(groupBoxSketcherColor);
        DatumColor->setObjectName(QString::fromUtf8("DatumColor"));
        DatumColor->setColor(QColor(255, 38, 0));
        DatumColor->setProperty("prefEntry", QVariant(QByteArray("ConstrainedDimColor")));
        DatumColor->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout_2->addWidget(DatumColor, 9, 1, 1, 1);

        ConstructionColor = new Gui::PrefColorButton(groupBoxSketcherColor);
        ConstructionColor->setObjectName(QString::fromUtf8("ConstructionColor"));
        ConstructionColor->setColor(QColor(0, 0, 220));
        ConstructionColor->setProperty("prefEntry", QVariant(QByteArray("ConstructionColor")));
        ConstructionColor->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout_2->addWidget(ConstructionColor, 4, 1, 1, 1);

        label_20 = new QLabel(groupBoxSketcherColor);
        label_20->setObjectName(QString::fromUtf8("label_20"));
        label_20->setMinimumSize(QSize(182, 0));

        gridLayout_2->addWidget(label_20, 5, 0, 1, 1);

        ExternalColor = new Gui::PrefColorButton(groupBoxSketcherColor);
        ExternalColor->setObjectName(QString::fromUtf8("ExternalColor"));
        ExternalColor->setColor(QColor(204, 51, 115));
        ExternalColor->setProperty("prefEntry", QVariant(QByteArray("ExternalColor")));
        ExternalColor->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout_2->addWidget(ExternalColor, 5, 1, 1, 1);

        label_4 = new QLabel(groupBoxSketcherColor);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setMinimumSize(QSize(182, 0));

        gridLayout_2->addWidget(label_4, 6, 0, 1, 1);

        label_14 = new QLabel(groupBoxSketcherColor);
        label_14->setObjectName(QString::fromUtf8("label_14"));
        label_14->setMinimumSize(QSize(182, 0));

        gridLayout_2->addWidget(label_14, 7, 0, 1, 1);

        FullyConstrainedColor = new Gui::PrefColorButton(groupBoxSketcherColor);
        FullyConstrainedColor->setObjectName(QString::fromUtf8("FullyConstrainedColor"));
        FullyConstrainedColor->setColor(QColor(0, 255, 0));
        FullyConstrainedColor->setProperty("prefEntry", QVariant(QByteArray("FullyConstrainedColor")));
        FullyConstrainedColor->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout_2->addWidget(FullyConstrainedColor, 6, 1, 1, 1);

        label_15 = new QLabel(groupBoxSketcherColor);
        label_15->setObjectName(QString::fromUtf8("label_15"));
        label_15->setMinimumSize(QSize(182, 0));

        gridLayout_2->addWidget(label_15, 9, 0, 1, 1);

        label_16 = new QLabel(groupBoxSketcherColor);
        label_16->setObjectName(QString::fromUtf8("label_16"));
        label_16->setMinimumSize(QSize(182, 0));

        gridLayout_2->addWidget(label_16, 10, 0, 1, 1);

        label_12 = new QLabel(groupBoxSketcherColor);
        label_12->setObjectName(QString::fromUtf8("label_12"));
        label_12->setMinimumSize(QSize(182, 0));

        gridLayout_2->addWidget(label_12, 11, 0, 1, 1);

        SketcherDatumWidth = new Gui::PrefSpinBox(groupBoxSketcherColor);
        SketcherDatumWidth->setObjectName(QString::fromUtf8("SketcherDatumWidth"));
        SketcherDatumWidth->setMaximum(9);
        SketcherDatumWidth->setValue(2);
        SketcherDatumWidth->setProperty("prefEntry", QVariant(QByteArray("DefaultSketcherVertexWidth")));
        SketcherDatumWidth->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout_2->addWidget(SketcherDatumWidth, 10, 1, 1, 1);

        label_13 = new QLabel(groupBoxSketcherColor);
        label_13->setObjectName(QString::fromUtf8("label_13"));
        label_13->setMinimumSize(QSize(182, 0));

        gridLayout_2->addWidget(label_13, 12, 0, 1, 1);

        DefaultSketcherVertexWidth = new Gui::PrefSpinBox(groupBoxSketcherColor);
        DefaultSketcherVertexWidth->setObjectName(QString::fromUtf8("DefaultSketcherVertexWidth"));
        DefaultSketcherVertexWidth->setMaximum(9);
        DefaultSketcherVertexWidth->setValue(2);
        DefaultSketcherVertexWidth->setProperty("prefEntry", QVariant(QByteArray("DefaultSketcherVertexWidth")));
        DefaultSketcherVertexWidth->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout_2->addWidget(DefaultSketcherVertexWidth, 11, 1, 1, 1);

        label_5 = new QLabel(groupBoxSketcherColor);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setMinimumSize(QSize(182, 0));

        gridLayout_2->addWidget(label_5, 13, 0, 1, 1);

        CursorTextColor = new Gui::PrefColorButton(groupBoxSketcherColor);
        CursorTextColor->setObjectName(QString::fromUtf8("CursorTextColor"));
        CursorTextColor->setColor(QColor(0, 0, 255));
        CursorTextColor->setProperty("prefEntry", QVariant(QByteArray("CursorTextColor")));
        CursorTextColor->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout_2->addWidget(CursorTextColor, 13, 1, 1, 1);

        DefaultSketcherLineWidth = new Gui::PrefSpinBox(groupBoxSketcherColor);
        DefaultSketcherLineWidth->setObjectName(QString::fromUtf8("DefaultSketcherLineWidth"));
        DefaultSketcherLineWidth->setMaximum(9);
        DefaultSketcherLineWidth->setValue(2);
        DefaultSketcherLineWidth->setProperty("prefEntry", QVariant(QByteArray("DefaultShapeLineWidth")));
        DefaultSketcherLineWidth->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout_2->addWidget(DefaultSketcherLineWidth, 12, 1, 1, 1);

        label_8 = new QLabel(groupBoxSketcherColor);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        gridLayout_2->addWidget(label_8, 8, 0, 1, 1);

        ConstrainedColor = new Gui::PrefColorButton(groupBoxSketcherColor);
        ConstrainedColor->setObjectName(QString::fromUtf8("ConstrainedColor"));
        ConstrainedColor->setColor(QColor(255, 38, 0));
        ConstrainedColor->setProperty("prefEntry", QVariant(QByteArray("ConstrainedIcoColor")));
        ConstrainedColor->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout_2->addWidget(ConstrainedColor, 7, 1, 1, 1);

        NonDrivingConstraintColor = new Gui::PrefColorButton(groupBoxSketcherColor);
        NonDrivingConstraintColor->setObjectName(QString::fromUtf8("NonDrivingConstraintColor"));
        NonDrivingConstraintColor->setColor(QColor(0, 38, 255));
        NonDrivingConstraintColor->setProperty("prefEntry", QVariant(QByteArray("NonDrivingConstrDimColor")));
        NonDrivingConstraintColor->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout_2->addWidget(NonDrivingConstraintColor, 8, 1, 1, 1);


        horizontalLayout_2->addLayout(gridLayout_2);


        gridLayout_3->addWidget(groupBoxSketcherColor, 0, 0, 1, 1);

        groupBox = new QGroupBox(SketcherGui__SketcherSettings);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        gridLayout = new QGridLayout(groupBox);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label_6 = new QLabel(groupBox);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setMinimumSize(QSize(182, 0));

        gridLayout->addWidget(label_6, 0, 0, 1, 1);

        EditSketcherFontSize = new Gui::PrefSpinBox(groupBox);
        EditSketcherFontSize->setObjectName(QString::fromUtf8("EditSketcherFontSize"));
        EditSketcherFontSize->setMinimum(1);
        EditSketcherFontSize->setMaximum(100);
        EditSketcherFontSize->setValue(17);
        EditSketcherFontSize->setProperty("prefEntry", QVariant(QByteArray("EditSketcherFontSize")));
        EditSketcherFontSize->setProperty("prefPath", QVariant(QByteArray("View")));

        gridLayout->addWidget(EditSketcherFontSize, 0, 1, 1, 1);

        label_marker = new QLabel(groupBox);
        label_marker->setObjectName(QString::fromUtf8("label_marker"));
        label_marker->setMinimumSize(QSize(182, 0));

        gridLayout->addWidget(label_marker, 1, 0, 1, 1);

        EditSketcherMarkerSize = new QComboBox(groupBox);
        EditSketcherMarkerSize->setObjectName(QString::fromUtf8("EditSketcherMarkerSize"));

        gridLayout->addWidget(EditSketcherMarkerSize, 1, 1, 1, 1);

        label_7 = new QLabel(groupBox);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        gridLayout->addWidget(label_7, 2, 0, 1, 1);

        comboBox = new QComboBox(groupBox);
        comboBox->setObjectName(QString::fromUtf8("comboBox"));

        gridLayout->addWidget(comboBox, 2, 1, 1, 1);

        dialogOnDistanceConstraint = new Gui::PrefCheckBox(groupBox);
        dialogOnDistanceConstraint->setObjectName(QString::fromUtf8("dialogOnDistanceConstraint"));
        dialogOnDistanceConstraint->setChecked(true);
        dialogOnDistanceConstraint->setProperty("prefEntry", QVariant(QByteArray("ShowDialogOnDistanceConstraint")));
        dialogOnDistanceConstraint->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher")));

        gridLayout->addWidget(dialogOnDistanceConstraint, 3, 0, 1, 2);

        continueMode = new Gui::PrefCheckBox(groupBox);
        continueMode->setObjectName(QString::fromUtf8("continueMode"));
        continueMode->setChecked(true);
        continueMode->setProperty("prefEntry", QVariant(QByteArray("ContinuousCreationMode")));
        continueMode->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher")));

        gridLayout->addWidget(continueMode, 4, 0, 1, 2);


        gridLayout_3->addWidget(groupBox, 1, 0, 1, 1);

        groupBox_2 = new QGroupBox(SketcherGui__SketcherSettings);
        groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
        gridLayout_4 = new QGridLayout(groupBox_2);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        checkBoxAdvancedSolverTaskBox = new Gui::PrefCheckBox(groupBox_2);
        checkBoxAdvancedSolverTaskBox->setObjectName(QString::fromUtf8("checkBoxAdvancedSolverTaskBox"));
        checkBoxAdvancedSolverTaskBox->setProperty("prefEntry", QVariant(QByteArray("ShowSolverAdvancedWidget")));
        checkBoxAdvancedSolverTaskBox->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher")));

        gridLayout_4->addWidget(checkBoxAdvancedSolverTaskBox, 0, 0, 1, 1);


        gridLayout_3->addWidget(groupBox_2, 3, 0, 1, 1);

        verticalSpacer = new QSpacerItem(20, 217, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_3->addItem(verticalSpacer, 4, 0, 1, 1);

        QWidget::setTabOrder(CursorTextColor, EditedEdgeColor);
        QWidget::setTabOrder(EditedEdgeColor, EditedVertexColor);
        QWidget::setTabOrder(EditedVertexColor, ConstructionColor);
        QWidget::setTabOrder(ConstructionColor, FullyConstrainedColor);

        retranslateUi(SketcherGui__SketcherSettings);

        comboBox->setCurrentIndex(-1);


        QMetaObject::connectSlotsByName(SketcherGui__SketcherSettings);
    } // setupUi

    void retranslateUi(QWidget *SketcherGui__SketcherSettings)
    {
        SketcherGui__SketcherSettings->setWindowTitle(QApplication::translate("SketcherGui::SketcherSettings", "Sketcher", 0, QApplication::UnicodeUTF8));
        groupBoxSketcherColor->setTitle(QApplication::translate("SketcherGui::SketcherSettings", "Sketcher colors", 0, QApplication::UnicodeUTF8));
        label_17->setText(QApplication::translate("SketcherGui::SketcherSettings", "Default edge color", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        SketchEdgeColor->setToolTip(QApplication::translate("SketcherGui::SketcherSettings", "The color of edges being edited", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        label_18->setText(QApplication::translate("SketcherGui::SketcherSettings", "Default vertex color", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        SketchVertexColor->setToolTip(QApplication::translate("SketcherGui::SketcherSettings", "The color of vertices being edited", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        label->setText(QApplication::translate("SketcherGui::SketcherSettings", "Edit edge color", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        EditedEdgeColor->setToolTip(QApplication::translate("SketcherGui::SketcherSettings", "The color of edges being edited", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        label_2->setText(QApplication::translate("SketcherGui::SketcherSettings", "Edit vertex color", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        EditedVertexColor->setToolTip(QApplication::translate("SketcherGui::SketcherSettings", "The color of vertices being edited", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        label_3->setText(QApplication::translate("SketcherGui::SketcherSettings", "Construction geometry", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        DatumColor->setToolTip(QApplication::translate("SketcherGui::SketcherSettings", "The color of fully constrained geometry in edit mode", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_TOOLTIP
        ConstructionColor->setToolTip(QApplication::translate("SketcherGui::SketcherSettings", "The color of construction geometry in edit mode", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        label_20->setText(QApplication::translate("SketcherGui::SketcherSettings", "External geometry", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        ExternalColor->setToolTip(QApplication::translate("SketcherGui::SketcherSettings", "The color of external geometry in edit mode", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        label_4->setText(QApplication::translate("SketcherGui::SketcherSettings", "Fully constrained geometry", 0, QApplication::UnicodeUTF8));
        label_14->setText(QApplication::translate("SketcherGui::SketcherSettings", "Constraint color", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        FullyConstrainedColor->setToolTip(QApplication::translate("SketcherGui::SketcherSettings", "The color of fully constrained geometry in edit mode", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        label_15->setText(QApplication::translate("SketcherGui::SketcherSettings", "Datum color", 0, QApplication::UnicodeUTF8));
        label_16->setText(QApplication::translate("SketcherGui::SketcherSettings", "Datum text size", 0, QApplication::UnicodeUTF8));
        label_12->setText(QApplication::translate("SketcherGui::SketcherSettings", "Default vertex size", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        SketcherDatumWidth->setToolTip(QApplication::translate("SketcherGui::SketcherSettings", "The default line thickness for new shapes", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        SketcherDatumWidth->setSuffix(QApplication::translate("SketcherGui::SketcherSettings", "px", 0, QApplication::UnicodeUTF8));
        label_13->setText(QApplication::translate("SketcherGui::SketcherSettings", "Default line width", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        DefaultSketcherVertexWidth->setToolTip(QApplication::translate("SketcherGui::SketcherSettings", "The default line thickness for new shapes", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        DefaultSketcherVertexWidth->setSuffix(QApplication::translate("SketcherGui::SketcherSettings", "px", 0, QApplication::UnicodeUTF8));
        label_5->setText(QApplication::translate("SketcherGui::SketcherSettings", "Cursor text color", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        DefaultSketcherLineWidth->setToolTip(QApplication::translate("SketcherGui::SketcherSettings", "The default line thickness for new shapes", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        DefaultSketcherLineWidth->setSuffix(QApplication::translate("SketcherGui::SketcherSettings", "px", 0, QApplication::UnicodeUTF8));
        label_8->setText(QApplication::translate("SketcherGui::SketcherSettings", "Non-driving Datum color", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        ConstrainedColor->setToolTip(QApplication::translate("SketcherGui::SketcherSettings", "The color of driving constraints in edit mode", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_TOOLTIP
        NonDrivingConstraintColor->setToolTip(QApplication::translate("SketcherGui::SketcherSettings", "The color of non-driving constrains or dimensions in edit mode", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        groupBox->setTitle(QApplication::translate("SketcherGui::SketcherSettings", "Sketch editing", 0, QApplication::UnicodeUTF8));
        label_6->setText(QApplication::translate("SketcherGui::SketcherSettings", "Font size", 0, QApplication::UnicodeUTF8));
        EditSketcherFontSize->setSuffix(QApplication::translate("SketcherGui::SketcherSettings", "px", 0, QApplication::UnicodeUTF8));
        label_marker->setText(QApplication::translate("SketcherGui::SketcherSettings", "Marker size", 0, QApplication::UnicodeUTF8));
        label_7->setText(QApplication::translate("SketcherGui::SketcherSettings", "Grid line pattern", 0, QApplication::UnicodeUTF8));
        dialogOnDistanceConstraint->setText(QApplication::translate("SketcherGui::SketcherSettings", "Ask for value after creating a distance constraint", 0, QApplication::UnicodeUTF8));
        continueMode->setText(QApplication::translate("SketcherGui::SketcherSettings", "Geometry Creation \"Continue Mode\"", 0, QApplication::UnicodeUTF8));
        groupBox_2->setTitle(QApplication::translate("SketcherGui::SketcherSettings", "Sketch Solver", 0, QApplication::UnicodeUTF8));
        checkBoxAdvancedSolverTaskBox->setText(QApplication::translate("SketcherGui::SketcherSettings", "Show Advanced Solver Control in the Task bar", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace SketcherGui

namespace SketcherGui {
namespace Ui {
    class SketcherSettings: public Ui_SketcherSettings {};
} // namespace Ui
} // namespace SketcherGui

#endif // UI_SKETCHERSETTINGS_H
