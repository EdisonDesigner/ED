/********************************************************************************
** Form generated from reading UI file 'DlgSmoothing.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DLGSMOOTHING_H
#define UI_DLGSMOOTHING_H

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
#include <QtGui/QRadioButton>
#include <QtGui/QSpinBox>
#include <QtGui/QWidget>

namespace MeshGui {

class Ui_DlgSmoothing
{
public:
    QGridLayout *gridLayout_3;
    QGroupBox *groupBox_3;
    QGridLayout *gridLayout;
    QRadioButton *radioButtonTaubin;
    QRadioButton *radioButtonLaplace;
    QGroupBox *groupBox_2;
    QGridLayout *gridLayout_2;
    QLabel *label;
    QSpinBox *iterations;
    QLabel *labelLambda;
    QDoubleSpinBox *spinLambda;
    QLabel *labelMu;
    QDoubleSpinBox *spinMicro;
    QCheckBox *checkBoxSelection;

    void setupUi(QWidget *MeshGui__DlgSmoothing)
    {
        if (MeshGui__DlgSmoothing->objectName().isEmpty())
            MeshGui__DlgSmoothing->setObjectName(QString::fromUtf8("MeshGui__DlgSmoothing"));
        MeshGui__DlgSmoothing->resize(210, 227);
        MeshGui__DlgSmoothing->setProperty("sizeGripEnabled", QVariant(true));
        gridLayout_3 = new QGridLayout(MeshGui__DlgSmoothing);
        gridLayout_3->setSpacing(6);
        gridLayout_3->setContentsMargins(11, 11, 11, 11);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        groupBox_3 = new QGroupBox(MeshGui__DlgSmoothing);
        groupBox_3->setObjectName(QString::fromUtf8("groupBox_3"));
        gridLayout = new QGridLayout(groupBox_3);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        radioButtonTaubin = new QRadioButton(groupBox_3);
        radioButtonTaubin->setObjectName(QString::fromUtf8("radioButtonTaubin"));
        radioButtonTaubin->setChecked(true);

        gridLayout->addWidget(radioButtonTaubin, 0, 0, 1, 1);

        radioButtonLaplace = new QRadioButton(groupBox_3);
        radioButtonLaplace->setObjectName(QString::fromUtf8("radioButtonLaplace"));

        gridLayout->addWidget(radioButtonLaplace, 0, 1, 1, 1);


        gridLayout_3->addWidget(groupBox_3, 0, 0, 1, 1);

        groupBox_2 = new QGroupBox(MeshGui__DlgSmoothing);
        groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
        gridLayout_2 = new QGridLayout(groupBox_2);
        gridLayout_2->setSpacing(6);
        gridLayout_2->setContentsMargins(11, 11, 11, 11);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        label = new QLabel(groupBox_2);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout_2->addWidget(label, 0, 0, 1, 1);

        iterations = new QSpinBox(groupBox_2);
        iterations->setObjectName(QString::fromUtf8("iterations"));
        iterations->setMinimum(1);
        iterations->setValue(4);

        gridLayout_2->addWidget(iterations, 0, 1, 1, 1);

        labelLambda = new QLabel(groupBox_2);
        labelLambda->setObjectName(QString::fromUtf8("labelLambda"));

        gridLayout_2->addWidget(labelLambda, 1, 0, 1, 1);

        spinLambda = new QDoubleSpinBox(groupBox_2);
        spinLambda->setObjectName(QString::fromUtf8("spinLambda"));
        spinLambda->setDecimals(4);
        spinLambda->setMaximum(1);
        spinLambda->setSingleStep(0.001);
        spinLambda->setValue(0.6307);

        gridLayout_2->addWidget(spinLambda, 1, 1, 1, 1);

        labelMu = new QLabel(groupBox_2);
        labelMu->setObjectName(QString::fromUtf8("labelMu"));

        gridLayout_2->addWidget(labelMu, 2, 0, 1, 1);

        spinMicro = new QDoubleSpinBox(groupBox_2);
        spinMicro->setObjectName(QString::fromUtf8("spinMicro"));
        spinMicro->setDecimals(4);
        spinMicro->setMaximum(1);
        spinMicro->setSingleStep(0.001);
        spinMicro->setValue(0.0424);

        gridLayout_2->addWidget(spinMicro, 2, 1, 1, 1);

        checkBoxSelection = new QCheckBox(groupBox_2);
        checkBoxSelection->setObjectName(QString::fromUtf8("checkBoxSelection"));

        gridLayout_2->addWidget(checkBoxSelection, 3, 0, 1, 2);


        gridLayout_3->addWidget(groupBox_2, 1, 0, 1, 1);


        retranslateUi(MeshGui__DlgSmoothing);

        QMetaObject::connectSlotsByName(MeshGui__DlgSmoothing);
    } // setupUi

    void retranslateUi(QWidget *MeshGui__DlgSmoothing)
    {
        MeshGui__DlgSmoothing->setWindowTitle(QApplication::translate("MeshGui::DlgSmoothing", "Smoothing", 0, QApplication::UnicodeUTF8));
        groupBox_3->setTitle(QApplication::translate("MeshGui::DlgSmoothing", "Method", 0, QApplication::UnicodeUTF8));
        radioButtonTaubin->setText(QApplication::translate("MeshGui::DlgSmoothing", "Taubin", 0, QApplication::UnicodeUTF8));
        radioButtonLaplace->setText(QApplication::translate("MeshGui::DlgSmoothing", "Laplace", 0, QApplication::UnicodeUTF8));
        groupBox_2->setTitle(QApplication::translate("MeshGui::DlgSmoothing", "Parameter", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("MeshGui::DlgSmoothing", "Iterations:", 0, QApplication::UnicodeUTF8));
        labelLambda->setText(QApplication::translate("MeshGui::DlgSmoothing", "Lambda:", 0, QApplication::UnicodeUTF8));
        labelMu->setText(QApplication::translate("MeshGui::DlgSmoothing", "Mu:", 0, QApplication::UnicodeUTF8));
        checkBoxSelection->setText(QApplication::translate("MeshGui::DlgSmoothing", "Only selection", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace MeshGui

namespace MeshGui {
namespace Ui {
    class DlgSmoothing: public Ui_DlgSmoothing {};
} // namespace Ui
} // namespace MeshGui

#endif // UI_DLGSMOOTHING_H
