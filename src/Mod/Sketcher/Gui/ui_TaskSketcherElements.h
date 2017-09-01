/********************************************************************************
** Form generated from reading UI file 'TaskSketcherElements.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TASKSKETCHERELEMENTS_H
#define UI_TASKSKETCHERELEMENTS_H

#include <QListWidget>
#include <QtCore/QLocale>
#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QCheckBox>
#include <QtGui/QComboBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>

namespace SketcherGui {

class Ui_TaskSketcherElements
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QComboBox *comboBoxElementFilter;
    ElementView *listWidgetElements;
    QCheckBox *namingBox;
    QCheckBox *autoSwitchBox;
    QLabel *Explanation;

    void setupUi(QWidget *SketcherGui__TaskSketcherElements)
    {
        if (SketcherGui__TaskSketcherElements->objectName().isEmpty())
            SketcherGui__TaskSketcherElements->setObjectName(QString::fromUtf8("SketcherGui__TaskSketcherElements"));
        SketcherGui__TaskSketcherElements->resize(214, 401);
        verticalLayout = new QVBoxLayout(SketcherGui__TaskSketcherElements);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label = new QLabel(SketcherGui__TaskSketcherElements);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout->addWidget(label);

        comboBoxElementFilter = new QComboBox(SketcherGui__TaskSketcherElements);
        comboBoxElementFilter->setObjectName(QString::fromUtf8("comboBoxElementFilter"));
        comboBoxElementFilter->setEnabled(false);
        comboBoxElementFilter->setLocale(QLocale(QLocale::English, QLocale::UnitedStates));
        comboBoxElementFilter->setEditable(false);

        horizontalLayout->addWidget(comboBoxElementFilter);


        verticalLayout->addLayout(horizontalLayout);

        listWidgetElements = new ElementView(SketcherGui__TaskSketcherElements);
        listWidgetElements->setObjectName(QString::fromUtf8("listWidgetElements"));
        listWidgetElements->setModelColumn(0);

        verticalLayout->addWidget(listWidgetElements);

        namingBox = new QCheckBox(SketcherGui__TaskSketcherElements);
        namingBox->setObjectName(QString::fromUtf8("namingBox"));
        namingBox->setChecked(false);

        verticalLayout->addWidget(namingBox);

        autoSwitchBox = new QCheckBox(SketcherGui__TaskSketcherElements);
        autoSwitchBox->setObjectName(QString::fromUtf8("autoSwitchBox"));
        autoSwitchBox->setChecked(false);

        verticalLayout->addWidget(autoSwitchBox);

        Explanation = new QLabel(SketcherGui__TaskSketcherElements);
        Explanation->setObjectName(QString::fromUtf8("Explanation"));

        verticalLayout->addWidget(Explanation);


        retranslateUi(SketcherGui__TaskSketcherElements);

        comboBoxElementFilter->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(SketcherGui__TaskSketcherElements);
    } // setupUi

    void retranslateUi(QWidget *SketcherGui__TaskSketcherElements)
    {
        SketcherGui__TaskSketcherElements->setWindowTitle(QApplication::translate("SketcherGui::TaskSketcherElements", "Form", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("SketcherGui::TaskSketcherElements", "Type:", 0, QApplication::UnicodeUTF8));
        comboBoxElementFilter->clear();
        comboBoxElementFilter->insertItems(0, QStringList()
         << QApplication::translate("SketcherGui::TaskSketcherElements", "Edge", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("SketcherGui::TaskSketcherElements", "Starting Point", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("SketcherGui::TaskSketcherElements", "End Point", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("SketcherGui::TaskSketcherElements", "Center Point", 0, QApplication::UnicodeUTF8)
        );
        namingBox->setText(QApplication::translate("SketcherGui::TaskSketcherElements", "Extended Naming", 0, QApplication::UnicodeUTF8));
        autoSwitchBox->setText(QApplication::translate("SketcherGui::TaskSketcherElements", "Auto-switch to Edge", 0, QApplication::UnicodeUTF8));
        Explanation->setText(QApplication::translate("SketcherGui::TaskSketcherElements", "<html><head/><body><p>&quot;Ctrl&quot;: multiple selection</p><p>&quot;Z&quot;: switch to next valid type</p></body></html>", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace SketcherGui

namespace SketcherGui {
namespace Ui {
    class TaskSketcherElements: public Ui_TaskSketcherElements {};
} // namespace Ui
} // namespace SketcherGui

#endif // UI_TASKSKETCHERELEMENTS_H
