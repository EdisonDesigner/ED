/********************************************************************************
** Form generated from reading UI file 'TaskPocketParameters.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TASKPOCKETPARAMETERS_H
#define UI_TASKPOCKETPARAMETERS_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QCheckBox>
#include <QtGui/QComboBox>
#include <QtGui/QFrame>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QPushButton>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>
#include "Gui/QuantitySpinBox.h"

namespace PartDesignGui {

class Ui_TaskPocketParameters
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QLabel *textLabel1;
    QComboBox *changeMode;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label;
    Gui::QuantitySpinBox *pocketLength;
    QCheckBox *checkBoxMidplane;
    QCheckBox *checkBoxReversed;
    QHBoxLayout *horizontalLayout_3;
    QPushButton *buttonFace;
    QLineEdit *lineFaceName;
    QFrame *line;
    QCheckBox *checkBoxUpdateView;

    void setupUi(QWidget *PartDesignGui__TaskPocketParameters)
    {
        if (PartDesignGui__TaskPocketParameters->objectName().isEmpty())
            PartDesignGui__TaskPocketParameters->setObjectName(QString::fromUtf8("PartDesignGui__TaskPocketParameters"));
        PartDesignGui__TaskPocketParameters->resize(241, 192);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(PartDesignGui__TaskPocketParameters->sizePolicy().hasHeightForWidth());
        PartDesignGui__TaskPocketParameters->setSizePolicy(sizePolicy);
        PartDesignGui__TaskPocketParameters->setMinimumSize(QSize(233, 134));
        verticalLayout = new QVBoxLayout(PartDesignGui__TaskPocketParameters);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        textLabel1 = new QLabel(PartDesignGui__TaskPocketParameters);
        textLabel1->setObjectName(QString::fromUtf8("textLabel1"));

        horizontalLayout->addWidget(textLabel1);

        changeMode = new QComboBox(PartDesignGui__TaskPocketParameters);
        changeMode->setObjectName(QString::fromUtf8("changeMode"));

        horizontalLayout->addWidget(changeMode);


        verticalLayout->addLayout(horizontalLayout);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label = new QLabel(PartDesignGui__TaskPocketParameters);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout_2->addWidget(label);

        pocketLength = new Gui::QuantitySpinBox(PartDesignGui__TaskPocketParameters);
        pocketLength->setObjectName(QString::fromUtf8("pocketLength"));
        pocketLength->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        pocketLength->setMinimum(0);

        horizontalLayout_2->addWidget(pocketLength);


        verticalLayout->addLayout(horizontalLayout_2);

        checkBoxMidplane = new QCheckBox(PartDesignGui__TaskPocketParameters);
        checkBoxMidplane->setObjectName(QString::fromUtf8("checkBoxMidplane"));
        checkBoxMidplane->setEnabled(true);

        verticalLayout->addWidget(checkBoxMidplane);

        checkBoxReversed = new QCheckBox(PartDesignGui__TaskPocketParameters);
        checkBoxReversed->setObjectName(QString::fromUtf8("checkBoxReversed"));
        checkBoxReversed->setEnabled(true);

        verticalLayout->addWidget(checkBoxReversed);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        buttonFace = new QPushButton(PartDesignGui__TaskPocketParameters);
        buttonFace->setObjectName(QString::fromUtf8("buttonFace"));

        horizontalLayout_3->addWidget(buttonFace);

        lineFaceName = new QLineEdit(PartDesignGui__TaskPocketParameters);
        lineFaceName->setObjectName(QString::fromUtf8("lineFaceName"));

        horizontalLayout_3->addWidget(lineFaceName);


        verticalLayout->addLayout(horizontalLayout_3);

        line = new QFrame(PartDesignGui__TaskPocketParameters);
        line->setObjectName(QString::fromUtf8("line"));
        line->setFrameShape(QFrame::HLine);
        line->setFrameShadow(QFrame::Sunken);

        verticalLayout->addWidget(line);

        checkBoxUpdateView = new QCheckBox(PartDesignGui__TaskPocketParameters);
        checkBoxUpdateView->setObjectName(QString::fromUtf8("checkBoxUpdateView"));
        checkBoxUpdateView->setChecked(true);

        verticalLayout->addWidget(checkBoxUpdateView);


        retranslateUi(PartDesignGui__TaskPocketParameters);

        QMetaObject::connectSlotsByName(PartDesignGui__TaskPocketParameters);
    } // setupUi

    void retranslateUi(QWidget *PartDesignGui__TaskPocketParameters)
    {
        PartDesignGui__TaskPocketParameters->setWindowTitle(QApplication::translate("PartDesignGui::TaskPocketParameters", "Form", 0, QApplication::UnicodeUTF8));
        textLabel1->setText(QApplication::translate("PartDesignGui::TaskPocketParameters", "Type", 0, QApplication::UnicodeUTF8));
        changeMode->clear();
        changeMode->insertItems(0, QStringList()
         << QApplication::translate("PartDesignGui::TaskPocketParameters", "Dimension", 0, QApplication::UnicodeUTF8)
        );
        label->setText(QApplication::translate("PartDesignGui::TaskPocketParameters", "Length", 0, QApplication::UnicodeUTF8));
        checkBoxMidplane->setText(QApplication::translate("PartDesignGui::TaskPocketParameters", "Symmetric to plane", 0, QApplication::UnicodeUTF8));
        checkBoxReversed->setText(QApplication::translate("PartDesignGui::TaskPocketParameters", "Reversed", 0, QApplication::UnicodeUTF8));
        buttonFace->setText(QApplication::translate("PartDesignGui::TaskPocketParameters", "Face", 0, QApplication::UnicodeUTF8));
        checkBoxUpdateView->setText(QApplication::translate("PartDesignGui::TaskPocketParameters", "Update view", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace PartDesignGui

namespace PartDesignGui {
namespace Ui {
    class TaskPocketParameters: public Ui_TaskPocketParameters {};
} // namespace Ui
} // namespace PartDesignGui

#endif // UI_TASKPOCKETPARAMETERS_H
