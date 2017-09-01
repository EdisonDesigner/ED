/********************************************************************************
** Form generated from reading UI file 'TaskSketcherSolverAdvanced.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TASKSKETCHERSOLVERADVANCED_H
#define UI_TASKSKETCHERSOLVERADVANCED_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>
#include "Gui/PrefWidgets.h"

QT_BEGIN_NAMESPACE

class Ui_TaskSketcherSolverAdvanced
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout_4;
    QLabel *labelDefaultSolver;
    Gui::PrefComboBox *comboBoxDefaultSolver;
    QHBoxLayout *horizontalLayout_4_2;
    QLabel *labelDogLegGaussStep;
    Gui::PrefComboBox *comboBoxDogLegGaussStep;
    QHBoxLayout *horizontalLayout_2;
    QLabel *labelMaxIter;
    Gui::PrefSpinBox *spinBoxMaxIter;
    QHBoxLayout *horizontalLayout_3;
    QLabel *labelSketchSizeMultiplier;
    Gui::PrefCheckBox *checkBoxSketchSizeMultiplier;
    QHBoxLayout *horizontalLayout_9;
    QLabel *labelSolverConvergence;
    Gui::PrefLineEdit *lineEditConvergence;
    QHBoxLayout *horizontalLayout_10;
    QLabel *labelSolverParam1;
    Gui::PrefLineEdit *lineEditSolverParam1;
    QHBoxLayout *horizontalLayout_11;
    QLabel *labelSolverParam2;
    Gui::PrefLineEdit *lineEditSolverParam2;
    QHBoxLayout *horizontalLayout_12;
    QLabel *labelSolverParam3;
    Gui::PrefLineEdit *lineEditSolverParam3;
    QHBoxLayout *horizontalLayout;
    QLabel *labelQRAlgorithm;
    Gui::PrefComboBox *comboBoxQRMethod;
    QHBoxLayout *horizontalLayout_18;
    QLabel *labelPivotThreshold;
    Gui::PrefLineEdit *lineEditQRPivotThreshold;
    QHBoxLayout *horizontalLayout_5;
    QLabel *labelRedundantSolver;
    Gui::PrefComboBox *comboBoxRedundantDefaultSolver;
    QHBoxLayout *horizontalLayout_6;
    QLabel *labelRedundantSolverMaxIterations;
    Gui::PrefSpinBox *spinBoxRedundantSolverMaxIterations;
    QHBoxLayout *horizontalLayout_7;
    QLabel *labelRedundantSketchSizeMultiplier;
    Gui::PrefCheckBox *checkBoxRedundantSketchSizeMultiplier;
    QHBoxLayout *horizontalLayout_13;
    QLabel *labelRedundantConvergence;
    Gui::PrefLineEdit *lineEditRedundantConvergence;
    QHBoxLayout *horizontalLayout_14;
    QLabel *labelRedundantSolverParam1;
    Gui::PrefLineEdit *lineEditRedundantSolverParam1;
    QHBoxLayout *horizontalLayout_15;
    QLabel *labelRedundantSolverParam2;
    Gui::PrefLineEdit *lineEditRedundantSolverParam2;
    QHBoxLayout *horizontalLayout_16;
    QLabel *labelRedundantSolverParam3;
    Gui::PrefLineEdit *lineEditRedundantSolverParam3;
    QHBoxLayout *horizontalLayout_8;
    QLabel *labelDebugMode;
    Gui::PrefComboBox *comboBoxDebugMode;
    QHBoxLayout *horizontalLayout_17;
    QPushButton *pushButtonSolve;
    QPushButton *pushButtonDefaults;

    void setupUi(QWidget *TaskSketcherSolverAdvanced)
    {
        if (TaskSketcherSolverAdvanced->objectName().isEmpty())
            TaskSketcherSolverAdvanced->setObjectName(QString::fromUtf8("TaskSketcherSolverAdvanced"));
        TaskSketcherSolverAdvanced->resize(326, 630);
        verticalLayout = new QVBoxLayout(TaskSketcherSolverAdvanced);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        labelDefaultSolver = new QLabel(TaskSketcherSolverAdvanced);
        labelDefaultSolver->setObjectName(QString::fromUtf8("labelDefaultSolver"));

        horizontalLayout_4->addWidget(labelDefaultSolver);

        comboBoxDefaultSolver = new Gui::PrefComboBox(TaskSketcherSolverAdvanced);
        comboBoxDefaultSolver->setObjectName(QString::fromUtf8("comboBoxDefaultSolver"));
        comboBoxDefaultSolver->setProperty("prefEntry", QVariant(QByteArray("DefaultSolver")));
        comboBoxDefaultSolver->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher/SolverAdvanced")));

        horizontalLayout_4->addWidget(comboBoxDefaultSolver);


        verticalLayout->addLayout(horizontalLayout_4);

        horizontalLayout_4_2 = new QHBoxLayout();
        horizontalLayout_4_2->setObjectName(QString::fromUtf8("horizontalLayout_4_2"));
        labelDogLegGaussStep = new QLabel(TaskSketcherSolverAdvanced);
        labelDogLegGaussStep->setObjectName(QString::fromUtf8("labelDogLegGaussStep"));

        horizontalLayout_4_2->addWidget(labelDogLegGaussStep);

        comboBoxDogLegGaussStep = new Gui::PrefComboBox(TaskSketcherSolverAdvanced);
        comboBoxDogLegGaussStep->setObjectName(QString::fromUtf8("comboBoxDogLegGaussStep"));
        comboBoxDogLegGaussStep->setProperty("prefEntry", QVariant(QByteArray("DogLegGaussStep")));
        comboBoxDogLegGaussStep->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher/SolverAdvanced")));

        horizontalLayout_4_2->addWidget(comboBoxDogLegGaussStep);


        verticalLayout->addLayout(horizontalLayout_4_2);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        labelMaxIter = new QLabel(TaskSketcherSolverAdvanced);
        labelMaxIter->setObjectName(QString::fromUtf8("labelMaxIter"));

        horizontalLayout_2->addWidget(labelMaxIter);

        spinBoxMaxIter = new Gui::PrefSpinBox(TaskSketcherSolverAdvanced);
        spinBoxMaxIter->setObjectName(QString::fromUtf8("spinBoxMaxIter"));
        spinBoxMaxIter->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        spinBoxMaxIter->setMaximum(999);
        spinBoxMaxIter->setValue(100);
        spinBoxMaxIter->setProperty("prefEntry", QVariant(QByteArray("MaxIter")));
        spinBoxMaxIter->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher/SolverAdvanced")));

        horizontalLayout_2->addWidget(spinBoxMaxIter);


        verticalLayout->addLayout(horizontalLayout_2);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        labelSketchSizeMultiplier = new QLabel(TaskSketcherSolverAdvanced);
        labelSketchSizeMultiplier->setObjectName(QString::fromUtf8("labelSketchSizeMultiplier"));

        horizontalLayout_3->addWidget(labelSketchSizeMultiplier);

        checkBoxSketchSizeMultiplier = new Gui::PrefCheckBox(TaskSketcherSolverAdvanced);
        checkBoxSketchSizeMultiplier->setObjectName(QString::fromUtf8("checkBoxSketchSizeMultiplier"));
        QSizePolicy sizePolicy(QSizePolicy::Minimum, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(checkBoxSketchSizeMultiplier->sizePolicy().hasHeightForWidth());
        checkBoxSketchSizeMultiplier->setSizePolicy(sizePolicy);
        checkBoxSketchSizeMultiplier->setLayoutDirection(Qt::RightToLeft);
        checkBoxSketchSizeMultiplier->setProperty("prefEntry", QVariant(QByteArray("SketchSizeMultiplier")));
        checkBoxSketchSizeMultiplier->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher/SolverAdvanced")));

        horizontalLayout_3->addWidget(checkBoxSketchSizeMultiplier);


        verticalLayout->addLayout(horizontalLayout_3);

        horizontalLayout_9 = new QHBoxLayout();
        horizontalLayout_9->setObjectName(QString::fromUtf8("horizontalLayout_9"));
        labelSolverConvergence = new QLabel(TaskSketcherSolverAdvanced);
        labelSolverConvergence->setObjectName(QString::fromUtf8("labelSolverConvergence"));

        horizontalLayout_9->addWidget(labelSolverConvergence);

        lineEditConvergence = new Gui::PrefLineEdit(TaskSketcherSolverAdvanced);
        lineEditConvergence->setObjectName(QString::fromUtf8("lineEditConvergence"));
        lineEditConvergence->setLayoutDirection(Qt::LeftToRight);
        lineEditConvergence->setText(QString::fromUtf8("1E-10"));
        lineEditConvergence->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        lineEditConvergence->setProperty("prefEntry", QVariant(QByteArray("Convergence")));
        lineEditConvergence->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher/SolverAdvanced")));

        horizontalLayout_9->addWidget(lineEditConvergence);


        verticalLayout->addLayout(horizontalLayout_9);

        horizontalLayout_10 = new QHBoxLayout();
        horizontalLayout_10->setObjectName(QString::fromUtf8("horizontalLayout_10"));
        labelSolverParam1 = new QLabel(TaskSketcherSolverAdvanced);
        labelSolverParam1->setObjectName(QString::fromUtf8("labelSolverParam1"));

        horizontalLayout_10->addWidget(labelSolverParam1);

        lineEditSolverParam1 = new Gui::PrefLineEdit(TaskSketcherSolverAdvanced);
        lineEditSolverParam1->setObjectName(QString::fromUtf8("lineEditSolverParam1"));
        lineEditSolverParam1->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        lineEditSolverParam1->setProperty("prefEntry", QVariant(QByteArray("param")));
        lineEditSolverParam1->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher/SolverAdvanced")));

        horizontalLayout_10->addWidget(lineEditSolverParam1);


        verticalLayout->addLayout(horizontalLayout_10);

        horizontalLayout_11 = new QHBoxLayout();
        horizontalLayout_11->setObjectName(QString::fromUtf8("horizontalLayout_11"));
        labelSolverParam2 = new QLabel(TaskSketcherSolverAdvanced);
        labelSolverParam2->setObjectName(QString::fromUtf8("labelSolverParam2"));

        horizontalLayout_11->addWidget(labelSolverParam2);

        lineEditSolverParam2 = new Gui::PrefLineEdit(TaskSketcherSolverAdvanced);
        lineEditSolverParam2->setObjectName(QString::fromUtf8("lineEditSolverParam2"));
        lineEditSolverParam2->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        lineEditSolverParam2->setProperty("prefEntry", QVariant(QByteArray("param")));
        lineEditSolverParam2->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher/SolverAdvanced")));

        horizontalLayout_11->addWidget(lineEditSolverParam2);


        verticalLayout->addLayout(horizontalLayout_11);

        horizontalLayout_12 = new QHBoxLayout();
        horizontalLayout_12->setObjectName(QString::fromUtf8("horizontalLayout_12"));
        labelSolverParam3 = new QLabel(TaskSketcherSolverAdvanced);
        labelSolverParam3->setObjectName(QString::fromUtf8("labelSolverParam3"));

        horizontalLayout_12->addWidget(labelSolverParam3);

        lineEditSolverParam3 = new Gui::PrefLineEdit(TaskSketcherSolverAdvanced);
        lineEditSolverParam3->setObjectName(QString::fromUtf8("lineEditSolverParam3"));
        lineEditSolverParam3->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        lineEditSolverParam3->setProperty("prefEntry", QVariant(QByteArray("param")));
        lineEditSolverParam3->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher/SolverAdvanced")));

        horizontalLayout_12->addWidget(lineEditSolverParam3);


        verticalLayout->addLayout(horizontalLayout_12);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        labelQRAlgorithm = new QLabel(TaskSketcherSolverAdvanced);
        labelQRAlgorithm->setObjectName(QString::fromUtf8("labelQRAlgorithm"));

        horizontalLayout->addWidget(labelQRAlgorithm);

        comboBoxQRMethod = new Gui::PrefComboBox(TaskSketcherSolverAdvanced);
        comboBoxQRMethod->setObjectName(QString::fromUtf8("comboBoxQRMethod"));
        comboBoxQRMethod->setProperty("prefEntry", QVariant(QByteArray("QRMethod")));
        comboBoxQRMethod->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher/SolverAdvanced")));

        horizontalLayout->addWidget(comboBoxQRMethod);


        verticalLayout->addLayout(horizontalLayout);

        horizontalLayout_18 = new QHBoxLayout();
        horizontalLayout_18->setObjectName(QString::fromUtf8("horizontalLayout_18"));
        labelPivotThreshold = new QLabel(TaskSketcherSolverAdvanced);
        labelPivotThreshold->setObjectName(QString::fromUtf8("labelPivotThreshold"));

        horizontalLayout_18->addWidget(labelPivotThreshold);

        lineEditQRPivotThreshold = new Gui::PrefLineEdit(TaskSketcherSolverAdvanced);
        lineEditQRPivotThreshold->setObjectName(QString::fromUtf8("lineEditQRPivotThreshold"));
        lineEditQRPivotThreshold->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        lineEditQRPivotThreshold->setProperty("prefEntry", QVariant(QByteArray("QRPivotThreshold")));
        lineEditQRPivotThreshold->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher/SolverAdvanced")));

        horizontalLayout_18->addWidget(lineEditQRPivotThreshold);


        verticalLayout->addLayout(horizontalLayout_18);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        labelRedundantSolver = new QLabel(TaskSketcherSolverAdvanced);
        labelRedundantSolver->setObjectName(QString::fromUtf8("labelRedundantSolver"));

        horizontalLayout_5->addWidget(labelRedundantSolver);

        comboBoxRedundantDefaultSolver = new Gui::PrefComboBox(TaskSketcherSolverAdvanced);
        comboBoxRedundantDefaultSolver->setObjectName(QString::fromUtf8("comboBoxRedundantDefaultSolver"));
        comboBoxRedundantDefaultSolver->setProperty("prefEntry", QVariant(QByteArray("RedundantDefaultSolver")));
        comboBoxRedundantDefaultSolver->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher/SolverAdvanced")));

        horizontalLayout_5->addWidget(comboBoxRedundantDefaultSolver);


        verticalLayout->addLayout(horizontalLayout_5);

        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setObjectName(QString::fromUtf8("horizontalLayout_6"));
        labelRedundantSolverMaxIterations = new QLabel(TaskSketcherSolverAdvanced);
        labelRedundantSolverMaxIterations->setObjectName(QString::fromUtf8("labelRedundantSolverMaxIterations"));

        horizontalLayout_6->addWidget(labelRedundantSolverMaxIterations);

        spinBoxRedundantSolverMaxIterations = new Gui::PrefSpinBox(TaskSketcherSolverAdvanced);
        spinBoxRedundantSolverMaxIterations->setObjectName(QString::fromUtf8("spinBoxRedundantSolverMaxIterations"));
        spinBoxRedundantSolverMaxIterations->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        spinBoxRedundantSolverMaxIterations->setMaximum(999);
        spinBoxRedundantSolverMaxIterations->setValue(100);
        spinBoxRedundantSolverMaxIterations->setProperty("prefEntry", QVariant(QByteArray("RedundantSolverMaxIterations")));
        spinBoxRedundantSolverMaxIterations->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher/SolverAdvanced")));

        horizontalLayout_6->addWidget(spinBoxRedundantSolverMaxIterations);


        verticalLayout->addLayout(horizontalLayout_6);

        horizontalLayout_7 = new QHBoxLayout();
        horizontalLayout_7->setObjectName(QString::fromUtf8("horizontalLayout_7"));
        labelRedundantSketchSizeMultiplier = new QLabel(TaskSketcherSolverAdvanced);
        labelRedundantSketchSizeMultiplier->setObjectName(QString::fromUtf8("labelRedundantSketchSizeMultiplier"));

        horizontalLayout_7->addWidget(labelRedundantSketchSizeMultiplier);

        checkBoxRedundantSketchSizeMultiplier = new Gui::PrefCheckBox(TaskSketcherSolverAdvanced);
        checkBoxRedundantSketchSizeMultiplier->setObjectName(QString::fromUtf8("checkBoxRedundantSketchSizeMultiplier"));
        checkBoxRedundantSketchSizeMultiplier->setLayoutDirection(Qt::RightToLeft);
        checkBoxRedundantSketchSizeMultiplier->setProperty("prefEntry", QVariant(QByteArray("RedundantSketchSizeMultiplier")));
        checkBoxRedundantSketchSizeMultiplier->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher/SolverAdvanced")));

        horizontalLayout_7->addWidget(checkBoxRedundantSketchSizeMultiplier);


        verticalLayout->addLayout(horizontalLayout_7);

        horizontalLayout_13 = new QHBoxLayout();
        horizontalLayout_13->setObjectName(QString::fromUtf8("horizontalLayout_13"));
        labelRedundantConvergence = new QLabel(TaskSketcherSolverAdvanced);
        labelRedundantConvergence->setObjectName(QString::fromUtf8("labelRedundantConvergence"));

        horizontalLayout_13->addWidget(labelRedundantConvergence);

        lineEditRedundantConvergence = new Gui::PrefLineEdit(TaskSketcherSolverAdvanced);
        lineEditRedundantConvergence->setObjectName(QString::fromUtf8("lineEditRedundantConvergence"));
        lineEditRedundantConvergence->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        lineEditRedundantConvergence->setProperty("prefEntry", QVariant(QByteArray("RedundantConvergence")));
        lineEditRedundantConvergence->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher/SolverAdvanced")));

        horizontalLayout_13->addWidget(lineEditRedundantConvergence);


        verticalLayout->addLayout(horizontalLayout_13);

        horizontalLayout_14 = new QHBoxLayout();
        horizontalLayout_14->setObjectName(QString::fromUtf8("horizontalLayout_14"));
        labelRedundantSolverParam1 = new QLabel(TaskSketcherSolverAdvanced);
        labelRedundantSolverParam1->setObjectName(QString::fromUtf8("labelRedundantSolverParam1"));

        horizontalLayout_14->addWidget(labelRedundantSolverParam1);

        lineEditRedundantSolverParam1 = new Gui::PrefLineEdit(TaskSketcherSolverAdvanced);
        lineEditRedundantSolverParam1->setObjectName(QString::fromUtf8("lineEditRedundantSolverParam1"));
        lineEditRedundantSolverParam1->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        lineEditRedundantSolverParam1->setProperty("prefEntry", QVariant(QByteArray("param")));
        lineEditRedundantSolverParam1->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher/SolverAdvanced")));

        horizontalLayout_14->addWidget(lineEditRedundantSolverParam1);


        verticalLayout->addLayout(horizontalLayout_14);

        horizontalLayout_15 = new QHBoxLayout();
        horizontalLayout_15->setObjectName(QString::fromUtf8("horizontalLayout_15"));
        labelRedundantSolverParam2 = new QLabel(TaskSketcherSolverAdvanced);
        labelRedundantSolverParam2->setObjectName(QString::fromUtf8("labelRedundantSolverParam2"));

        horizontalLayout_15->addWidget(labelRedundantSolverParam2);

        lineEditRedundantSolverParam2 = new Gui::PrefLineEdit(TaskSketcherSolverAdvanced);
        lineEditRedundantSolverParam2->setObjectName(QString::fromUtf8("lineEditRedundantSolverParam2"));
        lineEditRedundantSolverParam2->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        lineEditRedundantSolverParam2->setProperty("prefEntry", QVariant(QByteArray("param")));
        lineEditRedundantSolverParam2->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher/SolverAdvanced")));

        horizontalLayout_15->addWidget(lineEditRedundantSolverParam2);


        verticalLayout->addLayout(horizontalLayout_15);

        horizontalLayout_16 = new QHBoxLayout();
        horizontalLayout_16->setObjectName(QString::fromUtf8("horizontalLayout_16"));
        labelRedundantSolverParam3 = new QLabel(TaskSketcherSolverAdvanced);
        labelRedundantSolverParam3->setObjectName(QString::fromUtf8("labelRedundantSolverParam3"));

        horizontalLayout_16->addWidget(labelRedundantSolverParam3);

        lineEditRedundantSolverParam3 = new Gui::PrefLineEdit(TaskSketcherSolverAdvanced);
        lineEditRedundantSolverParam3->setObjectName(QString::fromUtf8("lineEditRedundantSolverParam3"));
        lineEditRedundantSolverParam3->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        lineEditRedundantSolverParam3->setProperty("prefEntry", QVariant(QByteArray("param")));
        lineEditRedundantSolverParam3->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher/SolverAdvanced")));

        horizontalLayout_16->addWidget(lineEditRedundantSolverParam3);


        verticalLayout->addLayout(horizontalLayout_16);

        horizontalLayout_8 = new QHBoxLayout();
        horizontalLayout_8->setObjectName(QString::fromUtf8("horizontalLayout_8"));
        labelDebugMode = new QLabel(TaskSketcherSolverAdvanced);
        labelDebugMode->setObjectName(QString::fromUtf8("labelDebugMode"));

        horizontalLayout_8->addWidget(labelDebugMode);

        comboBoxDebugMode = new Gui::PrefComboBox(TaskSketcherSolverAdvanced);
        comboBoxDebugMode->setObjectName(QString::fromUtf8("comboBoxDebugMode"));
        comboBoxDebugMode->setProperty("prefEntry", QVariant(QByteArray("DebugMode")));
        comboBoxDebugMode->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher/SolverAdvanced")));

        horizontalLayout_8->addWidget(comboBoxDebugMode);


        verticalLayout->addLayout(horizontalLayout_8);

        horizontalLayout_17 = new QHBoxLayout();
        horizontalLayout_17->setObjectName(QString::fromUtf8("horizontalLayout_17"));
        pushButtonSolve = new QPushButton(TaskSketcherSolverAdvanced);
        pushButtonSolve->setObjectName(QString::fromUtf8("pushButtonSolve"));

        horizontalLayout_17->addWidget(pushButtonSolve);

        pushButtonDefaults = new QPushButton(TaskSketcherSolverAdvanced);
        pushButtonDefaults->setObjectName(QString::fromUtf8("pushButtonDefaults"));

        horizontalLayout_17->addWidget(pushButtonDefaults);


        verticalLayout->addLayout(horizontalLayout_17);


        retranslateUi(TaskSketcherSolverAdvanced);

        comboBoxDefaultSolver->setCurrentIndex(2);
        comboBoxDogLegGaussStep->setCurrentIndex(0);
        comboBoxQRMethod->setCurrentIndex(1);
        comboBoxRedundantDefaultSolver->setCurrentIndex(2);
        comboBoxDebugMode->setCurrentIndex(1);


        QMetaObject::connectSlotsByName(TaskSketcherSolverAdvanced);
    } // setupUi

    void retranslateUi(QWidget *TaskSketcherSolverAdvanced)
    {
        TaskSketcherSolverAdvanced->setWindowTitle(QApplication::translate("TaskSketcherSolverAdvanced", "Form", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        labelDefaultSolver->setToolTip(QApplication::translate("TaskSketcherSolverAdvanced", "Default algorithm used for Sketch solving", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        labelDefaultSolver->setText(QApplication::translate("TaskSketcherSolverAdvanced", "Default Solver:", 0, QApplication::UnicodeUTF8));
        comboBoxDefaultSolver->clear();
        comboBoxDefaultSolver->insertItems(0, QStringList()
         << QApplication::translate("TaskSketcherSolverAdvanced", "BFGS", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("TaskSketcherSolverAdvanced", "LevenbergMarquardt", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("TaskSketcherSolverAdvanced", "DogLeg", 0, QApplication::UnicodeUTF8)
        );
#ifndef QT_NO_TOOLTIP
        labelDogLegGaussStep->setToolTip(QApplication::translate("TaskSketcherSolverAdvanced", "Type of function to apply in DogLeg for the Gauss step", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        labelDogLegGaussStep->setText(QApplication::translate("TaskSketcherSolverAdvanced", "DogLeg Gauss step:", 0, QApplication::UnicodeUTF8));
        comboBoxDogLegGaussStep->clear();
        comboBoxDogLegGaussStep->insertItems(0, QStringList()
         << QApplication::translate("TaskSketcherSolverAdvanced", "FullPivLU", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("TaskSketcherSolverAdvanced", "LeastNorm-FullPivLU", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("TaskSketcherSolverAdvanced", "LeastNorm-LDLT", 0, QApplication::UnicodeUTF8)
        );
#ifndef QT_NO_TOOLTIP
        labelMaxIter->setToolTip(QApplication::translate("TaskSketcherSolverAdvanced", "Maximum number of iterations of the default algorithm", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        labelMaxIter->setText(QApplication::translate("TaskSketcherSolverAdvanced", "Maximum Iterations:", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        labelSketchSizeMultiplier->setToolTip(QApplication::translate("TaskSketcherSolverAdvanced", "If selected, the Maximum iterations value is multiplied by the sketch size", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        labelSketchSizeMultiplier->setText(QApplication::translate("TaskSketcherSolverAdvanced", "Sketch size multiplier:", 0, QApplication::UnicodeUTF8));
        checkBoxSketchSizeMultiplier->setText(QString());
#ifndef QT_NO_TOOLTIP
        labelSolverConvergence->setToolTip(QApplication::translate("TaskSketcherSolverAdvanced", "Error threshold under which convergence is reached", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        labelSolverConvergence->setText(QApplication::translate("TaskSketcherSolverAdvanced", "Convergence:", 0, QApplication::UnicodeUTF8));
        labelSolverParam1->setText(QApplication::translate("TaskSketcherSolverAdvanced", "Param1", 0, QApplication::UnicodeUTF8));
        labelSolverParam2->setText(QApplication::translate("TaskSketcherSolverAdvanced", "Param2", 0, QApplication::UnicodeUTF8));
        labelSolverParam3->setText(QApplication::translate("TaskSketcherSolverAdvanced", "Param3", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        labelQRAlgorithm->setToolTip(QApplication::translate("TaskSketcherSolverAdvanced", "Algorithm used for the rank revealing QR decomposition", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        labelQRAlgorithm->setText(QApplication::translate("TaskSketcherSolverAdvanced", "QR Algorithm:", 0, QApplication::UnicodeUTF8));
        comboBoxQRMethod->clear();
        comboBoxQRMethod->insertItems(0, QStringList()
         << QApplication::translate("TaskSketcherSolverAdvanced", "Eigen Dense QR", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("TaskSketcherSolverAdvanced", "Eigen Sparse QR", 0, QApplication::UnicodeUTF8)
        );
        labelPivotThreshold->setText(QApplication::translate("TaskSketcherSolverAdvanced", "Pivot threshold", 0, QApplication::UnicodeUTF8));
        lineEditQRPivotThreshold->setText(QApplication::translate("TaskSketcherSolverAdvanced", "1E-13", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        labelRedundantSolver->setToolTip(QApplication::translate("TaskSketcherSolverAdvanced", "Solving algorithm used for determination of Redundant constraints", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        labelRedundantSolver->setText(QApplication::translate("TaskSketcherSolverAdvanced", "Redundant Solver:", 0, QApplication::UnicodeUTF8));
        comboBoxRedundantDefaultSolver->clear();
        comboBoxRedundantDefaultSolver->insertItems(0, QStringList()
         << QApplication::translate("TaskSketcherSolverAdvanced", "BFGS", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("TaskSketcherSolverAdvanced", "LevenbergMarquardt", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("TaskSketcherSolverAdvanced", "DogLeg", 0, QApplication::UnicodeUTF8)
        );
#ifndef QT_NO_TOOLTIP
        labelRedundantSolverMaxIterations->setToolTip(QApplication::translate("TaskSketcherSolverAdvanced", "Maximum number of iterations of the solver used for determination of Redundant constraints", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        labelRedundantSolverMaxIterations->setText(QApplication::translate("TaskSketcherSolverAdvanced", "Red. Max Iterations:", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        spinBoxRedundantSolverMaxIterations->setToolTip(QString());
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_TOOLTIP
        labelRedundantSketchSizeMultiplier->setToolTip(QApplication::translate("TaskSketcherSolverAdvanced", "If selected, the Maximum iterations value for the redundant algorithm is multiplied by the sketch size", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        labelRedundantSketchSizeMultiplier->setText(QApplication::translate("TaskSketcherSolverAdvanced", "Red. Sketch size multiplier:", 0, QApplication::UnicodeUTF8));
        checkBoxRedundantSketchSizeMultiplier->setText(QString());
#ifndef QT_NO_TOOLTIP
        labelRedundantConvergence->setToolTip(QApplication::translate("TaskSketcherSolverAdvanced", "Error threshold under which convergence is reached for the solving of redundant constraints", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        labelRedundantConvergence->setText(QApplication::translate("TaskSketcherSolverAdvanced", "Red. Convergence", 0, QApplication::UnicodeUTF8));
        lineEditRedundantConvergence->setText(QApplication::translate("TaskSketcherSolverAdvanced", "1E-10", 0, QApplication::UnicodeUTF8));
        labelRedundantSolverParam1->setText(QApplication::translate("TaskSketcherSolverAdvanced", "Red. Param1", 0, QApplication::UnicodeUTF8));
        labelRedundantSolverParam2->setText(QApplication::translate("TaskSketcherSolverAdvanced", "Red. Param2", 0, QApplication::UnicodeUTF8));
        labelRedundantSolverParam3->setText(QApplication::translate("TaskSketcherSolverAdvanced", "Red. Param3", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        labelDebugMode->setToolTip(QApplication::translate("TaskSketcherSolverAdvanced", "Degree of verbosity of the debug output to the console", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        labelDebugMode->setText(QApplication::translate("TaskSketcherSolverAdvanced", "Console  Debug mode:", 0, QApplication::UnicodeUTF8));
        comboBoxDebugMode->clear();
        comboBoxDebugMode->insertItems(0, QStringList()
         << QApplication::translate("TaskSketcherSolverAdvanced", "None", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("TaskSketcherSolverAdvanced", "Minimum", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("TaskSketcherSolverAdvanced", "Iteration Level", 0, QApplication::UnicodeUTF8)
        );
        pushButtonSolve->setText(QApplication::translate("TaskSketcherSolverAdvanced", "Solve", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        pushButtonDefaults->setToolTip(QApplication::translate("TaskSketcherSolverAdvanced", "Resets all solver values to their default values", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        pushButtonDefaults->setText(QApplication::translate("TaskSketcherSolverAdvanced", "Restore Defaults", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class TaskSketcherSolverAdvanced: public Ui_TaskSketcherSolverAdvanced {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_TASKSKETCHERSOLVERADVANCED_H
