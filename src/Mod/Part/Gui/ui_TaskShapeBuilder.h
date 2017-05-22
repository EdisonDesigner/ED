/********************************************************************************
** Form generated from reading UI file 'TaskShapeBuilder.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TASKSHAPEBUILDER_H
#define UI_TASKSHAPEBUILDER_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QCheckBox>
#include <QtGui/QFrame>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>
#include <QtGui/QRadioButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QWidget>

namespace PartGui {

class Ui_TaskShapeBuilder
{
public:
    QGridLayout *gridLayout_2;
    QGroupBox *groupBox;
    QGridLayout *gridLayout;
    QRadioButton *radioButtonEdgeFromVertex;
    QRadioButton *radioButtonFaceFromVertex;
    QRadioButton *radioButtonFaceFromEdge;
    QRadioButton *radioButtonShellFromFace;
    QRadioButton *radioButtonSolidFromShell;
    QFrame *line;
    QCheckBox *checkPlanar;
    QCheckBox *checkRefine;
    QCheckBox *checkFaces;
    QHBoxLayout *horizontalLayout;
    QSpacerItem *horizontalSpacer_2;
    QPushButton *createButton;
    QSpacerItem *verticalSpacer;
    QLabel *label;

    void setupUi(QWidget *PartGui__TaskShapeBuilder)
    {
        if (PartGui__TaskShapeBuilder->objectName().isEmpty())
            PartGui__TaskShapeBuilder->setObjectName(QString::fromUtf8("PartGui__TaskShapeBuilder"));
        PartGui__TaskShapeBuilder->resize(200, 336);
        gridLayout_2 = new QGridLayout(PartGui__TaskShapeBuilder);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        groupBox = new QGroupBox(PartGui__TaskShapeBuilder);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        gridLayout = new QGridLayout(groupBox);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        radioButtonEdgeFromVertex = new QRadioButton(groupBox);
        radioButtonEdgeFromVertex->setObjectName(QString::fromUtf8("radioButtonEdgeFromVertex"));

        gridLayout->addWidget(radioButtonEdgeFromVertex, 0, 0, 1, 1);

        radioButtonFaceFromVertex = new QRadioButton(groupBox);
        radioButtonFaceFromVertex->setObjectName(QString::fromUtf8("radioButtonFaceFromVertex"));

        gridLayout->addWidget(radioButtonFaceFromVertex, 1, 0, 1, 1);

        radioButtonFaceFromEdge = new QRadioButton(groupBox);
        radioButtonFaceFromEdge->setObjectName(QString::fromUtf8("radioButtonFaceFromEdge"));

        gridLayout->addWidget(radioButtonFaceFromEdge, 2, 0, 1, 1);

        radioButtonShellFromFace = new QRadioButton(groupBox);
        radioButtonShellFromFace->setObjectName(QString::fromUtf8("radioButtonShellFromFace"));

        gridLayout->addWidget(radioButtonShellFromFace, 3, 0, 1, 1);

        radioButtonSolidFromShell = new QRadioButton(groupBox);
        radioButtonSolidFromShell->setObjectName(QString::fromUtf8("radioButtonSolidFromShell"));

        gridLayout->addWidget(radioButtonSolidFromShell, 4, 0, 1, 1);

        line = new QFrame(groupBox);
        line->setObjectName(QString::fromUtf8("line"));
        line->setFrameShape(QFrame::HLine);
        line->setFrameShadow(QFrame::Sunken);

        gridLayout->addWidget(line, 5, 0, 1, 1);

        checkPlanar = new QCheckBox(groupBox);
        checkPlanar->setObjectName(QString::fromUtf8("checkPlanar"));

        gridLayout->addWidget(checkPlanar, 6, 0, 1, 1);

        checkRefine = new QCheckBox(groupBox);
        checkRefine->setObjectName(QString::fromUtf8("checkRefine"));
        checkRefine->setChecked(true);

        gridLayout->addWidget(checkRefine, 7, 0, 1, 1);

        checkFaces = new QCheckBox(groupBox);
        checkFaces->setObjectName(QString::fromUtf8("checkFaces"));

        gridLayout->addWidget(checkFaces, 8, 0, 1, 1);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_2);

        createButton = new QPushButton(groupBox);
        createButton->setObjectName(QString::fromUtf8("createButton"));

        horizontalLayout->addWidget(createButton);


        gridLayout->addLayout(horizontalLayout, 9, 0, 1, 1);


        gridLayout_2->addWidget(groupBox, 0, 0, 1, 2);

        verticalSpacer = new QSpacerItem(20, 127, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_2->addItem(verticalSpacer, 1, 1, 1, 1);

        label = new QLabel(PartGui__TaskShapeBuilder);
        label->setObjectName(QString::fromUtf8("label"));
        label->setText(QString::fromUtf8("TextLabel"));

        gridLayout_2->addWidget(label, 2, 0, 1, 1);

        QWidget::setTabOrder(radioButtonEdgeFromVertex, radioButtonFaceFromVertex);
        QWidget::setTabOrder(radioButtonFaceFromVertex, radioButtonFaceFromEdge);
        QWidget::setTabOrder(radioButtonFaceFromEdge, radioButtonShellFromFace);
        QWidget::setTabOrder(radioButtonShellFromFace, radioButtonSolidFromShell);
        QWidget::setTabOrder(radioButtonSolidFromShell, checkPlanar);
        QWidget::setTabOrder(checkPlanar, checkRefine);
        QWidget::setTabOrder(checkRefine, checkFaces);
        QWidget::setTabOrder(checkFaces, createButton);

        retranslateUi(PartGui__TaskShapeBuilder);

        QMetaObject::connectSlotsByName(PartGui__TaskShapeBuilder);
    } // setupUi

    void retranslateUi(QWidget *PartGui__TaskShapeBuilder)
    {
        PartGui__TaskShapeBuilder->setWindowTitle(QApplication::translate("PartGui::TaskShapeBuilder", "Create shape", 0, QApplication::UnicodeUTF8));
        groupBox->setTitle(QApplication::translate("PartGui::TaskShapeBuilder", "Create shape", 0, QApplication::UnicodeUTF8));
        radioButtonEdgeFromVertex->setText(QApplication::translate("PartGui::TaskShapeBuilder", "Edge from vertices", 0, QApplication::UnicodeUTF8));
        radioButtonFaceFromVertex->setText(QApplication::translate("PartGui::TaskShapeBuilder", "Face from vertices", 0, QApplication::UnicodeUTF8));
        radioButtonFaceFromEdge->setText(QApplication::translate("PartGui::TaskShapeBuilder", "Face from edges", 0, QApplication::UnicodeUTF8));
        radioButtonShellFromFace->setText(QApplication::translate("PartGui::TaskShapeBuilder", "Shell from faces", 0, QApplication::UnicodeUTF8));
        radioButtonSolidFromShell->setText(QApplication::translate("PartGui::TaskShapeBuilder", "Solid from shell", 0, QApplication::UnicodeUTF8));
        checkPlanar->setText(QApplication::translate("PartGui::TaskShapeBuilder", "Planar", 0, QApplication::UnicodeUTF8));
        checkRefine->setText(QApplication::translate("PartGui::TaskShapeBuilder", "Refine shape", 0, QApplication::UnicodeUTF8));
        checkFaces->setText(QApplication::translate("PartGui::TaskShapeBuilder", "All faces", 0, QApplication::UnicodeUTF8));
        createButton->setText(QApplication::translate("PartGui::TaskShapeBuilder", "Create", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace PartGui

namespace PartGui {
namespace Ui {
    class TaskShapeBuilder: public Ui_TaskShapeBuilder {};
} // namespace Ui
} // namespace PartGui

#endif // UI_TASKSHAPEBUILDER_H
