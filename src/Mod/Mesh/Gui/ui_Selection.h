/********************************************************************************
** Form generated from reading UI file 'Selection.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SELECTION_H
#define UI_SELECTION_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QCheckBox>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QWidget>

namespace MeshGui {

class Ui_Selection
{
public:
    QGridLayout *gridLayout_2;
    QGroupBox *groupBox;
    QGridLayout *gridLayout;
    QSpacerItem *horizontalSpacer;
    QPushButton *addSelection;
    QPushButton *clearSelection;
    QCheckBox *visibleTriangles;
    QCheckBox *screenTriangles;
    QLabel *label;

    void setupUi(QWidget *MeshGui__Selection)
    {
        if (MeshGui__Selection->objectName().isEmpty())
            MeshGui__Selection->setObjectName(QString::fromUtf8("MeshGui__Selection"));
        MeshGui__Selection->resize(304, 143);
        gridLayout_2 = new QGridLayout(MeshGui__Selection);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        groupBox = new QGroupBox(MeshGui__Selection);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        gridLayout = new QGridLayout(groupBox);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        horizontalSpacer = new QSpacerItem(101, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer, 0, 0, 1, 1);

        addSelection = new QPushButton(groupBox);
        addSelection->setObjectName(QString::fromUtf8("addSelection"));

        gridLayout->addWidget(addSelection, 0, 1, 1, 1);

        clearSelection = new QPushButton(groupBox);
        clearSelection->setObjectName(QString::fromUtf8("clearSelection"));

        gridLayout->addWidget(clearSelection, 0, 2, 1, 1);

        visibleTriangles = new QCheckBox(groupBox);
        visibleTriangles->setObjectName(QString::fromUtf8("visibleTriangles"));
        visibleTriangles->setChecked(false);

        gridLayout->addWidget(visibleTriangles, 1, 0, 1, 2);

        screenTriangles = new QCheckBox(groupBox);
        screenTriangles->setObjectName(QString::fromUtf8("screenTriangles"));
        screenTriangles->setChecked(true);

        gridLayout->addWidget(screenTriangles, 2, 0, 1, 3);

        label = new QLabel(groupBox);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout->addWidget(label, 3, 0, 1, 3);


        gridLayout_2->addWidget(groupBox, 0, 0, 1, 1);


        retranslateUi(MeshGui__Selection);

        QMetaObject::connectSlotsByName(MeshGui__Selection);
    } // setupUi

    void retranslateUi(QWidget *MeshGui__Selection)
    {
        MeshGui__Selection->setWindowTitle(QApplication::translate("MeshGui::Selection", "Selection", 0, QApplication::UnicodeUTF8));
        groupBox->setTitle(QApplication::translate("MeshGui::Selection", "Selection", 0, QApplication::UnicodeUTF8));
        addSelection->setText(QApplication::translate("MeshGui::Selection", "Add", 0, QApplication::UnicodeUTF8));
        clearSelection->setText(QApplication::translate("MeshGui::Selection", "Clear", 0, QApplication::UnicodeUTF8));
        visibleTriangles->setText(QApplication::translate("MeshGui::Selection", "Respect only visible triangles", 0, QApplication::UnicodeUTF8));
        screenTriangles->setText(QApplication::translate("MeshGui::Selection", "Respect only triangles with normals facing screen", 0, QApplication::UnicodeUTF8));
        label->setText(QString());
    } // retranslateUi

};

} // namespace MeshGui

namespace MeshGui {
namespace Ui {
    class Selection: public Ui_Selection {};
} // namespace Ui
} // namespace MeshGui

#endif // UI_SELECTION_H
