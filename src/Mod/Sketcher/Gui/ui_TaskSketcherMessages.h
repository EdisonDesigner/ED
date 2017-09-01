/********************************************************************************
** Form generated from reading UI file 'TaskSketcherMessages.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TASKSKETCHERMESSAGES_H
#define UI_TASKSKETCHERMESSAGES_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>
#include "Gui/PrefWidgets.h"

QT_BEGIN_NAMESPACE

class Ui_TaskSketcherMessages
{
public:
    QVBoxLayout *verticalLayout;
    QLabel *labelConstrainStatus;
    QLabel *labelSolverStatus;
    QSpacerItem *horizontalSpacer;
    QHBoxLayout *horizontalLayout;
    Gui::PrefCheckBox *autoUpdate;
    QPushButton *manualUpdate;

    void setupUi(QWidget *TaskSketcherMessages)
    {
        if (TaskSketcherMessages->objectName().isEmpty())
            TaskSketcherMessages->setObjectName(QString::fromUtf8("TaskSketcherMessages"));
        TaskSketcherMessages->resize(253, 115);
        verticalLayout = new QVBoxLayout(TaskSketcherMessages);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        labelConstrainStatus = new QLabel(TaskSketcherMessages);
        labelConstrainStatus->setObjectName(QString::fromUtf8("labelConstrainStatus"));
        QFont font;
        font.setFamily(QString::fromUtf8("Bitstream Charter"));
        font.setPointSize(9);
        labelConstrainStatus->setFont(font);
        labelConstrainStatus->setWordWrap(true);

        verticalLayout->addWidget(labelConstrainStatus);

        labelSolverStatus = new QLabel(TaskSketcherMessages);
        labelSolverStatus->setObjectName(QString::fromUtf8("labelSolverStatus"));
        labelSolverStatus->setFont(font);
        labelSolverStatus->setWordWrap(true);

        verticalLayout->addWidget(labelSolverStatus);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        verticalLayout->addItem(horizontalSpacer);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        autoUpdate = new Gui::PrefCheckBox(TaskSketcherMessages);
        autoUpdate->setObjectName(QString::fromUtf8("autoUpdate"));
        autoUpdate->setChecked(false);
        autoUpdate->setProperty("prefEntry", QVariant(QByteArray("AutoRecompute")));
        autoUpdate->setProperty("prefPath", QVariant(QByteArray("Mod/Sketcher")));

        horizontalLayout->addWidget(autoUpdate);

        manualUpdate = new QPushButton(TaskSketcherMessages);
        manualUpdate->setObjectName(QString::fromUtf8("manualUpdate"));

        horizontalLayout->addWidget(manualUpdate);


        verticalLayout->addLayout(horizontalLayout);


        retranslateUi(TaskSketcherMessages);

        QMetaObject::connectSlotsByName(TaskSketcherMessages);
    } // setupUi

    void retranslateUi(QWidget *TaskSketcherMessages)
    {
        TaskSketcherMessages->setWindowTitle(QApplication::translate("TaskSketcherMessages", "Form", 0, QApplication::UnicodeUTF8));
        labelConstrainStatus->setText(QApplication::translate("TaskSketcherMessages", "Undefined degrees of freedom", 0, QApplication::UnicodeUTF8));
        labelSolverStatus->setText(QApplication::translate("TaskSketcherMessages", "Not solved yet", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        autoUpdate->setToolTip(QApplication::translate("TaskSketcherMessages", "Executes a recompute of the active document after every command", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        autoUpdate->setText(QApplication::translate("TaskSketcherMessages", "Auto Update", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        manualUpdate->setToolTip(QApplication::translate("TaskSketcherMessages", "Forces a recompute of the active document", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        manualUpdate->setText(QApplication::translate("TaskSketcherMessages", "Update", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class TaskSketcherMessages: public Ui_TaskSketcherMessages {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_TASKSKETCHERMESSAGES_H
