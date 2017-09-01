/********************************************************************************
** Form generated from reading UI file 'DlgPrimitives.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DLGPRIMITIVES_H
#define UI_DLGPRIMITIVES_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QComboBox>
#include <QtGui/QDoubleSpinBox>
#include <QtGui/QFrame>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QSpinBox>
#include <QtGui/QStackedWidget>
#include <QtGui/QWidget>
#include "Gui/QuantitySpinBox.h"

namespace PartGui {

class Ui_DlgPrimitives
{
public:
    QGridLayout *gridLayout;
    QComboBox *comboBox1;
    QGroupBox *groupBox_2;
    QGridLayout *gridLayout1;
    QStackedWidget *widgetStack2;
    QWidget *page0_plane;
    QGridLayout *gridLayout2;
    QGridLayout *gridLayout3;
    Gui::QuantitySpinBox *planeLength;
    QLabel *textLabel3_2;
    QLabel *textLabel2_2;
    Gui::QuantitySpinBox *planeWidth;
    QSpacerItem *spacerItem;
    QWidget *Page1_box;
    QGridLayout *gridLayout4;
    QSpacerItem *spacerItem1;
    QGridLayout *gridLayout5;
    Gui::QuantitySpinBox *boxWidth;
    Gui::QuantitySpinBox *boxHeight;
    QLabel *textLabel4;
    QLabel *textLabel2;
    QLabel *textLabel3;
    Gui::QuantitySpinBox *boxLength;
    QWidget *Page2_cylinder;
    QGridLayout *gridLayout6;
    QHBoxLayout *hboxLayout;
    QLabel *label;
    Gui::QuantitySpinBox *cylinderAngle;
    QFrame *line_2;
    QSpacerItem *spacerItem2;
    QGridLayout *gridLayout7;
    QLabel *textLabel5;
    QLabel *textLabel6;
    Gui::QuantitySpinBox *cylinderHeight;
    Gui::QuantitySpinBox *cylinderRadius;
    QWidget *Page3_cone;
    QGridLayout *gridLayout8;
    QHBoxLayout *hboxLayout1;
    QLabel *label_4;
    Gui::QuantitySpinBox *coneAngle;
    QFrame *line_3;
    QSpacerItem *spacerItem3;
    QGridLayout *gridLayout9;
    Gui::QuantitySpinBox *coneHeight;
    Gui::QuantitySpinBox *coneRadius1;
    QLabel *textLabel11;
    QLabel *textLabel9;
    QLabel *textLabel10;
    Gui::QuantitySpinBox *coneRadius2;
    QWidget *Page4_sphere;
    QGridLayout *gridLayout10;
    QFrame *line;
    QGridLayout *gridLayout11;
    QSpacerItem *spacerItem4;
    QLabel *label_3;
    QLabel *label_2;
    Gui::QuantitySpinBox *sphereAngle1;
    Gui::QuantitySpinBox *sphereAngle2;
    Gui::QuantitySpinBox *sphereAngle3;
    QSpacerItem *spacerItem5;
    QHBoxLayout *hboxLayout2;
    QLabel *textLabel14;
    Gui::QuantitySpinBox *sphereRadius;
    QWidget *Page5_ellipsoid;
    QGridLayout *gridLayout12;
    QSpacerItem *spacerItem6;
    QFrame *line_5;
    QGridLayout *gridLayout13;
    QLabel *textLabel21;
    QLabel *textLabel22;
    QLabel *textLabel23;
    Gui::QuantitySpinBox *ellipsoidRadius1;
    Gui::QuantitySpinBox *ellipsoidRadius2;
    Gui::QuantitySpinBox *ellipsoidRadius3;
    QGridLayout *gridLayout14;
    QLabel *label23;
    QSpacerItem *spacerItem7;
    QLabel *label24;
    Gui::QuantitySpinBox *ellipsoidAngle3;
    Gui::QuantitySpinBox *ellipsoidAngle1;
    Gui::QuantitySpinBox *ellipsoidAngle2;
    QWidget *Page6_torus;
    QGridLayout *gridLayout15;
    QFrame *line_4;
    QGridLayout *gridLayout16;
    QLabel *label_5;
    QSpacerItem *spacerItem8;
    QLabel *label_6;
    Gui::QuantitySpinBox *torusAngle3;
    Gui::QuantitySpinBox *torusAngle1;
    Gui::QuantitySpinBox *torusAngle2;
    QSpacerItem *spacerItem9;
    QGridLayout *gridLayout17;
    Gui::QuantitySpinBox *torusRadius1;
    QLabel *textLabel20;
    QLabel *textLabel19;
    Gui::QuantitySpinBox *torusRadius2;
    QWidget *page_prism;
    QGridLayout *gridLayout18;
    QGridLayout *gridLayout19;
    Gui::QuantitySpinBox *prismCircumradius;
    QLabel *labelPrismPolygon;
    QSpinBox *prismPolygon;
    QLabel *labelPrismCircumradius;
    QLabel *labelPrismHeight;
    Gui::QuantitySpinBox *prismHeight;
    QSpacerItem *spacerItem10;
    QWidget *page7_wedge;
    QGridLayout *gridLayout_8;
    QGridLayout *gridLayout_2;
    QLabel *label_10;
    QLabel *label_11;
    QLabel *label_12;
    QLabel *label_13;
    QLabel *label_14;
    Gui::QuantitySpinBox *wedgeXmin;
    Gui::QuantitySpinBox *wedgeXmax;
    Gui::QuantitySpinBox *wedgeYmin;
    Gui::QuantitySpinBox *wedgeYmax;
    Gui::QuantitySpinBox *wedgeZmin;
    Gui::QuantitySpinBox *wedgeZmax;
    Gui::QuantitySpinBox *wedgeX2min;
    Gui::QuantitySpinBox *wedgeX2max;
    Gui::QuantitySpinBox *wedgeZ2min;
    Gui::QuantitySpinBox *wedgeZ2max;
    QSpacerItem *verticalSpacer_2;
    QWidget *page8_helix;
    QGridLayout *gridLayout20;
    QSpacerItem *spacerItem11;
    QGridLayout *gridLayout21;
    QLabel *label_9;
    QLabel *label_7;
    QLabel *label_8;
    QLabel *label_20;
    QLabel *label_15;
    QComboBox *helixLocalCS;
    Gui::QuantitySpinBox *helixAngle;
    Gui::QuantitySpinBox *helixPitch;
    Gui::QuantitySpinBox *helixHeight;
    Gui::QuantitySpinBox *helixRadius;
    QWidget *page9_spiral;
    QGridLayout *gridLayout22;
    QSpacerItem *spacerItem12;
    QGridLayout *gridLayout23;
    QLabel *label_spiral_radius;
    QLabel *label_spiral_growth;
    QLabel *label_spiral_rotation;
    Gui::QuantitySpinBox *spiralGrowth;
    QDoubleSpinBox *spiralRotation;
    Gui::QuantitySpinBox *spiralRadius;
    QWidget *page10_circle;
    QGridLayout *gridLayout_3;
    QGridLayout *circleParameters;
    QLabel *Radius;
    QLabel *Angle0;
    QLabel *Angle1;
    Gui::QuantitySpinBox *circleAngle0;
    Gui::QuantitySpinBox *circleAngle1;
    Gui::QuantitySpinBox *circleRadius;
    QHBoxLayout *horizontalLayout;
    QSpacerItem *horizontalSpacer;
    QPushButton *buttonCircleFromThreePoints;
    QSpacerItem *verticalSpacer;
    QWidget *page;
    QGridLayout *gridLayout_11;
    QGridLayout *gridLayout_10;
    QLabel *labelEllMajorRadius;
    QLabel *labelEllMinorRadius;
    QLabel *labelEllAngle1;
    QLabel *labelEllAngle2;
    Gui::QuantitySpinBox *ellipseMajorRadius;
    Gui::QuantitySpinBox *ellipseMinorRadius;
    Gui::QuantitySpinBox *ellipseAngle0;
    Gui::QuantitySpinBox *ellipseAngle1;
    QSpacerItem *verticalSpacer_5;
    QWidget *page11_vertex;
    QGridLayout *gridLayout_9;
    QGridLayout *gridLayout_4;
    QLabel *label_X_Axis;
    QLabel *label_Y_Axis;
    QLabel *label_Z_Axis;
    Gui::QuantitySpinBox *vertexX;
    Gui::QuantitySpinBox *vertexY;
    Gui::QuantitySpinBox *vertexZ;
    QSpacerItem *verticalSpacer_3;
    QWidget *page12_edge;
    QGridLayout *gridLayout_6;
    QGridLayout *gridLayout_5;
    QLabel *X1;
    QLabel *Y1;
    QLabel *Z1;
    QFrame *line_6;
    QLabel *Finish_Vertex;
    QLabel *Start_Vertex;
    QLabel *X2;
    QLabel *Y2;
    QLabel *Z2;
    Gui::QuantitySpinBox *edgeX1;
    Gui::QuantitySpinBox *edgeY1;
    Gui::QuantitySpinBox *edgeZ1;
    Gui::QuantitySpinBox *edgeX2;
    Gui::QuantitySpinBox *edgeY2;
    Gui::QuantitySpinBox *edgeZ2;
    QSpacerItem *verticalSpacer_4;
    QWidget *page_regularPolygon;
    QGridLayout *gridLayout24;
    QGridLayout *gridLayout25;
    QLabel *labelRegularPolygonPolygon;
    QSpinBox *regularPolygonPolygon;
    QLabel *labelRegularPolygonCircumradius;
    Gui::QuantitySpinBox *regularPolygonCircumradius;
    QSpacerItem *spacerItem13;

    void setupUi(QWidget *PartGui__DlgPrimitives)
    {
        if (PartGui__DlgPrimitives->objectName().isEmpty())
            PartGui__DlgPrimitives->setObjectName(QString::fromUtf8("PartGui__DlgPrimitives"));
        PartGui__DlgPrimitives->resize(317, 370);
        PartGui__DlgPrimitives->setProperty("sizeGripEnabled", QVariant(true));
        gridLayout = new QGridLayout(PartGui__DlgPrimitives);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        comboBox1 = new QComboBox(PartGui__DlgPrimitives);
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/icons/Tree_Part_Plane_Parametric.svg"), QSize(), QIcon::Normal, QIcon::Off);
        comboBox1->addItem(icon, QString());
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/icons/Tree_Part_Box_Parametric.svg"), QSize(), QIcon::Normal, QIcon::Off);
        comboBox1->addItem(icon1, QString());
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/icons/Tree_Part_Cylinder_Parametric.svg"), QSize(), QIcon::Normal, QIcon::Off);
        comboBox1->addItem(icon2, QString());
        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/icons/Tree_Part_Cone_Parametric.svg"), QSize(), QIcon::Normal, QIcon::Off);
        comboBox1->addItem(icon3, QString());
        QIcon icon4;
        icon4.addFile(QString::fromUtf8(":/icons/Tree_Part_Sphere_Parametric.svg"), QSize(), QIcon::Normal, QIcon::Off);
        comboBox1->addItem(icon4, QString());
        QIcon icon5;
        icon5.addFile(QString::fromUtf8(":/icons/Tree_Part_Ellipsoid_Parametric.svg"), QSize(), QIcon::Normal, QIcon::Off);
        comboBox1->addItem(icon5, QString());
        QIcon icon6;
        icon6.addFile(QString::fromUtf8(":/icons/Tree_Part_Torus_Parametric.svg"), QSize(), QIcon::Normal, QIcon::Off);
        comboBox1->addItem(icon6, QString());
        QIcon icon7;
        icon7.addFile(QString::fromUtf8(":/icons/Tree_Part_Prism.svg"), QSize(), QIcon::Normal, QIcon::Off);
        comboBox1->addItem(icon7, QString());
        QIcon icon8;
        icon8.addFile(QString::fromUtf8(":/icons/Tree_Part_Wedge.svg"), QSize(), QIcon::Normal, QIcon::Off);
        comboBox1->addItem(icon8, QString());
        QIcon icon9;
        icon9.addFile(QString::fromUtf8(":/icons/Part_Helix_Parametric.svg"), QSize(), QIcon::Normal, QIcon::Off);
        comboBox1->addItem(icon9, QString());
        QIcon icon10;
        icon10.addFile(QString::fromUtf8(":/icons/Part_Spiral_Parametric.svg"), QSize(), QIcon::Normal, QIcon::Off);
        comboBox1->addItem(icon10, QString());
        QIcon icon11;
        icon11.addFile(QString::fromUtf8(":/icons/Part_Circle_Parametric.svg"), QSize(), QIcon::Normal, QIcon::Off);
        comboBox1->addItem(icon11, QString());
        QIcon icon12;
        icon12.addFile(QString::fromUtf8(":/icons/Part_Ellipse_Parametric.svg"), QSize(), QIcon::Normal, QIcon::Off);
        comboBox1->addItem(icon12, QString());
        QIcon icon13;
        icon13.addFile(QString::fromUtf8(":/icons/Part_Point_Parametric.svg"), QSize(), QIcon::Normal, QIcon::Off);
        comboBox1->addItem(icon13, QString());
        QIcon icon14;
        icon14.addFile(QString::fromUtf8(":/icons/Part_Line_Parametric.svg"), QSize(), QIcon::Normal, QIcon::Off);
        comboBox1->addItem(icon14, QString());
        QIcon icon15;
        icon15.addFile(QString::fromUtf8(":/icons/Part_Polygon_Parametric.svg"), QSize(), QIcon::Normal, QIcon::Off);
        comboBox1->addItem(icon15, QString());
        comboBox1->setObjectName(QString::fromUtf8("comboBox1"));
        QSizePolicy sizePolicy(QSizePolicy::Minimum, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(comboBox1->sizePolicy().hasHeightForWidth());
        comboBox1->setSizePolicy(sizePolicy);
        comboBox1->setMaxVisibleItems(16);

        gridLayout->addWidget(comboBox1, 0, 0, 1, 1);

        groupBox_2 = new QGroupBox(PartGui__DlgPrimitives);
        groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
        gridLayout1 = new QGridLayout(groupBox_2);
        gridLayout1->setSpacing(6);
        gridLayout1->setContentsMargins(9, 9, 9, 9);
        gridLayout1->setObjectName(QString::fromUtf8("gridLayout1"));
        widgetStack2 = new QStackedWidget(groupBox_2);
        widgetStack2->setObjectName(QString::fromUtf8("widgetStack2"));
        page0_plane = new QWidget();
        page0_plane->setObjectName(QString::fromUtf8("page0_plane"));
        gridLayout2 = new QGridLayout(page0_plane);
        gridLayout2->setSpacing(6);
        gridLayout2->setContentsMargins(9, 9, 9, 9);
        gridLayout2->setObjectName(QString::fromUtf8("gridLayout2"));
        gridLayout3 = new QGridLayout();
        gridLayout3->setSpacing(6);
        gridLayout3->setContentsMargins(0, 0, 0, 0);
        gridLayout3->setObjectName(QString::fromUtf8("gridLayout3"));
        planeLength = new Gui::QuantitySpinBox(page0_plane);
        planeLength->setObjectName(QString::fromUtf8("planeLength"));
        planeLength->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        planeLength->setValue(10);

        gridLayout3->addWidget(planeLength, 0, 2, 1, 1);

        textLabel3_2 = new QLabel(page0_plane);
        textLabel3_2->setObjectName(QString::fromUtf8("textLabel3_2"));

        gridLayout3->addWidget(textLabel3_2, 1, 0, 1, 1);

        textLabel2_2 = new QLabel(page0_plane);
        textLabel2_2->setObjectName(QString::fromUtf8("textLabel2_2"));

        gridLayout3->addWidget(textLabel2_2, 0, 0, 1, 1);

        planeWidth = new Gui::QuantitySpinBox(page0_plane);
        planeWidth->setObjectName(QString::fromUtf8("planeWidth"));
        planeWidth->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        planeWidth->setValue(10);

        gridLayout3->addWidget(planeWidth, 1, 2, 1, 1);


        gridLayout2->addLayout(gridLayout3, 0, 0, 1, 1);

        spacerItem = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout2->addItem(spacerItem, 1, 0, 1, 1);

        widgetStack2->addWidget(page0_plane);
        Page1_box = new QWidget();
        Page1_box->setObjectName(QString::fromUtf8("Page1_box"));
        gridLayout4 = new QGridLayout(Page1_box);
        gridLayout4->setSpacing(6);
        gridLayout4->setContentsMargins(9, 9, 9, 9);
        gridLayout4->setObjectName(QString::fromUtf8("gridLayout4"));
        spacerItem1 = new QSpacerItem(20, 51, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout4->addItem(spacerItem1, 1, 0, 1, 1);

        gridLayout5 = new QGridLayout();
        gridLayout5->setSpacing(6);
        gridLayout5->setContentsMargins(0, 0, 0, 0);
        gridLayout5->setObjectName(QString::fromUtf8("gridLayout5"));
        boxWidth = new Gui::QuantitySpinBox(Page1_box);
        boxWidth->setObjectName(QString::fromUtf8("boxWidth"));
        boxWidth->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        boxWidth->setValue(10);

        gridLayout5->addWidget(boxWidth, 1, 2, 1, 1);

        boxHeight = new Gui::QuantitySpinBox(Page1_box);
        boxHeight->setObjectName(QString::fromUtf8("boxHeight"));
        boxHeight->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        boxHeight->setValue(10);

        gridLayout5->addWidget(boxHeight, 2, 2, 1, 1);

        textLabel4 = new QLabel(Page1_box);
        textLabel4->setObjectName(QString::fromUtf8("textLabel4"));

        gridLayout5->addWidget(textLabel4, 2, 0, 1, 1);

        textLabel2 = new QLabel(Page1_box);
        textLabel2->setObjectName(QString::fromUtf8("textLabel2"));

        gridLayout5->addWidget(textLabel2, 0, 0, 1, 1);

        textLabel3 = new QLabel(Page1_box);
        textLabel3->setObjectName(QString::fromUtf8("textLabel3"));

        gridLayout5->addWidget(textLabel3, 1, 0, 1, 1);

        boxLength = new Gui::QuantitySpinBox(Page1_box);
        boxLength->setObjectName(QString::fromUtf8("boxLength"));
        boxLength->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        boxLength->setValue(10);

        gridLayout5->addWidget(boxLength, 0, 2, 1, 1);


        gridLayout4->addLayout(gridLayout5, 0, 0, 1, 1);

        widgetStack2->addWidget(Page1_box);
        Page2_cylinder = new QWidget();
        Page2_cylinder->setObjectName(QString::fromUtf8("Page2_cylinder"));
        gridLayout6 = new QGridLayout(Page2_cylinder);
        gridLayout6->setSpacing(6);
        gridLayout6->setContentsMargins(9, 9, 9, 9);
        gridLayout6->setObjectName(QString::fromUtf8("gridLayout6"));
        hboxLayout = new QHBoxLayout();
        hboxLayout->setSpacing(6);
        hboxLayout->setContentsMargins(0, 0, 0, 0);
        hboxLayout->setObjectName(QString::fromUtf8("hboxLayout"));
        label = new QLabel(Page2_cylinder);
        label->setObjectName(QString::fromUtf8("label"));

        hboxLayout->addWidget(label);

        cylinderAngle = new Gui::QuantitySpinBox(Page2_cylinder);
        cylinderAngle->setObjectName(QString::fromUtf8("cylinderAngle"));
        cylinderAngle->setProperty("unit", QVariant(QString::fromUtf8("deg")));
        cylinderAngle->setValue(360);

        hboxLayout->addWidget(cylinderAngle);


        gridLayout6->addLayout(hboxLayout, 2, 0, 1, 1);

        line_2 = new QFrame(Page2_cylinder);
        line_2->setObjectName(QString::fromUtf8("line_2"));
        line_2->setFrameShape(QFrame::HLine);
        line_2->setFrameShadow(QFrame::Sunken);

        gridLayout6->addWidget(line_2, 1, 0, 1, 1);

        spacerItem2 = new QSpacerItem(31, 81, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout6->addItem(spacerItem2, 3, 0, 1, 1);

        gridLayout7 = new QGridLayout();
        gridLayout7->setSpacing(6);
        gridLayout7->setContentsMargins(0, 0, 0, 0);
        gridLayout7->setObjectName(QString::fromUtf8("gridLayout7"));
        textLabel5 = new QLabel(Page2_cylinder);
        textLabel5->setObjectName(QString::fromUtf8("textLabel5"));

        gridLayout7->addWidget(textLabel5, 0, 0, 1, 1);

        textLabel6 = new QLabel(Page2_cylinder);
        textLabel6->setObjectName(QString::fromUtf8("textLabel6"));

        gridLayout7->addWidget(textLabel6, 1, 0, 1, 1);

        cylinderHeight = new Gui::QuantitySpinBox(Page2_cylinder);
        cylinderHeight->setObjectName(QString::fromUtf8("cylinderHeight"));
        cylinderHeight->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        cylinderHeight->setValue(10);

        gridLayout7->addWidget(cylinderHeight, 1, 1, 1, 1);

        cylinderRadius = new Gui::QuantitySpinBox(Page2_cylinder);
        cylinderRadius->setObjectName(QString::fromUtf8("cylinderRadius"));
        cylinderRadius->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        cylinderRadius->setValue(2);

        gridLayout7->addWidget(cylinderRadius, 0, 1, 1, 1);


        gridLayout6->addLayout(gridLayout7, 0, 0, 1, 1);

        widgetStack2->addWidget(Page2_cylinder);
        Page3_cone = new QWidget();
        Page3_cone->setObjectName(QString::fromUtf8("Page3_cone"));
        gridLayout8 = new QGridLayout(Page3_cone);
        gridLayout8->setSpacing(6);
        gridLayout8->setContentsMargins(9, 9, 9, 9);
        gridLayout8->setObjectName(QString::fromUtf8("gridLayout8"));
        hboxLayout1 = new QHBoxLayout();
        hboxLayout1->setSpacing(6);
        hboxLayout1->setContentsMargins(0, 0, 0, 0);
        hboxLayout1->setObjectName(QString::fromUtf8("hboxLayout1"));
        label_4 = new QLabel(Page3_cone);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        hboxLayout1->addWidget(label_4);

        coneAngle = new Gui::QuantitySpinBox(Page3_cone);
        coneAngle->setObjectName(QString::fromUtf8("coneAngle"));
        coneAngle->setProperty("unit", QVariant(QString::fromUtf8("deg")));
        coneAngle->setValue(360);

        hboxLayout1->addWidget(coneAngle);


        gridLayout8->addLayout(hboxLayout1, 2, 0, 1, 1);

        line_3 = new QFrame(Page3_cone);
        line_3->setObjectName(QString::fromUtf8("line_3"));
        line_3->setFrameShape(QFrame::HLine);
        line_3->setFrameShadow(QFrame::Sunken);

        gridLayout8->addWidget(line_3, 1, 0, 1, 1);

        spacerItem3 = new QSpacerItem(31, 91, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout8->addItem(spacerItem3, 3, 0, 1, 1);

        gridLayout9 = new QGridLayout();
        gridLayout9->setSpacing(6);
        gridLayout9->setContentsMargins(0, 0, 0, 0);
        gridLayout9->setObjectName(QString::fromUtf8("gridLayout9"));
        coneHeight = new Gui::QuantitySpinBox(Page3_cone);
        coneHeight->setObjectName(QString::fromUtf8("coneHeight"));
        coneHeight->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        coneHeight->setValue(10);

        gridLayout9->addWidget(coneHeight, 3, 2, 1, 1);

        coneRadius1 = new Gui::QuantitySpinBox(Page3_cone);
        coneRadius1->setObjectName(QString::fromUtf8("coneRadius1"));
        coneRadius1->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        coneRadius1->setValue(2);

        gridLayout9->addWidget(coneRadius1, 0, 2, 1, 1);

        textLabel11 = new QLabel(Page3_cone);
        textLabel11->setObjectName(QString::fromUtf8("textLabel11"));

        gridLayout9->addWidget(textLabel11, 2, 0, 2, 1);

        textLabel9 = new QLabel(Page3_cone);
        textLabel9->setObjectName(QString::fromUtf8("textLabel9"));

        gridLayout9->addWidget(textLabel9, 0, 0, 1, 1);

        textLabel10 = new QLabel(Page3_cone);
        textLabel10->setObjectName(QString::fromUtf8("textLabel10"));

        gridLayout9->addWidget(textLabel10, 1, 0, 1, 1);

        coneRadius2 = new Gui::QuantitySpinBox(Page3_cone);
        coneRadius2->setObjectName(QString::fromUtf8("coneRadius2"));
        coneRadius2->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        coneRadius2->setValue(4);

        gridLayout9->addWidget(coneRadius2, 1, 2, 1, 1);


        gridLayout8->addLayout(gridLayout9, 0, 0, 1, 1);

        widgetStack2->addWidget(Page3_cone);
        Page4_sphere = new QWidget();
        Page4_sphere->setObjectName(QString::fromUtf8("Page4_sphere"));
        gridLayout10 = new QGridLayout(Page4_sphere);
        gridLayout10->setSpacing(6);
        gridLayout10->setContentsMargins(9, 9, 9, 9);
        gridLayout10->setObjectName(QString::fromUtf8("gridLayout10"));
        line = new QFrame(Page4_sphere);
        line->setObjectName(QString::fromUtf8("line"));
        line->setFrameShape(QFrame::HLine);
        line->setFrameShadow(QFrame::Sunken);

        gridLayout10->addWidget(line, 1, 0, 1, 1);

        gridLayout11 = new QGridLayout();
        gridLayout11->setSpacing(6);
        gridLayout11->setContentsMargins(0, 0, 0, 0);
        gridLayout11->setObjectName(QString::fromUtf8("gridLayout11"));
        spacerItem4 = new QSpacerItem(81, 20, QSizePolicy::Preferred, QSizePolicy::Minimum);

        gridLayout11->addItem(spacerItem4, 2, 0, 1, 1);

        label_3 = new QLabel(Page4_sphere);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout11->addWidget(label_3, 0, 0, 1, 1);

        label_2 = new QLabel(Page4_sphere);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout11->addWidget(label_2, 1, 0, 1, 1);

        sphereAngle1 = new Gui::QuantitySpinBox(Page4_sphere);
        sphereAngle1->setObjectName(QString::fromUtf8("sphereAngle1"));
        sphereAngle1->setProperty("unit", QVariant(QString::fromUtf8("deg")));
        sphereAngle1->setValue(-90);

        gridLayout11->addWidget(sphereAngle1, 1, 2, 1, 1);

        sphereAngle2 = new Gui::QuantitySpinBox(Page4_sphere);
        sphereAngle2->setObjectName(QString::fromUtf8("sphereAngle2"));
        sphereAngle2->setProperty("unit", QVariant(QString::fromUtf8("deg")));
        sphereAngle2->setValue(90);

        gridLayout11->addWidget(sphereAngle2, 2, 2, 1, 1);

        sphereAngle3 = new Gui::QuantitySpinBox(Page4_sphere);
        sphereAngle3->setObjectName(QString::fromUtf8("sphereAngle3"));
        sphereAngle3->setProperty("unit", QVariant(QString::fromUtf8("deg")));
        sphereAngle3->setValue(360);

        gridLayout11->addWidget(sphereAngle3, 0, 2, 1, 1);


        gridLayout10->addLayout(gridLayout11, 2, 0, 1, 1);

        spacerItem5 = new QSpacerItem(21, 151, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout10->addItem(spacerItem5, 3, 0, 1, 1);

        hboxLayout2 = new QHBoxLayout();
        hboxLayout2->setSpacing(6);
        hboxLayout2->setContentsMargins(0, 0, 0, 0);
        hboxLayout2->setObjectName(QString::fromUtf8("hboxLayout2"));
        textLabel14 = new QLabel(Page4_sphere);
        textLabel14->setObjectName(QString::fromUtf8("textLabel14"));

        hboxLayout2->addWidget(textLabel14);

        sphereRadius = new Gui::QuantitySpinBox(Page4_sphere);
        sphereRadius->setObjectName(QString::fromUtf8("sphereRadius"));
        sphereRadius->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        sphereRadius->setValue(5);

        hboxLayout2->addWidget(sphereRadius);


        gridLayout10->addLayout(hboxLayout2, 0, 0, 1, 1);

        widgetStack2->addWidget(Page4_sphere);
        Page5_ellipsoid = new QWidget();
        Page5_ellipsoid->setObjectName(QString::fromUtf8("Page5_ellipsoid"));
        gridLayout12 = new QGridLayout(Page5_ellipsoid);
        gridLayout12->setSpacing(6);
        gridLayout12->setContentsMargins(9, 9, 9, 9);
        gridLayout12->setObjectName(QString::fromUtf8("gridLayout12"));
        spacerItem6 = new QSpacerItem(20, 20, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout12->addItem(spacerItem6, 3, 0, 1, 1);

        line_5 = new QFrame(Page5_ellipsoid);
        line_5->setObjectName(QString::fromUtf8("line_5"));
        line_5->setFrameShape(QFrame::HLine);
        line_5->setFrameShadow(QFrame::Sunken);

        gridLayout12->addWidget(line_5, 1, 0, 1, 1);

        gridLayout13 = new QGridLayout();
        gridLayout13->setSpacing(6);
        gridLayout13->setContentsMargins(0, 0, 0, 0);
        gridLayout13->setObjectName(QString::fromUtf8("gridLayout13"));
        textLabel21 = new QLabel(Page5_ellipsoid);
        textLabel21->setObjectName(QString::fromUtf8("textLabel21"));

        gridLayout13->addWidget(textLabel21, 0, 0, 1, 1);

        textLabel22 = new QLabel(Page5_ellipsoid);
        textLabel22->setObjectName(QString::fromUtf8("textLabel22"));

        gridLayout13->addWidget(textLabel22, 1, 0, 1, 1);

        textLabel23 = new QLabel(Page5_ellipsoid);
        textLabel23->setObjectName(QString::fromUtf8("textLabel23"));

        gridLayout13->addWidget(textLabel23, 2, 0, 1, 1);

        ellipsoidRadius1 = new Gui::QuantitySpinBox(Page5_ellipsoid);
        ellipsoidRadius1->setObjectName(QString::fromUtf8("ellipsoidRadius1"));
        ellipsoidRadius1->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        ellipsoidRadius1->setValue(2);

        gridLayout13->addWidget(ellipsoidRadius1, 0, 1, 1, 1);

        ellipsoidRadius2 = new Gui::QuantitySpinBox(Page5_ellipsoid);
        ellipsoidRadius2->setObjectName(QString::fromUtf8("ellipsoidRadius2"));
        ellipsoidRadius2->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        ellipsoidRadius2->setValue(4);

        gridLayout13->addWidget(ellipsoidRadius2, 1, 1, 1, 1);

        ellipsoidRadius3 = new Gui::QuantitySpinBox(Page5_ellipsoid);
        ellipsoidRadius3->setObjectName(QString::fromUtf8("ellipsoidRadius3"));
        ellipsoidRadius3->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        ellipsoidRadius3->setValue(4);

        gridLayout13->addWidget(ellipsoidRadius3, 2, 1, 1, 1);


        gridLayout12->addLayout(gridLayout13, 0, 0, 1, 1);

        gridLayout14 = new QGridLayout();
        gridLayout14->setSpacing(6);
        gridLayout14->setContentsMargins(0, 0, 0, 0);
        gridLayout14->setObjectName(QString::fromUtf8("gridLayout14"));
        label23 = new QLabel(Page5_ellipsoid);
        label23->setObjectName(QString::fromUtf8("label23"));

        gridLayout14->addWidget(label23, 0, 0, 1, 1);

        spacerItem7 = new QSpacerItem(81, 20, QSizePolicy::Preferred, QSizePolicy::Minimum);

        gridLayout14->addItem(spacerItem7, 2, 0, 1, 1);

        label24 = new QLabel(Page5_ellipsoid);
        label24->setObjectName(QString::fromUtf8("label24"));

        gridLayout14->addWidget(label24, 1, 0, 1, 1);

        ellipsoidAngle3 = new Gui::QuantitySpinBox(Page5_ellipsoid);
        ellipsoidAngle3->setObjectName(QString::fromUtf8("ellipsoidAngle3"));
        ellipsoidAngle3->setProperty("unit", QVariant(QString::fromUtf8("deg")));
        ellipsoidAngle3->setValue(360);

        gridLayout14->addWidget(ellipsoidAngle3, 0, 1, 1, 1);

        ellipsoidAngle1 = new Gui::QuantitySpinBox(Page5_ellipsoid);
        ellipsoidAngle1->setObjectName(QString::fromUtf8("ellipsoidAngle1"));
        ellipsoidAngle1->setProperty("unit", QVariant(QString::fromUtf8("deg")));
        ellipsoidAngle1->setValue(-90);

        gridLayout14->addWidget(ellipsoidAngle1, 1, 1, 1, 1);

        ellipsoidAngle2 = new Gui::QuantitySpinBox(Page5_ellipsoid);
        ellipsoidAngle2->setObjectName(QString::fromUtf8("ellipsoidAngle2"));
        ellipsoidAngle2->setProperty("unit", QVariant(QString::fromUtf8("deg")));
        ellipsoidAngle2->setValue(90);

        gridLayout14->addWidget(ellipsoidAngle2, 2, 1, 1, 1);


        gridLayout12->addLayout(gridLayout14, 2, 0, 1, 1);

        widgetStack2->addWidget(Page5_ellipsoid);
        Page6_torus = new QWidget();
        Page6_torus->setObjectName(QString::fromUtf8("Page6_torus"));
        gridLayout15 = new QGridLayout(Page6_torus);
        gridLayout15->setSpacing(6);
        gridLayout15->setContentsMargins(9, 9, 9, 9);
        gridLayout15->setObjectName(QString::fromUtf8("gridLayout15"));
        line_4 = new QFrame(Page6_torus);
        line_4->setObjectName(QString::fromUtf8("line_4"));
        line_4->setFrameShape(QFrame::HLine);
        line_4->setFrameShadow(QFrame::Sunken);

        gridLayout15->addWidget(line_4, 1, 0, 1, 1);

        gridLayout16 = new QGridLayout();
        gridLayout16->setSpacing(6);
        gridLayout16->setContentsMargins(0, 0, 0, 0);
        gridLayout16->setObjectName(QString::fromUtf8("gridLayout16"));
        label_5 = new QLabel(Page6_torus);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        gridLayout16->addWidget(label_5, 0, 0, 1, 1);

        spacerItem8 = new QSpacerItem(81, 20, QSizePolicy::Preferred, QSizePolicy::Minimum);

        gridLayout16->addItem(spacerItem8, 2, 0, 1, 1);

        label_6 = new QLabel(Page6_torus);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        gridLayout16->addWidget(label_6, 1, 0, 1, 1);

        torusAngle3 = new Gui::QuantitySpinBox(Page6_torus);
        torusAngle3->setObjectName(QString::fromUtf8("torusAngle3"));
        torusAngle3->setProperty("unit", QVariant(QString::fromUtf8("deg")));
        torusAngle3->setValue(360);

        gridLayout16->addWidget(torusAngle3, 0, 1, 1, 1);

        torusAngle1 = new Gui::QuantitySpinBox(Page6_torus);
        torusAngle1->setObjectName(QString::fromUtf8("torusAngle1"));
        torusAngle1->setProperty("unit", QVariant(QString::fromUtf8("deg")));
        torusAngle1->setValue(-180);

        gridLayout16->addWidget(torusAngle1, 1, 1, 1, 1);

        torusAngle2 = new Gui::QuantitySpinBox(Page6_torus);
        torusAngle2->setObjectName(QString::fromUtf8("torusAngle2"));
        torusAngle2->setProperty("unit", QVariant(QString::fromUtf8("deg")));
        torusAngle2->setValue(180);

        gridLayout16->addWidget(torusAngle2, 2, 1, 1, 1);


        gridLayout15->addLayout(gridLayout16, 2, 0, 1, 1);

        spacerItem9 = new QSpacerItem(20, 91, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout15->addItem(spacerItem9, 3, 0, 1, 1);

        gridLayout17 = new QGridLayout();
        gridLayout17->setSpacing(6);
        gridLayout17->setContentsMargins(0, 0, 0, 0);
        gridLayout17->setObjectName(QString::fromUtf8("gridLayout17"));
        torusRadius1 = new Gui::QuantitySpinBox(Page6_torus);
        torusRadius1->setObjectName(QString::fromUtf8("torusRadius1"));
        torusRadius1->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        torusRadius1->setValue(10);

        gridLayout17->addWidget(torusRadius1, 0, 2, 1, 1);

        textLabel20 = new QLabel(Page6_torus);
        textLabel20->setObjectName(QString::fromUtf8("textLabel20"));

        gridLayout17->addWidget(textLabel20, 1, 0, 1, 1);

        textLabel19 = new QLabel(Page6_torus);
        textLabel19->setObjectName(QString::fromUtf8("textLabel19"));

        gridLayout17->addWidget(textLabel19, 0, 0, 1, 1);

        torusRadius2 = new Gui::QuantitySpinBox(Page6_torus);
        torusRadius2->setObjectName(QString::fromUtf8("torusRadius2"));
        torusRadius2->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        torusRadius2->setValue(2);

        gridLayout17->addWidget(torusRadius2, 1, 2, 1, 1);


        gridLayout15->addLayout(gridLayout17, 0, 0, 1, 1);

        widgetStack2->addWidget(Page6_torus);
        page_prism = new QWidget();
        page_prism->setObjectName(QString::fromUtf8("page_prism"));
        gridLayout18 = new QGridLayout(page_prism);
        gridLayout18->setSpacing(6);
        gridLayout18->setContentsMargins(9, 9, 9, 9);
        gridLayout18->setObjectName(QString::fromUtf8("gridLayout18"));
        gridLayout19 = new QGridLayout();
        gridLayout19->setSpacing(6);
        gridLayout19->setContentsMargins(0, 0, 0, 0);
        gridLayout19->setObjectName(QString::fromUtf8("gridLayout19"));
        prismCircumradius = new Gui::QuantitySpinBox(page_prism);
        prismCircumradius->setObjectName(QString::fromUtf8("prismCircumradius"));
        prismCircumradius->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        prismCircumradius->setValue(2);

        gridLayout19->addWidget(prismCircumradius, 1, 2, 1, 1);

        labelPrismPolygon = new QLabel(page_prism);
        labelPrismPolygon->setObjectName(QString::fromUtf8("labelPrismPolygon"));

        gridLayout19->addWidget(labelPrismPolygon, 0, 0, 1, 1);

        prismPolygon = new QSpinBox(page_prism);
        prismPolygon->setObjectName(QString::fromUtf8("prismPolygon"));
        prismPolygon->setMinimum(3);
        prismPolygon->setMaximum(1000);
        prismPolygon->setValue(6);

        gridLayout19->addWidget(prismPolygon, 0, 2, 1, 1);

        labelPrismCircumradius = new QLabel(page_prism);
        labelPrismCircumradius->setObjectName(QString::fromUtf8("labelPrismCircumradius"));

        gridLayout19->addWidget(labelPrismCircumradius, 1, 0, 1, 1);

        labelPrismHeight = new QLabel(page_prism);
        labelPrismHeight->setObjectName(QString::fromUtf8("labelPrismHeight"));

        gridLayout19->addWidget(labelPrismHeight, 2, 0, 1, 1);

        prismHeight = new Gui::QuantitySpinBox(page_prism);
        prismHeight->setObjectName(QString::fromUtf8("prismHeight"));
        prismHeight->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        prismHeight->setValue(10);

        gridLayout19->addWidget(prismHeight, 2, 2, 1, 1);


        gridLayout18->addLayout(gridLayout19, 0, 0, 1, 1);

        spacerItem10 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout18->addItem(spacerItem10, 1, 0, 1, 1);

        widgetStack2->addWidget(page_prism);
        page7_wedge = new QWidget();
        page7_wedge->setObjectName(QString::fromUtf8("page7_wedge"));
        gridLayout_8 = new QGridLayout(page7_wedge);
        gridLayout_8->setSpacing(6);
        gridLayout_8->setContentsMargins(11, 11, 11, 11);
        gridLayout_8->setObjectName(QString::fromUtf8("gridLayout_8"));
        gridLayout_2 = new QGridLayout();
        gridLayout_2->setSpacing(6);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        gridLayout_2->setSizeConstraint(QLayout::SetDefaultConstraint);
        gridLayout_2->setHorizontalSpacing(4);
        label_10 = new QLabel(page7_wedge);
        label_10->setObjectName(QString::fromUtf8("label_10"));

        gridLayout_2->addWidget(label_10, 0, 0, 1, 1);

        label_11 = new QLabel(page7_wedge);
        label_11->setObjectName(QString::fromUtf8("label_11"));

        gridLayout_2->addWidget(label_11, 1, 0, 1, 1);

        label_12 = new QLabel(page7_wedge);
        label_12->setObjectName(QString::fromUtf8("label_12"));

        gridLayout_2->addWidget(label_12, 2, 0, 1, 1);

        label_13 = new QLabel(page7_wedge);
        label_13->setObjectName(QString::fromUtf8("label_13"));

        gridLayout_2->addWidget(label_13, 3, 0, 1, 1);

        label_14 = new QLabel(page7_wedge);
        label_14->setObjectName(QString::fromUtf8("label_14"));

        gridLayout_2->addWidget(label_14, 4, 0, 1, 1);

        wedgeXmin = new Gui::QuantitySpinBox(page7_wedge);
        wedgeXmin->setObjectName(QString::fromUtf8("wedgeXmin"));
        wedgeXmin->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        wedgeXmin->setValue(0);

        gridLayout_2->addWidget(wedgeXmin, 0, 1, 1, 1);

        wedgeXmax = new Gui::QuantitySpinBox(page7_wedge);
        wedgeXmax->setObjectName(QString::fromUtf8("wedgeXmax"));
        wedgeXmax->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        wedgeXmax->setValue(10);

        gridLayout_2->addWidget(wedgeXmax, 0, 2, 1, 1);

        wedgeYmin = new Gui::QuantitySpinBox(page7_wedge);
        wedgeYmin->setObjectName(QString::fromUtf8("wedgeYmin"));
        wedgeYmin->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        wedgeYmin->setValue(0);

        gridLayout_2->addWidget(wedgeYmin, 1, 1, 1, 1);

        wedgeYmax = new Gui::QuantitySpinBox(page7_wedge);
        wedgeYmax->setObjectName(QString::fromUtf8("wedgeYmax"));
        wedgeYmax->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        wedgeYmax->setValue(10);

        gridLayout_2->addWidget(wedgeYmax, 1, 2, 1, 1);

        wedgeZmin = new Gui::QuantitySpinBox(page7_wedge);
        wedgeZmin->setObjectName(QString::fromUtf8("wedgeZmin"));
        wedgeZmin->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        wedgeZmin->setValue(0);

        gridLayout_2->addWidget(wedgeZmin, 2, 1, 1, 1);

        wedgeZmax = new Gui::QuantitySpinBox(page7_wedge);
        wedgeZmax->setObjectName(QString::fromUtf8("wedgeZmax"));
        wedgeZmax->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        wedgeZmax->setValue(10);

        gridLayout_2->addWidget(wedgeZmax, 2, 2, 1, 1);

        wedgeX2min = new Gui::QuantitySpinBox(page7_wedge);
        wedgeX2min->setObjectName(QString::fromUtf8("wedgeX2min"));
        wedgeX2min->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        wedgeX2min->setValue(2);

        gridLayout_2->addWidget(wedgeX2min, 3, 1, 1, 1);

        wedgeX2max = new Gui::QuantitySpinBox(page7_wedge);
        wedgeX2max->setObjectName(QString::fromUtf8("wedgeX2max"));
        wedgeX2max->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        wedgeX2max->setValue(8);

        gridLayout_2->addWidget(wedgeX2max, 3, 2, 1, 1);

        wedgeZ2min = new Gui::QuantitySpinBox(page7_wedge);
        wedgeZ2min->setObjectName(QString::fromUtf8("wedgeZ2min"));
        wedgeZ2min->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        wedgeZ2min->setValue(2);

        gridLayout_2->addWidget(wedgeZ2min, 4, 1, 1, 1);

        wedgeZ2max = new Gui::QuantitySpinBox(page7_wedge);
        wedgeZ2max->setObjectName(QString::fromUtf8("wedgeZ2max"));
        wedgeZ2max->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        wedgeZ2max->setValue(8);

        gridLayout_2->addWidget(wedgeZ2max, 4, 2, 1, 1);


        gridLayout_8->addLayout(gridLayout_2, 0, 0, 1, 1);

        verticalSpacer_2 = new QSpacerItem(20, 81, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_8->addItem(verticalSpacer_2, 1, 0, 1, 1);

        widgetStack2->addWidget(page7_wedge);
        page8_helix = new QWidget();
        page8_helix->setObjectName(QString::fromUtf8("page8_helix"));
        gridLayout20 = new QGridLayout(page8_helix);
        gridLayout20->setSpacing(6);
        gridLayout20->setContentsMargins(9, 9, 9, 9);
        gridLayout20->setObjectName(QString::fromUtf8("gridLayout20"));
        spacerItem11 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout20->addItem(spacerItem11, 1, 0, 1, 1);

        gridLayout21 = new QGridLayout();
        gridLayout21->setSpacing(6);
        gridLayout21->setContentsMargins(0, 0, 0, 0);
        gridLayout21->setObjectName(QString::fromUtf8("gridLayout21"));
        label_9 = new QLabel(page8_helix);
        label_9->setObjectName(QString::fromUtf8("label_9"));

        gridLayout21->addWidget(label_9, 2, 0, 1, 1);

        label_7 = new QLabel(page8_helix);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        gridLayout21->addWidget(label_7, 0, 0, 1, 1);

        label_8 = new QLabel(page8_helix);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        gridLayout21->addWidget(label_8, 1, 0, 1, 1);

        label_20 = new QLabel(page8_helix);
        label_20->setObjectName(QString::fromUtf8("label_20"));

        gridLayout21->addWidget(label_20, 3, 0, 1, 1);

        label_15 = new QLabel(page8_helix);
        label_15->setObjectName(QString::fromUtf8("label_15"));

        gridLayout21->addWidget(label_15, 4, 0, 1, 1);

        helixLocalCS = new QComboBox(page8_helix);
        helixLocalCS->setObjectName(QString::fromUtf8("helixLocalCS"));

        gridLayout21->addWidget(helixLocalCS, 4, 1, 1, 1);

        helixAngle = new Gui::QuantitySpinBox(page8_helix);
        helixAngle->setObjectName(QString::fromUtf8("helixAngle"));
        helixAngle->setProperty("unit", QVariant(QString::fromUtf8("deg")));
        helixAngle->setValue(0);

        gridLayout21->addWidget(helixAngle, 3, 1, 1, 1);

        helixPitch = new Gui::QuantitySpinBox(page8_helix);
        helixPitch->setObjectName(QString::fromUtf8("helixPitch"));
        helixPitch->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        helixPitch->setValue(1);

        gridLayout21->addWidget(helixPitch, 0, 1, 1, 1);

        helixHeight = new Gui::QuantitySpinBox(page8_helix);
        helixHeight->setObjectName(QString::fromUtf8("helixHeight"));
        helixHeight->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        helixHeight->setValue(2);

        gridLayout21->addWidget(helixHeight, 1, 1, 1, 1);

        helixRadius = new Gui::QuantitySpinBox(page8_helix);
        helixRadius->setObjectName(QString::fromUtf8("helixRadius"));
        helixRadius->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        helixRadius->setValue(1);

        gridLayout21->addWidget(helixRadius, 2, 1, 1, 1);


        gridLayout20->addLayout(gridLayout21, 0, 0, 1, 1);

        widgetStack2->addWidget(page8_helix);
        page9_spiral = new QWidget();
        page9_spiral->setObjectName(QString::fromUtf8("page9_spiral"));
        gridLayout22 = new QGridLayout(page9_spiral);
        gridLayout22->setSpacing(6);
        gridLayout22->setContentsMargins(9, 9, 9, 9);
        gridLayout22->setObjectName(QString::fromUtf8("gridLayout22"));
        spacerItem12 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout22->addItem(spacerItem12, 1, 0, 1, 1);

        gridLayout23 = new QGridLayout();
        gridLayout23->setSpacing(6);
        gridLayout23->setContentsMargins(0, 0, 0, 0);
        gridLayout23->setObjectName(QString::fromUtf8("gridLayout23"));
        label_spiral_radius = new QLabel(page9_spiral);
        label_spiral_radius->setObjectName(QString::fromUtf8("label_spiral_radius"));

        gridLayout23->addWidget(label_spiral_radius, 2, 0, 1, 1);

        label_spiral_growth = new QLabel(page9_spiral);
        label_spiral_growth->setObjectName(QString::fromUtf8("label_spiral_growth"));

        gridLayout23->addWidget(label_spiral_growth, 0, 0, 1, 1);

        label_spiral_rotation = new QLabel(page9_spiral);
        label_spiral_rotation->setObjectName(QString::fromUtf8("label_spiral_rotation"));

        gridLayout23->addWidget(label_spiral_rotation, 1, 0, 1, 1);

        spiralGrowth = new Gui::QuantitySpinBox(page9_spiral);
        spiralGrowth->setObjectName(QString::fromUtf8("spiralGrowth"));
        spiralGrowth->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        spiralGrowth->setValue(1);

        gridLayout23->addWidget(spiralGrowth, 0, 1, 1, 1);

        spiralRotation = new QDoubleSpinBox(page9_spiral);
        spiralRotation->setObjectName(QString::fromUtf8("spiralRotation"));
        spiralRotation->setMaximum(1000);
        spiralRotation->setValue(2);

        gridLayout23->addWidget(spiralRotation, 1, 1, 1, 1);

        spiralRadius = new Gui::QuantitySpinBox(page9_spiral);
        spiralRadius->setObjectName(QString::fromUtf8("spiralRadius"));
        spiralRadius->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        spiralRadius->setValue(1);

        gridLayout23->addWidget(spiralRadius, 2, 1, 1, 1);


        gridLayout22->addLayout(gridLayout23, 0, 0, 1, 1);

        widgetStack2->addWidget(page9_spiral);
        page10_circle = new QWidget();
        page10_circle->setObjectName(QString::fromUtf8("page10_circle"));
        gridLayout_3 = new QGridLayout(page10_circle);
        gridLayout_3->setSpacing(6);
        gridLayout_3->setContentsMargins(11, 11, 11, 11);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        circleParameters = new QGridLayout();
        circleParameters->setSpacing(6);
        circleParameters->setContentsMargins(0, 0, 0, 0);
        circleParameters->setObjectName(QString::fromUtf8("circleParameters"));
        Radius = new QLabel(page10_circle);
        Radius->setObjectName(QString::fromUtf8("Radius"));

        circleParameters->addWidget(Radius, 0, 0, 1, 1);

        Angle0 = new QLabel(page10_circle);
        Angle0->setObjectName(QString::fromUtf8("Angle0"));

        circleParameters->addWidget(Angle0, 1, 0, 1, 1);

        Angle1 = new QLabel(page10_circle);
        Angle1->setObjectName(QString::fromUtf8("Angle1"));

        circleParameters->addWidget(Angle1, 2, 0, 1, 1);

        circleAngle0 = new Gui::QuantitySpinBox(page10_circle);
        circleAngle0->setObjectName(QString::fromUtf8("circleAngle0"));
        circleAngle0->setProperty("unit", QVariant(QString::fromUtf8("deg")));
        circleAngle0->setValue(0);

        circleParameters->addWidget(circleAngle0, 1, 1, 1, 1);

        circleAngle1 = new Gui::QuantitySpinBox(page10_circle);
        circleAngle1->setObjectName(QString::fromUtf8("circleAngle1"));
        circleAngle1->setProperty("unit", QVariant(QString::fromUtf8("deg")));
        circleAngle1->setValue(360);

        circleParameters->addWidget(circleAngle1, 2, 1, 1, 1);

        circleRadius = new Gui::QuantitySpinBox(page10_circle);
        circleRadius->setObjectName(QString::fromUtf8("circleRadius"));
        circleRadius->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        circleRadius->setValue(2);

        circleParameters->addWidget(circleRadius, 0, 1, 1, 1);


        gridLayout_3->addLayout(circleParameters, 0, 0, 1, 1);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        buttonCircleFromThreePoints = new QPushButton(page10_circle);
        buttonCircleFromThreePoints->setObjectName(QString::fromUtf8("buttonCircleFromThreePoints"));

        horizontalLayout->addWidget(buttonCircleFromThreePoints);


        gridLayout_3->addLayout(horizontalLayout, 1, 0, 1, 1);

        verticalSpacer = new QSpacerItem(20, 95, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_3->addItem(verticalSpacer, 2, 0, 1, 1);

        widgetStack2->addWidget(page10_circle);
        page = new QWidget();
        page->setObjectName(QString::fromUtf8("page"));
        gridLayout_11 = new QGridLayout(page);
        gridLayout_11->setSpacing(6);
        gridLayout_11->setContentsMargins(11, 11, 11, 11);
        gridLayout_11->setObjectName(QString::fromUtf8("gridLayout_11"));
        gridLayout_10 = new QGridLayout();
        gridLayout_10->setSpacing(6);
        gridLayout_10->setObjectName(QString::fromUtf8("gridLayout_10"));
        labelEllMajorRadius = new QLabel(page);
        labelEllMajorRadius->setObjectName(QString::fromUtf8("labelEllMajorRadius"));

        gridLayout_10->addWidget(labelEllMajorRadius, 0, 0, 1, 1);

        labelEllMinorRadius = new QLabel(page);
        labelEllMinorRadius->setObjectName(QString::fromUtf8("labelEllMinorRadius"));

        gridLayout_10->addWidget(labelEllMinorRadius, 1, 0, 1, 1);

        labelEllAngle1 = new QLabel(page);
        labelEllAngle1->setObjectName(QString::fromUtf8("labelEllAngle1"));

        gridLayout_10->addWidget(labelEllAngle1, 2, 0, 1, 1);

        labelEllAngle2 = new QLabel(page);
        labelEllAngle2->setObjectName(QString::fromUtf8("labelEllAngle2"));

        gridLayout_10->addWidget(labelEllAngle2, 3, 0, 1, 1);

        ellipseMajorRadius = new Gui::QuantitySpinBox(page);
        ellipseMajorRadius->setObjectName(QString::fromUtf8("ellipseMajorRadius"));
        ellipseMajorRadius->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        ellipseMajorRadius->setValue(4);

        gridLayout_10->addWidget(ellipseMajorRadius, 0, 1, 1, 1);

        ellipseMinorRadius = new Gui::QuantitySpinBox(page);
        ellipseMinorRadius->setObjectName(QString::fromUtf8("ellipseMinorRadius"));
        ellipseMinorRadius->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        ellipseMinorRadius->setValue(2);

        gridLayout_10->addWidget(ellipseMinorRadius, 1, 1, 1, 1);

        ellipseAngle0 = new Gui::QuantitySpinBox(page);
        ellipseAngle0->setObjectName(QString::fromUtf8("ellipseAngle0"));
        ellipseAngle0->setProperty("unit", QVariant(QString::fromUtf8("deg")));
        ellipseAngle0->setValue(0);

        gridLayout_10->addWidget(ellipseAngle0, 2, 1, 1, 1);

        ellipseAngle1 = new Gui::QuantitySpinBox(page);
        ellipseAngle1->setObjectName(QString::fromUtf8("ellipseAngle1"));
        ellipseAngle1->setProperty("unit", QVariant(QString::fromUtf8("deg")));
        ellipseAngle1->setValue(360);

        gridLayout_10->addWidget(ellipseAngle1, 3, 1, 1, 1);


        gridLayout_11->addLayout(gridLayout_10, 0, 0, 1, 1);

        verticalSpacer_5 = new QSpacerItem(20, 131, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_11->addItem(verticalSpacer_5, 1, 0, 1, 1);

        widgetStack2->addWidget(page);
        page11_vertex = new QWidget();
        page11_vertex->setObjectName(QString::fromUtf8("page11_vertex"));
        gridLayout_9 = new QGridLayout(page11_vertex);
        gridLayout_9->setSpacing(6);
        gridLayout_9->setContentsMargins(11, 11, 11, 11);
        gridLayout_9->setObjectName(QString::fromUtf8("gridLayout_9"));
        gridLayout_4 = new QGridLayout();
        gridLayout_4->setSpacing(6);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        label_X_Axis = new QLabel(page11_vertex);
        label_X_Axis->setObjectName(QString::fromUtf8("label_X_Axis"));
        label_X_Axis->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        gridLayout_4->addWidget(label_X_Axis, 0, 0, 1, 1);

        label_Y_Axis = new QLabel(page11_vertex);
        label_Y_Axis->setObjectName(QString::fromUtf8("label_Y_Axis"));
        label_Y_Axis->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        gridLayout_4->addWidget(label_Y_Axis, 1, 0, 1, 1);

        label_Z_Axis = new QLabel(page11_vertex);
        label_Z_Axis->setObjectName(QString::fromUtf8("label_Z_Axis"));
        label_Z_Axis->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        gridLayout_4->addWidget(label_Z_Axis, 2, 0, 1, 1);

        vertexX = new Gui::QuantitySpinBox(page11_vertex);
        vertexX->setObjectName(QString::fromUtf8("vertexX"));
        vertexX->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        vertexX->setValue(0);

        gridLayout_4->addWidget(vertexX, 0, 1, 1, 1);

        vertexY = new Gui::QuantitySpinBox(page11_vertex);
        vertexY->setObjectName(QString::fromUtf8("vertexY"));
        vertexY->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        vertexY->setValue(0);

        gridLayout_4->addWidget(vertexY, 1, 1, 1, 1);

        vertexZ = new Gui::QuantitySpinBox(page11_vertex);
        vertexZ->setObjectName(QString::fromUtf8("vertexZ"));
        vertexZ->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        vertexZ->setValue(0);

        gridLayout_4->addWidget(vertexZ, 2, 1, 1, 1);


        gridLayout_9->addLayout(gridLayout_4, 0, 0, 1, 1);

        verticalSpacer_3 = new QSpacerItem(20, 139, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_9->addItem(verticalSpacer_3, 1, 0, 1, 1);

        widgetStack2->addWidget(page11_vertex);
        page12_edge = new QWidget();
        page12_edge->setObjectName(QString::fromUtf8("page12_edge"));
        gridLayout_6 = new QGridLayout(page12_edge);
        gridLayout_6->setSpacing(6);
        gridLayout_6->setContentsMargins(11, 11, 11, 11);
        gridLayout_6->setObjectName(QString::fromUtf8("gridLayout_6"));
        gridLayout_5 = new QGridLayout();
        gridLayout_5->setSpacing(6);
        gridLayout_5->setObjectName(QString::fromUtf8("gridLayout_5"));
        X1 = new QLabel(page12_edge);
        X1->setObjectName(QString::fromUtf8("X1"));
        X1->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        gridLayout_5->addWidget(X1, 1, 0, 1, 1);

        Y1 = new QLabel(page12_edge);
        Y1->setObjectName(QString::fromUtf8("Y1"));
        Y1->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        gridLayout_5->addWidget(Y1, 2, 0, 1, 1);

        Z1 = new QLabel(page12_edge);
        Z1->setObjectName(QString::fromUtf8("Z1"));
        Z1->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        gridLayout_5->addWidget(Z1, 3, 0, 1, 1);

        line_6 = new QFrame(page12_edge);
        line_6->setObjectName(QString::fromUtf8("line_6"));
        line_6->setFrameShape(QFrame::HLine);
        line_6->setFrameShadow(QFrame::Sunken);

        gridLayout_5->addWidget(line_6, 4, 0, 1, 1);

        Finish_Vertex = new QLabel(page12_edge);
        Finish_Vertex->setObjectName(QString::fromUtf8("Finish_Vertex"));
        Finish_Vertex->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        gridLayout_5->addWidget(Finish_Vertex, 5, 0, 1, 1);

        Start_Vertex = new QLabel(page12_edge);
        Start_Vertex->setObjectName(QString::fromUtf8("Start_Vertex"));

        gridLayout_5->addWidget(Start_Vertex, 0, 0, 1, 1);

        X2 = new QLabel(page12_edge);
        X2->setObjectName(QString::fromUtf8("X2"));
        X2->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        gridLayout_5->addWidget(X2, 6, 0, 1, 1);

        Y2 = new QLabel(page12_edge);
        Y2->setObjectName(QString::fromUtf8("Y2"));
        Y2->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        gridLayout_5->addWidget(Y2, 7, 0, 1, 1);

        Z2 = new QLabel(page12_edge);
        Z2->setObjectName(QString::fromUtf8("Z2"));
        Z2->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        gridLayout_5->addWidget(Z2, 8, 0, 1, 1);

        edgeX1 = new Gui::QuantitySpinBox(page12_edge);
        edgeX1->setObjectName(QString::fromUtf8("edgeX1"));
        edgeX1->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        edgeX1->setValue(0);

        gridLayout_5->addWidget(edgeX1, 1, 1, 1, 1);

        edgeY1 = new Gui::QuantitySpinBox(page12_edge);
        edgeY1->setObjectName(QString::fromUtf8("edgeY1"));
        edgeY1->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        edgeY1->setValue(0);

        gridLayout_5->addWidget(edgeY1, 2, 1, 1, 1);

        edgeZ1 = new Gui::QuantitySpinBox(page12_edge);
        edgeZ1->setObjectName(QString::fromUtf8("edgeZ1"));
        edgeZ1->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        edgeZ1->setValue(0);

        gridLayout_5->addWidget(edgeZ1, 3, 1, 1, 1);

        edgeX2 = new Gui::QuantitySpinBox(page12_edge);
        edgeX2->setObjectName(QString::fromUtf8("edgeX2"));
        edgeX2->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        edgeX2->setValue(10);

        gridLayout_5->addWidget(edgeX2, 6, 1, 1, 1);

        edgeY2 = new Gui::QuantitySpinBox(page12_edge);
        edgeY2->setObjectName(QString::fromUtf8("edgeY2"));
        edgeY2->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        edgeY2->setValue(10);

        gridLayout_5->addWidget(edgeY2, 7, 1, 1, 1);

        edgeZ2 = new Gui::QuantitySpinBox(page12_edge);
        edgeZ2->setObjectName(QString::fromUtf8("edgeZ2"));
        edgeZ2->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        edgeZ2->setValue(10);

        gridLayout_5->addWidget(edgeZ2, 8, 1, 1, 1);


        gridLayout_6->addLayout(gridLayout_5, 0, 0, 1, 1);

        verticalSpacer_4 = new QSpacerItem(20, 0, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_6->addItem(verticalSpacer_4, 1, 0, 1, 1);

        widgetStack2->addWidget(page12_edge);
        page_regularPolygon = new QWidget();
        page_regularPolygon->setObjectName(QString::fromUtf8("page_regularPolygon"));
        gridLayout24 = new QGridLayout(page_regularPolygon);
        gridLayout24->setSpacing(6);
        gridLayout24->setContentsMargins(9, 9, 9, 9);
        gridLayout24->setObjectName(QString::fromUtf8("gridLayout24"));
        gridLayout25 = new QGridLayout();
        gridLayout25->setSpacing(6);
        gridLayout25->setContentsMargins(0, 0, 0, 0);
        gridLayout25->setObjectName(QString::fromUtf8("gridLayout25"));
        labelRegularPolygonPolygon = new QLabel(page_regularPolygon);
        labelRegularPolygonPolygon->setObjectName(QString::fromUtf8("labelRegularPolygonPolygon"));

        gridLayout25->addWidget(labelRegularPolygonPolygon, 0, 0, 1, 1);

        regularPolygonPolygon = new QSpinBox(page_regularPolygon);
        regularPolygonPolygon->setObjectName(QString::fromUtf8("regularPolygonPolygon"));
        regularPolygonPolygon->setMinimum(3);
        regularPolygonPolygon->setMaximum(1000);
        regularPolygonPolygon->setValue(6);

        gridLayout25->addWidget(regularPolygonPolygon, 0, 1, 1, 1);

        labelRegularPolygonCircumradius = new QLabel(page_regularPolygon);
        labelRegularPolygonCircumradius->setObjectName(QString::fromUtf8("labelRegularPolygonCircumradius"));

        gridLayout25->addWidget(labelRegularPolygonCircumradius, 1, 0, 1, 1);

        regularPolygonCircumradius = new Gui::QuantitySpinBox(page_regularPolygon);
        regularPolygonCircumradius->setObjectName(QString::fromUtf8("regularPolygonCircumradius"));
        regularPolygonCircumradius->setProperty("unit", QVariant(QString::fromUtf8("mm")));
        regularPolygonCircumradius->setValue(2);

        gridLayout25->addWidget(regularPolygonCircumradius, 1, 1, 1, 1);


        gridLayout24->addLayout(gridLayout25, 0, 0, 1, 1);

        spacerItem13 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout24->addItem(spacerItem13, 1, 0, 1, 1);

        widgetStack2->addWidget(page_regularPolygon);

        gridLayout1->addWidget(widgetStack2, 1, 0, 1, 1);


        gridLayout->addWidget(groupBox_2, 1, 0, 1, 1);

        QWidget::setTabOrder(comboBox1, planeLength);
        QWidget::setTabOrder(planeLength, planeWidth);
        QWidget::setTabOrder(planeWidth, boxLength);
        QWidget::setTabOrder(boxLength, boxWidth);
        QWidget::setTabOrder(boxWidth, boxHeight);
        QWidget::setTabOrder(boxHeight, cylinderRadius);
        QWidget::setTabOrder(cylinderRadius, cylinderHeight);
        QWidget::setTabOrder(cylinderHeight, cylinderAngle);
        QWidget::setTabOrder(cylinderAngle, coneRadius1);
        QWidget::setTabOrder(coneRadius1, coneRadius2);
        QWidget::setTabOrder(coneRadius2, coneHeight);
        QWidget::setTabOrder(coneHeight, coneAngle);
        QWidget::setTabOrder(coneAngle, sphereRadius);
        QWidget::setTabOrder(sphereRadius, sphereAngle3);
        QWidget::setTabOrder(sphereAngle3, sphereAngle1);
        QWidget::setTabOrder(sphereAngle1, sphereAngle2);
        QWidget::setTabOrder(sphereAngle2, ellipsoidRadius1);
        QWidget::setTabOrder(ellipsoidRadius1, ellipsoidRadius2);
        QWidget::setTabOrder(ellipsoidRadius2, ellipsoidRadius3);
        QWidget::setTabOrder(ellipsoidRadius3, ellipsoidAngle3);
        QWidget::setTabOrder(ellipsoidAngle3, ellipsoidAngle1);
        QWidget::setTabOrder(ellipsoidAngle1, ellipsoidAngle2);
        QWidget::setTabOrder(ellipsoidAngle2, torusRadius1);
        QWidget::setTabOrder(torusRadius1, torusRadius2);
        QWidget::setTabOrder(torusRadius2, torusAngle3);
        QWidget::setTabOrder(torusAngle3, torusAngle1);
        QWidget::setTabOrder(torusAngle1, torusAngle2);
        QWidget::setTabOrder(torusAngle2, prismPolygon);
        QWidget::setTabOrder(prismPolygon, prismCircumradius);
        QWidget::setTabOrder(prismCircumradius, prismHeight);
        QWidget::setTabOrder(prismHeight, wedgeXmin);
        QWidget::setTabOrder(wedgeXmin, wedgeXmax);
        QWidget::setTabOrder(wedgeXmax, wedgeYmin);
        QWidget::setTabOrder(wedgeYmin, wedgeYmax);
        QWidget::setTabOrder(wedgeYmax, wedgeZmin);
        QWidget::setTabOrder(wedgeZmin, wedgeZmax);
        QWidget::setTabOrder(wedgeZmax, wedgeX2min);
        QWidget::setTabOrder(wedgeX2min, wedgeX2max);
        QWidget::setTabOrder(wedgeX2max, wedgeZ2min);
        QWidget::setTabOrder(wedgeZ2min, wedgeZ2max);
        QWidget::setTabOrder(wedgeZ2max, helixPitch);
        QWidget::setTabOrder(helixPitch, helixHeight);
        QWidget::setTabOrder(helixHeight, helixRadius);
        QWidget::setTabOrder(helixRadius, helixAngle);
        QWidget::setTabOrder(helixAngle, helixLocalCS);
        QWidget::setTabOrder(helixLocalCS, spiralGrowth);
        QWidget::setTabOrder(spiralGrowth, spiralRotation);
        QWidget::setTabOrder(spiralRotation, spiralRadius);
        QWidget::setTabOrder(spiralRadius, circleRadius);
        QWidget::setTabOrder(circleRadius, circleAngle0);
        QWidget::setTabOrder(circleAngle0, circleAngle1);
        QWidget::setTabOrder(circleAngle1, buttonCircleFromThreePoints);
        QWidget::setTabOrder(buttonCircleFromThreePoints, ellipseMajorRadius);
        QWidget::setTabOrder(ellipseMajorRadius, ellipseMinorRadius);
        QWidget::setTabOrder(ellipseMinorRadius, ellipseAngle0);
        QWidget::setTabOrder(ellipseAngle0, ellipseAngle1);
        QWidget::setTabOrder(ellipseAngle1, vertexX);
        QWidget::setTabOrder(vertexX, vertexY);
        QWidget::setTabOrder(vertexY, vertexZ);
        QWidget::setTabOrder(vertexZ, edgeX1);
        QWidget::setTabOrder(edgeX1, edgeY1);
        QWidget::setTabOrder(edgeY1, edgeZ1);
        QWidget::setTabOrder(edgeZ1, edgeX2);
        QWidget::setTabOrder(edgeX2, edgeY2);
        QWidget::setTabOrder(edgeY2, edgeZ2);
        QWidget::setTabOrder(edgeZ2, regularPolygonPolygon);
        QWidget::setTabOrder(regularPolygonPolygon, regularPolygonCircumradius);

        retranslateUi(PartGui__DlgPrimitives);
        QObject::connect(comboBox1, SIGNAL(activated(int)), widgetStack2, SLOT(setCurrentIndex(int)));

        widgetStack2->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(PartGui__DlgPrimitives);
    } // setupUi

    void retranslateUi(QWidget *PartGui__DlgPrimitives)
    {
        PartGui__DlgPrimitives->setWindowTitle(QApplication::translate("PartGui::DlgPrimitives", "Geometric Primitives", 0, QApplication::UnicodeUTF8));
        comboBox1->setItemText(0, QApplication::translate("PartGui::DlgPrimitives", "Plane", 0, QApplication::UnicodeUTF8));
        comboBox1->setItemText(1, QApplication::translate("PartGui::DlgPrimitives", "Box", 0, QApplication::UnicodeUTF8));
        comboBox1->setItemText(2, QApplication::translate("PartGui::DlgPrimitives", "Cylinder", 0, QApplication::UnicodeUTF8));
        comboBox1->setItemText(3, QApplication::translate("PartGui::DlgPrimitives", "Cone", 0, QApplication::UnicodeUTF8));
        comboBox1->setItemText(4, QApplication::translate("PartGui::DlgPrimitives", "Sphere", 0, QApplication::UnicodeUTF8));
        comboBox1->setItemText(5, QApplication::translate("PartGui::DlgPrimitives", "Ellipsoid", 0, QApplication::UnicodeUTF8));
        comboBox1->setItemText(6, QApplication::translate("PartGui::DlgPrimitives", "Torus", 0, QApplication::UnicodeUTF8));
        comboBox1->setItemText(7, QApplication::translate("PartGui::DlgPrimitives", "Prism", 0, QApplication::UnicodeUTF8));
        comboBox1->setItemText(8, QApplication::translate("PartGui::DlgPrimitives", "Wedge", 0, QApplication::UnicodeUTF8));
        comboBox1->setItemText(9, QApplication::translate("PartGui::DlgPrimitives", "Helix", 0, QApplication::UnicodeUTF8));
        comboBox1->setItemText(10, QApplication::translate("PartGui::DlgPrimitives", "Spiral", 0, QApplication::UnicodeUTF8));
        comboBox1->setItemText(11, QApplication::translate("PartGui::DlgPrimitives", "Circle", 0, QApplication::UnicodeUTF8));
        comboBox1->setItemText(12, QApplication::translate("PartGui::DlgPrimitives", "Ellipse", 0, QApplication::UnicodeUTF8));
        comboBox1->setItemText(13, QApplication::translate("PartGui::DlgPrimitives", "Point", 0, QApplication::UnicodeUTF8));
        comboBox1->setItemText(14, QApplication::translate("PartGui::DlgPrimitives", "Line", 0, QApplication::UnicodeUTF8));
        comboBox1->setItemText(15, QApplication::translate("PartGui::DlgPrimitives", "Regular polygon", 0, QApplication::UnicodeUTF8));

        groupBox_2->setTitle(QApplication::translate("PartGui::DlgPrimitives", "Parameter", 0, QApplication::UnicodeUTF8));
        textLabel3_2->setText(QApplication::translate("PartGui::DlgPrimitives", "Width:", 0, QApplication::UnicodeUTF8));
        textLabel2_2->setText(QApplication::translate("PartGui::DlgPrimitives", "Length:", 0, QApplication::UnicodeUTF8));
        textLabel4->setText(QApplication::translate("PartGui::DlgPrimitives", "Height:", 0, QApplication::UnicodeUTF8));
        textLabel2->setText(QApplication::translate("PartGui::DlgPrimitives", "Length:", 0, QApplication::UnicodeUTF8));
        textLabel3->setText(QApplication::translate("PartGui::DlgPrimitives", "Width:", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("PartGui::DlgPrimitives", "Angle:", 0, QApplication::UnicodeUTF8));
        textLabel5->setText(QApplication::translate("PartGui::DlgPrimitives", "Radius:", 0, QApplication::UnicodeUTF8));
        textLabel6->setText(QApplication::translate("PartGui::DlgPrimitives", "Height:", 0, QApplication::UnicodeUTF8));
        label_4->setText(QApplication::translate("PartGui::DlgPrimitives", "Angle:", 0, QApplication::UnicodeUTF8));
        textLabel11->setText(QApplication::translate("PartGui::DlgPrimitives", "Height:", 0, QApplication::UnicodeUTF8));
        textLabel9->setText(QApplication::translate("PartGui::DlgPrimitives", "Radius 1:", 0, QApplication::UnicodeUTF8));
        textLabel10->setText(QApplication::translate("PartGui::DlgPrimitives", "Radius 2:", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("PartGui::DlgPrimitives", "U parameter:", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("PartGui::DlgPrimitives", "V parameters:", 0, QApplication::UnicodeUTF8));
        textLabel14->setText(QApplication::translate("PartGui::DlgPrimitives", "Radius:", 0, QApplication::UnicodeUTF8));
        textLabel21->setText(QApplication::translate("PartGui::DlgPrimitives", "Radius 1:", 0, QApplication::UnicodeUTF8));
        textLabel22->setText(QApplication::translate("PartGui::DlgPrimitives", "Radius 2:", 0, QApplication::UnicodeUTF8));
        textLabel23->setText(QApplication::translate("PartGui::DlgPrimitives", "Radius 3:", 0, QApplication::UnicodeUTF8));
        label23->setText(QApplication::translate("PartGui::DlgPrimitives", "U parameter:", 0, QApplication::UnicodeUTF8));
        label24->setText(QApplication::translate("PartGui::DlgPrimitives", "V parameter:", 0, QApplication::UnicodeUTF8));
        label_5->setText(QApplication::translate("PartGui::DlgPrimitives", "U Parameter:", 0, QApplication::UnicodeUTF8));
        label_6->setText(QApplication::translate("PartGui::DlgPrimitives", "V parameter:", 0, QApplication::UnicodeUTF8));
        textLabel20->setText(QApplication::translate("PartGui::DlgPrimitives", "Radius 2:", 0, QApplication::UnicodeUTF8));
        textLabel19->setText(QApplication::translate("PartGui::DlgPrimitives", "Radius 1:", 0, QApplication::UnicodeUTF8));
        labelPrismPolygon->setText(QApplication::translate("PartGui::DlgPrimitives", "Polygon:", 0, QApplication::UnicodeUTF8));
        labelPrismCircumradius->setText(QApplication::translate("PartGui::DlgPrimitives", "Circumradius:", 0, QApplication::UnicodeUTF8));
        labelPrismHeight->setText(QApplication::translate("PartGui::DlgPrimitives", "Height:", 0, QApplication::UnicodeUTF8));
        label_10->setText(QApplication::translate("PartGui::DlgPrimitives", "X min/max:", 0, QApplication::UnicodeUTF8));
        label_11->setText(QApplication::translate("PartGui::DlgPrimitives", "Y min/max:", 0, QApplication::UnicodeUTF8));
        label_12->setText(QApplication::translate("PartGui::DlgPrimitives", "Z min/max:", 0, QApplication::UnicodeUTF8));
        label_13->setText(QApplication::translate("PartGui::DlgPrimitives", "X2 min/max:", 0, QApplication::UnicodeUTF8));
        label_14->setText(QApplication::translate("PartGui::DlgPrimitives", "Z2 min/max:", 0, QApplication::UnicodeUTF8));
        label_9->setText(QApplication::translate("PartGui::DlgPrimitives", "Radius:", 0, QApplication::UnicodeUTF8));
        label_7->setText(QApplication::translate("PartGui::DlgPrimitives", "Pitch:", 0, QApplication::UnicodeUTF8));
        label_8->setText(QApplication::translate("PartGui::DlgPrimitives", "Height:", 0, QApplication::UnicodeUTF8));
        label_20->setText(QApplication::translate("PartGui::DlgPrimitives", "Angle:", 0, QApplication::UnicodeUTF8));
        label_15->setText(QApplication::translate("PartGui::DlgPrimitives", "Coordinate system:", 0, QApplication::UnicodeUTF8));
        helixLocalCS->clear();
        helixLocalCS->insertItems(0, QStringList()
         << QApplication::translate("PartGui::DlgPrimitives", "Right-handed", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("PartGui::DlgPrimitives", "Left-handed", 0, QApplication::UnicodeUTF8)
        );
        label_spiral_radius->setText(QApplication::translate("PartGui::DlgPrimitives", "Radius:", 0, QApplication::UnicodeUTF8));
        label_spiral_growth->setText(QApplication::translate("PartGui::DlgPrimitives", "Growth:", 0, QApplication::UnicodeUTF8));
        label_spiral_rotation->setText(QApplication::translate("PartGui::DlgPrimitives", "Number of rotations:", 0, QApplication::UnicodeUTF8));
        Radius->setText(QApplication::translate("PartGui::DlgPrimitives", "Radius:", 0, QApplication::UnicodeUTF8));
        Angle0->setText(QApplication::translate("PartGui::DlgPrimitives", "Angle 1:", 0, QApplication::UnicodeUTF8));
        Angle1->setText(QApplication::translate("PartGui::DlgPrimitives", "Angle 2:", 0, QApplication::UnicodeUTF8));
        buttonCircleFromThreePoints->setText(QApplication::translate("PartGui::DlgPrimitives", "From three points", 0, QApplication::UnicodeUTF8));
        labelEllMajorRadius->setText(QApplication::translate("PartGui::DlgPrimitives", "Major radius:", 0, QApplication::UnicodeUTF8));
        labelEllMinorRadius->setText(QApplication::translate("PartGui::DlgPrimitives", "Minor radius:", 0, QApplication::UnicodeUTF8));
        labelEllAngle1->setText(QApplication::translate("PartGui::DlgPrimitives", "Angle 1:", 0, QApplication::UnicodeUTF8));
        labelEllAngle2->setText(QApplication::translate("PartGui::DlgPrimitives", "Angle 2:", 0, QApplication::UnicodeUTF8));
        label_X_Axis->setText(QApplication::translate("PartGui::DlgPrimitives", "X:", 0, QApplication::UnicodeUTF8));
        label_Y_Axis->setText(QApplication::translate("PartGui::DlgPrimitives", "Y:", 0, QApplication::UnicodeUTF8));
        label_Z_Axis->setText(QApplication::translate("PartGui::DlgPrimitives", "Z:", 0, QApplication::UnicodeUTF8));
        X1->setText(QApplication::translate("PartGui::DlgPrimitives", "X:", 0, QApplication::UnicodeUTF8));
        Y1->setText(QApplication::translate("PartGui::DlgPrimitives", "Y:", 0, QApplication::UnicodeUTF8));
        Z1->setText(QApplication::translate("PartGui::DlgPrimitives", "Z:", 0, QApplication::UnicodeUTF8));
        Finish_Vertex->setText(QApplication::translate("PartGui::DlgPrimitives", "End point", 0, QApplication::UnicodeUTF8));
        Start_Vertex->setText(QApplication::translate("PartGui::DlgPrimitives", "Start point", 0, QApplication::UnicodeUTF8));
        X2->setText(QApplication::translate("PartGui::DlgPrimitives", "X:", 0, QApplication::UnicodeUTF8));
        Y2->setText(QApplication::translate("PartGui::DlgPrimitives", "Y:", 0, QApplication::UnicodeUTF8));
        Z2->setText(QApplication::translate("PartGui::DlgPrimitives", "Z:", 0, QApplication::UnicodeUTF8));
        labelRegularPolygonPolygon->setText(QApplication::translate("PartGui::DlgPrimitives", "Polygon:", 0, QApplication::UnicodeUTF8));
        labelRegularPolygonCircumradius->setText(QApplication::translate("PartGui::DlgPrimitives", "Circumradius:", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

} // namespace PartGui

namespace PartGui {
namespace Ui {
    class DlgPrimitives: public Ui_DlgPrimitives {};
} // namespace Ui
} // namespace PartGui

#endif // UI_DLGPRIMITIVES_H
